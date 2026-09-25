#!/usr/bin/env python3
"""
script_11_apewisdom.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Obtener trending tickers de Reddit via ApeWisdom (gratuito, keyless).
    Cubre 15+ subreddits cripto.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

APEWISDOM_URL = "https://apewisdom.io/api/v1.0/filter/all-crypto/page/1"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
SOCIAL_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "social" / "apewisdom"
SOCIAL_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] ApeWisdom - {ts}")

    try:
        response = requests.get(APEWISDOM_URL, timeout=TIMEOUT)
        data = response.json()

        out_path = SOCIAL_DIR / f"apewisdom_trending_{ts}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[YIN] Guardado: {out_path}")

    except Exception as e:
        print(f"[YIN] Error: {e}")

    print("[YIN] Script 11 finalizado.")


if __name__ == "__main__":
    main()