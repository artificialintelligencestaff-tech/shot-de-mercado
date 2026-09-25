#!/usr/bin/env python3
"""
script_70_news_aggregator.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume cryptocurrency.cv API (300+ fuentes, x402 micropagos).
    Breaking news + sentiment AI + narratives.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

NEWS_API = "https://cryptocurrency.cv/api/v1"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
NEWS_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "news"
NEWS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Endpoints gratuitos (sin x402)
ENDPOINTS = [
    {"name": "news", "path": "/news"},
    {"name": "breaking", "path": "/breaking"},
    {"name": "trending", "path": "/trending"},
    {"name": "fear_greed", "path": "/fear-greed"},
]


def fetch_endpoint(name, path):
    try:
        r = requests.get(f"{NEWS_API}{path}", headers=HEADERS, timeout=TIMEOUT)
        if r.status_code == 200:
            return {"name": name, "http_status": 200, "data": r.json()}
        return {"name": name, "error": f"HTTP {r.status_code}", "preview": r.text[:200]}
    except Exception as e:
        return {"name": name, "error": str(e)[:150]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] News Aggregator - {ts}")

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

    out = {"timestamp": ts, "fase": "news_aggregator", "endpoints": resultados}
    out_path = NEWS_DIR / f"news_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()