#!/usr/bin/env python3
"""
script_38b_tracking_degradacion.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Tracking de precios + alerta automatica cuando
    la liquidez cae mas de 30% desde el pico registrado.
"""

import json
import os
import glob
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path(r"D:\Proyecto Shot de Mercado\04_Config\.env")
load_dotenv(ENV_PATH)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

DEXSCREENER_URL = "https://api.dexscreener.com/latest/dex/tokens"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
TRACKING_DIR = PROJECT_ROOT / "02_Analisis" / "tracking"
TRACKING_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 20

# Tokens en tracking
TOKENS = [
    {"name": "Catwifout", "address": "5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump", "peak_liq": 91800, "peak_mcap": 1150000}
]


def send_telegram(text):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return {"error": "sin credenciales"}
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    try:
        r = requests.post(TELEGRAM_URL, json=payload, timeout=TIMEOUT)
        return {"status": r.status_code}
    except Exception as e:
        return {"error": str(e)[:100]}


def check_dex(address):
    try:
        r = requests.get(f"{DEXSCREENER_URL}/{address}", timeout=TIMEOUT)
        if r.status_code != 200:
            return {"error": f"HTTP {r.status_code}"}
        data = r.json()
        pairs = data.get("pairs", [])
        if not pairs:
            return {"error": "no pairs"}
        best = max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0))
        return {
            "priceUsd": best.get("priceUsd"),
            "liquidity_usd": best.get("liquidity", {}).get("usd"),
            "volume_24h": best.get("volume", {}).get("h24"),
            "marketCap": best.get("marketCap"),
            "fdv": best.get("fdv"),
        }
    except Exception as e:
        return {"error": str(e)[:100]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Tracking con degradacion - {ts}")

    resultados = []
    alertas = []

    for token in TOKENS:
        print(f"[YIN] {token['name']}...")
        data = check_dex(token["address"])

        if "error" in data:
            resultados.append({"name": token["name"], "error": data["error"]})
            continue

        liq_actual = float(data.get("liquidity_usd", 0) or 0)
        mcap_actual = float(data.get("marketCap", 0) or 0)
        peak_liq = token.get("peak_liq", 0)
        peak_mcap = token.get("peak_mcap", 0)

        # Calcular cambio desde pico
        cambio_liq = ((liq_actual - peak_liq) / peak_liq * 100) if peak_liq else 0
        cambio_mcap = ((mcap_actual - peak_mcap) / peak_mcap * 100) if peak_mcap else 0

        entry = {
            "name": token["name"],
            "address": token["address"],
            "check_ts": ts,
            "priceUsd": data.get("priceUsd"),
            "liquidity_usd": liq_actual,
            "marketCap": mcap_actual,
            "volume_24h": data.get("volume_24h"),
            "peak_liq": peak_liq,
            "peak_mcap": peak_mcap,
            "cambio_liq_pct": round(cambio_liq, 2),
            "cambio_mcap_pct": round(cambio_mcap, 2)
        }
        resultados.append(entry)

        # Verificar si hay degradacion critica
        if cambio_liq < -30:
            alerta = (
                f"🚨 ALERTA DE DEGRADACION\n"
                f"Proyecto Shot de Mercado\n\n"
                f"Token: {token['name']}\n\n"
                f"📉 LIQUIDEZ CAYO {cambio_liq:.1f}%\n"
                f"   Pico: ${peak_liq:,.0f}\n"
                f"   Actual: ${liq_actual:,.0f}\n\n"
                f"📉 Market Cap: {cambio_mcap:.1f}%\n"
                f"   Pico: ${peak_mcap:,.0f}\n"
                f"   Actual: ${mcap_actual:,.0f}\n\n"
                f"⚠️ Posible rug pull en curso.\n"
                f"⚠️ Los proveedores de liquidez estan\n"
                f"   retirando capital.\n\n"
                f"ACCION RECOMENDADA:\n"
                f"- NO comprar mas\n"
                f"- Considerar salida si estas dentro\n"
                f"- Verificar en Dexscreener:\n"
                f"  https://dexscreener.com/solana/{token['address']}"
            )
            alertas.append(alerta)
            print(f"[YIN] 🚨 DEGRADACION DETECTADA: {token['name']}")

    # Guardar log
    out = {"timestamp": ts, "fase": "tracking_degradacion", "tokens": resultados, "alertas": alertas}
    out_path = TRACKING_DIR / f"tracking_degradacion_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")

    # Enviar alertas si corresponde
    for alerta in alertas:
        print(f"[YIN] Enviando alerta a Telegram...")
        result = send_telegram(alerta)
        print(f"[YIN] Resultado: {result}")

    print(f"[YIN] Total alertas: {len(alertas)}")


if __name__ == "__main__":
    main()