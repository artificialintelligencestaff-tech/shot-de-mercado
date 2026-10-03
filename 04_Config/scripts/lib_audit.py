#!/usr/bin/env python3
"""
lib_audit.py — auto-monitoreo por bot (patrón #15). Plantilla: 02_Analisis/sources/_audit_template/_README.md.

Cada corrida de un bot agrega una línea a 02_Analisis/sources/<bot>/_audit.jsonl y recalcula <bot>/_metrics.json
sobre los últimos 30 días. Retención de _audit.jsonl: 90 días (se poda al agregar). Dueño: el propio bot.

Línea: {ts, timestamp, bot, items_in, items_new, items_discarded, errors, sources, duration_s, status, run_id}
  status: success (0 errores) · partial (algunas fuentes con error) · failure (todas con error, o 0 fuentes)
Solo biblioteca estándar.
"""
import json
import os
from datetime import datetime, timezone
from pathlib import Path

METRICS_DAYS = 30
RETENTION_DAYS = 90


def status_of(errors, sources):
    if sources <= 0 or errors >= sources:
        return "failure"
    return "partial" if errors else "success"


def audit_line(bot, now, items_in, items_new, errors, sources, duration_s, run_id=None):
    items_in, items_new = int(items_in), int(items_new)
    return {"ts": int(now), "timestamp": datetime.fromtimestamp(now, timezone.utc).isoformat(timespec="seconds"),
            "bot": bot, "items_in": items_in, "items_new": items_new,
            "items_discarded": max(0, items_in - items_new), "errors": int(errors), "sources": int(sources),
            "duration_s": round(float(duration_s), 2), "status": status_of(errors, sources),
            "run_id": run_id if run_id is not None else os.environ.get("GITHUB_RUN_ID")}


def read_lines(path):
    out = []
    try:
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(line)
            except ValueError:
                continue
            if isinstance(r, dict):
                out.append(r)
    except OSError:
        pass
    return out


def metrics(lines, now, sources_healthy, sources_total):
    recent = [r for r in lines if now - (r.get("ts") or 0) <= METRICS_DAYS * 86400]
    runs = len(recent)
    items_in = sum(r.get("items_in") or 0 for r in recent)
    items_new = sum(r.get("items_new") or 0 for r in recent)
    queried = sum(r.get("sources") or 0 for r in recent)
    return {"runs": runs, "items_total": items_new,
            "dedup_rate": round(sum(r.get("items_discarded") or 0 for r in recent) / items_in, 4) if items_in else 0,
            "error_rate": round(sum(r.get("errors") or 0 for r in recent) / queried, 4) if queried else 0,
            "availability": round(sum(r.get("status") != "failure" for r in recent) / runs, 4) if runs else 0,
            "last_update": int(now), "avg_items_per_run": round(items_new / runs, 2) if runs else 0,
            "avg_duration_s": round(sum(r.get("duration_s") or 0 for r in recent) / runs, 2) if runs else 0,
            "sources_healthy": int(sources_healthy), "sources_total": int(sources_total), "window_days": METRICS_DAYS}


def record_run(folder, line, sources_healthy, sources_total):
    """Agrega la línea (podando lo de más de 90 días) y reescribe _metrics.json. Devuelve las métricas."""
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    now = line["ts"]
    lines = [r for r in read_lines(folder / "_audit.jsonl") if now - (r.get("ts") or 0) <= RETENTION_DAYS * 86400]
    lines.append(line)
    tmp = folder / "_audit.jsonl.tmp"
    tmp.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in lines), encoding="utf-8")
    tmp.replace(folder / "_audit.jsonl")
    m = metrics(lines, now, sources_healthy, sources_total)
    (folder / "_metrics.json").write_text(json.dumps(m, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    return m
