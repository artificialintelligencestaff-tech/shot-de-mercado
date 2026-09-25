#!/usr/bin/env python3
"""
script_02_signalstack.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Obtener el Candle Review score diario de SignalStack MCP.
    Score 0-100 basado en 7 categorias.
    Sin API key.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

SIGNALSTACK_URL = "http://96.126.106.225:3458"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
MERCADOS_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "mercados"
MERCADOS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30


def get_endpoint(path):
    try:
        response = requests.get(f"{SIGNALSTACK_URL}{path}", timeout=TIMEOUT)
        return {
            "http_status": response.status_code,
            "body": response.text[:5000]
        }
    except Exception as e:
        return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] SignalStack MCP - {ts}")

    result = {
        "timestamp": ts,
        "fase": "signalstack",
        "estado": "exito",
        "datos": {}
    }

    # 1. Health
    print("[YIN] Verificando health...")
    result["datos"]["health"] = get_endpoint("/health")

    # 2. Candle Review de hoy
    print("[YIN] Solicitando Candle Review de hoy...")
    result["datos"]["candle_today"] = get_endpoint("/candle/today")

    # 3. Historial 30 dias
    print("[YIN] Solicitando historial 30 dias...")
    result["datos"]["history"] = get_endpoint("/candle/history?limit=30")

    # Guardar
    out_path = MERCADOS_DIR / f"signalstack_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print("[YIN] Script 02 finalizado.")


if __name__ == "__main__":
    main()