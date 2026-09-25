#!/usr/bin/env python3
import asyncio
import json
import time
import requests
import websockets
from datetime import datetime
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv(r"D:\Proyecto Shot de mercado\04_Config\.env")

MADEONSOL_API_KEY = os.getenv("MADEONSOL_API_KEY")
PUMPPORTAL_WS = "wss://pumpportal.fun/api/data"
MADEONSOL_TOKEN_URL = "https://madeonsol.com/api/v1/token/"
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/tokens/"

OUTPUT_DIR = r"D:\Proyecto Shot de mercado\02_Analisis\shadow_mode"
os.makedirs(OUTPUT_DIR, exist_ok=True)
ACCUMULATED_FILE = os.path.join(OUTPUT_DIR, "_accumulated.json")

def fetch_token_data(mint):
    headers = {"Authorization": f"Bearer {MADEONSOL_API_KEY}"}
    try:
        r = requests.get(f"{MADEONSOL_TOKEN_URL}{mint}", headers=headers, timeout=10)
        if r.status_code == 200:
            return r.json().get("token", {})
    except:
        pass
    return {}

def score_token_v7(token, ms_data, dx_data):
    # Simplified scoring for shadow mode validation
    score = 0
    sol_amount = token.get("solAmount", 0)
    mcap_sol = token.get("marketCapSol", 0)
    
    # Bonificaciones
    if sol_amount >= 50: score += 20
    elif sol_amount >= 5: score += 10
    if mcap_sol >= 100: score += 15
    elif mcap_sol >= 30: score += 10
    
    # Penalizaciones (pre-filtro ya hizo parte)
    liq_usd = ms_data.get("liquidity_usd", 0) or dx_data.get("liquidityUsd", 0)
    if liq_usd < 10000: score -= 20
    
    return max(0, score)

async def shadow_mode():
    start_ts = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    candidates = []
    
    print(f"[YIN] Shadow Mode Iniciado - {start_ts}")
    
    try:
        async with websockets.connect(PUMPPORTAL_WS) as ws:
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
            print("[YIN] PumpPortal WS suscrito")
            
            end_time = time.time() + 1200 # 20 min
            while time.time() < end_time:
                msg = await asyncio.wait_for(ws.recv(), timeout=5.0)
                data = json.loads(msg)
                if data.get("txType") == "create":
                    # Pre-filtros strictos
                    sol_amt = float(data.get("solAmount", 0) or 0)
                    mcap_sol = float(data.get("marketCapSol", 0) or 0)
                    
                    if sol_amt >= 1.0 and 20 <= mcap_sol <= 5000:
                        mint = data.get("mint")
                        token_meta = {"mint": mint, "symbol": data.get("symbol"), "solAmount": sol_amt, "marketCapSol": mcap_sol}
                        
                        ms_data = fetch_token_data(mint)
                        
                        # Pre-filtro MadeOnSol
                        early_exit = ms_data.get("early_buyer_exit", {}).get("still_holding_pct", 0)
                        deployer = ms_data.get("deployer", {})
                        if early_exit > 70 or deployer.get("total_deployed", 0) > 100 or ms_data.get("kol_activity", {}).get("signal") == "distributing":
                            continue
                            
                        # Validar Score
                        score = score_token_v7(token_meta, ms_data, {})
                        if score >= 50:
                            entry = {**token_meta, "score": score, "timestamp": datetime.utcnow().isoformat()}
                            candidates.append(entry)
                            print(f"[CANDIDATO] {entry['symbol']} | Score: {score}")
                            
    except Exception as e:
        print(f"[ERROR] {e}")
        
    # Guardar
    with open(f"{OUTPUT_DIR}/candidates_{start_ts}.json", "w") as f:
        json.dump(candidates, f, indent=2)
        
    print(f"\n[YIN] Ciclo shadow finalizado. Total: {len(candidates)}")

if __name__ == "__main__":
    asyncio.run(shadow_mode())
