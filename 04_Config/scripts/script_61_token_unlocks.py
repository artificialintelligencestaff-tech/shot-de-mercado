#!/usr/bin/env python3
"""
script_61_token_unlocks.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume API publica de token unlocks via Dropstab.
    Sin auth.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

DROPSTAB_API = "https://public-api.dropstab.com/api/v1/tokenUnlocks"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
UNLOCKS_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "pre_launch" / "unlocks"
UNLOCKS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Tokens principales a monitorear
TOKENS = ["bitcoin", "ethereum", "solana", "arbitrum", "optimism", "sui", "aptos"]


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Token Unlocks - {ts}")

    resultados = []
    for slug in TOKENS:
        try:
            r = requests.get(f"{DROPSTAB_API}/chart/{slug}", headers=HEADERS, timeout=TIMEOUT)
            if r.status_code == 200:
                resultados.append({"slug": slug, "data": r.json()})
                print(f"[YIN] {slug}: OK")
            else:
                print(f"[YIN] {slug}: HTTP {r.status_code}")
        except Exception as e:
            print(f"[YIN] {slug}: {str(e)[:100]}")

    out = {"timestamp": ts, "fase": "token_unlocks", "total": len(resultados), "unlocks": resultados}
    out_path = UNLOCKS_DIR / f"unlocks_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()