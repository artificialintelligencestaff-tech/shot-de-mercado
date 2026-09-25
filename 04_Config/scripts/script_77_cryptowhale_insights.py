#!/usr/bin/env python3
"""
script_77_cryptowhale_insights.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume CryptoWhaleInsights MCP (17 tools, 14 chains).
    Alternativa GRATUITA a MadeOnSol surge_detection.
    No requiere API key, no KYC.
"""

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

try:
    from fastmcp import Client
    from fastmcp.client.transports import StdioTransport
    MCP_OK = True
except ImportError:
    MCP_OK = False

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
WHALE_DIR = PROJECT_ROOT / "02_Analisis" / "cryptowhale_insights"
WHALE_DIR.mkdir(parents=True, exist_ok=True)

# Endpoint MCP remoto (via HTTP/SSE)
CW_INSIGHTS_URL = "https://cryptowhaleinsights.com/api-for-ai-agents"


async def run_insights():
    results = {}
    try:
        # Conexion via SSE remoto
        transport = StdioTransport(command="npx", args=["-y", "@cryptowhaleinsights/mcp-server"])
        async with Client(transport) as client:
            # Listar tools disponibles
            try:
                tools = await asyncio.wait_for(client.list_tools(), timeout=30)
                results["tools"] = [{"name": t.name, "desc": (t.description or "")[:100]} for t in tools]
            except Exception as e:
                results["tools_error"] = str(e)[:200]

            # Consultar trends
            try:
                raw = await asyncio.wait_for(
                    client.call_tool("get_trending_tokens", {}),
                    timeout=45
                )
                results["trending"] = str(raw)[:3000]
            except Exception as e:
                results["trending_error"] = str(e)[:200]

            # Consultar whale movements
            try:
                raw = await asyncio.wait_for(
                    client.call_tool("get_whale_movements", {"limit": 20}),
                    timeout=45
                )
                results["whale_movements"] = str(raw)[:3000]
            except Exception as e:
                results["whale_error"] = str(e)[:200]

    except Exception as e:
        results["connection_error"] = str(e)[:300]

    return results


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] CryptoWhaleInsights MCP - {ts}")

    if not MCP_OK:
        print("[YIN] ERROR: fastmcp no instalado")
        return

    results = asyncio.run(run_insights())

    out = {"timestamp": ts, "fase": "cryptowhale_insights", "results": results}
    out_path = WHALE_DIR / f"whale_insights_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()