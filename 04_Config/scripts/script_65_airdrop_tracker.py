#!/usr/bin/env python3
"""
script_65_airdrop_tracker.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Consume API de airdrops de testnet (Moltbook).
    Trackea MegaETH, Monad y proximos proyectos.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

TRACKER_API = "https://airdrop-tracker-omega.vercel.app/api/airdrops"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
TRACKER_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "pre_launch" / "testnet_airdrops"
TRACKER_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Airdrop Tracker (Testnet) - {ts}")

    try:
        r = requests.get(TRACKER_API, timeout=TIMEOUT)
        if r.status_code != 200:
            print(f"[YIN] ERROR: HTTP {r.status_code}")
            return

        data = r.json()
        airdrops = data.get("airdrops", data if isinstance(data, list) else [])

        out = {"timestamp": ts, "fase": "testnet_airdrops", "total": len(airdrops), "airdrops": airdrops}
        out_path = TRACKER_DIR / f"testnet_airdrops_{ts}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2, ensure_ascii=False)
        print(f"[YIN] Guardado: {out_path}")
        print(f"[YIN] Total airdrops: {len(airdrops)}")

        for a in airdrops[:10]:
            print(f"[YIN]   {a.get('name', '?')} | {a.get('status', '?')}")

    except Exception as e:
        print(f"[YIN] ERROR: {str(e)[:200]}")


if __name__ == "__main__":
    main()