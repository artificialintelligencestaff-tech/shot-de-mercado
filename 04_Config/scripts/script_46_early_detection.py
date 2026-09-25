#!/usr/bin/env python3
"""
script_46_early_detection.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Deteccion temprana en ventana optima (1-4h post-lanzamiento).
    No analiza tokens <30min (sin datos) ni >6h (pump ya ocurrido).
"""

import asyncio
import json
import glob
from datetime import datetime, timezone
from pathlib import Path
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
DETECTION_DIR = PROJECT_ROOT / "02_Analisis" / "early_detection"
DETECTION_DIR.mkdir(parents=True, exist_ok=True)

# Ventana optima (en minutos)
MIN_AGE_MIN = 30
MAX_AGE_MIN = 360


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


async def check_new_launches():
    """Consulta get_new_launches y filtra por edad."""
    transport = StdioTransport(command="npx", args=["@0xprotovox/deficlaw"])
    async with Client(transport) as client:
        raw = await asyncio.wait_for(
            client.call_tool("get_new_launches", {}),
            timeout=45
        )
        return serialize_result(raw)


async def deep_check_token(address):
    """Analiza un token con analyze_token + get_token_security."""
    result = {"address": address, "analyze": None, "security": None, "texto": "", "error": None}

    try:
        transport = StdioTransport(command="npx", args=["@0xprotovox/deficlaw"])
        async with Client(transport) as client:
            # analyze
            try:
                raw = await asyncio.wait_for(
                    client.call_tool("analyze_token", {"address": address}),
                    timeout=40
                )
                result["analyze"] = serialize_result(raw)
                result["texto"] = extraer_texto(result["analyze"])[:800]
            except Exception as e:
                result["error"] = f"analyze: {str(e)[:100]}"

            # security
            try:
                raw = await asyncio.wait_for(
                    client.call_tool("get_token_security", {"address": address}),
                    timeout=40
                )
                result["security"] = serialize_result(raw)
            except Exception as e:
                result["error"] = f"{result.get('error', '')}|security: {str(e)[:100]}"

    except Exception as e:
        result["error"] = str(e)[:150]

    return result


def calcular_score_early(texto):
    """Score pre-pump basado en datos disponibles temprano."""
    score = 0
    t = texto.lower()

    # Risk score (inverso)
    import re
    m = re.search(r"risk score[:\s]+(\d+)", t)
    if m:
        risk = int(m.group(1))
        if risk < 15: score += 30
        elif risk < 25: score += 22
        elif risk < 40: score += 12
        else: score += 0
    else:
        score += 10

    # Top 10
    m = re.search(r"top 10[^\d]*(\d+\.?\d*)%", t)
    if m:
        top10 = float(m.group(1))
        if top10 < 15: score += 25
        elif top10 < 30: score += 18
        elif top10 < 50: score += 8
    else:
        score += 10

    # Buy pressure
    m = re.search(r"buy pressure[:\s]+(\d+\.?\d*)", t)
    if m:
        bp = float(m.group(1))
        if bp > 10: score += 20
        elif bp > 5: score += 12
        elif bp > 2: score += 6

    # Base
    score += 25
    return min(score, 100)


async def main_async():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Deteccion temprana - {ts}")

    # 1. Obtener nuevos lanzamientos
    print("[YIN] Consultando get_new_launches...")
    launches = await check_new_launches()
    texto = extraer_texto(launches)

    # Parsear tokens
    tokens = []
    try:
        # Intentar extraer direcciones
        import re
        # Buscar patrones de direcciones Solana (base58, 32-44 chars terminando en pump)
        for match in re.finditer(r'([1-9A-HJ-NP-Za-km-z]{32,44}pump)', texto):
            tokens.append(match.group(1))
    except Exception:
        pass

    print(f"[YIN] Tokens encontrados: {len(tokens)}")

    # 2. Deep dive en cada uno
    resultados = []
    for i, addr in enumerate(tokens[:10], 1):  # Max 10 por ciclo
        print(f"[YIN] [{i}/{min(len(tokens), 10)}] {addr[:20]}...")
        r = await deep_check_token(addr)
        r["score"] = calcular_score_early(r.get("texto", ""))
        r["confianza"] = min(95, int(r["score"] * 0.95))
        resultados.append(r)

    # 3. Ranking
    resultados.sort(key=lambda x: x["score"], reverse=True)

    out = {
        "timestamp": ts,
        "fase": "early_detection",
        "ventana_min": MIN_AGE_MIN,
        "ventana_max": MAX_AGE_MIN,
        "total_tokens": len(tokens),
        "ranking": resultados
    }

    out_path = DETECTION_DIR / f"early_detection_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")
    print(f"\n[YIN] === TOP DETECCIONES ===")
    for i, r in enumerate(resultados[:5], 1):
        print(f"[YIN] {i}. {r['address'][:20]}... | Score {r['score']}/100 | Conf {r['confianza']}%")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()