#!/usr/bin/env python3
"""
script_51_api_direct_launches.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume APIs directas (JSON) de lanzamientos sin scraping.
    Fuentes: Metaplex Genesis, three.ws, Clawnch (Base).
    Todas gratuitas, sin autenticacion.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
API_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "api_launches"
API_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0"}

APIS = [
    {
        "name": "metaplex_genesis",
        "url": "https://api.metaplex.com/v1/launches",
        "params": {"status": "upcoming"},
        "chain": "solana"
    },
    {
        "name": "metaplex_live",
        "url": "https://api.metaplex.com/v1/launches",
        "params": {"status": "live"},
        "chain": "solana"
    },
    {
        "name": "three_ws_launches",
        "url": "https://three.ws/api/v1/pump/launches",
        "params": {},
        "chain": "solana"
    },
    {
        "name": "clawnch_base",
        "url": "https://www.clawn.ch/api/launches",
        "params": {"limit": 50},
        "chain": "base"
    },
]


def fetch_api(name, url, params, chain):
    try:
        r = requests.get(url, params=params, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code != 200:
            return {"name": name, "error": f"HTTP {r.status_code}", "preview": r.text[:200]}
        data = r.json()
        return {
            "name": name,
            "chain": chain,
            "http_status": 200,
            "data_type": type(data).__name__,
            "preview": str(data)[:500],
            "data": data
        }
    except Exception as e:
        return {"name": name, "error": str(e)[:200]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] API Direct Launches - {ts}")

    resultados = []
    for api in APIS:
        print(f"[YIN] {api['name']}...")
        r = fetch_api(api["name"], api["url"], api["params"], api["chain"])
        resultados.append(r)
        if "error" in r:
            print(f"[YIN]   ERROR: {r['error']}")
        else:
            print(f"[YIN]   OK | {r.get('data_type')}")

    out = {
        "timestamp": ts,
        "fase": "api_direct_launches",
        "fuentes": resultados
    }

    out_path = API_DIR / f"api_launches_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()