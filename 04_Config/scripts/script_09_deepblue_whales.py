#!/usr/bin/env python3
"""
script_09_deepblue_whales.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Obtener datos de ballenas de Deep Blue Alpha (gratuito, sin API key).
    Alternativa directa a Whale Alert.
"""

import json
import requests
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
        return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Deep Blue Alpha - {ts}")

    result = {
        "timestamp": ts,
        "fase": "deepblue_whales",
        "estado": "exito",
        "datos": {}
    }

    # 1. Estadisticas de ballenas
    print("[YIN] Obteniendo whale stats...")
    result["datos"]["stats"] = fetch("/stats")

    # 2. Indice de sentimiento de ballenas
    print("[YIN] Obteniendo whale index...")
    result["datos"]["whale_index"] = fetch("/whale-index")

    # Guardar
    out_path = ONCHAIN_DIR / f"deepblue_whales_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print("[YIN] Script 09 finalizado.")

if __name__ == "__main__":
    main()