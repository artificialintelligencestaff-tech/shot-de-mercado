#!/usr/bin/env python3
"""
young_watch_analysis.py — Cobertura de tokens jóvenes en el early watch (Fase 12 / D-014-R, entregable 3).
Solo lectura. Sin outcome: describe qué se vio, no si funcionó.

Fuente: el historial de git de 02_Analisis/early/_watch_{a,b}.json (cada commit es un snapshot del poll) o, con
--current, solo los archivos actuales. De cada snapshot se usa:
  · top: las 15 mejores filas del poll (score v7.2.1 + bono, señales activas, edad). SESGO: es el top por score,
    no la población; sirve para "cuántos de los mejores activan >= 3 señales", no para la distribución completa.
  · state.liquidity: serie de liquidez (DexScreener) de TODOS los tokens vigilados; con watch[mint].since (momento
    en que el listener vio el lanzamiento ≈ creación) da la liquidez por edad para la población entera.

Salida: 02_Analisis/diagnostics/young_watch_analysis.json + resumen por consola.

Uso: python 04_Config/scripts/young_watch_analysis.py [--current] [--max-commits 200] [--root DIR]
"""
import argparse
import json
import os
import statistics
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
WATCH_FILES = ("02_Analisis/early/_watch_a.json", "02_Analisis/early/_watch_b.json")
YOUNG_MAX_MIN = 30
SCOPE_MAX_MIN = 60
LIQ_MIN_USD = 20_000
SCORE_BUCKETS = (0, 10, 20, 30, 40, 50, 56, 60, 70, 80, 101)


def parse_iso(value):
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None
    return (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).timestamp()


def bucket(score, edges=SCORE_BUCKETS):
    for lo, hi in zip(edges, edges[1:]):
        if lo <= score < hi:
            return f"{lo}-{hi - 1}"
    return "n/d"


def git_snapshots(root, rel, max_commits=200, run=subprocess.run):
    """[(commit, json)] del historial de `rel` (más viejo primero)."""
    r = run(["git", "log", f"-{max_commits}", "--format=%H", "--", rel], cwd=str(root), capture_output=True,
            text=True)
    out = []
    for sha in reversed(r.stdout.split() if r.returncode == 0 else []):
        s = run(["git", "show", f"{sha}:{rel}"], cwd=str(root), capture_output=True, text=True)
        if s.returncode == 0:
            try:
                out.append((sha[:8], json.loads(s.stdout)))
            except ValueError:
                continue
    return out


def collect(snapshots):
    """Filas del top (dedup por mint+updated_at) y liquidez por mint (unión de series)."""
    rows, seen, liq, since = [], set(), defaultdict(dict), {}
    for _, snap in snapshots:
        at = snap.get("updated_at")
        for t in snap.get("top") or []:
            key = (t.get("mint"), at)
            if key in seen or not t.get("mint"):
                continue
            seen.add(key)
            rows.append(dict(t, at=at, instance=snap.get("instance")))
        for mint, w in (snap.get("watch") or {}).items():
            if w.get("since") and mint not in since:
                since[mint] = parse_iso(w["since"])
        for mint, series in ((snap.get("state") or {}).get("liquidity") or {}).items():
            for ts, v in series or []:
                liq[mint][round(ts)] = v
    return rows, liq, since


def score_distribution(rows, max_age=YOUNG_MAX_MIN):
    """Por mint, el mejor score BASE (v7.2.1) observado con edad < max_age (sólo filas del top)."""
    best = {}
    for r in rows:
        age = r.get("age_min")
        if age is None or age >= max_age or r.get("base") is None:
            continue
        best[r["mint"]] = max(best.get(r["mint"], -1), r["base"])
    vals = sorted(best.values())
    return {"n_mints": len(vals), "buckets": dict(Counter(bucket(v) for v in vals)),
            "median": statistics.median(vals) if vals else None, "max": max(vals) if vals else None,
            "ge_56": sum(v >= 56 for v in vals), "ge_50": sum(v >= 50 for v in vals)}


def signal_coverage(rows, max_age=SCOPE_MAX_MIN):
    """Señales activas por fila (top) en tokens < max_age: cuántas filas / mints llegan a >= 2 / >= 3."""
    young = [r for r in rows if r.get("age_min") is not None and r["age_min"] < max_age]
    n_active = [len(r.get("active") or []) for r in young]
    by_signal = Counter(s for r in young for s in r.get("active") or [])
    mints3 = {r["mint"] for r in young if len(r.get("active") or []) >= 3}
    mints3_young = {r["mint"] for r in young if len(r.get("active") or []) >= 3 and r["age_min"] < YOUNG_MAX_MIN}
    return {"n_rows": len(young), "n_mints": len({r["mint"] for r in young}),
            "rows_by_n_active": dict(sorted(Counter(n_active).items())),
            "rows_ge3": sum(n >= 3 for n in n_active), "mints_ge3": len(mints3),
            "mints_ge3_lt30min": len(mints3_young), "by_signal": dict(by_signal.most_common())}


def liquidity_by_age(liq, since, max_age=SCOPE_MAX_MIN, liq_min=LIQ_MIN_USD):
    """Población entera: por mint con 'since', liquidez máxima vista antes de max_age y si superó liq_min."""
    out = {"n_mints": 0, "liq_zero_always": 0, "liq_gt_min": 0, "liq_gt_min_lt30": 0, "first_cross_age_min": []}
    for mint, pts in liq.items():
        t0 = since.get(mint)
        if t0 is None:
            continue
        young = sorted((ts, v) for ts, v in pts.items() if 0 <= (ts - t0) / 60 < max_age)
        if not young:
            continue
        out["n_mints"] += 1
        vals = [v or 0 for _, v in young]
        if max(vals) <= 0:
            out["liq_zero_always"] += 1
        cross = next(((ts - t0) / 60 for ts, v in young if (v or 0) > liq_min), None)
        if cross is not None:
            out["liq_gt_min"] += 1
            out["first_cross_age_min"].append(round(cross, 1))
            out["liq_gt_min_lt30"] += cross < YOUNG_MAX_MIN
    ages = out.pop("first_cross_age_min")
    out["first_cross_age_median_min"] = statistics.median(ages) if ages else None
    return out


def run(root=None, current=False, max_commits=200):
    root = Path(root or ROOT)
    snaps = []
    for rel in WATCH_FILES:
        if current:
            p = root / rel
            if p.exists():
                snaps.append(("current", json.loads(p.read_text(encoding="utf-8"))))
        else:
            snaps += git_snapshots(root, rel, max_commits)
    rows, liq, since = collect(snaps)
    ats = sorted(parse_iso(s.get("updated_at")) or 0 for _, s in snaps)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "archivos actuales" if current else f"historial git de {', '.join(WATCH_FILES)}",
        "snapshots": len(snaps),
        "window": [datetime.fromtimestamp(ats[0], timezone.utc).isoformat(timespec="minutes"),
                   datetime.fromtimestamp(ats[-1], timezone.utc).isoformat(timespec="minutes")] if ats else None,
        "caveat": "top = 15 mejores por score de cada poll (sesgado hacia scores altos); la liquidez es de la "
                  "población entera vigilada. Sin outcome.",
        "score_v721_lt30min_top": score_distribution(rows),
        "signals_lt60min_top": signal_coverage(rows),
        "liquidity_lt60min_population": liquidity_by_age(liq, since),
    }


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--current", action="store_true")
    ap.add_argument("--max-commits", type=int, default=200)
    ap.add_argument("--root")
    ap.add_argument("--out")
    args = ap.parse_args(argv)
    root = Path(args.root or ROOT)
    report = run(root, args.current, args.max_commits)
    out = Path(args.out or root / "02_Analisis" / "diagnostics" / "young_watch_analysis.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "caveat"}, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
