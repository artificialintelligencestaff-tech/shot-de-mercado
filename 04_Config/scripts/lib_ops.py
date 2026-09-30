#!/usr/bin/env python3
"""
lib_ops.py — Utilidades compartidas de los bots gemelos (solo biblioteca estándar).

- send_ops_telegram(): SOLO al chat de operaciones (secreto TELEGRAM_OPS_CHAT_ID + TELEGRAM_BOT_TOKEN).
  Nunca usa TELEGRAM_CHAT_ID (el chat de alertas al público). Si falta el chat de operaciones, no envía.
- gh_api(): API REST de GitHub con GITHUB_TOKEN (Actions) o, en local, vía `gh api` (sin manejar tokens).
- write_json_atomic(), read_json(), append_capped(): estado en JSON versionado.
"""
import json
import os
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(os.environ.get("SHOT_ROOT") or Path(__file__).resolve().parents[2])
REPO = os.environ.get("GITHUB_REPOSITORY", "artificialintelligencestaff-tech/shot-de-mercado")
USER_AGENT = "shot-de-mercado-ops-bot/1.0"


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read_json(path, default=None):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def write_json_atomic(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, path)


def append_capped(path, entry, key="entries", cap=500):
    """Agrega `entry` a data[key] (lista) conservando las últimas `cap` entradas. Devuelve el dict."""
    data = read_json(path, {}) or {}
    if not isinstance(data, dict):
        data = {}
    items = data.get(key) if isinstance(data.get(key), list) else []
    items.append(entry)
    data[key] = items[-cap:]
    data["last_updated"] = now_iso()
    write_json_atomic(path, data)
    return data


def send_ops_telegram(text, dry_run=False):
    """Envía al chat de OPERACIONES. Devuelve 'sent' | 'skipped_no_ops_chat' | 'dry_run' | 'error:<detalle>'."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat = os.environ.get("TELEGRAM_OPS_CHAT_ID", "").strip()
    if dry_run:
        print(f"[DRY-RUN Telegram ops]\n{text}")
        return "dry_run"
    if not token or not chat:
        print("[INFO] Sin TELEGRAM_OPS_CHAT_ID/TELEGRAM_BOT_TOKEN: aviso no enviado (solo queda en el log).")
        return "skipped_no_ops_chat"
    body = json.dumps({"chat_id": chat, "text": text[:4000], "disable_web_page_preview": True}).encode()
    req = urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage", data=body,
                                 headers={"Content-Type": "application/json", "User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return "sent" if resp.status == 200 else f"error:HTTP {resp.status}"
    except (urllib.error.URLError, OSError) as e:
        return f"error:{type(e).__name__}"          # nunca imprime el token ni la URL completa


def gh_api(path, method="GET", payload=None):
    """GET/POST a la API de GitHub. Con GITHUB_TOKEN usa urllib; sin él, `gh api` (auth local de gh)."""
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        url = f"https://api.github.com/{path.lstrip('/')}"
        data = json.dumps(payload).encode() if payload is not None else None
        req = urllib.request.Request(url, data=data, method=method, headers={
            "Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28", "User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                raw = resp.read()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"GitHub API {method} {path}: HTTP {e.code}") from None
    cmd = ["gh", "api", "-X", method, path]
    if payload is not None:
        cmd += ["--input", "-"]
    out = subprocess.run(cmd, input=json.dumps(payload) if payload is not None else None,
                         capture_output=True, text=True, encoding="utf-8")
    if out.returncode != 0:
        raise RuntimeError(f"gh api {method} {path}: {out.stderr.strip()[:200]}")
    return json.loads(out.stdout) if out.stdout.strip() else {}


def workflow_runs(workflow_file, per_page=10):
    """Últimos runs de un workflow (más reciente primero), con los campos que usan los bots."""
    data = gh_api(f"repos/{REPO}/actions/workflows/{workflow_file}/runs?per_page={per_page}")
    return [{"id": r["id"], "status": r["status"], "conclusion": r.get("conclusion"),
             "created_at": r["created_at"], "run_attempt": r.get("run_attempt", 1),
             "head_sha": r.get("head_sha", "")[:7], "event": r.get("event")}
            for r in data.get("workflow_runs", [])]


def failed_step(run_id):
    """Nombre del primer step fallido del primer job del run (None si no hay)."""
    jobs = gh_api(f"repos/{REPO}/actions/runs/{run_id}/jobs").get("jobs", [])
    for job in jobs:
        for step in job.get("steps", []):
            if step.get("conclusion") == "failure":
                return step.get("name")
    return None
