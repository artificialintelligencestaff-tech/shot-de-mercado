#!/usr/bin/env python3
"""
script_36b_deep_dive_verified.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Deep dive con direcciones VERIFICADAS del archivo mcp_analytics_v2.
    Parametro correcto: address (no token).

SEGURIDAD:
    Solo analyze_token + get_token_security (lectura).
    NUNCA transfer, swap, o escritura.
"""

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
OUT_DIR = PROJECT_ROOT / "02_Analisis" / "deep_dive_verified"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Tokens con direcciones VERIFICADAS del archivo fuente
TOKENS = [
    # Prioridad 1: cambios extremos
    {"name": "TRADE", "address": "5dDeBvYERiX7Vks5TU6aaSxQeYJk5jHncHwBaVqTpump", "razon": "+132% en 11m"},
    {"name": "ZIONIST_INU", "address": "4qyxvY9zD2AeveZGGVLhmA9KPe4AGx6fii7kWSz5wKtq", "razon": "+26% en 3m"},
    {"name": "tunie", "address": "56Vh88Y4dsUcYLuxHcTyermeHiCjRMg3t61bnbYRpump", "razon": "-52.81% en 14m"},
    {"name": "Catwifout", "address": "5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump", "razon": "Nuevo par con web+Twitter"},
    # Prioridad 2: trending top volumen
    {"name": "casinu", "address": "2eMoMqs194VxPHSWtCCzkBGqwCUbD4ZcqhecoGuh4tTp", "razon": "-87.97% 24h, $1.25M vol"},
    {"name": "PAIDDOGE", "address": "52qkNpgTHcjuDYhKVcg6rJS4uYYtJHpDRcJoSdKqpump", "razon": "-28.87% 24h, $5.35M vol"},
    {"name": "fomocoin", "address": "3wrwK9CctFXYedMVBGYD6sWSTfXgbh2DGQAL3z2epump", "razon": "-89.96% 24h, $252K vol"},
]


def serialize_result(result):
    """Convierte CallToolResult a dict JSON-serializable."""
    if result is None:
        return None
    if isinstance(result, (str, int, float, bool, list, dict)):
        return result
    if hasattr(result, "model_dump"):
        try:
            return result.model_dump()
        except Exception:
            pass
    serializable = {"isError": getattr(result, "isError", False), "content": []}
    content = getattr(result, "content", None)
    if content:
        for item in content:
            if hasattr(item, "text"):
                serializable["content"].append({"type": "text", "text": item.text})
            else:
                serializable["content"].append(str(item))
    return serializable


async def deep_dive(token_info):
    """Analiza un token con Deficlaw usando address."""
    print(f"\n[YIN] === {token_info['name']} ({token_info['razon']}) ===")
    print(f"[YIN]   Address: {token_info['address']}")

    result = {
        "name": token_info["name"],
        "address": token_info["address"],
        "razon": token_info["razon"],
        "analyze": None,
        "security": None,
        "errors": []
    }

    try:
        transport = StdioTransport(command="npx", args=["@0xprotovox/deficlaw"])
        async with Client(transport) as client:
            # analyze_token con address
            try:
                print(f"[YIN]   analyze_token...")
                raw = await client.call_tool("analyze_token", {"address": token_info["address"]})
                result["analyze"] = serialize_result(raw)
            except Exception as e:
                result["errors"].append(f"analyze_token: {str(e)[:200]}")

            # get_token_security con address
            try:
                print(f"[YIN]   get_token_security...")
                raw = await client.call_tool("get_token_security", {"address": token_info["address"]})
                result["security"] = serialize_result(raw)
            except Exception as e:
                result["errors"].append(f"get_token_security: {str(e)[:200]}")

    except Exception as e:
        result["errors"].append(f"connection: {str(e)[:200]}")

    return result


async def main_async():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Deep Dive Verified - {ts}")
    print(f"[YIN] Total tokens: {len(TOKENS)}")

    consolidated = {"timestamp": ts, "fase": "deep_dive_verified", "tokens": []}

    for token in TOKENS:
        resultado = await deep_dive(token)
        consolidated["tokens"].append(resultado)

    out_path = OUT_DIR / f"deep_dive_verified_{ts}.json"
    try:
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(consolidated, f, indent=2, ensure_ascii=False, default=str)
        print(f"\n[YIN] Guardado: {out_path}")

        exitosos = sum(1 for t in consolidated["tokens"] if t["analyze"] or t["security"])
        print(f"[YIN] Tokens con datos: {exitosos}/{len(TOKENS)}")
    except Exception as e:
        print(f"\n[YIN] ERROR guardando: {e}")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()