#!/usr/bin/env python3
"""
bot_health_check.py — Bot gemelo de fallas silenciosas (cron cada 2 h). Solo lectura de la API de GitHub.

Problemas que detecta:
  - consecutive_failures: >= 2 fallas seguidas en los últimos runs completos de un workflow activo.
  - pipeline_stale: pipeline_t0 sin un run exitoso en las últimas 2 h (corre cada 20 min).
  - no_detections_6h: ningún detection_*.json nuevo en 6 h (el pipeline no produce).
  - no_alerts_24h (informativo): ninguna alerta (activa o sombra) en 24 h. Con v7.2.1 + edad >= 30 min +
    umbral 56 el volumen esperado es bajo, por eso no se usa "0 alertas en 6 h" (daría falsas alarmas).
Registra cada chequeo en 02_Analisis/_health_log.json y avisa por Telegram (chat de operaciones) SOLO
cuando cambia el conjunto de problemas, para no repetir el mismo aviso cada 2 h.

Uso: python 04_Config/scripts/bot_health_check.py [--dry-run]
"""
import argparse
import glob
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_ops  # noqa: E402

LOG_FILE = lib_ops.ROOT / "02_Analisis" / "_health_log.json"
ALERTS_FILE = lib_ops.ROOT / "02_Analisis" / "alerts" / "_all_alerts.json"
DETECTION_GLOB = str(lib_ops.ROOT / "01_Datos_Crudos" / "final_detection" / "detection_*.json")
CONSECUTIVE_FAILURES = 2
PIPELINE_MAX_GAP = timedelta(hours=2)
NO_DETECTIONS_WINDOW = timedelta(hours=6)
NO_ALERTS_WINDOW = timedelta(hours=24)


def parse_ts(value):
    try:
        if "T" in value:
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        return datetime.strptime(value, "%Y-%m-%d_%H%M%S").replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return None


def active_workflows(api):
    data = api("repos/{repo}/actions/workflows?per_page=100".format(repo=lib_ops.REPO))
    return [w["path"].rsplit("/", 1)[-1] for w in data.get("workflows", []) if w.get("state") == "active"]


def check_workflows(api, runs_fn, now):
    status, problems = {}, []
    for wf in active_workflows(api):
        runs = [r for r in runs_fn(wf) if r["status"] == "completed"]
        streak = 0
        for r in runs:
            if r["conclusion"] == "failure":
                streak += 1
            elif r["conclusion"] in ("success", "skipped", "neutral"):
                break
        last_ok = next((r["created_at"] for r in runs if r["conclusion"] == "success"), None)
        status[wf] = {"last_conclusion": runs[0]["conclusion"] if runs else None,
                      "consecutive_failures": streak, "last_success_at": last_ok, "runs_seen": len(runs)}
        if streak >= CONSECUTIVE_FAILURES:
            problems.append({"type": "consecutive_failures", "workflow": wf, "count": streak})
        if wf == "pipeline_t0.yml":
            ok_at = parse_ts(last_ok) if last_ok else None
            if ok_at is None or now - ok_at > PIPELINE_MAX_GAP:
                problems.append({"type": "pipeline_stale", "workflow": wf, "last_success_at": last_ok})
    return status, problems


def check_data(now):
    problems, info = [], {}
    stamps = [parse_ts(Path(f).stem.replace("detection_", "")) for f in glob.glob(DETECTION_GLOB)]
    stamps = [s for s in stamps if s]
    last_det = max(stamps) if stamps else None
    info["last_detection_at"] = last_det.isoformat() if last_det else None
    if last_det is None or now - last_det > NO_DETECTIONS_WINDOW:
        problems.append({"type": "no_detections_6h", "last_detection_at": info["last_detection_at"]})
    alerts = lib_ops.read_json(ALERTS_FILE, []) or []
    alert_ts = [parse_ts(a.get("timestamp")) for a in alerts if isinstance(a, dict)]
    alert_ts = [t for t in alert_ts if t]
    last_alert = max(alert_ts) if alert_ts else None
    info["last_alert_at"] = last_alert.isoformat() if last_alert else None
    info["alerts_last_24h"] = sum(1 for t in alert_ts if now - t <= NO_ALERTS_WINDOW)
    if info["alerts_last_24h"] == 0:
        problems.append({"type": "no_alerts_24h", "severity": "info", "last_alert_at": info["last_alert_at"]})
    return problems, info


def problem_key(p):
    return f"{p['type']}:{p.get('workflow', '')}"


def run(api=lib_ops.gh_api, runs_fn=lib_ops.workflow_runs, now=None, dry_run=False, notify=lib_ops.send_ops_telegram):
    now = now or datetime.now(timezone.utc)
    wf_status, wf_problems = check_workflows(api, runs_fn, now)
    data_problems, info = check_data(now)
    problems = wf_problems + data_problems
    previous = (lib_ops.read_json(LOG_FILE, {}) or {}).get("entries", [])
    prev_keys = set(previous[-1].get("problem_keys", [])) if previous else set()
    keys = sorted(problem_key(p) for p in problems)
    changed = set(keys) != prev_keys
    notified = "not_needed"
    if changed:
        if problems:
            lines = [f"🩺 Salud Shot de Mercado — {now:%Y-%m-%d %H:%M} UTC"]
            lines += [f"• {p['type']} {p.get('workflow', '')} {p.get('count', '')}".rstrip() for p in problems]
        else:
            lines = [f"✅ Salud Shot de Mercado — {now:%Y-%m-%d %H:%M} UTC: problemas resueltos"]
        notified = notify("\n".join(lines), dry_run=dry_run)
    entry = {"checked_at": now.isoformat(timespec="seconds"), "workflows": wf_status, "data": info,
             "problems": problems, "problem_keys": keys, "changed": changed, "notified": notified}
    if not dry_run:
        lib_ops.append_capped(LOG_FILE, entry, cap=500)
    print(f"[health] problemas: {keys or 'ninguno'} · cambio: {changed} · aviso: {notified}")
    return entry


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--dry-run", action="store_true", help="no escribe el log ni envía Telegram")
    args = ap.parse_args(argv)
    run(dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
