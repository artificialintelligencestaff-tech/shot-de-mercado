#!/usr/bin/env python3
"""
bot_autorepair.py — Bot gemelo de reparación (cron cada 4 h). NO modifica código ni hace pushes.

Por qué no "git pull --rebase && git push de recovery": el estado de un run fallido vive en su runner y se
pierde con él; otro workflow no tiene nada que empujar. Lo que sí recupera la falla común (choque de push
entre crons) es relanzar el run.

Acciones:
  1. RELANZAR: si el último run completo de un workflow de producción falló en un step transitorio
     (TRANSIENT_STEPS, p.ej. el choque de push en "Commit state changes") y va por su 1.er intento,
     relanza sus jobs fallidos UNA vez (POST .../rerun-failed-jobs).
  2. ESCALAR: si el mismo step falló en >= 3 de los últimos 5 runs completos, abre un issue
     "[autorepair] <workflow>: falla repetida en '<step>'" o lo comenta si ya está abierto (solo si hay
     runs fallidos nuevos desde el último comentario).
Todo queda en 02_Analisis/_autorepair_log.json y se avisa al chat de operaciones de Telegram.

Uso: python 04_Config/scripts/bot_autorepair.py [--dry-run]
"""
import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_ops  # noqa: E402

LOG_FILE = lib_ops.ROOT / "02_Analisis" / "_autorepair_log.json"
PRODUCTION_WORKFLOWS = ["pipeline_t0.yml", "trust_update.yml", "prelaunch.yml"]
TRANSIENT_STEPS = {"Commit state changes", "Checkout repo", "Install dependencies"}
PATTERN_WINDOW, PATTERN_MIN = 5, 3
ISSUE_PREFIX = "[autorepair]"


def run_url(run_id):
    return f"https://github.com/{lib_ops.REPO}/actions/runs/{run_id}"


def find_open_issue(api, title):
    issues = api(f"repos/{lib_ops.REPO}/issues?state=open&per_page=100")
    return next((i for i in issues if isinstance(i, dict) and i.get("title") == title and "pull_request" not in i), None)


def run(api=lib_ops.gh_api, runs_fn=lib_ops.workflow_runs, step_fn=lib_ops.failed_step,
        dry_run=False, notify=lib_ops.send_ops_telegram):
    log = lib_ops.read_json(LOG_FILE, {}) or {}
    escalated = log.get("escalated", {})            # título -> ids de runs ya reportados
    actions = []
    for wf in PRODUCTION_WORKFLOWS:
        runs = [r for r in runs_fn(wf) if r["status"] == "completed"]
        if not runs:
            continue
        latest = runs[0]
        steps = {}
        for r in runs[:PATTERN_WINDOW]:
            if r["conclusion"] == "failure":
                steps[r["id"]] = step_fn(r["id"])
        # 1) relanzar una vez una falla transitoria
        if latest["conclusion"] == "failure" and latest.get("run_attempt", 1) == 1 \
                and steps.get(latest["id"]) in TRANSIENT_STEPS:
            act = {"type": "rerun", "workflow": wf, "run_id": latest["id"], "step": steps[latest["id"]]}
            if not dry_run:
                api(f"repos/{lib_ops.REPO}/actions/runs/{latest['id']}/rerun-failed-jobs", method="POST", payload={})
            actions.append(act)
        # 2) escalar un patrón repetido
        by_step = {}
        for rid, step in steps.items():
            by_step.setdefault(step, []).append(rid)
        for step, rids in by_step.items():
            if step is None or len(rids) < PATTERN_MIN:
                continue
            title = f"{ISSUE_PREFIX} {wf}: falla repetida en '{step}'"
            new = sorted(set(rids) - set(escalated.get(title, [])))
            if not new:
                continue
            body = (f"El step **{step}** de `{wf}` falló en {len(rids)} de los últimos {PATTERN_WINDOW} runs completos.\n\n"
                    + "\n".join(f"- {run_url(r)}" for r in sorted(rids)) +
                    "\n\nAbierto automáticamente por `bot_autorepair.py`. No se intentó ningún fix de código.")
            act = {"type": "escalate", "workflow": wf, "step": step, "runs": sorted(rids), "title": title}
            if not dry_run:
                issue = find_open_issue(api, title)
                if issue:
                    api(f"repos/{lib_ops.REPO}/issues/{issue['number']}/comments", method="POST", payload={"body": body})
                    act["issue"] = issue["number"]
                else:
                    created = api(f"repos/{lib_ops.REPO}/issues", method="POST", payload={"title": title, "body": body})
                    act["issue"] = created.get("number")
            escalated[title] = sorted(set(escalated.get(title, [])) | set(rids))
            actions.append(act)
    notified = "not_needed"
    if actions:
        lines = [f"🔧 Autorepair Shot de Mercado — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC"]
        for a in actions:
            if a["type"] == "rerun":
                lines.append(f"• Relanzado {a['workflow']} (falló en '{a['step']}'): {run_url(a['run_id'])}")
            else:
                lines.append(f"• Issue por falla repetida en {a['workflow']} / '{a['step']}' ({len(a['runs'])} runs)")
        notified = notify("\n".join(lines), dry_run=dry_run)
    entry = {"checked_at": lib_ops.now_iso(), "actions": actions, "notified": notified}
    if not dry_run:
        data = lib_ops.append_capped(LOG_FILE, entry, cap=300)
        data["escalated"] = escalated
        lib_ops.write_json_atomic(LOG_FILE, data)
    print(f"[autorepair] acciones: {[a['type'] + ':' + a['workflow'] for a in actions] or 'ninguna'} · aviso: {notified}")
    return entry


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--dry-run", action="store_true", help="no relanza, no abre issues, no escribe ni avisa")
    args = ap.parse_args(argv)
    run(dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
