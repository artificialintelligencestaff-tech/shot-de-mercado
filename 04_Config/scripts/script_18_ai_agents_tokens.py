#!/usr/bin/env python3
"""
script_18_ai_agents_tokens.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Verificar tokens asociados a la narrativa AI agents crypto.
    Narrativa #1 segun NarrativeScope (490 repos en 90d).
"""

import json
import requests
import time
from datetime import datetime, timezone
from pathlib import Path

COINGECKO_BASE = "https://api.coingecko.com/api/v3"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
NARRATIVAS_DIR = PROJECT_ROOT / "02_Analisis" / "narrativas"
NARRATIVAS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30

# Tokens candidatos de la narrativa AI agents
AI_AGENTS_TOKENS = [
    "fetch-ai", "singularitynet", "ocean-protocol", "render-token",
    "bittensor", "akash-network", "nosana", "phala-network",
    "graphlinq-protocol", "covalent"
]


def fetch(endpoint, params=None):
    try:
        url = f"{COINGECKO_BASE}{endpoint}"
        response = requests.get(url, params=params or {}, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] AI Agents Tokens - {ts}")

    result = {
        "timestamp": ts,
        "fase": "ai_agents_tokens",
        "estado": "exito",
        "tokens": []
    }

    for token_id in AI_AGENTS_TOKENS:
        print(f"[YIN] Analizando {token_id}...")
        data = fetch(f"/coins/{token_id}", {
            "localization": False,
            "tickers": False,
            "market_data": True,
            "sparkline": False
        })

        if "error" in data:
            result["tokens"].append({"id": token_id, "error": data["error"]})
            continue

        market = data.get("market_data", {})
        entry = {
            "id": token_id,
            "symbol": data.get("symbol"),
            "name": data.get("name"),
            "price_usd": market.get("current_price", {}).get("usd"),
            "change_24h": market.get("price_change_percentage_24h"),
            "change_7d": market.get("price_change_percentage_7d"),
            "change_30d": market.get("price_change_percentage_30d"),
            "market_cap": market.get("market_cap", {}).get("usd"),
            "volume_24h": market.get("total_volume", {}).get("usd"),
            "categories": data.get("categories", [])[:5],
            "etiqueta": "DATO VERIFICADO"
        }
        result["tokens"].append(entry)
        time.sleep(3)

    # Filtrar tokens con aceleración >20%
    result["aceleraciones"] = [
        t for t in result["tokens"]
        if isinstance(t.get("change_24h"), (int, float)) and t["change_24h"] >= 20
    ]

    # Guardar
    out_path = NARRATIVAS_DIR / f"ai_agents_tokens_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print(f"[YIN] Tokens con aceleracion >20%: {len(result['aceleraciones'])}")
    print("[YIN] Script 18 finalizado.")


if __name__ == "__main__":
    main()