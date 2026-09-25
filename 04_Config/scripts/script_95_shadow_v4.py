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

OUTPUT_DIR = r"D:\Proyecto Shot de mercado\02_Analisis\shadow_v4"
os.makedirs(OUTPUT_DIR, exist_ok=True)
ACCUMULATED_FILE = os.path.join(OUTPUT_DIR, "_accumulated.json")
PENDING_QUEUE_FILE = os.path.join(OUTPUT_DIR, "_pending_queue.json")
CACHE_DB = os.path.join(OUTPUT_DIR, "_cache.db")
API_LOG = os.path.join(OUTPUT_DIR, "_api_log.json")

http_error_counts = defaultdict(int)

def init_db():
    conn = sqlite3.connect(CACHE_DB)
    conn.execute("CREATE TABLE IF NOT EXISTS madeonsol_data (mint TEXT PRIMARY KEY, data TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()

def log_api(source, code):
    http_error_counts[str(code)] += 1
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
                time.sleep(2)
        except:
            log_api(url.split('/')[2], "timeout")
    return {}

def fetch_dexscreener(mint):
    data = safe_get(f"{DEXSCREENER_API}{mint}", retries=1, timeout=5)
    pairs = data.get("pairs", []) if isinstance(data, dict) else []
    if isinstance(pairs, list) and len(pairs) > 0:
        best = max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0) if isinstance(p, dict) else 0)
        return {
            "exists": True,
            "liquidityUsd": float(best.get("liquidity", {}).get("usd", 0) or 0) if isinstance(best.get("liquidity"), dict) else 0.0,
            "volume24hUsd": float(best.get("volume", {}).get("h24", 0) or 0) if isinstance(best.get("volume"), dict) else 0.0,
            "priceChange_h24": float(best.get("priceChange", {}).get("h24", 0) or 0) if isinstance(best.get("priceChange"), dict) else 0.0
        }
    return {"exists": False, "liquidityUsd": 0.0, "volume24hUsd": 0.0, "priceChange_h24": 0.0}

def fetch_madeonsol_token(mint):
    conn = sqlite3.connect(CACHE_DB)
    row = conn.execute("SELECT data FROM madeonsol_data WHERE mint=?", (mint,)).fetchone()
    conn.close()
    if row:
        return json.loads(row[0])

    headers = {"Authorization": f"Bearer {MADEONSOL_API_KEY}"} if MADEONSOL_API_KEY else {}
    data = safe_get(f"{MADEONSOL_TOKEN_URL}{mint}", headers=headers)
    token = data.get("token", {}) if isinstance(data, dict) else {}
    if token:
        conn = sqlite3.connect(CACHE_DB)
        conn.execute("REPLACE INTO madeonsol_data VALUES (?, ?, ?)", (mint, json.dumps(token), datetime.utcnow().isoformat()))
        conn.commit()
        conn.close()
    return token

def calculate_pre_score(token, dx):
    score = 0
    sol = float(token.get("solAmount", 0) or 0)
    mcap = float(token.get("marketCapSol", 0) or 0)
    liq = float(dx.get("liquidityUsd", 0) or 0)
    chg = float(dx.get("priceChange_h24", 0) or 0)

    if sol >= 50: score += 25
    elif sol >= 10: score += 15
    elif sol >= 5: score += 10

    if mcap >= 100: score += 15
    elif mcap >= 50: score += 10

    if liq >= 20000: score += 10
    if chg > 0: score += 5
    return score

def score_v7(token, ms_data, dx_data):
    score = 0
    reasons = []
    penalties = []

    sol_amount = float(token.get("solAmount", 0) or 0)
    mcap_sol = float(token.get("marketCapSol", 0) or 0)
    liq_usd = float(dx_data.get("liquidityUsd", 0) or ms_data.get("liquidity_usd", 0) or 0)

    if sol_amount >= 50: score += 20; reasons.append(f"Whale ({sol_amount:.1f} SOL)")
    elif sol_amount >= 5: score += 10; reasons.append(f"Large ({sol_amount:.1f} SOL)")

    if mcap_sol >= 100: score += 15; reasons.append(f"MCap high ({mcap_sol:.0f})")
    elif mcap_sol >= 30: score += 10; reasons.append(f"MCap good ({mcap_sol:.0f})")

    score += 10; reasons.append("Age T+0")

    kol_signal = ms_data.get("kol_activity", {}).get("signal") if isinstance(ms_data.get("kol_activity"), dict) else "neutral"
    if kol_signal == "accumulating": score += 30; reasons.append("KOL Accumulating")

    if liq_usd >= 20000: score += 10; reasons.append(f"Liq > $20K (${liq_usd:,.0f})")

    if kol_signal == "distributing": score -= 40; penalties.append("KOL Distributing")

    early_exit_pct = ms_data.get("early_buyer_exit", {}).get("still_holding_pct", 100) if isinstance(ms_data.get("early_buyer_exit"), dict) else 100
    exit_pct = 100 - (early_exit_pct if early_exit_pct is not None else 100)
    if exit_pct > 50: score -= 30; penalties.append(f"Early exit {exit_pct:.0f}% > 50%")

    deployer = ms_data.get("deployer", {}) if isinstance(ms_data.get("deployer"), dict) else {}
    total_deployed = deployer.get("total_deployed", 0) or 0
    total_bonded = deployer.get("total_bonded", 0) or 0
    success_rate = (total_bonded / total_deployed * 100) if total_deployed > 0 else 0
    if total_deployed > 10 and success_rate < 5: score -= 30; penalties.append(f"Deployer success < 5%")

    if total_deployed > 100: score -= 20; penalties.append(f"Deployer total > 100")

    mint_revoked = ms_data.get("mint_authority_revoked")
    freeze_revoked = ms_data.get("freeze_authority_revoked")
    if mint_revoked is False: score -= 50; penalties.append("Mint authority not revoked")
    if freeze_revoked is False: score -= 50; penalties.append("Freeze authority not revoked")

    final_score = max(0, score)
    is_alert = (
        final_score >= 70 and
        kol_signal != "distributing" and
        exit_pct < 50 and
        (total_deployed <= 10 or success_rate >= 5) and
        liq_usd >= 10000 and
        mint_revoked is True and
        freeze_revoked is True
    )
    verdict = "ALERTA REAL" if is_alert else ("WATCH REAL" if final_score >= 50 else "DESCARTAR")
    return final_score, verdict, is_alert, reasons, penalties

async def main():
    init_db()
    start_time = time.time()
    DURATION = 1200 # 20 min
    MADEONSOL_LIMIT = 25
    madeonsol_count = 0
    
    candidates_buffer = []
    evaluated_mints = {}
    last_call_time = 0
    call_interval = 45 # 1 call every 45s

    print(f"[YIN] Shadow v4 (Quality Gate + Priority Queue) Iniciado - {datetime.utcnow()}")

    async with websockets.connect(PUMPPORTAL_WS) as ws:
        await ws.send(json.dumps({"method": "subscribeNewToken"}))
        
        while time.time() - start_time < DURATION:
            try:
                msg = await asyncio.wait_for(ws.recv(), timeout=1.0)
                data = json.loads(msg)
                if data.get("txType") == "create":
                    sol_amt = float(data.get("solAmount", 0) or 0)
                    mcap_sol = float(data.get("marketCapSol", 0) or 0)
                    
                    # Etapa 1 & 2: Quality Gate fuerte (solAmount >= 5.0 OR marketCapSol >= 50)
                    if sol_amt >= 5.0 or mcap_sol >= 50.0:
                        mint = data.get("mint")
                        symbol = data.get("symbol", "?")
                        
                        # Etapa 3: Dexscreener enrichment
                        dx = fetch_dexscreener(mint)
                        
                        # Etapa 4: Cola de prioridad (pre-score)
                        pre_score = calculate_pre_score(data, dx)
                        
                        item = {
                            "mint": mint, "symbol": symbol, "solAmount": sol_amt,
                            "marketCapSol": mcap_sol, "dx": dx, "pre_score": pre_score,
                            "timestamp": datetime.utcnow().isoformat()
                        }
                        candidates_buffer.append(item)
            except asyncio.TimeoutError:
                pass
            except Exception:
                pass

            # Etapa 5: MadeOnSol selectivo (top priority, 1 every 45s, limit 25)
            if candidates_buffer and madeonsol_count < MADEONSOL_LIMIT:
                if time.time() - last_call_time >= call_interval:
                    # Sort buffer by pre_score descending
                    candidates_buffer.sort(key=lambda x: x["pre_score"], reverse=True)
                    top_item = candidates_buffer.pop(0)
                    
                    madeonsol_count += 1
                    last_call_time = time.time()
                    
                    ms = fetch_madeonsol_token(top_item["mint"])
                    score, verdict, is_alert, reasons, penalties = score_v7(top_item, ms, top_item["dx"])
                    
                    top_item.update({
                        "score": score, "verdict": verdict, "is_alert": is_alert,
                        "reasons": reasons, "penalties": penalties, "ms_data": ms
                    })
                    evaluated_mints[top_item["mint"]] = top_item
                    print(f"  [{verdict}] {top_item['symbol']} | Pre-Score: {top_item['pre_score']} | Final Score: {score} (MOS calls: {madeonsol_count}/{MADEONSOL_LIMIT})")

    # Save Pending Queue
    with open(PENDING_QUEUE_FILE, "w") as f:
        json.dump(candidates_buffer, f, indent=2)

    # Save Accumulated
    accumulated = {}
    if os.path.exists(ACCUMULATED_FILE):
        try:
            with open(ACCUMULATED_FILE, "r") as f: accumulated = json.load(f)
        except: pass
    for m, item in evaluated_mints.items(): accumulated[m] = item
    with open(ACCUMULATED_FILE, "w") as f: json.dump(accumulated, f, indent=2)

    # Save Final Report
    end_ts = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    final_file = os.path.join(OUTPUT_DIR, f"final_{end_ts}.json")
    with open(final_file, "w") as f:
        json.dump({
            "timestamp": end_ts,
            "madeonsol_calls": madeonsol_count,
            "http_errors": dict(http_error_counts),
            "candidates": list(evaluated_mints.values())
        }, f, indent=2)

    print(f"\n[YIN] Shadow v4 Finalizado. MadeOnSol calls: {madeonsol_count}/25")
    print(f"Reporte: {final_file}")

if __name__ == "__main__":
    asyncio.run(main())
