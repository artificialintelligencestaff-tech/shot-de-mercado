#!/usr/bin/env python3
"""
script_09d_coinlobster.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Conectar con CoinLobster MCP (JSON-RPC, SSE).
    17 tools operativas: whale_trades, whale_radar, whale_flow, flag_outcomes,
    market_snapshot, liquidations, crypto_news.
    Sin API key.
"""

import json
import requests
import time
from datetime import datetime, timezone
from pathlib import Path

COINLOBSTER_URL = "https://coinlobster.com/mcp"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
ONCHAIN_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "onchain"
ONCHAIN_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 5


def parse_sse(raw_text):
    try:
        for line in raw_text.split("\n"):
            line = line.strip()
            if line.startswith("data: "):
                return json.loads(line[6:])
        return json.loads(raw_text)
    except json.JSONDecodeError as e:
        return {"error": {"message": f"JSONDecodeError: {e}", "raw": raw_text[:500]}}


def call_coinlobster(method, params=None):
    payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params or {}}
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.post(
                COINLOBSTER_URL, json=payload, headers=headers, timeout=TIMEOUT
            )
            return {
                "http_status": response.status_code,
                "parsed": parse_sse(response.text),
                "raw_preview": response.text[:500]
            }
        except requests.exceptions.RequestException as e:
            print(f"[Intento {attempt}/{MAX_RETRIES}] Error: {e}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
            else:
                return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] CoinLobster MCP - {ts}")

    result = {
        "timestamp": ts,
        "fase": "coinlobster",
        "estado": "exito",
        "datos": {}
    }

    # 1. tools/list para verificar herramientas
    print("[YIN] Solicitando tools/list...")
    result["datos"]["tools"] = call_coinlobster("tools/list", {})
    time.sleep(2)

    # 2. whale_radar - Coins con flujo inusual
    print("[YIN] Solicitando whale_radar...")
    result["datos"]["whale_radar"] = call_coinlobster("tools/call", {
        "name": "whale_radar",
        "arguments": {"window": "4h"}
    })
    time.sleep(2)

    # 3. market_overview - Escaneo market-wide
    print("[YIN] Solicitando market_overview...")
    result["datos"]["market_overview"] = call_coinlobster("tools/call", {
        "name": "market_overview",
        "arguments": {}
    })
    time.sleep(2)

    # 4. whale_trades - Trades recientes
    print("[YIN] Solicitando whale_trades...")
    result["datos"]["whale_trades"] = call_coinlobster("tools/call", {
        "name": "whale_trades",
        "arguments": {"limit": 25}
    })

    # Guardar
    out_path = ONCHAIN_DIR / f"coinlobster_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print("[YIN] Script 09d finalizado.")


if __name__ == "__main__":
    main()