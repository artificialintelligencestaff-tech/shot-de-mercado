#!/usr/bin/env python3
import asyncio
import json
import time
import requests
import websockets
import sqlite3
from datetime import datetime
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv(r"D:\Proyecto Shot de mercado\04_Config\.env")

MADEONSOL_API_KEY = os.getenv("MADEONSOL_API_KEY", "")
PUMPPORTAL_WS = "wss://pumpportal.fun/api/data"
MADEONSOL_TOKEN_URL = "https://madeonsol.com/api/v1/token/"
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/tokens/"

OUTPUT_DIR = r"D:\Proyecto Shot de mercado\02_Analisis\shadow_v3"
os.makedirs(OUTPUT_DIR, exist_ok=True)
ACCUMULATED_FILE = os.path.join(OUTPUT_DIR, "_accumulated.json")
CACHE_DB = os.path.join(OUTPUT_DIR, "_cache.db")
API_LOG = os.path.join(OUTPUT_DIR, "_api_log.json")

def init_db():
    conn = sqlite3.connect(CACHE_DB)
    conn.execute("CREATE TABLE IF NOT EXISTS madeonsol_data (mint TEXT PRIMARY KEY, data TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()

def log_api(source, code):
    log = []
    if os.path.exists(API_LOG):
        try:
            with open(API_LOG, "r") as f: log = json.load(f)
        except: pass
    log.append({"ts": datetime.utcnow().isoformat(), "source": source, "code": code})
    with open(API_LOG, "w") as f: json.dump(log, f)

def safe_get(url, headers=None, params=None, retries=1, timeout=5):
    for attempt in range(retries + 1):
        try:
            r = requests.get(url, headers=headers, params=params, timeout=timeout)
            log_api(url.split('/')[2], r.status_code)
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 429:
                time.sleep(1)
        except:
            pass
    return {}

def fetch_madeonsol_token(mint):
    headers = {"Authorization": f"Bearer {MADEONSOL_API_KEY}"} if MADEONSOL_API_KEY else {}
    data = safe_get(f"{MADEONSOL_TOKEN_URL}{mint}", headers=headers)
    return data.get("token", {}) if isinstance(data, dict) else {}

def score_v7(token, ms_data):
    score = 0
    sol_amount = float(token.get("solAmount", 0) or 0)
    mcap_sol = float(token.get("marketCapSol", 0) or 0)
    
    if sol_amount >= 50: score += 20
    elif sol_amount >= 5: score += 10
    if mcap_sol >= 100: score += 15
    elif mcap_sol >= 30: score += 10
    score += 10 # Age bonus
    
    kol_signal = ms_data.get("kol_activity", {}).get("signal") if isinstance(ms_data, dict) else "neutral"
    if kol_signal == "accumulating": score += 30
    
    liq = float(ms_data.get("liquidity_usd", 0) or 0)
    if liq >= 20000: score += 10
    
    if kol_signal == "distributing": score -= 40
    
    final_score = max(0, score)
    return final_score, ("ALERTA" if final_score >= 70 else "DESCARTAR")

async def main():
    init_db()
    start_time = time.time()
    DURATION = 1200
    MADEONSOL_LIMIT = 25
    madeonsol_count = 0
    buffer = []
    
    print(f"[YIN] Pipeline v3 Iniciado - {datetime.utcnow()}")
    
    async with websockets.connect(PUMPPORTAL_WS) as ws:
        await ws.send(json.dumps({"method": "subscribeNewToken"}))
        
        while time.time() - start_time < DURATION:
            try:
                msg = await asyncio.wait_for(ws.recv(), timeout=2.0)
                data = json.loads(msg)
                if data.get("txType") == "create":
                    token = {
                        "mint": data.get("mint"), "symbol": data.get("symbol", "?"),
                        "solAmount": data.get("solAmount"), "marketCapSol": data.get("marketCapSol"),
                        "dev": data.get("dev", "unknown")
                    }
                    
                    # Pre-filtros triviales
                    if float(token["solAmount"] or 0) < 0.1 or not data.get("uri"): continue
                    
                    # MadeOnSol
                    if madeonsol_count < MADEONSOL_LIMIT:
                        ms = fetch_madeonsol_token(token["mint"])
                        madeonsol_count += 1
                        
                        score, verdict = score_v7(token, ms)
                        token.update({"score": score, "verdict": verdict})
                        buffer.append(token)
                        print(f"  [{verdict}] {token['symbol']} | Score: {score}")

            except: continue
            
    print(f"[YIN] Ciclo finalizado. Total: {len(buffer)}")

if __name__ == "__main__":
    asyncio.run(main())