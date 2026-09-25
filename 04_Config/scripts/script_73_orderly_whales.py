#!/usr/bin/env python3
"""
script_73_orderly_whales.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume Orderly Public Info API (zero-auth).
    Whale tracking, PnL de addresses, market summary.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

ORDERLY_API = "https://api.orderly.org/v1/public/query"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
WHALE_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "whales"
WHALE_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30

# Queries disponibles
QUERIES = [
    {"name": "market_summary", "payload": {"type": "marketSummary"}},
    {"name": "rate_limit", "payload": {"type": "rateLimitStatus"}},
]


def call_orderly(payload):
    try:
        r = requests.post(ORDERLY_API, json=payload, timeout=TIMEOUT)
        if r.status_code == 200:
            return {"http_status": 200, "data": r.json()}
        return {"error": f"HTTP {r.status_code}", "preview": r.text[:200]}
    except Exception as e:
        return {"error": str(e)[:150]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Orderly Whales - {ts}")

    resultados = []
    for q in QUERIES:
        print(f"[YIN] {q['name']}...")
        r = call_orderly(q["payload"])
        resultados.append({"name": q["name"], "result": r})
        if "error" in r:
            print(f"[YIN]   ERROR: {r['error']}")
        else:
            print(f"[YIN]   OK")

    out = {"timestamp": ts, "fase": "orderly_whales", "results": resultados}
    out_path = WHALE_DIR / f"orderly_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()