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

MADEONSOL_API_KEY = os.getenv("MADEONSOL_API_KEY", "")
PUMPPORTAL_WS = "wss://pumpportal.fun/api/data"
MADEONSOL_TOKEN_URL = "https://madeonsol.com/api/v1/token/"

OUTPUT_DIR = r"D:\Proyecto Shot de mercado\02_Analisis\shadow_v3"
os.makedirs(OUTPUT_DIR, exist_ok=True)
ACCUMULATED_FILE = os.path.join(OUTPUT_DIR, "_accumulated.json")

def safe_get(url, headers=None, params=None, retries=2, timeout=10):
    for attempt in range(retries + 1):
        try:
            r = requests.get(url, headers=headers, params=params, timeout=timeout)
            if r.status_code == 200:
                try:
                    data = r.json()
                    if isinstance(data, dict):
                        return data
                    return {}
                except Exception:
                    return {}
            elif r.status_code == 429:
                time.sleep(2)
            else:
                if attempt < retries:
                    time.sleep(2)
        except Exception:
            if attempt < retries:
                time.sleep(2)
    return {}

def fetch_madeonsol_token(mint):
    headers = {"Authorization": f"Bearer {MADEONSOL_API_KEY}"} if MADEONSOL_API_KEY else {}
    data = safe_get(f"{MADEONSOL_TOKEN_URL}{mint}", headers=headers, retries=2, timeout=10)
    if not data or not isinstance(data, dict):
        return {}
    token = data.get("token")
    if isinstance(token, dict):
        return token
    return {}

def score_preliminary(token):
    sol_amount = float(token.get("solAmount", 0) or 0)
    mcap_sol = float(token.get("marketCapSol", 0) or 0)
    score = 0
    if sol_amount >= 50:
        score += 20
    elif sol_amount >= 5:
        score += 10
    if mcap_sol >= 100:
        score += 15
    elif mcap_sol >= 30:
        score += 10
    score += 10  # Age 5-60 min
    return max(0, score)

def score_v7(token, ms_data):
    score = 0
    reasons = []
    penalties = []

    sol_amount = float(token.get("solAmount", 0) or 0)
    mcap_sol = float(token.get("marketCapSol", 0) or 0)

    if sol_amount >= 50:
        score += 20; reasons.append(f"Whale entry ({sol_amount:.1f} SOL) [+20]")
    elif sol_amount >= 5:
        score += 10; reasons.append(f"Large entry ({sol_amount:.1f} SOL) [+10]")

    if mcap_sol >= 100:
        score += 15; reasons.append(f"MCap SOL high ({mcap_sol:.0f}) [+15]")
    elif mcap_sol >= 30:
        score += 10; reasons.append(f"MCap SOL good ({mcap_sol:.0f}) [+10]")

    score += 10; reasons.append("Age 5-60m [+10]")

    kol_signal = ms_data.get("kol_activity", {}).get("signal") if isinstance(ms_data.get("kol_activity"), dict) else "neutral"
    if kol_signal == "accumulating":
        score += 30; reasons.append("KOL signal: ACCUMULATING [+30]")

    liq_usd = float(ms_data.get("liquidity_usd", 0) or 0)
    if liq_usd >= 20000:
        score += 10; reasons.append(f"Liquidity > $20K (${liq_usd:,.0f}) [+10]")

    if kol_signal == "distributing":
        score -= 40; penalties.append("KOL signal: DISTRIBUTING [-40]")

    early_exit_pct = ms_data.get("early_buyer_exit", {}).get("still_holding_pct", 100) if isinstance(ms_data.get("early_buyer_exit"), dict) else 100
    exit_pct = 100 - (early_exit_pct if early_exit_pct is not None else 100)
    if exit_pct > 50:
        score -= 30; penalties.append(f"Early exit {exit_pct:.0f}% > 50% [-30]")

    deployer = ms_data.get("deployer", {}) if isinstance(ms_data.get("deployer"), dict) else {}
    total_deployed = deployer.get("total_deployed", 0) or 0
    total_bonded = deployer.get("total_bonded", 0) or 0
    success_rate = (total_bonded / total_deployed * 100) if total_deployed > 0 else 0
    if total_deployed > 10 and success_rate < 5:
        score -= 30; penalties.append(f"Deployer success {success_rate:.1f}% < 5% [-30]")

    if total_deployed > 100:
        score -= 20; penalties.append(f"Deployer total {total_deployed} > 100 [-20]")

    tw_reuse = ms_data.get("twitter_reuse")
    if isinstance(tw_reuse, dict) and (tw_reuse.get("mints_same_handle", 0) or 0) > 1:
        score -= 25; penalties.append(f"Twitter reuse ({tw_reuse.get('handle')}: {tw_reuse.get('mints_same_handle')} mints) [-25]")

    price_change = ms_data.get("mc_change_pct", {}).get("h24", 0) if isinstance(ms_data.get("mc_change_pct"), dict) else 0
    if price_change < -20:
        score -= 20; penalties.append(f"Price 24h {price_change:.1f}% < -20% [-20]")

    if liq_usd < 1000:
        score -= 25; penalties.append(f"Liquidity ${liq_usd:,.0f} < $1K [-25]")
    elif liq_usd < 10000:
        score -= 15; penalties.append(f"Liquidity ${liq_usd:,.0f} < $10K [-15]")

    price_age = ms_data.get("price_age_seconds", 0) or 0
    if price_age > 600:
        score -= 20; penalties.append(f"Price stale ({price_age}s > 600s) [-20]")

    mint_revoked = ms_data.get("mint_authority_revoked")
    if mint_revoked is False:
        score -= 50; penalties.append("Mint authority NOT revoked [-50]")

    freeze_revoked = ms_data.get("freeze_authority_revoked")
    if freeze_revoked is False:
        score -= 50; penalties.append("Freeze authority NOT revoked [-50]")

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
    start_time = time.time()
    duration = 1200 # 20 min
    start_ts = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Shadow Mode v3 Iniciado - {start_ts}")

    stats = {
        "raw_captured": 0,
        "stage1_passed": 0,
        "stage2_passed": 0,
        "madeonsol_ok": 0,
        "stage3_passed": 0,
        "alertas_70": 0,
        "watch_50": 0
    }
    deployer_counts = defaultdict(int)
    stage1_buffer = []
    evaluated_mints = {}
    last_checkpoint = time.time()

    try:
        async with websockets.connect(PUMPPORTAL_WS) as ws:
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
            print("[YIN] PumpPortal WS conectado exitosamente")

            while time.time() - start_time < duration:
                try:
                    msg = await asyncio.wait_for(ws.recv(), timeout=2.0)
                    data = json.loads(msg)
                    if data.get("txType") == "create":
                        stats["raw_captured"] += 1
                        sol_amt = float(data.get("solAmount", 0) or 0)
                        mcap_sol = float(data.get("marketCapSol", 0) or 0)
                        dev = data.get("dev", "") or "unknown"
                        mint = data.get("mint", "")
                        symbol = data.get("symbol", "?")
                        uri = data.get("uri", "")

                        # Stage 1: trivial pre-filter
                        if sol_amt < 0.1:
                            continue
                        if not uri or not dev:
                            continue
                        deployer_counts[dev] += 1
                        if deployer_counts[dev] > 5:
                            continue
                        stage1_buffer.append({
                            "mint": mint,
                            "symbol": symbol,
                            "name": data.get("name", "?"),
                            "solAmount": sol_amt,
                            "marketCapSol": mcap_sol,
                            "dev": dev,
                            "uri": uri,
                            "timestamp": datetime.utcnow().isoformat()
                        })
                        stats["stage1_passed"] += 1

                        # Periodic processing every 30 seconds to avoid overload
                        if time.time() - last_checkpoint >= 30:
                            # Stage 2: preliminary scoring
                            stage2_candidates = []
                            for item in stage1_buffer:
                                pre_score = score_preliminary(item)
                                if pre_score >= 20:
                                    stage2_candidates.append(item)
                            stats["stage2_passed"] = len(stage2_candidates)
                            print(f"  [CHECKPOINT] Stage1: {stats['stage1_passed']} -> Stage2: {stats['stage2_passed']}")

                            # Stage 3: MadeOnSol for stage2 candidates
                            stage3_candidates = []
                            for item in stage2_candidates:
                                mint = item["mint"]
                                ms_token = fetch_madeonsol_token(mint)
                                if ms_token:
                                    stats["madeonsol_ok"] += 1
                                    item["ms_data"] = ms_token
                                    stage3_candidates.append(item)
                                else:
                                    # If MadeOnSol fails, we still keep but with empty ms_data; scoring will handle
                                    item["ms_data"] = {}
                                    stage3_candidates.append(item)
                            stats["stage3_passed"] = len(stage3_candidates)
                            print(f"  [CHECKPOINT] MadeOnSol OK: {stats['madeonsol_ok']} -> Stage3: {stats['stage3_passed']}")

                            # Stage 4 & 5: final scoring and post-filter
                            final_candidates = []
                            for item in stage3_candidates:
                                ms_data = item.get("ms_data", {})
                                score, verdict, is_alert, reasons, penalties = score_v7(item, ms_data)
                                item.update({
                                    "score": score,
                                    "verdict": verdict,
                                    "is_alert": is_alert,
                                    "reasons": reasons,
                                    "penalties": penalties
                                })
                                if score >= 50:
                                    final_candidates.append(item)
                                    if is_alert:
                                        stats["alertas_70"] += 1
                                        print(f"    🚨 ALERTA: {item['symbol']} | Score: {score}")
                                    elif score >= 50:
                                        stats["watch_50"] += 1
                                        print(f"    👀 WATCH: {item['symbol']} | Score: {score}")
                            # Update evaluated_mints for accumulation
                            for item in final_candidates:
                                evaluated_mints[item["mint"]] = item

                            # Checkpoint save
                            chk_ts = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
                            chk_file = os.path.join(OUTPUT_DIR, f"partial_{chk_ts}.json")
                            with open(chk_file, "w") as f:
                                json.dump({
                                    "timestamp": chk_ts,
                                    "stats": stats,
                                    "candidates": list(evaluated_mints.values())
                                }, f, indent=2)

                            # Accumulated file
                            accumulated = {}
                            if os.path.exists(ACCUMULATED_FILE):
                                try:
                                    with open(ACCUMULATED_FILE, "r") as f:
                                        accumulated = json.load(f)
                                except Exception:
                                    accumulated = {}
                            for m, item in evaluated_mints.items():
                                accumulated[m] = item
                            with open(ACCUMULATED_FILE, "w") as f:
                                json.dump(accumulated, f, indent=2)

                            last_checkpoint = time.time()
                            stage1_buffer = []  # reset buffer after processing

                except asyncio.TimeoutError:
                    pass
                except Exception as e:
                    pass

                time.sleep(0.1)  # avoid tight loop

    except Exception as e:
        print(f"[FATAL WS ERROR] {e}")

    # Final save
    end_ts = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    final_file = os.path.join(OUTPUT_DIR, f"final_{end_ts}.json")
    with open(final_file, "w") as f:
        json.dump({
            "timestamp": end_ts,
            "stats": stats,
            "candidates": list(evaluated_mints.values())
        }, f, indent=2)

    print(f"\n[YIN] Shadow Mode v3 FINALIZADO - {end_ts}")
    print(f"Reporte final guardado en: {final_file}")

if __name__ == "__main__":
    asyncio.run(main())