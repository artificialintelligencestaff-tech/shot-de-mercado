#!/usr/bin/env python3
"""
script_37c_alert_profesional.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Alerta PROFESIONAL con formato visual claro, separaciones,
    emojis y explicacion de calculos. Disenado para usuarios
    no tecnicos que necesitan entender rapidamente.
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
    print(f"[YIN] Alerta Profesional Catwifout - {ts}")

    mensaje = f"""🔔 ALERTA DE OPORTUNIDAD
Proyecto Shot de Mercado
{ts}

━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ RESUMEN EJECUTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟢 OPORTUNIDAD DETECTADA

Token: catwifout
Red: Solana (blockchain rapida y economica)
Precio actual: $0.000869 USD
Market Cap: $861,000
Liquidez: $38,700

⚠️ CAMBIO DESDE DETECCION INICIAL:
📉 Precio: -7.3% (de $0.0009371 a $0.000869)
📉 Liquidez: -53% (de $82.5K a $38.7K)
🚨 ALERTA: Liquidez bajando rapido

━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ QUE ES ESTE TOKEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━

catwifout es una memecoin (moneda con proposito 
recreativo) lanzada hace apenas 2 horas.

Su nombre es una combinacion de:
- "cat" (gato)
- "wifout" (juego de palabras con "without")

Tiene presencia web y Twitter, lo cual indica 
que hay un equipo detras intentando construir 
una comunidad.

🔗 Web oficial: https://catwifout.fun/
🔗 Twitter: @catwifoutsol

━━━━━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ POR QUE LO DETECTAMOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━

El sistema aplico un scoring de 6 criterios.
Cada criterio vale hasta 100 puntos.

📊 CALCULOS:

1. Distribucion de holders: 20/20
   Top 10 holders = 8% (excelente)
   
2. Presion compradora: 20/20
   Ratio compras/ventas = 20.1:1
   
3. Score de seguridad: 20/20
   Mint revoked, Freeze revoked
   
4. Liquidez relativa: 10/20
   $38.7K (bajando)
   
5. Edad del token: 8/10
   2h (muy nuevo)
   
6. Market Cap: 10/10
   $861K (escala adecuada)

🎯 SCORE TOTAL: 88/100 = OPORTUNIDAD
Umbral minimo: 75/100

━━━━━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ RIESGOS Y ADVERTENCIAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ RIESGO 1: LIQUIDEZ BAJANDO
La liquidez cayo 53% en pocas horas.
Esto puede indicar que ballenas estan 
retirando capital. Puede ser el inicio de 
un "rug pull" (robo de fondos).

⚠️ RIESGO 2: TOKEN MUY NUEVO
2 horas de vida. No tiene historial.
Los tokens muy nuevos son 73% mas propensos 
a ser estafas.

⚠️ RIESGO 3: VOLATILIDAD ALTA
El precio puede moverse +50% o -50% en minutos.
Solo invertir lo que puedas perder.

🛑 NO INVERTIR MAS DE 1-2% DE TU CAPITAL
🛑 NO USAR TODO EL CAPITAL EN UNA SOLA COMPRA
🛑 VERIFICAR LA DIRECCION ANTES DE OPERAR

━━━━━━━━━━━━━━━━━━━━━━━━━━━
5️⃣ COMO COMPRARLO — PASO A PASO
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📱 METODO: Jupiter (agregador descentralizado)

Antes de empezar, entender 3 conceptos:

CONCEPTO 1 — WALLET
Es como una cuenta bancaria digital. Vas a 
instalar "Phantom", que es una wallet para 
Solana. Solo vos tenes acceso.

CONCEPTO 2 — SOL
Es la moneda nativa de Solana. La necesitas 
para comprar catwifout. Se compra en exchanges 
tradicionales (Binance, Coinbase, etc.).

CONCEPTO 3 — SWAP
Es un intercambio. Cambias SOL por catwifout 
directamente, sin intermediarios.

━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 PASO 1: INSTALAR PHANTOM
1. Abrir Chrome en tu computadora
2. Ir a: https://phantom.app
3. Click en "Download"
4. Elegir "Chrome Extension"
5. Click en "Add to Chrome"
6. Click en "Add Extension"
7. Click en el icono de Phantom (arriba derecha)
8. Click en "Create new wallet"
9. GUARDAR las 12 palabras en un lugar seguro
   (papel, NO foto, NO nube)
10. Confirmar las palabras

⏱️ Tiempo: 5 minutos

━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 PASO 2: COMPRAR SOL
1. Abrir una cuenta en Binance.com (o Coinbase)
2. Verificar identidad (KYC)
3. Depositar dinero via transferencia o tarjeta
4. Comprar SOL
5. Ir a "Wallet" → "Withdraw"
6. Seleccionar "SOL" (red: Solana)
7. Pegar tu direccion Phantom (copiar de Phantom)
8. Confirmar envio
9. Esperar 5-10 minutos

⏱️ Tiempo: 20-30 minutos (primera vez)

━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 PASO 3: CONECTAR PHANTOM A JUPITER
1. Ir a: https://jup.ag
2. Click en "Connect Wallet" (arriba derecha)
3. Seleccionar "Phantom"
4. Click en "Connect"
5. Aprobar en la ventana de Phantom

⏱️ Tiempo: 1 minuto

━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 PASO 4: BUSCAR CATWIFOUT
1. En Jupiter, click en el campo "Search"
2. Pegar esta direccion EXACTA:
   5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump
3. Verificar que aparezca "catwifout"
4. ⚠️ NO confiar en busquedas por nombre
   (hay tokens falsos con nombres similares)

⏱️ Tiempo: 30 segundos

━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 PASO 5: CONFIGURAR SLIPPAGE
"SLIPPAGE" = tolerancia al cambio de precio.
Si el precio cambia mientras tu transaccion 
se procesa, se cancela si supera el slippage.

1. Click en el icono de engranaje (arriba)
2. Ajustar "Slippage" a 5%
3. Si la transaccion falla, subir a 10%
4. NO subir mas de 15% (riesgo de pagar mal)

⏱️ Tiempo: 30 segundos

━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 PASO 6: EJECUTAR EL SWAP
1. En Jupiter, elegir cuanto SOL intercambiar
2. Ejemplo: 0.1 SOL (~$10)
3. Ver el precio estimado de catwifout
4. Click en "Swap"
5. Aprobar en Phantom
6. Esperar confirmacion (10-30 segundos)

⏱️ Tiempo: 1 minuto

━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 PASO 7: VERIFICAR LA COMPRA
1. Abrir Phantom
2. Ver si aparece "catwifout" en tu lista
3. Si no aparece, click en "Manage tokens"
4. Pegar la direccion de catwifout
5. Click en "Add"

Alternativa: verificar en Dexscreener
🔗 https://dexscreener.com/solana/GF5KiRvxGZ9ermv4A8cMaeHr1cCW6HwhSux8WN1Eyv4i

⏱️ Tiempo: 1 minuto

━━━━━━━━━━━━━━━━━━━━━━━━━━━
6️⃣ SEGUIMIENTO Y ACTUALIZACIONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━

El sistema registrara el precio de catwifout en:

⏱️ 1 hora post-alerta
⏱️ 6 horas post-alerta
⏱️ 24 horas post-alerta
⏱️ 7 dias post-alerta

Esto nos permitira medir si la prediccion fue 
correcta y ajustar la formula.

━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔗 HERRAMIENTAS DE VERIFICACION
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Dexscreener (precio y liquidez):
https://dexscreener.com/solana/GF5KiRvxGZ9ermv4A8cMaeHr1cCW6HwhSux8WN1Eyv4i

📊 Birdeye (analytics):
https://birdeye.so/token/5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump?chain=solana

📊 Solscan (explorador de bloques):
https://solscan.io/token/5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump

━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 NOTA IMPORTANTE

Esta alerta NO es una recomendacion de inversion.
Es un informe analitico de patrones detectados.
La decision final es responsabilidad de cada uno.

Los datos tecnicos provienen de:
- Deficlaw MCP (analyze_token, get_token_security)
- Dexscreener API (precios y liquidez)

Score del sistema: 88/100
Umbral minimo: 75/100

━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fuente: Proyecto Shot de Mercado
Metodologia: Analisis cuantitativo de 6 dimensiones
"""

    result = send_telegram(mensaje)
    print(f"[YIN] Resultado: {result}")

    # Guardar log
    log_dir = Path(r"D:\Proyecto Shot de mercado\03_Informes\alertas")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"alerta_profesional_catwifout_{ts}.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump({"mensaje": mensaje, "resultado": result, "timestamp": ts}, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Log guardado: {log_path}")


if __name__ == "__main__":
    main()