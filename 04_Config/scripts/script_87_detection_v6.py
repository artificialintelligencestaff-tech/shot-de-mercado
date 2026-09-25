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

load_dotenv()

MADEONSOL_API_KEY = os.getenv("MADEONSOL_API_KEY")
PUMPPORTAL_WS = "wss://pumpportal.fun/api/data"
MADEONSOL_KOL_FEED = "https://madeonsol.com/api/v1/kol/feed"
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/tokens/"
DEXSCREENER_BOOSTED = "https://api.dexscreener.com/token-boosts/latest/v1"

OUTPUT_DIR = "02_Analisis/detection_v6"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_kol_feed():
    headers = {"Authorization": f"Bearer {MADEONSOL_API_KEY}"}
    try:
        r = requests.get(MADEONSOL_KOL_FEED, params={"limit": 50, "action": "buy", "min_sol": 0.5}, headers=headers, timeout=15)
        r.raise_for_status()
        return r.json()
    except Exception:
        return None

def fetch_dexscreener_boosted():
    try:
        r = requests.get(DEXSCREENER_BOOSTED, timeout=15)
        r.raise_for_status()
        return r.json()
    except Exception:
        return None

def fetch_dexscreener(mint):
    try:
        r = requests.get(f"{DEXSCREENER_API}{mint}", timeout=15)
        r.raise_for_status()
        data = r.json()
        pairs = data.get("pairs", [])
        if not pairs:
            return {"exists": False, "liquidityUsd": 0, "volume24hUsd": 0, "priceUsd": 0, "boosts": 0}
        best = max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0))
        return {
            "exists": True,
            "priceUsd": float(best.get("priceUsd", 0) or 0),
            "liquidityUsd": float(best.get("liquidity", {}).get("usd", 0) or 0),
            "volume24hUsd": float(best.get("volume", {}).get("h24", 0) or 0),
            "marketCapUsd": float(best.get("marketCap", 0) or 0),
            "boosts": int(best.get("boosts", {}).get("active", 0) or 0)
        }
    except Exception:
        return {"exists": False, "liquidityUsd": 0, "volume24hUsd": 0, "priceUsd": 0, "boosts": 0}

def score_token_v6(token, dex_data, kol_buyers, boosted_mints):
    sol_amount = token.get("solAmount", 0)
    mcap_sol = token.get("marketCapSol", 0)
    mint = token.get("mint", "")
    score = 0
    reasons = []

    if sol_amount >= 85:
        score += 25; reasons.append(f"WHALE: {sol_amount:.0f} SOL")
    elif sol_amount >= 5:
        score += 15; reasons.append(f"Large: {sol_amount:.1f} SOL")
    elif sol_amount >= 0.5:
        score += 5; reasons.append(f"Min: {sol_amount:.2f} SOL")

    if mcap_sol >= 100:
        score += 15; reasons.append(f"MCap high: {mcap_sol:.0f}")
    elif mcap_sol >= 30:
        score += 10; reasons.append(f"MCap good: {mcap_sol:.0f}")
    elif mcap_sol >= 10:
        score += 5; reasons.append(f"MCap min: {mcap_sol:.0f}")

    score += 5; reasons.append("Age: T+0")

    kol_names = []
    if kol_buyers:
        kol_names = [k.get("kol_name", "?") for k in kol_buyers]
        if len(kol_buyers) >= 2:
            score += 45; reasons.append(f"KOL x{len(kol_buyers)}: {', '.join(kol_names)}")
        else:
            score += 30; reasons.append(f"KOL: {kol_names[0]}")

    if dex_data.get("exists"):
        liq = dex_data.get("liquidityUsd", 0)
        if liq >= 20000:
            score += 10; reasons.append(f"Liq alta: ${liq:,.0f}")
        elif liq >= 10000:
            score += 5; reasons.append(f"Liq decente: ${liq:,.0f}")

    in_trending = mint in boosted_mints or dex_data.get("boosts", 0) > 0
    if in_trending:
        score += 20; reasons.append("TRENDING (boosted)")

    total = min(100, score)
    if total >= 70:
        nivel = "ALERTA"
    elif total >= 50:
        nivel = "WATCH"
    else:
        nivel = "DESCARTAR"

    return total, nivel, reasons, kol_names, in_trending

async def pumpportal_worker(duration, buffer_ref):
    print(f"[YIN] PumpPortal WS iniciado ({duration}s)...")
    try:
        async with websockets.connect(PUMPPORTAL_WS) as ws:
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
            start = time.time()
            while time.time() - start < duration:
                try:
                    msg = await asyncio.wait_for(ws.recv(), timeout=5.0)
                    data = json.loads(msg)
                    if data.get("txType") == "create":
                        sol_amt = float(data.get("solAmount", 0) or 0)
                        mcap_sol = float(data.get("marketCapSol", 0) or 0)
                        if sol_amt >= 0.5 and 10 <= mcap_sol <= 5000:
                            token = {
                                "mint": data.get("mint"),
                                "symbol": data.get("symbol", "?"),
                                "name": data.get("name", "?"),
                                "solAmount": sol_amt,
                                "marketCapSol": mcap_sol,
                                "dev": data.get("dev", ""),
                                "timestamp": datetime.utcnow().isoformat() + "Z"
                            }
                            buffer_ref.append(token)
                            print(f"  [PASS] {token['symbol']} | {sol_amt:.2f} SOL | MCap {mcap_sol:.1f} SOL")
                except asyncio.TimeoutError:
                    continue
                except Exception:
                    pass
    except Exception as e:
        print(f"[ERROR] PumpPortal: {e}")

async def kol_worker(duration, interval, kol_data_ref):
    print(f"[YIN] KOL Polling iniciado ({interval}s)...")
    start = time.time()
    while time.time() - start < duration:
        data = fetch_kol_feed()
        if data:
            trades = data.get("trades", data.get("data", data if isinstance(data, list) else []))
            if isinstance(trades, list):
                for t in trades:
                    mint = t.get("token_mint") or t.get("mint")
                    if mint and (t.get("action") == "buy" or t.get("side") == "buy"):
                        kol_data_ref[mint].append({
                            "kol_name": t.get("kol_name", t.get("trader", "?")),
                            "solAmount": float(t.get("solAmount", t.get("amount_sol", 0)) or 0),
                            "timestamp": t.get("traded_at", datetime.utcnow().isoformat() + "Z")
                        })
        await asyncio.sleep(interval)

async def cross_check_worker(duration, pp_buffer, kol_data, boosted_mints, start_ts):
    print("[YIN] Cross-check worker iniciado...")
    start = time.time()
    check_num = 0
    while time.time() - start < duration:
        await asyncio.sleep(60)
        check_num += 1
        now_str = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
        print(f"\n[YIN] Cross-check #{check_num} - {now_str} (PP: {len(pp_buffer)}, KOL mints: {len(kol_data)})")

        deployer_counts = defaultdict(list)
        for token in pp_buffer:
            dev = token.get("dev", "")
            if dev:
                deployer_counts[dev].append(token)
        
        deduped = []
        for dev, tokens in deployer_counts.items():
            if len(tokens) > 5:
                tokens.sort(key=lambda t: t.get("solAmount", 0), reverse=True)
                deduped.append(tokens[0])
            else:
                deduped.extend(tokens)
        
        tokens_no_dev = [t for t in pp_buffer if not t.get("dev")]
        deduped.extend(tokens_no_dev)

        results = []
        for token in deduped:
            mint = token.get("mint")
            kol_buyers = kol_data.get(mint, [])
            dex_data = fetch_dexscreener(mint)
            score, nivel, reasons, kol_names, in_trending = score_token_v6(
                token, dex_data, kol_buyers, boosted_mints
            )
            item = {
                "symbol": token.get("symbol"),
                "mint": mint,
                "solAmount": token.get("solAmount"),
                "marketCapSol": token.get("marketCapSol"),
                "score": score,
                "nivel": nivel,
                "reasons": reasons,
                "kol_buyers": kol_names,
                "in_trending": in_trending
            }
            results.append(item)
            if nivel == "ALERTA":
                print(f"  🚨 ALERTA DETECTADA: {token['symbol']} (Score: {score})")

        partial_out = {
            "timestamp": now_str,
            "check": check_num,
            "total_tokens": len(results),
            "kol_matches": len([r for r in results if r["kol_buyers"]]),
            "alertas": len([r for r in results if r["nivel"] == "ALERTA"]),
            "watch": len([r for r in results if r["nivel"] == "WATCH"]),
            "resultados": results
        }
        with open(f"{OUTPUT_DIR}/partial_{now_str}.json", "w") as f:
            json.dump(partial_out, f, indent=2)
        print(f"  [SAVED] partial_{now_str}.json | Alertas: {partial_out['alertas']} | Watch: {partial_out['watch']}")

async def main():
    start_ts = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Detection V6 Iniciado - {start_ts}")

    boosted_mints = set()
    boosted = fetch_dexscreener_boosted()
    if boosted and isinstance(boosted, list):
        for b in boosted:
            addr = b.get("tokenAddress", "")
            if addr:
                boosted_mints.add(addr)
    print(f"[YIN] Dexscreener Boosted cargados: {len(boosted_mints)}")

    pp_buffer = []
    kol_data = defaultdict(list)
    DURATION = 900 # 15 min

    await asyncio.gather(
        pumpportal_worker(DURATION, pp_buffer),
        kol_worker(DURATION, 20, kol_data),
        cross_check_worker(DURATION, pp_buffer, kol_data, boosted_mints, start_ts)
    )

    end_ts = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    print(f"\n[YIN] Ciclo V6 Finalizado - {end_ts}")

if __name__ == "__main__":
    asyncio.run(main())
