#!/usr/bin/env python3
"""
script_58_enrich_candidates.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Enriquece los candidatos filtrados de PumpPortal con datos
    de Metaplex (genesis info) y three.ws (trending score).
"""

import json
import glob
import requests
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
FILTER_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "pumpportal_filtered"
ENRICHED_DIR = PROJECT_ROOT / "02_Analisis" / "enriched_candidates"
ENRICHED_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 20


def leer_ultimo_filtrado():
    archivos = sorted(FILTER_DIR.glob("filtered_*.json"), reverse=True)
    if not archivos:
        return None
    with open(archivos[0], "r", encoding="utf-8") as f:
        return json.load(f)


def fetch_metaplex(mint):
    """Consulta Metaplex para info de genesis del token."""
    try:
        r = requests.get(f"https://api.metaplex.com/v1/launches/{mint}", timeout=TIMEOUT)
        if r.status_code == 200:
            return r.json()
        return None
    except Exception:
        return None


def fetch_threews_trending():
    """Obtiene trending de three.ws (indexado por mint)."""
    try:
        r = requests.get("https://three.ws/api/v1/pump/trending", timeout=TIMEOUT)
        if r.status_code == 200:
            data = r.json()
            trending = data.get("tokens", data) if isinstance(data, dict) else data
            return {t.get("mint"): t for t in trending if isinstance(t, dict) and t.get("mint")}
        return {}
    except Exception:
        return {}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Enrich Candidates - {ts}")

    data = leer_ultimo_filtrado()
    if not data:
        print("[YIN] ERROR: No hay datos filtrados")
        return

    candidatos = data.get("candidatos", [])
    print(f"[YIN] Candidatos a enriquecer: {len(candidatos)}")

    # Cargar trending de three.ws
    print("[YIN] Cargando trending three.ws...")
    trending_map = fetch_threews_trending()
    print(f"[YIN] Trending indexados: {len(trending_map)}")

    enriquecidos = []
    for i, cand in enumerate(candidatos, 1):
        mint = cand.get("mint")
        print(f"[YIN] [{i}/{len(candidatos)}] {cand.get('symbol', '?')}...")

        enriched = {
            "mint": mint,
            "symbol": cand.get("symbol"),
            "name": cand.get("name"),
            "sol_amount": cand.get("solAmount"),
            "initial_buy": cand.get("initialBuy"),
            "market_cap_sol": cand.get("marketCapSol"),
            "pool": cand.get("pool"),
            "metaplex": None,
            "threews_trending": trending_map.get(mint)
        }

        # Metaplex check
        if mint:
            enriched["metaplex"] = fetch_metaplex(mint)

        enriquecidos.append(enriched)

    out = {
        "timestamp": ts,
        "fase": "enriched_candidates",
        "total_candidatos": len(enriquecidos),
        "candidatos": enriquecidos
    }

    out_path = ENRICHED_DIR / f"enriched_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[YIN] Guardado: {out_path}")

    # Scoring basico
    print(f"\n[YIN] === CANDIDATOS ENRIQUECIDOS ===")
    for e in enriquecidos:
        tiene_metaplex = "✓" if e.get("metaplex") else "✗"
        en_trending = "✓" if e.get("threews_trending") else "✗"
        print(f"[YIN] {e.get('symbol', '?'):15} | Metaplex {tiene_metaplex} | Trending {en_trending} | SOL {e.get('sol_amount', 0)}")


if __name__ == "__main__":
    main()