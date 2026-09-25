#!/usr/bin/env python3
"""
script_57_pumpportal_filter.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Conectar a PumpPortal WS y filtrar tokens EN TIEMPO REAL.
    Solo guarda tokens que pasan filtros basicos.
    Salida: lista limpia de candidatos instantaneos.
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

# Filtros minimos instantaneos (aplicables en T+0)
MIN_SOL_AMOUNT = 0.5      # Al menos 0.5 SOL en el pool
MIN_INITIAL_BUY = 0.01    # Compra inicial minima
MAX_INITIAL_BUY = 100     # Compra inicial maxima (evitar snipers extremos)
EXCLUDE_NAMES = ["test", "rug", "scam", "honeypot"]


def pasa_filtros(token):
    """Aplica filtros instantaneos. Retorna (bool, razon)."""
    name = str(token.get("name", "")).lower()
    symbol = str(token.get("symbol", "")).lower()

    # Filtro 1: nombre sospechoso
    for bad in EXCLUDE_NAMES:
        if bad in name or bad in symbol:
            return False, f"nombre sospechoso: {bad}"

    # Filtro 2: sol amount minimo
    sol_amount = token.get("solAmount", 0)
    if sol_amount < MIN_SOL_AMOUNT:
        return False, f"solAmount {sol_amount} < {MIN_SOL_AMOUNT}"

    # Filtro 3: initial buy
    initial_buy = token.get("initialBuy", 0)
    if initial_buy < MIN_INITIAL_BUY:
        return False, f"initialBuy {initial_buy} < {MIN_INITIAL_BUY}"
    if initial_buy > MAX_INITIAL_BUY:
        return False, f"initialBuy {initial_buy} > {MAX_INITIAL_BUY}"

    # Filtro 4: uri presente (metadata en IPFS)
    if not token.get("uri"):
        return False, "sin uri (sin metadata)"

    # Filtro 5: pool valido
    if token.get("pool") not in ["pump", "bonk", "raydium"]:
        return False, f"pool invalido: {token.get('pool')}"

    return True, "OK"


async def listen_and_filter(duration_seconds=300):
    """Escucha y filtra por N segundos."""
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
                        print(f"[YIN]   ✓ PASA: {data.get('symbol', '?')} ({data.get('solAmount', 0):.2f} SOL)")
                    else:
                        descartados.append({"token": data, "razon": razon})
                except asyncio.TimeoutError:
                    continue
                except Exception as e:
                    print(f"[YIN]   Error: {e}")
                    break
    except Exception as e:
        return {"error": str(e)[:200]}

    return {
        "capturados": capturados,
        "filtrados": filtrados,
        "descartados": descartados
    }


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] PumpPortal Filter - {ts}")

    if not WS_OK:
        print("[YIN] ERROR: websockets no instalado")
        return

    result = asyncio.run(listen_and_filter(duration_seconds=300))

    if "error" in result:
        print(f"[YIN] ERROR: {result['error']}")
        return

    out = {
        "timestamp": ts,
        "fase": "pumpportal_filtered",
        "total_capturados": len(result["capturados"]),
        "total_pasan": len(result["filtrados"]),
        "total_descartados": len(result["descartados"]),
        "candidatos": result["filtrados"],
        "descartados_muestra": result["descartados"][:20]
    }

    out_path = FILTER_DIR / f"filtered_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[YIN] Guardado: {out_path}")
    print(f"[YIN] Capturados: {out['total_capturados']}")
    print(f"[YIN] Pasan filtros: {out['total_pasan']}")
    print(f"[YIN] Descartados: {out['total_descartados']}")


if __name__ == "__main__":
    main()