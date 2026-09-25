#!/usr/bin/env python3
"""
script_45b_volume_anomaly_v2.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Deteccion de volumen anomalo con umbrales realistas.
    Umbrales: >10x moderado, >20x fuerte, >30x extremo.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

DEXSCREENER_URL = "https://api.dexscreener.com/latest/dex/tokens"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
ANOMALY_DIR = PROJECT_ROOT / "02_Analisis" / "volume_anomaly"
ANOMALY_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 20

TOKENS = [
    {"symbol": "catwifout", "address": "5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump"},
]


def fetch_dex(address):
    try:
        r = requests.get(f"{DEXSCREENER_URL}/{address}", timeout=TIMEOUT)
        if r.status_code == 200:
            data = r.json()
            pairs = data.get("pairs", [])
            if pairs:
                return max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0))
        return None
    except Exception:
        return None


def detectar_anomalia(pair):
    if not pair:
        return {"error": "sin datos"}

    volume = float(pair.get("volume", {}).get("h24", 0) or 0)
    liquidity = float(pair.get("liquidity", {}).get("usd", 0) or 0)
    price_change = pair.get("priceChange", {})
    m5 = float(price_change.get("m5", 0) or 0)
    h1 = float(price_change.get("h1", 0) or 0)
    h6 = float(price_change.get("h6", 0) or 0)
    h24 = float(price_change.get("h24", 0) or 0)

    vol_liq_ratio = volume / liquidity if liquidity > 0 else 0

    # Umbrales REALISTAS
    if vol_liq_ratio > 30:
        nivel = "EXTREMO"
        anomalia = True
    elif vol_liq_ratio > 20:
        nivel = "FUERTE"
        anomalia = True
    elif vol_liq_ratio > 10:
        nivel = "MODERADO"
        anomalia = True
    else:
        nivel = "NORMAL"
        anomalia = False

    return {
        "vol_liq_ratio": round(vol_liq_ratio, 2),
        "price_change_5m": m5,
        "price_change_1h": h1,
        "price_change_6h": h6,
        "price_change_24h": h24,
        "nivel_anomalia": nivel,
        "anomalia_detectada": anomalia,
        "interpretacion": f"Actividad {nivel.lower()} - Vol/Liq {round(vol_liq_ratio, 1)}x"
    }


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Volume Anomaly v2 - {ts}")

    resultados = []
    for token in TOKENS:
        print(f"[YIN] {token['symbol']}...")
        pair = fetch_dex(token["address"])
        analisis = detectar_anomalia(pair)
        resultados.append({"symbol": token["symbol"], "address": token["address"], "analisis": analisis})
        print(f"[YIN]   Vol/Liq: {analisis.get('vol_liq_ratio')}x | Nivel: {analisis.get('nivel_anomalia')}")

    out = {"timestamp": ts, "fase": "volume_anomaly_v2", "tokens": resultados}
    out_path = ANOMALY_DIR / f"volume_anomaly_v2_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()