#!/usr/bin/env python3
"""
monitor_shadow.py — Seguimiento diario de las alertas en modo sombra (métrica dual), solo lectura.

Para cada alerta status=shadow de _all_alerts.json recupera la foto del token al detectarlo
(alert_{mint}_{timestamp}.json: detected_at, scoring_version, dexscreener) y mide:
  - primaria: tocar +20% antes de caer −30% (censurada hasta tocar una barrera)
  - secundaria: cierre >= +20% a 48 h (pendiente hasta cumplir 48 h)
  - exposición: alertas sobre tokens de < 60 min al detectar
  - frescura: minutos entre detected_at y la alerta (R1 exige <= 60)
Criterios de validación de v7.2.1 (Dirección, 30/09), con n resuelto >= 20:
  primaria >= 30% y cota inferior del IC90 > 15% · secundaria >= 5% y cota inferior > 2% · exposición < 20%.
Entrada = precio de DexScreener al detectar (initial_price); t0 = detected_at (o timestamp de la alerta).
Salida: 02_Analisis/diagnostics/shadow_monitor.json + bloque "DÍA N" por versión de scorer.

Uso: python 04_Config/scripts/monitor_shadow.py [--version 7.2.1] [--cache velas.json] [--offline]
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import calibrate_threshold_v72 as cal  # noqa: E402

ROOT = Path(os.environ.get("SHOT_ROOT") or Path(__file__).resolve().parents[2])
ALERTS_DIR = ROOT / "02_Analisis" / "alerts"
OUT_FILE = ROOT / "02_Analisis" / "diagnostics" / "shadow_monitor.json"
YOUNG_MIN = 60
CRITERIA = {"min_n": 20, "primary_rate": 0.30, "primary_ci_lo": 0.15, "secondary_rate": 0.05,
            "secondary_ci_lo": 0.02, "max_young_share": 0.20, "baseline_primary": 0.105}


def epoch(ts):
    if not ts:
        return None
    try:
        if "T" in ts:
            return datetime.fromisoformat(ts).timestamp()
        return datetime.strptime(ts, "%Y-%m-%d_%H%M%S").replace(tzinfo=timezone.utc).timestamp()
    except ValueError:
        return None


def snapshot(alert):
    path = ALERTS_DIR / f"alert_{alert['mint']}_{alert['timestamp']}.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def collect(version_filter=None):
    alerts = json.loads((ALERTS_DIR / "_all_alerts.json").read_text(encoding="utf-8"))
    rows = []
    for a in alerts:
        if a.get("status") != "shadow":
            continue
        snap = snapshot(a)
        dx = snap.get("dexscreener") or snap.get("dx") or {}
        version = snap.get("scoring_version") or "7.2-preR1"
        if version_filter and version != version_filter:
            continue
        t_alert = epoch(a["timestamp"])
        t_det = epoch(snap.get("detected_at"))
        created = dx.get("pairCreatedAt")
        age_min = (t_det - created / 1000) / 60 if (t_det and created) else None
        rows.append({"mint": a["mint"], "symbol": a.get("symbol"), "alert_ts": a["timestamp"], "version": version,
                     "score": a.get("score"), "pool": dx.get("pairAddress"), "price": a.get("initial_price"),
                     "t0": t_det or t_alert, "age_min_at_detection": round(age_min, 1) if age_min is not None else None,
                     "staleness_min": round((t_alert - t_det) / 60, 1) if (t_det and t_alert) else None,
                     "telegram_sent": a.get("telegram_sent")})
    return rows


OUTCOME_FIELDS = ("status", "primary", "secondary", "complete", "ambiguous_candles", "n_candles",
                  "max_ret", "min_ret", "last_ret")


def row_key(r):
    return f"{r['mint']}@{r['alert_ts']}"


def is_final(r):
    """Fila con resultado definitivo: ambas métricas resueltas (48 h cumplidas) o sin datos de entrada."""
    return r.get("status") == "sin_datos_de_entrada" or (
        r.get("status") in ("ok", "sin_velas") and r.get("primary") in ("hit", "miss")
        and r.get("secondary") in ("hit", "miss"))


def measure(rows, source, previous=None, max_calls=None):
    """Mide la métrica dual. `previous`: filas del reporte anterior (se reutilizan las definitivas, sin API).
    `max_calls`: tope de consultas por corrida; lo que excede queda 'pendiente_de_medicion' (próxima corrida)."""
    now = time.time()
    prev = {row_key(r): r for r in (previous or []) if isinstance(r, dict) and "alert_ts" in r}
    calls = 0
    for r in rows:
        old = prev.get(row_key(r))
        if old and is_final(old):
            r.update({k: old[k] for k in OUTCOME_FIELDS if k in old}, reused=True)
            continue
        if not (r["pool"] and r["price"] and r["t0"]):
            r.update(status="sin_datos_de_entrada", primary="sin_datos", secondary="sin_datos")
            continue
        if max_calls is not None and calls >= max_calls:
            r.update(status="pendiente_de_medicion", primary="pending", secondary="pending")
            continue
        calls += 1
        status, candles = source.get(r["pool"], r["t0"])
        if status == "ok":
            r.update(cal.evaluate_outcome(candles, r["price"], r["t0"], now), status="ok" if candles else "sin_velas")
        else:
            r.update(status=status, primary="sin_datos", secondary="sin_datos")
    source.save()
    return rows


def summarize(rows):
    measured = [r for r in rows if r["status"] in ("ok", "sin_velas")]
    prim = cal.precision_block(measured, "primary")
    sec = cal.precision_block(measured, "secondary")
    known_age = [r for r in rows if r["age_min_at_detection"] is not None]
    young = sum(r["age_min_at_detection"] < YOUNG_MIN for r in known_age)
    stale = sum(1 for r in rows if r["staleness_min"] is None or r["staleness_min"] > 60)
    first = min((epoch(r["alert_ts"]) for r in rows), default=None)
    day = int((time.time() - first) // 86400) + 1 if first else 0
    verdict = {}
    if prim["n_resolved"] >= CRITERIA["min_n"]:
        verdict["primary"] = bool(prim["rate"] >= CRITERIA["primary_rate"] and prim["ci90"][0] > CRITERIA["primary_ci_lo"])
    if sec["n_resolved"] >= CRITERIA["min_n"]:
        verdict["secondary"] = bool(sec["rate"] >= CRITERIA["secondary_rate"] and sec["ci90"][0] > CRITERIA["secondary_ci_lo"])
    if known_age:
        verdict["exposure_young"] = young / len(known_age) < CRITERIA["max_young_share"]
    return {"day": day, "n_alerts": len(rows), "telegram_sent_true": sum(1 for r in rows if r["telegram_sent"]),
            "status_counts": {s: sum(r["status"] == s for r in rows) for s in sorted({r["status"] for r in rows})},
            "primary": prim, "secondary": sec,
            "young_lt_60m": {"k": young, "n_known_age": len(known_age),
                             "share": round(young / len(known_age), 4) if known_age else None},
            "stale_or_undated": stale, "criteria": CRITERIA, "verdict_partial": verdict}


def block(version, s):
    p, q, y = s["primary"], s["secondary"], s["young_lt_60m"]
    return (f"DÍA {s['day']} — scorer v{version}\n"
            f"- Alertas shadow acumuladas: {s['n_alerts']} (enviadas a Telegram: {s['telegram_sent_true']}; "
            f"viejas o sin fecha: {s['stale_or_undated']})\n"
            f"- Primaria resueltas (tocó +20% antes de −30%): {p['k_hit']}/{p['n_resolved']} "
            f"({p['rate'] if p['rate'] is not None else '—'}, IC90 {p['ci90']})\n"
            f"- Primaria pendientes: {p['pending']}\n"
            f"- Secundarias resueltas (cierre ≥ +20% a 48 h): {q['k_hit']}/{q['n_resolved']} "
            f"({q['rate'] if q['rate'] is not None else '—'}, IC90 {q['ci90']})\n"
            f"- Secundarias pendientes: {q['pending']}\n"
            f"- Alertas en tokens < 60 min: {y['k']}/{y['n_known_age']} ({y['share']}) (objetivo < 20%)\n"
            f"- Estados: {s['status_counts']} · veredicto parcial: {s['verdict_partial'] or 'n < 20'}")


VERDICT_VERSION = "7.2.1"


def record_cycle(report, cycle_log, dry_run=False, notify=None):
    """Registra el DÍA N por versión en _cycle_log.json (clave shadow_monitor, una entrada por día y versión)
    y, si la versión validada alcanza n >= 20 primarias resueltas, avisa el veredicto UNA vez (clave
    shadow_verdict:<versión>). Devuelve el estado del aviso."""
    log = cal_read(cycle_log)
    days = log.setdefault("shadow_monitor", [])
    today = datetime.now(timezone.utc).date().isoformat()
    for version, s in report["by_version"].items():
        entry = {"date": today, "version": version, "day": s["day"], "n_alerts": s["n_alerts"],
                 "primary": {k: s["primary"][k] for k in ("k_hit", "n_resolved", "pending", "rate", "ci90")},
                 "secondary": {k: s["secondary"][k] for k in ("k_hit", "n_resolved", "pending", "rate", "ci90")},
                 "young_share": s["young_lt_60m"]["share"], "verdict_partial": s["verdict_partial"]}
        days[:] = [d for d in days if not (d.get("date") == today and d.get("version") == version)] + [entry]
    notified = "not_needed"
    s = report["by_version"].get(VERDICT_VERSION)
    key = f"shadow_verdict:{VERDICT_VERSION}"
    if s and s["primary"]["n_resolved"] >= CRITERIA["min_n"] and key not in log.get("verdicts", {}):
        v = s["verdict_partial"]
        passed = v.get("primary") is True and v.get("exposure_young") is True and v.get("secondary", True) is True
        text = (f"⚖️ Veredicto v{VERDICT_VERSION} en sombra (n primaria = {s['primary']['n_resolved']})\n"
                f"Primaria: {s['primary']['k_hit']}/{s['primary']['n_resolved']} = {s['primary']['rate']} IC90 {s['primary']['ci90']} "
                f"(criterio ≥ {CRITERIA['primary_rate']} con IC90 inf > {CRITERIA['primary_ci_lo']})\n"
                f"Secundaria: {s['secondary']['k_hit']}/{s['secondary']['n_resolved']} (pend {s['secondary']['pending']})\n"
                f"Exposición < 60 min: {s['young_lt_60m']['share']} (criterio < {CRITERIA['max_young_share']})\n"
                f"Resultado: {'CUMPLE' if passed else 'NO CUMPLE'} los criterios disponibles. "
                f"La decisión de reactivar emisiones es de Dirección.")
        notified = (notify or (lambda t, dry_run=False: "skipped_no_notifier"))(text, dry_run=dry_run)
        log.setdefault("verdicts", {})[key] = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                               "passed": passed, "summary": s["verdict_partial"], "notified": notified}
    log["last_updated"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if not dry_run:
        tmp = Path(str(cycle_log) + ".tmp")
        tmp.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")
        os.replace(tmp, cycle_log)
    return notified


def cal_read(path):
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Monitoreo diario de alertas en sombra (métrica dual)")
    ap.add_argument("--version", default=None, help="solo este scoring_version (p.ej. 7.2.1); por defecto todas")
    ap.add_argument("--include-pre-r1", action="store_true", help="incluir alertas sin detected_at (atraso pre-R1)")
    ap.add_argument("--cache", default=None)
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--incremental", action="store_true", help="reusar filas definitivas del reporte anterior")
    ap.add_argument("--max-calls", type=int, default=None, help="tope de consultas a la API por corrida")
    ap.add_argument("--cycle-log", action="store_true", help="registrar DÍA N (y veredicto) en _cycle_log.json")
    ap.add_argument("--notify", action="store_true", help="avisar el veredicto al chat de operaciones")
    ap.add_argument("--dry-run", action="store_true", help="no escribe el cycle log ni envía avisos")
    ap.add_argument("--record-only", action="store_true",
                    help="no mide: toma el reporte de --out y solo registra el DÍA N (lo usa el bot tras rebasar)")
    ap.add_argument("--notified-previous", action="store_true",
                    help="el veredicto ya se avisó en un intento anterior del bot: registrarlo sin reenviar")
    ap.add_argument("--out", default=str(OUT_FILE))
    args = ap.parse_args(argv)
    if args.record_only:
        report = cal_read(args.out)
        if not report.get("by_version"):
            print(f"[cycle_log] {args.out} sin by_version: nada que registrar")
            return 0
        return log_cycle(report, args)
    rows = collect(args.version)
    if not args.include_pre_r1:
        rows = [r for r in rows if r["version"] != "7.2-preR1"]
    previous = cal_read(args.out).get("rows") if args.incremental else None
    rows = measure(rows, cal.CandleSource(args.cache, offline=args.offline), previous, args.max_calls)
    report = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "by_version": {}, "rows": rows,
              "measured_this_run": sum(1 for r in rows if not r.get("reused") and r["status"] != "pendiente_de_medicion")}
    for version in sorted({r["version"] for r in rows}):
        s = summarize([r for r in rows if r["version"] == version])
        report["by_version"][version] = s
        print(block(version, s) + "\n")
    if not rows:
        print("Sin alertas shadow" + (f" de la versión {args.version}" if args.version else ""))
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[OK] {out}")
    return log_cycle(report, args) if args.cycle_log else 0


def log_cycle(report, args):
    notifier = None
    if args.notified_previous:
        notifier = lambda text, dry_run=False: "sent_previous_attempt"  # noqa: E731
    elif args.notify:
        import lib_ops
        notifier = lib_ops.send_ops_telegram
    status = record_cycle(report, ALERTS_DIR / "_cycle_log.json", dry_run=args.dry_run, notify=notifier)
    print(f"[cycle_log] DÍA registrado · veredicto: {status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
