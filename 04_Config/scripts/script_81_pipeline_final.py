#!/usr/bin/env python3
"""
script_81_pipeline_final.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Pipeline final con fuente corregida:
    - Usa /trending (tokens maduros) en lugar de /launches (T+0)
    - Enriquece con Dexscreener para liquidez
    - Scoring basado en datos reales
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

THREEWS_BASE = "https://three.ws/api/crypto"
DEXSCREENER_URL = "https://api.dexscreener.com/latest/dex/tokens"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
OUTPUT_DIR = PROJECT_ROOT / "03_Informes" / "shot_de_mercado"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0"}


def fetch_threews(path, params=None):
    try:
        r = requests.get(f"{THREEWS_BASE}{path}", params=params or {}, headers=HEADERS, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None


def fetch_dexscreener(mint):
    try:
        r = requests.get(f"{DEXSCREENER_URL}/{mint}", headers=HEADERS, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        data = r.json()
        pairs = data.get("pairs", [])
        if not pairs:
            return None
        return max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0))
    except Exception:
        return None


def calcular_score(token):
    """Score 0-100 con criterios de calidad."""
    score = 0
    razones = []

    mcap = token.get("marketCapUsd") or 0
    vol = token.get("volumeUsd") or 0
    liq = token.get("liquidityUsd") or 0

    # 1. Market Cap (0-25)
    if mcap >= 500000: score += 25; razones.append("MCap alto")
    elif mcap >= 200000: score += 18; razones.append("MCap medio")
    elif mcap >= 50000: score += 10; razones.append("MCap bajo")

    # 2. Volumen (0-30)
    if vol >= 1000000: score += 30; razones.append("Volumen masivo")
    elif vol >= 500000: score += 22; razones.append("Volumen alto")
    elif vol >= 100000: score += 15; razones.append("Volumen medio")
    elif vol >= 50000: score += 8; razones.append("Volumen bajo")

    # 3. Liquidez (0-25) - de Dexscreener
    if liq >= 100000: score += 25; razones.append("Liquidez alta")
    elif liq >= 50000: score += 18; razones.append("Liquidez media")
    elif liq >= 20000: score += 10; razones.append("Liquidez baja")

    # 4. Score three.ws (0-20)
    ws_score = token.get("score") or 0
    if ws_score >= 80: score += 20; razones.append("WS score alto")
    elif ws_score >= 60: score += 12; razones.append("WS score medio")
    elif ws_score >= 40: score += 5

    # 5. Cambio positivo (0-10)
    change = token.get("change") or 0
    if change > 50: score += 10; razones.append("Cambio fuerte")
    elif change > 20: score += 6
    elif change > 0: score += 3

    return min(score, 100), razones


def generar_hoja(token, score, razones):
    """Genera hoja de salida para usuario no tecnico."""
    nivel = "ALERTA" if score >= 70 else "WATCH" if score >= 50 else "DESCARTAR"

    return f"""# SHOT DE MERCADO — {token.get('symbol', '?')}

## ESTADO
- Nombre: {token.get('name', '?')}
- Simbolo: {token.get('symbol', '?')}
- Direccion: {token.get('mint', token.get('address', '?'))}
- Market Cap: ${token.get('marketCapUsd', 0):,.0f}
- Volumen 24h: ${token.get('volumeUsd', 0):,.0f}
- Liquidez: ${token.get('liquidityUsd', 0):,.0f}
- Score: {score}/100
- Nivel: {nivel}

## POR QUE LO DETECTAMOS
{chr(10).join('- ' + r for r in razones)}

## COMO ADQUIRIRLO
1. Instalar Phantom Wallet: https://phantom.app
2. Comprar SOL en Binance o Coinbase
3. Enviar SOL a tu wallet Phantom
4. Conectar Phantom a Jupiter: https://jup.ag
5. Pegar direccion: {token.get('mint', token.get('address', '?'))}
6. Configurar slippage 5-10%
7. Ejecutar swap

## ADVERTENCIAS
- No invertir mas del 1-2% del capital
- Verificar la direccion en Solscan antes de operar
"""


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Pipeline Final - {ts}")

    # 1. Trending (tokens maduros)
    trending = fetch_threews("/trending")
    tokens = trending.get("tokens", []) if trending else []
    print(f"[YIN] Trending tokens: {len(tokens)}")

    # 2. Enriquecer cada token con Dexscreener
    hojas = []
    for raw in tokens[:10]:
        mint = raw.get("mint", "")
        if not mint: continue

        # Enriquecer con Dexscreener
        dex = fetch_dexscreener(mint)
        if dex:
            raw["liquidityUsd"] = float(dex.get("liquidity", {}).get("usd", 0) or 0)
            if not raw.get("volumeUsd"):
                raw["volumeUsd"] = float(dex.get("volume", {}).get("h24", 0) or 0)

        score, razones = calcular_score(raw)
        hoja = generar_hoja(raw, score, razones)
        hojas.append({
            "symbol": raw.get("symbol"),
            "mint": mint,
            "score": score,
            "nivel": "ALERTA" if score >= 70 else "WATCH" if score >= 50 else "DESCARTAR",
            "razones": razones,
            "hoja": hoja
        })
        print(f"[YIN]   {raw.get('symbol', '?'):15} | Score {score:3} | {hojas[-1]['nivel']}")

    # 3. Guardar
    out = {"timestamp": ts, "fase": "pipeline_final", "total": len(hojas), "hojas": hojas}
    out_path = OUTPUT_DIR / f"shot_final_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()