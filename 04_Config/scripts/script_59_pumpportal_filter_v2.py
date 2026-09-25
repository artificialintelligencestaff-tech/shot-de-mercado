#!/usr/bin/env python3
"""
script_59_pumpportal_filter_v2.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Version 2 corregida. Elimina filtro de initialBuy (unidad incorrecta).
    Usa solAmount + marketCapSol como metricas reales.
"""

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

try:
    import websockets
    WS_OK = True
except ImportError:
    WS_OK = False

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
FILTER_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "pumpportal_filtered"
FILTER_DIR.mkdir(parents=True, exist_ok=True)

WS_URL = "wss://pumpportal.fun/api/data"

# FILTROS CORREGIDOS (basados en solAmount y marketCapSol)
MIN_SOL_AMOUNT = 0.5        # Minimo SOL en el pool
MIN_MARKET_CAP_SOL = 10     # Minimo market cap en SOL (~$1,500-2,000)
MAX_MARKET_CAP_SOL = 5000   # Maximo (evitar tokens ya pumpeados)

EXCLUDE_NAMES = ["test", "rug", "scam", "honeypot"]


def pasa_filtros(token):
    name = str(token.get("name", "")).lower()
    symbol = str(token.get("symbol", "")).lower()

    for bad in EXCLUDE_NAMES:
        if bad in name or bad in symbol:
            return False, f"nombre sospechoso: {bad}"

    sol_amount = token.get("solAmount", 0)
    if sol_amount < MIN_SOL_AMOUNT:
        return False, f"solAmount {sol_amount:.3f} < {MIN_SOL_AMOUNT}"

    mcap_sol = token.get("marketCapSol", 0)
    if mcap_sol < MIN_MARKET_CAP_SOL:
        return False, f"mcapSol {mcap_sol:.1f} < {MIN_MARKET_CAP_SOL}"
    if mcap_sol > MAX_MARKET_CAP_SOL:
        return False, f"mcapSol {mcap_sol:.1f} > {MAX_MARKET_CAP_SOL} (ya pumpeado)"

    if not token.get("uri"):
        return False, "sin uri (sin metadata)"

    if token.get("pool") not in ["pump", "bonk", "raydium", "pump-amm"]:
        return False, f"pool invalido: {token.get('pool')}"

    return True, "OK"


async def listen_and_filter(duration_seconds=300):
    capturados = []
    filtrados = []
    descartados = []

    try:
        async with websockets.connect(WS_URL) as ws:
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
            print(f"[YIN] Suscrito. Filtrando por {duration_seconds}s...")

            start = asyncio.get_event_loop().time()
            while asyncio.get_event_loop().time() - start < duration_seconds:
                try:
                    message = await asyncio.wait_for(ws.recv(), timeout=5)
                    data = json.loads(message)
                    capturados.append(data)

                    pasa, razon = pasa_filtros(data)
                    if pasa:
                        filtrados.append(data)
                        print(f"[YIN]   ✓ PASA: {data.get('symbol', '?')} | {data.get('solAmount', 0):.2f} SOL | MCap {data.get('marketCapSol', 0):.1f} SOL")
                    else:
                        descartados.append({"token": data, "razon": razon})
                except asyncio.TimeoutError:
                    continue
                except Exception as e:
                    print(f"[YIN]   Error: {e}")
                    break
    except Exception as e:
        return {"error": str(e)[:200]}

    return {"capturados": capturados, "filtrados": filtrados, "descartados": descartados}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] PumpPortal Filter v2 - {ts}")

    if not WS_OK:
        print("[YIN] ERROR: websockets no instalado")
        return

    result = asyncio.run(listen_and_filter(duration_seconds=300))

    if "error" in result:
        print(f"[YIN] ERROR: {result['error']}")
        return

    out = {
        "timestamp": ts,
        "fase": "pumpportal_filtered_v2",
        "total_capturados": len(result["capturados"]),
        "total_pasan": len(result["filtrados"]),
        "total_descartados": len(result["descartados"]),
        "candidatos": result["filtrados"],
        "descartados_muestra": result["descartados"][:20]
    }

    out_path = FILTER_DIR / f"filtered_v2_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[YIN] Capturados: {out['total_capturados']}")
    print(f"[YIN] Pasan filtros: {out['total_pasan']}")
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()