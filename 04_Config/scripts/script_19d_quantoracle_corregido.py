#!/usr/bin/env python3
"""
script_19d_quantoracle_corregido.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Corregir los parametros de QuantOracle API REST.
    Los nombres correctos son:
    - kelly: win_rate, avg_win, avg_loss
    - position_size: account_size, entry_price, stop_loss, risk_percent
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

QUANTORACLE_URL = "https://api.quantoracle.dev"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
RIESGO_DIR = PROJECT_ROOT / "02_Analisis" / "riesgo" / "quantoracle"
RIESGO_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30


def call_quantoracle(endpoint, payload=None):
    try:
        url = f"{QUANTORACLE_URL}{endpoint}"
        response = requests.post(url, json=payload or {}, timeout=TIMEOUT)
        return {
            "http_status": response.status_code,
            "body": response.text[:1000]
        }
    except Exception as e:
        return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] QuantOracle Corregido - {ts}")

    result = {
        "timestamp": ts,
        "fase": "quantoracle_corregido",
        "estado": "exito",
        "datos": {}
    }

    # 1. Kelly Criterion (parametros correctos: win_rate, avg_win, avg_loss)
    print("[YIN] Calculando Kelly Criterion...")
    result["datos"]["kelly"] = call_quantoracle("/v1/risk/kelly", {
        "win_rate": 0.65,
        "avg_win": 1.5,
        "avg_loss": 1.0
    })

    # 2. Position Size (parametros correctos: account_size, entry_price, stop_loss, risk_percent)
    print("[YIN] Calculando Position Size...")
    result["datos"]["position_size"] = call_quantoracle("/v1/risk/position-size", {
        "account_size": 10000,
        "entry_price": 75000,
        "stop_loss": 72000,
        "risk_percent": 2
    })

    # 3. Probar otros endpoints comunes de QuantOracle
    print("[YIN] Probando endpoint /v1/tools/list...")
    result["datos"]["tools_list"] = call_quantoracle("/v1/tools/list", {})

    print("[YIN] Probando endpoint /v1/health...")
    result["datos"]["health"] = call_quantoracle("/v1/health", {})

    # Guardar
    out_path = RIESGO_DIR / f"quantoracle_corregido_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print("[YIN] Script 19d finalizado.")


if __name__ == "__main__":
    main()