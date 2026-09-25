#!/usr/bin/env python3
"""
script_44_holder_analysis.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Analisis de distribucion de holders para detectar bundling y concentracion.
    Usa Dexscreener + Solscan API (gratuita).
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

SOLSCAN_API = "https://public-api.solscan.io"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
HOLDERS_DIR = PROJECT_ROOT / "02_Analisis" / "holder_analysis"
HOLDERS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 20

TOKENS = [
    {"symbol": "catwifout", "address": "5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump"},
]


def get_token_holders(address):
    """Obtiene los top holders de un token via Solscan."""
    try:
        url = f"{SOLSCAN_API}/token/holders"
        params = {"tokenAddress": address, "offset": 0, "limit": 20}
        r = requests.get(url, params=params, timeout=TIMEOUT)
        if r.status_code == 200:
            return r.json()
        return {"error": f"HTTP {r.status_code}"}
    except Exception as e:
        return {"error": str(e)[:150]}


def analizar_distribucion(holders_data):
    """Analiza la distribucion de holders."""
    if "error" in holders_data or "data" not in holders_data:
        return {"error": "sin datos"}

    holders = holders_data.get("data", [])
    if not holders:
        return {"error": "sin holders"}

    total_supply = 1_000_000_000  # Aproximado

    top1 = holders[0].get("amount", 0) / total_supply * 100 if holders else 0
    top5 = sum(h.get("amount", 0) for h in holders[:5]) / total_supply * 100
    top10 = sum(h.get("amount", 0) for h in holders[:10]) / total_supply * 100

    return {
        "top1_pct": round(top1, 2),
        "top5_pct": round(top5, 2),
        "top10_pct": round(top10, 2),
        "total_holders": len(holders),
        "riesgo": "ALTO" if top10 > 50 else "MEDIO" if top10 > 30 else "BAJO"
    }


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Analisis de holders - {ts}")

    resultados = []
    for token in TOKENS:
        print(f"[YIN] {token['symbol']}...")
        holders = get_token_holders(token["address"])
        analisis = analizar_distribucion(holders)

        entry = {
            "symbol": token["symbol"],
            "address": token["address"],
            "analisis": analisis,
            "top_holders": holders.get("data", [])[:10] if isinstance(holders, dict) else []
        }
        resultados.append(entry)
        print(f"[YIN]   Top 10: {analisis.get('top10_pct', '?')}% | Riesgo: {analisis.get('riesgo', '?')}")

    out = {"timestamp": ts, "fase": "holder_analysis", "tokens": resultados}
    out_path = HOLDERS_DIR / f"holder_analysis_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()