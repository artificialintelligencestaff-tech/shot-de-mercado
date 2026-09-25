#!/usr/bin/env python3
"""
script_63_token_unlocks.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume API de token unlocks via DropsTab (free tier para builders).
    Requiere API key gratuita (solicitar en dropstab.com).
"""

import json
import os
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path(r"D:\Proyecto Shot de Mercado\04_Config\.env")
load_dotenv(ENV_PATH)

DROPSTAB_API_KEY = os.getenv("DROPSTAB_API_KEY", "")
DROPSTAB_BASE = "https://public-api.dropstab.com/api/v1"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
UNLOCKS_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "pre_launch" / "unlocks"
UNLOCKS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
TOKENS = ["bitcoin", "ethereum", "solana", "arbitrum", "optimism", "sui", "aptos"]


def fetch_unlocks(slug):
    headers = {"User-Agent": "Mozilla/5.0"}
    if DROPSTAB_API_KEY:
        headers["Authorization"] = f"Bearer {DROPSTAB_API_KEY}"
    try:
        r = requests.get(f"{DROPSTAB_BASE}/tokenUnlocks/chart/{slug}", headers=headers, timeout=TIMEOUT)
        if r.status_code == 200:
            return r.json()
        return {"error": f"HTTP {r.status_code}"}
    except Exception as e:
        return {"error": str(e)[:150]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Token Unlocks - {ts}")
    print(f"[YIN] API key configurada: {'SI' if DROPSTAB_API_KEY else 'NO'}")

    if not DROPSTAB_API_KEY:
        print("[YIN] ADVERTENCIA: Sin API key. Solicitar en dropstab.com/builders")
        return

    resultados = []
    for slug in TOKENS:
        print(f"[YIN] {slug}...")
        data = fetch_unlocks(slug)
        resultados.append({"slug": slug, "data": data})

    out = {"timestamp": ts, "fase": "token_unlocks", "total": len(resultados), "unlocks": resultados}
    out_path = UNLOCKS_DIR / f"unlocks_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()