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
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/tokens/"
DEXSCREENER_BOOSTED = "https://api.dexscreener.com/token-boosts/latest/v1"

OUTPUT_DIR = r"D:\Proyecto Shot de mercado\02_Analisis\shadow_v2"
os.makedirs(OUTPUT_DIR, exist_ok=True)
ACCUMULATED_FILE = os.path.join(OUTPUT_DIR, "_accumulated.json")

# Error counters
error_counts = {
    "pumpportal": 0,
    "madeonsol": 0,
    "dexscreener": 0
}

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
        error_counts["madeonsol"] += 1
        return {}
    token = data.get("token")
    if isinstance(token, dict):
        return token
    error_counts["madeonsol"] += 1
    return {}

def fetch_dexscreener_token(mint):
    data = safe_get(f"{DEXSCREENER_API}{mint}", retries=2, timeout=10)
    if not data or not isinstance(data, dict):
        error_counts["dexscreener"] += 1
        return {}
    pairs = data.get("pairs", [])
    if isinstance(pairs, list) and len(pairs) > 0:
        best = max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0) if isinstance(p, dict) else 0)
        return {
            "exists": True,
            "liquidityUsd": float(best.get("liquidity", {}).get("usd", 0) or 0) if isinstance(best.get("liquidity"), dict) else 0.0,
            "volume24hUsd": float(best.get("volume", {}).get("h24", 0) or 0) if isinstance(best.get("volume"), dict) else 0.0,
            "priceChange_h24": float(best.get("priceChange", {}).get("h24", 0) or 0) if isinstance(best.get("priceChange"), dict) else 0.0,
            "boosts_active": int(best.get("boosts", {}).get("active", 0) or 0) if isinstance(best.get("boosts"), dict) else 0
        }
    return {"exists": False, "liquidityUsd": 0.0, "volume24hUsd": 0.0, "priceChange_h24": 0.0, "boosts_active": 0}

def score_token_v7(token, ms_data, dx_data):
    score = 0
    reasons = []
    penalties = []

    sol_amount = float(token.get("solAmount", 0) or 0)
    mcap_sol = float(token.get("marketCapSol", 0) or 0)

    # Bonificaciones
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

    price_change = dx_data.get("priceChange_h24", 0)
    boosts = dx_data.get("boosts_active", 0)
    if boosts > 0 and price_change > 0:
        score += 15; reasons.append("Boosted + Price Positive [+15]")

    liq_usd = float(ms_data.get("liquidity_usd", 0) or dx_data.get("liquidityUsd", 0) or 0)
    if liq_usd >= 20000:
        score += 10; reasons.append(f"Liquidity > $20K (${liq_usd:,.0f}) [+10]")

    # Penalizaciones
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
    print(f"[YIN] Shadow Mode v2 Iniciado - {start_ts}")

    raw_tokens = []
    stats = {
        "raw_captured": 0,
        "discarded_sol_amount": 0,
        "discarded_mcap": 0,
        "discarded_deployer_spam": 0,
        "discarded_ms_missing": 0,
        "discarded_secondary_filters": 0,
        "ms_ok": 0,
        "validated_v7": 0,
        "alertas_70": 0,
        "watch_50": 0
    }

    deployer_counts = defaultdict(int)
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

                        # Pre-filtro 1: solAmount >= 1.0
                        if sol_amt < 1.0:
                            stats["discarded_sol_amount"] += 1
                            continue

                        # Pre-filtro 2: MCap SOL 20-5000
                        if not (20 <= mcap_sol <= 5000):
                            stats["discarded_mcap"] += 1
                            continue

                        # Pre-filtro 3: Deployer <= 5 en buffer
                        deployer_counts[dev] += 1
                        if deployer_counts[dev] > 5:
                            stats["discarded_deployer_spam"] += 1
                            continue

                        token_meta = {
                            "mint": mint,
                            "symbol": symbol,
                            "name": data.get("name", "?"),
                            "solAmount": sol_amt,
                            "marketCapSol": mcap_sol,
                            "dev": dev,
                            "timestamp": datetime.utcnow().isoformat()
                        }

                        # MadeOnSol fetch (safe)
                        ms_token = fetch_madeonsol_token(mint)
                        if not ms_token:
                            stats["discarded_ms_missing"] += 1
                            continue
                        stats["ms_ok"] += 1

                        # Pre-filtros secundarios
                        early_exit_pct = ms_token.get("early_buyer_exit", {}).get("still_holding_pct", 100) if isinstance(ms_token.get("early_buyer_exit"), dict) else 100
                        exit_pct = 100 - (early_exit_pct if early_exit_pct is not None else 100)
                        deployer_info = ms_token.get("deployer", {}) if isinstance(ms_token.get("deployer"), dict) else {}
                        total_deployed = deployer_info.get("total_deployed", 0) or 0
                        kol_signal = ms_token.get("kol_activity", {}).get("signal") if isinstance(ms_token.get("kol_activity"), dict) else "neutral"
                        mint_rev = ms_token.get("mint_authority_revoked")
                        freeze_rev = ms_token.get("freeze_authority_revoked")

                        if exit_pct > 70 or total_deployed > 100 or kol_signal == "distributing" or mint_rev is not True or freeze_rev is not True:
                            stats["discarded_secondary_filters"] += 1
                            continue

                        # Dexscreener fetch
                        dx_data = fetch_dexscreener_token(mint)

                        # Scoring v7
                        score, verdict, is_alert, reasons, penalties = score_token_v7(token_meta, ms_token, dx_data)
                        stats["validated_v7"] += 1

                        item_result = {
                            **token_meta,
                            "score": score,
                            "verdict": verdict,
                            "is_alert": is_alert,
                            "reasons": reasons,
                            "penalties": penalties,
                            "liquidity_usd": ms_token.get("liquidity_usd", 0) or dx_data.get("liquidityUsd", 0),
                            "kol_signal": kol_signal,
                            "exit_pct": exit_pct,
                            "total_deployed": total_deployed
                        }
                        evaluated_mints[mint] = item_result

                        if score >= 70:
                            stats["alertas_70"] += 1
                            print(f"  🚨 [CANDIDATO ALERTA] {symbol} | Score: {score} | {verdict}")
                        elif score >= 50:
                            stats["watch_50"] += 1
                            print(f"  👀 [WATCH] {symbol} | Score: {score}")

                except asyncio.TimeoutError:
                    pass
                except Exception as e:
                    error_counts["pumpportal"] += 1

                # Checkpoint cada 60s
                if time.time() - last_checkpoint >= 60:
                    last_checkpoint = time.time()
                    chk_ts = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
                    chk_file = os.path.join(OUTPUT_DIR, f"partial_{chk_ts}.json")
                    with open(chk_file, "w") as f:
                        json.dump({
                            "timestamp": chk_ts,
                            "stats": stats,
                            "errors": error_counts,
                            "candidates": list(evaluated_mints.values())
                        }, f, indent=2)

                    # Update _accumulated.json
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
                    print(f"  [CHECKPOINT] {chk_ts} | Raw: {stats['raw_captured']} | Validados v7: {stats['validated_v7']} | Acumulados: {len(accumulated)}")

    except Exception as e:
        error_counts["pumpportal"] += 1
        print(f"[FATAL WS ERROR] {e}")

    # Final Save
    end_ts = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    final_file = os.path.join(OUTPUT_DIR, f"final_{end_ts}.json")
    with open(final_file, "w") as f:
        json.dump({
            "timestamp": end_ts,
            "stats": stats,
            "errors": error_counts,
            "candidates": list(evaluated_mints.values())
        }, f, indent=2)

    print(f"\n[YIN] Shadow Mode v2 FINALIZADO - {end_ts}")
    print(f"Reporte final guardado en: {final_file}")

if __name__ == "__main__":
    asyncio.run(main())
