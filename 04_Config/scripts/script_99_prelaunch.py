#!/usr/bin/env python3
# DEPRECADO (D-079, 2026-10-03): reemplazado por bot_prelaunch_calendar.py (sources_prelaunch.yml). prelaunch.yml quedó
# sin cron y con el job desactivado. Se conserva como histórico; no lo corre ningún workflow.
import json
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

from pathlib import Path as _Path
PROJECT_ROOT = _Path(os.getenv("SHOT_ROOT", str(_Path(__file__).resolve().parents[2])))
load_dotenv(PROJECT_ROOT / "04_Config" / ".env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# Alertas pre-launch = mensajes de mercado: van SOLO al grupo (TELEGRAM_PUBLIC_CHAT_ID). El chat personal
# (TELEGRAM_CHAT_ID) está deprecado y no se lee. El bot es solo emisor: no lee updates ni comandos.
TELEGRAM_PUBLIC_CHAT_ID = os.getenv("TELEGRAM_PUBLIC_CHAT_ID")
PRELAUNCH_DIR = str(PROJECT_ROOT / "01_Datos_Crudos" / "pre_launch")
ANALYSIS_PRELAUNCH = str(PROJECT_ROOT / "02_Analisis" / "pre_launch")
os.makedirs(PRELAUNCH_DIR, exist_ok=True)
os.makedirs(ANALYSIS_PRELAUNCH, exist_ok=True)

def send_telegram(text):
    chat_id = (TELEGRAM_PUBLIC_CHAT_ID or "").strip()
    if not TELEGRAM_BOT_TOKEN or not chat_id: return False
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown", "disable_web_page_preview": True}
    try:
        r = requests.post(url, json=payload, timeout=15)
        return r.status_code == 200
    except: return False

def fetch_metaplex_upcoming():
    try:
        r = requests.get("https://api.metaplex.com/launches?status=upcoming", timeout=15)
        if r.status_code == 200:
            return r.json()
    except: pass
    return []

def fetch_clawnch_base():
    try:
        r = requests.get("https://clawnch.xyz/api/launches?limit=50", timeout=15)
        if r.status_code == 200:
            data = r.json()
            launches = data.get("launches", data if isinstance(data, list) else [])
            return [l for l in launches if str(l.get("chainId")) == "8453" or l.get("chain") == "base"]
    except: pass
    return []

def fetch_threews_airdrops():
    try:
        r = requests.get("https://three.ws/api/crypto/airdrops", timeout=15)
        if r.status_code == 200:
            return r.json().get("airdrops", [])
    except: pass
    return []

def main():
    print("[YIN] Ejecutando Pipeline Pre-Launch (Script 99)...")
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")

    # Fetch sources
    metaplex = fetch_metaplex_upcoming()
    clawnch = fetch_clawnch_base()
    airdrops = fetch_threews_airdrops()

    # Save raw data
    with open(os.path.join(PRELAUNCH_DIR, f"metaplex_{timestamp}.json"), "w") as f:
        json.dump(metaplex, f, indent=2)
    with open(os.path.join(PRELAUNCH_DIR, f"clawnch_{timestamp}.json"), "w") as f:
        json.dump(clawnch, f, indent=2)
    with open(os.path.join(PRELAUNCH_DIR, f"airdrops_{timestamp}.json"), "w") as f:
        json.dump(airdrops, f, indent=2)

    consolidated = {
        "timestamp": timestamp,
        "tge_upcoming": metaplex,
        "base_launches": clawnch,
        "airdrops": airdrops
    }

    # Save accumulated
    accum_file = os.path.join(ANALYSIS_PRELAUNCH, "_prelaunch_accumulated.json")
    with open(accum_file, "w") as f:
        json.dump(consolidated, f, indent=2)

    print(f"[INFO] Pre-launch data guardada. Metaplex: {len(metaplex)}, Clawnch Base: {len(clawnch)}, Airdrops: {len(airdrops)}")

    # Check for TGE < 7 days (or notify high priority)
    # If metaplex returns items, check dates
    notified = 0
    for tge in metaplex:
        # Expecting launchDate or similar
        launch_date_str = tge.get("launchDate") or tge.get("date")
        if launch_date_str:
            try:
                launch_dt = datetime.fromisoformat(launch_date_str.replace("Z", "+00:00").replace("+00:00", ""))
                days_left = (launch_dt - datetime.utcnow()).days
                if 0 <= days_left <= 7:
                    name = tge.get("name", "Unknown")
                    symbol = tge.get("symbol", "?")
                    msg = f"🚀 *PRE-LAUNCH ALERTA — TGE en {days_left} días*\nProyecto: {name} ({symbol})\nFecha: {launch_date_str}\nPrioridad: ALTA"
                    send_telegram(msg)
                    notified += 1
            except:
                pass

    print(f"[INFO] Alertas pre-launch enviadas a Telegram: {notified}")

if __name__ == "__main__":
    main()
