#!/usr/bin/env python3
"""
latency_analysis.py — Latencia de detección: inicio del pump vs. emisión (Fase 10, T1). Solo lectura + un JSON.

Para las últimas N alertas de _all_alerts.json (por defecto 20):
  · Parte estructural (sin red): momento de emisión, detected_at de script_82, edad del par al detectar y al emitir,
    demora detección→emisión, cuánto se había movido ya el precio en el snapshot que se usó para emitir.
  · Parte medida (con red, desde Actions): velas de 1 minuto alrededor de la alerta. On-chain: GeckoTerminal
    (pool = dexscreener.pairAddress del alert_*.json). CEX: Binance data-api ({SYMBOL}USDT).
    Inicio del pump = primera vela cuyo cierre supera en >= 5 % al cierre de 5 minutos antes (si el pool tiene menos
    de 5 minutos, la referencia es la apertura de la primera vela: el pump arranca con el lanzamiento).
    Gap = emisión − inicio del pump (minutos; negativo = la alerta llegó antes del pump).
  · Cadencia real del cron de pipeline_t0 (API de Actions con GITHUB_TOKEN, o --runs-file): retraso de arranque
    sobre la grilla */20 y duración de la corrida.

Salida: 02_Analisis/diagnostics/latency_analysis.json (+ bitácora lib_persist "latency_analysis").

Uso: python 04_Config/scripts/latency_analysis.py [--n 20] [--offline] [--runs-file runs.json] [--root DIR]
"""
import argparse
import json
import os
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
VERSION = "lat-1.0"
PUMP_THRESHOLD = 0.05        # +5 %
PUMP_LOOKBACK_MIN = 5        # en 5 minutos
WINDOW_BEFORE_MIN = 360      # se busca el inicio del pump desde 6 h antes de la emisión (o desde el lanzamiento)
WINDOW_AFTER_MIN = 120       # ... hasta 2 h después (para ver si la alerta se anticipó)
CRON_EVERY_MIN = 20          # pipeline_t0: */20
FAST_GAP_MIN = 5             # métrica de éxito: alerta dentro de los primeros 5 min del pump
GT_OHLCV = ("https://api.geckoterminal.com/api/v2/networks/{net}/pools/{pool}/ohlcv/minute"
            "?aggregate=1&before_timestamp={before}&limit=1000&currency=usd")
BINANCE_KLINES = ("https://data-api.binance.vision/api/v3/klines?symbol={symbol}USDT&interval=1m"
                  "&startTime={start}&endTime={end}&limit=1000")
GT_NETWORKS = {"solana": "solana", "base": "base", "ethereum": "eth", "arbitrum": "arbitrum", "optimism": "optimism",
               "blast": "blast", "bsc": "bsc"}
ACTIONS_RUNS = "https://api.github.com/repos/{repo}/actions/workflows/pipeline_t0.yml/runs?event=schedule&per_page=100"


# ---------------------------------------------------------------------------
# Funciones puras
# ---------------------------------------------------------------------------

def parse_alert_ts(value):
    """'2026-10-01_171401' (UTC, formato de script_97) -> epoch s."""
    try:
        return datetime.strptime(value, "%Y-%m-%d_%H%M%S").replace(tzinfo=timezone.utc).timestamp()
    except (TypeError, ValueError):
        return None


def parse_iso(value):
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.timestamp()


def iso(epoch):
    return datetime.fromtimestamp(epoch, timezone.utc).isoformat(timespec="seconds") if epoch is not None else None


def _r(x, nd=1):
    return round(x, nd) if isinstance(x, (int, float)) else None


def last_alerts(all_alerts, n=20):
    """Últimas n alertas emitidas o registradas (todas menos las descartadas), en orden de emisión."""
    rows = [a for a in all_alerts if isinstance(a, dict) and parse_alert_ts(a.get("timestamp")) is not None
            and not str(a.get("status", "")).startswith("DESCARTAR")]
    rows.sort(key=lambda a: parse_alert_ts(a["timestamp"]))
    return rows[-n:]


def detail_name(alert):
    mint = str(alert.get("mint") or "").replace(":", "_")
    return f"alert_{mint}_{alert.get('timestamp')}.json"


def structural_row(alert, detail):
    """Lo que se sabe sin red: tiempos del pipeline y movimiento ya hecho en el snapshot usado para emitir."""
    emitted = parse_alert_ts(alert.get("timestamp"))
    detail = detail or {}
    dx = detail.get("dexscreener") or {}
    detected = parse_iso(detail.get("detected_at"))
    created = dx.get("pairCreatedAt")
    created = created / 1000 if isinstance(created, (int, float)) and created > 0 else None
    row = {
        "symbol": alert.get("symbol"), "mint": alert.get("mint"), "status": alert.get("status"),
        "route": "cex" if alert.get("status") == "active_tracking_cex" else "onchain",
        "group": alert.get("group") or detail.get("group") or ("a" if not alert.get("multichain") else None),
        "score": alert.get("score"), "emitted_at": iso(emitted), "detected_at": iso(detected),
        "pair_created_at": iso(created),
        "detect_to_emit_min": _r((emitted - detected) / 60) if emitted and detected else None,
        "pair_age_at_detect_min": _r((detected - created) / 60) if detected and created else None,
        "pair_age_at_emit_min": _r((emitted - created) / 60) if emitted and created else None,
        "price_change_at_snapshot": {k: dx.get(src) for k, src in
                                     (("m5", "priceChange_m5"), ("h1", "priceChange_h1"), ("h24", "priceChange24h"))
                                     if dx.get(src) is not None},
        "pool": dx.get("pairAddress"), "chain": detail.get("chain") or alert.get("chain") or "solana",
    }
    # Cota sin velas: par de < 60 min con h1 >= +5 % en el snapshot de detección -> el pump arrancó entre la creación
    # del par y la detección, así que el gap está entre (emisión − detección) y (emisión − creación).
    h1 = dx.get("priceChange_h1")
    if (isinstance(h1, (int, float)) and h1 >= PUMP_THRESHOLD * 100 and row["pair_age_at_detect_min"] is not None
            and row["pair_age_at_detect_min"] <= 60 and row["detect_to_emit_min"] is not None):
        row["gap_bounds_min"] = [row["detect_to_emit_min"], row["pair_age_at_emit_min"]]
    return row


def pump_start(candles, threshold=PUMP_THRESHOLD, lookback_min=PUMP_LOOKBACK_MIN, t_from=None, t_to=None):
    """candles: [(ts_s, open, close)] de 1 minuto en orden ascendente (puede haber huecos: GeckoTerminal omite los
    minutos sin trades). Devuelve (ts_inicio, cambio, desde_lanzamiento) del primer minuto con
    close / close_ref − 1 >= threshold, donde close_ref es el último cierre a >= lookback_min minutos antes.
    Sin vela de referencia (serie que arranca con el pool): referencia = apertura de la primera vela."""
    candles = sorted((c for c in candles if c and c[2]), key=lambda c: c[0])
    if not candles:
        return None
    first_ts, first_open = candles[0][0], candles[0][1] or candles[0][2]
    j = -1
    for i, (ts, _o, close) in enumerate(candles):
        while j + 1 < i and candles[j + 1][0] <= ts - lookback_min * 60:
            j += 1
        if t_from is not None and ts < t_from:
            continue
        if t_to is not None and ts > t_to:
            break
        if j >= 0:
            ref, from_launch = candles[j][2], False
        elif ts - first_ts < lookback_min * 60:
            ref, from_launch = first_open, True
        else:
            continue
        if ref and close / ref - 1 >= threshold:
            return ts, close / ref - 1, from_launch
    return None


def price_at(candles, ts):
    """Cierre de la última vela con inicio <= ts."""
    best = None
    for c in sorted(candles, key=lambda c: c[0]):
        if c[0] <= ts:
            best = c[2]
        else:
            break
    return best


def measured_row(row, candles, emitted):
    if not candles:
        return dict(row, measured=False, reason="sin velas de 1 min")
    created = parse_iso(row.get("pair_created_at"))
    t_from = max(emitted - WINDOW_BEFORE_MIN * 60, created or 0)
    hit = pump_start(candles, t_from=t_from, t_to=emitted + WINDOW_AFTER_MIN * 60)
    out = dict(row, measured=True, candles=len(candles))
    if not hit:
        out.update(pump_start_at=None, gap_min=None, reason="sin +5 % en 5 min en la ventana")
        return out
    ts, change, from_launch = hit
    p0, pe = price_at(candles, ts), price_at(candles, emitted)
    out.update(pump_start_at=iso(ts), pump_start_change=round(change, 4), pump_from_launch=from_launch,
               gap_min=round((emitted - ts) / 60, 1),
               move_since_pump_start_at_emit=round(pe / p0 - 1, 4) if p0 and pe else None)
    return out


def summarize_gaps(rows):
    gaps = [r["gap_min"] for r in rows if r.get("gap_min") is not None]
    if not gaps:
        return {"n_measured": 0}
    return {"n_measured": len(gaps), "gap_mean_min": round(statistics.mean(gaps), 1),
            "gap_median_min": round(statistics.median(gaps), 1), "gap_max_min": max(gaps), "gap_min_min": min(gaps),
            "within_5min_pct": round(100 * sum(0 <= g <= FAST_GAP_MIN for g in gaps) / len(gaps), 1),
            "anticipated_pct": round(100 * sum(g < 0 for g in gaps) / len(gaps), 1)}


def summarize_structural(rows):
    def stats(key):
        vals = [r[key] for r in rows if isinstance(r.get(key), (int, float))]
        if not vals:
            return None
        return {"n": len(vals), "mean": round(statistics.mean(vals), 1), "median": round(statistics.median(vals), 1),
                "min": min(vals), "max": max(vals)}
    moved = [r["symbol"] for r in rows if any(isinstance(v, (int, float)) and v >= 100
                                               for v in (r.get("price_change_at_snapshot") or {}).values())]
    bounds = [r["gap_bounds_min"] for r in rows if r.get("gap_bounds_min")]
    gap_bounds = None
    if bounds:
        gap_bounds = {"n": len(bounds), "lower_mean_min": round(statistics.mean(b[0] for b in bounds), 1),
                      "upper_mean_min": round(statistics.mean(b[1] for b in bounds), 1),
                      "symbols": [r["symbol"] for r in rows if r.get("gap_bounds_min")]}
    return {"gap_bounds_from_snapshot": gap_bounds,
            "detect_to_emit_min": stats("detect_to_emit_min"),
            "pair_age_at_detect_min": stats("pair_age_at_detect_min"),
            "pair_age_at_emit_min": stats("pair_age_at_emit_min"),
            "already_moved_100pct_at_snapshot": moved}


def cron_drift(runs, every_min=CRON_EVERY_MIN):
    """Retraso de arranque de cada corrida programada respecto de su tick de la grilla (piso a every_min) y
    duración (updated_at − run_started_at)."""
    delays, durations = [], []
    for r in runs or []:
        if r.get("event", "schedule") != "schedule":
            continue
        start = parse_iso(r.get("run_started_at") or r.get("created_at"))
        end = parse_iso(r.get("updated_at"))
        if start is None:
            continue
        tick = start - (start % (every_min * 60))
        delays.append((start - tick) / 60)
        if end and end > start:
            durations.append((end - start) / 60)
    if not delays:
        return {"n": 0}
    return {"n": len(delays), "start_delay_mean_min": round(statistics.mean(delays), 1),
            "start_delay_median_min": round(statistics.median(delays), 1),
            "start_delay_max_min": round(max(delays), 1),
            "run_duration_mean_min": round(statistics.mean(durations), 1) if durations else None,
            "note": "retraso del scheduler de GitHub Actions sobre la grilla */20; la corrida incluye 5 min de "
                    "escucha de PumpPortal (script_82) antes de puntuar"}


def structural_floor(cron, age_gate_min=30, cadence_min=CRON_EVERY_MIN):
    """Piso de latencia del diseño actual para un token nuevo de pump.fun (minutos desde la creación del par).
    script_82 lo detecta a los ~4 min (escucha de PumpPortal) pero script_97 no lo emite hasta que tenga
    edad >= EMIT_MIN_AGE_MIN; el chequeo siguiente llega en promedio cadence/2 después. El retraso del scheduler
    desplaza todas las corridas por igual: no suma al piso de un token ya detectado, sí a uno detectado tarde."""
    return {"age_gate_min": age_gate_min, "cadence_min": cadence_min,
            "scheduler_delay_mean_min": cron.get("start_delay_mean_min"),
            "run_duration_mean_min": cron.get("run_duration_mean_min"),
            "expected_first_emit_age_min": round(age_gate_min + cadence_min / 2, 1),
            "explanation": "edad mínima de emisión + media cadencia del cron; con un poll de P minutos el piso "
                           "baja a age_gate + P/2"}


# ---------------------------------------------------------------------------
# Red (inyectable)
# ---------------------------------------------------------------------------

def _get_json(get, url, headers=None):
    try:
        r = get(url, headers=headers or {"Accept": "application/json"}, timeout=20)
        if getattr(r, "status_code", 200) != 200:
            return None
        return r.json()
    except Exception:
        return None


def fetch_gt_candles(get, chain, pool, emitted):
    net = GT_NETWORKS.get(chain or "solana")
    if not net or not pool:
        return []
    url = GT_OHLCV.format(net=net, pool=pool, before=int(emitted + WINDOW_AFTER_MIN * 60))
    data = _get_json(get, url)
    try:
        rows = data["data"]["attributes"]["ohlcv_list"]
    except (TypeError, KeyError):
        return []
    return [(int(r[0]), float(r[1]), float(r[4])) for r in rows if r and len(r) >= 5]


def fetch_binance_candles(get, symbol, emitted):
    if not symbol:
        return []
    start = int((emitted - WINDOW_BEFORE_MIN * 60) * 1000)
    out, end = [], int((emitted + WINDOW_AFTER_MIN * 60) * 1000)
    while start < end:
        data = _get_json(get, BINANCE_KLINES.format(symbol=symbol.upper(), start=start, end=end))
        if not isinstance(data, list) or not data:
            break
        out.extend((int(k[0]) // 1000, float(k[1]), float(k[4])) for k in data)
        start = int(data[-1][0]) + 60_000
        if len(data) < 1000:
            break
    return out


def fetch_runs(get, repo, token):
    if not repo:
        return []
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = _get_json(get, ACTIONS_RUNS.format(repo=repo), headers)
    return (data or {}).get("workflow_runs") or []


# ---------------------------------------------------------------------------
# Corrida
# ---------------------------------------------------------------------------

def run(root=None, n=20, get=None, runs=None, now=None, sleep=time.sleep):
    root = Path(root or ROOT)
    alerts_dir = root / "02_Analisis" / "alerts"
    all_alerts = json.loads((alerts_dir / "_all_alerts.json").read_text(encoding="utf-8"))
    rows = []
    for alert in last_alerts(all_alerts, n):
        path = alerts_dir / detail_name(alert)
        detail = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        row = structural_row(alert, detail)
        if get is not None:
            emitted = parse_alert_ts(alert["timestamp"])
            if row["route"] == "cex":
                candles, source = fetch_binance_candles(get, row["symbol"], emitted), "binance 1m"
            else:
                candles, source = fetch_gt_candles(get, row["chain"], row["pool"], emitted), "geckoterminal 1m"
                sleep(2.5)   # GeckoTerminal: 30 req/min sin clave
            row = dict(measured_row(row, candles, emitted), candle_source=source)
        rows.append(row)
    if runs is None and get is not None:
        runs = fetch_runs(get, os.environ.get("GITHUB_REPOSITORY"), os.environ.get("GITHUB_TOKEN"))
    cron = cron_drift(runs or [])
    return {
        "version": VERSION, "generated_at": iso(now or time.time()),
        "method": {"pump_start": f"primer minuto con cierre >= +{int(PUMP_THRESHOLD * 100)} % sobre el cierre de "
                                 f"{PUMP_LOOKBACK_MIN} min antes, en [emisión − {WINDOW_BEFORE_MIN} min (o lanzamiento),"
                                 f" emisión + {WINDOW_AFTER_MIN} min]",
                   "gap": "emisión − inicio del pump (min); negativo = anticipada",
                   "measured": get is not None},
        "summary": {"n_alerts": len(rows), "structural": summarize_structural(rows),
                    "measured": summarize_gaps(rows) if get is not None else None},
        "cron_pipeline_t0": cron,
        "structural_floor_new_token": structural_floor(cron),
        "alerts": rows,
    }


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--offline", action="store_true", help="solo la parte estructural (sin red)")
    ap.add_argument("--runs-file", help="JSON de la API de Actions (workflow_runs) en lugar de pedirlo")
    ap.add_argument("--root")
    ap.add_argument("--out")
    args = ap.parse_args(argv)
    root = Path(args.root or ROOT)
    get = None
    if not args.offline:
        import requests
        get = requests.get
    runs = None
    if args.runs_file:
        runs = json.loads(Path(args.runs_file).read_text(encoding="utf-8")).get("workflow_runs") or []
    report = run(root, args.n, get, runs)
    out = Path(args.out or root / "02_Analisis" / "diagnostics" / "latency_analysis.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    try:
        import lib_persist
        lib_persist.log_operation("latency_analysis", "latency_analysis", [out], alerts=len(report["alerts"]),
                                  measured=bool(get))
    except Exception:
        pass
    s = report["summary"]
    print(json.dumps({"structural": s["structural"], "measured": s["measured"],
                      "cron": report["cron_pipeline_t0"], "floor": report["structural_floor_new_token"]},
                     indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
