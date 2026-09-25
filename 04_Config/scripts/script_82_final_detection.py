#!/usr/bin/env python3
import asyncio
import json
import time
import requests
import websockets
from datetime import datetime
from collections import OrderedDict

# Config
THREEWS_BASE = "https://three.ws/api/crypto"
PUMPPORTAL_WS = "wss://pumpportal.fun/api/data"
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/tokens/"

OUTPUT_DIR = "03_Informes/shot_de_mercado"
RAW_DIR = "01_Datos_Crudos/final_detection"

import os
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(RAW_DIR, exist_ok=True)

def fetch_threews_trending(window):
    """Consulta three.ws trending con ventana específica"""
    url = f"{THREEWS_BASE}/trending?window={window}"
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"[ERROR] three.ws {window}: {e}")
        return None

def fetch_dexscreener(mint):
    """Consulta Dexscreener para un mint"""
    url = f"{DEXSCREENER_API}{mint}"
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        data = r.json()
        pairs = data.get("pairs", [])
        if not pairs:
            return None
        best = max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0))
        return {
            "priceUsd": float(best.get("priceUsd", 0) or 0),
            "liquidityUsd": float(best.get("liquidity", {}).get("usd", 0) or 0),
            "volume24hUsd": float(best.get("volume", {}).get("h24", 0) or 0),
            "marketCapUsd": float(best.get("marketCap", 0) or 0),
            "priceChange24h": float(best.get("priceChange", {}).get("h24", 0) or 0),
            "dexId": best.get("dexId", ""),
            "pairAddress": best.get("pairAddress", "")
        }
    except Exception as e:
        print(f"[ERROR] Dexscreener {mint}: {e}")
        return None

def score_token(token_data, dexscreener_data=None):
    """Scoring adaptativo 0-100"""
    score = 0
    reasons = []
    
    ws_score = token_data.get("score", 0)
    score += ws_score * 0.3
    if ws_score >= 80:
        reasons.append("WS score muy alto")
    elif ws_score >= 60:
        reasons.append("WS score alto")
    
    mcap = token_data.get("marketCapUsd", 0)
    if dexscreener_data and dexscreener_data.get("marketCapUsd"):
        mcap = dexscreener_data["marketCapUsd"]
    
    if mcap >= 1_000_000:
        score += 25
        reasons.append("MCap > $1M")
    elif mcap >= 100_000:
        score += 15
        reasons.append("MCap > $100K")
    elif mcap >= 50_000:
        score += 10
        reasons.append("MCap > $50K")
    else:
        reasons.append("MCap bajo")
    
    vol = token_data.get("volumeUsd", 0)
    if dexscreener_data and dexscreener_data.get("volume24hUsd"):
        vol = dexscreener_data["volume24hUsd"]
    
    if vol >= 1_000_000:
        score += 20
        reasons.append("Volumen masivo")
    elif vol >= 100_000:
        score += 15
        reasons.append("Volumen alto")
    elif vol >= 50_000:
        score += 10
        reasons.append("Volumen decente")
    else:
        reasons.append("Volumen bajo")
    
    liq = 0
    if dexscreener_data and dexscreener_data.get("liquidityUsd"):
        liq = dexscreener_data["liquidityUsd"]
    
    if liq >= 100_000:
        score += 15
        reasons.append("Liquidez alta")
    elif liq >= 50_000:
        score += 10
        reasons.append("Liquidez decente")
    elif liq >= 20_000:
        score += 5
        reasons.append("Liquidez mínima")
    else:
        reasons.append("Liquidez baja")
    
    change = token_data.get("change", 0)
    if dexscreener_data and dexscreener_data.get("priceChange24h"):
        change = dexscreener_data["priceChange24h"]
    
    if change >= 50:
        score += 10
        reasons.append("Pump 24h")
    elif change >= 20:
        score += 5
        reasons.append("Subida 24h")
    elif change <= -30:
        score -= 5
        reasons.append("Dump 24h")
    
    return min(100, max(0, int(score))), reasons

async def pumpportal_listen(duration_seconds=300):
    """Escucha PumpPortal WebSocket por N segundos"""
    print(f"[YIN] Conectando a PumpPortal WebSocket por {duration_seconds}s...")
    tokens = []
    
    try:
        async with websockets.connect(PUMPPORTAL_WS) as ws:
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
            print("[YIN] Suscrito a nuevos tokens")
            
            start = time.time()
            while time.time() - start < duration_seconds:
                try:
                    msg = await asyncio.wait_for(ws.recv(), timeout=5.0)
                    data = json.loads(msg)
                    
                    if data.get("txType") == "create":
                        token = {
                            "mint": data.get("mint"),
                            "symbol": data.get("symbol", "?"),
                            "name": data.get("name", "?"),
                            "solAmount": float(data.get("solAmount", 0) or 0),
                            "marketCapSol": float(data.get("marketCapSol", 0) or 0),
                            "initialBuy": float(data.get("initialBuy", 0) or 0),
                            "bondingCurveKey": data.get("bondingCurveKey"),
                            "vTokensInBondingCurve": float(data.get("vTokensInBondingCurve", 0) or 0),
                            "vSolInBondingCurve": float(data.get("vSolInBondingCurve", 0) or 0),
                            "pool": data.get("pool", "pump"),
                            "is_mayhem_mode": data.get("is_mayhem_mode", False),
                            "uri": data.get("uri", ""),
                            "signature": data.get("signature"),
                            "traderPublicKey": data.get("traderPublicKey"),
                            "timestamp": datetime.utcnow().isoformat() + "Z"
                        }
                        tokens.append(token)
                        print(f"  [NEW] {token['symbol']} | {token['solAmount']:.4f} SOL | MCap {token['marketCapSol']:.2f} SOL")
                        
                except asyncio.TimeoutError:
                    continue
                except Exception as e:
                    print(f"[WS ERROR] {e}")
                    continue
                    
    except Exception as e:
        print(f"[ERROR] PumpPortal connection: {e}")
    
    return tokens

def filter_pumpportal_tokens(tokens):
    """Aplica filtros: solAmount >= 0.5, marketCapSol 10-5000"""
    passed = []
    failed = []
    for t in tokens:
        sol_amt = t.get("solAmount", 0)
        mcap_sol = t.get("marketCapSol", 0)
        
        if sol_amt >= 0.5 and 10 <= mcap_sol <= 5000:
            passed.append(t)
        else:
            reason = []
            if sol_amt < 0.5:
                reason.append(f"solAmount {sol_amt:.4f} < 0.5")
            if mcap_sol < 10 or mcap_sol > 5000:
                reason.append(f"marketCapSol {mcap_sol:.2f} fuera de rango 10-5000")
            failed.append({"token": t, "razon": "; ".join(reason)})
    return passed, failed

def main():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Pipeline Final Detection - {timestamp}")
    
    # ===== 1. THREE.WS TRENDING - 3 VENTANAS =====
    print("\n[YIN] Consultando three.ws /trending (1h, 4h, 24h)...")
    all_trending = {}
    windows = ["1h", "4h", "24h"]
    
    for window in windows:
        data = fetch_threews_trending(window)
        if data and "tokens" in data:
            for token in data["tokens"]:
                mint = token.get("mint")
                if mint and mint not in all_trending:
                    token["window"] = window
                    all_trending[mint] = token
            print(f"  {window}: {len(data.get('tokens', []))} tokens")
    
    trending_tokens = list(all_trending.values())
    print(f"  TOTAL ÚNICOS: {len(trending_tokens)}")
    
    # ===== 2. PUMPPORTAL WEBSOCKET =====
    print("\n[YIN] Iniciando PumpPortal WebSocket...")
    pp_tokens = asyncio.run(pumpportal_listen(300))
    print(f"  Capturados: {len(pp_tokens)}")
    
    pp_passed, pp_failed = filter_pumpportal_tokens(pp_tokens)
    print(f"  Pasan filtros: {len(pp_passed)}")
    print(f"  Descartados: {len(pp_failed)}")
    
    # ===== 3. ENRIQUECER CON DEXSCREENER =====
    print("\n[YIN] Enriqueciendo con Dexscreener...")
    
    tokens_to_enrich = {}
    
    for t in trending_tokens:
        mint = t.get("mint")
        if mint:
            tokens_to_enrich[mint] = {"source": "trending", "data": t, "windows": t.get("window")}
    
    for t in pp_passed:
        mint = t.get("mint")
        if mint and mint not in tokens_to_enrich:
            tokens_to_enrich[mint] = {"source": "pumpportal", "data": t}
    
    print(f"  Tokens a enriquecer: {len(tokens_to_enrich)}")
    
    enriched = {}
    for mint, info in tokens_to_enrich.items():
        print(f"  Dexscreener: {mint[:8]}... ({info['source']})")
        dex_data = fetch_dexscreener(mint)
        if dex_data:
            score, reasons = score_token(info["data"], dex_data)
            enriched[mint] = {
                "source": info["source"],
                "windows": info.get("windows"),
                "token": info["data"],
                "dexscreener": dex_data,
                "score": score,
                "reasons": reasons
            }
        else:
            score, reasons = score_token(info["data"])
            enriched[mint] = {
                "source": info["source"],
                "windows": info.get("windows"),
                "token": info["data"],
                "dexscreener": None,
                "score": score,
                "reasons": reasons
            }
        time.sleep(0.2)
    
    # ===== RESULTADOS =====
    alertas = {m: d for m, d in enriched.items() if d["score"] >= 70}
    watch = {m: d for m, d in enriched.items() if 50 <= d["score"] < 70}
    descartar = {m: d for m, d in enriched.items() if d["score"] < 50}
    
    print(f"\n[YIN] RESULTADOS:")
    print(f"  ALERTAS (>=70): {len(alertas)}")
    print(f"  WATCH (50-69): {len(watch)}")
    print(f"  DESCARTAR (<50): {len(descartar)}")
    
    raw_file = f"{RAW_DIR}/detection_{timestamp}.json"
    with open(raw_file, "w") as f:
        json.dump({
            "timestamp": timestamp,
            "trending_raw": trending_tokens,
            "pumpportal_raw": pp_tokens,
            "pumpportal_filtered": pp_passed,
            "pumpportal_failed": pp_failed,
            "enriched": enriched
        }, f, indent=2)
    print(f"  Raw guardado: {raw_file}")
    
    report = {
        "timestamp": timestamp,
        "fase": "final_detection",
        "resumen": {
            "trending_unicos": len(trending_tokens),
            "pumpportal_capturados": len(pp_tokens),
            "pumpportal_filtrados": len(pp_passed),
            "total_enriquecidos": len(enriched),
            "alertas": len(alertas),
            "watch": len(watch),
            "descartar": len(descartar)
        },
        "trending": [],
        "pumpportal": [],
        "alertas": [],
        "watch": [],
        "descartar": []
    }
    
    for mint, data in enriched.items():
        if data["source"] == "trending":
            t = data["token"]
            d = data["dexscreener"]
            report["trending"].append({
                "symbol": t.get("symbol"),
                "mint": mint,
                "marketCapUsd": d.get("marketCapUsd") if d else t.get("marketCapUsd"),
                "volumeUsd": d.get("volume24hUsd") if d else t.get("volumeUsd"),
                "liquidityUsd": d.get("liquidityUsd") if d else None,
                "score": data["score"],
                "nivel": "ALERTA" if data["score"] >= 70 else "WATCH" if data["score"] >= 50 else "DESCARTAR",
                "reasons": data["reasons"]
            })
    
    for mint, data in enriched.items():
        if data["source"] == "pumpportal":
            t = data["token"]
            d = data["dexscreener"]
            report["pumpportal"].append({
                "symbol": t.get("symbol"),
                "mint": mint,
                "solAmount": t.get("solAmount"),
                "marketCapSol": t.get("marketCapSol"),
                "marketCapUsd": d.get("marketCapUsd") if d else None,
                "score": data["score"],
                "nivel": "ALERTA" if data["score"] >= 70 else "WATCH" if data["score"] >= 50 else "DESCARTAR",
                "reasons": data["reasons"]
            })
    
    for cat, tokens in [("alertas", alertas), ("watch", watch), ("descartar", descartar)]:
        for mint, data in tokens.items():
            t = data["token"]
            d = data["dexscreener"]
            report[cat].append({
                "symbol": t.get("symbol") or t.get("name"),
                "mint": mint,
                "source": data["source"],
                "score": data["score"],
                "reasons": data["reasons"]
            })
    
    report_file = f"{OUTPUT_DIR}/shot_final_{timestamp}.json"
    with open(report_file, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\n[YIN] Reporte guardado: {report_file}")
    
    print("\n" + "="*60)
    print("RESUMEN EJECUTIVO")
    print("="*60)
    print(f"Trending únicos (3 ventanas): {len(trending_tokens)}")
    print(f"PumpPortal capturados: {len(pp_tokens)}")
    print(f"PumpPortal filtrados: {len(pp_passed)}")
    print(f"Total enriquecidos: {len(enriched)}")
    print(f"ALERTAS (>=70): {len(alertas)}")
    print(f"WATCH (50-69): {len(watch)}")
    print(f"DESCARTAR (<50): {len(descartar)}")
    
    if alertas:
        print("\n🚨 ALERTAS:")
        for mint, data in alertas.items():
            t = data["token"]
            sym = t.get("symbol") or t.get("name", "?")
            print(f"  {sym} ({mint[:8]}...) | Score {data['score']} | {data['reasons']}")
    
    return report

if __name__ == "__main__":
    main()