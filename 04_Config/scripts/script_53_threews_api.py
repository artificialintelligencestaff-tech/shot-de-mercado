#!/usr/bin/env python3
"""
script_53_threews_api.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume la API publica de three.ws para lanzamientos pump.fun.
    Documentacion: https://three.ws/docs/api-reference
    Gratis, sin key. Rate limit: 20 req/min (unauth).
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

THREEWS_API = "https://three.ws/api/v1"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
THREEWS_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "pre_launch" / "threews"
THREEWS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0"}

ENDPOINTS = [
    {"name": "launches", "path": "/pump/launches", "params": {}},
    {"name": "trending", "path": "/pump/trending", "params": {}},
    {"name": "whales", "path": "/pump/whales", "params": {}},
]


def fetch_endpoint(name, path, params):
    try:
        r = requests.get(f"{THREEWS_API}{path}", params=params, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code == 429:
            return {"name": name, "error": "Rate limit exceeded (429)"}
        if r.status_code != 200:
            return {"name": name, "error": f"HTTP {r.status_code}", "preview": r.text[:300]}
        return {"name": name, "http_status": 200, "data": r.json()}
    except Exception as e:
        return {"name": name, "error": str(e)[:200]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] three.ws API - {ts}")

    resultados = []
    for ep in ENDPOINTS:
        print(f"[YIN] {ep['name']}...")
        r = fetch_endpoint(ep["name"], ep["path"], ep["params"])
        resultados.append(r)
        if "error" in r:
            print(f"[YIN]   ERROR: {r['error']}")
        else:
            data = r.get("data", {})
            count = len(data) if isinstance(data, list) else "?"
            print(f"[YIN]   OK | {count} items")

    out = {"timestamp": ts, "fase": "threews", "endpoints": resultados}
    out_path = THREEWS_DIR / f"threews_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()