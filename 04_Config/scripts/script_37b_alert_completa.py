#!/usr/bin/env python3
"""
script_37b_alert_completa.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Alerta COMPLETA con instrucciones de adquisicion paso a paso.
"""

import json
import os
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path(r"D:\Proyecto Shot de mercado\04_Config\.env")
load_dotenv(ENV_PATH)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
TIMEOUT = 30


def send_telegram(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return {"error": "Credenciales no configuradas"}
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        response = requests.post(TELEGRAM_URL, json=payload, timeout=TIMEOUT)
        return {"http_status": response.status_code, "body": response.text[:500]}
    except Exception as e:
        return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Alerta Completa Catwifout - {ts}")

    mensaje = f"""ALERTA - PROYECTO SHOT DE MERCADO
Timestamp: {ts}

=========================================
OPORTUNIDAD DETECTADA: CATWIFOUT
=========================================

RED: Solana (SPL Token)
TOKEN: Catwifout
ADDRESS (MINT): 5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump
PAIR ADDRESS: GF5KiRvxGZ9ermv4A8cMaeHr1cCW6HwhSux8WN1Eyv4i

-----------------------------------------
VERDICT Y DATOS
-----------------------------------------
Verdict Deficlaw: STRONG BUY
Risk Score: 12/100 (LOW)

Precio actual: $0.0009371
Market Cap: $928.9K
Liquidez: $82.5K
Volumen 24h: $744.1K
Top 10 holders: 8.0% (excelente distribucion)
Buy pressure: 20.1:1
Holders rentables: 99%
Security: SAFE (mint/freeze revoked)

Score del sistema: 0.92 (OPORTUNIDAD)
Umbral: >0.75

-----------------------------------------
DONDE COMPRAR - PASO A PASO
-----------------------------------------

PLATAFORMA PRINCIPAL: Jupiter Aggregator
- Web: https://jup.ag
- DEX subyacente: PumpSwap
- Slippage recomendado: 5-10% (token nuevo)

PASOS DE ADQUISICION:

1. INSTALAR WALLET PHANTOM
   - Web: https://phantom.app
   - Descargar extension para Chrome/Brave
   - O app movil iOS/Android
   - Crear wallet nueva
   - GUARDAR seed phrase en lugar seguro (12 palabras)

2. FONDEAR CON SOL
   - Comprar SOL en cualquier exchange (Binance, Coinbase, Kraken)
   - Enviar SOL a la address de tu wallet Phantom
   - Recomendado: minimo 0.5 SOL para operar comodo
   - Dejar 0.01 SOL extra para gas

3. CONECTAR PHANTOM A JUPITER
   - Ir a https://jup.ag
   - Click en "Connect Wallet"
   - Seleccionar Phantom
   - Aprobar conexion

4. PEGAR LA MINT ADDRESS
   - En Jupiter, buscar el campo de input
   - Pegar: 5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump
   - Verificar que aparezca "Catwifout"

5. CONFIGURAR SLIPPAGE
   - Click en icono de settings (arriba derecha)
   - Ajustar slippage a 5% (o hasta 10% si falla)
   - Confirmar

6. EJECUTAR SWAP
   - Elegir monto de SOL a intercambiar
   - Click en "Swap"
   - Confirmar en Phantom
   - Esperar confirmacion (10-30 segundos)

7. VERIFICAR EN DEXSCREENER
   - Web: https://dexscreener.com/solana/GF5KiRvxGZ9ermv4A8cMaeHr1cCW6HwhSux8WN1Eyv4i
   - Confirmar que el token aparece en tu wallet

-----------------------------------------
WARNINGS CRITICOS
-----------------------------------------

- NO envies SOL a la mint address directamente. Solo se compra via swap.
- VERIFICA la mint address caracter por caracter antes de operar.
- USA solo wallets propias. No exchanges centralizados (no listan este token).
- SLIPPAGE alto = mas riesgo de precio desfavorable.
- Posicion recomendada: max 1-2% del capital (token de 2h de vida).
- NO uses todo el capital en una sola compra.

-----------------------------------------
HERRAMIENTAS DE VERIFICACION
-----------------------------------------

- Dexscreener: https://dexscreener.com/solana/GF5KiRvxGZ9ermv4A8cMaeHr1cCW6HwhSux8WN1Eyv4i
- Birdeye: https://birdeye.so/token/5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump?chain=solana
- Solscan: https://solscan.io/token/5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump

-----------------------------------------
SIGUIENTE PASO
-----------------------------------------

Antes de ejecutar cualquier operacion:
1. Verificar la mint address en Solscan
2. Confirmar liquidez >$50K
3. Revisar si hay reportes de rug en X/Twitter
4. Definir monto maximo (1-2% capital)

Fuente: Deficlaw analyze_token + get_token_security + Dexscreener
"""

    result = send_telegram(mensaje)
    print(f"[YIN] Resultado: {result}")

    # Guardar log
    log_dir = Path(r"D:\Proyecto Shot de mercado\03_Informes\alertas")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"alerta_completa_catwifout_{ts}.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump({"mensaje": mensaje, "resultado": result, "timestamp": ts}, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Log guardado: {log_path}")


if __name__ == "__main__":
    main()