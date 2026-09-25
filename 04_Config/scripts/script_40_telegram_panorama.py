#!/usr/bin/env python3
"""
script_40_telegram_panorama.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Envia panorama multi-activo a Telegram.
    Ranking de tokens + porcentaje de confianza.
"""

import json
import os
import glob
import time
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path(r"D:\Proyecto Shot de Mercado\04_Config\.env")
load_dotenv(ENV_PATH)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
PANORAMA_DIR = PROJECT_ROOT / "02_Analisis" / "panorama"
TIMEOUT = 30


def send_message(text):
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    try:
        r = requests.post(TELEGRAM_URL, json=payload, timeout=TIMEOUT)
        return {"status": r.status_code}
    except Exception as e:
        return {"error": str(e)[:100]}


def leer_ultimo_panorama():
    archivos = sorted(glob.glob(str(PANORAMA_DIR / "panorama_*.json")), reverse=True)
    if not archivos:
        return None
    with open(archivos[0], "r", encoding="utf-8") as f:
        return json.load(f)


def construir_mensaje_panorama(data, ts):
    """Construye el mensaje de panorama general."""
    ranking = data.get("ranking", [])

    msg = f"""📊 PANORAMA DE MERCADO
Proyecto Shot de Mercado
{ts}

━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 RANKING DE OPORTUNIDADES
━━━━━━━━━━━━━━━━━━━━━━━━━━

Total analizados: {len(ranking)}

"""

    for i, t in enumerate(ranking[:10], 1):  # Top 10
        emoji = "🟢" if t["score"] >= 75 else "🟡" if t["score"] >= 50 else "🔴"
        msg += f"""{emoji} {i}. {t['name']}
   Score: {t['score']}/100
   Confianza: {t['confianza']}%
   Fuente: {t['fuente']}
   
"""

    msg += """━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 LEYENDA
━━━━━━━━━━━━━━━━━━━━━━━━━━

🟢 Score ≥ 75 = OPORTUNIDAD
🟡 Score 50-74 = VIGILAR
🔴 Score < 50 = DESCARTAR

Confianza = % estimado de que el analisis
sea correcto basado en los criterios aplicados.

━━━━━━━━━━━━━━━━━━━━━━━━━━

Detalles individuales en mensajes siguientes.
"""

    return msg


def construir_mensaje_detalle(token, idx, total):
    """Construye mensaje detallado por token."""
    criterios = token.get("criterios", {})

    msg = f"""📋 DETALLE [{idx}/{total}]
Token: {token['name']}

━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 SCORE: {token['score']}/100
🎯 CONFIANZA: {token['confianza']}%
━━━━━━━━━━━━━━━━━━━━━━━━━━

CRITERIOS:
• Distribucion: {criterios.get('distribucion', 0)}/20
• Risk Score: {criterios.get('risk', 0)}/20
• Verdict: {criterios.get('verdict', 0)}/20
• Buy Pressure: {criterios.get('buy_pressure', 0)}/20
• Base: {criterios.get('base', 0)}/20

Direccion: {token['address'][:20]}...

Fuente: {token['fuente']}
"""

    if token.get("error"):
        msg += f"\n⚠️ ERROR: {token['error'][:100]}\n"

    return msg


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Telegram Panorama - {ts}")

    data = leer_ultimo_panorama()
    if not data:
        print("[YIN] ERROR: No hay panorama generado")
        return

    ranking = data.get("ranking", [])
    print(f"[YIN] Enviando panorama de {len(ranking)} tokens...")

    # 1. Mensaje de panorama general
    msg_panorama = construir_mensaje_panorama(data, ts)
    print(f"[YIN]   Panorama general ({len(msg_panorama)} chars)...")
    r1 = send_message(msg_panorama)
    print(f"[YIN]   Resultado: {r1}")
    time.sleep(1.5)

    # 2. Detalles de top 5
    top5 = ranking[:5]
    for i, token in enumerate(top5, 1):
        msg_detalle = construir_mensaje_detalle(token, i, len(top5))
        print(f"[YIN]   Detalle {i}/5: {token['name']} ({len(msg_detalle)} chars)...")
        r = send_message(msg_detalle)
        print(f"[YIN]   Resultado: {r}")
        time.sleep(1.5)

    # Guardar log
    log_dir = PROJECT_ROOT / "03_Informes" / "alertas"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"panorama_telegram_{ts}.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": ts,
            "total_tokens": len(ranking),
            "mensajes_enviados": 1 + len(top5)
        }, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Log guardado: {log_path}")
    print(f"[YIN] Total mensajes: {1 + len(top5)}")


if __name__ == "__main__":
    main()