#!/usr/bin/env python3
"""
script_43_historical_cases.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Estudiar casos historicos de pumps y dumps documentados.
    Extrae patrones para calibrar la formula de scoring.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

DEXSCREENER_URL = "https://api.dexscreener.com/latest/dex/tokens"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
CASOS_DIR = PROJECT_ROOT / "02_Analisis" / "casos_historicos"
CASOS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 20

# Casos historicos documentados
CASOS = [
    {
        "name": "SIREN",
        "address": "0x...",  # Direccion real pendiente de verificar
        "red": "ethereum",
        "periodo": "Marzo 2026",
        "patron": "Un solo entity controlaba ~50% del supply. MCap subio de $40M a $2B.",
        "resultado": "Crash -50%+ tras advertencia de BubbleMaps",
        "leccion": "Concentracion extrema de supply es senal de alerta"
    },
    {
        "name": "RAVE",
        "address": "0x...",
        "red": "ethereum",
        "periodo": "Abril 2026",
        "patron": "MCap cayo de $1.52B a $320M. Precio de $2.1 a $0.44.",
        "resultado": "Dump masivo tras advertencias de exchanges",
        "leccion": "Los exchanges emiten advertencias antes del colapso"
    },
    {
        "name": "ARGUS",
        "address": "pendiente",
        "red": "solana",
        "periodo": "Septiembre 2026",
        "patron": "+754.7% en 24h. Sin ficha en CoinGecko.",
        "resultado": "Pendiente de verificar",
        "leccion": "Los pumps extremos pueden ocurrir en tokens sin historial"
    },
    {
        "name": "CATWIFOUT",
        "address": "5cT9mMKGwJP42xdgwSxu9zsYCScCXqwpq49GfQoXpump",
        "red": "solana",
        "periodo": "Septiembre 2026",
        "patron": "+366% en 24h. Liquidez -57% en 6h.",
        "resultado": "Fase de distribucion en curso",
        "leccion": "Liquidez cayendo >30% en <6h = inicio de dump"
    }
]


def fetch_dex(address):
    """Consulta Dexscreener para un token."""
    if not address or "pendiente" in address or "..." in address:
        return {"error": "direccion no disponible"}
    try:
        r = requests.get(f"{DEXSCREENER_URL}/{address}", timeout=TIMEOUT)
        if r.status_code != 200:
            return {"error": f"HTTP {r.status_code}"}
        data = r.json()
        pairs = data.get("pairs", [])
        if not pairs:
            return {"error": "no pairs"}
        best = max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0))
        return {
            "priceUsd": best.get("priceUsd"),
            "liquidity_usd": best.get("liquidity", {}).get("usd"),
            "volume_24h": best.get("volume", {}).get("h24"),
            "fdv": best.get("fdv"),
            "marketCap": best.get("marketCap"),
            "priceChange": best.get("priceChange"),
            "txns": best.get("txns"),
            "pairCreatedAt": best.get("pairCreatedAt")
        }
    except Exception as e:
        return {"error": str(e)[:150]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Analisis casos historicos - {ts}")

    resultados = []
    for caso in CASOS:
        print(f"[YIN] {caso['name']}...")
        data = fetch_dex(caso["address"])
        entry = {**caso, "datos_actuales": data}
        resultados.append(entry)

    out = {
        "timestamp": ts,
        "fase": "analisis_casos_historicos",
        "total_casos": len(resultados),
        "casos": resultados,
        "patrones_identificados": [
            "Concentracion de supply >50% precede crashes",
            "Advertencias de BubbleMaps/ZachXBT preceden dumps",
            "Liquidez cayendo >30% en <6h = senal de distribucion",
            "Pumps extremos (+500%+) ocurren en tokens sin historial",
            "Narrativas con producto real sobreviven correcciones"
        ]
    }

    out_path = CASOS_DIR / f"casos_historicos_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print(f"[YIN] Total casos: {len(resultados)}")

    # Imprimir resumen
    print(f"\n[YIN] === CASOS HISTORICOS ===")
    for c in resultados:
        print(f"[YIN] {c['name']:12} | {c['periodo']:20} | {c['leccion'][:60]}")


if __name__ == "__main__":
    main()