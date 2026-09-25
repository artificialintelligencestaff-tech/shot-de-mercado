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
MADEONSOL_DEPLOYER = "https://madeonsol.com/api/v1/deployer-hunter/alerts"
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/tokens/"
DEXSCREENER_BOOSTED = "https://api.dexscreener.com/token-boosts/latest/v1"

OUTPUT_DIR = "02_Analisis/detection_v5"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_kol_feed():
    """MadeOnSol KOL feed REST (polling)"""
    headers = {"Authorization": f"Bearer {MADEONSOL_API_KEY}"}
    try:
        r = requests.get(MADEONSOL_KOL_FEED, params={"limit": 50, "action": "buy", "min_sol": 0.5}, headers=headers, timeout=20)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return None

def fetch_deployer_alerts():
    """Deployer-hunter con params"""
    headers = {"Authorization": f"Bearer {MADEONSOL_API_KEY}"}
    for params in [
        {"limit": 50, "min_score": 50, "period": "7d"},
        {"limit": 50},
        {},
    ]:
        try:
            r = requests.get(MADEONSOL_DEPLOYER, params=params, headers=headers, timeout=20)
            r.raise_for_status()
            data = r.json()
            if data:
                return data
        except Exception:
            continue
    return None

def fetch_dexscreener_boosted():
    """Dexscreener boosted tokens (alternativa a MemeScout)"""
    try:
        r = requests.get(DEXSCREENER_BOOSTED, timeout=20)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return None

def fetch_dexscreener(mint):
    try:
        r = requests.get(f"{DEXSCREENER_API}{mint}", timeout=20)
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
            "boosts": int(best.get("boosts", {}).get("active", 0) or 0),
            "dexId": best.get("dexId", ""),
            "pairAddress": best.get("pairAddress", "")
        }
    except Exception:
        return {"exists": False, "liquidityUsd": 0, "volume24hUsd": 0, "priceUsd": 0, "boosts": 0}

async def pumpportal_listen(duration_seconds=600, buffer_ref=None):
    print(f"[YIN] PumpPortal WS por {duration_seconds}s...")
    tokens = []
    try:
        async with websockets.connect(PUMPPORTAL_WS) as ws:
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
            print("[YIN] Suscrito a PumpPortal")
            start = time.time()
            while time.time() - start < duration_seconds:
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
                            tokens.append(token)
                            if buffer_ref is not None:
                                buffer_ref.append(token)
                            print(f"  [PASS] {token['symbol']} | {sol_amt:.2f} SOL | MCap {mcap_sol:.1f} SOL")
                except asyncio.TimeoutError:
                    continue
                except Exception as e:
                    pass
    except Exception as e:
        print(f"[ERROR] PumpPortal: {e}")
    return tokens

async def kol_polling_loop(duration_seconds=600, interval=30, kol_buffer_ref=None):
    """MadeOnSol REST polling cada 30s"""
    print(f"[YIN] KOL REST polling cada {interval}s por {duration_seconds}s...")
    kol_data = defaultdict(list)
    start = time.time()
    while time.time() - start < duration_seconds:
        data = fetch_kol_feed()
        if data:
            trades = data.get("trades", data.get("data", data if isinstance(data, list) else []))
            if isinstance(trades, list):
                for t in trades:
                    mint = t.get("token_mint") or t.get("mint")
                    if mint and (t.get("action") == "buy" or t.get("side") == "buy"):
                        kol_data[mint].append({
                            "kol_name": t.get("kol_name", t.get("trader", "?")),
                            "solAmount": float(t.get("solAmount", t.get("amount_sol", 0)) or 0),
                            "timestamp": t.get("traded_at", datetime.utcnow().isoformat() + "Z")
                        })
            if kol_buffer_ref is not None:
                kol_buffer_ref.update(kol_data)
            print(f"  [KOL] Mints acumulados: {len(kol_data)}")
        await asyncio.sleep(interval)
    return kol_data

def score_token_v5(token, dex_data, kol_buyers, elite_deployers, boosted_mints, deployer):
    sol_amount = token.get("solAmount", 0)
    mcap_sol = token.get("marketCapSol", 0)
    mint = token.get("mint", "")
    score = 0
    reasons = []

    # 1. Whale entry
    if sol_amount >= 85:
        score += 25; reasons.append(f"WHALE: {sol_amount:.0f} SOL")
    elif sol_amount >= 5:
        score += 15; reasons.append(f"Large: {sol_amount:.1f} SOL")
    elif sol_amount >= 0.5:
        score += 5; reasons.append(f"Min: {sol_amount:.2f} SOL")

    # 2. MCap SOL
    if mcap_sol >= 100:
        score += 15; reasons.append(f"MCap high: {mcap_sol:.0f}")
    elif mcap_sol >= 30:
        score += 10; reasons.append(f"MCap good: {mcap_sol:.0f}")
    elif mcap_sol >= 10:
        score += 5; reasons.append(f"MCap min: {mcap_sol:.0f}")

    # 3. Age
    score += 5; reasons.append("Age: T+0")

    # 4. KOL boost (REST)
    kol_names = []
    if kol_buyers:
        total_sol = sum(k.get("solAmount", 0) for k in kol_buyers)
        kol_names = [k.get("kol_name", "?") for k in kol_buyers]
        if len(kol_buyers) >= 2:
            score += 45; reasons.append(f"KOL x{len(kol_buyers)}: {', '.join(kol_names)}")
        elif total_sol >= 5:
            score += 30; reasons.append(f"KOL whale: {kol_names[0]}")
        else:
            score += 15; reasons.append(f"KOL: {kol_names[0]}")

    # 5. Deployer boost
    if deployer and deployer in elite_deployers:
        score += 10; reasons.append(f"Deployer ELITE")

    # 6. Dexscreener liquidity
    if dex_data.get("exists"):
        liq = dex_data.get("liquidityUsd", 0)
        if liq >= 20000:
            score += 10; reasons.append(f"Liq alta: ${liq:,.0f}")
        elif liq >= 10000:
            score += 5; reasons.append(f"Liq decente: ${liq:,.0f}")
        else:
            reasons.append(f"Liq baja: ${liq:,.0f}")
    else:
        reasons.append("Sin par Dexscreener")

    # 7. Trending boost (Dexscreener boosted como proxy MemeScout)
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

async def main():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Detection V5 - {timestamp}")

    # Deployers elite
    print("[YIN] Consultando deployers elite...")
    dep_data = fetch_deployer_alerts()
    elite_deployers = set()
    if dep_data:
        alerts = dep_data.get("alerts", dep_data.get("data", []))
        if isinstance(alerts, list):
            for a in alerts:
                score = a.get("score", 0)
                if isinstance(score, (int, float)) and score >= 50:
                    elite_deployers.add(a.get("deployer", a.get("address", "")))
    print(f"  Deployers elite: {len(elite_deployers)}")

    # Dexscreener boosted (proxy MemeScout)
    print("[YIN] Consultando Dexscreener boosted (proxy MemeScout)...")
    boosted_mints = set()
    boosted = fetch_dexscreener_boosted()
    if boosted:
        for b in boosted:
            token_addr = b.get("tokenAddress", "")
            if token_addr:
                boosted_mints.add(token_addr)
    print(f"  Boosted mints: {len(boosted_mints)}")

    # Captura paralela
    print("[YIN] Iniciando captura paralela (10 min)...")
    pp_buffer = []
    kol_buffer = defaultdict(list)

    pp_task = asyncio.create_task(pumpportal_listen(600, pp_buffer))
    kol_task = asyncio.create_task(kol_polling_loop(600, 30, kol_buffer))

    pp_tokens, kol_data = await asyncio.gather(pp_task, kol_task)

    print(f"\n[YIN] Captura completada:")
    print(f"  PumpPortal tokens: {len(pp_tokens)}")
    print(f"  KOL mints (REST): {len(kol_data)}")

    # Dedup
    print("[YIN] Aplicando dedup por deployer...")
    deployer_counts = defaultdict(list)
    for token in pp_tokens:
        dev = token.get("dev", "")
        if dev:
            deployer_counts[dev].append(token)

    deduped = []
    for dev, tokens in deployer_counts.items():
        if len(tokens) > 5:
            tokens.sort(key=lambda t: t.get("solAmount", 0), reverse=True)
            deduped.append(tokens[0])
            print(f"  [DEDUP] {dev[:8]}... {len(tokens)}->1 ({tokens[0]['symbol']})")
        else:
            deduped.extend(tokens)

    print(f"  Dedup: {len(pp_tokens)} -> {len(deduped)}")

    # Enriquecer + scoring
    print("[YIN] Enriqueciendo con Dexscreener + scoring V5...")
    results = []
    for token in deduped:
        mint = token.get("mint")
        deployer = token.get("dev", "")
        dex_data = fetch_dexscreener(mint)
        time.sleep(0.1)

        score, nivel, reasons, kol_names, in_trending = score_token_v5(
            token, dex_data, kol_data.get(mint, []), elite_deployers, boosted_mints, deployer
        )

        results.append({
            "symbol": token.get("symbol"),
            "mint": mint,
            "solAmount": token.get("solAmount"),
            "marketCapSol": token.get("marketCapSol"),
            "deployer": deployer,
            "kol_buyers": kol_names,
            "in_trending": in_trending,
            "dexscreener": dex_data,
            "score": score,
            "nivel": nivel,
            "reasons": reasons
        })
        print(f"  {token['symbol']} | Score {score} | {nivel} | KOLs {len(kol_names)} | Liq ${dex_data.get('liquidityUsd',0):,.0f} | Trending {in_trending}")

    alertas = [r for r in results if r["nivel"] == "ALERTA"]
    watch = [r for r in results if r["nivel"] == "WATCH"]
    descartar = [r for r in results if r["nivel"] == "DESCARTAR"]

    output = {
        "timestamp": timestamp,
        "fase": "detection_v5",
        "resumen": {
            "total": len(results),
            "alertas": len(alertas),
            "watch": len(watch),
            "descartar": len(descartar),
            "kol_matches": len([r for r in results if r["kol_buyers"]]),
            "trending_matches": len([r for r in results if r["in_trending"]]),
            "deployer_boosts": len([r for r in results if r.get("deployer") in elite_deployers]),
            "original": len(pp_tokens),
            "deduped": len(deduped)
        },
        "resultados": results
    }

    out_file = f"{OUTPUT_DIR}/detection_v5_{timestamp}.json"
    with open(out_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n[YIN] RESULTADOS:")
    print(f"  ALERTAS (>=70): {len(alertas)}")
    print(f"  WATCH (50-69): {len(watch)}")
    print(f"  DESCARTAR (<50): {len(descartar)}")
    print(f"  KOL matches: {len([r for r in results if r['kol_buyers']])}")
    print(f"  Trending matches: {len([r for r in results if r['in_trending']])}")
    print(f"  Guardado: {out_file}")

    if alertas:
        print("\n🚨 ALERTAS:")
        for r in alertas:
            print(f"  {r['symbol']} | Score {r['score']} | KOLs {r['kol_buyers']} | Trending {r['in_trending']}")
            for reason in r["reasons"]:
                print(f"    - {reason}")

    top3 = sorted(results, key=lambda x: x["score"], reverse=True)[:3]
    print("\n🏆 TOP 3:")
    for i, r in enumerate(top3, 1):
        print(f"  {i}. {r['symbol']} ({r['mint'][:8]}...) | Score {r['score']} | {r['nivel']}")
        for reason in r["reasons"]:
            print(f"    - {reason}")

if __name__ == "__main__":
    asyncio.run(main())
