#!/usr/bin/env python3
"""
script_38_price_tracker.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Registra el precio actual de los activos alertados para feedback loop.
    Fuente: Dexscreener API (gratuita, sin key).
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

DEXSCREENER_URL = "https://api.dexscreener.com/latest/dex/tokens"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
TRACKING_DIR = PROJECT_ROOT / "02_Analisis" / "tracking"
TRACKING_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 20

# Tokens alertados con direcciones
TOKENS_ALERTADOS = [
    {"name": "Catwifout", "address": "5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump", "alerta_ts": "2026-09-17_181616"},
    # Futuras alertas se añaden aqui
]


def check_price(address):
    """Consulta Dexscreener para un token."""
    try:
        url = f"{DEXSCREENER_URL}/{address}"
        response = requests.get(url, timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            pairs = data.get("pairs", [])
            if pairs:
                # Tomar el par con mayor liquidez
                best = max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0))
                return {
                    "priceUsd": best.get("priceUsd"),
                    "priceNative": best.get("priceNative"),
                    "liquidity_usd": best.get("liquidity", {}).get("usd"),
                    "volume_24h": best.get("volume", {}).get("h24"),
                    "fdv": best.get("fdv"),
                    "marketCap": best.get("marketCap"),
                    "dexId": best.get("dexId"),
                    "pairAddress": best.get("pairAddress")
                }
        return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)[:150]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Price Tracker - {ts}")

    resultados = []
    for token in TOKENS_ALERTADOS:
        print(f"[YIN] {token['name']}...")
        precio = check_price(token["address"])
        resultados.append({
            "name": token["name"],
            "address": token["address"],
            "alerta_ts": token["alerta_ts"],
            "check_ts": ts,
            "price_data": precio
        })

    out = {"timestamp": ts, "fase": "price_tracking", "tokens": resultados}
    out_path = TRACKING_DIR / f"price_tracking_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()