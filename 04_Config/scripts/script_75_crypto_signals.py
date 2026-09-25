#!/usr/bin/env python3
"""
script_75_crypto_signals.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Alternativa GRATUITA a MadeOnSol surge_detection.
    Detecta anomalias de volumen en 50+ tokens.
    Fuente: github.com/MarcinDudekDev/crypto-signals-mcp
"""

import json
import asyncio
from datetime import datetime, timezone
from pathlib import Path

try:
    from fastmcp import Client
    from fastmcp.client.transports import StdioTransport
    MCP_OK = True
except ImportError:
    MCP_OK = False

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
SIGNALS_DIR = PROJECT_ROOT / "02_Analisis" / "crypto_signals"
SIGNALS_DIR.mkdir(parents=True, exist_ok=True)


async def run_signals_mcp():
    """Ejecuta crypto-signals-mcp via stdio."""
    results = {}
    try:
        transport = StdioTransport(command="fastmcp", args=["run", "crypto-signals-mcp"])
        async with Client(transport) as client:
            # 1. Scan all tokens
            try:
                raw = await asyncio.wait_for(
                    client.call_tool("scan_all_tokens", {}),
                    timeout=60
                )
                results["scan_all"] = str(raw)[:5000]
            except Exception as e:
                results["scan_all_error"] = str(e)[:200]

            # 2. High-confidence alerts
            try:
                raw = await asyncio.wait_for(
                    client.call_tool("get_anomaly_alerts", {}),
                    timeout=60
                )
                results["alerts"] = str(raw)[:5000]
            except Exception as e:
                results["alerts_error"] = str(e)[:200]

    except Exception as e:
        results["connection_error"] = str(e)[:300]

    return results


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Crypto Signals MCP - {ts}")

    if not MCP_OK:
        print("[YIN] ERROR: fastmcp no instalado")
        return

    results = asyncio.run(run_signals_mcp())

    out = {"timestamp": ts, "fase": "crypto_signals", "results": results}
    out_path = SIGNALS_DIR / f"signals_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")

    for key, val in results.items():
        if "error" in key:
            print(f"[YIN] {key}: {val[:100]}")


if __name__ == "__main__":
    main()