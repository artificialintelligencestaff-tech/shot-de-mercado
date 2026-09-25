#!/usr/bin/env python3
"""
script_37d_alert_multipart.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Alerta profesional dividida en 3 mensajes.
    Cada mensaje < 4096 caracteres (limite Telegram).
"""

import json
import os
import time
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path(r"D:\Proyecto Shot de Mercado\04_Config\.env")
load_dotenv(ENV_PATH)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
TIMEOUT = 30


def send_message(text):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return {"error": "Credenciales no configuradas"}
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    try:
        response = requests.post(TELEGRAM_URL, json=payload, timeout=TIMEOUT)
        return {"http_status": response.status_code, "body": response.text[:200]}
    except Exception as e:
        return {"error": str(e)}


def build_messages():
    """Construye los 3 mensajes de la alerta."""

    # === MENSAJE 1: RESUMEN + QUE ES + POR QUE ===
    msg1 = """🔔 ALERTA DE OPORTUNIDAD
Proyecto Shot de Mercado
[1/3]

━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 RESUMEN EJECUTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━

🟢 OPORTUNIDAD DETECTADA

Token: catwifout
Red: Solana
Precio: $0.000869 USD
Market Cap: $861,000
Liquidez: $38,700

⚠️ CAMBIO DESDE DETECCION:
📉 Precio: -7.3%
📉 Liquidez: -57.8% (ALERTA)
🚨 Liquidez cayendo rapido

━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 QUE ES ESTE TOKEN
━━━━━━━━━━━━━━━━━━━━━━━━━━

catwifout es una memecoin lanzada hace 2 horas.
Combinacion de "cat" + "wifout" (juego de palabras).

Tiene web y Twitter oficial, lo cual indica
que hay un equipo detras.

🔗 Web: https://catwifout.fun/
🔗 Twitter: @catwifoutsol

━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 POR QUE LO DETECTAMOS
━━━━━━━━━━━━━━━━━━━━━━━━━━

El sistema aplico un scoring de 6 criterios:

1. Distribucion holders: 20/20
   Top 10 = 8% (excelente)
2. Presion compradora: 20/20
   Ratio = 20.1:1
3. Seguridad: 20/20
   Mint/Freeze revoked
4. Liquidez: 10/20
   $38.7K y bajando
5. Edad: 8/10
   2h (muy nuevo)
6. Market Cap: 10/10
   $861K

SCORE TOTAL: 88/100 = OPORTUNIDAD
Umbral minimo: 75/100

Continua en [2/3]"""

    # === MENSAJE 2: RIESGOS + PASOS 1-4 ===
    msg2 = """🔔 ALERTA - Continuacion
Proyecto Shot de Mercado
[2/3]

━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ RIESGOS Y ADVERTENCIAS
━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ RIESGO 1: LIQUIDEZ BAJANDO
Cayo 57% en pocas horas. Puede ser el
inicio de un "rug pull" (robo de fondos).

⚠️ RIESGO 2: TOKEN NUEVO
2 horas de vida, sin historial.
73% de tokens nuevos son estafas.

⚠️ RIESGO 3: VOLATILIDAD
Puede moverse +50% o -50% en minutos.

🛑 NO INVERTIR MAS DE 1-2% DEL CAPITAL
🛑 NO USAR TODO EN UNA SOLA COMPRA
🛑 VERIFICAR DIRECCION ANTES DE OPERAR

━━━━━━━━━━━━━━━━━━━━━━━━━━
🛒 COMO COMPRARLO - PASOS 1-4
━━━━━━━━━━━━━━━━━━━━━━━━━━

📱 METODO: Jupiter (agregador DEX)

CONCEPTOS BASICOS:

WALLET: cuenta digital para guardar crypto.
Vas a instalar "Phantom".

SOL: moneda nativa de Solana. Se compra
en exchanges (Binance, Coinbase).

SWAP: intercambio directo SOL por token.

━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 PASO 1: INSTALAR PHANTOM
━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Ir a https://phantom.app
2. Click en "Download"
3. Elegir "Chrome Extension"
4. Click en "Add to Chrome"
5. Click en "Create new wallet"
6. GUARDAR las 12 palabras en papel
   (NO foto, NO nube)
7. Confirmar palabras

Tiempo: 5 minutos

━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 PASO 2: COMPRAR SOL
━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Cuenta en Binance.com o Coinbase
2. Verificar identidad (KYC)
3. Depositar dinero
4. Comprar SOL
5. Retirar a tu Phantom
6. Red: Solana (SPL)
7. Esperar 5-10 minutos

Tiempo: 20-30 min

━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 PASO 3: CONECTAR PHANTOM A JUPITER
━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Ir a https://jup.ag
2. Click en "Connect Wallet"
3. Seleccionar Phantom
4. Aprobar conexion

Tiempo: 1 minuto

━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 PASO 4: BUSCAR CATWIFOUT
━━━━━━━━━━━━━━━━━━━━━━━━━━
1. En Jupiter, campo "Search"
2. Pegar direccion EXACTA:
5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump
3. Verificar que aparezca "catwifout"

⚠️ NO confiar en busquedas por nombre
(hay tokens falsos similares)

Tiempo: 30 segundos

Continua en [3/3]"""

    # === MENSAJE 3: PASOS 5-7 + VERIFICACION + SEGUIMIENTO ===
    msg3 = """🔔 ALERTA - Continuacion final
Proyecto Shot de Mercado
[3/3]

━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 PASO 5: CONFIGURAR SLIPPAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━

SLIPPAGE = tolerancia al cambio de precio.
Si el precio se mueve mas de lo permitido,
la transaccion se cancela.

1. Click en engranaje (arriba)
2. Ajustar a 5%
3. Si falla, subir a 10%
4. NO pasar de 15%

Tiempo: 30 segundos

━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 PASO 6: EJECUTAR SWAP
━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Elegir cuanto SOL cambiar
   Ejemplo: 0.1 SOL (~$10)
2. Ver precio estimado
3. Click en "Swap"
4. Aprobar en Phantom
5. Esperar 10-30 segundos

Tiempo: 1 minuto

━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 PASO 7: VERIFICAR
━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Abrir Phantom
2. Ver si aparece "catwifout"
3. Si no, click en "Manage tokens"
4. Pegar direccion y agregar

Tiempo: 1 minuto

━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 HERRAMIENTAS DE VERIFICACION
━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Dexscreener (precio/liquidez):
https://dexscreener.com/solana/GF5KiRvxGZ9ermv4A8cMaeHr1cCW6HwhSux8WN1Eyv4i

📊 Birdeye (analytics):
https://birdeye.so/token/5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump?chain=solana

📊 Solscan (explorador):
https://solscan.io/token/5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump

━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ ANTES DE OPERAR - CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━

[ ] Mint address verificada en Solscan
[ ] Liquidez del pool > $50,000 (esto
    NO es tu capital, es el total en el
    pool del token)
[ ] Sin reportes de rug en X/Twitter
[ ] Monto maximo definido (1-2% capital)

━━━━━━━━━━━━━━━━━━━━━━━━━━
⏱️ SEGUIMIENTO
━━━━━━━━━━━━━━━━━━━━━━━━━━

El sistema registrara precio cada:
• 1h / 6h / 24h / 7d

Esto permite medir si la prediccion
fue correcta y ajustar la formula.

━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ Esta alerta NO es recomendacion de
inversion. Es un informe analitico.
La decision final es tuya.

Fuente: Deficlaw + Dexscreener
Score: 88/100 | Umbral: 75/100"""

    return [msg1, msg2, msg3]


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Alerta Multipart - {ts}")

    mensajes = build_messages()
    print(f"[YIN] Enviando {len(mensajes)} mensajes...")

    resultados = []
    for i, msg in enumerate(mensajes, 1):
        print(f"[YIN]   Mensaje {i}/{len(mensajes)} ({len(msg)} chars)...")
        result = send_message(msg)
        resultados.append({"part": i, "chars": len(msg), "result": result})
        time.sleep(1.5)  # Evitar rate limit

    # Guardar log
    log_dir = Path(r"D:\Proyecto Shot de Mercado\03_Informes\alertas")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"alerta_multipart_{ts}.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": ts,
            "total_mensajes": len(mensajes),
            "mensajes": [{"n": i+1, "chars": len(m), "preview": m[:100]} for i, m in enumerate(mensajes)],
            "resultados": resultados
        }, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Log guardado: {log_path}")

    exitos = sum(1 for r in resultados if r["result"].get("http_status") == 200)
    print(f"[YIN] Entregados: {exitos}/{len(mensajes)}")


if __name__ == "__main__":
    main()