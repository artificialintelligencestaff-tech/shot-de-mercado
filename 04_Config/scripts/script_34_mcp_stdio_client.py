#!/usr/bin/env python3
"""
script_34_mcp_stdio_client.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Conectar a servidores MCP stdio via fastmcp.Client.
    Descubre tools disponibles de:
    - @three-ws/kol-mcp
    - soliris-mcp
    - @0xprotovox/deficlaw
"""

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

from fastmcp import Client

PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
OUT_DIR = PROJECT_ROOT / "02_Analisis" / "mcp_stdio"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# MCPs stdio a consultar
MCPS = [
    {"name": "kol_mcp", "command": ["npx", "@three-ws/kol-mcp"]},
    {"name": "soliris_mcp", "command": ["npx", "soliris-mcp"]},
    {"name": "deficlaw", "command": ["npx", "@0xprotovox/deficlaw"]},
]


async def discover_tools(name, command):
    """Conecta al MCP y lista sus tools."""
    print(f"\n[YIN] Conectando a {name}...")
    result = {"name": name, "command": " ".join(command), "tools": [], "error": None}

    try:
        async with Client(command[0], args=command[1:]) as client:
            tools = await client.list_tools()
            for tool in tools:
                result["tools"].append({
                    "name": tool.name,
                    "description": (tool.description or "")[:200],
                    "input_schema": tool.inputSchema if hasattr(tool, "inputSchema") else None
                })
            print(f"[YIN] {name}: {len(result['tools'])} tools descubiertas")
    except Exception as e:
        result["error"] = str(e)
        print(f"[YIN] ERROR en {name}: {e}")

    return result


async def main_async():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] MCP stdio client - {ts}")

    resultados = []
    for mcp in MCPS:
        resultado = await discover_tools(mcp["name"], mcp["command"])
        resultados.append(resultado)

    # Guardar consolidado
    out = {
        "timestamp": ts,
        "fase": "mcp_stdio_discovery",
        "mcps": resultados
    }
    out_path = OUT_DIR / f"mcp_stdio_tools_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\n[YIN] Guardado: {out_path}")

    # Resumen
    total_tools = sum(len(r["tools"]) for r in resultados)
    print(f"[YIN] Total tools descubiertas: {total_tools}")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()