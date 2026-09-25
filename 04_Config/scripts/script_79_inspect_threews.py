#!/usr/bin/env python3
"""
script_79_inspect_threews.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Inspecciona la estructura REAL de las respuestas de three.ws
    antes de asumir nombres de campos.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

THREEWS_BASE = "https://three.ws/api/crypto"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
INSPECT_DIR = PROJECT_ROOT / "02_Analisis" / "inspect_threews"
INSPECT_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0"}


def fetch_raw(path, params=None):
    try:
        r = requests.get(f"{THREEWS_BASE}{path}", params=params or {}, headers=HEADERS, timeout=TIMEOUT)
        return {"http_status": r.status_code, "body": r.text[:3000]}
    except Exception as e:
        return {"error": str(e)[:200]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Inspeccion three.ws - {ts}")

    # 1. Launches (estructura completa de un item)
    print("[YIN] Inspeccionando /launches...")
    launches = fetch_raw("/launches", {"limit": 2})
    print(f"[YIN] HTTP {launches.get('http_status')}")
    print(f"[YIN] Body: {launches.get('body', '')[:1000]}")

    # 2. Trending
    print("\n[YIN] Inspeccionando /trending...")
    trending = fetch_raw("/trending")
    print(f"[YIN] HTTP {trending.get('http_status')}")
    print(f"[YIN] Body: {trending.get('body', '')[:1000]}")

    # 3. Token especifico (usar un mint del launch)
    print("\n[YIN] Extrayendo mint del launch para consultar /token...")
    try:
        body = launches.get("body", "{}")
        parsed = json.loads(body) if body.startswith("{") else {}
        launches_list = parsed.get("launches", [])
        if launches_list:
            mint = launches_list[0].get("mint") or launches_list[0].get("address")
            if mint:
                print(f"[YIN] Consultando /token para {mint[:20]}...")
                token = fetch_raw("/token", {"address": mint})
                print(f"[YIN] HTTP {token.get('http_status')}")
                print(f"[YIN] Body: {token.get('body', '')[:1500]}")
    except Exception as e:
        print(f"[YIN] Error extrayendo mint: {e}")

    out = {
        "timestamp": ts,
        "fase": "inspect_threews",
        "launches": launches,
        "trending": trending,
    }

    out_path = INSPECT_DIR / f"inspect_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\n[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()