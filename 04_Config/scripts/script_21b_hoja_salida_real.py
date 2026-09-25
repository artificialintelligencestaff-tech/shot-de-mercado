#!/usr/bin/env python3
"""
script_21b_hoja_salida_real.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Version 2 corregida. En lugar de inventar datos, LEE los archivos
    generados por los scripts previos y cruza informacion real.
    Fuentes cruzadas:
    - CoinGecko (precios, categorias)
    - ApeWisdom (menciones Reddit)
    - NarrativeScope (narrativas GitHub)
    - CoinLobster (ballenas)
    - Deep Blue Alpha (whale index)
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
COINLOBSTER_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "onchain" / "coinlobster_auth"
DEEPBLUE_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "onchain"

INFORMES_DIR.mkdir(parents=True, exist_ok=True)
TIMEOUT = 30


def leer_ultimo_archivo(directorio, patron):
    """Lee el archivo mas reciente que coincide con el patron."""
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


def buscar_en_apewisdom(apewisdom_data, symbol):
    """Busca el symbol en los datos de ApeWisdom."""
    if not apewisdom_data:
        return None
    results = apewisdom_data.get("results", [])
    for r in results:
        if r.get("ticker", "").upper().startswith(symbol.upper()):
            return {
                "rank": r.get("rank"),
                "mentions": r.get("mentions"),
                "upvotes": r.get("upvotes"),
                "rank_24h_ago": r.get("rank_24h_ago"),
                "mentions_24h_ago": r.get("mentions_24h_ago")
            }
    return None


def buscar_en_narrativas(narrativas_data, keyword):
    """Busca una narrativa en el archivo de NarrativeScope."""
    if not narrativas_data:
        return None
    for n in narrativas_data.get("narrativas", []):
        if keyword.lower() in n.get("narrativa", "").lower():
            return n
    return None


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Hoja de Salida v2 (real) - {ts}")

    # Leer archivos previos
    print("[YIN] Leyendo datos previos...")
    apewisdom = leer_ultimo_archivo(APEWISDOM_DIR, "apewisdom_trending_*.json")
    narrativescope = leer_ultimo_archivo(NARRATIVAS_DIR, "narrativescope_*.json")
    coinlobster = leer_ultimo_archivo(COINLOBSTER_DIR, "whale_radar_*.json")
    deepblue = leer_ultimo_archivo(DEEPBLUE_DIR, "deepblue_*.json")

    print(f"[YIN] ApeWisdom cargado: {'SI' if apewisdom else 'NO'}")
    print(f"[YIN] NarrativeScope cargado: {'SI' if narrativescope else 'NO'}")
    print(f"[YIN] CoinLobster cargado: {'SI' if coinlobster else 'NO'}")
    print(f"[YIN] Deep Blue cargado: {'SI' if deepblue else 'NO'}")

    # Tokens a procesar
    tokens = [
        {"id": "zcash", "symbol": "ZEC", "keyword": "ZEC"},
        {"id": "lisk", "symbol": "LSK", "keyword": "LSK"}
    ]

    for token in tokens:
        print(f"[YIN] Procesando {token['symbol']}...")

        # CoinGecko (fuente real)
        data = fetch_coingecko(f"/coins/{token['id']}", {
            "localization": False, "tickers": False,
            "market_data": True, "sparkline": False
        })

        if "error" in data:
            print(f"[YIN] Error CoinGecko para {token['symbol']}")
            continue

        market = data.get("market_data", {})
        pct_24h = market.get("price_change_percentage_24h") or 0
        pct_7d = market.get("price_change_percentage_7d") or 0
        pct_30d = market.get("price_change_percentage_30d") or 0

        # ApeWisdom real
        aw_data = buscar_en_apewisdom(apewisdom, token["symbol"])

        # Narrativa real (buscando por categorias del token)
        categorias_token = data.get("categories", [])
        narrativa_match = None
        for cat in categorias_token:
            n = buscar_en_narrativas(narrativescope, cat)
            if n:
                narrativa_match = n
                break

        # CALCULAR SCORE CON DATOS REALES
        # Señal mercado: basada en cambio 24h (con umbral >20%)
        if pct_24h >= 50:
            s_mercado = 1.0
        elif pct_24h >= 20:
            s_mercado = 0.8
        elif pct_24h >= 10:
            s_mercado = 0.4
        else:
            s_mercado = 0.0

        # Señal social: basada en ApeWisdom (si esta)
        if aw_data:
            rank = aw_data.get("rank", 100)
            if rank <= 3:
                s_social = 1.0
            elif rank <= 10:
                s_social = 0.7
            elif rank <= 30:
                s_social = 0.4
            else:
                s_social = 0.1
        else:
            s_social = 0.0

        # Señal narrativa: basada en NarrativeScope
        if narrativa_match:
            score_dev = narrativa_match.get("score_desarrollo", 0)
            s_narrativa = score_dev / 40  # Normalizar a 0-1
        else:
            s_narrativa = 0.0

        # Score total (3 señales verificables)
        score_total = (s_mercado + s_social + s_narrativa) / 3

        # Clasificar
        if score_total > 0.75:
            nivel = "PREDICCION FUERTE"
        elif score_total > 0.65:
            nivel = "PREDICCION POSITIVA"
        elif score_total > 0.45:
            nivel = "OBSERVACION"
        else:
            nivel = "DESCARTAR"

        # Generar hoja con datos REALES
        hoja = f"""# HOJA DE ACTIVO — {data.get('name', token['symbol']).upper()}

**ID:** PSM-{ts}-{token['symbol']}
**Fecha:** {ts}
**Score total:** {score_total:.2f} ({nivel})

---

## 1. DATOS DE MERCADO (fuente: CoinGecko)
- **Precio:** ${market.get('current_price', {}).get('usd', 'N/A')}
- **Cambio 24h:** {pct_24h:.2f}% {'(CUMPLE >20%)' if pct_24h >= 20 else '(no cumple umbral >20%)'}
- **Cambio 7d:** {pct_7d:.2f}%
- **Cambio 30d:** {pct_30d:.2f}%
- **Market Cap:** ${market.get('market_cap', {}).get('usd', 0):,}
- **Volumen 24h:** ${market.get('total_volume', {}).get('usd', 0):,}

## 2. SEÑALES CALCULADAS
- **Señal mercado:** {s_mercado:.2f} (basada en cambio 24h)
- **Señal social:** {s_social:.2f} (basada en ApeWisdom)
- **Señal narrativa:** {s_narrativa:.2f} (basada en NarrativeScope)
- **Score total:** {score_total:.2f}
- **Nivel:** {nivel}

## 3. HISTERIA SOCIAL (fuente: ApeWisdom Reddit)
"""
        if aw_data:
            hoja += f"""- **Ranking Reddit:** #{aw_data.get('rank')}
- **Menciones:** {aw_data.get('mentions')}
- **Upvotes:** {aw_data.get('upvotes')}
- **Ranking 24h atras:** #{aw_data.get('rank_24h_ago')}
- **Menciones 24h atras:** {aw_data.get('mentions_24h_ago')}
"""
        else:
            hoja += "- **No aparece en ApeWisdom top 109**\n"

        hoja += f"""
## 4. NARRATIVA ASOCIADA (fuente: NarrativeScope GitHub)
"""
        if narrativa_match:
            hoja += f"""- **Narrativa:** {narrativa_match.get('narrativa')}
- **Repos 90d:** {narrativa_match.get('repos_recientes_90d')}
- **Stars promedio:** {narrativa_match.get('stars_promedio')}
- **Score desarrollo:** {narrativa_match.get('score_desarrollo')}/40
"""
        else:
            hoja += "- **Sin match directo en narrativas**\n"

        hoja += f"""
## 5. CATEGORIAS (fuente: CoinGecko)
{', '.join(categorias_token[:10])}

## 6. ETIQUETADO Y FUENTES
- **Datos de mercado:** [DATO VERIFICADO] CoinGecko
- **Datos sociales:** [DATO VERIFICADO] ApeWisdom
- **Datos narrativas:** [DATO VERIFICADO] NarrativeScope
- **Score calculado:** [INFERENCIA ESTRUCTURAL] Formula YANG

---

**Generado por:** Proyecto Shot de Mercado — Hoja v2 (real)
"""

        # Guardar
        out_path = INFORMES_DIR / f"hoja_real_{token['symbol']}_{ts}.md"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(hoja)
        print(f"[YIN] Guardado: {out_path} (score: {score_total:.2f}, {nivel})")

        time.sleep(5)

    print("[YIN] Script 21b finalizado.")


if __name__ == "__main__":
    main()