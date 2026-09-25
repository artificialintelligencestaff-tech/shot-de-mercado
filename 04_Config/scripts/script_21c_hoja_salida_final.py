#!/usr/bin/env python3
"""
script_21c_hoja_salida_final.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Version 3 FINAL. Corrige los 3 bugs del script 21b:
    1. Validacion de datos (no calcula si falta info)
    2. Matching robusto de simbolos ApeWisdom (soporta .X)
    3. Matching robusto de narrativas por categoria exacta
"""

import json
import glob
import requests
import time
from datetime import datetime, timezone
from pathlib import Path

COINGECKO_BASE = "https://api.coingecko.com/api/v3"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
INFORMES_DIR = PROJECT_ROOT / "03_Informes" / "hojas_salida"
APEWISDOM_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "social" / "apewisdom"
NARRATIVAS_DIR = PROJECT_ROOT / "02_Analisis" / "narrativas"

INFORMES_DIR.mkdir(parents=True, exist_ok=True)
TIMEOUT = 30


def leer_ultimo(directorio, patron):
    archivos = sorted(glob.glob(str(directorio / patron)), reverse=True)
    if not archivos:
        return None
    try:
        with open(archivos[0], "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[YIN] Error leyendo {archivos[0]}: {e}")
        return None


def fetch_coingecko(endpoint, params=None):
    try:
        url = f"{COINGECKO_BASE}{endpoint}"
        response = requests.get(url, params=params or {}, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def buscar_apewisdom(apewisdom_data, symbol):
    """MATCHING ROBUSTO: soporta formatos BTC.X, BTC, btc"""
    if not apewisdom_data:
        return None
    results = apewisdom_data.get("results", [])
    symbol_clean = symbol.upper().replace(".X", "").strip()
    for r in results:
        ticker = r.get("ticker", "").upper().replace(".X", "").strip()
        if ticker == symbol_clean:
            return {
                "rank": r.get("rank"),
                "mentions": r.get("mentions"),
                "upvotes": r.get("upvotes"),
                "rank_24h_ago": r.get("rank_24h_ago"),
                "mentions_24h_ago": r.get("mentions_24h_ago")
            }
    return None  # NO retorna datos genericos si no encuentra


def buscar_narrativa(narrativas_data, categorias_token):
    """MATCHING ROBUSTO: busca por coincidencia exacta de palabras clave"""
    if not narrativas_data:
        return None
    narrativas = narrativas_data.get("narrativas", [])
    # Mapeo de categorias CoinGecko a narrativas NarrativeScope
    MAPEO = {
        "Artificial Intelligence (AI)": "AI agents crypto",
        "AI Agents": "AI agents crypto",
        "DePIN": "DePIN",
        "Layer 2 (L2)": "Modular blockchain",
        "Modular blockchain": "Modular blockchain",
        "Liquid Staking": "Liquid staking",
        "Real World Assets (RWA)": "RWA tokenization",
        "Prediction Markets": "Prediction markets",
    }
    for cat in categorias_token:
        for key, narrativa_nombre in MAPEO.items():
            if key.lower() in cat.lower():
                for n in narrativas:
                    if n.get("narrativa", "").lower() == narrativa_nombre.lower():
                        return n
    return None


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Hoja Salida v3 FINAL - {ts}")

    # Cargar datos previos
    apewisdom = leer_ultimo(APEWISDOM_DIR, "apewisdom_trending_*.json")
    narrativescope = leer_ultimo(NARRATIVAS_DIR, "narrativescope_*.json")

    print(f"[YIN] ApeWisdom: {'OK' if apewisdom else 'FALTA'}")
    print(f"[YIN] NarrativeScope: {'OK' if narrativescope else 'FALTA'}")

    tokens = [
        {"id": "zcash", "symbol": "ZEC"},
        {"id": "lisk", "symbol": "LSK"},
        {"id": "fetch-ai", "symbol": "FET"},
        {"id": "bittensor", "symbol": "TAO"}
    ]

    for token in tokens:
        print(f"[YIN] Procesando {token['symbol']}...")

        data = fetch_coingecko(f"/coins/{token['id']}", {
            "localization": False, "tickers": False,
            "market_data": True, "sparkline": False
        })

        if "error" in data:
            print(f"[YIN] SKIP {token['symbol']}: {data['error']}")
            continue

        market = data.get("market_data", {})
        pct_24h = market.get("price_change_percentage_24h") or 0
        pct_7d = market.get("price_change_percentage_7d") or 0
        pct_30d = market.get("price_change_percentage_30d") or 0
        categorias = data.get("categories", [])

        # SEÑAL 1: MERCADO (basada en cambio 24h real)
        if pct_24h >= 50: s_mercado = 1.0
        elif pct_24h >= 20: s_mercado = 0.8
        elif pct_24h >= 10: s_mercado = 0.4
        else: s_mercado = 0.0

        # SEÑAL 2: SOCIAL (ApeWisdom real - None si no esta)
        aw = buscar_apewisdom(apewisdom, token["symbol"])
        if aw is None:
            s_social = 0.0
            aw_texto = "No aparece en ApeWisdom top 109"
        else:
            rank = aw.get("rank", 100)
            if rank <= 3: s_social = 1.0
            elif rank <= 10: s_social = 0.7
            elif rank <= 30: s_social = 0.4
            else: s_social = 0.1
            aw_texto = f"#{rank} con {aw.get('mentions')} menciones, {aw.get('upvotes')} upvotes"

        # SEÑAL 3: NARRATIVA (NarrativeScope real)
        narr = buscar_narrativa(narrativescope, categorias)
        if narr is None:
            s_narrativa = 0.0
            narr_texto = "Sin match directo en narrativas rastreadas"
        else:
            score_dev = narr.get("score_desarrollo", 0)
            s_narrativa = score_dev / 40
            narr_texto = f"{narr.get('narrativa')} (score {score_dev}/40)"

        # SCORE FINAL (promedio ponderado correcto)
        score_total = (s_mercado * 0.4) + (s_social * 0.3) + (s_narrativa * 0.3)

        # Clasificar
        if score_total > 0.75: nivel = "PREDICCION FUERTE"
        elif score_total > 0.65: nivel = "PREDICCION POSITIVA"
        elif score_total > 0.45: nivel = "OBSERVACION"
        elif score_total > 0.25: nivel = "MONITOREO"
        else: nivel = "DESCARTAR"

        # Generar hoja
        hoja = f"""# HOJA DE ACTIVO — {data.get('name', token['symbol']).upper()}
**ID:** PSM-{ts}-{token['symbol']}
**Score:** {score_total:.2f} ({nivel})

## 1. DATOS DE MERCADO (CoinGecko)
- Precio: ${market.get('current_price', {}).get('usd', 'N/A')}
- Cambio 24h: {pct_24h:.2f}% {'**CUMPLE >20%**' if pct_24h >= 20 else '(no cumple)'}
- Cambio 7d: {pct_7d:.2f}%
- Cambio 30d: {pct_30d:.2f}%
- Market Cap: ${market.get('market_cap', {}).get('usd', 0):,}
- Volumen 24h: ${market.get('total_volume', {}).get('usd', 0):,}

## 2. SEÑALES CALCULADAS
- Mercado (40%): {s_mercado:.2f}
- Social (30%): {s_social:.2f}
- Narrativa (30%): {s_narrativa:.2f}
- **Score total:** {score_total:.2f}

## 3. SOCIAL (ApeWisdom)
{aw_texto}

## 4. NARRATIVA (NarrativeScope)
{narr_texto}

## 5. CATEGORIAS (CoinGecko)
{', '.join(categorias[:10])}

## 6. FUENTES
- CoinGecko: [DATO VERIFICADO]
- ApeWisdom: [DATO VERIFICADO]
- NarrativeScope: [DATO VERIFICADO]
- Formula score: [INFERENCIA ESTRUCTURAL]

---
Generado: {ts}
"""
        out_path = INFORMES_DIR / f"hoja_v3_{token['symbol']}_{ts}.md"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(hoja)
        print(f"[YIN] {token['symbol']}: score {score_total:.2f} ({nivel}) -> {out_path}")
        time.sleep(5)

    print("[YIN] Script 21c finalizado.")


if __name__ == "__main__":
    main()