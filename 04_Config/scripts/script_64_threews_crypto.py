#!/usr/bin/env python3
"""
script_64_threews_crypto.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume three.ws Crypto Data API (11 endpoints, keyless).
    Incluye: portfolio, airdrop eligibility, narrativas, trending.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

THREEWS_BASE = "https://three.ws/api"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
THREEWS_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "api_launches" / "threews_crypto"
THREEWS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
ENDPOINTS = [
    {"name": "airdrops", "path": "/crypto/airdrops"},
    {"name": "portfolio", "path": "/crypto/portfolio"},
    {"name": "trending", "path": "/crypto/trending"},
]


def fetch_endpoint(name, path):
    try:
        r = requests.get(f"{THREEWS_BASE}{path}", timeout=TIMEOUT)
        if r.status_code != 200:
            return {"name": name, "error": f"HTTP {r.status_code}"}
        return {"name": name, "http_status": 200, "data": r.json()}
    except Exception as e:
        return {"name": name, "error": str(e)[:150]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] three.ws Crypto API - {ts}")

    resultados = []
    for ep in ENDPOINTS:
        print(f"[YIN] {ep['name']}...")
        r = fetch_endpoint(ep["name"], ep["path"])
        resultados.append(r)
        if "error" in r:
            print(f"[YIN]   ERROR: {r['error']}")
        else:
            data = r.get("data", {})
            count = len(data) if isinstance(data, list) else "?"
            print(f"[YIN]   OK | {count} items")

    out = {"timestamp": ts, "fase": "threews_crypto", "endpoints": resultados}
    out_path = THREEWS_DIR / f"threews_crypto_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()