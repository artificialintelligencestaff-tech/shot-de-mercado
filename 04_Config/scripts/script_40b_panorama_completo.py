#!/usr/bin/env python3
"""
script_40b_panorama_completo.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Analiza TODOS los candidatos sin filtrar.
    Muestra todos con su score y confianza.
    NO descarta ninguno.
"""

import asyncio
import json
import glob
import re
from datetime import datetime, timezone
from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
PANORAMA_DIR = PROJECT_ROOT / "02_Analisis" / "panorama"
PANORAMA_DIR.mkdir(parents=True, exist_ok=True)

# Analizar hasta este numero (amplio)
MAX_TOKENS = 25


def leer_ultimos_candidatos():
    """Lee el archivo de candidatos mas reciente."""
    archivos = sorted(glob.glob(str(PANORAMA_DIR / "candidatos_*.json")), reverse=True)
    if not archivos:
        return None
    with open(archivos[0], "r", encoding="utf-8") as f:
        return json.load(f)


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


def texto_completo(data):
    """Extrae todo el texto de un resultado."""
    if not isinstance(data, dict):
        return str(data)
    texto = ""
    content = data.get("content", [])
    for item in content:
        if isinstance(item, dict) and item.get("type") == "text":
            texto += item.get("text", "") + "\n"
    return texto


def calcular_score(texto):
    """Calcula score 0-100 basado en criterios detectados."""
    score = 0
    criterios = {}
    t = texto.lower()

    # Risk score (inverso)
    m = re.search(r"risk score[:\s]+(\d+)", t)
    if m:
        risk = int(m.group(1))
        if risk < 15: score += 25; criterios["risk"] = 25
        elif risk < 25: score += 20; criterios["risk"] = 20
        elif risk < 40: score += 12; criterios["risk"] = 12
        elif risk < 55: score += 5; criterios["risk"] = 5
        else: criterios["risk"] = 0
    else:
        criterios["risk"] = 10; score += 10

    # Verdict
    if "strong buy" in t: score += 25; criterios["verdict"] = 25
    elif "buy signal" in t: score += 20; criterios["verdict"] = 20
    elif "neutral" in t: score += 10; criterios["verdict"] = 10
    elif "caution" in t: score += 5; criterios["verdict"] = 5
    elif "sell" in t: criterios["verdict"] = 0
    else: criterios["verdict"] = 8; score += 8

    # Top 10 holders
    m = re.search(r"top 10[^\d]*(\d+\.?\d*)%", t)
    if m:
        top10 = float(m.group(1))
        if top10 < 10: score += 20; criterios["top10"] = 20
        elif top10 < 25: score += 15; criterios["top10"] = 15
        elif top10 < 50: score += 8; criterios["top10"] = 8
        else: criterios["top10"] = 0
    else:
        criterios["top10"] = 10; score += 10

    # Buy pressure
    m = re.search(r"buy pressure[:\s]+(\d+\.?\d*)", t)
    if m:
        bp = float(m.group(1))
        if bp > 10: score += 15; criterios["bp"] = 15
        elif bp > 5: score += 10; criterios["bp"] = 10
        elif bp > 2: score += 5; criterios["bp"] = 5
        else: criterios["bp"] = 0
    else:
        criterios["bp"] = 5; score += 5

    # Base
    score += 15; criterios["base"] = 15

    return min(score, 100), criterios


async def analizar(candidato):
    """Analiza un token via Deficlaw."""
    result = {
        "symbol": candidato.get("symbol", "?"),
        "address": candidato["address"],
        "fuente": candidato.get("fuente", "?"),
        "texto": "",
        "score": 0,
        "confianza": 0,
        "criterios": {},
        "error": None
    }

    try:
        transport = StdioTransport(command="npx", args=["@0xprotovox/deficlaw"])
        async with Client(transport) as client:
            try:
                raw = await asyncio.wait_for(
                    client.call_tool("analyze_token", {"address": candidato["address"]}),
                    timeout=40
                )
                data = serialize_result(raw)
                result["texto"] = texto_completo(data)[:500]
            except Exception as e:
                result["error"] = str(e)[:100]

        score, crit = calcular_score(result["texto"])
        result["score"] = score
        result["criterios"] = crit
        # Confianza simplificada
        result["confianza"] = min(95, int(score * 0.95))

    except Exception as e:
        result["error"] = str(e)[:150]

    return result


async def main_async():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Panorama completo - {ts}")

    data = leer_ultimos_candidatos()
    if not data:
        print("[YIN] ERROR: No hay candidatos")
        return

    candidatos = data.get("candidatos", [])[:MAX_TOKENS]
    print(f"[YIN] Analizando {len(candidatos)} candidatos (sin filtro)...")

    resultados = []
    for i, c in enumerate(candidatos, 1):
        print(f"[YIN] [{i}/{len(candidatos)}] {c.get('symbol', '?')}...")
        r = await analizar(c)
        resultados.append(r)

    # Ordenar pero SIN filtrar
    resultados.sort(key=lambda x: x["score"], reverse=True)

    panorama = {
        "timestamp": ts,
        "fase": "panorama_completo",
        "total_analizados": len(resultados),
        "ranking": resultados
    }

    out_path = PANORAMA_DIR / f"panorama_completo_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(panorama, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[YIN] Guardado: {out_path}")

    print(f"\n[YIN] === RANKING COMPLETO ({len(resultados)}) ===")
    for i, r in enumerate(resultados, 1):
        print(f"[YIN] {i:2}. {r['symbol']:15} | Score {r['score']:3} | Conf {r['confianza']}% | {r['fuente'][:30]}")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()