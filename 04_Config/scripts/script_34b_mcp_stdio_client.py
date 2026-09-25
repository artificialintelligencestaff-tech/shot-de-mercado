#!/usr/bin/env python3
"""
script_34b_mcp_stdio_client.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Version corregida. Usa StdioTransport en lugar de args.
    Descubre tools de los 3 MCPs stdio.
"""

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
OUT_DIR = PROJECT_ROOT / "02_Analisis" / "mcp_stdio"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# MCPs stdio (comando y argumentos separados)
MCPS = [
    {"name": "kol_mcp", "command": "npx", "args": ["@three-ws/kol-mcp"]},
    {"name": "soliris_mcp", "command": "npx", "args": ["soliris-mcp"]},
    {"name": "deficlaw", "command": "npx", "args": ["@0xprotovox/deficlaw"]},
]


async def discover_tools(name, command, args):
    """Conecta al MCP via StdioTransport y lista sus tools."""
    print(f"\n[YIN] Conectando a {name}...")
    result = {"name": name, "command": f"{command} {' '.join(args)}", "tools": [], "error": None}

    try:
        # Crear transporte stdio explicitamente
        transport = StdioTransport(command=command, args=args)
        client = Client(transport)

        async with client:
            tools = await client.list_tools()
            for tool in tools:
                result["tools"].append({
                    "name": tool.name,
                    "description": (tool.description or "")[:200]
                })
            print(f"[YIN] {name}: {len(result['tools'])} tools descubiertas")
    except Exception as e:
        result["error"] = str(e)
        print(f"[YIN] ERROR en {name}: {e}")

    return result


async def main_async():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] MCP stdio client v2 - {ts}")

    resultados = []
    for mcp in MCPS:
        resultado = await discover_tools(mcp["name"], mcp["command"], mcp["args"])
        resultados.append(resultado)

    out = {"timestamp": ts, "fase": "mcp_stdio_discovery_v2", "mcps": resultados}
    out_path = OUT_DIR / f"mcp_stdio_tools_v2_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\n[YIN] Guardado: {out_path}")

    total_tools = sum(len(r["tools"]) for r in resultados)
    print(f"[YIN] Total tools descubiertas: {total_tools}")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()