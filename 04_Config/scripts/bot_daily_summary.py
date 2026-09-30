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


SEP = "━━━━━━━━━━━━━━━━━━━━━━━━━━━"
YOUNG_SHARE_MAX = 0.20          # criterio de Dirección para v7.2.1 (doc 22 §1.1): exposición < 60 min
STATUS_LABELS = {"shadow": "shadow", "active_tracking": "activas"}


def fmt_int(n):
    """1440 -> "1.440" (separador de miles rioplatense)."""
    return f"{int(n):,}".replace(",", ".") if isinstance(n, (int, float)) else "n/d"


def fmt_pct(x):
    return f"{x * 100:.0f}%" if isinstance(x, (int, float)) else "n/d"


def version_key(v):
    try:
        return tuple(int(p) for p in v.split("."))
    except (AttributeError, ValueError):
        return ()


def current_version(s):
    """Scorer vigente = la versión numérica más alta vista en detecciones o en la métrica dual."""
    seen = [v for v in s["detections"]["scoring_versions"] if version_key(v)]
    seen += [v for v in s["dual_metric"] if version_key(v)]
    return max(seen, key=version_key) if seen else None


def metric_line(label, m):
    m = m or {}
    if not m:
        return f"• {label}: n/d"
    return (f"• {label}: {fmt_int(m.get('k_hit') or 0)}/{fmt_int(m.get('n_resolved') or 0)} resueltas · "
            f"{fmt_int(m.get('pending') or 0)} pendientes")


def young_line(share):
    mark = " ⚠️" if isinstance(share, (int, float)) and share > YOUNG_SHARE_MAX else ""
    return f"• Exposición a <60 min: {fmt_pct(share)}{mark}"


def mode_line(mode):
    if str(mode.get("PAUSE_EMISSIONS")).lower() == "true":
        return "⛔ Modo: PAUSA (no se procesan emisiones)"
    if str(mode.get("SHADOW_MODE")).lower() == "true":
        return "⏸️ Modo: SOMBRA (emisiones pausadas)"
    if mode.get("SHADOW_MODE") is None:
        return "❔ Modo: n/d"
    return "▶️ Modo: EMISIÓN ACTIVA"


def render(s):
    try:
        stamp = datetime.fromisoformat(s["generated_at"]).strftime("%d/%m/%Y · %H:%M UTC")
    except (KeyError, TypeError, ValueError):
        stamp = s.get("date", "n/d")
    alerts = s["alerts_24h"]
    by_status = alerts.get("by_status") or {}
    order = list(STATUS_LABELS)                       # shadow, activas y después el resto por nombre
    ordered = sorted(by_status.items(),
                     key=lambda kv: (order.index(kv[0]) if kv[0] in order else len(order), str(kv[0])))
    detail = " · ".join(f"{fmt_int(n)} {STATUS_LABELS.get(k, k)}" for k, n in ordered)
    lines = ["📊 SHOT DE MERCADO — RESUMEN DIARIO", f"📅 {stamp}", SEP, "",
             "🔍 ACTIVIDAD (24h)",
             f"• Corridas del pipeline: {fmt_int(s['detections']['runs'])}",
             f"• Tokens analizados: {fmt_int(s['detections']['tokens'])}",
             f"• Alertas registradas: {fmt_int(alerts['total'])}" + (f" ({detail})" if detail else ""),
             f"• Enviadas al público: {fmt_int(alerts['telegram_sent'])}", ""]

    # Calidad separada por versión del scorer (anomalía A-b: el 83% agregado mezclaba v7.2 y v7.2.1)
    current = current_version(s)
    dual = s["dual_metric"]
    lines.append(f"📈 CALIDAD (v{current})" if current else "📈 CALIDAD")
    if current in dual:
        d = dual[current]
        lines += [metric_line("Primaria (tocar +20%)", d.get("primary")),
                  metric_line("Secundaria (cerrar +20%)", d.get("secondary")), young_line(d.get("young_share"))]
    else:
        lines.append("• Sin alertas de esta versión todavía")
    for v in sorted((v for v in dual if v != current), key=lambda v: (version_key(v), v), reverse=True):
        d = dual[v]
        p, q = d.get("primary") or {}, d.get("secondary") or {}
        lines.append(f"• v{v} (anterior): primaria {fmt_int(p.get('k_hit') or 0)}/{fmt_int(p.get('n_resolved') or 0)} · "
                     f"secundaria {fmt_int(q.get('k_hit') or 0)}/{fmt_int(q.get('n_resolved') or 0)} · "
                     f"<60 min {fmt_pct(d.get('young_share'))}")
    lines.append("")

    lines.append("🚀 SCORER")
    versions = s["detections"]["scoring_versions"]
    for v in sorted((v for v in versions if version_key(v)), key=version_key, reverse=True):
        label = f"v{v}" if v == current else f"v{v} (transición)"
        lines.append(f"• {label}: {fmt_int(versions[v])} tokens")
    legacy = sum(n for v, n in versions.items() if not version_key(v))
    if legacy:
        lines.append(f"• Legacy (sin versión): {fmt_int(legacy)} tokens")
    if not versions:
        lines.append("• Sin detecciones en 24 h")
    lines.append("")

    lines.append("🛡️ SALUD")
    problems = s["health"].get("problems") or []
    lines += [f"⚠️ {p}" for p in problems] or ["✅ Sin problemas"]
    repairs = s["autorepair_actions_24h"]
    lines.append("✅ 0 reparaciones en 24h" if not repairs else f"🔧 {fmt_int(repairs)} reparaciones en 24h")
    lines += ["", mode_line(s.get("emission_mode") or {})]
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
