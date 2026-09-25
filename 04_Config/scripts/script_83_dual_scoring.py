#!/usr/bin/env python3
import asyncio
import json
import time
import requests
import websockets
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

MADEONSOL_API_KEY = os.getenv("MADEONSOL_API_KEY")
PUMPPORTAL_WS = "wss://pumpportal.fun/api/data"
THREEWS_TRENDING = "https://three.ws/api/crypto/trending"
MADEONSOL_KOL_FEED = "https://madeonsol.com/api/v1/kol/feed"

OUTPUT_DIR = "02_Analisis/dual_scoring"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_madeonsol_kol_feed(limit=50, action="buy", min_sol=0.5):
    """Consulta MadeOnSol KOL feed"""
    headers = {"Authorization": f"Bearer {MADEONSOL_API_KEY}"}
    params = {"limit": limit, "action": action, "min_sol": min_sol}
    try:
        r = requests.get(MADEONSOL_KOL_FEED, headers=headers, params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"[ERROR] MadeOnSol KOL feed: {e}")
        return None

def fetch_threews_trending():
    """Consulta three.ws trending"""
    try:
        r = requests.get(THREEWS_TRENDING, params={"window": "1h"}, timeout=30)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"[ERROR] three.ws trending: {e}")
        return None

def score_token_dual(token, kol_buyers, in_trending):
    """Scoring dual T+0: Base (0-50) + KOL boost (0-30) + WS boost (0-20)"""
    sol_amount = token.get("solAmount", 0)
    mcap_sol = token.get("marketCapSol", 0)
    age_min = 0  # PumpPortal tokens are ~0 min old
    
    # BASE SCORE (0-50)
    base = 0
    reasons = []
    
    # solAmount weight
    if sol_amount >= 10:
        base += 15
        reasons.append(f"Whale entry: {sol_amount:.1f} SOL")
    elif sol_amount >= 5:
        base += 10
        reasons.append(f"Large entry: {sol_amount:.1f} SOL")
    elif sol_amount >= 1:
        base += 7
        reasons.append(f"Decent entry: {sol_amount:.2f} SOL")
    elif sol_amount >= 0.5:
        base += 3
        reasons.append(f"Min entry: {sol_amount:.2f} SOL")
    
    # marketCapSol weight
    if 10 <= mcap_sol <= 100:
        base += 15
        reasons.append(f"MCap sweet spot: {mcap_sol:.0f} SOL")
    elif 100 < mcap_sol <= 500:
        base += 10
        reasons.append(f"MCap growing: {mcap_sol:.0f} SOL")
    elif 500 < mcap_sol <= 2000:
        base += 5
        reasons.append(f"MCap mid: {mcap_sol:.0f} SOL")
    elif mcap_sol > 2000:
        reasons.append(f"MCap high: {mcap_sol:.0f} SOL")
    
    # KOL BOOST (0-30)
    kol_boost = 0
    kol_names = [k.get("kol_name", "?") for k in kol_buyers]
    if len(kol_buyers) >= 2:
        kol_boost = 30
        reasons.append(f"KOL BOOST x{len(kol_buyers)}: {', '.join(kol_names)}")
    elif len(kol_buyers) == 1:
        kol_boost = 15
        reasons.append(f"KOL BOOST: {kol_names[0]}")
    
    # WS BOOST (0-20)
    ws_boost = 20 if in_trending else 0
    if in_trending:
        reasons.append("WS TRENDING: token en three.ws")
    
    total = min(100, base + kol_boost + ws_boost)
    
    if total >= 70:
        nivel = "ALERTA"
    elif total >= 50:
        nivel = "WATCH"
    else:
        nivel = "DESCARTAR"
    
    return total, nivel, reasons, kol_names

async def pumpportal_listen(duration_seconds=300):
    """Escucha PumpPortal WebSocket"""
    print(f"[YIN] PumpPortal WS por {duration_seconds}s...")
    tokens = []
    try:
        async with websockets.connect(PUMPPORTAL_WS) as ws:
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
            print("[YIN] Suscrito")
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
                                "initialBuy": float(data.get("initialBuy", 0) or 0),
                                "pool": data.get("pool", "pump"),
                                "is_mayhem_mode": data.get("is_mayhem_mode", False),
                                "timestamp": datetime.utcnow().isoformat() + "Z"
                            }
                            tokens.append(token)
                            print(f"  [PASS] {token['symbol']} | {sol_amt:.2f} SOL | MCap {mcap_sol:.1f} SOL")
                        else:
                            pass  # silently discard
                except asyncio.TimeoutError:
                    continue
                except Exception as e:
                    print(f"[WS ERROR] {e}")
    except Exception as e:
        print(f"[ERROR] PumpPortal: {e}")
    return tokens

def main():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Dual Scoring Pipeline - {timestamp}")
    
    # 1. Fetch KOL feed
    print("[YIN] Consultando MadeOnSol KOL feed...")
    kol_data = fetch_madeonsol_kol_feed(limit=50, action="buy", min_sol=0.5)
    kol_by_mint = {}
    if kol_data and "trades" in kol_data:
        for trade in kol_data["trades"]:
            mint = trade.get("token_mint")
            if mint:
                if mint not in kol_by_mint:
                    kol_by_mint[mint] = []
                kol_by_mint[mint].append(trade)
    print(f"  KOL trades: {len(kol_by_mint)} mints únicos")
    
    # 2. Fetch three.ws trending
    print("[YIN] Consultando three.ws trending...")
    ws_data = fetch_threews_trending()
    trending_mints = set()
    if ws_data and "tokens" in ws_data:
        for t in ws_data["tokens"]:
            trending_mints.add(t.get("mint"))
    print(f"  Trending mints: {len(trending_mints)}")
    
    # 3. PumpPortal WS
    print("[YIN] Iniciando PumpPortal WebSocket (5 min)...")
    pp_tokens = asyncio.run(pumpportal_listen(300))
    print(f"  Tokens filtrados: {len(pp_tokens)}")
    
    # 4. Score cada token
    print("[YIN] Aplicando scoring dual...")
    results = []
    for token in pp_tokens:
        mint = token.get("mint")
        kol_buyers = kol_by_mint.get(mint, [])
        in_trending = mint in trending_mints
        
        score, nivel, reasons, kol_names = score_token_dual(token, kol_buyers, in_trending)
        
        result = {
            "symbol": token.get("symbol"),
            "name": token.get("name"),
            "mint": mint,
            "solAmount": token.get("solAmount"),
            "marketCapSol": token.get("marketCapSol"),
            "pool": token.get("pool"),
            "is_mayhem_mode": token.get("is_mayhem_mode"),
            "kol_buyers": kol_names,
            "in_trending": in_trending,
            "score": score,
            "nivel": nivel,
            "reasons": reasons
        }
        results.append(result)
        print(f"  {token['symbol']} | Score: {score} | {nivel} | KOLs: {len(kol_buyers)} | Trending: {in_trending}")
    
    # 5. Guardar
    alertas = [r for r in results if r["nivel"] == "ALERTA"]
    watch = [r for r in results if r["nivel"] == "WATCH"]
    descartar = [r for r in results if r["nivel"] == "DESCARTAR"]
    
    output = {
        "timestamp": timestamp,
        "fase": "dual_scoring",
        "resumen": {
            "total_capturados": len(results),
            "alertas": len(alertas),
            "watch": len(watch),
            "descartar": len(descartar),
            "kol_mints": len(kol_by_mint),
            "trending_mints": len(trending_mints)
        },
        "resultados": results
    }
    
    output_file = f"{OUTPUT_DIR}/dual_{timestamp}.json"
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\n[YIN] RESULTADOS:")
    print(f"  ALERTAS (>=70): {len(alertas)}")
    print(f"  WATCH (50-69): {len(watch)}")
    print(f"  DESCARTAR (<50): {len(descartar)}")
    print(f"  Guardado: {output_file}")
    
    if alertas:
        print("\n🚨 ALERTAS:")
        for r in alertas:
            print(f"  {r['symbol']} | Score {r['score']} | KOLs: {r['kol_buyers']} | Trending: {r['in_trending']}")
            for reason in r["reasons"]:
                print(f"    - {reason}")
    
    return output

if __name__ == "__main__":
    import time
    main()