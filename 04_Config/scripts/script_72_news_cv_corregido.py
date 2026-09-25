#!/usr/bin/env python3
"""
script_72_news_cv_corregido.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Version corregida. Usa endpoints GRATUITOS de cryptocurrency.cv.
    Endpoints premium (x402) NO se usan.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

NEWS_API = "https://cryptocurrency.cv/api"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
NEWS_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "news"
NEWS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30

# Endpoints GRATUITOS (sin x402)
ENDPOINTS = [
    {"name": "news", "path": "/news"},
    {"name": "bitcoin", "path": "/bitcoin"},
    {"name": "defi", "path": "/defi"},
    {"name": "breaking", "path": "/breaking"},
    {"name": "health", "path": "/health"},
    {"name": "sources", "path": "/sources"},
]


def fetch_endpoint(name, path):
    try:
        r = requests.get(f"{NEWS_API}{path}", timeout=TIMEOUT)
        if r.status_code == 200:
            return {"name": name, "http_status": 200, "data": r.json()}
        return {"name": name, "error": f"HTTP {r.status_code}", "preview": r.text[:200]}
    except Exception as e:
        return {"name": name, "error": str(e)[:150]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] News cv (corregido) - {ts}")

    resultados = []
    for ep in ENDPOINTS:
        print(f"[YIN] {ep['name']}...")
        r = fetch_endpoint(ep["name"], ep["path"])
        resultados.append(r)
        if "error" in r:
            print(f"[YIN]   ERROR: {r['error']}")
        else:
            data = r.get("data", {})
            if isinstance(data, list):
                print(f"[YIN]   OK | {len(data)} items")
            elif isinstance(data, dict):
                count = len(data.get("articles", data.get("news", [])))
                print(f"[YIN]   OK | {count} items")

    out = {"timestamp": ts, "fase": "news_cv_corregido", "endpoints": resultados}
    out_path = NEWS_DIR / f"news_cv_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()