#!/usr/bin/env python3
import asyncio
import json
import time
import requests
import websockets
import sqlite3
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv(r"D:\Proyecto Shot de mercado\04_Config\.env")

MADEONSOL_API_KEY = os.getenv("MADEONSOL_API_KEY", "")
PUMPPORTAL_WS = "wss://pumpportal.fun/api/data"
MADEONSOL_TOKEN_URL = "https://madeonsol.com/api/v1/token/"
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/tokens/"

OUTPUT_DIR = r"D:\Proyecto Shot de mercado\02_Analisis\shadow_v5"
os.makedirs(OUTPUT_DIR, exist_ok=True)
ACCUMULATED_FILE = os.path.join(OUTPUT_DIR, "_accumulated.json")
CACHE_DB = os.path.join(OUTPUT_DIR, "_cache.db")

def init_db():
    conn = sqlite3.connect(CACHE_DB)
    conn.execute("CREATE TABLE IF NOT EXISTS madeonsol_data (mint TEXT PRIMARY KEY, data TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()

def safe_get_madeonsol(mint):
    headers = {"Authorization": f"Bearer {MADEONSOL_API_KEY}"} if MADEONSOL_API_KEY else {}
    try:
        r = requests.get(f"{MADEONSOL_TOKEN_URL}{mint}", headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json().get("token", {})
            conn = sqlite3.connect(CACHE_DB)
            conn.execute("REPLACE INTO madeonsol_data VALUES (?, ?, ?)", (mint, json.dumps(data), datetime.utcnow().isoformat()))
            conn.commit()
            conn.close()
            return data
    except: pass
    return {}

def score_v7(token, ms_data):
    score = 0
    sol_amount = float(token.get("solAmount", 0) or 0)
    mcap_sol = float(token.get("marketCapSol", 0) or 0)
    liq = float(ms_data.get("liquidity_usd", 0) or 0)
    
    if sol_amount >= 50: score += 20
    elif sol_amount >= 5: score += 10
    if mcap_sol >= 100: score += 15
    elif mcap_sol >= 30: score += 10
    score += 10 # Age
    
    kol_signal = ms_data.get("kol_activity", {}).get("signal") if isinstance(ms_data.get("kol_activity"), dict) else "neutral"
    if kol_signal == "accumulating": score += 30
    if liq >= 20000: score += 10
    
    if kol_signal == "distributing": score -= 40
    
    early_exit_pct = 100 - (ms_data.get("early_buyer_exit", {}).get("still_holding_pct", 100) or 100)
    if early_exit_pct > 50: score -= 30
    
    return max(0, score), ("ALERTA REAL" if score >= 70 else ("WATCH REAL" if score >= 50 else "DESCARTAR"))

async def main():
    init_db()
    start_time = time.time()
    DURATION = 1200
    MADEONSOL_LIMIT = 25
    madeonsol_count = 0
    buffer = []
    watch_tokens = []
    
    print(f"[YIN] Pipeline Shadow v5 Iniciado - {datetime.utcnow()}")
    
    async with websockets.connect(PUMPPORTAL_WS) as ws:
        await ws.send(json.dumps({"method": "subscribeNewToken"}))
        
        while time.time() - start_time < DURATION:
            try:
                msg = await asyncio.wait_for(ws.recv(), timeout=2.0)
                data = json.loads(msg)
                if data.get("txType") == "create":
                    token = {"mint": data.get("mint"), "symbol": data.get("symbol", "?"), "solAmount": data.get("solAmount"), "marketCapSol": data.get("marketCapSol"), "dev": data.get("dev", "unknown")}
                    if float(token["solAmount"] or 0) < 0.1 or not data.get("uri"): continue
                    
                    if madeonsol_count < MADEONSOL_LIMIT:
                        ms = safe_get_madeonsol(token["mint"])
                        madeonsol_count += 1
                        score, verdict = score_v7(token, ms)
                        token.update({"score": score, "verdict": verdict, "ms_data": ms})
                        buffer.append(token)
                        if score >= 50:
                            watch_tokens.append(token)
                            # Save partial enrichment
                            with open(f"{OUTPUT_DIR}/watch_{token['symbol']}_{datetime.utcnow().strftime('%H%M%S')}.json", "w") as f:
                                json.dump(token, f, indent=2)
                        print(f"  [{verdict}] {token['symbol']} | Score: {score}")
            except: continue
            
    # Final cleanup & stats
    print(f"[YIN] Ciclo finalizado. Total: {len(buffer)}")
    
    # Save _accumulated
    accumulated = {}
    if os.path.exists(ACCUMULATED_FILE):
        with open(ACCUMULATED_FILE, "r") as f: accumulated = json.load(f)
    for t in buffer: accumulated[t["mint"]] = t
    with open(ACCUMULATED_FILE, "w") as f: json.dump(accumulated, f, indent=2)

if __name__ == "__main__":
    asyncio.run(main())
