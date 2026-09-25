#!/usr/bin/env python3
"""
script_35_mcp_analytics.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Recolectar datos de SOLO LECTURA desde los 3 MCPs stdio.
    NUNCA llama a herramientas de escritura/transaccion.

SEGURIDAD:
    Solo lee. Nunca transfiere fondos.
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


async def run_stdio_mcp(command, args, tool_calls):
    """Ejecuta una lista de tools de solo lectura en un MCP stdio."""
    results = {}
    try:
        transport = StdioTransport(command=command, args=args)
        async with Client(transport) as client:
            for tool_name, tool_args in tool_calls:
                print(f"[YIN]   Ejecutando {tool_name}...")
                try:
                    result = await client.call_tool(tool_name, tool_args)
                    results[tool_name] = result
                except Exception as e:
                    results[tool_name] = {"error": str(e)}
    except Exception as e:
        results["_connection_error"] = str(e)
    return results


async def main_async():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] MCP Analytics (solo lectura) - {ts}")

    consolidated = {"timestamp": ts, "fase": "mcp_analytics_readonly", "resultados": {}}

    # --- DEFICLAW (9 tools lectura) ---
    print("\n[YIN] === Deficlaw ===")
    deficlaw_calls = [
        ("get_trending", {}),
        ("get_new_launches", {}),
        ("get_top_traders", {}),
    ]
    consolidated["resultados"]["deficlaw"] = await run_stdio_mcp(
        "npx", ["@0xprotovox/deficlaw"], deficlaw_calls
    )

    # --- SOLIRIS (solo lectura Solana) ---
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

    # --- KOL MCP (solo lectura) ---
    print("\n[YIN] === KOL MCP ===")
    # NOTA: requiere wallet_address concreta. Aqui solo listamos tools sin llamarlas.
    consolidated["resultados"]["kol_mcp"] = {
        "nota": "Requiere wallet_address. No se ejecuta sin direcciones validas.",
        "tools_disponibles": ["get_wallet_portfolio", "get_wallet_trades"]
    }

    # Guardar
    out_path = DATA_DIR / f"mcp_analytics_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(consolidated, f, indent=2, ensure_ascii=False)
    print(f"\n[YIN] Guardado: {out_path}")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()