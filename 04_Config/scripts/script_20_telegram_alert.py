#!/usr/bin/env python3
"""
script_20_telegram_alert.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Enviar alertas a Telegram. Lee credenciales desde .env en ruta absoluta.
"""

import json
import os
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path(r"D:\Proyecto Shot de mercado\04_Config\.env")
load_dotenv(ENV_PATH)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

TIMEOUT = 30


def send_telegram(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return {"error": "Credenciales no configuradas"}
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        response = requests.post(TELEGRAM_URL, json=payload, timeout=TIMEOUT)
        return {"http_status": response.status_code, "body": response.text[:500]}
    except Exception as e:
        return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Telegram Alert - {ts}")
    print(f"[YIN] ENV path: {ENV_PATH}")
    print(f"[YIN] ENV existe: {ENV_PATH.exists()}")
    print(f"[YIN] Token presente: {'SI' if TELEGRAM_TOKEN else 'NO'}")
    print(f"[YIN] Chat ID presente: {'SI' if TELEGRAM_CHAT_ID else 'NO'}")

    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("[YIN] ERROR: Credenciales faltantes")
        return

    mensaje = f"""PROYECTO SHOT DE MERCADO

Sistema operativo.
Timestamp: {ts}

Fuentes activas:
- CoinGecko
- CoinLobster
- Deep Blue Alpha
- Alpha MCP
- Coinfuty
- ApeWisdom
- NarrativeScope

Esperando predicciones positivas (score > 0.65)."""

    result = send_telegram(mensaje)
    print(f"[YIN] Resultado: {result}")

    log_dir = Path(r"D:\Proyecto Shot de mercado\03_Informes\telegram")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"telegram_test_{ts}.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump({"mensaje": mensaje, "resultado": result, "timestamp": ts}, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Log guardado: {log_path}")


if __name__ == "__main__":
    main()