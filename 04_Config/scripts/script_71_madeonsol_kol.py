#!/usr/bin/env python3
"""
script_71_madeonsol_kol.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume MadeOnSol API (KOL tracking, deployer intel, surge detection).
    Free tier: 200 req/dia, sin signup.
"""

import json
import os
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path(r"D:\Proyecto Shot de Mercado\04_Config\.env")
load_dotenv(ENV_PATH)

MADEONSOL_KEY = os.getenv("MADEONSOL_API_KEY", "")
MADEONSOL_BASE = "https://madeonsol.com/api/v1"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
KOL_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "kol_tracking"
KOL_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0"}
if MADEONSOL_KEY:
    HEADERS["Authorization"] = f"Bearer {MADEONSOL_KEY}"

ENDPOINTS = [
    {"name": "kol_trades", "path": "/kol/trades"},
    {"name": "deployer_scores", "path": "/deployer/scores"},
    {"name": "surge_detection", "path": "/tokens/surges"},
]


def fetch_endpoint(name, path):
    try:
        r = requests.get(f"{MADEONSOL_BASE}{path}", headers=HEADERS, timeout=TIMEOUT)
        if r.status_code == 200:
            return {"name": name, "http_status": 200, "data": r.json()}
        return {"name": name, "error": f"HTTP {r.status_code}", "preview": r.text[:200]}
    except Exception as e:
        return {"name": name, "error": str(e)[:150]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] MadeOnSol KOL - {ts}")
    print(f"[YIN] API key: {'SI' if MADEONSOL_KEY else 'NO'}")

    if not MADEONSOL_KEY:
        print("[YIN] ADVERTENCIA: Sin API key. Free tier no requiere signup, pero puede tener limites.")
        print("[YIN] Solicitar en madeonsol.com/developer")

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

    out = {"timestamp": ts, "fase": "madeonsol_kol", "endpoints": resultados}
    out_path = KOL_DIR / f"kol_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()