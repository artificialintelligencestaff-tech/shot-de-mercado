#!/usr/bin/env python3
"""
script_35b_mcp_analytics.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Version 2. Corrige serializacion de CallToolResult.
    SOLO LECTURA. Nunca llama a transfer, swap, o cualquier tool de escritura.
"""

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
DATA_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "mcp_analytics"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def serialize_result(result):
    """Convierte CallToolResult a dict JSON-serializable."""
    if result is None:
        return None

    # Si ya es dict serializable
    if isinstance(result, (str, int, float, bool, list, dict)):
        return result

    # Intentar model_dump (pydantic) primero
    if hasattr(result, "model_dump"):
        try:
            return result.model_dump()
        except Exception:
            pass

    # CallToolResult: extraer content
    serializable = {
        "isError": getattr(result, "isError", False),
        "content": []
    }

    content = getattr(result, "content", None)
    if content:
        for item in content:
            if hasattr(item, "text"):
                serializable["content"].append({"type": "text", "text": item.text})
            elif hasattr(item, "model_dump"):
                try:
                    serializable["content"].append(item.model_dump())
                except Exception:
                    serializable["content"].append(str(item))
            else:
                serializable["content"].append(str(item))

    return serializable


async def run_stdio_mcp(command, args, tool_calls):
    """Ejecuta tools de solo lectura en un MCP stdio."""
    results = {}
    try:
        transport = StdioTransport(command=command, args=args)
        async with Client(transport) as client:
            for tool_name, tool_args in tool_calls:
                print(f"[YIN]   Ejecutando {tool_name}...")
                try:
                    raw = await client.call_tool(tool_name, tool_args)
                    results[tool_name] = serialize_result(raw)
                except Exception as e:
                    results[tool_name] = {"error": str(e)}
    except Exception as e:
        results["_connection_error"] = str(e)
    return results


async def main_async():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] MCP Analytics v2 (solo lectura) - {ts}")

    consolidated = {"timestamp": ts, "fase": "mcp_analytics_v2", "resultados": {}}

    # --- DEFICLAW ---
    print("\n[YIN] === Deficlaw ===")
    deficlaw_calls = [
        ("get_trending", {}),
        ("get_new_launches", {}),
        ("get_top_traders", {}),
    ]
    consolidated["resultados"]["deficlaw"] = await run_stdio_mcp(
        "npx", ["@0xprotovox/deficlaw"], deficlaw_calls
    )

    # --- SOLIRIS (solo lectura) ---
    print("\n[YIN] === Soliris (solo lectura) ===")
    soliris_calls = [
        ("soliris_get_network_stats", {}),
        ("soliris_new_pairs", {}),
        ("soliris_birdeye_trending", {}),
        ("soliris_pumpfun_hot", {}),
        ("soliris_momentum_scan", {}),
        ("soliris_bounce_radar", {}),
    ]
    consolidated["resultados"]["soliris"] = await run_stdio_mcp(
        "npx", ["soliris-mcp"], soliris_calls
    )

    # Guardar con manejo de errores
    out_path = DATA_DIR / f"mcp_analytics_v2_{ts}.json"
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