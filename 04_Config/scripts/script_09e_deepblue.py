#!/usr/bin/env python3
"""
script_09e_deepblue.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Conectar con Deep Blue Alpha (API REST, GET).
    3 endpoints gratuitos: stats, whale-index, top-tokens.
    Sin API key, sin auth.
"""

import json
import requests
import time
from datetime import datetime, timezone
from pathlib import Path

DEEPBLUE_BASE = "https://deepbluealpha.io/api/v1/public"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
ONCHAIN_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "onchain"
ONCHAIN_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30


def fetch(endpoint):
    try:
        url = f"{DEEPBLUE_BASE}{endpoint}"
        response = requests.get(url, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        return {"error": f"HTTP {response.status_code}", "body": response.text[:500]}
    except Exception as e:
        return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Deep Blue Alpha - {ts}")

    result = {
        "timestamp": ts,
        "fase": "deepblue_alpha",
        "estado": "exito",
        "datos": {}
    }

    # 1. Stats
    print("[YIN] Solicitando stats...")
    result["datos"]["stats"] = fetch("/stats")
    time.sleep(2)

    # 2. Whale Index
    print("[YIN] Solicitando whale-index...")
    result["datos"]["whale_index"] = fetch("/whale-index")
    time.sleep(2)

    # 3. Top Tokens
    print("[YIN] Solicitando top-tokens...")
    result["datos"]["top_tokens"] = fetch("/top-tokens")

    # Guardar
    out_path = ONCHAIN_DIR / f"deepblue_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print("[YIN] Script 09e finalizado.")


if __name__ == "__main__":
    main()