#!/usr/bin/env python3
"""
script_39b_panorama_multi.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Analisis multi-activo: toma los tokens mas relevantes de las
    fuentes actuales, los puntua, y genera un panorama.
    NO solo un activo. Multiples activos con ranking.
"""

import asyncio
import json
import glob
from datetime import datetime, timezone
from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
MCP_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "mcp_analytics"
PANORAMA_DIR = PROJECT_ROOT / "02_Analisis" / "panorama"
PANORAMA_DIR.mkdir(parents=True, exist_ok=True)

# Cuantos tokens analizar
TOP_N = 8


def leer_ultimo_mcp_analytics():
    """Lee el ultimo archivo mcp_analytics_v2."""
    archivos = sorted(glob.glob(str(MCP_DIR / "mcp_analytics_v2_*.json")), reverse=True)
    if not archivos:
        return None
    with open(archivos[0], "r", encoding="utf-8") as f:
        return json.load(f)


def extraer_candidatos(data):
    """Extrae tokens con direccion del archivo mcp_analytics."""
    candidatos = []

    def_text = data.get("resultados", {}).get("deficlaw", {})

    # Del get_trending
    trending = def_text.get("get_trending", {})
    if isinstance(trending, dict) and "content" in trending:
        for item in trending["content"]:
            if item.get("type") == "text":
                try:
                    parsed = json.loads(item["text"])
                    if isinstance(parsed, list):
                        for t in parsed:
                            if t.get("address"):
                                candidatos.append({
                                    "name": t.get("symbol", "?"),
                                    "address": t["address"],
                                    "fuente": "trending",
                                    "datos_previos": t
                                })
                except (json.JSONDecodeError, TypeError):
                    pass

    # Del get_new_launches
    launches = def_text.get("get_new_launches", {})
    if isinstance(launches, dict) and "content" in launches:
        for item in launches["content"]:
            if item.get("type") == "text":
                try:
                    parsed = json.loads(item["text"])
                    if isinstance(parsed, list):
                        for t in parsed:
                            if t.get("address"):
                                candidatos.append({
                                    "name": t.get("symbol", "?"),
                                    "address": t["address"],
                                    "fuente": "new_launch",
                                    "datos_previos": t
                                })
                except (json.JSONDecodeError, TypeError):
                    pass

    return candidatos


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


def calcular_score_simple(data_analyze):
    """Calcula score basado en el output de analyze_token."""
    score = 0
    criterios = {}

    # Extraer verdict si existe
    verdict = ""
    if isinstance(data_analyze, dict):
        content = data_analyze.get("content", [])
        for item in content:
            if item.get("type") == "text":
                verdict += item.get("text", "")

    # Criterios basicos
    v = verdict.lower()

    # 1. Distribucion (top 10 < 20% = 20 pts)
    if "top 10" in v:
        # Extraer porcentaje
        import re
        m = re.search(r"top 10[:\s]+(\d+\.?\d*)%", v)
        if m:
            top10 = float(m.group(1))
            if top10 < 10:
                score += 20; criterios["distribucion"] = 20
            elif top10 < 20:
                score += 15; criterios["distribucion"] = 15
            elif top10 < 40:
                score += 8; criterios["distribucion"] = 8
            else:
                criterios["distribucion"] = 0
        else:
            criterios["distribucion"] = 0
    else:
        criterios["distribucion"] = 0

    # 2. Risk score inverso (risk 0-20 = 20pts)
    if "risk score" in v:
        import re
        m = re.search(r"risk score[:\s]+(\d+)", v)
        if m:
            risk = int(m.group(1))
            if risk < 20:
                score += 20; criterios["risk"] = 20
            elif risk < 30:
                score += 15; criterios["risk"] = 15
            elif risk < 45:
                score += 8; criterios["risk"] = 8
            else:
                criterios["risk"] = 0
        else:
            criterios["risk"] = 0
    else:
        criterios["risk"] = 0

    # 3. Verdict
    if "strong buy" in v:
        score += 20; criterios["verdict"] = 20
    elif "buy signal" in v:
        score += 15; criterios["verdict"] = 15
    elif "neutral" in v:
        score += 8; criterios["verdict"] = 8
    elif "caution" in v:
        score += 5; criterios["verdict"] = 5
    elif "sell" in v:
        criterios["verdict"] = 0
    else:
        criterios["verdict"] = 5

    # 4. Buy pressure
    if "buy pressure" in v:
        import re
        m = re.search(r"buy pressure[:\s]+(\d+\.?\d*)", v)
        if m:
            bp = float(m.group(1))
            if bp > 10:
                score += 20; criterios["buy_pressure"] = 20
            elif bp > 5:
                score += 12; criterios["buy_pressure"] = 12
            else:
                criterios["buy_pressure"] = 5
        else:
            criterios["buy_pressure"] = 5
    else:
        criterios["buy_pressure"] = 5

    # 5. Base
    score += 20; criterios["base"] = 20

    return min(score, 100), criterios


def calcular_confianza(score):
    """Convierte score a porcentaje de confianza."""
    # Mapeo lineal: score 75 -> 70%, score 100 -> 90%
    if score >= 90:
        return 90
    elif score >= 80:
        return 82
    elif score >= 75:
        return 75
    elif score >= 65:
        return 60
    elif score >= 50:
        return 40
    else:
        return 20


async def analizar_token(token):
    """Deep dive de un token."""
    result = {"name": token["name"], "address": token["address"], "fuente": token["fuente"],
              "analyze": None, "security": None, "score": 0, "confianza": 0, "criterios": {}, "error": None}

    try:
        transport = StdioTransport(command="npx", args=["@0xprotovox/deficlaw"])
        async with Client(transport) as client:
            try:
                raw = await asyncio.wait_for(
                    client.call_tool("analyze_token", {"address": token["address"]}),
                    timeout=45
                )
                result["analyze"] = serialize_result(raw)
            except Exception as e:
                result["error"] = f"analyze: {str(e)[:100]}"
                return result

        score, criterios = calcular_score_simple(result["analyze"])
        result["score"] = score
        result["criterios"] = criterios
        result["confianza"] = calcular_confianza(score)

    except Exception as e:
        result["error"] = str(e)[:150]

    return result


async def main_async():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Panorama multi-activo - {ts}")

    # 1. Leer datos previos
    data = leer_ultimo_mcp_analytics()
    if not data:
        print("[YIN] ERROR: No hay archivo mcp_analytics_v2")
        return

    candidatos = extraer_candidatos(data)
    print(f"[YIN] Candidatos encontrados: {len(candidatos)}")

    # 2. Tomar top N
    candidatos = candidatos[:TOP_N]
    print(f"[YIN] Analizando top {len(candidatos)}")

    # 3. Analizar cada uno
    resultados = []
    for i, c in enumerate(candidatos, 1):
        print(f"[YIN] [{i}/{len(candidatos)}] {c['name']}...")
        r = await analizar_token(c)
        resultados.append(r)

    # 4. Ranking por score
    resultados.sort(key=lambda x: x["score"], reverse=True)

    # 5. Panorama
    panorama = {
        "timestamp": ts,
        "fase": "panorama_multi",
        "total_analizados": len(resultados),
        "ranking": resultados
    }

    out_path = PANORAMA_DIR / f"panorama_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(panorama, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")

    # 6. Reporte en consola
    print(f"\n[YIN] === PANORAMA ===")
    for i, r in enumerate(resultados, 1):
        print(f"[YIN] {i}. {r['name']:12} | Score {r['score']:3}/100 | Conf {r['confianza']}% | {r['fuente']}")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()