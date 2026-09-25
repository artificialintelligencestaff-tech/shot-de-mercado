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
MADEONSOL_WS = "wss://madeonsol.com/ws/v1/stream"
MADEONSOL_DEPLOYER_ALERTS = "https://madeonsol.com/api/v1/deployer-hunter/alerts"
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/tokens/"
THREEWS_TRENDING = "https://three.ws/api/crypto/trending"

OUTPUT_DIR = "02_Analisis/detection_v4"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_madeonsol_deployer_alerts():
    """Consulta deployers elite (score >= 80)"""
    headers = {"Authorization": f"Bearer {MADEONSOL_API_KEY}"}
    try:
        r = requests.get(MADEONSOL_DEPLOYER_ALERTS, headers=headers, timeout=30)
        r.raise_for_status()
        data = r.json()
        elite = set()
        if "alerts" in data:
            for alert in data["alerts"]:
                if alert.get("score", 0) >= 80:
                    elite.add(alert.get("deployer"))
        return elite
    except Exception as e:
        print(f"[ERROR] MadeOnSol deployer alerts: {e}")
        return set()

def fetch_threews_trending_24h():
    """Consulta three.ws trending 24h"""
    try:
        r = requests.get(THREEWS_TRENDING, params={"window": "24h"}, timeout=30)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"[ERROR] three.ws 24h: {e}")
        return None

def fetch_dexscreener(mint):
    """Consulta Dexscreener para un mint"""
    try:
        r = requests.get(f"{DEXSCREENER_API}{mint}", timeout=30)
        r.raise_for_status()
        data = r.json()
        pairs = data.get("pairs", [])
        if not pairs:
            return {"exists": False, "liquidityUsd": 0, "volume24hUsd": 0, "priceUsd": 0}
        best = max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0))
        return {
            "exists": True,
            "priceUsd": float(best.get("priceUsd", 0) or 0),
            "liquidityUsd": float(best.get("liquidity", {}).get("usd", 0) or 0),
            "volume24hUsd": float(best.get("volume", {}).get("h24", 0) or 0),
            "marketCapUsd": float(best.get("marketCap", 0) or 0),
            "dexId": best.get("dexId", ""),
            "pairAddress": best.get("pairAddress", "")
        }
    except Exception as e:
        print(f"[ERROR] Dexscreener {mint}: {e}")
        return {"exists": False, "liquidityUsd": 0, "volume24hUsd": 0, "priceUsd": 0}

def fetch_trending_24h():
    """Consulta three.ws trending 24h para trending boost"""
    data = fetch_threews_trending_24h()
    trending = set()
    if data and "tokens" in data:
        for t in data["tokens"]:
            mint = t.get("mint")
            if mint:
                trending.add(mint)
    return trending

async def pumpportal_listen(duration_seconds=600, buffer_ref=None):
    """Escucha PumpPortal WebSocket"""
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
                                "initialBuy": float(data.get("initialBuy", 0) or 0),
                                "pool": data.get("pool", "pump"),
                                "is_mayhem_mode": data.get("is_mayhem_mode", False),
                                "dev": data.get("dev", ""),
                                "timestamp": datetime.utcnow().isoformat() + "Z"
                            }
                            tokens.append(token)
                            if buffer_ref is not None:
                                buffer_ref.append(token)
                            print(f"  [PASS] {token['symbol']} | {sol_amt:.2f} SOL | MCap {mcap_sol:.1f} SOL | dev: {token['dev'][:8]}...")
                except asyncio.TimeoutError:
                    continue
                except Exception as e:
                    print(f"[WS ERROR] {e}")
    except Exception as e:
        print(f"[ERROR] PumpPortal: {e}")
    return tokens

async def madeonsol_ws_listen(duration_seconds=600, kol_buffer_ref=None):
    """Escucha MadeOnSol WebSocket para KOL trades en tiempo real"""
    print(f"[YIN] MadeOnSol WS por {duration_seconds}s...")
    kol_data = defaultdict(list)
    try:
        async with websockets.connect(MADEONSOL_WS) as ws:
            # Obtener token de stream
            await ws.send(json.dumps({"type": "get_stream_token"}))
            resp = await ws.recv()
            token_data = json.loads(resp)
            stream_token = token_data.get("token")
            
            # Suscribirse a kol:trades
            await ws.send(json.dumps({
                "type": "subscribe",
                "channels": ["kol:trades"],
                "token": stream_token
            }))
            print("[YIN] Suscrito a MadeOnSol kol:trades")
            
            start = time.time()
            while time.time() - start < duration_seconds:
                try:
                    msg = await asyncio.wait_for(ws.recv(), timeout=5.0)
                    data = json.loads(msg)
                    
                    if data.get("channel") == "kol:trades":
                        for trade in data.get("data", []):
                            mint = trade.get("token_mint")
                            if mint and trade.get("action") == "buy":
                                kol_info = {
                                    "kol_name": trade.get("kol_name", "?"),
                                    "kol_twitter": trade.get("kol_twitter", ""),
                                    "solAmount": float(trade.get("solAmount", 0) or 0),
                                    "timestamp": trade.get("traded_at", datetime.utcnow().isoformat() + "Z")
                                }
                                kol_data[mint].append(kol_info)
                                print(f"  [KOL WS] {kol_info['kol_name']} compró {mint[:8]}... | {kol_info['solAmount']:.2f} SOL")
                except asyncio.TimeoutError:
                    continue
                except Exception as e:
                    print(f"[MadeOnSol WS ERROR] {e}")
    except Exception as e:
        print(f"[ERROR] MadeOnSol WS: {e}")
    return kol_data

def score_token_v4(token, dex_data, kol_buyers, elite_deployers, trending_24h, deployer):
    """Scoring V4: 7 factores, max 100"""
    sol_amount = token.get("solAmount", 0)
    mcap_sol = token.get("marketCapSol", 0)
    
    score = 0
    reasons = []
    
    # 1. WHALE ENTRY (0-25)
    if sol_amount >= 85:
        score += 25
        reasons.append(f"WHALE: {sol_amount:.0f} SOL")
    elif sol_amount >= 5:
        score += 15
        reasons.append(f"Large: {sol_amount:.1f} SOL")
    elif sol_amount >= 0.5:
        score += 5
        reasons.append(f"Min: {sol_amount:.2f} SOL")
    
    # 2. MCAP SOL (0-15)
    if mcap_sol >= 100:
        score += 15
        reasons.append(f"MCap SOL high: {mcap_sol:.0f}")
    elif mcap_sol >= 30:
        score += 10
        reasons.append(f"MCap SOL good: {mcap_sol:.0f}")
    elif mcap_sol >= 10:
        score += 5
        reasons.append(f"MCap SOL min: {mcap_sol:.0f}")
    
    # 3. AGE (0-10) - todos son ~0 min
    score += 5
    reasons.append("Age: T+0")
    
    # 4. KOL BOOST (0-45)
    kol_boost = 0
    kol_names = []
    if kol_buyers:
        total_sol = sum(k.get("solAmount", 0) for k in kol_buyers)
        kol_names = [k.get("kol_name", "?") for k in kol_buyers]
        if len(kol_buyers) >= 2:
            kol_boost = 45
            reasons.append(f"KOL x{len(kol_buyers)}: {', '.join(kol_names)}")
        elif total_sol >= 5:
            kol_boost = 30
            reasons.append(f"KOL whale: {kol_names[0]} ({total_sol:.1f} SOL)")
        else:
            kol_boost = 15
            reasons.append(f"KOL: {kol_names[0]}")
    score += kol_boost
    
    # 5. DEPLOYER BOOST (0-10)
    if deployer and deployer in elite_deployers:
        score += 10
        reasons.append(f"Deployer ELITE: {deployer[:8]}...")
    
    # 6. DEXSCREENER LIQUIDITY (0-10)
    if dex_data.get("exists"):
        liq = dex_data.get("liquidityUsd", 0)
        if liq >= 20000:
            score += 10
            reasons.append(f"Liq alta: ${liq:,.0f}")
        elif liq >= 10000:
            score += 5
            reasons.append(f"Liq decente: ${liq:,.0f}")
        else:
            reasons.append(f"Liq baja: ${liq:,.0f}")
    else:
        reasons.append("Sin par Dexscreener (T+0)")
    
    # 7. TRENDING BOOST (0-20)
    in_trending = False
    if token.get("mint") in trending_24h:
        in_trending = True
        score += 20
        reasons.append("TRENDING 24h")
    
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
    print(f"[YIN] Detection V4 - {timestamp}")
    
    # 1. Obtener deployers elite
    print("[YIN] Consultando deployers elite...")
    elite_deployers = fetch_madeonsol_deployer_alerts()
    print(f"  Deployers elite (score>=80): {len(elite_deployers)}")
    
    # 2. Obtener trending 24h
    print("[YIN] Consultando trending 24h...")
    trending_24h = fetch_trending_24h()
    print(f"  Trending 24h mints: {len(trending_24h)}")
    
    # 3. Captura paralela
    print("[YIN] Iniciando captura paralela (10 min)...")
    
    pumpportal_buffer = []
    kol_buffer = defaultdict(list)
    
    # Ejecutar en paralelo
    pp_task = asyncio.create_task(pumpportal_listen(600, pumpportal_buffer))
    kol_task = asyncio.create_task(madeonsol_ws_listen(600, kol_buffer))
    
    pp_tokens, kol_data = await asyncio.gather(pp_task, kol_task)
    
    print(f"\n[YIN] Captura completada:")
    print(f"  PumpPortal tokens: {len(pp_tokens)}")
    print(f"  KOL mints (WS): {len(kol_data)}")
    
    # 4. Dedup por deployer
    print("[YIN] Aplicando dedup por deployer...")
    deployer_counts = defaultdict(list)
    tokens_with_deployer = []
    tokens_without_deployer = []
    
    for token in pp_tokens:
        dev = token.get("dev", "")
        if dev:
            deployer_counts[dev].append(token)
            tokens_with_deployer.append(token)
        else:
            tokens_without_deployer.append(token)
    
    # Solo conservar el de mayor solAmount por deployer con >5 mints
    deduped = []
    for dev, tokens in deployer_counts.items():
        if len(tokens) > 5:
            # Ordenar por solAmount descendente
            tokens.sort(key=lambda t: t.get("solAmount", 0), reverse=True)
            deduped.append(tokens[0])
            print(f"  [DEDUP] Deployer {dev[:8]}... tenía {len(tokens)} mints, conservando {tokens[0]['symbol']} ({tokens[0]['solAmount']:.1f} SOL)")
        else:
            deduped.extend(tokens)
    
    # Añadir tokens sin deployer
    deduped.extend(tokens_without_deployer)
    
    print(f"  Tokens después de dedup: {len(deduped)} (antes: {len(pp_tokens)})")
    
    # 4. Enriquecer con Dexscreener y scoring
    print("[YIN] Enriqueciendo con Dexscreener y aplicando scoring V4...")
    results = []
    
    for token in deduped:
        mint = token.get("mint")
        deployer = token.get("dev", "")
        kol_buyers = kol_data.get(mint, [])
        in_trending = mint in trending_24h
        
        print(f"  Dexscreener: {mint[:8]}... (deployer: {deployer[:8]}...)")
        dex_data = fetch_dexscreener(mint)
        time.sleep(0.15)
        
        score, nivel, reasons, kol_names, in_trending = score_token_v4(
            token, dex_data, kol_data.get(mint, []), elite_deployers, trending_24h, deployer
        )
        
        result = {
            "symbol": token.get("symbol"),
            "name": token.get("name"),
            "mint": mint,
            "solAmount": token.get("solAmount"),
            "marketCapSol": token.get("marketCapSol"),
            "pool": token.get("pool"),
            "is_mayhem_mode": token.get("is_mayhem_mode"),
            "deployer": deployer,
            "kol_buyers": kol_names,
            "in_trending": in_trending,
            "dexscreener": dex_data,
            "score": score,
            "nivel": nivel,
            "reasons": reasons
        }
        results.append(result)
        print(f"  {token['symbol']} | Score: {score} | {nivel} | KOLs: {len(kol_buyers)} | Deployer: {deployer[:8] if deployer else '?'} | Liq: ${dex_data.get('liquidityUsd', 0):,.0f} | Trending: {in_trending}")
    
    # 5. Guardar
    alertas = [r for r in results if r["nivel"] == "ALERTA"]
    watch = [r for r in results if r["nivel"] == "WATCH"]
    descartar = [r for r in results if r["nivel"] == "DESCARTAR"]
    
    output = {
        "timestamp": timestamp,
        "fase": "detection_v4",
        "resumen": {
            "total_capturados": len(results),
            "alertas": len(alertas),
            "watch": len(watch),
            "descartar": len(descartar),
            "kol_matches": len([r for r in results if r["kol_buyers"]]),
            "trending_matches": len([r for r in results if r["in_trending"]]),
            "deployer_boosts": len([r for r in results if r.get("deployer") in elite_deployers]),
            "original_tokens": len(pp_tokens),
            "deduped_tokens": len(deduped)
        },
        "resultados": results
    }
    
    output_file = f"{OUTPUT_DIR}/detection_v4_{timestamp}.json"
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\n[YIN] RESULTADOS:")
    print(f"  ALERTAS (>=70): {len(alertas)}")
    print(f"  WATCH (50-69): {len(watch)}")
    print(f"  DESCARTAR (<50): {len(descartar)}")
    print(f"  KOL matches: {len([r for r in results if r['kol_buyers']])}")
    print(f"  Deployer elite boosts: {len([r for r in results if r.get('deployer') in elite_deployers])}")
    print(f"  Trending 24h matches: {len([r for r in results if r['in_trending']])}")
    print(f"  Dedup aplicado: {len(pp_tokens)} -> {len(deduped)}")
    print(f"  Guardado: {output_file}")
    
    if alertas:
        print("\n🚨 ALERTAS:")
        for r in alertas:
            print(f"  {r['symbol']} | Score {r['score']} | KOLs: {r['kol_buyers']} | Deployer elite: {r['deployer'] in elite_deployers} | Trending: {r['in_trending']}")
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
    asyncio.run(main())