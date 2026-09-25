#!/usr/bin/env python3
"""
script_54_clawnch_api.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume la API publica de Clawnch para lanzamientos en Base.
    Documentacion: https://docs.base.org/agents/plugins/native/clawnch
    Gratis, sin key.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

CLAWNCH_API = "https://www.clawn.ch/api"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
CLAWNCH_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "pre_launch" / "clawnch"
CLAWNCH_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0"}

ENDPOINTS = [
    {"name": "launches", "path": "/launches", "params": {"limit": 50}},
    {"name": "top_volume", "path": "/tokens/top-volume", "params": {}},
]


def fetch_endpoint(name, path, params):
    try:
        r = requests.get(f"{CLAWNCH_API}{path}", params=params, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code != 200:
            return {"name": name, "error": f"HTTP {r.status_code}", "preview": r.text[:300]}
        return {"name": name, "http_status": 200, "data": r.json()}
    except Exception as e:
        return {"name": name, "error": str(e)[:200]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Clawnch API - {ts}")

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

    out = {"timestamp": ts, "fase": "clawnch", "endpoints": resultados}
    out_path = CLAWNCH_DIR / f"clawnch_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()