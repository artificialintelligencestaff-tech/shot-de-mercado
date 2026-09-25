#!/usr/bin/env python3
"""
script_03_coingecko.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Extraer datos de mercado de CoinGecko API gratuita.
    Trending coins, global stats, top 20 coins.
    Sin API key.
"""

import json
import requests
import time
from datetime import datetime, timezone
from pathlib import Path

COINGECKO_BASE = "https://api.coingecko.com/api/v3"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
MERCADOS_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "mercados"
MERCADOS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30


def fetch(endpoint, params=None):
    try:
        url = f"{COINGECKO_BASE}{endpoint}"
        response = requests.get(url, params=params or {}, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"HTTP {response.status_code}", "body": response.text[:500]}
    except Exception as e:
        return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] CoinGecko - {ts}")

    result = {
        "timestamp": ts,
        "fase": "coingecko",
        "estado": "exito",
        "datos": {}
    }

    # 1. Ping
    print("[YIN] Ping...")
    result["datos"]["ping"] = fetch("/ping")
    time.sleep(2)

    # 2. Trending coins
    print("[YIN] Trending coins...")
    result["datos"]["trending"] = fetch("/search/trending")
    time.sleep(2)

    # 3. Global stats
    print("[YIN] Global stats...")
    result["datos"]["global"] = fetch("/global")
    time.sleep(2)

    # 4. Top 20 coins
    print("[YIN] Top 20 coins...")
    result["datos"]["top_20"] = fetch("/coins/markets", {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1,
        "sparkline": False,
        "price_change_percentage": "1h,24h,7d"
    })

    # Guardar
    out_path = MERCADOS_DIR / f"coingecko_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print("[YIN] Script 03 finalizado.")


if __name__ == "__main__":
    main()