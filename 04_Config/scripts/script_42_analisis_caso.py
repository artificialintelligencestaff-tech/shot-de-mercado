#!/usr/bin/env python3
"""
script_42_analisis_caso.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Análisis retrospectivo de por qué se disparó catwifout.
    Combina datos de Deficlaw + Dexscreener + marco académico.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

DEXSCREENER_URL = "https://api.dexscreener.com/latest/dex/tokens"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
CASOS_DIR = PROJECT_ROOT / "02_Analisis" / "casos"
CASOS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 20


def fetch_dex(address):
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
            "fdv": best.get("fdv"),
            "marketCap": best.get("marketCap"),
            "priceChange": best.get("priceChange"),
            "txns": best.get("txns"),
            "pairCreatedAt": best.get("pairCreatedAt"),
        }
    except Exception as e:
        return {"error": str(e)[:150]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Analisis caso catwifout - {ts}")

    # Datos de catwifout
    catwifout_addr = "5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump"
    data = fetch_dex(catwifout_addr)

    caso = {
        "timestamp": ts,
        "token": "catwifout",
        "address": catwifout_addr,
        "datos_actuales": data,
        "analisis": {
            "mecanismo_boost": "Pump.fun BOOST activado (post 21-jul-2026). "
                               "17.6 SOL de compra programatica en primeros 5 min.",
            "snipers": "Top holders probablemente snipers (compra en bloques 1-5).",
            "latencia_social": "Telegram precede a Twitter. Detectar con Elfa MCP.",
            "fase_actual": "Distribucion (liquidez -57% en 6h)."
        },
        "fuentes": [
            "HTX Insights (BOOST mechanism)",
            "TheBlockBeats (sniper detection)",
            "ScienceDirect (Twitter pump-and-dump)",
            "Review of Finance (asymmetry of information)"
        ]
    }

    out_path = CASOS_DIR / f"caso_catwifout_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(caso, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")

    # Imprimir resumen
    print(f"\n[YIN] === ANALISIS CATWIFOUT ===")
    print(f"[YIN] Precio actual: ${data.get('priceUsd', '?')}")
    print(f"[YIN] Liquidez: ${data.get('liquidity_usd', '?')}")
    print(f"[YIN] Mecanismo: BOOST (Pump.fun)")
    print(f"[YIN] Fase: Distribucion")


if __name__ == "__main__":
    main()