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
DEXSCREENER_SEARCH = "https://api.dexscreener.com/latest/dex/search"

OUTPUT_DIR = "02_Analisis/detection_v3"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_madeonsol_kol_feed(limit=50, action="buy", min_sol=0.5):
    headers = {"Authorization": f"Bearer {MADEONSOL_API_KEY}"}
    params = {"limit": limit, "action": action, "min_sol": min_sol}
    try:
        r = requests.get(MADEONSOL_KOL_FEED, headers=headers, params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"[ERROR] MadeOnSol KOL feed: {e}")
        return None

def fetch_threews_trending(window="1h"):
    try:
        r = requests.get(THREEWS_TRENDING, params={"window": window}, timeout=30)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"[ERROR] three.ws {window}: {e}")
        return None

def fetch_dexscreener_trending():
    try:
        r = requests.get(DEXSCREENER_SEARCH, params={"q": "trending"}, timeout=30)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"[ERROR] Dexscreener trending: {e}")
        return None

async def pumpportal_listen(duration_seconds=600, buffer_ref=None, stop_event=None):
    """Escucha PumpPortal WebSocket, llena buffer compartido"""
    print(f"[YIN] PumpPortal WS por {duration_seconds}s...")
    tokens = []
    try:
        async with websockets.connect(PUMPPORTAL_WS) as ws:
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
            print("[YIN] Suscrito a PumpPortal")
            start = time.time()
            while time.time() - start < duration_seconds and not (stop_event and stop_event.is_set()):
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
                                "timestamp": datetime.utcnow().isoformat() + "Z",
                                "age_min": 0
                            }
                            tokens.append(token)
                            if buffer_ref is not None:
                                buffer_ref.append(token)
                            print(f"  [PASS] {token['symbol']} | {sol_amt:.2f} SOL | MCap {mcap_sol:.1f} SOL")
                except asyncio.TimeoutError:
                    continue
                except Exception as e:
                    print(f"[WS ERROR] {e}")
    except Exception as e:
        print(f"[ERROR] PumpPortal: {e}")
    return tokens

def poll_kols(duration_seconds=600, interval=60, kol_buffer_ref=None, stop_event=None):
    """Poll MadeOnSol KOL feed cada interval segundos"""
    print(f"[YIN] Iniciando KOL polling cada {interval}s por {duration_seconds}s...")
    all_kol_mints = set()
    kol_data_by_mint = {}
    start = time.time()
    while time.time() - start < duration_seconds and not (stop_event and stop_event.is_set()):
        data = fetch_madeonsol_kol_feed(limit=50, action="buy", min_sol=0.5)
        if data and "trades" in data:
            for trade in data["trades"]:
                mint = trade.get("token_mint")
                if mint:
                    all_kol_mints.add(mint)
                    if mint not in kol_data_by_mint:
                        kol_data_by_mint[mint] = []
                    kol_data_by_mint[mint].append(trade)
        if kol_buffer_ref is not None:
            kol_buffer_ref.clear()
            kol_buffer_ref.update(kol_data_by_mint)
        print(f"  [KOL] Mints únicos acumulados: {len(all_kol_mints)}")
        time.sleep(interval)
    return kol_data_by_mint

def fetch_trending_sources():
    """Consulta 3 fuentes de trending"""
    all_trending = {}
    
    # 1. three.ws 3 ventanas
    for window in ["1h", "4h", "24h"]:
        data = fetch_threews_trending(window)
        if data and "tokens" in data:
            for t in data["tokens"]:
                mint = t.get("mint")
                if mint:
                    all_trending[mint] = {"source": f"three.ws_{window}", "data": t}
    
    # 2. Dexscreener trending
    data = fetch_dexscreener_trending()
    if data and "pairs" in data:
        for pair in data["pairs"][:20]:
            mint = pair.get("baseToken", {}).get("address")
            if mint:
                all_trending[mint] = {"source": "dexscreener", "data": pair}
    
    # 3. PumpPortal trending (via API si existe)
    try:
        r = requests.get("https://pumpportal.fun/api/trending", timeout=30)
        if r.status_code == 200:
            data = r.json()
            if isinstance(data, list):
                for t in data:
                    mint = t.get("mint") or t.get("address")
                    if mint:
                        all_trending[mint] = {"source": "pumpportal", "data": t}
    except:
        pass
    
    return all_trending

def score_token_v3(token, kol_buyers, in_trending):
    """Scoring V3 recalibrado: max 100"""
    sol_amount = token.get("solAmount", 0)
    mcap_sol = token.get("marketCapSol", 0)
    
    score = 0
    reasons = []
    
    # WHALE ENTRY (0-25)
    if sol_amount >= 50:
        score += 25
        reasons.append(f"WHALE: {sol_amount:.0f} SOL")
    elif sol_amount >= 5:
        score += 15
        reasons.append(f"Large: {sol_amount:.1f} SOL")
    elif sol_amount >= 0.5:
        score += 5
        reasons.append(f"Min: {sol_amount:.2f} SOL")
    
    # MCAP SOL (0-15)
    if mcap_sol >= 100:
        score += 15
        reasons.append(f"MCap SOL high: {mcap_sol:.0f}")
    elif mcap_sol >= 30:
        score += 10
        reasons.append(f"MCap SOL good: {mcap_sol:.0f}")
    elif mcap_sol >= 10:
        score += 5
        reasons.append(f"MCap SOL min: {mcap_sol:.0f}")
    
    # AGE (0-10) - tokens son ~0 min, dar puntos base
    score += 5
    reasons.append("Age: T+0")
    
    # KOL BOOST (0-30)
    kol_boost = 0
    kol_names = []
    if kol_buyers:
        total_sol = sum(float(k.get("solAmount", 0) or 0) for k in kol_buyers)
        kol_names = [k.get("kol_name", "?") for k in kol_buyers]
        if len(kol_buyers) >= 2:
            kol_boost = 30
            reasons.append(f"KOL x{len(kol_buyers)}: {', '.join(kol_names)}")
        elif total_sol >= 5:
            kol_boost = 25
            reasons.append(f"KOL whale: {kol_names[0]} ({total_sol:.1f} SOL)")
        else:
            kol_boost = 15
            reasons.append(f"KOL: {kol_names[0]}")
    score += kol_boost
    
    # TRENDING BOOST (0-20)
    if in_trending:
        score += 20
        reasons.append("TRENDING")
    
    total = min(100, score)
    
    if total >= 70:
        nivel = "ALERTA"
    elif total >= 50:
        nivel = "WATCH"
    else:
        nivel = "DESCARTAR"
    
    return total, nivel, reasons, kol_names

def main():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Detection V3 - {timestamp}")
    
    # Buffer compartido
    pumpportal_buffer = []
    kol_buffer = {}
    stop_event = asyncio.Event()
    
    # 1. Obtener trending sources al inicio
    print("[YIN] Consultando trending sources...")
    trending = fetch_trending_sources()
    trending_mints = set(trending.keys())
    print(f"  Trending mints: {len(trending_mints)}")
    
    # 2. Iniciar PumpPortal y KOL polling en paralelo
    print("[YIN] Iniciando captura paralela (10 min)...")
    
    async def run_parallel():
        # Crear tasks
        pp_task = asyncio.create_task(pumpportal_listen(600, pumpportal_buffer, stop_event))
        
        # KOL polling en thread separado
        def run_kols():
            return poll_kols(600, 60, kol_buffer, stop_event)
        
        kol_task = asyncio.to_thread(run_kols)
        
        # Esperar ambos
        pp_tokens, kol_data = await asyncio.gather(pp_task, kol_task)
        return pp_tokens, kol_data
    
    pp_tokens, kol_data = asyncio.run(run_parallel())
    
    # Actualizar kol_buffer final
    kol_buffer.update(kol_data)
    
    print(f"\n[YIN] Captura completada:")
    print(f"  PumpPortal tokens: {len(pumpportal_buffer)}")
    print(f"  KOL mints: {len(kol_buffer)}")
    print(f"  Trending mints: {len(trending_mints)}")
    
    # 3. Cross-match y scoring
    print("[YIN] Aplicando scoring V3...")
    results = []
    
    for token in pumpportal_buffer:
        mint = token.get("mint")
        kol_buyers = kol_buffer.get(mint, [])
        in_trending = mint in trending_mints
        
        score, nivel, reasons, kol_names = score_token_v3(token, kol_buyers, in_trending)
        
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
    
    # 4. Guardar
    alertas = [r for r in results if r["nivel"] == "ALERTA"]
    watch = [r for r in results if r["nivel"] == "WATCH"]
    descartar = [r for r in results if r["nivel"] == "DESCARTAR"]
    
    output = {
        "timestamp": timestamp,
        "fase": "detection_v3",
        "resumen": {
            "total_capturados": len(results),
            "alertas": len(alertas),
            "watch": len(watch),
            "descartar": len(descartar),
            "kol_mints": len(kol_buffer),
            "trending_mints": len(trending_mints)
        },
        "resultados": results
    }
    
    output_file = f"{OUTPUT_DIR}/detection_v3_{timestamp}.json"
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
    
    # Top 3
    top3 = sorted(results, key=lambda x: x["score"], reverse=True)[:3]
    print("\n🏆 TOP 3:")
    for i, r in enumerate(top3, 1):
        print(f"  {i}. {r['symbol']} ({r['mint'][:8]}...) | Score {r['score']} | {r['nivel']}")
        for reason in r["reasons"]:
            print(f"    - {reason}")
    
    return output

if __name__ == "__main__":
    import time
    main()