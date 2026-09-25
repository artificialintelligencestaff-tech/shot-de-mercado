#!/usr/bin/env python3
"""
script_66_crypto_early_radar.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Implementa el scoring de CryptoEarlyRadar (MoltStreet).
    6 señales ponderadas, score 0-100.
    Fuente: github.com/Lolarok/crypto-early-radar
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
RADAR_DIR = PROJECT_ROOT / "02_Analisis" / "early_radar"
RADAR_DIR.mkdir(parents=True, exist_ok=True)

COINGECKO_BASE = "https://api.coingecko.com/api/v3"
TIMEOUT = 30

# Tokens a analizar (se pueden cargar desde otro script)
TOKENS = ["solana", "arbitrum", "optimism", "sui", "aptos", "render-token"]


def fetch_coingecko(coin_id):
    try:
        r = requests.get(f"{COINGECKO_BASE}/coins/{coin_id}", params={
            "localization": False, "tickers": False, "market_data": True,
            "community_data": False, "developer_data": True, "sparkline": False
        }, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None


def fetch_fear_greed():
    try:
        r = requests.get("https://api.alternative.me/fng/", timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None


def calcular_score(data, fng_data):
    """Score 0-100 con 6 señales (CryptoEarlyRadar methodology)."""
    if not data or "market_data" not in data:
        return None

    market = data["market_data"]
    score = 0
    detalle = {}

    # 1. ATH Discount (25 pts)
    ath = market.get("ath", {}).get("usd", 1)
    precio = market.get("current_price", {}).get("usd", 0)
    ath_discount = (precio / ath) * 100 if ath > 0 else 100
    if ath_discount < 20: score += 25; detalle["ath_discount"] = 25
    elif ath_discount < 40: score += 18; detalle["ath_discount"] = 18
    elif ath_discount < 60: score += 10; detalle["ath_discount"] = 10
    else: detalle["ath_discount"] = 0

    # 2. Volume Momentum (20 pts)
    vol_24h = market.get("total_volume", {}).get("usd", 0)
    vol_7d_avg = vol_24h  # simplificado
    if vol_24h > 1000000: score += 20; detalle["volume"] = 20
    elif vol_24h > 100000: score += 12; detalle["volume"] = 12
    else: detalle["volume"] = 5

    # 3. Price 7d (15 pts)
    pct_7d = market.get("price_change_percentage_7d", 0) or 0
    if pct_7d > 20: score += 15; detalle["price_7d"] = 15
    elif pct_7d > 5: score += 10; detalle["price_7d"] = 10
    elif pct_7d > -10: score += 5; detalle["price_7d"] = 5
    else: detalle["price_7d"] = 0

    # 4. Fear/Greed (15 pts) - contrarian
    if fng_data and "data" in fng_data:
        fng = int(fng_data["data"][0]["value"])
        if fng < 20: score += 15; detalle["fear_greed"] = 15
        elif fng < 40: score += 10; detalle["fear_greed"] = 10
        elif fng < 60: score += 5; detalle["fear_greed"] = 5
        else: detalle["fear_greed"] = 0

    # 5. GitHub Activity (15 pts)
    dev = data.get("developer_data", {})
    commits_4w = dev.get("commit_count_4_weeks", 0) or 0
    if commits_4w > 50: score += 15; detalle["github"] = 15
    elif commits_4w > 10: score += 10; detalle["github"] = 10
    else: detalle["github"] = 5

    # 6. MCap Upside (10 pts) - small cap = asymmetric
    mcap = market.get("market_cap", {}).get("usd", 0)
    if mcap < 50000000: score += 10; detalle["mcap_upside"] = 10
    elif mcap < 500000000: score += 7; detalle["mcap_upside"] = 7
    else: detalle["mcap_upside"] = 3

    return {"score": min(score, 100), "detalle": detalle}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Crypto Early Radar - {ts}")

    fng = fetch_fear_greed()
    resultados = []

    for token in TOKENS:
        print(f"[YIN] {token}...")
        data = fetch_coingecko(token)
        if not data:
            print(f"[YIN]   SKIP: sin datos")
            continue

        score_data = calcular_score(data, fng)
        if not score_data:
            continue

        symbol = data.get("symbol", "?").upper()
        nombre = data.get("name", "?")
        precio = data.get("market_data", {}).get("current_price", {}).get("usd", 0)
        mcap = data.get("market_data", {}).get("market_cap", {}).get("usd", 0)

        nivel = "ALERT" if score_data["score"] >= 65 else "WATCH" if score_data["score"] >= 50 else "HOLD"
        print(f"[YIN]   {symbol}: Score {score_data['score']}/100 ({nivel})")

        resultados.append({
            "coin_id": token, "symbol": symbol, "name": nombre,
            "precio": precio, "market_cap": mcap,
            "score": score_data["score"], "nivel": nivel,
            "detalle": score_data["detalle"]
        })

    resultados.sort(key=lambda x: x["score"], reverse=True)

    out = {
        "timestamp": ts, "fase": "early_radar",
        "fear_greed": fng.get("data", [{}])[0].get("value") if fng else None,
        "total": len(resultados), "tokens": resultados
    }

    out_path = RADAR_DIR / f"early_radar_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\n[YIN] Guardado: {out_path}")

    print(f"\n[YIN] === RANKING ===")
    for r in resultados:
        print(f"[YIN] {r['symbol']:10} | Score {r['score']:3} | {r['nivel']}")


if __name__ == "__main__":
    main()