#!/usr/bin/env python3
"""
script_67_cryptoguard.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Verifica riesgo de tokens via CryptoGuard API.
    Free tier: 5 calls/dia. Detecta crashes 27 dias antes.
    Endpoint: https://gpartin--cryptoguard-api-fastapi-app.modal.run/v1/validate-trade
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

CRYPTOGUARD_URL = "https://gpartin--cryptoguard-api-fastapi-app.modal.run/v1/validate-trade"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
RISK_DIR = PROJECT_ROOT / "02_Analisis" / "risk_check"
RISK_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30

TOKENS = ["solana", "arbitrum", "optimism"]


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] CryptoGuard Risk Scanner - {ts}")

    resultados = []
    for token in TOKENS:
        print(f"[YIN] {token}...")
        try:
            r = requests.post(CRYPTOGUARD_URL, json={
                "token": token, "action": "buy", "amount_usd": 100
            }, timeout=TIMEOUT)
            if r.status_code == 200:
                data = r.json()
                verdict = data.get("verdict", "?")
                score = data.get("anomaly_score", "?")
                print(f"[YIN]   {verdict} | Score: {score}")
                resultados.append({"token": token, "verdict": verdict, "anomaly_score": score, "data": data})
            else:
                print(f"[YIN]   HTTP {r.status_code}")
                resultados.append({"token": token, "error": f"HTTP {r.status_code}"})
        except Exception as e:
            print(f"[YIN]   ERROR: {str(e)[:100]}")
            resultados.append({"token": token, "error": str(e)[:100]})

    out = {"timestamp": ts, "fase": "cryptoguard", "total": len(resultados), "resultados": resultados}
    out_path = RISK_DIR / f"cryptoguard_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()