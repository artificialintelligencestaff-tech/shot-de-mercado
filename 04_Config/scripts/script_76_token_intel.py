#!/usr/bin/env python3
"""
script_76_token_intel.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Endpoint de inteligencia completa de token: /v1/token/{mint}
    Devuelve price, market cap, deployer reputation, KOL activity.
    Disponible en todos los tiers (BASIC incluido).
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
TOKEN_DIR = PROJECT_ROOT / "02_Analisis" / "token_intel"
TOKEN_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0", "Authorization": f"Bearer {MADEONSOL_KEY}"}

# Mints de ejemplo (reemplazar con tokens reales)
TOKENS = [
    "26s2aYqxAJ3JFeHqqV8i94m8EkH4XzCakMTaYbPQpump",  # ejemplo del blog
]


def fetch_token_intel(mint):
    try:
        r = requests.get(f"{MADEONSOL_BASE}/token/{mint}", headers=HEADERS, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else {"error": f"HTTP {r.status_code}", "preview": r.text[:300]}
    except Exception as e:
        return {"error": str(e)[:150]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Token Intel - {ts}")
    print(f"[YIN] API key: {'SI' if MADEONSOL_KEY else 'NO'}")

    if not MADEONSOL_KEY:
        print("[YIN] ERROR: MADEONSOL_API_KEY no configurada")
        return

    resultados = []
    for mint in TOKENS:
        print(f"[YIN] {mint[:20]}...")
        data = fetch_token_intel(mint)
        resultados.append({"mint": mint, "data": data})
        if "error" not in data:
            token = data.get("token", {})
            print(f"[YIN]   {token.get('mint', '?')[:20]} | MCap ${token.get('market_cap', '?')}")
            kol = token.get("kol_activity", {})
            print(f"[YIN]   KOL signal: {kol.get('signal', '?')} | buying: {kol.get('buying_kols', 0)} | selling: {kol.get('selling_kols', 0)}")

    out = {"timestamp": ts, "fase": "token_intel", "resultados": resultados}
    out_path = TOKEN_DIR / f"token_intel_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()