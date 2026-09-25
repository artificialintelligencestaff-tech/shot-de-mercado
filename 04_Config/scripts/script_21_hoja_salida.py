#!/usr/bin/env python3
"""
script_21_hoja_salida.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Generar la hoja de salida final del bot con 9 secciones.
    Combina datos de todas las fuentes activas.
    Output: informe estructurado en Markdown.
"""

import json
import requests
import time
from datetime import datetime, timezone
from pathlib import Path

COINGECKO_BASE = "https://api.coingecko.com/api/v3"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
INFORMES_DIR = PROJECT_ROOT / "03_Informes" / "hojas_salida"
INFORMES_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30


def fetch_coingecko(endpoint, params=None):
    try:
        url = f"{COINGECKO_BASE}{endpoint}"
        response = requests.get(url, params=params or {}, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def generar_hoja(token_id, symbol):
    """Genera la hoja de salida para un token."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")

    # Obtener datos
    data = fetch_coingecko(f"/coins/{token_id}", {
        "localization": False,
        "tickers": False,
        "market_data": True,
        "community_data": True,
        "developer_data": True,
        "sparkline": False
    })

    if "error" in data:
        return {"error": data["error"], "token": token_id}

    market = data.get("market_data", {})
    pct_24h = market.get("price_change_percentage_24h") or 0
    pct_7d = market.get("price_change_percentage_7d") or 0
    pct_30d = market.get("price_change_percentage_30d") or 0

    # Calcular score simple
    score_lider = min(pct_30d / 100, 1.0) if pct_30d > 0 else 0
    score_mercado = 1.0 if pct_24h >= 20 else (0.5 if pct_24h >= 10 else 0)
    score_total = (score_lider + score_mercado) / 2

    # Clasificar nivel
    if score_total > 0.75:
        nivel = "PREDICCION FUERTE"
    elif score_total > 0.65:
        nivel = "PREDICCION POSITIVA"
    elif score_total > 0.45:
        nivel = "OBSERVACION"
    else:
        nivel = "DESCARTAR"

    # Generar Markdown
    hoja = f"""# HOJA DE ACTIVO — {data.get('name', symbol).upper()}
**ID:** PSM-{ts}
**Fecha:** {ts}
**Score:** {score_total:.2f} ({nivel})

---

## 1. IDENTIFICACION
- **Nombre:** {data.get('name', 'N/A')}
- **Simbolo:** {data.get('symbol', 'N/A').upper()}
- **Red:** {', '.join(list((data.get('platforms') or {}).keys())[:3])}
- **Categorias:** {', '.join(data.get('categories', [])[:5])}

## 2. DATOS DE MERCADO
- **Precio:** ${market.get('current_price', {}).get('usd', 'N/A')}
- **Cambio 24h:** {pct_24h:.2f}%
- **Cambio 7d:** {pct_7d:.2f}%
- **Cambio 30d:** {pct_30d:.2f}%
- **Market Cap:** ${market.get('market_cap', {}).get('usd', 'N/A'):,}
- **Volumen 24h:** ${market.get('total_volume', {}).get('usd', 'N/A'):,}
- **Circulating Supply:** {market.get('circulating_supply', 'N/A'):,}
- **Total Supply:** {market.get('total_supply', 'N/A')}

## 3. ANALISIS FUNDAMENTAL
- **Descripcion:** {data.get('description', {}).get('en', 'N/A')[:500]}
- **Genesis Date:** {data.get('genesis_date', 'N/A')}
- **Homepage:** {data.get('links', {}).get('homepage', ['N/A'])[0]}

## 4. NARRATIVAS ACTIVAS
- **Categorias:** {', '.join(data.get('categories', [])[:10])}
- **Convergencia:** {len(data.get('categories', []))} categorias

## 5. HISTERIA SOCIAL
- **Twitter Followers:** {data.get('community_data', {}).get('twitter_followers', 'N/A')}
- **Reddit Subscribers:** {data.get('community_data', {}).get('reddit_subscribers', 'N/A')}
- **Telegram Users:** {data.get('community_data', {}).get('telegram_channel_user_count', 'N/A')}

## 6. NOTICIAS Y FUENTES
- **Fuente de datos:** CoinGecko
- **Ultima actualizacion:** {market.get('last_updated', 'N/A')}

## 7. PROBABILIDAD DE EXPANSION
- **Score:** {score_total:.2f}
- **Nivel:** {nivel}
- **Horizonte:** 15-45 dias
- **Confianza:** {'Alta' if score_total > 0.75 else 'Media' if score_total > 0.45 else 'Baja'}

## 8. DONDE COMPRAR (paso a paso)
1. **Plataforma:** Binance, Coinbase, Kraken (verificar disponibilidad por pais)
2. **Registro:** Crear cuenta con email + verificacion KYC
3. **Deposito:** Transferencia bancaria o tarjeta
4. **Compra:** Orden a mercado o limite segun precio
5. **Transferencia:** Mover a wallet personal (no dejar en exchange)

## 9. MATRIZ DE RIESGO
- **Rug pull:** {'Alto' if len(data.get('categories', [])) < 3 else 'Medio'}
- **Manipulacion:** {'Alto' if market.get('market_cap', {}).get('usd', 0) < 10000000 else 'Medio'}
- **Regulatorio:** Depende de jurisdiccion
- **Liquidez:** {'Bajo' if market.get('total_volume', {}).get('usd', 0) > 1000000 else 'Alto'}

---

**Etiqueta global:** [DATO VERIFICADO / INFERENCIA ESTRUCTURAL]
**Fuente:** CoinGecko API
**Generado por:** Proyecto Shot de Mercado
"""

    return {
        "hoja": hoja,
        "token": token_id,
        "symbol": symbol,
        "score": score_total,
        "nivel": nivel,
        "timestamp": ts
    }


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Hoja de Salida - {ts}")

    # Tokens a generar hoja
    tokens = [
        ("zcash", "ZEC"),
        ("lisk", "LSK"),
        ("fetch-ai", "FET"),
        ("bittensor", "TAO")
    ]

    for token_id, symbol in tokens:
        print(f"[YIN] Generando hoja para {symbol}...")
        try:
            resultado = generar_hoja(token_id, symbol)
            if "error" in resultado:
                print(f"[YIN] Error en {symbol}: {resultado['error']}")
                continue

            # Guardar
            out_path = INFORMES_DIR / f"hoja_{symbol}_{ts}.md"
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(resultado["hoja"])
            print(f"[YIN] Guardado: {out_path} (score: {resultado['score']:.2f}, {resultado['nivel']})")

            # Guardar tambien como JSON para procesamiento
            json_path = INFORMES_DIR / f"hoja_{symbol}_{ts}.json"
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(resultado, f, indent=2, ensure_ascii=False)

        except Exception as e:
            print(f"[YIN] Error en {symbol}: {e}")
        time.sleep(5)  # Rate limit

    print("[YIN] Script 21 finalizado.")


if __name__ == "__main__":
    main()