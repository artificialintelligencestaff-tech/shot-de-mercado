#!/usr/bin/env python3
"""
script_09g_coinlobster_auth.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Conectar con CoinLobster MCP usando API key para eliminar delay de 30 min.
    Lee la key desde .env
"""

import json
import os
import requests
import time
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

# Cargar .env
load_dotenv(Path(r"D:\Proyecto Shot de mercado\04_Config\.env"))

COINLOBSTER_API_KEY = os.getenv("COINLOBSTER_API_KEY", "")
COINLOBSTER_URL = "https://coinlobster.com/mcp"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
ONCHAIN_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "onchain" / "coinlobster_auth"
ONCHAIN_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30


def parse_sse(raw_text):
    try:
        for line in raw_text.split("\n"):
            line = line.strip()
            if line.startswith("data: "):
                return json.loads(line[6:])
        return json.loads(raw_text)
    except json.JSONDecodeError as e:
        return {"error": {"message": str(e), "raw": raw_text[:500]}}


def call_coinlobster(tool_name, arguments=None):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": arguments or {}}
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "Authorization": f"Bearer {COINLOBSTER_API_KEY}"
    }
    try:
        response = requests.post(COINLOBSTER_URL, json=payload, headers=headers, timeout=TIMEOUT)
        return {
            "tool": tool_name,
            "http_status": response.status_code,
            "parsed": parse_sse(response.text)
        }
    except Exception as e:
        return {"tool": tool_name, "error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] CoinLobster Auth - {ts}")
    print(f"[YIN] API Key configurada: {'SI' if COINLOBSTER_API_KEY else 'NO'}")

    if not COINLOBSTER_API_KEY:
        print("[YIN] ERROR: No se encontro COINLOBSTER_API_KEY en .env")
        return

    # Ejecutar las 3 herramientas
    herramientas = [
        ("whale_radar", {"window": "4h"}),
        ("market_overview", {}),
        ("whale_trades", {"limit": 25})
    ]

    for tool_name, arguments in herramientas:
        print(f"[YIN] Ejecutando {tool_name}...")
        result = call_coinlobster(tool_name, arguments)

        out_path = ONCHAIN_DIR / f"{tool_name}_{ts}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"[YIN] Guardado: {out_path}")
        time.sleep(2)

    print("[YIN] Script 09g finalizado.")


if __name__ == "__main__":
    main()