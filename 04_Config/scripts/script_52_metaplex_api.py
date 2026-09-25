#!/usr/bin/env python3
"""
script_52_metaplex_api.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume la API publica de Metaplex Genesis para TGEs en Solana.
    Documentacion: https://www.metaplex.com/docs/smart-contracts/genesis/integration-apis
    Sin autenticacion. Rate limit: 429 si se excede.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

METAPLEX_API = "https://api.metaplex.com/v1"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
GENESIS_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "pre_launch" / "metaplex"
GENESIS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Endpoints conocidos (segun documentacion)
ENDPOINTS = [
    {"name": "launches_upcoming", "path": "/launches", "params": {"status": "upcoming"}},
    {"name": "launches_live", "path": "/launches", "params": {"status": "live"}},
    {"name": "launches_all", "path": "/launches", "params": {}},
]


def fetch_endpoint(name, path, params):
    try:
        r = requests.get(f"{METAPLEX_API}{path}", params=params, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code == 429:
            return {"name": name, "error": "Rate limit exceeded (429)"}
        if r.status_code != 200:
            return {"name": name, "error": f"HTTP {r.status_code}", "preview": r.text[:300]}
        data = r.json()
        return {"name": name, "http_status": 200, "data": data}
    except Exception as e:
        return {"name": name, "error": str(e)[:200]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Metaplex Genesis API - {ts}")

    resultados = []
    for ep in ENDPOINTS:
        print(f"[YIN] {ep['name']}...")
        r = fetch_endpoint(ep["name"], ep["path"], ep["params"])
        resultados.append(r)
        if "error" in r:
            print(f"[YIN]   ERROR: {r['error']}")
        else:
            data = r.get("data", {})
            # Intentar contar items
            count = 0
            if isinstance(data, list):
                count = len(data)
            elif isinstance(data, dict):
                for key in ["launches", "data", "items", "results"]:
                    if key in data and isinstance(data[key], list):
                        count = len(data[key])
                        break
            print(f"[YIN]   OK | {count} items")

    out = {"timestamp": ts, "fase": "metaplex_genesis", "endpoints": resultados}
    out_path = GENESIS_DIR / f"metaplex_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()