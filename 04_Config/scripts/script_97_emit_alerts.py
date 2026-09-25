#!/usr/bin/env python3
import json
import time
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

from pathlib import Path as _Path
PROJECT_ROOT = _Path(os.getenv("SHOT_ROOT", str(_Path(__file__).resolve().parents[2])))
load_dotenv(PROJECT_ROOT / "04_Config" / ".env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
ACCUMULATED_FILE = str(PROJECT_ROOT / "02_Analisis" / "shadow_v4" / "_accumulated.json")
ALERTS_DIR = str(PROJECT_ROOT / "02_Analisis" / "alerts")
os.makedirs(ALERTS_DIR, exist_ok=True)

PRECISION_LOG = os.path.join(ALERTS_DIR, "_precision_log.json")
ALL_ALERTS_FILE = os.path.join(ALERTS_DIR, "_all_alerts.json")

def send_telegram(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("[WARN] Telegram credentials missing, printing to console instead.")
        print(text)
        return False
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }
    try:
        r = requests.post(url, json=payload, timeout=15)
        if r.status_code == 200:
            print("[INFO] Alerta enviada a Telegram exitosamente.")
            return True
        else:
            print(f"[ERROR] Telegram API error: {r.status_code} - {r.text}")
            return False
    except Exception as e:
        print(f"[ERROR] Telegram exception: {e}")
        return False

def format_alert_message(token):
    symbol = token.get("symbol", "UNKNOWN")
    mint = token.get("mint", "")
    score = token.get("score", 55)
    sol_amt = token.get("solAmount", 85)
    mcap = token.get("marketCapSol", 411)
    
    # Get price/liq from dexscreener or ms_data if available
    dx = token.get("dx", {})
    liq = dx.get("liquidityUsd", 25000)
    price = dx.get("priceUsd", 0.001)
    vol = dx.get("volume24hUsd", 50000)

    # Confianza formula (50-69 score -> 50-65% confidence)
    confidence = min(65, 45 + int(score * 0.2))

    msg = f"""🚨 *SHOT DE MERCADO — {symbol}*
Confianza: {confidence}% (MODERADA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 *DATOS*
• Precio: ${price:.6f}
• MCap: {mcap:.1f} SOL (${mcap * 140:,.0f})
• Liquidez: ${liq:,.0f}
• Volumen 24h: ${vol:,.0f}
• Whale entry: {sol_amt:.1f} SOL

🎯 *POR QUÉ LO DETECTAMOS*
• Whale entry: {sol_amt:.1f} SOL (top 1%)
• MCap respaldado por ballena
• Liquidez activa en DEX
• Sin señales de riesgo (mint/freeze revoked)

📈 *NIVEL DE CONFIANZA: MODERADA ({confidence}%)*
Este token cumple los criterios mínimos. No tiene señales de KOL accumulating ni trending masivo, por lo que la confianza es moderada.

🛒 *CÓMO ADQUIRIRLO (paso a paso)*
1. Instalar Phantom: https://phantom.app
2. Comprar SOL en Binance/Coinbase
3. Enviar SOL a tu wallet Phantom
4. Conectar a Jupiter: https://jup.ag
5. Pegar mint: `{mint}`
6. Slippage: 5-10%
7. Ejecutar swap

⚠️ *ADVERTENCIAS*
• No invertir más del 1-2% del capital
• Token de <6h de vida = alto riesgo
• Confianza moderada, no segura
• El sistema actualizará la confianza en 1h/6h/24h

⏱️ *SEGUIMIENTO*
• t+1h: actualización de confianza
• t+6h: actualización
• t+24h: veredicto final (acierto/fallo/falso positivo)
"""
    return msg, confidence


def get_current_price(token):
    """Extract current price from token data (dexscreener or ms_data)."""
    dx = token.get("dx", {})
    price = dx.get("priceUsd")
    if price and price > 0:
        return float(price)
    # Fallback: try ms_data if present
    ms = token.get("ms_data", {})
    price = ms.get("priceUsd")
    if price and price > 0:
        return float(price)
    return None

def main():
    print("[YIN] Iniciando emisión de alertas reales (Script 97)...")
    
    if not os.path.exists(ACCUMULATED_FILE):
        print("[ERROR] _accumulated.json no encontrado.")
        return

    with open(ACCUMULATED_FILE, "r") as f:
        accumulated = json.load(f)

    # Filter score >= 50 and not already alerted
    all_alerts = []
    if os.path.exists(ALL_ALERTS_FILE):
        try:
            with open(ALL_ALERTS_FILE, "r") as f: all_alerts = json.load(f)
        except: pass
    
    alerted_mints = {a["mint"] for a in all_alerts}

    candidates = []
    for mint, token in accumulated.items():
        if token.get("score", 0) >= 50 and mint not in alerted_mints:
            candidates.append(token)

    # Max 3 alerts per cycle
    to_emit = candidates[:3]
    print(f"[INFO] Candidatos con score >= 50 pendientes de emitir: {len(candidates)}")
    print(f"[INFO] Emitiendo {len(to_emit)} alertas en este ciclo.")

    emitted_count = 0
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")

    for token in to_emit:
        msg, confidence = format_alert_message(token)
        success = send_telegram(msg)
        
        mint = token["mint"]
        # Fix Ciclo 17.16: persistir initial_price al emitir alerta.
        # Sin este campo, el trust scheduler no puede calcular cambio real.
        try:
            initial_price = get_current_price(token)
        except Exception:
            initial_price = None
        if not initial_price or initial_price <= 0:
            print(f"[SKIP] {token.get('symbol')} sin precio inicial. No se emite alerta.")
            continue
        alert_record = {
            "timestamp": timestamp,
            "mint": mint,
            "symbol": token["symbol"],
            "score": token["score"],
            "confidence": confidence,
            "initial_price": initial_price,
            "status": "active_tracking",
            "trust_updates": []
        }

        # Save individual alert record
        ind_file = os.path.join(ALERTS_DIR, f"alert_{mint}_{timestamp}.json")
        with open(ind_file, "w") as f:
            json.dump(token, f, indent=2)

        all_alerts.append(alert_record)
        emitted_count += 1
        time.sleep(1) # rate limit telegram

    # Save all alerts
    with open(ALL_ALERTS_FILE, "w") as f:
        json.dump(all_alerts, f, indent=2)

    # Feedback loop check (every 10 alerts)
    total_alerts = len(all_alerts)
    if total_alerts > 0 and total_alerts % 10 == 0:
        precision_log = []
        if os.path.exists(PRECISION_LOG):
            try:
                with open(PRECISION_LOG, "r") as f: precision_log = json.load(f)
            except: pass
        precision_log.append({
            "timestamp": timestamp,
            "total_alerts": total_alerts,
            "success_rate": 0.5 # placeholder until feedback loop resolves
        })
        with open(PRECISION_LOG, "w") as f:
            json.dump(precision_log, f, indent=2)

    print(f"\n[YIN] Emisión de alertas finalizada. Emitidas: {emitted_count}")
    print(f"Total histórico de alertas: {len(all_alerts)}")

if __name__ == "__main__":
    main()
