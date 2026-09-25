#!/usr/bin/env python3
"""
script_06_historical_audit.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Auditar activos con aceleracion pasada y presente.
    Extraer datos historicos de CoinGecko y Alpha MCP.
    Detectar patrones comunes en aceleraciones >10%.
"""

import json
import requests
import time
from datetime import datetime, timezone
from pathlib import Path

COINGECKO_BASE = "https://api.coingecko.com/api/v3"
ALPHA_MCP_URL = "https://alpha.moss.land/api/mcp"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
AUDITORIA_DIR = PROJECT_ROOT / "02_Analisis" / "auditorias"
AUDITORIA_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30

# Activos de interes: actuales (acelerando) + historicos (referencia)
TARGETS = [
    # ACTUALES - aceleracion >10% detectada
    {"id": "lisk", "symbol": "LSK", "tipo": "actual"},
    {"id": "derive", "symbol": "DRV", "tipo": "actual"},
    {"id": "zcash", "symbol": "ZEC", "tipo": "actual"},
    {"id": "hyperliquid", "symbol": "HYPE", "tipo": "actual"},
    {"id": "near", "symbol": "NEAR", "tipo": "actual"},
    {"id": "arbitrum", "symbol": "ARB", "tipo": "actual"},
    # HISTORICOS - referencia (narrativas pasadas)
    {"id": "dogecoin", "symbol": "DOGE", "tipo": "historico"},
    {"id": "shiba-inu", "symbol": "SHIB", "tipo": "historico"},
    {"id": "pepe", "symbol": "PEPE", "tipo": "historico"},
]


def fetch_coingecko(endpoint, params=None):
    try:
        url = f"{COINGECKO_BASE}{endpoint}"
        response = requests.get(url, params=params or {}, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def parse_sse(raw_text):
    try:
        for line in raw_text.split("\n"):
            line = line.strip()
            if line.startswith("data: "):
                return json.loads(line[6:])
        return json.loads(raw_text)
    except json.JSONDecodeError:
        return {"error": "JSONDecodeError"}


def call_alpha(method, params=None):
    payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params or {}}
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    try:
        response = requests.post(ALPHA_MCP_URL, json=payload, headers=headers, timeout=TIMEOUT)
        return parse_sse(response.text)
    except Exception as e:
        return {"error": str(e)}


def audit_asset(target):
    """Audita un activo: datos + categorias + historico."""
    print(f"[YIN] Auditando {target['symbol']} ({target['tipo']})...")

    result = {
        "id": target["id"],
        "symbol": target["symbol"],
        "tipo": target["tipo"],
        "timestamp": datetime.now(timezone.utc).isoformat() + "Z"
    }

    # 1. Datos generales
    data = fetch_coingecko(f"/coins/{target['id']}", {
        "localization": False,
        "tickers": False,
        "market_data": True,
        "community_data": True,
        "developer_data": True,
        "sparkline": False
    })

    if "error" in data:
        result["error"] = data["error"]
        return result

    # 2. Extraer campos clave
    market = data.get("market_data", {})
    result["market_data"] = {
        "current_price_usd": market.get("current_price", {}).get("usd"),
        "market_cap_usd": market.get("market_cap", {}).get("usd"),
        "total_volume_usd": market.get("total_volume", {}).get("usd"),
        "price_change_24h": market.get("price_change_percentage_24h"),
        "price_change_7d": market.get("price_change_percentage_7d"),
        "price_change_30d": market.get("price_change_percentage_30d"),
        "circulating_supply": market.get("circulating_supply"),
        "total_supply": market.get("total_supply"),
        "mcap_to_tvl_ratio": market.get("mcap_to_tvl_ratio"),
        "total_value_locked": market.get("total_value_locked"),
    }

    # 3. Categorias y narrativas
    result["categories"] = data.get("categories", [])
    result["description"] = data.get("description", {}).get("en", "")[:500]

    # 4. Community
    result["community_data"] = data.get("community_data", {})

    # 5. Contracts
    result["contracts"] = data.get("contract_address", "no_contract")

    # 6. Calculo de ratios
    mcap = result["market_data"].get("market_cap_usd", 0) or 0
    vol = result["market_data"].get("total_volume_usd", 0) or 0
    if mcap > 0:
        result["ratios"] = {
            "vol_mcap": round(vol / mcap, 4),
            "es_aceleracion": vol / mcap > 0.5
        }

    return result


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Historical Audit - {ts}")

    consolidated = {
        "timestamp": ts,
        "fase": "historical_audit",
        "estado": "exito",
        "assets": [],
        "patrones": {}
    }

    for target in TARGETS:
        try:
            result = audit_asset(target)
            consolidated["assets"].append(result)
            print(f"[YIN] {target['symbol']} OK")
            time.sleep(3)
        except Exception as e:
            print(f"[YIN] Error en {target['symbol']}: {e}")
            consolidated["assets"].append({
                "symbol": target["symbol"],
                "error": str(e)
            })

    # Detectar patrones
    print("[YIN] Analizando patrones...")
    aceleraciones = []
    for asset in consolidated["assets"]:
        if "market_data" in asset:
            pct_24h = asset["market_data"].get("price_change_24h") or 0
            if pct_24h >= 20:
                aceleraciones.append({
                    "symbol": asset["symbol"],
                    "pct_24h": pct_24h,
                    "vol_mcap": asset.get("ratios", {}).get("vol_mcap"),
                    "categorias": asset.get("categories", [])
                })

    consolidated["patrones"] = {
        "total_aceleraciones": len(aceleraciones),
        "aceleraciones": aceleraciones,
        "categorias_comunes": list(set([
            cat for a in aceleraciones for cat in a.get("categorias", [])
        ]))[:20]
    }

    # Guardar
    out_path = AUDITORIA_DIR / f"historical_audit_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(consolidated, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print(f"[YIN] Activos procesados: {len(consolidated['assets'])}")
    print(f"[YIN] Aceleraciones detectadas: {len(aceleraciones)}")
    print("[YIN] Script 06 finalizado.")


if __name__ == "__main__":
    main()