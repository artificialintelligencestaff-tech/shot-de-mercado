#!/usr/bin/env python3
"""
script_46b_early_filtered.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Deteccion temprana CON FILTROS DUROS. Solo tokens que
    pasan filtros llegan al scoring. Resto se descartan.
    Ventana ampliada: 90 min a 8h.
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

# FILTROS DUROS
MIN_LIQUIDITY_USD = 20000
MIN_MARKET_CAP_USD = 50000
MAX_TOP10_PCT = 40
MIN_AGE_MIN = 90
MAX_AGE_MIN = 480  # 8 horas


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
    """Extrae metricas del texto de analyze_token."""
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

    # Liquidez (formato "$3.4K" o "$1.5M")
    m = re.search(r'\$(\d+\.?\d*)\s*([kmKM])?\s*liquidity', t)
    if m:
        val = float(m.group(1))
        suffix = m.group(2)
        if suffix and suffix.lower() == 'k': val *= 1000
        elif suffix and suffix.lower() == 'm': val *= 1000000
        metrics["liquidity_usd"] = val

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

    # Detectar dumping
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


def aplicar_filtros(metrics):
    """Aplica filtros duros. Si falla 1, score = 0."""
    razones = []

    if metrics["liquidity_usd"] < MIN_LIQUIDITY_USD:
        razones.append(f"Liquidez ${metrics['liquidity_usd']:.0f} < ${MIN_LIQUIDITY_USD}")
    if metrics["market_cap_usd"] < MIN_MARKET_CAP_USD:
        razones.append(f"MCap ${metrics['market_cap_usd']:.0f} < ${MIN_MARKET_CAP_USD}")
    if metrics["top10_pct"] > MAX_TOP10_PCT:
        razones.append(f"Top 10 = {metrics['top10_pct']:.1f}% > {MAX_TOP10_PCT}%")
    if metrics["age_min"] < MIN_AGE_MIN:
        razones.append(f"Edad {metrics['age_min']}min < {MIN_AGE_MIN}min")
    if metrics["age_min"] > MAX_AGE_MIN:
        razones.append(f"Edad {metrics['age_min']}min > {MAX_AGE_MIN}min")
    if metrics["is_dead"]:
        razones.append("Token DEAD ($0 liquidez)")
    if metrics["is_dumping"]:
        razones.append("Token dumping")
    if metrics["verdict"] in ["DEAD", "SELL", "CAUTION"]:
        razones.append(f"Verdict {metrics['verdict']}")

    if razones:
        return False, razones
    return True, []


def calcular_score(metrics):
    """Score ponderado para tokens que pasaron filtros."""
    score = 0

    # Distribucion (25 pts)
    if metrics["top10_pct"] < 15: score += 25
    elif metrics["top10_pct"] < 25: score += 18
    elif metrics["top10_pct"] < 40: score += 10

    # Liquidez (20 pts)
    if metrics["liquidity_usd"] > 100000: score += 20
    elif metrics["liquidity_usd"] > 50000: score += 15
    elif metrics["liquidity_usd"] > 20000: score += 10

    # MCap (20 pts)
    if metrics["market_cap_usd"] > 500000: score += 20
    elif metrics["market_cap_usd"] > 200000: score += 15
    elif metrics["market_cap_usd"] > 50000: score += 10

    # Buy pressure (20 pts)
    if metrics["buy_pressure"] > 10: score += 20
    elif metrics["buy_pressure"] > 5: score += 15
    elif metrics["buy_pressure"] > 2: score += 8

    # Age (15 pts)
    if 120 <= metrics["age_min"] <= 360: score += 15
    elif 90 <= metrics["age_min"] < 120: score += 10
    elif 360 < metrics["age_min"] <= 480: score += 8

    return min(score, 100)


async def main_async():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Early Filtered - {ts}")

    print("[YIN] Consultando get_new_launches...")
    launches = await get_new_launches()
    texto = extraer_texto(launches)

    # Extraer direcciones
    tokens = []
    for match in re.finditer(r'([1-9A-HJ-NP-Za-km-z]{32,44}pump)', texto):
        addr = match.group(1)
        if addr not in tokens:
            tokens.append(addr)

    print(f"[YIN] Tokens unicos: {len(tokens)}")

    resultados = []
    descartados = []

    for i, addr in enumerate(tokens[:12], 1):
        print(f"[YIN] [{i}/{min(len(tokens), 12)}] {addr[:20]}...")
        r = await deep_check(addr)
        metrics = extraer_metricas(r.get("texto", ""))
        r["metrics"] = metrics

        pasa, razones = aplicar_filtros(metrics)
        if pasa:
            r["score"] = calcular_score(metrics)
            r["confianza"] = min(95, int(r["score"] * 0.95))
            r["status"] = "PASA_FILTROS"
            resultados.append(r)
            print(f"[YIN]   ✓ PASA | Score {r['score']}")
        else:
            r["status"] = "DESCARTADO"
            r["razones_descarte"] = razones
            descartados.append(r)
            print(f"[YIN]   ✗ DESCARTADO: {razones[0][:50]}")

    resultados.sort(key=lambda x: x["score"], reverse=True)

    out = {
        "timestamp": ts,
        "fase": "early_filtered",
        "total_tokens": len(tokens),
        "total_pasaron": len(resultados),
        "total_descartados": len(descartados),
        "pasan_filtros": resultados,
        "descartados": descartados
    }

    out_path = DETECTION_DIR / f"early_filtered_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[YIN] Guardado: {out_path}")
    print(f"[YIN] Pasaron filtros: {len(resultados)}/{len(tokens)}")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()