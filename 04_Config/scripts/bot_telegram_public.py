#!/usr/bin/env python3
"""
bot_telegram_public.py — bot de canales públicos de Telegram (doc 34 §3; D-041 T5). Solo la vista web pública
t.me/s/<canal>: sin cuenta, sin API de Telegram, sin Telethon / Pyrogram (prohibidos en el proyecto).

Job largo: un loop de `loop_minutes` (40) con una pasada cada `poll_minutes` (4). Corren 2 instancias desfasadas
(sources_telegram_a.yml en :05, _b.yml en :35) que se solapan 10 min y cubren el desfase del cron de Actions.

  1. Lee 04_Config/sources/telegram.yaml (sumar canal = sumar línea; enabled: false lo saca).
  2. Descarga cada canal y lo parsea con BeautifulSoup (html.parser): un ítem por mensaje (data-post, <time>,
     texto, enlaces del texto — el contrato suele venir en un enlace a pump.fun / dexscreener / solscan —, vistas).
  3. Cursor por canal (id del último post) + dedup de 72 h: cada instancia escribe solo lo nuevo para ella; lo que
     ven las dos se descarta en el merge (dedup global por src, ts, h).
  4. src-1 (lib_sources_store) en 02_Analisis/sources/telegram/<fecha>_<inst>.jsonl, sin cuerpo de texto.
  5. Estado por instancia en telegram/_state_<inst>.json (un dueño por archivo): salud por canal, cursor, vista
     previa. Un canal sin vista previa (redirige a t.me/<canal>) se apaga y se reintenta cada recheck_hours.
  6. Respeta los auto_off de bot_self_repair (_repair_state.json).
  7. Commitea su carpeta cada `commit_every` pasadas y al final; auditoría al final (_audit_<inst>.jsonl).

Uso: python 04_Config/scripts/bot_telegram_public.py --instance a [--loop-minutes 40] [--once] [--dry-run]
"""
import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlsplit

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_audit as audit  # noqa: E402
import lib_normalize as norm  # noqa: E402
import lib_sources_store as store  # noqa: E402

BOT = "telegram"
VERSION = "tg-0.1"
TIMEOUT_S = 20
HEADERS = {"User-Agent": "shot-de-mercado-sources/1.0 (research; repo artificialintelligencestaff-tech/shot-de-mercado)"}
VIEWS_RE = re.compile(r"^([\d.,]+)\s*([KkMm]?)$")


def config_path(root=None):
    return Path(root or store.ROOT) / "04_Config" / "sources" / "telegram.yaml"


def load_config(path):
    import yaml
    doc = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    channels = doc.get("channels") if isinstance(doc, dict) else None
    if not isinstance(channels, list) or not channels:
        raise ValueError("telegram.yaml: falta la lista 'channels'")
    names = set()
    for c in channels:
        if not isinstance(c, dict) or not re.fullmatch(r"[A-Za-z0-9_]{4,64}", str(c.get("name") or "")):
            raise ValueError(f"telegram.yaml: canal inválido: {c!r}")
        if c["name"].lower() in names:
            raise ValueError(f"telegram.yaml: canal repetido: {c['name']}")
        names.add(c["name"].lower())
    return doc


def parse_views(text):
    m = VIEWS_RE.match((text or "").strip())
    if not m:
        return None
    n = float(m.group(1).replace(",", ""))
    return int(n * {"k": 1_000, "m": 1_000_000}.get(m.group(2).lower(), 1))


def parse_preview(html):
    """Mensajes de la vista previa: [{"post", "num", "ts", "text", "views"}] (texto + enlaces, para extraer CAs)."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html or "", "html.parser")
    out = []
    for m in soup.select("div.tgme_widget_message[data-post]"):
        post = m["data-post"]
        num = post.rsplit("/", 1)[-1]
        body = m.select_one(".tgme_widget_message_text")
        text = body.get_text(" ", strip=True) if body else ""
        links = [a.get("href") for a in (body.select("a[href]") if body else []) if a.get("href")]
        t = m.select_one("time[datetime]")
        views = m.select_one(".tgme_widget_message_views")
        out.append({"post": post, "num": int(num) if num.isdigit() else None,
                    "ts": norm.timestamp(t["datetime"]) if t else None,
                    "text": " ".join([text] + links).strip(),
                    "views": parse_views(views.get_text()) if views else None})
    return out


def has_preview(final_url, channel):
    """La vista previa vive en /s/<canal>; sin ella, Telegram redirige a t.me/<canal>."""
    path = urlsplit(final_url or "").path.rstrip("/").lower()
    return path == f"/s/{channel.lower()}"


def http_fetch(channel):
    """(estado, html|None, url final). Nunca lanza."""
    import requests
    url = f"https://t.me/s/{channel}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT_S)
    except requests.RequestException as e:
        return f"error {type(e).__name__}", None, url
    return r.status_code, (r.text if r.status_code == 200 else None), r.url


def load_state(path):
    try:
        st = json.loads(Path(path).read_text(encoding="utf-8"))
        return st if isinstance(st, dict) else {}
    except (OSError, ValueError):
        return {}


def poll(config, state, now, fetch=http_fetch, sleep=time.sleep, auto_off=None, keywords=store.DEFAULT_KEYWORDS):
    """Una pasada por los canales. Devuelve (registros nuevos, estado actualizado)."""
    keep_s = float(config.get("dedup_hours") or 72) * 3600
    recheck_s = float(config.get("recheck_hours") or 24) * 3600
    seen = {k: t for k, t in (state.get("seen") or {}).items() if now - t <= keep_s}
    active = [c for c in config["channels"] if c.get("enabled", True) is not False]
    names = {c["name"] for c in active}
    health = {k: v for k, v in (state.get("sources") or {}).items() if k in names}
    records, first = [], True
    for ch in active:
        name = ch["name"]
        prev = health.get(name) or {}
        if prev.get("preview") is False and now < (prev.get("next_check") or 0):
            continue                                       # sin vista previa: se reintenta cada recheck_hours
        off = (auto_off or {}).get(name) or {}
        if (off.get("until") or 0) > now:
            health[name] = {**prev, "auto_off_until": int(off["until"])}
            continue
        if not first:
            sleep(float(ch.get("pause_s", config.get("pause_s", 2))))
        first = False
        status, html, final_url = fetch(name)
        row = {"status": status, "items": 0, "new": 0, "checked_at": int(now), "last_ok": prev.get("last_ok"),
               "fails": 0, "cursor": prev.get("cursor"), "preview": True}
        msgs = []
        if status == 200 and not has_preview(final_url, name):
            row.update(preview=False, next_check=int(now + recheck_s))
        elif status == 200:
            try:
                msgs = parse_preview(html)
            except Exception as e:                         # HTML inesperado: cuenta como falla del canal
                row["parse_error"] = f"{type(e).__name__}: {str(e)[:100]}"
        if status != 200 or "parse_error" in row:
            row["fails"] = int(prev.get("fails") or 0) + 1
        elif row["preview"]:
            row["last_ok"] = int(now)
        row["items"] = len(msgs)
        cursor = prev.get("cursor") or 0
        for msg in msgs:
            if (msg["num"] or 0) <= cursor or msg["post"] in seen:
                continue
            seen[msg["post"]] = now
            records.append(store.make_record(BOT, name, "message", msg["text"], id=msg["post"],
                                             url=f"https://t.me/{msg['post']}", ts=msg["ts"], seen=now, author=name,
                                             meta={"views": msg["views"]} if msg["views"] is not None else {},
                                             keywords=keywords))
            row["new"] += 1
        nums = [m["num"] for m in msgs if m["num"]]
        row["cursor"] = max([cursor] + nums) or None
        health[name] = row
    return records, {"version": VERSION, "last_run": int(now), "items_last_run": len(records), "sources": health,
                     "seen": seen}


def git_commit(paths, message, retries=4, run=subprocess.run, sleep=time.sleep):
    """Commit solo de `paths` + pull --rebase + push, con reintentos (mismo patrón que los workflows). Nunca --force."""
    def git(*args):
        return run(["git", *args], capture_output=True, text=True).returncode == 0
    git("add", "-A", "--", *[str(p) for p in paths])
    if git("diff", "--staged", "--quiet"):
        return True                                        # sin cambios
    if not git("commit", "-q", "-m", message):
        return False
    for i in range(1, retries + 1):
        if git("pull", "-q", "--rebase", "origin", "main") and git("push", "origin", "HEAD:main"):
            return True
        git("rebase", "--abort")
        sleep(i * 15)
    return False


def run_loop(config, instance, root=None, loop_minutes=None, fetch=http_fetch, clock=time.time, sleep=time.sleep,
             commit=None, commit_every=3, write=True):
    """Job largo: pasadas cada poll_minutes durante loop_minutes. Devuelve el resumen del job."""
    base = store.sources_dir(root) / BOT
    state_file = base / f"_state_{instance}.json"
    state = load_state(state_file)
    repair = load_state(store.sources_dir(root) / "_repair_state.json")
    auto_off = (repair.get("auto_off") or {}).get(BOT)
    keywords = store.load_keywords(root)
    t_start = clock()
    minutes = loop_minutes if loop_minutes is not None else (config.get("loop_minutes") or 40)   # 0 = una pasada
    end = t_start + float(minutes) * 60
    poll_s = float(config.get("poll_minutes") or 4) * 60
    totals = {"polls": 0, "items_in": 0, "items_new": 0, "errors": 0, "sources": 0, "commits": 0}
    while True:
        now = clock()
        records, state = poll(config, state, now, fetch=fetch, sleep=sleep, auto_off=auto_off, keywords=keywords)
        polled = {k: v for k, v in state["sources"].items() if v.get("checked_at") == int(now)}
        totals["polls"] += 1
        totals["items_in"] += sum(v.get("items") or 0 for v in polled.values())
        totals["items_new"] += len(records)
        totals["errors"] += sum(1 for v in polled.values() if v.get("status") != 200 or v.get("parse_error"))
        totals["sources"] += len(polled)
        if write:
            store.append_records(BOT, records, now, instance=instance, root=root)
            base.mkdir(parents=True, exist_ok=True)
            state_file.write_text(json.dumps(state, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
        last = clock() + poll_s >= end
        if write and commit and (totals["polls"] % commit_every == 0 or last):
            if last:
                write_audit(state, totals, clock() - t_start, instance, base)
            totals["commits"] += bool(commit([base], f"sources_telegram_{instance}: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(now))}"))
        elif write and last:
            write_audit(state, totals, clock() - t_start, instance, base)
        if last:
            return totals
        sleep(max(0.0, now + poll_s - clock()))


def write_audit(state, totals, duration_s, instance, folder):
    """Una línea por job en telegram/_audit_<inst>.jsonl + _metrics_<inst>.json (patrón #15)."""
    line = audit.audit_line(f"{BOT}_{instance}", state["last_run"], totals["items_in"], totals["items_new"],
                            totals["errors"], totals["sources"], duration_s)
    healthy = sum(1 for v in state["sources"].values() if v.get("status") == 200 and v.get("preview") is not False
                  and not v.get("parse_error"))
    return audit.record_run(folder, line, healthy, len(state["sources"]), suffix=f"_{instance}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--instance", choices=["a", "b"], required=True)
    ap.add_argument("--loop-minutes", type=float, default=None)
    ap.add_argument("--once", action="store_true", help="una sola pasada (loop de 0 min)")
    ap.add_argument("--no-commit", action="store_true", help="no commitea desde el loop (lo hace el workflow)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    config = load_config(config_path())
    totals = run_loop(config, args.instance, loop_minutes=0 if args.once else args.loop_minutes,
                      commit=None if (args.no_commit or args.dry_run) else git_commit, write=not args.dry_run)
    print(f"{BOT}_{args.instance}: {totals['polls']} pasadas · {totals['items_new']} ítems nuevos de "
          f"{totals['items_in']} leídos · errores {totals['errors']}/{totals['sources']} · commits {totals['commits']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
