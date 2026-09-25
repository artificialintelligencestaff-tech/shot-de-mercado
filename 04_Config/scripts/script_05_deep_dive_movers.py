#!/usr/bin/env python3
"""
script_05_deep_dive_movers.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Hacer deep dive en los activos con aceleracion vertical detectada.
    ARGUS, Lisk (LSK), Derive (DRV).
    Consulta CoinGecko coins/{id} para obtener:
    - Descripcion del proyecto
    - Comunidad y desarrollo
    - Contract addresses
    - Liquidez y volumen detallado
"""

import json
import requests
import time
from datetime import datetime, timezone
from pathlib import Path

COINGECKO_BASE = "https://api.coingecko.com/api/v3"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
ANALISIS_DIR = PROJECT_ROOT / "02_Analisis" / "auditorias"
ANALISIS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30

# Activos con aceleracion vertical detectada (CoinGecko IDs)
TARGETS = [
    {"id": "argus", "symbol": "ARGUS", "cambio_24h": "+754.7%"},
    {"id": "lisk", "symbol": "LSK", "cambio_24h": "+87.9%"},
    {"id": "derive", "symbol": "DRV", "cambio_24h": "+30.51%"},
    {"id": "zcash", "symbol": "ZEC", "cambio_24h": "+12.98%"}
]


def fetch(endpoint, params=None):
    try:
        url = f"{COINGECKO_BASE}{endpoint}"
        response = requests.get(url, params=params or {}, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def deep_dive(coin_id, symbol):
    """Extrae informacion profunda de un activo."""
    print(f"[YIN] Deep dive: {symbol} ({coin_id})")

    result = {
        "coin_id": coin_id,
        "symbol": symbol,
        "timestamp": datetime.now(timezone.utc).isoformat() + "Z"
    }

    # 1. Datos generales
    data = fetch(f"/coins/{coin_id}", {
        "localization": False,
        "tickers": False,
        "market_data": True,
        "community_data": True,
        "developer_data": True,
        "sparkline": False
    })
    result["general"] = data
    time.sleep(3)

    # 2. Market chart 7 dias
    chart = fetch(f"/coins/{coin_id}/market_chart", {
        "vs_currency": "usd",
        "days": 7,
        "interval": "hourly"
    })
    result["chart_7d"] = chart
    time.sleep(3)

    # 3. Top holders / contract info (si disponible)
    result["contract"] = data.get("contract_address", "no_contract") if isinstance(data, dict) else "error"

    return result


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Deep Dive Movers - {ts}")

    consolidated = {
        "timestamp": ts,
        "fase": "deep_dive_movers",
        "estado": "exito",
        "targets": [],
        "notas": "Analisis de activos con aceleracion vertical detectada en CoinGecko trending"
    }

    for target in TARGETS:
        print(f"[YIN] Procesando {target['symbol']}...")
        try:
            result = deep_dive(target["id"], target["symbol"])
            result["cambio_24h_detectado"] = target["cambio_24h"]
            consolidated["targets"].append(result)
            print(f"[YIN] {target['symbol']} OK")
        except Exception as e:
            print(f"[YIN] Error en {target['symbol']}: {e}")
            consolidated["targets"].append({
                "symbol": target["symbol"],
                "error": str(e)
            })

    # Guardar
    out_path = ANALISIS_DIR / f"deep_dive_movers_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(consolidated, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print(f"[YIN] Activos procesados: {len(consolidated['targets'])}")
    print("[YIN] Script 05 finalizado.")


if __name__ == "__main__":
    main()