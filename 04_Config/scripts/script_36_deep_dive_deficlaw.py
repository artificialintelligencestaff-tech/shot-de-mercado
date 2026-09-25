#!/usr/bin/env python3
"""
script_36_deep_dive_deficlaw.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Deep dive de tokens nuevos detectados por Deficlaw.
    Usa analyze_token + get_token_security (SOLO LECTURA).

SEGURIDAD:
    Solo tools de lectura. Nunca swap, transfer, o escritura.
"""

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
OUT_DIR = PROJECT_ROOT / "02_Analisis" / "deep_dive_deficlaw"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Tokens a analizar (del reporte de script 35b)
TOKENS_A_ANALIZAR = [
    # Direcciones Solana de los tokens nuevos mas interesantes
    # NOTA: YIN debe obtener las direcciones exactas de los resultados de get_new_launches
    "Catwifout",
    "ZIONIST INU",
    "TRADE",
    "tunie",
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


async def deep_dive_token(token_name):
    """Analiza un token con Deficlaw: analyze_token + get_token_security."""
    print(f"\n[YIN] === Analizando {token_name} ===")
    result = {"token": token_name, "analyze": None, "security": None, "errors": []}

    try:
        transport = StdioTransport(command="npx", args=["@0xprotovox/deficlaw"])
        async with Client(transport) as client:
            # 1. analyze_token
            try:
                print(f"[YIN]   analyze_token({token_name})...")
                raw = await client.call_tool("analyze_token", {"query": token_name})
                result["analyze"] = serialize_result(raw)
            except Exception as e:
                result["errors"].append(f"analyze_token: {e}")

            # 2. get_token_security
            try:
                print(f"[YIN]   get_token_security({token_name})...")
                raw = await client.call_tool("get_token_security", {"query": token_name})
                result["security"] = serialize_result(raw)
            except Exception as e:
                result["errors"].append(f"get_token_security: {e}")

    except Exception as e:
        result["errors"].append(f"connection: {e}")

    return result


async def main_async():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Deep Dive Deficlaw - {ts}")

    consolidated = {"timestamp": ts, "fase": "deep_dive_deficlaw", "tokens": []}

    for token in TOKENS_A_ANALIZAR:
        resultado = await deep_dive_token(token)
        consolidated["tokens"].append(resultado)

    # Guardar
    out_path = OUT_DIR / f"deep_dive_deficlaw_{ts}.json"
    try:
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(consolidated, f, indent=2, ensure_ascii=False, default=str)
        print(f"\n[YIN] Guardado: {out_path}")
    except Exception as e:
        print(f"\n[YIN] ERROR guardando: {e}")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()