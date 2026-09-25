#!/usr/bin/env python3
"""
script_71b_madeonsol_kol_feed.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Version corregida. Usa el endpoint /kol/feed con parametros correctos.
    Documentacion: https://madeonsol.com/api-docs
"""

import json
import os
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path(r"D:\Proyecto Shot de Mercado\04_Config\.env")
load_dotenv(ENV_PATH)

MADEONSOL_KEY = os.getenv("MADEONSOL_API_KEY", "")
MADEONSOL_BASE = "https://madeonsol.com/api/v1"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
KOL_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "kol_tracking"
KOL_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0", "Authorization": f"Bearer {MADEONSOL_KEY}"}


def fetch_kol_feed(limit=50, action=None, min_sol=None):
    """GET /kol/feed - Real-time KOL trade feed."""
    params = {"limit": limit}
    if action:
        params["action"] = action
    if min_sol:
        params["min_sol"] = min_sol
    try:
        r = requests.get(f"{MADEONSOL_BASE}/kol/feed", params=params, headers=HEADERS, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else {"error": f"HTTP {r.status_code}", "preview": r.text[:300]}
    except Exception as e:
        return {"error": str(e)[:150]}


def fetch_kol_leaderboard(period="7d"):
    """GET /kol/leaderboard - KOL PnL leaderboard."""
    try:
        r = requests.get(f"{MADEONSOL_BASE}/kol/leaderboard", params={"period": period}, headers=HEADERS, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else {"error": f"HTTP {r.status_code}"}
    except Exception as e:
        return {"error": str(e)[:150]}


def fetch_deployer_alerts(limit=10):
    """GET /deployer-hunter/alerts - Elite deployer launches."""
    try:
        r = requests.get(f"{MADEONSOL_BASE}/deployer-hunter/alerts", params={"limit": limit}, headers=HEADERS, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else {"error": f"HTTP {r.status_code}"}
    except Exception as e:
        return {"error": str(e)[:150]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] MadeOnSol KOL Feed (corregido) - {ts}")
    print(f"[YIN] API key: {'SI' if MADEONSOL_KEY else 'NO'}")

    if not MADEONSOL_KEY:
        print("[YIN] ERROR: MADEONSOL_API_KEY no configurada")
        return

    resultados = {}

    # 1. KOL Feed (solo buys, tokens <60min)
    print("[YIN] Consultando KOL feed (buys, tokens <60min)...")
    feed = fetch_kol_feed(limit=50, action="buy", min_sol=0.5)
    resultados["kol_feed"] = feed
    if "error" not in feed:
        trades = feed.get("trades", [])
        print(f"[YIN]   KOL trades: {len(trades)}")
        for t in trades[:5]:
            print(f"[YIN]     {t.get('kol_name')} compro {t.get('token_symbol')} | {t.get('sol_amount', 0):.2f} SOL")

    # 2. KOL Leaderboard
    print("[YIN] Consultando leaderboard (7d)...")
    lb = fetch_kol_leaderboard(period="7d")
    resultados["leaderboard"] = lb
    if "error" not in lb:
        board = lb.get("leaderboard", [])
        print(f"[YIN]   KOLs en ranking: {len(board)}")

    # 3. Deployer Alerts
    print("[YIN] Consultando deployer alerts...")
    da = fetch_deployer_alerts(limit=10)
    resultados["deployer_alerts"] = da
    if "error" not in da:
        alerts = da.get("alerts", [])
        print(f"[YIN]   Deployer alerts: {len(alerts)}")

    out = {"timestamp": ts, "fase": "madeonsol_corregido", "resultados": resultados}
    out_path = KOL_DIR / f"kol_corregido_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()