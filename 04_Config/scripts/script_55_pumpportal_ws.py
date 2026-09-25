#!/usr/bin/env python3
"""
script_55_pumpportal_ws.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Conectar a PumpPortal WebSocket para detectar nuevos tokens en tiempo real.
    Fuente: https://pumpportal.fun/data-api/real-time
    Gratis, sin API key.
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
WS_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "pre_launch" / "pumpportal"
WS_DIR.mkdir(parents=True, exist_ok=True)

WS_URL = "wss://pumpportal.fun/api/data"


async def listen_for_tokens(duration_seconds=60):
    """Escucha eventos de nuevos tokens por X segundos."""
    tokens = []
    try:
        async with websockets.connect(WS_URL) as ws:
            # Suscribirse a nuevos tokens
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
            print(f"[YIN] Suscrito a nuevos tokens. Escuchando {duration_seconds}s...")

            start = asyncio.get_event_loop().time()
            while asyncio.get_event_loop().time() - start < duration_seconds:
                try:
                    message = await asyncio.wait_for(ws.recv(), timeout=5)
                    data = json.loads(message)
                    tokens.append(data)
                    print(f"[YIN]   Nuevo token: {data.get('symbol', '?')} ({data.get('mint', '?')[:20]}...)")
                except asyncio.TimeoutError:
                    continue
                except Exception as e:
                    print(f"[YIN]   Error en mensaje: {e}")
                    break
    except Exception as e:
        return {"error": str(e)[:200], "tokens": []}
    return {"tokens": tokens}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] PumpPortal WebSocket - {ts}")

    if not WS_OK:
        print("[YIN] ERROR: websockets no instalado. Ejecutar: python -m pip install websockets")
        return

    result = asyncio.run(listen_for_tokens(duration_seconds=60))

    out = {
        "timestamp": ts,
        "fase": "pumpportal_ws",
        "total_tokens": len(result.get("tokens", [])),
        "tokens": result.get("tokens", []),
        "error": result.get("error")
    }

    out_path = WS_DIR / f"pumpportal_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[YIN] Guardado: {out_path}")
    print(f"[YIN] Total tokens capturados: {len(out['tokens'])}")


if __name__ == "__main__":
    main()