#!/usr/bin/env python3
"""
script_74_funding_anomaly.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Detecta anomalias en funding rates de Orderly.
    Funding >0.03% = sobreextension (senal de movimiento inminente).
"""

import json
import glob
import requests
from datetime import datetime, timezone
from pathlib import Path

ORDERLY_API = "https://api.orderly.org/v1/public/query"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
ANOMALY_DIR = PROJECT_ROOT / "02_Analisis" / "funding_anomaly"
ANOMALY_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
FUNDING_THRESHOLD = 0.03


def fetch_market_summary():
    try:
        r = requests.post(ORDERLY_API, json={"type": "marketSummary"}, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Funding Anomaly - {ts}")

    data = fetch_market_summary()
    if not data:
        print("[YIN] ERROR: sin datos de Orderly")
        return

    rows = data.get("data", {}).get("rows", [])
    print(f"[YIN] Mercados analizados: {len(rows)}")

    anomalias = []
    normales = []

    for m in rows:
        symbol = m.get("symbol", "?")
        funding = float(m.get("funding_rate", 0) or 0) * 100  # a %
        oi = float(m.get("open_interest", 0) or 0)
        mark = float(m.get("mark_price", 0) or 0)

        entry = {
            "symbol": symbol,
            "funding_rate_pct": round(funding, 4),
            "open_interest": oi,
            "mark_price": mark,
            "vol_24h": float(m.get("24h_volume", 0) or 0)
        }

        if abs(funding) > FUNDING_THRESHOLD:
            anomalias.append(entry)
        else:
            normales.append(entry)

    anomalias.sort(key=lambda x: abs(x["funding_rate_pct"]), reverse=True)

    out = {
        "timestamp": ts,
        "fase": "funding_anomaly",
        "threshold_pct": FUNDING_THRESHOLD,
        "total_mercados": len(rows),
        "total_anomalias": len(anomalias),
        "anomalias": anomalias,
        "normales_muestra": normales[:20]
    }

    out_path = ANOMALY_DIR / f"funding_anomaly_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print(f"[YIN] Anomalias detectadas: {len(anomalias)}")

    for a in anomalias[:10]:
        print(f"[YIN]   {a['symbol']:25} | Funding {a['funding_rate_pct']:+.4f}% | OI ${a['open_interest']:,.0f}")


if __name__ == "__main__":
    main()