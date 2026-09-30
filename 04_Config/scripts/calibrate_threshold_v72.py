#!/usr/bin/env python3
"""
calibrate_threshold_v72.py — Calibración del umbral de ALERTA del scoring v7.2 (solo lectura).

Hipótesis de Dirección  [H1]: "el umbral 50 quedó desactualizado tras las bonificaciones de v7.2".
Hipótesis complementaria [H2]: "la inflación se explica por tokens de < 60 min, donde vol_m5/vol_h1 ≈ 1
                                por construcción: los bonos de 'aceleración' premian la juventud".

Datos: 01_Datos_Crudos/final_detection/detection_*.json
  - Conjunto A: detecciones con campos v7.2 (dexscreener.volume_m5 presente) -> se RECALCULA el
    score con script_82.score_token, con el reloj fijado al momento de la detección (la edad del par
    se mide entonces, no hoy) y sin _accumulated.json (evita leer estado posterior: bp_delta = 0).
  - Conjunto B: detecciones legadas (sin campos v7.2) -> solo el score v7.1 guardado, como línea base.
Resultados (opcional, --outcomes-sample N): muestra estratificada por score del Conjunto B con ventana de
48 h ya cumplida; OHLCV de 15 min de GeckoTerminal (sin key) del mismo pool. Evento definitivo de
Dirección: > +20% en <= 48 h, medido de dos formas: máximo (high) y cierre a 48 h. Además: rug
(mínimo <= -90%) y AUC del score.
Salida: 02_Analisis/diagnostics/threshold_analysis.json (+ resumen en consola)

Uso: python 04_Config/scripts/calibrate_threshold_v72.py [--outcomes-sample 50]
"""
import argparse
import glob
import importlib.util
import json
import math
import os
import random
import statistics
import sys
import tempfile
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

import requests

SCRIPTS = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
DETECTION_GLOB = str(ROOT / "01_Datos_Crudos" / "final_detection" / "detection_*.json")
OUT_FILE = ROOT / "02_Analisis" / "diagnostics" / "threshold_analysis.json"
THRESHOLDS = [50, 60, 70, 80, 90]
FINE_THRESHOLDS = list(range(50, 61))
SCORING_DELAY_S = 330   # script_82 escucha PumpPortal 300 s y luego enriquece: ~5.5 min tras el timestamp
TARGET_RATE = (0.05, 0.15)
ACCEL_BONUSES = {"Volumen acelerado (5m/1h > 50%)": 25, "Volumen en aceleración (5m/1h > 25%)": 15,
                 "Trades acelerados (5m/1h > 50%)": 20, "Trades en aceleración (5m/1h > 25%)": 10}
# Resultados a 48 h (pipeline de detección = memecoins de Solana)
GT_OHLCV = "https://api.geckoterminal.com/api/v2/networks/solana/pools/{pool}/ohlcv/minute"
GT_INTERVAL_S = 6.5          # [V] a 2.2 s, 128/164 llamadas devolvieron HTTP 429
GT_MAX_RETRIES = 3
GT_BACKOFF_S = 30.0
HORIZON_S = 48 * 3600
EVENT_MOVE = 0.20
RUG_MOVE = -0.90
SCORE_BUCKETS = [(0, 30), (30, 50), (50, 70), (70, 101)]
SEED = 20260930


def wilson(k, n, z=1.645):
    """IC 90% de Wilson para una proporción."""
    if n == 0:
        return None
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [round(c - h, 4), round(c + h, 4)]


def auc(scores_pos, scores_neg):
    """AUC = P(score de un positivo > score de un negativo), empates cuentan 1/2 (Mann-Whitney)."""
    if not scores_pos or not scores_neg:
        return None
    wins = sum((p > q) + 0.5 * (p == q) for p in scores_pos for q in scores_neg)
    return round(wins / (len(scores_pos) * len(scores_neg)), 4)


def fetch_outcome(pool, t0, p0, session):
    """Máximo, cierre y mínimo en (t0, t0+48h] relativos al precio de detección p0."""
    for attempt in range(GT_MAX_RETRIES + 1):
        try:
            r = session.get(GT_OHLCV.format(pool=pool), timeout=20,
                            params={"aggregate": 15, "before_timestamp": int(t0 + HORIZON_S + 900), "limit": 200,
                                    "currency": "usd"},
                            headers={"Accept": "application/json;version=20230302",
                                     "User-Agent": "shot-de-mercado-calibration/1.0"})
        except requests.RequestException as e:
            return {"status": "error", "detail": str(e)[:120]}
        if r.status_code == 429 and attempt < GT_MAX_RETRIES:
            ra = r.headers.get("Retry-After", "")
            time.sleep(float(ra) if ra.isdigit() else GT_BACKOFF_S * (attempt + 1))
            continue
        break
    if r.status_code != 200:
        return {"status": f"http_{r.status_code}"}
    rows = ((r.json().get("data") or {}).get("attributes") or {}).get("ohlcv_list") or []
    win = sorted(c for c in rows if t0 < c[0] <= t0 + HORIZON_S - 900)
    if not win:
        return {"status": "sin_velas"}
    return {"status": "ok", "n_candles": len(win), "coverage": round(len(win) / (HORIZON_S / 900), 3),
            "max_ret": round(max(c[2] for c in win) / p0 - 1, 4),
            "close_ret": round(win[-1][4] / p0 - 1, 4),
            "min_ret": round(min(c[3] for c in win) / p0 - 1, 4)}


def outcome_study(set_b_rows, per_bucket):
    """Muestra estratificada por score v7.1 (semilla fija), ventana de 48 h cumplida."""
    now = time.time()
    eligible = [r for r in set_b_rows if r.get("pool") and r.get("price") and r["t0"] + HORIZON_S + 3600 < now]
    seen, pool_rows = set(), []
    for r in eligible:                       # un token una sola vez (su primera detección)
        if r["mint"] not in seen:
            seen.add(r["mint"])
            pool_rows.append(r)
    rng = random.Random(SEED)
    sample = []
    for lo, hi in SCORE_BUCKETS:
        bucket = [r for r in pool_rows if lo <= r["score"] < hi]
        sample += rng.sample(bucket, min(per_bucket, len(bucket)))
    session, results = requests.Session(), []
    for i, r in enumerate(sample):
        if i:
            time.sleep(GT_INTERVAL_S)
        out = fetch_outcome(r["pool"], r["t0"], r["price"], session)
        results.append({"mint": r["mint"], "run": r["run"], "score": r["score"], **out})
        if (i + 1) % 25 == 0:
            print(f"   resultados: {i + 1}/{len(sample)}", flush=True)
    ok = [x for x in results if x["status"] == "ok"]
    summary = {"eligible_unique_tokens": len(pool_rows), "sampled": len(sample), "with_data": len(ok),
               "status_counts": dict(Counter(x["status"] for x in results)), "by_bucket": {}, "by_threshold": {}}
    for name, key in (("max_48h", "max_ret"), ("close_48h", "close_ret")):
        pos = [x["score"] for x in ok if x[key] >= EVENT_MOVE]
        neg = [x["score"] for x in ok if x[key] < EVENT_MOVE]
        summary[f"base_rate_{name}"] = {"k": len(pos), "n": len(ok), "rate": round(len(pos) / len(ok), 4) if ok else None,
                                        "ci90": wilson(len(pos), len(ok))}
        summary[f"auc_{name}"] = auc(pos, neg)
    rugs = sum(x["min_ret"] <= RUG_MOVE for x in ok)
    summary["rug_rate_48h"] = {"k": rugs, "n": len(ok), "rate": round(rugs / len(ok), 4) if ok else None, "ci90": wilson(rugs, len(ok))}
    for lo, hi in SCORE_BUCKETS:
        b = [x for x in ok if lo <= x["score"] < hi]
        k_max = sum(x["max_ret"] >= EVENT_MOVE for x in b)
        k_close = sum(x["close_ret"] >= EVENT_MOVE for x in b)
        summary["by_bucket"][f"{lo}-{hi - 1}"] = {
            "n": len(b),
            "hit_max_48h": {"k": k_max, "ci90": wilson(k_max, len(b))},
            "hit_close_48h": {"k": k_close, "ci90": wilson(k_close, len(b))},
            "rug_48h": {"k": sum(x["min_ret"] <= RUG_MOVE for x in b)},
        }
    for t in THRESHOLDS:
        a = [x for x in ok if x["score"] >= t]
        k = sum(x["max_ret"] >= EVENT_MOVE for x in a)
        kc = sum(x["close_ret"] >= EVENT_MOVE for x in a)
        summary["by_threshold"][str(t)] = {"n": len(a), "precision_max": round(k / len(a), 4) if a else None,
                                           "ci90_max": wilson(k, len(a)), "precision_close": round(kc / len(a), 4) if a else None,
                                           "ci90_close": wilson(kc, len(a))}
    summary["note"] = ("Muestra estratificada: las tasas por umbral NO son la tasa poblacional (los buckets altos están "
                       "sobre-representados). La base poblacional se estima ponderando por bucket.")
    weights, pop = {}, 0.0
    for lo, hi in SCORE_BUCKETS:
        w = sum(lo <= r["score"] < hi for r in pool_rows)
        weights[f"{lo}-{hi - 1}"] = w
        b = [x for x in ok if lo <= x["score"] < hi]
        if b and pool_rows:
            pop += w / len(pool_rows) * sum(x["max_ret"] >= EVENT_MOVE for x in b) / len(b)
    summary["population_weighted_base_rate_max_48h"] = round(pop, 4)
    summary["population_bucket_counts"] = weights
    return summary, results


def load_script_82(workdir):
    """Importa script_82 con cwd en un directorio temporal: sus makedirs relativos y la lectura
    relativa de _accumulated.json no tocan el repo."""
    prev = os.getcwd()
    os.chdir(workdir)
    try:
        spec = importlib.util.spec_from_file_location("script_82_calib", SCRIPTS / "script_82_final_detection.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    finally:
        os.chdir(prev)


def detection_epoch(ts):
    return datetime.strptime(ts, "%Y-%m-%d_%H%M%S").replace(tzinfo=timezone.utc).timestamp()


def rate_table(scores):
    n = len(scores)
    return {str(t): {"n_alerta": sum(s >= t for s in scores), "rate": round(sum(s >= t for s in scores) / n, 4) if n else None}
            for t in THRESHOLDS}


def histogram(scores, width=10):
    h = Counter(min(int(s) // width * width, 100) for s in scores)
    return {f"{k}-{k + width - 1 if k < 100 else 100}": h[k] for k in sorted(h)}


def age_bucket(age_min):
    if age_min is None:
        return "sin_par"
    for lim, name in ((5, "<5m"), (60, "5-60m"), (240, "1-4h"), (1440, "4-24h")):
        if age_min < lim:
            return name
    return ">24h"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Calibración del umbral v7.2")
    ap.add_argument("--outcomes-sample", type=int, default=0,
                    help="tokens por bucket de score para medir resultados a 48 h (0 = no medir)")
    args = ap.parse_args(argv)
    files = sorted(glob.glob(DETECTION_GLOB))
    set_a, set_b, per_run = [], [], {}
    with tempfile.TemporaryDirectory() as work:
        s82 = load_script_82(work)
        prev = os.getcwd()
        os.chdir(work)                       # sin _accumulated.json -> bp_delta = 0
        try:
            for f in files:
                d = json.load(open(f, encoding="utf-8"))
                ts = d.get("timestamp")
                t_score = detection_epoch(ts) + SCORING_DELAY_S
                run_scores = []
                for mint, x in (d.get("enriched") or {}).items():
                    dx = x.get("dexscreener")
                    if isinstance(dx, dict) and "volume_m5" in dx:
                        with mock.patch("time.time", return_value=t_score):
                            score, reasons = s82.score_token(x.get("token") or {}, dx)
                        age = (t_score - dx["pairCreatedAt"] / 1000) / 60 if dx.get("pairCreatedAt") else None
                        vol_ratio = dx["volume_m5"] / dx["volume_h1"] if dx.get("volume_h1") else None
                        set_a.append({"run": ts, "mint": mint, "source": x.get("source"), "stored": x.get("score"),
                                      "recomputed": score, "reasons": reasons, "age_min": age, "vol_ratio": vol_ratio,
                                      "mcap": dx.get("marketCapUsd"), "liq": dx.get("liquidityUsd")})
                        run_scores.append(x.get("score"))
                    elif isinstance(x.get("score"), (int, float)):
                        set_b.append({"run": ts, "mint": mint, "score": x["score"], "has_dex": isinstance(dx, dict),
                                      "pool": dx.get("pairAddress") if isinstance(dx, dict) else None,
                                      "price": dx.get("priceUsd") if isinstance(dx, dict) else None,
                                      "t0": t_score})
                if run_scores:
                    per_run[ts] = {"n": len(run_scores), **{str(t): sum(s >= t for s in run_scores) for t in THRESHOLDS}}
        finally:
            os.chdir(prev)

    stored = [r["stored"] for r in set_a]
    recomp = [r["recomputed"] for r in set_a]
    agree = sum(1 for r in set_a if r["stored"] == r["recomputed"])
    within15 = sum(1 for r in set_a if abs(r["stored"] - r["recomputed"]) <= 15)

    # H2: ¿qué explica las ALERTAS (>= 70)?
    alerts = [r for r in set_a if r["recomputed"] >= 70]
    by_age = {}
    for r in set_a:
        b = by_age.setdefault(age_bucket(r["age_min"]), {"n": 0, "alerta_70": 0})
        b["n"] += 1
        b["alerta_70"] += r["recomputed"] >= 70
    young_saturated = sum(1 for r in alerts if r["age_min"] is not None and r["age_min"] < 60
                          and r["vol_ratio"] is not None and r["vol_ratio"] >= 0.9)
    reason_freq = Counter(reason for r in alerts for reason in r["reasons"])
    low_fund = sum(1 for r in alerts if "MCap bajo" in r["reasons"] and "Volumen bajo" in r["reasons"])

    # Contrafáctico: bonos de aceleración solo con la ventana h1 completa (edad >= 60 min).
    # Aproximación: se restan del score final ya topeado en 100, así que subestima levemente
    # a los tokens que superaban 100 antes del tope (los deja más bajos, no más altos).
    gated = []
    for r in set_a:
        s = r["recomputed"]
        if r["age_min"] is not None and r["age_min"] < 60:
            s = s - sum(v for k, v in ACCEL_BONUSES.items() if k in r["reasons"])
        r["gated"] = max(0, s)
        gated.append(r["gated"])
    fine = {str(t): round(sum(g >= t for g in gated) / len(gated), 4) for t in FINE_THRESHOLDS} if gated else {}

    legacy = [r["score"] for r in set_b]
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "hypotheses": {"H1": "umbral desactualizado tras bonos v7.2",
                       "H2": "inflación por tokens < 60 min con vol_m5/vol_h1 ≈ 1 por construcción"},
        "data": {"files": len(files), "set_a_v72_complete": len(set_a), "set_a_runs": sorted(per_run),
                 "set_b_legacy": len(set_b), "set_b_with_dex": sum(r["has_dex"] for r in set_b)},
        "method": {"clock": f"timestamp de la corrida + {SCORING_DELAY_S}s", "bp_delta": "0 (sin _accumulated.json)",
                   "scorer": "script_82_final_detection.score_token (código actual)"},
        "reproducibility": {"exact_match": agree, "within_15": within15, "n": len(set_a),
                            "note": "diferencias esperadas: bp_delta (±15) y reloj (±1 min en los cortes de edad)"},
        "set_a": {
            "stored_production_score": {"histogram": histogram(stored), "rates": rate_table(stored),
                                        "median": statistics.median(stored) if stored else None},
            "recomputed_v72": {"histogram": histogram(recomp), "rates": rate_table(recomp),
                               "median": statistics.median(recomp) if recomp else None},
            "per_run_stored": per_run,
            "by_age_bucket": by_age,
            "alerts_70": {"n": len(alerts), "young_and_saturated_ratio": young_saturated,
                          "mcap_bajo_y_volumen_bajo": low_fund, "top_reasons": reason_freq.most_common(12)},
            "counterfactual_accel_gated_60m": {"rates": rate_table(gated), "histogram": histogram(gated),
                                               "fine_sweep_rates": fine},
            "rows": [{k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items() if k != "reasons"}
                     for r in set_a],
        },
        "set_b_legacy_v71": {"histogram": histogram(legacy), "rates": rate_table(legacy),
                             "median": statistics.median(legacy) if legacy else None},
        "target_rate": list(TARGET_RATE),
    }
    if args.outcomes_sample > 0:
        print(f"[INFO] midiendo resultados a 48 h: hasta {args.outcomes_sample} tokens por bucket "
              f"(GeckoTerminal, {GT_INTERVAL_S}s entre llamadas)", flush=True)
        summary, rows = outcome_study(set_b, args.outcomes_sample)
        report["outcomes_legacy_v71"] = summary
        report["outcome_rows"] = rows
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[OK] {OUT_FILE}")
    print(f"Conjunto A (v7.2 completo): n={len(set_a)} en {len(per_run)} corridas · Conjunto B (legado): n={len(set_b)}")
    print(f"Reproducibilidad: exacto {agree}/{len(set_a)} · |Δ|<=15: {within15}/{len(set_a)}")
    for name, sc in (("v7.2 producción (guardado)", stored), ("v7.2 recalculado", recomp),
                     ("v7.2 con bonos gateados >=60m", gated), ("v7.1 legado", legacy)):
        rt = rate_table(sc)
        print(f"  {name:<30} " + "  ".join(f">={t}: {rt[str(t)]['rate']:.1%}" for t in THRESHOLDS if rt[str(t)]['rate'] is not None))
    print(f"ALERTAS>=70: {len(alerts)} · <60min y m5/h1>=0.9: {young_saturated} · 'MCap bajo'+'Volumen bajo': {low_fund}")
    print("Por edad:", {k: f"{v['alerta_70']}/{v['n']}" for k, v in sorted(by_age.items())})
    print("Gateado, barrido fino:", fine)
    o = report.get("outcomes_legacy_v71")
    if o:
        print(f"Resultados 48h: con datos {o['with_data']}/{o['sampled']} · base (max) {o['base_rate_max_48h']} · "
              f"base (cierre) {o['base_rate_close_48h']} · rug {o['rug_rate_48h']} · AUC max {o['auc_max_48h']} · "
              f"AUC cierre {o['auc_close_48h']} · base poblacional ponderada {o['population_weighted_base_rate_max_48h']}")
        for b, v in o["by_bucket"].items():
            print(f"   score {b:<7} n={v['n']:<3} hit_max={v['hit_max_48h']} hit_close={v['hit_close_48h']} rugs={v['rug_48h']['k']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
