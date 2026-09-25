#!/usr/bin/env python3
"""
script_60_airdrops_json.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume API publica de airdrops via web3-discover-data.
    CC0, sin auth, sin rate limit.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

AIRDROP_API = "https://web3-discover.vercel.app/api/airdrops.json"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
AIRDROP_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "pre_launch" / "airdrops_json"
AIRDROP_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0"}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Airdrops JSON - {ts}")

    try:
        r = requests.get(AIRDROP_API, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code != 200:
            print(f"[YIN] ERROR: HTTP {r.status_code}")
            return

        data = r.json()
        entries = data.get("entries", [])

        out = {
            "timestamp": ts,
            "fase": "airdrops_json",
            "generated_at": data.get("generatedAt"),
            "total": len(entries),
            "airdrops": entries
        }

        out_path = AIRDROP_DIR / f"airdrops_{ts}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2, ensure_ascii=False)
        print(f"[YIN] Guardado: {out_path}")
        print(f"[YIN] Total airdrops: {len(entries)}")

        # Resumen
        for a in entries[:15]:
            print(f"[YIN]   {a.get('project', '?')} | {a.get('chain', '?')} | {a.get('status', '?')}")

    except Exception as e:
        print(f"[YIN] ERROR: {str(e)[:200]}")


if __name__ == "__main__":
    main()