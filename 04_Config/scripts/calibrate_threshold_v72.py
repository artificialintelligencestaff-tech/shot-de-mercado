#!/usr/bin/env python3
"""
calibrate_threshold_v72.py — Calibración del umbral de ALERTA del scoring (v7.2 / v7.2.1), solo lectura.

Hipótesis de Dirección  [H1]: "el umbral 50 quedó desactualizado tras las bonificaciones de v7.2".
Hipótesis complementaria [H2]: "la inflación se explica por tokens de < 60 min, donde vol_m5/vol_h1 ≈ 1
                                por construcción: los bonos de 'aceleración' premian la juventud".

Datos: 01_Datos_Crudos/final_detection/detection_*.json
  - Conjunto A: detecciones con campos v7.2 (dexscreener.volume_m5 presente) -> se RECALCULA el score
    con el script_82 del árbol actual (versión = script_82.SCORING_VERSION, "7.2" si no existe), con el
    reloj fijado al momento de la detección y sin _accumulated.json (bp_delta = 0).
  - Conjunto B: detecciones legadas (sin campos v7.2) -> solo el score v7.1 guardado, como línea base.

Métrica dual de precisión (decisión de Dirección, 2026-09-30):
  - PRIMARIA (operativa, para calibrar): tocar +20% antes de caer −30% desde el precio de entrada.
  - SECUNDARIA (honestidad, para el público): cierre >= +20% a las 48 h.
  Precios: OHLCV de 15 min de GeckoTerminal (sin key) del mismo pool. Dentro de cada vela se asume el
  orden open -> low -> high -> close: si una vela toca −30% y +20% a la vez, cuenta primero la caída
  (resolución conservadora; las velas ambiguas se reportan). Entrada = precio de DexScreener en la
  detección. Ventana (t0, t0 + 48 h].
  Observación censurada (Conjunto A, 48 h aún no cumplidas): la primaria queda decidida en cuanto se
  toca una barrera; si no, queda "pendiente". La secundaria queda pendiente hasta cumplir 48 h.

Uso:
  python 04_Config/scripts/calibrate_threshold_v72.py                          # tasas (sin red)
  python 04_Config/scripts/calibrate_threshold_v72.py --outcomes-sample 50     # + legado, métrica dual
  python 04_Config/scripts/calibrate_threshold_v72.py --outcomes-set-a         # + Conjunto A (censurado)
  opciones: --out RUTA · --cache RUTA (velas ya descargadas; evita repetir llamadas)
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
THRESHOLDS = [50, 56, 60, 70, 80, 90]
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
CANDLE_S = 900
CACHE_MAX_AGE_S = 6 * 3600
HORIZON_S = 48 * 3600
EVENT_UP = 0.20              # primaria y secundaria: +20%
EVENT_DOWN = -0.30           # primaria: antes de caer −30%
RUG_MOVE = -0.90
SCORE_BUCKETS = [(0, 30), (30, 50), (50, 70), (70, 101)]
SEED = 20260930


# ---------------------------------------------------------------------------
# Métrica dual (definiciones de Dirección)
# ---------------------------------------------------------------------------

def event_primary(prices_48h, entry_price):
    """Tocar +20% antes de caer -30%."""
    peak = entry_price
    for p in prices_48h:
        peak = max(peak, p)
        if peak >= entry_price * (1 + EVENT_UP):
            return True
        if p <= entry_price * (1 + EVENT_DOWN):
            return False
    return False


def event_secondary(prices_48h, entry_price):
    """Cierre >= +20% a 48h."""
    if not prices_48h:
        return False
    return prices_48h[-1] >= entry_price * (1 + EVENT_UP)


def candle_path(candles):
    """Velas [ts, o, h, l, c, v] -> serie de precios con orden open -> low -> high -> close."""
    path = []
    for c in candles:
        path += [c[1], c[3], c[2], c[4]]
    return path


def evaluate_outcome(candles, p0, t0, now):
    """Estados 'hit' | 'miss' | 'pending' para la primaria y la secundaria (+ diagnósticos)."""
    complete = now >= t0 + HORIZON_S
    up, down = p0 * (1 + EVENT_UP), p0 * (1 + EVENT_DOWN)
    path = candle_path(candles)
    touched = any(p >= up or p <= down for p in path)
    if complete or touched:
        primary = "hit" if event_primary(path, p0) else "miss"
    else:
        primary = "pending"
    secondary = ("hit" if event_secondary([c[4] for c in candles] or [p0], p0) else "miss") if complete else "pending"
    return {
        "primary": primary, "secondary": secondary, "complete": complete,
        "ambiguous_candles": sum(1 for c in candles if c[2] >= up and c[3] <= down),
        "n_candles": len(candles),
        "max_ret": round(max((c[2] for c in candles), default=p0) / p0 - 1, 4),
        "min_ret": round(min((c[3] for c in candles), default=p0) / p0 - 1, 4),
        "last_ret": round((candles[-1][4] if candles else p0) / p0 - 1, 4),
    }


# ---------------------------------------------------------------------------
# Estadística
# ---------------------------------------------------------------------------

def wilson(k, n, z=1.645):
    """IC 90% de Wilson para una proporción."""
    if n == 0:
        return None
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [round(max(0.0, c - h), 4), round(min(1.0, c + h), 4)]


def auc(scores_pos, scores_neg):
    """AUC = P(score de un positivo > score de un negativo), empates cuentan 1/2 (Mann-Whitney)."""
    if not scores_pos or not scores_neg:
        return None
    wins = sum((p > q) + 0.5 * (p == q) for p in scores_pos for q in scores_neg)
    return round(wins / (len(scores_pos) * len(scores_neg)), 4)


def precision_block(rows, metric):
    """k/n de 'hit' entre las observaciones resueltas de `metric`; informa las pendientes."""
    resolved = [r for r in rows if r[metric] in ("hit", "miss")]
    k = sum(r[metric] == "hit" for r in resolved)
    return {"n_resolved": len(resolved), "k_hit": k, "pending": sum(r[metric] == "pending" for r in rows),
            "rate": round(k / len(resolved), 4) if resolved else None, "ci90": wilson(k, len(resolved))}


def precision_by_threshold(rows, score_key):
    out = {"all": {"n": len(rows), "primary": precision_block(rows, "primary"),
                   "secondary": precision_block(rows, "secondary")}}
    for t in THRESHOLDS:
        sel = [r for r in rows if r[score_key] >= t]
        out[str(t)] = {"n": len(sel), "primary": precision_block(sel, "primary"),
                       "secondary": precision_block(sel, "secondary")}
    return out


# ---------------------------------------------------------------------------
# Descarga de velas (con caché)
# ---------------------------------------------------------------------------

class CandleSource:
    def __init__(self, cache_path=None, offline=False):
        self.cache_path = Path(cache_path) if cache_path else None
        self.offline = offline
        self.cache = {}
        if self.cache_path and self.cache_path.exists():
            self.cache = json.loads(self.cache_path.read_text(encoding="utf-8"))
        self.session, self.calls, self.last = requests.Session(), 0, 0.0

    def get(self, pool, t0):
        key = f"{pool}@{int(t0)}"
        hit = self.cache.get(key)
        if self.offline:                     # solo caché: mismo resultado que la corrida que la llenó, sin red
            return (hit["status"], hit.get("candles", [])) if hit else ("no_cacheado", [])
        # Se reutiliza solo lo descargado bien: completo, o censurado de hace < 6 h. Los errores se reintentan.
        if hit and hit["status"] == "ok" and (hit.get("complete") or time.time() - hit["fetched_at"] < CACHE_MAX_AGE_S):
            return hit["status"], hit.get("candles", [])
        wait = GT_INTERVAL_S - (time.monotonic() - self.last)
        if self.calls and wait > 0:
            time.sleep(wait)
        status, candles = self._fetch(pool, t0)
        self.last, self.calls = time.monotonic(), self.calls + 1
        self.cache[key] = {"status": status, "candles": candles, "fetched_at": time.time(),
                           "complete": time.time() >= t0 + HORIZON_S}
        return status, candles

    def _fetch(self, pool, t0):
        for attempt in range(GT_MAX_RETRIES + 1):
            try:
                r = self.session.get(GT_OHLCV.format(pool=pool), timeout=20,
                                     params={"aggregate": 15, "before_timestamp": int(t0 + HORIZON_S + CANDLE_S),
                                             "limit": 200, "currency": "usd"},
                                     headers={"Accept": "application/json;version=20230302",
                                              "User-Agent": "shot-de-mercado-calibration/1.1"})
            except requests.RequestException:
                return "error", []
            if r.status_code == 429 and attempt < GT_MAX_RETRIES:
                ra = r.headers.get("Retry-After", "")
                time.sleep(float(ra) if ra.isdigit() else GT_BACKOFF_S * (attempt + 1))
                continue
            break
        if r.status_code != 200:
            return f"http_{r.status_code}", []
        rows = ((r.json().get("data") or {}).get("attributes") or {}).get("ohlcv_list") or []
        return "ok", sorted(c for c in rows if t0 < c[0] <= t0 + HORIZON_S - CANDLE_S)

    def save(self):
        if self.cache_path:
            self.cache_path.parent.mkdir(parents=True, exist_ok=True)
            self.cache_path.write_text(json.dumps(self.cache), encoding="utf-8")


def measure(rows, source, label):
    """Evalúa la métrica dual para filas con pool, price, t0. 'sin_velas' con API ok = sin operaciones."""
    now, out = time.time(), []
    for i, r in enumerate(rows):
        status, candles = source.get(r["pool"], r["t0"])
        if status == "ok":
            res = evaluate_outcome(candles, r["price"], r["t0"], now)
            res["status"] = "ok" if candles else "sin_velas"
        else:
            res = {"status": status, "primary": "sin_datos", "secondary": "sin_datos"}
        out.append({**{k: r[k] for k in ("mint", "run") if k in r}, **{k: v for k, v in r.items() if k.startswith("score")}, **res})
        if (i + 1) % 25 == 0:
            print(f"   {label}: {i + 1}/{len(rows)} (llamadas a la API: {source.calls})", flush=True)
            source.save()
    source.save()
    return out


def unique_first(rows):
    seen, out = set(), []
    for r in rows:
        if r["mint"] not in seen and r.get("pool") and r.get("price"):
            seen.add(r["mint"])
            out.append(r)
    return out


def outcome_study_legacy(set_b_rows, per_bucket, source):
    """Conjunto B: muestra estratificada por score v7.1 (semilla fija), ventana de 48 h cumplida."""
    now = time.time()
    pool_rows = unique_first([r for r in set_b_rows if r["t0"] + HORIZON_S + 3600 < now])
    rng = random.Random(SEED)
    sample = []
    for lo, hi in SCORE_BUCKETS:
        bucket = [r for r in pool_rows if lo <= r["score"] < hi]
        sample += rng.sample(bucket, min(per_bucket, len(bucket)))
    rows = measure([{**r, "score": r["score"]} for r in sample], source, "legado")
    ok = [x for x in rows if x["status"] == "ok"]
    summary = {"eligible_unique_tokens": len(pool_rows), "sampled": len(sample), "with_candles": len(ok),
               "status_counts": dict(Counter(x["status"] for x in rows)),
               "precision_excluding_no_candles": precision_by_threshold(ok, "score"),
               "precision_no_candles_as_miss": precision_by_threshold(
                   [dict(x, primary="miss", secondary="miss") if x["status"] == "sin_velas" else x
                    for x in rows if x["status"] in ("ok", "sin_velas")], "score"),
               "rug_48h": precision_block([dict(x, rug="hit" if x["min_ret"] <= RUG_MOVE else "miss") for x in ok], "rug"),
               "primary_hit_and_rug": sum(1 for x in ok if x["primary"] == "hit" and x["min_ret"] <= RUG_MOVE),
               "ambiguous_candles_total": sum(x.get("ambiguous_candles", 0) for x in ok),
               "by_bucket": {}}
    for lo, hi in SCORE_BUCKETS:
        b = [x for x in ok if lo <= x["score"] < hi]
        summary["by_bucket"][f"{lo}-{hi - 1}"] = {"n": len(b), "primary": precision_block(b, "primary"),
                                                  "secondary": precision_block(b, "secondary"),
                                                  "rugs": sum(x["min_ret"] <= RUG_MOVE for x in b)}
    for m in ("primary", "secondary"):
        pos = [x["score"] for x in ok if x[m] == "hit"]
        neg = [x["score"] for x in ok if x[m] == "miss"]
        summary[f"auc_{m}"] = auc(pos, neg)
    weights, pop = {}, 0.0
    for lo, hi in SCORE_BUCKETS:
        w = sum(lo <= r["score"] < hi for r in pool_rows)
        weights[f"{lo}-{hi - 1}"] = w
        b = [x for x in ok if lo <= x["score"] < hi and x["primary"] in ("hit", "miss")]
        if b and pool_rows:
            pop += w / len(pool_rows) * sum(x["primary"] == "hit" for x in b) / len(b)
    summary["population_weighted_primary_rate"] = round(pop, 4)
    summary["population_bucket_counts"] = weights
    summary["note"] = ("Muestra estratificada: por umbral NO es la tasa poblacional (buckets altos sobre-representados); "
                       "la base poblacional se pondera por bucket. 'sin_velas' = el pool no operó en la ventana.")
    return summary, rows


def outcome_study_set_a(set_a_rows, source, version):
    """Conjunto A: todas las detecciones v7.2 (primera por token), censura hasta cumplir 48 h."""
    uniq = unique_first(set_a_rows)
    rows = measure([{"mint": r["mint"], "run": r["run"], "pool": r["pool"], "price": r["price"], "t0": r["t0"],
                     "score_v72_prod": r["stored"], "score_current": r["recomputed"]} for r in uniq], source, "conjunto A")
    ok = [x for x in rows if x["status"] in ("ok", "sin_velas")]
    return {"unique_tokens": len(uniq), "status_counts": dict(Counter(x["status"] for x in rows)),
            "current_scorer_version": version,
            "precision_v72_prod": precision_by_threshold(ok, "score_v72_prod"),
            f"precision_v{version}": precision_by_threshold(ok, "score_current"),
            "complete_48h": sum(1 for x in ok if x.get("complete")),
            "note": "Censurado: 'pending' = sin barrera tocada todavía (primaria) o 48 h no cumplidas (secundaria)."}, rows


# ---------------------------------------------------------------------------
# Recálculo del score
# ---------------------------------------------------------------------------

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


def fmt_prec(block):
    p = block["primary"]
    s = block["secondary"]
    return (f"n={block['n']:<4} primaria {p['k_hit']}/{p['n_resolved']}={p['rate']} IC90={p['ci90']} (pend {p['pending']}) · "
            f"secundaria {s['k_hit']}/{s['n_resolved']}={s['rate']} IC90={s['ci90']} (pend {s['pending']})")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Calibración del umbral de ALERTA (v7.2 / v7.2.1)")
    ap.add_argument("--outcomes-sample", type=int, default=0,
                    help="tokens por bucket del legado para medir la métrica dual (0 = no medir)")
    ap.add_argument("--outcomes-set-a", action="store_true", help="medir la métrica dual en el Conjunto A (censurado)")
    ap.add_argument("--out", default=str(OUT_FILE), help="ruta del reporte JSON")
    ap.add_argument("--cache", default=None, help="caché de velas (JSON) para no repetir llamadas")
    ap.add_argument("--offline", action="store_true", help="usar solo la caché (sin red); faltantes = 'no_cacheado'")
    args = ap.parse_args(argv)
    files = sorted(glob.glob(DETECTION_GLOB))
    set_a, set_b, per_run = [], [], {}
    with tempfile.TemporaryDirectory() as work:
        s82 = load_script_82(work)
        version = getattr(s82, "SCORING_VERSION", "7.2")
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
                                      "mcap": dx.get("marketCapUsd"), "liq": dx.get("liquidityUsd"),
                                      "pool": dx.get("pairAddress"), "price": dx.get("priceUsd"), "t0": t_score})
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

    # H2: ¿qué explica las ALERTAS (>= 70) del score recalculado?
    alerts = [r for r in set_a if r["recomputed"] >= 70]
    by_age = {}
    for r in set_a:
        b = by_age.setdefault(age_bucket(r["age_min"]), {"n": 0, "alerta_70": 0, "emite_56": 0})
        b["n"] += 1
        b["alerta_70"] += r["recomputed"] >= 70
        b["emite_56"] += r["recomputed"] >= 56
    young_saturated = sum(1 for r in alerts if r["age_min"] is not None and r["age_min"] < 60
                          and r["vol_ratio"] is not None and r["vol_ratio"] >= 0.9)
    reason_freq = Counter(reason for r in alerts for reason in r["reasons"])
    low_fund = sum(1 for r in alerts if "MCap bajo" in r["reasons"] and "Volumen bajo" in r["reasons"])

    # Contrafáctico v7.2 (solo tiene sentido si el scorer actual es v7.2): bonos de aceleración con edad >= 60 min.
    gated = []
    for r in set_a:
        s = r["recomputed"]
        if r["age_min"] is not None and r["age_min"] < 60:
            s = s - sum(v for k, v in ACCEL_BONUSES.items() if k in r["reasons"])
        r["gated"] = max(0, s)
        gated.append(r["gated"])
    fine_cf = {str(t): round(sum(g >= t for g in gated) / len(gated), 4) for t in FINE_THRESHOLDS} if gated else {}
    fine_current = {str(t): round(sum(s >= t for s in recomp) / len(recomp), 4) for t in FINE_THRESHOLDS} if recomp else {}

    legacy = [r["score"] for r in set_b]
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "hypotheses": {"H1": "umbral desactualizado tras bonos v7.2",
                       "H2": "inflación por tokens < 60 min con vol_m5/vol_h1 ≈ 1 por construcción"},
        "event_definitions": {"primary": "tocar +20% antes de caer −30% desde la entrada (calibración)",
                              "secondary": "cierre >= +20% a 48 h (público)",
                              "intra_candle_order": "open -> low -> high -> close (conservador)"},
        "data": {"files": len(files), "set_a_v72_complete": len(set_a), "set_a_runs": sorted(per_run),
                 "set_b_legacy": len(set_b), "set_b_with_dex": sum(r["has_dex"] for r in set_b)},
        "method": {"clock": f"timestamp de la corrida + {SCORING_DELAY_S}s", "bp_delta": "0 (sin _accumulated.json)",
                   "scorer": f"script_82_final_detection.score_token (árbol actual, versión {version})"},
        "current_scorer_version": version,
        "reproducibility_vs_production": {"exact_match": agree, "within_15": within15, "n": len(set_a),
                                          "note": "exacto esperado solo si el scorer actual es el de producción (v7.2)"},
        "set_a": {
            "stored_production_score_v72": {"histogram": histogram(stored), "rates": rate_table(stored),
                                            "median": statistics.median(stored) if stored else None},
            f"recomputed_v{version}": {"histogram": histogram(recomp), "rates": rate_table(recomp),
                                       "median": statistics.median(recomp) if recomp else None,
                                       "fine_sweep_rates": fine_current},
            "per_run_stored": per_run,
            "by_age_bucket": by_age,
            "alerts_70_recomputed": {"n": len(alerts), "young_and_saturated_ratio": young_saturated,
                                     "mcap_bajo_y_volumen_bajo": low_fund, "top_reasons": reason_freq.most_common(12)},
            "counterfactual_accel_gated_60m": {"rates": rate_table(gated), "histogram": histogram(gated),
                                               "fine_sweep_rates": fine_cf},
            "rows": [{k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items()
                      if k not in ("reasons", "pool", "price", "t0")} for r in set_a],
        },
        "set_b_legacy_v71": {"histogram": histogram(legacy), "rates": rate_table(legacy),
                             "median": statistics.median(legacy) if legacy else None},
        "target_rate": list(TARGET_RATE),
    }
    source = CandleSource(args.cache, offline=args.offline) if (args.outcomes_sample > 0 or args.outcomes_set_a) else None
    if args.outcomes_set_a:
        print(f"[INFO] métrica dual, Conjunto A (censurado): GeckoTerminal, {GT_INTERVAL_S}s entre llamadas", flush=True)
        summary, rows = outcome_study_set_a(set_a, source, version)
        report["outcomes_set_a"] = summary
        report["outcome_rows_set_a"] = rows
    if args.outcomes_sample > 0:
        print(f"[INFO] métrica dual, legado: hasta {args.outcomes_sample} tokens por bucket", flush=True)
        summary, rows = outcome_study_legacy(set_b, args.outcomes_sample, source)
        report["outcomes_legacy_v71"] = summary
        report["outcome_rows_legacy"] = rows
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[OK] {out}")
    print(f"Scorer actual: v{version} · Conjunto A: n={len(set_a)} en {len(per_run)} corridas · Legado: n={len(set_b)}")
    print(f"Coincidencia con producción (v7.2): exacto {agree}/{len(set_a)} · |Δ|<=15: {within15}/{len(set_a)}")
    for name, sc in (("v7.2 producción (guardado)", stored), (f"v{version} recalculado", recomp),
                     ("contrafáctico gate (sobre recalculado)", gated), ("v7.1 legado", legacy)):
        rt = rate_table(sc)
        print(f"  {name:<40} " + "  ".join(f">={t}: {rt[str(t)]['rate']:.1%}" for t in THRESHOLDS if rt[str(t)]['rate'] is not None))
    print(f"Barrido fino v{version}: {fine_current}")
    print("Por edad:", {k: f"≥70 {v['alerta_70']} · ≥56 {v['emite_56']} / {v['n']}" for k, v in sorted(by_age.items())})
    oa = report.get("outcomes_set_a")
    if oa:
        print(f"Conjunto A resultados: {oa['status_counts']} · 48h completas: {oa['complete_48h']}")
        for lbl, key in (("v7.2 prod", "precision_v72_prod"), (f"v{version}", f"precision_v{version}")):
            for t in ("all", "56", "70"):
                print(f"   {lbl:<9} >= {t:<4} {fmt_prec(oa[key][t])}")
    ol = report.get("outcomes_legacy_v71")
    if ol:
        print(f"Legado resultados: {ol['status_counts']} · rug {ol['rug_48h']} · primaria-hit con rug: {ol['primary_hit_and_rug']} · "
              f"velas ambiguas: {ol['ambiguous_candles_total']} · AUC prim {ol['auc_primary']} · AUC sec {ol['auc_secondary']} · "
              f"base poblacional primaria {ol['population_weighted_primary_rate']}")
        for t in ("all", "50", "56", "70"):
            print(f"   excl. sin velas >= {t:<4} {fmt_prec(ol['precision_excluding_no_candles'][t])}")
            print(f"   sin velas=miss  >= {t:<4} {fmt_prec(ol['precision_no_candles_as_miss'][t])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
