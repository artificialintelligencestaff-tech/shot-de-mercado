#!/usr/bin/env python3
"""
script_15b_coinfuty_corregido.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Corregir el script 15. El parametro correcto es "symbol", no "coin".
"""

import json
import requests
import time
from datetime import datetime, timezone
from pathlib import Path

COINFUTY_URL = "https://mcp.coinfuty.com/api/mcp"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
MERCADOS_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "mercados" / "coinfuty"
MERCADOS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30


def parse_sse(raw_text):
    try:
        for line in raw_text.split("\n"):
            line = line.strip()
            if line.startswith("data: "):
                return json.loads(line[6:])
        return json.loads(raw_text)
    except json.JSONDecodeError:
        return {"error": "JSONDecodeError"}


def call_coinfuty(tool_name, arguments=None):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": arguments or {}}
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    try:
        response = requests.post(COINFUTY_URL, json=payload, headers=headers, timeout=TIMEOUT)
        return {
            "tool": tool_name,
            "http_status": response.status_code,
            "parsed": parse_sse(response.text)
        }
    except Exception as e:
        return {"tool": tool_name, "error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Coinfuty Corregido - {ts}")

    # 1. Funding rates de BTC (parametro correcto: symbol)
    print("[YIN] Solicitando funding rates de BTC...")
    funding = call_coinfuty("get_funding_rates", {"symbol": "BTC"})
    funding_path = MERCADOS_DIR / f"funding_rates_btc_{ts}.json"
    with open(funding_path, "w", encoding="utf-8") as f:
        json.dump(funding, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {funding_path}")
    time.sleep(2)

    # 2. Coin summary de ETH (parametro correcto: symbol)
    print("[YIN] Solicitando coin summary de ETH...")
    eth_summary = call_coinfuty("get_coin_summary", {"symbol": "ETH"})
    eth_path = MERCADOS_DIR / f"eth_summary_{ts}.json"
    with open(eth_path, "w", encoding="utf-8") as f:
        json.dump(eth_summary, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {eth_path}")

    print("[YIN] Script 15b finalizado.")


if __name__ == "__main__":
    main()