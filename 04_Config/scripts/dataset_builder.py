#!/usr/bin/env python3
"""
dataset_builder.py — Datasets públicos y propio (Fase 9: T1, T2, T5). Corre en Actions (datasets_build.yml).

  memechain   MemeChain (Zenodo 18246856, CC-BY-4.0; arXiv 2601.22185): 34.988 memecoins de Ethereum, BSC, Solana y
              Base, snapshot de mediados de octubre de 2024. Se bajan SOLO los CSV (módulos Core, Financial Metadata y
              Digital Presence); los ZIP de HTML y logos no (≈ 1,4 GB, y GitHub rechaza archivos > 100 MB).
              -> 01_Datos_Crudos/datasets/memechain/*.csv + _manifest.json
              -> 02_Analisis/datasets/memechain_index.json: tasas base por chain y por narrativa.
  binance     Velas diarias completas de BTC/ETH/SOL (desde 2017) por la API pública data-api.binance.vision
              (la misma ya verificada desde Actions), paginando de a 1000.
              -> 01_Datos_Crudos/datasets/binance/<SYM>USDT_1d.csv
              -> 02_Analisis/datasets/binance_index.json: cobertura, vol realizada y GARCH(1,1) por activo.
  historical  --backfill: inicia 02_Analisis/datasets/historical_alerts.jsonl con las alertas de _all_alerts.json.

Definiciones del índice MemeChain [método propio; el dataset no trae etiqueta de rug, arXiv 2601.22185 §3.2.3]:
  inactive      = sin precio ni market cap en el snapshot: sin pool de liquidez activo (el paper lo explica así).
  one_day       = dejó de operar dentro de las 24 h de su creación, si el CSV trae columnas de actividad (el paper
                  reporta 5,15%); si no, queda None.
  web/x/tg      = presencia declarada (website_url, X_url, telegram_url).
Uso: python 04_Config/scripts/dataset_builder.py {memechain|binance|historical} [--backfill] [--offline-dir DIR]
"""
import argparse
import csv
import hashlib
import io
import json
import math
import os
import re
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_persist  # noqa: E402

ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
RAW_DIR = ROOT / "01_Datos_Crudos" / "datasets"
OUT_DIR = ROOT / "02_Analisis" / "datasets"
ZENODO_RECORD = "https://zenodo.org/api/records/18246856"
MAX_CSV_BYTES = 90 * 1024 * 1024          # debajo del límite de 100 MB de GitHub
HEADERS = {"User-Agent": "shot-de-mercado-datasets/1.0 (research; repo artificialintelligencestaff-tech/shot-de-mercado)"}
BINANCE = "https://data-api.binance.vision/api/v3/klines"
BINANCE_SYMBOLS = ("BTC", "ETH", "SOL")
NARRATIVES = {   # por palabra en nombre o símbolo (el paper observa el paso de perros a IA y gatos en 2024)
    "canino": r"\b(dog|doge|inu|shib|shiba|puppy|pup|wif|bonk)\b",
    "felino": r"\b(cat|kitty|meow|neko|popcat|mew)\b",
    "ia": r"\b(ai|gpt|agent|bot|neural|agi)\b",
    "rana_pepe": r"\b(pepe|frog|toad)\b",
    "politica": r"\b(trump|maga|biden|kamala|elon|musk|vance)\b",
}


# ---------------------------------------------------------------------------
# MemeChain
# ---------------------------------------------------------------------------

def _col(fieldnames, *patterns):
    """Primer nombre de columna que coincide (sin mayúsculas, ignorando separadores) con algún patrón."""
    norm = {re.sub(r"[^a-z0-9]", "", (f or "").lower()): f for f in fieldnames or []}
    for p in patterns:
        for k, f in norm.items():
            if re.fullmatch(p, k):
                return f
    return None


def _num(x):
    try:
        v = float(str(x).replace(",", "")) if x not in (None, "", "nan", "NaN", "None") else None
    except ValueError:
        return None
    return v if v is not None and math.isfinite(v) else None


def _ts(x):
    if x in (None, ""):
        return None
    s = str(x).strip()
    if re.fullmatch(r"\d{10}(\.\d+)?", s):
        return float(s)
    if re.fullmatch(r"\d{13}", s):
        return float(s) / 1000
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00").replace(" ", "T"))
    except ValueError:
        return None
    return (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).timestamp()


def narrative_of(name, symbol):
    text = f"{name or ''} {symbol or ''}".lower()
    for label, pat in NARRATIVES.items():
        if re.search(pat, text):
            return label
    return "otra"


def merge_rows(tables):
    """Une los CSV de MemeChain por (dirección, chain): cada módulo aporta columnas."""
    merged = {}
    for rows in tables:
        if not rows:
            continue
        fields = list(rows[0].keys())
        a, c = _col(fields, r"tokenaddress", r"contractaddress", r"address"), _col(fields, r"chain", r"blockchain", r"platform", r"network")
        if not a or not c:
            continue
        for r in rows:
            key = (str(r.get(a) or "").strip().lower(), str(r.get(c) or "").strip().lower())
            if key[0]:
                merged.setdefault(key, {}).update({k: v for k, v in r.items() if v not in (None, "")})
                merged[key]["_address"], merged[key]["_chain"] = key
    return list(merged.values())


def _rate(k, n):
    return round(k / n, 4) if n else None


def summarize(tokens):
    fields = set()
    for t in tokens[:500]:
        fields |= set(t)
    fields = sorted(fields)
    c_price = _col(fields, r"priceusd", r"price")
    c_mcap = _col(fields, r"marketcap", r"marketcapusd", r"mcap")
    c_deploy = _col(fields, r"deploydate", r"creationdate", r"createdat", r"deploytime")
    c_last = _col(fields, r"last(trade|tx|transaction|activity|swap)(date|time|timestamp)?", r"lasttradeat")
    c_web, c_x = _col(fields, r"websiteurl", r"website"), _col(fields, r"xurl", r"twitterurl", r"twitter", r"x")
    c_tg = _col(fields, r"telegramurl", r"telegram")
    c_name, c_sym = _col(fields, r"tokenname", r"name"), _col(fields, r"symbol", r"ticker")

    def stats(group):
        n = len(group)
        priced = [t for t in group if _num(t.get(c_price)) or _num(t.get(c_mcap))]
        one_day = None
        if c_deploy and c_last:
            spans = [(_ts(t.get(c_last)) or 0) - (_ts(t.get(c_deploy)) or 0) for t in group
                     if _ts(t.get(c_deploy)) and _ts(t.get(c_last))]
            one_day = {"n_with_dates": len(spans), "rate": _rate(sum(1 for s in spans if s < 86400), len(spans))}
        mcaps = sorted(v for v in (_num(t.get(c_mcap)) for t in group) if v)
        q = (lambda p: round(mcaps[min(len(mcaps) - 1, int(p * len(mcaps)))], 2)) if mcaps else (lambda p: None)
        inactive = n - len(priced)
        by_bucket = {}
        for label, lo, hi in (("< $10K", 0, 1e4), ("$10K–$100K", 1e4, 1e5), ("$100K–$1M", 1e5, 1e6),
                              ("$1M–$10M", 1e6, 1e7), ("≥ $10M", 1e7, float("inf"))):
            by_bucket[label] = sum(1 for m in mcaps if lo <= m < hi)
        return {"n": n, "inactive": inactive, "inactive_rate": _rate(inactive, n), "one_day": one_day,
                "web_rate": _rate(sum(1 for t in group if t.get(c_web)), n) if c_web else None,
                "x_rate": _rate(sum(1 for t in group if t.get(c_x)), n) if c_x else None,
                "telegram_rate": _rate(sum(1 for t in group if t.get(c_tg)), n) if c_tg else None,
                "mcap_quantiles": {"p25": q(0.25), "p50": q(0.5), "p75": q(0.75), "p90": q(0.9)},
                "mcap_buckets": by_bucket}

    by_chain, by_narr, cross = {}, {}, {}
    for t in tokens:
        ch = t.get("_chain") or "?"
        nar = narrative_of(t.get(c_name), t.get(c_sym))
        by_chain.setdefault(ch, []).append(t)
        by_narr.setdefault(nar, []).append(t)
        cross.setdefault(ch, {}).setdefault(nar, []).append(t)
    return {"columns_detected": {"price": c_price, "market_cap": c_mcap, "deploy": c_deploy, "last_activity": c_last,
                                 "website": c_web, "x": c_x, "telegram": c_tg, "name": c_name, "symbol": c_sym},
            "all": stats(tokens),
            "by_chain": {k: stats(v) for k, v in sorted(by_chain.items())},
            "by_narrative": {k: stats(v) for k, v in sorted(by_narr.items())},
            "chain_x_narrative": {ch: {nar: {"n": len(v), "inactive_rate": _rate(len(v) - sum(
                1 for t in v if _num(t.get(c_price)) or _num(t.get(c_mcap))), len(v))} for nar, v in sorted(d.items())}
                for ch, d in sorted(cross.items())}}


def read_csv_bytes(data):
    text = data.decode("utf-8-sig", "replace")
    return list(csv.DictReader(io.StringIO(text)))


def build_memechain(session=None, offline_dir=None, raw_dir=None, out_dir=None):
    raw_dir = Path(raw_dir or RAW_DIR / "memechain")
    out_dir = Path(out_dir or OUT_DIR)
    manifest = {"record": ZENODO_RECORD, "license": "CC-BY-4.0",
                "citation": "Mongardini & Mei (2026), MemeChain, Zenodo 18246856, arXiv 2601.22185",
                "downloaded_at": lib_persist.now_iso(), "files": [], "skipped": []}
    tables = []
    if offline_dir:
        for p in sorted(Path(offline_dir).glob("*.csv")):
            tables.append(read_csv_bytes(p.read_bytes()))
            manifest["files"].append({"key": p.name, "source": "offline"})
    else:
        session = session or requests.Session()
        rec = session.get(ZENODO_RECORD, headers=HEADERS, timeout=60)
        rec.raise_for_status()
        meta = rec.json()
        manifest["title"] = (meta.get("metadata") or {}).get("title")
        for f in meta.get("files") or []:
            key = f.get("key") or ""
            size = f.get("size") or 0
            link = (f.get("links") or {}).get("self") or (f.get("links") or {}).get("content")
            if not key.lower().endswith(".csv") or size > MAX_CSV_BYTES or not link:
                manifest["skipped"].append({"key": key, "size": size, "reason": "no es CSV o supera 90 MB"})
                continue
            r = session.get(link, headers=HEADERS, timeout=300)
            r.raise_for_status()
            raw_dir.mkdir(parents=True, exist_ok=True)
            (raw_dir / Path(key).name).write_bytes(r.content)
            manifest["files"].append({"key": key, "size": len(r.content), "sha256": hashlib.sha256(r.content).hexdigest(),
                                      "checksum_zenodo": f.get("checksum")})
            tables.append(read_csv_bytes(r.content))
    tokens = merge_rows(tables)
    index = {"dataset": "MemeChain", "license": "CC-BY-4.0", "source": ZENODO_RECORD,
             "snapshot": "mediados de octubre de 2024 (arXiv 2601.22185 §3.2)", "built_at": lib_persist.now_iso(),
             "n_tokens": len(tokens), "definitions": {
                 "inactive": "sin precio ni market cap en el snapshot (sin pool de liquidez activo)",
                 "one_day": "dejó de operar dentro de las 24 h de su creación (si hay columnas de actividad)"},
             **summarize(tokens)}
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "memechain_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    written = [out_dir / "memechain_index.json"]
    if manifest["files"] and not offline_dir:
        raw_dir.mkdir(parents=True, exist_ok=True)
        (raw_dir / "_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
        written += [raw_dir / "_manifest.json"] + [raw_dir / Path(f["key"]).name for f in manifest["files"]]
    lib_persist.log_operation("dataset_memechain", "dataset_builder.py", written, tokens=len(tokens),
                              files=len(manifest["files"]), skipped=len(manifest["skipped"]))
    return index


# ---------------------------------------------------------------------------
# Binance (velas diarias completas)
# ---------------------------------------------------------------------------

def fetch_klines(session, sym, start_ms=1500000000000, sleep=time.sleep):
    rows, start = [], start_ms
    while True:
        r = session.get(BINANCE, params={"symbol": f"{sym}USDT", "interval": "1d", "startTime": start, "limit": 1000},
                        headers=HEADERS, timeout=30)
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        rows += [[int(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4]), float(k[5]), int(k[6])] for k in batch]
        if len(batch) < 1000:
            break
        start = int(batch[-1][0]) + 86_400_000
        sleep(0.5)
    return rows


def build_binance(session=None, raw_dir=None, out_dir=None, sleep=time.sleep, now_ms=None):
    import lib_scoring_multichain as lsm
    session = session or requests.Session()
    raw_dir, out_dir = Path(raw_dir or RAW_DIR / "binance"), Path(out_dir or OUT_DIR)
    now_ms = now_ms or int(time.time() * 1000)
    index, written = {"source": BINANCE, "built_at": lib_persist.now_iso(), "assets": {}}, []
    for sym in BINANCE_SYMBOLS:
        rows = lsm.closed_klines(fetch_klines(session, sym, sleep=sleep), now_ms)
        raw_dir.mkdir(parents=True, exist_ok=True)
        path = raw_dir / f"{sym}USDT_1d.csv"
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["open_time_ms", "open", "high", "low", "close", "volume", "close_time_ms"])
            w.writerows(rows)
        written.append(path)
        rets = lsm.log_returns([r[4] for r in rows])
        g = lsm.garch11(rets[-1500:]) if len(rets) >= 100 else None
        index["assets"][sym] = {
            "rows": len(rows),
            "first_day": datetime.fromtimestamp(rows[0][0] / 1000, timezone.utc).date().isoformat() if rows else None,
            "last_day": datetime.fromtimestamp(rows[-1][0] / 1000, timezone.utc).date().isoformat() if rows else None,
            "vol_daily_all": round(statistics.pstdev(rets), 6) if len(rets) > 1 else None,
            "vol_daily_365": round(statistics.pstdev(rets[-365:]), 6) if len(rets) > 1 else None,
            "days_abs_ret_ge_20pct": sum(1 for x in rets if abs(math.exp(x) - 1) >= 0.20),
            "garch11_last_1500": {k: round(v, 6) for k, v in g.items()} if g else None}
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "binance_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    written.append(out_dir / "binance_index.json")
    lib_persist.log_operation("dataset_binance", "dataset_builder.py", written,
                              **{f"rows_{s}": a["rows"] for s, a in index["assets"].items()})
    return index


# ---------------------------------------------------------------------------
# Dataset propio: backfill
# ---------------------------------------------------------------------------

def backfill_historical(alerts_file=None):
    """Inicia historical_alerts.jsonl con las alertas ya registradas (una vez; no duplica claves+timestamp)."""
    alerts_file = Path(alerts_file or ROOT / "02_Analisis" / "alerts" / "_all_alerts.json")
    alerts = json.loads(alerts_file.read_text(encoding="utf-8"))
    seen = {(r.get("key"), r.get("timestamp")) for r in lib_persist.read_jsonl(lib_persist.historical_path())
            if r.get("type") == "alert"}
    added = 0
    for a in alerts:
        if not isinstance(a, dict) or ((a.get("asset_key") or a.get("mint")), a.get("timestamp")) in seen:
            continue
        # El registro individual alert_<mint>_<ts>.json trae los motivos, la versión del scorer y los componentes.
        detail = {}
        safe = re.sub(r"[^A-Za-z0-9]+", "_", str(a.get("asset_key") or "")) if a.get("multichain") else a.get("mint")
        for name in (f"alert_{a.get('mint')}_{a.get('timestamp')}.json", f"alert_{safe}_{a.get('timestamp')}.json"):
            try:
                detail = json.loads((alerts_file.parent / name).read_text(encoding="utf-8"))
                break
            except (OSError, ValueError):
                continue
        merged = dict(a, scoring_version=a.get("scoring_version") or detail.get("scoring_version"),
                      group=a.get("group") or detail.get("group"), chain=a.get("chain") or detail.get("chain"))
        lib_persist.record_alert(merged, components=detail.get("components"),
                                 reasons=a.get("reasons") or detail.get("reasons"), source="backfill:_all_alerts.json")
        added += 1
    lib_persist.log_operation("dataset_historical_backfill", "dataset_builder.py", [lib_persist.historical_path()],
                              added=added, total_alerts=len(alerts))
    return added


def main(argv=None):
    ap = argparse.ArgumentParser(description="Datasets públicos y propio (Fase 9).")
    ap.add_argument("what", choices=["memechain", "binance", "historical"])
    ap.add_argument("--offline-dir", help="memechain: CSV ya descargados (sin red)")
    ap.add_argument("--backfill", action="store_true", help="historical: cargar las alertas existentes")
    args = ap.parse_args(argv)
    if args.what == "memechain":
        idx = build_memechain(offline_dir=args.offline_dir)
        print(f"[DS] MemeChain: {idx['n_tokens']} tokens · por chain: "
              f"{ {k: v['n'] for k, v in idx['by_chain'].items()} } · inactivos: {idx['all']['inactive_rate']}")
    elif args.what == "binance":
        idx = build_binance()
        print(f"[DS] Binance: { {k: (v['rows'], v['first_day']) for k, v in idx['assets'].items()} }")
    else:
        print(f"[DS] historical_alerts.jsonl: +{backfill_historical() if args.backfill else 0} alertas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
