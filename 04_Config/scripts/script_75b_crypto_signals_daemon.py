#!/usr/bin/env python3
"""
script_75b_crypto_signals_daemon.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Version corregida. Ejecuta crypto-signals-mcp como subprocess
    y se comunica via stdio.
"""

import asyncio
import json
import sys
import subprocess
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


async def run_signals():
    results = {}

    # Encontrar la ruta del paquete instalado
    try:
        import importlib.util
        spec = importlib.util.find_spec("crypto_signals_mcp")
        if spec and spec.origin:
            server_path = Path(spec.origin).parent / "server.py"
        else:
            results["error"] = "crypto-signals-mcp no esta instalado. Ejecutar: python -m pip install crypto-signals-mcp"
            return results
    except Exception as e:
        results["error"] = f"No se pudo localizar el paquete: {str(e)[:200]}"
        return results

    if not server_path.exists():
        results["error"] = f"server.py no encontrado en {server_path}"
        return results

    results["server_path"] = str(server_path)

    # Ejecutar via stdio
    try:
        transport = StdioTransport(command="fastmcp", args=["run", str(server_path)])
        async with Client(transport) as client:
            try:
                raw = await asyncio.wait_for(
                    client.call_tool("scan_all_tokens", {}),
                    timeout=60
                )
                results["scan_all"] = str(raw)[:5000]
            except Exception as e:
                results["scan_all_error"] = str(e)[:200]

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
    print(f"[YIN] Crypto Signals Daemon - {ts}")

    if not MCP_OK:
        print("[YIN] ERROR: fastmcp no instalado")
        return

    results = asyncio.run(run_signals())

    out = {"timestamp": ts, "fase": "crypto_signals_daemon", "results": results}
    out_path = SIGNALS_DIR / f"signals_daemon_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")

    for key, val in results.items():
        if "error" in key:
            print(f"[YIN] {key}: {str(val)[:150]}")


if __name__ == "__main__":
    main()