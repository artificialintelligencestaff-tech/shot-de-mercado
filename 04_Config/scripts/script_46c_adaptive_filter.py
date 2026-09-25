#!/usr/bin/env python3
"""
script_46c_adaptive_filter.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Filtros adaptativos: la edad NO descarta, solo penaliza.
    Solo se descarta por fallas CRITICAS de calidad:
    - Liquidez < $15K
    - MCap < $30K
    - Top 10 > 45%
    - Token DEAD o dumping severo

    La edad se convierte en penalizacion gradual.
"""

import asyncio
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
DETECTION_DIR = PROJECT_ROOT / "02_Analisis" / "early_detection"
DETECTION_DIR.mkdir(parents=True, exist_ok=True)

# FILTROS CRITICOS (solo estos descartan)
MIN_LIQUIDITY_HARD = 15000
MIN_MARKET_CAP_HARD = 30000
MAX_TOP10_HARD = 45

# VENTANA AMPLIADA
MIN_AGE_MIN = 20
MAX_AGE_MIN = 720  # 12 horas


def serialize_result(result):
    if result is None:
        return None
    if isinstance(result, (str, int, float, bool, list, dict)):
        return result
    if hasattr(result, "model_dump"):
        try:
            return result.model_dump()
        except Exception:
            pass
    out = {"isError": getattr(result, "isError", False), "content": []}
    content = getattr(result, "content", None)
    if content:
        for item in content:
            if hasattr(item, "text"):
                out["content"].append({"type": "text", "text": item.text})
    return out


def extraer_texto(data):
    if not isinstance(data, dict):
        return str(data)
    texto = ""
    for item in data.get("content", []):
        if isinstance(item, dict) and item.get("type") == "text":
            texto += item.get("text", "") + "\n"
    return texto


async def get_new_launches():
    transport = StdioTransport(command="npx", args=["@0xprotovox/deficlaw"])
    async with Client(transport) as client:
        raw = await asyncio.wait_for(
            client.call_tool("get_new_launches", {}),
            timeout=45
        )
        return serialize_result(raw)


async def deep_check(address):
    result = {"address": address, "texto": "", "error": None}
    try:
        transport = StdioTransport(command="npx", args=["@0xprotovox/deficlaw"])
        async with Client(transport) as client:
            try:
                raw = await asyncio.wait_for(
                    client.call_tool("analyze_token", {"address": address}),
                    timeout=40
                )
                result["analyze"] = serialize_result(raw)
                result["texto"] = extraer_texto(result["analyze"])[:800]
            except Exception as e:
                result["error"] = f"analyze: {str(e)[:100]}"
    except Exception as e:
        result["error"] = str(e)[:150]
    return result


def extraer_metricas(texto):
    t = texto.lower()
    metrics = {
        "liquidity_usd": 0,
        "market_cap_usd": 0,
        "top10_pct": 0,
        "buy_pressure": 0,
        "age_min": 0,
        "is_dead": False,
        "is_dumping": False,
        "verdict": "UNKNOWN"
    }

    # Liquidez
    for pattern in [r'\$(\d+\.?\d*)\s*([kmKM])?\s*liquidity', r'liquidity[:\s]+\$(\d+\.?\d*)\s*([kmKM])?']:
        m = re.search(pattern, t)
        if m:
            val = float(m.group(1))
            suffix = m.group(2) if len(m.groups()) > 1 else None
            if suffix and suffix.lower() == 'k': val *= 1000
            elif suffix and suffix.lower() == 'm': val *= 1000000
            metrics["liquidity_usd"] = val
            break

    # Market cap
    m = re.search(r'\$(\d+\.?\d*)\s*([kmKM])?\s*market cap', t)
    if m:
        val = float(m.group(1))
        suffix = m.group(2)
        if suffix and suffix.lower() == 'k': val *= 1000
        elif suffix and suffix.lower() == 'm': val *= 1000000
        metrics["market_cap_usd"] = val

    # Top 10
    m = re.search(r'top\s*10[^\d]*(\d+\.?\d*)%', t)
    if m:
        metrics["top10_pct"] = float(m.group(1))

    # Buy pressure
    m = re.search(r'buy pressure[:\s]+(\d+\.?\d*)', t)
    if m:
        metrics["buy_pressure"] = float(m.group(1))

    # Edad
    m = re.search(r'(\d+)\s*(m|min|minutes?)\s*old', t)
    if m:
        metrics["age_min"] = int(m.group(1))

    # Detectar dead
    if "$0 liquidity" in t or "liquidity and $0 market cap" in t:
        metrics["is_dead"] = True

    # Detectar dumping severo
    if "dumping" in t or "-88%" in t or "-94%" in t or "-49%" in t or "-48%" in t:
        metrics["is_dumping"] = True

    # Verdict
    if "dead" in t: metrics["verdict"] = "DEAD"
    elif "strong buy" in t: metrics["verdict"] = "STRONG_BUY"
    elif "buy signal" in t: metrics["verdict"] = "BUY"
    elif "neutral" in t: metrics["verdict"] = "NEUTRAL"
    elif "caution" in t: metrics["verdict"] = "CAUTION"
    elif "sell" in t: metrics["verdict"] = "SELL"

    return metrics


def aplicar_filtros_criticos(metrics):
    """Solo descarta por fallas criticas de calidad."""
    razones = []

    if metrics["liquidity_usd"] < MIN_LIQUIDITY_HARD:
        razones.append(f"Liquidez ${metrics['liquidity_usd']:.0f} < ${MIN_LIQUIDITY_HARD}")
    if metrics["market_cap_usd"] < MIN_MARKET_CAP_HARD:
        razones.append(f"MCap ${metrics['market_cap_usd']:.0f} < ${MIN_MARKET_CAP_HARD}")
    if metrics["top10_pct"] > MAX_TOP10_HARD:
        razones.append(f"Top 10 = {metrics['top10_pct']:.1f}% > {MAX_TOP10_HARD}%")
    if metrics["is_dead"]:
        razones.append("Token DEAD")
    if metrics["is_dumping"]:
        razones.append("Token dumping")
    if metrics["verdict"] in ["DEAD", "SELL"]:
        razones.append(f"Verdict {metrics['verdict']}")

    return (len(razones) == 0, razones)


def score_distribucion(top10):
    if top10 < 15: return 25
    if top10 < 25: return 18
    if top10 < 35: return 12
    if top10 < 45: return 6
    return 0


def score_liquidez(liq):
    if liq >= 100000: return 20
    if liq >= 50000: return 15
    if liq >= 30000: return 12
    if liq >= 20000: return 8
    if liq >= 15000: return 5
    return 0


def score_mcap(mcap):
    if mcap >= 500000: return 20
    if mcap >= 200000: return 15
    if mcap >= 100000: return 12
    if mcap >= 50000: return 8
    if mcap >= 30000: return 5
    return 0


def score_buy_pressure(bp):
    if bp > 10: return 15
    if bp > 5: return 12
    if bp > 2: return 8
    if bp > 1: return 4
    return 0


def score_edad(age_min):
    """Edad como bonus/penalizacion adaptativo."""
    if 120 <= age_min <= 360: return 20     # Sweet spot optimo
    if 60 <= age_min < 120: return 18       # Sweet spot inicial
    if 30 <= age_min < 60: return 15        # Alta ventaja, alto riesgo
    if 360 < age_min <= 720: return 12      # Tarde
    if 20 <= age_min < 30: return 8         # Muy temprano, muy riesgoso
    return 5                                 # Muy tarde


def calcular_score_adaptativo(metrics):
    """Score ponderado SIN descartar por edad."""
    score = 0
    score += score_distribucion(metrics["top10_pct"])   # Max 25
    score += score_liquidez(metrics["liquidity_usd"])   # Max 20
    score += score_mcap(metrics["market_cap_usd"])      # Max 20
    score += score_buy_pressure(metrics["buy_pressure"]) # Max 15
    score += score_edad(metrics["age_min"])              # Max 20
    return min(score, 100)


async def main_async():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Adaptive Filter - {ts}")

    print("[YIN] Consultando get_new_launches...")
    launches = await get_new_launches()
    texto = extraer_texto(launches)

    tokens = []
    for match in re.finditer(r'([1-9A-HJ-NP-Za-km-z]{32,44}pump)', texto):
        addr = match.group(1)
        if addr not in tokens:
            tokens.append(addr)

    print(f"[YIN] Tokens unicos: {len(tokens)}")

    resultados = []
    descartados = []

    for i, addr in enumerate(tokens[:15], 1):
        print(f"[YIN] [{i}/{min(len(tokens), 15)}] {addr[:20]}...")
        r = await deep_check(addr)
        metrics = extraer_metricas(r.get("texto", ""))
        r["metrics"] = metrics

        pasa, razones = aplicar_filtros_criticos(metrics)
        if pasa:
            r["score"] = calcular_score_adaptativo(metrics)
            r["confianza"] = min(95, int(r["score"] * 0.95))
            r["status"] = "CANDIDATO"
            resultados.append(r)
            print(f"[YIN]   ✓ CANDIDATO | Score {r['score']} | Edad {metrics['age_min']}min")
        else:
            r["status"] = "DESCARTADO"
            r["razones_descarte"] = razones
            descartados.append(r)
            print(f"[YIN]   ✗ {razones[0][:60]}")

    resultados.sort(key=lambda x: x["score"], reverse=True)

    out = {
        "timestamp": ts,
        "fase": "adaptive_filter",
        "total_tokens": len(tokens),
        "total_candidatos": len(resultados),
        "total_descartados": len(descartados),
        "candidatos": resultados,
        "descartados": descartados
    }

    out_path = DETECTION_DIR / f"adaptive_filter_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[YIN] Guardado: {out_path}")
    print(f"[YIN] Candidatos: {len(resultados)}/{len(tokens)}")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()