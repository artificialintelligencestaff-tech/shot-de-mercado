#!/usr/bin/env python3
"""
script_37_alert_catwifout.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Enviar alerta a Telegram sobre Catwifout.
    Primera deteccion de OPORTUNIDAD REAL del sistema.
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
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        response = requests.post(TELEGRAM_URL, json=payload, timeout=TIMEOUT)
        return {"http_status": response.status_code, "body": response.text[:500]}
    except Exception as e:
        return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Alerta Catwifout - {ts}")

    mensaje = (
        f"ALERTA - PROYECTO SHOT DE MERCADO\n"
        f"Timestamp: {ts}\n\n"
        f"OPORTUNIDAD DETECTADA: CATWIFOUT\n\n"
        f"Token: Catwifout (Solana)\n"
        f"Address: 5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump\n"
        f"Verdict Deficlaw: STRONG BUY\n"
        f"Risk Score: 12/100 (LOW)\n\n"
        f"Datos clave:\n"
        f"- Market Cap: $1.15M\n"
        f"- Liquidez: $91.8K\n"
        f"- Top 5 holders: 5.8%\n"
        f"- Top 10 holders: 8.0%\n"
        f"- Buy pressure: 20.1:1\n"
        f"- Holders rentables: 99%\n"
        f"- Security: SAFE (mint/freeze revoked)\n\n"
        f"Contexto:\n"
        f"- 2h de vida\n"
        f"- Nuevo par en PumpSwap\n"
        f"- Infraestructura social presente (web + Twitter)\n\n"
        f"Score del sistema: 0.92 (OPORTUNIDAD)\n"
        f"Umbral: >0.75\n\n"
        f"Evaluacion complementaria requerida antes de decision de capital.\n"
        f"Fuente: Deficlaw analyze_token + get_token_security"
    )

    result = send_telegram(mensaje)
    print(f"[YIN] Resultado: {result}")

    # Guardar log
    log_dir = Path(r"D:\Proyecto Shot de mercado\03_Informes\alertas")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"alerta_catwifout_{ts}.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump({"mensaje": mensaje, "resultado": result, "timestamp": ts}, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Log guardado: {log_path}")


if __name__ == "__main__":
    main()