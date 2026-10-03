#!/usr/bin/env python3
"""
bot_rss_news.py — bot de fuentes RSS (doc 34 §3). Cada 20 min (workflow sources_rss.yml).

  1. Lee 04_Config/sources/rss.yaml (sumar feed = sumar línea; enabled: false lo saca).
  2. Descarga cada feed (RSS 2.0 o Atom; parser de lib_repetition, biblioteca estándar).
  3. Dedup por título normalizado + URL: dentro de la corrida y contra las claves vistas en dedup_hours (72 h).
  4. Escribe ítems src-1 (lib_sources_store) en 02_Analisis/sources/rss/<fecha>.jsonl. Sin cuerpo de texto.
  5. _state.json: claves vistas + salud por feed (estado HTTP, ítems, nuevos, fallas seguidas). Lo lee el orquestador.

Un feed caído no corta los demás. Solo GET públicos, sin secretos ni envíos.

Uso: python 04_Config/scripts/bot_rss_news.py [--dry-run] [--config ruta]
"""
import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_audit as audit  # noqa: E402
import lib_repetition as rep  # noqa: E402
import lib_sources_store as store  # noqa: E402

BOT = "rss"
VERSION = "rss-0.1"
TIMEOUT_S = 20
HEADERS = {"User-Agent": "shot-de-mercado-sources/1.0 (research; repo artificialintelligencestaff-tech/shot-de-mercado)"}


def config_path(root=None):
    return Path(root or store.ROOT) / "04_Config" / "sources" / "rss.yaml"


def load_config(path):
    import yaml
    doc = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    feeds = doc.get("feeds") if isinstance(doc, dict) else None
    if not isinstance(feeds, list):
        raise ValueError("rss.yaml: falta la lista 'feeds'")
    names = set()
    for f in feeds:
        if not isinstance(f, dict) or not f.get("name") or not f.get("url"):
            raise ValueError(f"rss.yaml: feed sin name/url: {f!r}")
        if f["name"] in names:
            raise ValueError(f"rss.yaml: nombre repetido: {f['name']}")
        names.add(f["name"])
    return doc


def dedup_key(title, url):
    norm = " ".join(str(title or "").lower().split())
    return hashlib.sha256(f"{norm}|{(url or '').strip()}".encode("utf-8")).hexdigest()[:16]


def parse_items(xml_text):
    """RSS 2.0 o Atom → [{"title", "url", "id", "ts", "text", "author"}] (fechas y HTML con lib_repetition)."""
    import xml.etree.ElementTree as ET
    out = []
    for node in ET.fromstring(xml_text).iter():
        if rep._local(node.tag) not in ("item", "entry"):
            continue
        f = {}
        for child in node:
            name = rep._local(child.tag)
            if name == "link" and child.get("href"):                     # Atom
                f.setdefault("link", child.get("href"))
            elif name == "author":
                f.setdefault("author", "".join(child.itertext()).strip() or None)
            elif name not in f:
                f[name] = "".join(child.itertext()).strip()
        title = rep.strip_html(f.get("title"))
        url = f.get("link") or None
        body = rep.strip_html(f.get("description") or f.get("summary") or f.get("content") or "")
        out.append({"title": title, "url": url, "id": f.get("guid") or f.get("id") or url,
                    "ts": rep._epoch(f.get("pubDate") or f.get("published") or f.get("updated") or f.get("date")),
                    "text": body, "author": f.get("author") or f.get("creator")})
    return out


def http_fetch(url):
    """Una request. Nunca lanza: devuelve (estado, texto|None)."""
    import requests
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT_S)
    except requests.RequestException as e:
        return f"error {type(e).__name__}", None
    return (200, r.text) if r.status_code == 200 else (r.status_code, None)


def load_state(path):
    try:
        st = json.loads(Path(path).read_text(encoding="utf-8"))
        return st if isinstance(st, dict) else {}
    except (OSError, ValueError):
        return {}


def run(config, state, fetch=http_fetch, now=None, sleep=time.sleep, keywords=store.DEFAULT_KEYWORDS, auto_off=None):
    """Una pasada por los feeds. Devuelve (registros nuevos, estado actualizado).
    `auto_off`: {feed: {"until": epoch}} de bot_self_repair; el feed se salta hasta `until` (reintenta después)."""
    now = now if now is not None else time.time()
    keep_s = float(config.get("dedup_hours") or 72) * 3600
    seen = {k: t for k, t in (state.get("seen") or {}).items() if now - t <= keep_s}
    configured = {f["name"] for f in config["feeds"] if f.get("enabled", True) is not False}
    health = {k: v for k, v in (state.get("feeds") or {}).items() if k in configured}   # lo que se sacó, se va
    records, first = [], True
    for feed in config["feeds"]:
        name = feed["name"]
        if feed.get("enabled", True) is False:
            continue
        off = (auto_off or {}).get(name) or {}
        if (off.get("until") or 0) > now:
            health[name] = {**(health.get(name) or {}), "auto_off_until": int(off["until"])}
            continue
        if not first:
            sleep(float(feed.get("pause_s", config.get("pause_s", 1))))
        first = False
        prev = health.get(name) or {}
        status, text = fetch(feed["url"])
        row = {"status": status, "items": 0, "new": 0, "checked_at": int(now),
               "last_ok": prev.get("last_ok"), "fails": 0}
        parsed = []
        if status == 200:
            try:
                parsed = parse_items(text)
            except Exception as e:          # 200 que no es XML (página de bloqueo, HTML)
                row["parse_error"] = f"{type(e).__name__}: {str(e)[:100]}"
        if status != 200 or "parse_error" in row:
            row["fails"] = int(prev.get("fails") or 0) + 1
        else:
            row["last_ok"] = int(now)
        row["items"] = len(parsed)
        for it in parsed:
            key = dedup_key(it["title"], it["url"] or it["id"])
            if key in seen:
                continue
            seen[key] = now
            records.append(store.make_record(BOT, name, "news", it["text"], id=it["id"], url=it["url"],
                                             ts=it["ts"], seen=now, title=it["title"],
                                             author=it.get("author"), keywords=keywords))
            row["new"] += 1
        health[name] = row
    return records, {"version": VERSION, "last_run": int(now), "items_last_run": len(records),
                     "feeds": health, "seen": seen}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--config", default=None)
    args = ap.parse_args(argv)
    config = load_config(args.config or config_path())
    state_file = store.sources_dir() / BOT / "_state.json"
    t_start = time.time()
    repair = load_state(store.sources_dir() / "_repair_state.json")
    records, state = run(config, load_state(state_file), fetch=http_fetch, keywords=store.load_keywords(),
                         auto_off=(repair.get("auto_off") or {}).get(BOT))
    ok = sum(1 for f in state["feeds"].values() if f["status"] == 200 and "parse_error" not in f)
    print(f"{BOT}: {len(records)} ítems nuevos · feeds OK {ok}/{len(state['feeds'])}")
    for name, f in sorted(state["feeds"].items()):
        print(f"  {name:28s} {str(f['status']):>14s} ítems {f['items']:3d} nuevos {f['new']:3d}"
              + (f"  {f['parse_error']}" if f.get("parse_error") else ""))
    if args.dry_run:
        return 0
    store.append_records(BOT, records, state["last_run"])
    state_file.parent.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(state, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    write_audit(state, len(records), time.time() - t_start)
    return 0


def write_audit(state, items_new, duration_s, folder=None):
    """Una línea en rss/_audit.jsonl + _metrics.json (patrón #15). Solo cuenta los feeds consultados en esta corrida."""
    now = state["last_run"]
    fetched = {k: f for k, f in state["feeds"].items() if f.get("checked_at") == now}
    errors = sum(1 for f in fetched.values() if f.get("status") != 200 or f.get("parse_error"))
    line = audit.audit_line(BOT, now, sum(f.get("items") or 0 for f in fetched.values()), items_new, errors,
                            len(fetched), duration_s)
    healthy = sum(1 for f in state["feeds"].values() if f.get("status") == 200 and not f.get("parse_error"))
    return audit.record_run(folder or store.sources_dir() / BOT, line, healthy, len(state["feeds"]))


if __name__ == "__main__":
    sys.exit(main())
