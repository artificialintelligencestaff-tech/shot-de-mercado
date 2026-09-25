#!/usr/bin/env python3
"""
script_21d_hoja_auditada.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Version 4. Reporta valores intermedios para auditoria.
    Corrige el bug del script 21c donde el cambio 24h no coincidia
    con el calculo del score.
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
    except Exception:
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
                "upvotes": r.get("upvotes")
            }
    return None


def calcular_s_mercado(pct_24h):
    """Calcula senal de mercado con auditoria."""
    if pct_24h >= 50: return 1.0, f"+{pct_24h:.2f}% >= 50% -> 1.0"
    elif pct_24h >= 20: return 0.8, f"+{pct_24h:.2f}% >= 20% -> 0.8"
    elif pct_24h >= 10: return 0.4, f"+{pct_24h:.2f}% >= 10% -> 0.4"
    else: return 0.0, f"+{pct_24h:.2f}% < 10% -> 0.0"


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Hoja Auditada v4 - {ts}")

    apewisdom = leer_ultimo(APEWISDOM_DIR, "apewisdom_trending_*.json")

    tokens = [
        {"id": "zcash", "symbol": "ZEC"},
        {"id": "lisk", "symbol": "LSK"},
        {"id": "fetch-ai", "symbol": "FET"},
        {"id": "bittensor", "symbol": "TAO"}
    ]

    for token in tokens:
        print(f"\n[YIN] ========== {token['symbol']} ==========")

        data = fetch_coingecko(f"/coins/{token['id']}", {
            "localization": False, "tickers": False,
            "market_data": True, "sparkline": False
        })

        if "error" in data:
            print(f"[YIN] SKIP: {data['error']}")
            continue

        market = data.get("market_data", {})
        # CRITICO: usar el mismo pct_24h para reportar Y calcular
        pct_24h = market.get("price_change_percentage_24h") or 0
        pct_7d = market.get("price_change_percentage_7d") or 0
        pct_30d = market.get("price_change_percentage_30d") or 0

        print(f"[YIN] Cambio 24h real: {pct_24h:.4f}%")

        # Senal mercado (con auditoria)
        s_mercado, s_mercado_razon = calcular_s_mercado(pct_24h)
        print(f"[YIN] s_mercado = {s_mercado} ({s_mercado_razon})")

        # Senal social
        aw = buscar_apewisdom(apewisdom, token["symbol"])
        if aw is None:
            s_social = 0.0
            aw_texto = "No en ApeWisdom"
            print(f"[YIN] s_social = 0.0 (no en ApeWisdom)")
        else:
            rank = aw.get("rank", 100)
            if rank <= 3: s_social = 1.0
            elif rank <= 10: s_social = 0.7
            elif rank <= 30: s_social = 0.4
            else: s_social = 0.1
            aw_texto = f"#{rank} con {aw.get('mentions')} menciones"
            print(f"[YIN] s_social = {s_social} (ApeWisdom #{rank})")

        # Senal narrativa: por ahora 0.0 (sin match fiable)
        s_narrativa = 0.0
        narr_texto = "Sin match fiable"
        print(f"[YIN] s_narrativa = 0.0 (sin match directo)")

        # Score con auditoria completa
        score_total = (s_mercado * 0.4) + (s_social * 0.3) + (s_narrativa * 0.3)
        print(f"[YIN] SCORE TOTAL = ({s_mercado}*0.4) + ({s_social}*0.3) + ({s_narrativa}*0.3) = {score_total:.4f}")

        # Clasificar
        if score_total > 0.75: nivel = "PREDICCION FUERTE"
        elif score_total > 0.65: nivel = "PREDICCION POSITIVA"
        elif score_total > 0.45: nivel = "OBSERVACION"
        elif score_total > 0.25: nivel = "MONITOREO"
        else: nivel = "DESCARTAR"

        # Generar hoja CON AUDITORIA
        hoja = f"""# HOJA AUDITADA v4 — {data.get('name', token['symbol']).upper()}
**ID:** PSM-{ts}-{token['symbol']}
**Score:** {score_total:.4f} ({nivel})

## 1. AUDITORIA DEL CALCULO
- **Cambio 24h real (CoinGecko):** {pct_24h:.4f}%
- **s_mercado (40%):** {s_mercado} — {s_mercado_razon}
- **s_social (30%):** {s_social} — {aw_texto}
- **s_narrativa (30%):** {s_narrativa} — {narr_texto}
- **CALCULO:** ({s_mercado}*0.4) + ({s_social}*0.3) + ({s_narrativa}*0.3) = **{score_total:.4f}**
- **Nivel:** {nivel}

## 2. DATOS DE MERCADO
- Precio: ${market.get('current_price', {}).get('usd', 'N/A')}
- Cambio 7d: {pct_7d:.2f}%
- Cambio 30d: {pct_30d:.2f}%
- Market Cap: ${market.get('market_cap', {}).get('usd', 0):,}
- Volumen 24h: ${market.get('total_volume', {}).get('usd', 0):,}

## 3. FUENTES
- CoinGecko: [DATO VERIFICADO]
- ApeWisdom: [DATO VERIFICADO] {aw_texto}

---
Generado: {ts}
"""
        out_path = INFORMES_DIR / f"hoja_v4_{token['symbol']}_{ts}.md"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(hoja)
        print(f"[YIN] Guardado: {out_path}")
        time.sleep(5)


if __name__ == "__main__":
    main()