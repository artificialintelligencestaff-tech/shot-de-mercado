#!/usr/bin/env python3
import json
import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

from pathlib import Path as _Path
PROJECT_ROOT = _Path(os.getenv("SHOT_ROOT", str(_Path(__file__).resolve().parents[2])))
load_dotenv(PROJECT_ROOT / "04_Config" / ".env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
ALERTS_DIR = str(PROJECT_ROOT / "02_Analisis" / "alerts")
ALL_ALERTS_FILE = os.path.join(ALERTS_DIR, "_all_alerts.json")
PRECISION_LOG = os.path.join(ALERTS_DIR, "_precision_log.json")
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/tokens/"

def send_telegram(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print(f"[WARN] Telegram missing. Msg: {text[:50]}...")
        return False
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown", "disable_web_page_preview": True}
    try:
        r = requests.post(url, json=payload, timeout=15)
        return r.status_code == 200
    except:
        return False

def get_current_price(mint):
    try:
        r = requests.get(f"{DEXSCREENER_API}{mint}", timeout=10)
        if r.status_code == 200:
            data = r.json()
            pairs = data.get("pairs", [])
            if pairs:
                best = max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0))
                return float(best.get("priceUsd", 0) or 0)
    except:
        pass
    return None

def main():
    print("[YIN] Ejecutando Trust Update Scheduler (Script 98)...")
    if not os.path.exists(ALL_ALERTS_FILE):
        print("[INFO] No hay alertas en _all_alerts.json para actualizar.")
        return

    with open(ALL_ALERTS_FILE, "r") as f:
        all_alerts = json.load(f)

    updated_any = False
    now = datetime.utcnow()

    for alert in all_alerts:
        mint = alert["mint"]
        symbol = alert["symbol"]
        initial_score = alert["score"]
        base_confidence = alert["confidence"]
        
        # Parse emit timestamp
        # alert["timestamp"] format: YYYY-MM-DD_HHMMSS
        try:
            emit_time = datetime.strptime(alert["timestamp"], "%Y-%m-%d_%H%M%S")
        except:
            continue

        # Get original price if stored, or fetch baseline (we approximate baseline from DEX or alert record if stored)
        # For simplicity, we store/fetch current price and compare with initial expected price
        current_price = get_current_price(mint)
        if not current_price:
            print(f"[SKIP] {symbol} ({mint[:8]}...) sin precio consultable. Se reintentará en el próximo ciclo.")
            continue

        trust_updates = alert.setdefault("trust_updates", [])
        completed_stages = {u["stage"] for u in trust_updates}

        # Determine which stage is due
        age_hours = (now - emit_time).total_seconds() / 3600.0

        stages_to_check = [
            ("t+1h", 1.0),
            ("t+6h", 6.0),
            ("t+24h", 24.0)
        ]

        for stage, threshold_hours in stages_to_check:
            if stage not in completed_stages and age_hours >= threshold_hours:
                # Perform update
                # For baseline comparison, let's look at trust_updates history or fetch previous price
                # Fix baseline (Ciclo 17.15): comparar contra initial_price si existe.
                # Fallback 1: primer trust_update. Fallback 2: backfill con precio actual.
                if alert.get("initial_price") and alert["initial_price"] > 0:
                    prev_price = alert["initial_price"]
                elif trust_updates:
                    prev_price = trust_updates[0].get("price", current_price)
                else:
                    print(f"[WARN] {symbol} sin initial_price ni historial. Backfill = current_price.")
                    alert["initial_price"] = current_price
                    prev_price = current_price
                
                price_change_pct = 0.0
                if prev_price > 0:
                    price_change_pct = ((current_price - prev_price) / prev_price) * 100.0

                conf_delta = 0
                verdict_stage = "NEUTRAL"
                if price_change_pct >= 20:
                    conf_delta = 15
                    verdict_stage = "ACIERTO"
                elif price_change_pct <= -50:
                    conf_delta = -100 # triggers 0
                    verdict_stage = "FALSO POSITIVO"
                elif price_change_pct <= -20:
                    conf_delta = -25
                    verdict_stage = "FALLO"

                new_confidence = max(0, min(95, round(base_confidence + conf_delta)))

                update_record = {
                    "stage": stage,
                    "timestamp": now.strftime("%Y-%m-%d_%H%M%S"),
                    "price": current_price,
                    "price_change_pct": round(price_change_pct, 2),
                    "confidence_adjustment": conf_delta,
                    "new_confidence": new_confidence,
                    "stage_verdict": verdict_stage
                }
                trust_updates.append(update_record)
                updated_any = True

                print(f"[TRUST UPDATE] {symbol} ({stage}): Precio=${current_price:.6f} ({price_change_pct:+.1f}%) -> Confianza: {new_confidence}% [{verdict_stage}]")

                # Notify Telegram if significant change (>10 pts)
                if abs(conf_delta) >= 10:
                    send_telegram(f"⏱️ *Actualización {stage} — {symbol}*\nPrecio: ${current_price:.6f} ({price_change_pct:+.1f}%)\nNueva Confianza: {new_confidence}%\nVeredicto parcial: {verdict_stage}")

                # If t+24h, set final verdict
                if stage == "t+24h":
                    # Fix Ciclo 18.1: priorizar el peor veredicto de toda la historia.
                    # Razón: si t+6h fue FALSO POSITIVO pero t+24h es NEUTRAL,
                    # el veredicto final debe reflejar el peor momento (FALSO POSITIVO).
                    _priority = {"FALSO POSITIVO": 4, "FALLO": 3, "NEUTRAL": 2, "ACIERTO": 1}
                    _all_verdicts = [u.get("stage_verdict", "NEUTRAL") for u in trust_updates] + ["NEUTRAL"]
                    alert["final_verdict"] = max(_all_verdicts, key=lambda v: _priority.get(v, 0))

                # Save individual trust file
                trust_file = os.path.join(ALERTS_DIR, f"trust_{mint}.json")
                with open(trust_file, "w") as f:
                    json.dump(trust_updates, f, indent=2)

                # Fix Ciclo 18.1: solo procesar UN stage por ejecución.
                # Los stages atrasados se procesan en ejecuciones posteriores (cada 20 min).
                break

    if updated_any:
        with open(ALL_ALERTS_FILE, "w") as f:
            json.dump(all_alerts, f, indent=2)
        print("[INFO] _all_alerts.json actualizado con nuevos trust updates.")
    else:
        print("[INFO] Ningún trust update pendiente en este momento.")

if __name__ == "__main__":
    main()