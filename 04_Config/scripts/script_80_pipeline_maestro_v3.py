#!/usr/bin/env python3
"""
script_80_pipeline_maestro_v3.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Version 3. Corrige dos bugs:
    1. Parser flexible de campos three.ws (multiple nombres)
    2. Drift detection calibrado (no pausa por texto literal)
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

THREEWS_BASE = "https://three.ws/api/crypto"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
OUTPUT_DIR = PROJECT_ROOT / "03_Informes" / "shot_de_mercado"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0"}


def fetch(path, params=None):
    try:
        r = requests.get(f"{THREEWS_BASE}{path}", params=params or {}, headers=HEADERS, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None


def get_field(data, *names, default=None):
    """Busca un campo con multiples nombres alternativos."""
    if not isinstance(data, dict):
        return default
    for name in names:
        if name in data and data[name] is not None:
            return data[name]
    return default


def normalizar_token(raw):
    """Normaliza un token a estructura canonica."""
    if not raw:
        return None
    return {
        "symbol": get_field(raw, "symbol", "ticker", "token_symbol", default="?"),
        "name": get_field(raw, "name", "token_name", default="?"),
        "mint": get_field(raw, "mint", "address", "token_address", default="?"),
        "price": get_field(raw, "priceUsd", "price_usd", "price", "current_price", default=None),
        "mcap": get_field(raw, "marketCap", "market_cap", "mcap", "fdv", default=None),
        "liquidity": get_field(raw, "liquidity", "liquidity_usd", "liq", default=None),
        "volume_24h": get_field(raw, "volume24h", "volume_24h", "volume", default=None),
        "age_min": get_field(raw, "ageMinutes", "age_minutes", "age", default=None),
        "risk_level": get_field(raw, "riskLevel", "risk_level", "risk", default="UNKNOWN"),
        "raw": raw
    }


def calcular_score(token):
    """Score 0-100 basado en datos disponibles."""
    if not token:
        return 0
    score = 0
    # Liquidez
    liq = token.get("liquidity") or 0
    if isinstance(liq, str): liq = 0
    if liq >= 100000: score += 30
    elif liq >= 50000: score += 20
    elif liq >= 20000: score += 12
    elif liq >= 5000: score += 5

    # MCap
    mcap = token.get("mcap") or 0
    if isinstance(mcap, str): mcap = 0
    if mcap >= 500000: score += 25
    elif mcap >= 200000: score += 18
    elif mcap >= 50000: score += 10

    # Edad (sweet spot 30min - 4h)
    age = token.get("age_min") or 0
    if isinstance(age, str): age = 0
    if 30 <= age <= 240: score += 25
    elif 240 < age <= 720: score += 15
    elif age < 30: score += 10

    # Risk
    risk = str(token.get("risk_level", "")).upper()
    if risk == "LOW": score += 20
    elif risk == "MEDIUM": score += 10

    return min(score, 100)


def generar_hoja(token):
    """Genera hoja markdown para usuario no tecnico."""
    if not token:
        return None

    nivel = "ALERTA" if token["price"] and token["liquidity"] and calcular_score(token) >= 60 else "OBSERVACION"
    if calcular_score(token) < 40:
        nivel = "DESCARTAR"

    precio = token["price"] if token["price"] else "pendiente"
    mcap = token["mcap"] if token["mcap"] else "pendiente"
    liq = token["liquidity"] if token["liquidity"] else "pendiente"

    hoja = f"""# SHOT DE MERCADO — {token['symbol']}

## 📊 ESTADO
- Nombre: {token['name']}
- Simbolo: {token['symbol']}
- Direccion: {token['mint']}
- Precio: ${precio}
- Market Cap: ${mcap}
- Liquidez: ${liq}
- Nivel: {nivel}
- Score: {calcular_score(token)}/100

## 🛒 COMO ADQUIRIRLO
1. Instalar Phantom Wallet: https://phantom.app
2. Comprar SOL en Binance o Coinbase
3. Enviar SOL a tu wallet Phantom
4. Conectar Phantom a Jupiter: https://jup.ag
5. Pegar direccion del token: {token['mint']}
6. Configurar slippage 5-10%
7. Ejecutar swap

## ⚠️ ADVERTENCIAS
- No invertir mas del 1-2% del capital
- Verificar la direccion en Solscan antes de operar
- Token nuevo = riesgo alto
"""
    return {"symbol": token["symbol"], "mint": token["mint"], "nivel": nivel, "score": calcular_score(token), "hoja": hoja}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Pipeline Maestro v3 - {ts}")

    # 1. Recolectar
    launches_raw = fetch("/launches", {"limit": 20})
    trending_raw = fetch("/trending")

    launches = get_field(launches_raw, "launches", "data", "tokens", default=[])

    print(f"[YIN] Launches: {len(launches)}")

    # 2. Analizar cada launch
    hojas = []
    for raw in launches[:5]:
        token = normalizar_token(raw)
        if not token: continue

        # Consultar token completo
        if token["mint"] and token["mint"] != "?":
            full = fetch("/token", {"address": token["mint"]})
            if full:
                token_full = normalizar_token(full)
                if token_full:
                    # Combinar
                    for k, v in token_full.items():
                        if v and v != "?" and k != "raw":
                            token[k] = v

        hoja = generar_hoja(token)
        if hoja:
            hojas.append(hoja)
            print(f"[YIN]   {hoja['symbol']:15} | Score {hoja['score']:3} | {hoja['nivel']}")

    # 3. Guardar
    out = {
        "timestamp": ts,
        "fase": "pipeline_maestro_v3",
        "total_launches": len(launches),
        "total_hojas": len(hojas),
        "hojas": hojas
    }

    out_path = OUTPUT_DIR / f"shot_v3_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print(f"[YIN] Hojas generadas: {len(hojas)}")


if __name__ == "__main__":
    main()