#!/usr/bin/env python3
"""
script_10_santiment.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Obtener sentimiento social de Santiment MCP.
    Usa API key gratuita (1,000 llamadas).
    Herramientas: get_sentiment_balance, get_social_volume, get_trending_words.
"""

import json
import os
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

# Cargar .env
load_dotenv(Path(r"D:\Proyecto Shot de mercado\04_Config\.env"))

SANTIMENT_API_KEY = os.getenv("SANTIMENT_API_KEY", "")
SANTIMENT_MCP_URL = "https://mcp.santiment.net/mcp"  # Endpoint MCP oficial
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
SOCIAL_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "social" / "santiment"
SOCIAL_DIR.mkdir(parents=True, exist_ok=True)

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


def call_santiment(tool_name, arguments=None):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": arguments or {}}
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "Authorization": f"Bearer {SANTIMENT_API_KEY}"
    }
    try:
        response = requests.post(SANTIMENT_MCP_URL, json=payload, headers=headers, timeout=TIMEOUT)
        return {
            "tool": tool_name,
            "http_status": response.status_code,
            "parsed": parse_sse(response.text)
        }
    except Exception as e:
        return {"tool": tool_name, "error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Santiment MCP - {ts}")

    if not SANTIMENT_API_KEY:
        print("[YIN] ERROR: No se encontro SANTIMENT_API_KEY en .env")
        return

    # Herramientas de Santiment
    herramientas = [
        ("get_sentiment_balance", {"asset": "BTC"}),
        ("get_social_volume", {"asset": "BTC", "hours": 24}),
        ("get_trending_words", {}),
    ]

    for tool_name, arguments in herramientas:
        print(f"[YIN] Ejecutando {tool_name}...")
        result = call_santiment(tool_name, arguments)

        out_path = SOCIAL_DIR / f"{tool_name}_{ts}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"[YIN] Guardado: {out_path}")

    print("[YIN] Script 10 finalizado.")


if __name__ == "__main__":
    main()