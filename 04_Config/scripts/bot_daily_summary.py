#!/usr/bin/env python3
"""
bot_daily_summary.py — Bot gemelo de reporte diario (cron 06:00 UTC). Solo lee archivos del repo.

Resume las últimas 24 h:
  - detecciones (corridas y tokens) y versión del scorer
  - alertas nuevas por estado (sombra / activas) y envíos a Telegram
  - métrica dual rolling por versión (desde shadow_monitor.json)
  - salud (último chequeo de _health_log.json) y acciones de reparación
  - modo de emisión (SHADOW_MODE / PAUSE_EMISSIONS en pipeline_t0.yml)
Guarda una entrada por día en 02_Analisis/_daily_summary.json y la envía al chat de operaciones.

Uso: python 04_Config/scripts/bot_daily_summary.py [--dry-run]
"""
import argparse
import glob
import json
import re
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_ops  # noqa: E402

R = lib_ops.ROOT
OUT = R / "02_Analisis" / "_daily_summary.json"
ALERTS = R / "02_Analisis" / "alerts" / "_all_alerts.json"
MONITOR = R / "02_Analisis" / "diagnostics" / "shadow_monitor.json"
HEALTH = R / "02_Analisis" / "_health_log.json"
REPAIR = R / "02_Analisis" / "_autorepair_log.json"
DETECTIONS = str(R / "01_Datos_Crudos" / "final_detection" / "detection_*.json")
WORKFLOW = R / ".github" / "workflows" / "pipeline_t0.yml"


def ts(value):
    try:
        if "T" in value:
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        return datetime.strptime(value, "%Y-%m-%d_%H%M%S").replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return None


def emission_mode():
    try:
        text = WORKFLOW.read_text(encoding="utf-8")
    except OSError:
        return {}
    grab = lambda k: (re.search(rf'{k}:\s*"?(\w+)"?', text) or [None, None])[1]
    return {"SHADOW_MODE": grab("SHADOW_MODE"), "PAUSE_EMISSIONS": grab("PAUSE_EMISSIONS")}


def build(now):
    since = now - timedelta(hours=24)
    det_files = [f for f in glob.glob(DETECTIONS) if (t := ts(Path(f).stem.replace("detection_", ""))) and t >= since]
    tokens, versions = 0, Counter()
    for f in det_files:
        d = lib_ops.read_json(f, {}) or {}
        enriched = d.get("enriched") or {}
        tokens += len(enriched)
        versions.update(v.get("scoring_version", "sin_version") for v in enriched.values() if isinstance(v, dict))
    alerts = [a for a in (lib_ops.read_json(ALERTS, []) or []) if isinstance(a, dict)]
    new = [a for a in alerts if (t := ts(a.get("timestamp"))) and t >= since]
    monitor = (lib_ops.read_json(MONITOR, {}) or {}).get("by_version", {})
    dual = {v: {"alerts": s.get("n_alerts"), "primary": s.get("primary"), "secondary": s.get("secondary"),
                "young_share": (s.get("young_lt_60m") or {}).get("share"), "verdict": s.get("verdict_partial")}
            for v, s in monitor.items()}
    health = ((lib_ops.read_json(HEALTH, {}) or {}).get("entries") or [{}])[-1]
    repairs = [e for e in (lib_ops.read_json(REPAIR, {}) or {}).get("entries", [])
               if (t := ts(e.get("checked_at"))) and t >= since and e.get("actions")]
    return {"date": now.date().isoformat(), "generated_at": now.isoformat(timespec="seconds"),
            "window_hours": 24, "emission_mode": emission_mode(),
            "detections": {"runs": len(det_files), "tokens": tokens, "scoring_versions": dict(versions)},
            "alerts_24h": {"total": len(new), "by_status": dict(Counter(a.get("status") for a in new)),
                           "telegram_sent": sum(1 for a in new if a.get("telegram_sent"))},
            "alerts_total": len(alerts), "dual_metric": dual,
            "health": {"checked_at": health.get("checked_at"), "problems": health.get("problem_keys", [])},
            "autorepair_actions_24h": sum(len(e["actions"]) for e in repairs)}


def render(s):
    lines = [f"📋 Resumen diario Shot de Mercado — {s['date']}",
             f"Modo: SHADOW_MODE={s['emission_mode'].get('SHADOW_MODE')} · PAUSE={s['emission_mode'].get('PAUSE_EMISSIONS')}",
             f"Detecciones 24 h: {s['detections']['runs']} corridas · {s['detections']['tokens']} tokens · "
             f"scorer {s['detections']['scoring_versions']}",
             f"Alertas 24 h: {s['alerts_24h']['total']} {s['alerts_24h']['by_status']} · enviadas: {s['alerts_24h']['telegram_sent']}"]
    for v, d in s["dual_metric"].items():
        p, q = d.get("primary") or {}, d.get("secondary") or {}
        lines.append(f"v{v}: primaria {p.get('k_hit')}/{p.get('n_resolved')} (pend {p.get('pending')}) · "
                     f"secundaria {q.get('k_hit')}/{q.get('n_resolved')} (pend {q.get('pending')}) · "
                     f"<60 min {d.get('young_share')} · veredicto {d.get('verdict') or 'n<20'}")
    lines.append(f"Salud: {s['health']['problems'] or 'sin problemas'} · reparaciones 24 h: {s['autorepair_actions_24h']}")
    return "\n".join(lines)


def run(now=None, dry_run=False, notify=lib_ops.send_ops_telegram):
    now = now or datetime.now(timezone.utc)
    summary = build(now)
    text = render(summary)
    summary["notified"] = notify(text, dry_run=dry_run)
    if not dry_run:
        data = lib_ops.read_json(OUT, {}) or {}
        days = [d for d in data.get("days", []) if d.get("date") != summary["date"]]
        data["days"] = (days + [summary])[-365:]
        data["last_updated"] = lib_ops.now_iso()
        lib_ops.write_json_atomic(OUT, data)
    print(text)
    return summary


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--dry-run", action="store_true", help="no escribe ni envía")
    args = ap.parse_args(argv)
    run(dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
