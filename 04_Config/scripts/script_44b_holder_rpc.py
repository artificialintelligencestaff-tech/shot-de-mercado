#!/usr/bin/env python3
"""
script_44b_holder_rpc.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Analisis de holders via RPC de Solana (getTokenLargestAccounts).
    NO requiere API key. Solo RPC endpoint publico o gratuito.
    Detecta concentracion y posible bundling.
"""

import json
import os
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path(r"D:\Proyecto Shot de Mercado\04_Config\.env")
load_dotenv(ENV_PATH)

# RPC de Solana (publico, gratuito, sin API key)
SOLANA_RPC = os.getenv("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
HOLDERS_DIR = PROJECT_ROOT / "02_Analisis" / "holder_analysis"
HOLDERS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30

TOKENS = [
    {"symbol": "catwifout", "address": "5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump"},
]


def rpc_call(method, params):
    """Llama al RPC de Solana con JSON-RPC."""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }
    try:
        r = requests.post(SOLANA_RPC, json=payload, timeout=TIMEOUT)
        return r.json()
    except Exception as e:
        return {"error": str(e)[:150]}


def get_token_supply(mint):
    """Obtiene el supply total del token."""
    result = rpc_call("getTokenSupply", [mint])
    if "result" in result and "value" in result["result"]:
        return float(result["result"]["value"].get("uiAmount", 0))
    return 0


def get_largest_accounts(mint):
    """Obtiene las 20 cuentas mas grandes del token."""
    result = rpc_call("getTokenLargestAccounts", [mint])
    if "result" in result and "value" in result["result"]:
        return result["result"]["value"]
    return []


def analizar_holders(mint):
    """Analiza la distribucion de holders."""
    supply = get_token_supply(mint)
    accounts = get_largest_accounts(mint)

    if not accounts or supply == 0:
        return {"error": "sin datos de holders o supply"}

    # Calcular concentracion
    amounts = []
    for acc in accounts:
        ui_amount = float(acc.get("uiAmount", 0) or 0)
        amounts.append(ui_amount)

    top1 = (amounts[0] / supply * 100) if len(amounts) > 0 else 0
    top5 = (sum(amounts[:5]) / supply * 100) if len(amounts) >= 5 else 0
    top10 = (sum(amounts[:10]) / supply * 100) if len(amounts) >= 10 else 0
    top20 = (sum(amounts[:20]) / supply * 100) if len(amounts) >= 20 else 0

    # Gini coefficient simplificado
    total = sum(amounts)
    n = len(amounts)
    if n > 0 and total > 0:
        sorted_amounts = sorted(amounts)
        gini_sum = sum((2 * i - n + 1) * amt for i, amt in enumerate(sorted_amounts, 1))
        gini = gini_sum / (n * total)
    else:
        gini = 0

    # Clasificar riesgo
    if top10 > 50:
        riesgo = "ALTO"
    elif top10 > 30:
        riesgo = "MEDIO"
    else:
        riesgo = "BAJO"

    return {
        "supply_total": supply,
        "top1_pct": round(top1, 2),
        "top5_pct": round(top5, 2),
        "top10_pct": round(top10, 2),
        "top20_pct": round(top20, 2),
        "gini_coefficient": round(gini, 3),
        "riesgo_concentracion": riesgo,
        "top_holders": [
            {
                "address": acc.get("address", ""),
                "uiAmount": acc.get("uiAmount", 0),
                "pct": round(float(acc.get("uiAmount", 0) or 0) / supply * 100, 2)
            }
            for acc in accounts[:10]
        ]
    }


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Holder Analysis (RPC) - {ts}")
    print(f"[YIN] RPC: {SOLANA_RPC}")

    resultados = []
    for token in TOKENS:
        print(f"[YIN] {token['symbol']}...")
        analisis = analizar_holders(token["address"])
        resultados.append({
            "symbol": token["symbol"],
            "address": token["address"],
            "analisis": analisis
        })
        if "error" in analisis:
            print(f"[YIN]   ERROR: {analisis['error']}")
        else:
            print(f"[YIN]   Top 10: {analisis.get('top10_pct')}% | Riesgo: {analisis.get('riesgo_concentracion')}")

    out = {"timestamp": ts, "fase": "holder_analysis_rpc", "tokens": resultados}
    out_path = HOLDERS_DIR / f"holder_rpc_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()