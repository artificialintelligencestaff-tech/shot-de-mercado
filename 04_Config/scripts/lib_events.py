#!/usr/bin/env python3
"""
lib_events.py — eventos entre bots (Ola 3, C-005 P1). Hechos vigentes con vencimiento; los hechos cerrados van a la
memoria episódica (#12).

  {"v":1, "id":"<sha16>", "type":"<tipo>", "subject":"<mint|bot|H-id>", "ts":<epoch>, "bucket":<epoch>,
   "writer":"<instancia>", "severity":<0-3>, "ttl_s":<int>, "parent":"<id|null>", "data":{}}

- id = sha16(type, subject, bucket), con bucket = ts redondeado hacia abajo a la ventana del tipo: el mismo hecho
  escrito por dos instancias (early_watch a y b) tiene el mismo id → dedup entre escritores.
- Un archivo por escritor y por día: 02_Analisis/events/<writer>/<YYYY-MM-DD>.jsonl (append-only, un dueño). Dos
  workflows nunca escriben el mismo archivo, así que el `pull --rebase` no choca (doc 34).
- Tipos cerrados (TYPES) con TTL y ventana propios. TTL vencido = el evento ya no se entrega.
- read_events: lectura unificada, dedup por id, TTL aplicado.
- consume: entrega al menos una vez desde un cursor propio (02_Analisis/events/_cursors/<consumer>.json) que guarda
  cuántas líneas leyó de CADA archivo, no un timestamp: un evento viejo que llega tarde por un merge de git
  igual se entrega. Si el callback falla, ese archivo se frena ahí (orden por escritor) y se reintenta después.
Retención: 8 días (el TTL más largo es 7). La poda la hace cada escritor sobre su propia carpeta.
Solo biblioteca estándar.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_normalize as norm  # noqa: E402

ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
EVENTS_REL = "02_Analisis/events"
SCHEMA = 1
RETENTION_DAYS = 8
DATA_MAX_BYTES = 4096
NAME_RE = re.compile(r"^[a-z0-9_]{1,40}$")
ID_RE = re.compile(r"^[0-9a-f]{16}$")
# TTL de pump_naciente, feed_caido y narrativa_emergente: D-067. El resto y todas las ventanas: [H].
# Tipos del calendario de preventa: D-079.
TYPES = {
    "feed_caido":          {"ttl_s": 7200,   "bucket_s": 7200},
    "feed_recuperado":     {"ttl_s": 7200,   "bucket_s": 7200},
    "fuente_saturada":     {"ttl_s": 3600,   "bucket_s": 3600},
    "narrativa_emergente": {"ttl_s": 14400,  "bucket_s": 14400},
    "mencion_acelerada":   {"ttl_s": 3600,   "bucket_s": 3600},
    "pump_naciente":       {"ttl_s": 3600,   "bucket_s": 3600},
    "graduacion":          {"ttl_s": 21600,  "bucket_s": 86400},     # un token gradúa una vez: ventana de un día
    "alerta_emitida":      {"ttl_s": 172800, "bucket_s": 3600},      # vive las 48 h de la ventana del evento
    "resultado_medido":    {"ttl_s": 604800, "bucket_s": 86400},
    "hipotesis_evaluada":  {"ttl_s": 604800, "bucket_s": 86400},
    # Calendario de activos no nacidos (D-079). token_nacido lo emitirán early_watch y multichain_scanner.
    "token_nacido":        {"ttl_s": 86400,  "bucket_s": 86400},     # un token nace una vez; 24 h > cadencia 6 h del calendario
    "token_anunciado":     {"ttl_s": 604800, "bucket_s": 2592000},   # ventana de 30 días: un anuncio por activo
    "token_confirmado":    {"ttl_s": 604800, "bucket_s": 2592000},
    "prelaunch_nacido":    {"ttl_s": 259200, "bucket_s": 2592000},   # vive las 72 h de seguimiento
    "token_purgado":       {"ttl_s": 86400,  "bucket_s": 2592000},
}


def events_dir(root=None):
    return Path(root or ROOT) / EVENTS_REL


def _day(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d")


def _check_name(kind, value):
    if not isinstance(value, str) or not NAME_RE.match(value):
        raise ValueError(f"{kind} inválido {value!r}: [a-z0-9_]{{1,40}}")
    return value


def default_writer():
    return os.environ.get("EVENTS_WRITER") or "local"


def event_id(type, subject, bucket):
    return hashlib.sha256(f"{type}|{subject}|{bucket}".encode("utf-8")).hexdigest()[:16]


def make_event(type, subject, severity=1, data=None, writer=None, parent=None, ttl_s=None, now=None):
    if type not in TYPES:
        raise ValueError(f"tipo {type!r} fuera de la lista cerrada: {sorted(TYPES)}")
    if norm.is_null(subject):
        raise ValueError("subject vacío")
    subject = norm.address(str(subject).strip()) or str(subject).strip()
    if len(subject) > 200:
        raise ValueError("subject de más de 200 caracteres")
    if not isinstance(severity, int) or isinstance(severity, bool) or not 0 <= severity <= 3:
        raise ValueError("severity debe ser un entero 0-3")
    if data is not None and not isinstance(data, dict):
        raise ValueError("data debe ser un dict")
    if parent is not None and not (isinstance(parent, str) and ID_RE.match(parent)):
        raise ValueError("parent debe ser un id de 16 hex o None")
    if len(json.dumps(data or {}, ensure_ascii=False)) > DATA_MAX_BYTES:
        raise ValueError(f"data de más de {DATA_MAX_BYTES} bytes: los eventos avisan, no transportan datasets")
    spec = TYPES[type]
    ts = int(now if now is not None else time.time())
    bucket = ts - ts % spec["bucket_s"]
    return {"v": SCHEMA, "id": event_id(type, subject, bucket), "type": type, "subject": subject, "ts": ts,
            "bucket": bucket, "writer": _check_name("writer", writer or default_writer()), "severity": severity,
            "ttl_s": int(ttl_s if ttl_s is not None else spec["ttl_s"]), "parent": parent, "data": data or {}}


def _parse_lines(path):
    """[(índice, evento|None, línea completa?)] — una última línea sin salto puede ser un push a medias."""
    try:
        raw = Path(path).read_text(encoding="utf-8")
    except OSError:
        return []
    out = []
    lines = raw.split("\n")
    for i, line in enumerate(lines):
        if i == len(lines) - 1 and line == "":
            break
        complete = i < len(lines) - 1
        try:
            ev = json.loads(line)
        except ValueError:
            ev = None
        out.append((i, ev if isinstance(ev, dict) and ev.get("type") in TYPES and ev.get("id") else None, complete))
    return out


def _files(root=None, since_day=None):
    base = events_dir(root)
    out = []
    for p in sorted(base.glob("*/*.jsonl")):
        if p.parent.name.startswith("_") or not NAME_RE.match(p.parent.name):
            continue
        if since_day and p.stem < since_day:
            continue
        out.append(p)
    return sorted(out, key=lambda p: (p.stem, p.parent.name))


def _known_ids(root, days):
    ids = set()
    for p in _files(root):
        if p.stem in days:
            ids.update(ev["id"] for _, ev, _ in _parse_lines(p) if ev)
    return ids


def prune(writer, now=None, root=None, keep_days=RETENTION_DAYS):
    now = now if now is not None else time.time()
    cutoff = _day(now - keep_days * 86400)
    removed = []
    for p in (events_dir(root) / _check_name("writer", writer)).glob("*.jsonl"):
        if p.stem < cutoff:
            p.unlink()
            removed.append(p.name)
    return sorted(removed)


def write_event(type, subject, severity=1, data=None, writer=None, parent=None, ttl_s=None, now=None, root=None):
    """Escribe en el archivo del escritor. Devuelve el evento, o None si ese hecho (mismo id) ya estaba escrito por
    cualquier escritor."""
    ev = make_event(type, subject, severity, data, writer, parent, ttl_s, now)
    days = {_day(ev["bucket"]), _day(ev["ts"])}
    if ev["id"] in _known_ids(root, days):
        return None
    path = events_dir(root) / ev["writer"] / f"{_day(ev['ts'])}.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(ev, ensure_ascii=False, sort_keys=True) + "\n")
    prune(ev["writer"], ev["ts"], root)
    return ev


def write_events(items, writer=None, now=None, root=None):
    """Lote: [(type, subject, severity, data), ...] con los ids conocidos cargados UNA vez (un poll del early watch
    puede traer cientos de candidatos). Devuelve los eventos nuevos escritos."""
    evs = [make_event(t, s, sev, d, writer, None, None, now) for t, s, sev, d in items]
    if not evs:
        return []
    days = {_day(e["bucket"]) for e in evs} | {_day(e["ts"]) for e in evs}
    known, new = _known_ids(root, days), []
    for e in evs:
        if e["id"] not in known:
            known.add(e["id"])
            new.append(e)
    if new:
        path = events_dir(root) / new[0]["writer"] / f"{_day(new[0]['ts'])}.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8", newline="\n") as f:
            for e in new:
                f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
        prune(new[0]["writer"], new[0]["ts"], root)
    return new


def alive(ev, now):
    return now <= (ev.get("ts") or 0) + (ev.get("ttl_s") or 0)


def read_events(since_ts=None, types=None, max_severity=None, min_severity=None, now=None, root=None,
                include_expired=False):
    """Todos los escritores, dedup por id (gana el primero en el tiempo), TTL aplicado, orden (ts, id)."""
    now = now if now is not None else time.time()
    since_day = _day(since_ts) if since_ts else _day(now - RETENTION_DAYS * 86400)
    types = {types} if isinstance(types, str) else (set(types) if types else None)
    best = {}
    for p in _files(root, since_day):
        for _, ev, _ in _parse_lines(p):
            if not ev:
                continue
            if since_ts is not None and ev["ts"] < since_ts:
                continue
            if types and ev["type"] not in types:
                continue
            if max_severity is not None and ev["severity"] > max_severity:
                continue
            if min_severity is not None and ev["severity"] < min_severity:
                continue
            if not include_expired and not alive(ev, now):
                continue
            prev = best.get(ev["id"])
            if prev is None or (ev["ts"], ev["writer"]) < (prev["ts"], prev["writer"]):
                best[ev["id"]] = ev
    return sorted(best.values(), key=lambda e: (e["ts"], e["id"]))


# ---------------------------------------------------------------------------
# Consumo con cursor propio
# ---------------------------------------------------------------------------

def cursor_path(consumer_id, root=None):
    return events_dir(root) / "_cursors" / f"{_check_name('consumer_id', consumer_id)}.json"


def load_cursor(consumer_id, root=None):
    try:
        cur = json.loads(cursor_path(consumer_id, root).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        cur = {}
    cur = cur if isinstance(cur, dict) else {}
    return {"version": SCHEMA, "files": dict(cur.get("files") or {}), "seen": dict(cur.get("seen") or {})}


def consume(consumer_id, callback, types=None, now=None, root=None):
    """Entrega cada evento nuevo (vivo, no visto, del tipo pedido) a `callback(evento)`, en orden (ts, id).
    Devuelve {"delivered": [...], "errors": [...]}. Al menos una vez: un fallo deja ese archivo frenado en esa línea
    y se reintenta en la próxima llamada; los demás archivos siguen."""
    now = now if now is not None else time.time()
    types = {types} if isinstance(types, str) else (set(types) if types else None)
    cur = load_cursor(consumer_id, root)
    seen = {k: v for k, v in cur["seen"].items() if v >= now}
    base = events_dir(root)
    candidates, advance = [], {}
    for p in _files(root, _day(now - RETENTION_DAYS * 86400)):
        rel = p.relative_to(base).as_posix()
        start = int(cur["files"].get(rel, 0))
        pos = start
        for i, ev, complete in _parse_lines(p):
            if i < start:
                continue
            if not complete:
                break                                        # línea a medio escribir: se relee la próxima vez
            pos = i + 1
            if ev and alive(ev, now) and (not types or ev["type"] in types):
                candidates.append((ev["ts"], ev["id"], rel, i, ev))
        advance[rel] = pos
    delivered, errors, pending = [], [], {}         # pending[rel] = primera línea de ese archivo que quedó sin entregar
    for _, _, rel, i, ev in sorted(candidates, key=lambda c: (c[0], c[1], c[2])):
        if ev["id"] in seen:
            continue
        if rel in pending:                           # archivo frenado: se reintenta desde la primera no entregada
            pending[rel] = min(pending[rel], i)
            continue
        try:
            callback(ev)
        except Exception as exc:                             # noqa: BLE001 — un consumidor roto no pierde eventos
            pending[rel] = i
            errors.append({"id": ev["id"], "file": rel, "error": f"{type(exc).__name__}: {exc}"[:300]})
            continue
        seen[ev["id"]] = ev["ts"] + ev["ttl_s"]
        delivered.append(ev)
    cur["files"] = {rel: pending.get(rel, pos) for rel, pos in advance.items()}
    cur.update(seen=seen, updated_at=int(now))
    path = cursor_path(consumer_id, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = Path(str(path) + ".tmp")
    tmp.write_text(json.dumps(cur, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    tmp.replace(path)
    return {"delivered": delivered, "errors": errors}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Eventos entre bots (Ola 3)")
    ap.add_argument("--type", action="append")
    ap.add_argument("--since-h", type=float, default=24)
    ap.add_argument("--all", action="store_true", help="incluye vencidos")
    a = ap.parse_args(argv)
    now = time.time()
    for ev in read_events(now - a.since_h * 3600, a.type, now=now, include_expired=a.all):
        ts = datetime.fromtimestamp(ev["ts"], timezone.utc).strftime("%Y-%m-%d %H:%M")
        print(f"{ts}  s{ev['severity']}  {ev['type']:20s} {ev['subject'][:44]:44s} {ev['writer']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
