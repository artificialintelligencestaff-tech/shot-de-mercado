#!/usr/bin/env python3
"""
script_19b_quantoracle.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Conectar con QuantOracle API REST (gratuita, 1,000 calls/dia, sin key).
    73 calculadoras deterministas: Kelly, position sizing, VaR, Sharpe.
    Endpoint verificado: https://api.quantoracle.dev
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
        if response.status_code == 200:
            return response.json()
        return {"error": f"HTTP {response.status_code}", "body": response.text[:500]}
    except Exception as e:
        return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] QuantOracle - {ts}")

    result = {
        "timestamp": ts,
        "fase": "quantoracle",
        "estado": "exito",
        "datos": {}
    }

    # 1. Kelly Criterion
    print("[YIN] Calculando Kelly Criterion...")
    result["datos"]["kelly"] = call_quantoracle("/v1/risk/kelly", {
        "win_probability": 0.65,
        "win_loss_ratio": 1.5,
        "bankroll": 10000
    })

    # 2. Position Size (fixed-fractional)
    print("[YIN] Calculando Position Size...")
    result["datos"]["position_size"] = call_quantoracle("/v1/risk/position-size", {
        "capital": 10000,
        "risk_percent": 2,
        "entry": 75000,
        "stop_loss": 72000
    })

    # 3. VaR (Value at Risk)
    print("[YIN] Calculando VaR...")
    result["datos"]["var"] = call_quantoracle("/v1/risk/var", {
        "returns": [0.02, -0.01, 0.03, 0.01, -0.02, 0.04, -0.03, 0.01],
        "confidence_level": 0.95
    })

    # Guardar
    out_path = RIESGO_DIR / f"quantoracle_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print("[YIN] Script 19b finalizado.")


if __name__ == "__main__":
    main()