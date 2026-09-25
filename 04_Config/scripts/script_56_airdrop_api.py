#!/usr/bin/env python3
"""
script_56_airdrop_api.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Reemplaza el scraping de airdrops por MCP/API.
    Usa airdrop-intel-mcp via MCPize (tier gratuito limitado).
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
AIRDROP_DIR = PROJECT_ROOT / "02_Analisis" / "airdrops_parsed"
AIRDROP_DIR.mkdir(parents=True, exist_ok=True)

# MCPize endpoint para airdrop-intel-mcp
MCPIZE_URL = "https://airdrop-intel-mcp.mcpize.run"
TIMEOUT = 30


def fetch_airdrop_intel():
    """Intenta consultar el MCP de airdrops via MCPize."""
    try:
        # MCP requiere JSON-RPC
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": "search_airdrops",
                "arguments": {"query": "", "limit": 20}
            }
        }
        headers = {"Content-Type": "application/json"}
        r = requests.post(MCPIZE_URL, json=payload, headers=headers, timeout=TIMEOUT)
        return {"http_status": r.status_code, "data": r.json() if r.status_code == 200 else r.text[:500]}
    except Exception as e:
        return {"error": str(e)[:200]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Airdrop API - {ts}")

    result = fetch_airdrop_intel()
    print(f"[YIN] Resultado: {result}")

    out = {"timestamp": ts, "fase": "airdrop_api", "result": result}
    out_path = AIRDROP_DIR / f"airdrop_api_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()