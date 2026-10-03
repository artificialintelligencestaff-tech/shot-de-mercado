#!/usr/bin/env python3
"""
early_review.py — Revisión de la vigilancia temprana (Fase 10b). Cada 6 h (early_review.yml) o manual.

1. Edad mínima de emisión (decisión de Dirección, 10b): el early watch emite desde los 10 min de edad.
   Monitoreo: primaria (+20 % antes de −30 %, 48 h; calibrate_threshold_v72.evaluate_outcome con velas de 15 min
   de GeckoTerminal) de las alertas tempranas emitidas con gate <= 10. Cuando pasaron >= 24 h desde la primera
   y hay >= MIN_RESOLVED primarias resueltas: si la tasa es < 40 % -> 02_Analisis/early/_gate.json con
   early_min_age_min = 15 (script_116 lo lee en cada poll). La suba es pegajosa: nunca se baja sola.
2. Cobertura de PumpPortal: unión de los intervalos de conexión (listener_intervals) de las instancias
   (_watch_<inst>.json) en las últimas 24 h, total y por instancia.

Salida: 02_Analisis/diagnostics/early_review.json (+ _gate.json si cambia). Bitácora lib_persist "early_review".

Uso: python 04_Config/scripts/early_review.py [--offline] [--cache velas.json] [--dry-run]
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
VERSION = "review-1.0"
EARLY_DIR_REL = "02_Analisis/early"
TRIAL_GATE_MAX = 10          # alertas emitidas con edad mínima <= 10 min
TRIAL_HOURS = 24
PRIMARY_MIN = 0.40
RAISE_TO = 15
MIN_RESOLVED = 5             # sin al menos 5 primarias resueltas no se decide (se informa)
COVERAGE_HOURS = 24


def iso(epoch):
    return datetime.fromtimestamp(epoch, timezone.utc).isoformat(timespec="seconds") if epoch is not None else None


def alert_epoch(ts):
    try:
        return datetime.strptime(ts, "%Y-%m-%d_%H%M%S").replace(tzinfo=timezone.utc).timestamp()
    except (TypeError, ValueError):
        return None


def read_json(path, default):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


# ---------------------------------------------------------------------------
# Cobertura
# ---------------------------------------------------------------------------

def union_seconds(intervals, t_from, t_to):
    """Segundos cubiertos por la unión de [inicio, fin] recortada a [t_from, t_to]."""
    clipped = sorted((max(a, t_from), min(b, t_to)) for a, b in intervals if b > t_from and a < t_to and b > a)
    total, cur_a, cur_b = 0.0, None, None
    for a, b in clipped:
        if cur_b is None or a > cur_b:
            if cur_b is not None:
                total += cur_b - cur_a
            cur_a, cur_b = a, b
        else:
            cur_b = max(cur_b, b)
    if cur_b is not None:
        total += cur_b - cur_a
    return total


def coverage(by_instance, now, hours=COVERAGE_HOURS):
    t_from = now - hours * 3600
    span = hours * 3600
    out = {"window_h": hours, "from": iso(t_from), "to": iso(now), "by_instance": {}}
    allv = []
    for inst, intervals in sorted(by_instance.items()):
        out["by_instance"][inst] = round(union_seconds(intervals, t_from, now) / span, 4)
        allv += intervals
    out["union"] = round(union_seconds(allv, t_from, now) / span, 4)
    out["reference_script_82"] = 0.25      # 5 min de escucha cada 20 min
    return out


def load_intervals(root):
    out = {}
    for path in sorted((Path(root) / EARLY_DIR_REL).glob("_watch_*.json")):
        data = read_json(path, {})
        inst = data.get("instance") or path.stem.split("_")[-1]
        out[inst] = [i for i in data.get("listener_intervals") or [] if isinstance(i, list) and len(i) == 2]
    return out


# ---------------------------------------------------------------------------
# Edad mínima
# ---------------------------------------------------------------------------

def early_records(root):
    root = Path(root)
    recs = []
    legacy = read_json(root / EARLY_DIR_REL / "_early_alerts.json", [])
    recs += [r for r in legacy if isinstance(r, dict)] if isinstance(legacy, list) else []
    for path in sorted((root / EARLY_DIR_REL / "alerts").glob("*.json")):
        r = read_json(path, None)
        if isinstance(r, dict):
            recs.append(r)
    return recs


def trial_rows(root, gate_max=TRIAL_GATE_MAX):
    rows = []
    for r in early_records(root):
        gate = r.get("gate_min")
        if not isinstance(gate, (int, float)) or gate > gate_max:
            continue
        detail = read_json(Path(root) / "02_Analisis" / "alerts" / f"alert_{r.get('mint')}_{r.get('timestamp')}.json", {})
        dx = detail.get("dexscreener") or {}
        rows.append({"mint": r.get("mint"), "symbol": r.get("symbol"), "alert_ts": r.get("timestamp"),
                     "t0": alert_epoch(r.get("timestamp")), "price": r.get("initial_price"),
                     "pool": dx.get("pairAddress"), "gate_min": gate, "age_min_at_alert": r.get("age_min_at_alert"),
                     "score": r.get("score"), "early_bonus": r.get("early_bonus")})
    return rows


def h0_rows(root):
    """Alertas del scorer joven con subtotales (D-014-R-5), para la H-0 pre-registrada (doc 32 §6)."""
    rows = []
    for r in early_records(root):
        if r.get("h0_group") not in ("info_ge20", "info_lt20"):
            continue
        detail = read_json(Path(root) / "02_Analisis" / "alerts" / f"alert_{r.get('mint')}_{r.get('timestamp')}.json", {})
        rows.append({"mint": r.get("mint"), "symbol": r.get("symbol"), "alert_ts": r.get("timestamp"),
                     "t0": alert_epoch(r.get("timestamp")), "price": r.get("initial_price"),
                     "pool": (detail.get("dexscreener") or {}).get("pairAddress"), "h0_group": r["h0_group"],
                     "info_score": r.get("info_score"), "struct_score": r.get("struct_score"),
                     "pv_score": r.get("pv_score")})
    return rows


def fisher_one_sided(k1, n1, k2, n2):
    """P(X >= k1) con X hipergeométrica (márgenes fijos): ¿la tasa del grupo 1 supera a la del 2?"""
    from math import comb
    K, N = k1 + k2, n1 + n2
    total = comb(N, K)
    return sum(comb(n1, x) * comb(n2, K - x) for x in range(k1, min(n1, K) + 1)) / total if total else 1.0


H0_MIN_N = 40
H0_ALPHA = 0.10


def evaluate_h0(rows, min_n=H0_MIN_N, alpha=H0_ALPHA):
    """H-0 (pre-registrada 2026-10-02): la tasa primaria con info_score >= 20 NO supera a la de < 20.
    Se decide con n >= 40 primarias resueltas en total; Fisher exacto a una cola, alfa 0,10. H-0 se rechaza (lo
    informacional discrimina) solo si p < alfa."""
    groups = {}
    for g in ("info_ge20", "info_lt20"):
        res = [r for r in rows if r["h0_group"] == g and r.get("primary") in ("hit", "miss")]
        k = sum(r["primary"] == "hit" for r in res)
        groups[g] = {"n": len(res), "k_hit": k, "rate": round(k / len(res), 4) if res else None}
    n = groups["info_ge20"]["n"] + groups["info_lt20"]["n"]
    out = {"hypothesis": "H-0: info_score >= 20 no supera a info_score < 20 en tasa primaria (tokens < 60 min)",
           "min_n": min_n, "alpha": alpha, "n_resolved": n, "groups": groups}
    if n < min_n or not groups["info_ge20"]["n"] or not groups["info_lt20"]["n"]:
        return dict(out, verdict="pendiente")
    p = fisher_one_sided(groups["info_ge20"]["k_hit"], groups["info_ge20"]["n"],
                         groups["info_lt20"]["k_hit"], groups["info_lt20"]["n"])
    return dict(out, p_value=round(p, 4), verdict="H-0 rechazada" if p < alpha else "H-0 no rechazada")


def measure(rows, source, now):
    import calibrate_threshold_v72 as cal
    for r in rows:
        if not (r["pool"] and r["price"] and r["t0"]):
            r.update(status="sin_datos_de_entrada", primary="sin_datos")
            continue
        status, candles = source.get(r["pool"], r["t0"])
        if status == "ok":
            out = cal.evaluate_outcome(candles, r["price"], r["t0"], now)
            r.update(status="ok", primary=out["primary"], max_ret=out["max_ret"], min_ret=out["min_ret"])
        else:
            r.update(status=status, primary="sin_datos")
    return rows


def decide(rows, gate, now, trial_hours=TRIAL_HOURS, primary_min=PRIMARY_MIN, min_resolved=MIN_RESOLVED,
           raise_to=RAISE_TO):
    """Devuelve (decisión, nuevo gate o None). La suba es pegajosa: si _gate.json ya la tiene, no se toca."""
    resolved = [r for r in rows if r.get("primary") in ("hit", "miss")]
    k = sum(r["primary"] == "hit" for r in resolved)
    rate = k / len(resolved) if resolved else None
    starts = [r["t0"] for r in rows if r.get("t0")]
    elapsed_h = (now - min(starts)) / 3600 if starts else 0.0
    info = {"n_alerts": len(rows), "n_resolved": len(resolved), "k_hit": k,
            "rate": round(rate, 4) if rate is not None else None, "elapsed_h": round(elapsed_h, 1),
            "criterion": f"primaria < {primary_min:.0%} tras {trial_hours} h -> gate {raise_to} min",
            "current_gate": gate.get("early_min_age_min", TRIAL_GATE_MAX)}
    if (gate.get("early_min_age_min") or 0) >= raise_to:
        return dict(info, decision="ya_subido"), None
    if elapsed_h < trial_hours:
        return dict(info, decision="en_prueba"), None
    if len(resolved) < min_resolved:
        return dict(info, decision="sin_datos_suficientes"), None
    if rate < primary_min:
        return dict(info, decision="subir"), raise_to
    return dict(info, decision="mantener"), None


def run(root=None, source=None, now=None, dry_run=False):
    root = Path(root or ROOT)
    now = now or time.time()
    gate_path = root / EARLY_DIR_REL / "_gate.json"
    gate = read_json(gate_path, {})
    rows = trial_rows(root)
    if source is not None:
        measure(rows, source, now)
    decision, new_gate = decide(rows, gate, now) if source is not None else ({"decision": "sin_medir"}, None)
    h0 = h0_rows(root)
    if source is not None:
        measure(h0, source, now)
    report = {"version": VERSION, "generated_at": iso(now), "gate": decision,
              "h0": evaluate_h0(h0) if source is not None else {"verdict": "sin_medir"},
              "coverage_pumpportal": coverage(load_intervals(root), now), "rows": rows}
    if new_gate and not dry_run:
        gate_path.parent.mkdir(parents=True, exist_ok=True)
        gate_path.write_text(json.dumps({"early_min_age_min": new_gate, "decided_at": iso(now),
                                         "by": "early_review.py", "evidence": decision}, indent=1,
                                        ensure_ascii=False) + "\n", encoding="utf-8")
    if not dry_run:
        out = root / "02_Analisis" / "diagnostics" / "early_review.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        try:
            import lib_persist
            lib_persist.log_operation("early_review", "early_review", [out] + ([gate_path] if new_gate else []),
                                      decision=decision.get("decision"),
                                      coverage=report["coverage_pumpportal"]["union"])
        except Exception:
            pass
    return report


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="solo caché de velas")
    ap.add_argument("--no-measure", action="store_true", help="solo cobertura")
    ap.add_argument("--cache", default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    source = None
    if not args.no_measure:
        import calibrate_threshold_v72 as cal
        source = cal.CandleSource(args.cache, offline=args.offline)
    report = run(ROOT, source, dry_run=args.dry_run)
    if source is not None:
        source.save()
    print(json.dumps({"gate": report["gate"], "coverage": report["coverage_pumpportal"]}, indent=1,
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
