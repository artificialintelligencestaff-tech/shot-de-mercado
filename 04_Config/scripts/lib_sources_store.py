#!/usr/bin/env python3
"""
lib_sources_store.py — almacén unificado de los bots de fuentes (doc 34). No es un bot: lo usan los bots para
escribir, el orquestador para fusionar y los scorers para consultar.

  make_record(...)       ítem en el esquema src-1 (sin cuerpo de texto: identificadores, palabras clave, hash)
  append_records(...)    agrega al diario del bot 02_Analisis/sources/<bot>/<fecha>[_<inst>].jsonl
  merge(...)             une los diarios de las últimas 48 h, dedup global (src, ts, h) -> _merged.jsonl + _index.json
  query(keyword)         menciones por dirección, cashtag o palabra clave, de la más reciente a la más vieja
  to_items_store(...)    forma de _items.json de script_115 ({"ts", "a", "c", "f"}) para lib_info_signals.mentions

Solo biblioteca estándar (PyYAML opcional para keywords.yaml).
"""
import hashlib
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
import sys  # noqa: E402
sys.path.insert(0, str(SCRIPTS))
import lib_normalize as norm  # noqa: E402  forma canónica de direcciones, cashtags, keywords, fechas y URLs (#19)

SCHEMA = "src-1"
TITLE_MAX = 160
MERGE_HOURS = 48
MERGED_STALE_S = 15 * 60          # _merged.jsonl más viejo que esto: query() reconstruye en memoria
KINDS = {"news", "message", "post", "repo", "tweet", "token"}   # token: lanzamiento/pool/ficha de un token (recetas, Ola 3)
# Misma sal y mismas expresiones que script_115 (doc 26): seudónimo de autor, sin handles en el repo.
AUTHOR_SALT = os.environ.get("NARRATIVE_AUTHOR_SALT") or "shot-de-mercado/rep-0.1"
BASE58_RE = re.compile(r"(?<![0-9A-Za-z])[1-9A-HJ-NP-Za-km-z]{32,44}(?![1-9A-HJ-NP-Za-km-z])")
EVM_RE = re.compile(r"(?<![0-9A-Za-z])0x[0-9a-fA-F]{40}(?![0-9a-fA-F])")
CASHTAG_RE = re.compile(r"(?<![\w$])\$([A-Za-z][A-Za-z0-9]{0,14})(?!\w)")
ADDRESS_RE = re.compile(r"[1-9A-HJ-NP-Za-km-z]{32,44}|0x[0-9a-fA-F]{40}")
DEFAULT_KEYWORDS = ("memecoin", "pump.fun", "presale", "airdrop", "solana", "depin", "rwa", "tokenization",
                    "governance", "synthetic", "layer 2", "l2", "listing", "launch")


def sources_dir(root=None):
    return Path(root or ROOT) / "02_Analisis" / "sources"


def load_keywords(root=None):
    """04_Config/sources/keywords.yaml → lista plana en minúsculas; por defecto DEFAULT_KEYWORDS."""
    path = Path(root or ROOT) / "04_Config" / "sources" / "keywords.yaml"
    try:
        import yaml
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, ImportError, ValueError):
        return list(DEFAULT_KEYWORDS)
    groups = doc.get("keywords") if isinstance(doc, dict) else None
    words = []
    for v in (groups.values() if isinstance(groups, dict) else [groups or []]):
        words += [str(w).strip().lower() for w in (v or []) if str(w).strip()]
    return sorted(set(words)) or list(DEFAULT_KEYWORDS)


def _kw_pattern(word):
    return re.compile(rf"(?<!\w){re.escape(word)}(?!\w)", re.IGNORECASE)


def extract(text, keywords=DEFAULT_KEYWORDS):
    """(direcciones, cashtags, palabras clave) del texto. EVM en minúsculas; base58 exacto."""
    text = text or ""
    addresses = set(BASE58_RE.findall(text)) | {a.lower() for a in EVM_RE.findall(text)}
    cashtags = {c.upper() for c in CASHTAG_RE.findall(text)}
    kws = {w for w in keywords if _kw_pattern(w).search(text)}
    return sorted(addresses), sorted(cashtags), sorted(kws)


def text_hash(text):
    norm = " ".join(str(text or "").lower().split())
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()[:16]


def author_hash(author):
    if not author:
        return None
    return hashlib.sha256(f"{AUTHOR_SALT}|{str(author).strip().lower()}".encode("utf-8")).hexdigest()[:12]


def make_record(bot, src, kind, text, *, id=None, url=None, ts=None, seen=None, title=None, author=None,
                meta=None, keywords=DEFAULT_KEYWORDS):
    """Ítem src-1. `text` se usa para extraer y hashear; no se guarda."""
    if kind not in KINDS:
        raise ValueError(f"kind desconocido: {kind}")
    a, c, k = extract(" ".join(x for x in (title, text) if x), keywords)
    t = " ".join(str(title).split())[:TITLE_MAX] if title and kind not in ("message", "tweet") else None
    return norm.record({"v": SCHEMA, "bot": bot, "src": src, "kind": kind, "id": id or url, "url": url,
                        "ts": ts, "seen": seen if seen is not None else time.time(), "title": t, "a": a, "c": c,
                        "k": k, "h": text_hash(" ".join(x for x in (title, text) if x)), "au": author_hash(author),
                        "m": meta or {}})


def day_path(bot, when=None, instance=None, root=None):
    day = datetime.fromtimestamp(when if when is not None else time.time(), timezone.utc).strftime("%Y-%m-%d")
    return sources_dir(root) / bot / (f"{day}_{instance}.jsonl" if instance else f"{day}.jsonl")


def append_records(bot, records, when=None, instance=None, root=None):
    """Agrega al diario del bot. Devuelve la ruta (o None si no hay registros)."""
    if not records:
        return None
    path = day_path(bot, when, instance, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
    return path


def read_jsonl(path):
    out = []
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError:
        return out
    for line in lines:
        try:
            r = json.loads(line)
        except ValueError:
            continue                      # línea cortada por un push a medias: se ignora
        if isinstance(r, dict):
            out.append(r)
    return out


def _when(r):
    return r.get("ts") if isinstance(r.get("ts"), (int, float)) else (r.get("seen") or 0)


def dedup_key(r):
    return (r.get("src"), r.get("ts"), r.get("h"))


def collect(now=None, hours=MERGE_HOURS, root=None, stats=None):
    """Todos los diarios de los bots dentro de la ventana, dedup global por (src, ts, h), más reciente primero.
    `stats` (dict opcional): 'read' = ítems src-1 leídos antes de ventana y dedup (auditoría del orquestador)."""
    now = now if now is not None else time.time()
    cutoff = now - hours * 3600
    days = {datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%d")
            for t in range(int(cutoff), int(now) + 86400, 86400)}
    seen, out = set(), []
    base = sources_dir(root)
    for path in sorted(base.glob("*/*.jsonl")):
        if path.name[:10] not in days:
            continue
        for r in read_jsonl(path):
            if r.get("v") != SCHEMA:
                continue
            if stats is not None:
                stats["read"] = stats.get("read", 0) + 1
            r = norm.record(r)            # diarios viejos o de otro bot: misma forma canónica al fusionar
            if _when(r) < cutoff or _when(r) > now + 600:
                continue
            key = dedup_key(r)
            if key in seen:
                continue
            seen.add(key)
            out.append(r)
    out.sort(key=_when, reverse=True)
    return out


def build_index(records):
    """{"a": {dirección: [fila]}, "c": {CASHTAG: [fila]}, "k": {palabra: [fila]}} sobre la lista ya ordenada."""
    idx = {"a": {}, "c": {}, "k": {}}
    for i, r in enumerate(records):
        for field in ("a", "c", "k"):
            for v in r.get(field) or []:
                idx[field].setdefault(v, []).append(i)
    return idx


def merge(now=None, root=None, hours=MERGE_HOURS, stats=None):
    """Escribe _merged.jsonl y _index.json (dueño: bot_orchestrator). Devuelve la cantidad de ítems."""
    now = now if now is not None else time.time()
    records = collect(now, hours, root, stats)
    base = sources_dir(root)
    base.mkdir(parents=True, exist_ok=True)
    tmp = base / "_merged.jsonl.tmp"
    with tmp.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
    tmp.replace(base / "_merged.jsonl")
    index = {"generated_at": int(now), "hours": hours, "count": len(records), **build_index(records)}
    (base / "_index.json").write_text(json.dumps(index, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    return len(records)


def load(now=None, root=None):
    """_merged.jsonl si está fresco; si no, reconstruye en memoria desde los diarios (no depende del orquestador)."""
    now = now if now is not None else time.time()
    base = sources_dir(root)
    try:
        gen = json.loads((base / "_index.json").read_text(encoding="utf-8")).get("generated_at") or 0
    except (OSError, ValueError, AttributeError):
        gen = 0
    if now - gen <= MERGED_STALE_S:
        return read_jsonl(base / "_merged.jsonl")
    return collect(now, MERGE_HOURS, root)


def matches(r, keyword):
    q = str(keyword or "").strip()
    if not q:
        return False
    if ADDRESS_RE.fullmatch(q):
        return (q.lower() if q.startswith("0x") else q) in (r.get("a") or [])
    if q.startswith("$"):
        return norm.cashtag(q) in (r.get("c") or [])
    low, canon = q.lower(), norm.keyword(q)
    return (q.upper() in (r.get("c") or []) or low in (r.get("k") or []) or canon in (r.get("k") or [])
            or bool(r.get("title") and _kw_pattern(low).search(r["title"])))


def query(keyword, since=None, limit=None, now=None, root=None, records=None):
    """Menciones de `keyword` (dirección, $CASHTAG, cashtag sin $, o palabra clave), más reciente primero."""
    rows = records if records is not None else load(now, root)
    out = [r for r in rows if matches(r, keyword) and (since is None or _when(r) >= since)]
    out.sort(key=_when, reverse=True)
    return out[:limit] if limit else out


def to_items_store(records):
    """Forma de _items.json de script_115: lib_info_signals.mentions la lee sin cambios."""
    return [{"ts": _when(r), "a": r.get("a") or [], "c": r.get("c") or [], "f": f"{r.get('bot')}:{r.get('src')}"}
            for r in records]


def index(records=None, now=None, root=None):
    """Índice (a / c / k) sobre los registros dados o sobre el almacén cargado."""
    return build_index(records if records is not None else load(now, root))


def safe_load(now=None, root=None):
    """load() sin dependencia dura: sin almacén o con error devuelve [] (el scorer sigue con 0 de este aporte)."""
    try:
        return load(now, root)
    except Exception:
        return []


def mention_items(mint, symbol, records):
    """query(mint) + query($symbol) sobre `records`, sin repetir, en la forma de _items.json."""
    hits, seen = [], set()
    for q in [mint] + ([f"${symbol}"] if symbol else []):
        for r in query(q, records=records):
            k = dedup_key(r)
            if k not in seen:
                seen.add(k)
                hits.append(r)
    return to_items_store(hits)


PRELAUNCH_CALENDAR_REL = "02_Analisis/prelaunch/_calendar.json"


def prelaunch_lookup(mint, root=None):
    """D-082: el activo del calendario de preventa (bot_prelaunch_calendar) que nació con este contrato, si el
    calendario lo siguió antes de nacer (prelaunch_known). Solo por contrato exacto: nunca por símbolo. Sin
    calendario, corrupto o sin coincidencia: None. Nunca lanza (el emisor no se bloquea por esto)."""
    addr = norm.address(mint) if mint else None
    if not addr:
        return None
    try:
        doc = json.loads((Path(root or ROOT) / PRELAUNCH_CALENDAR_REL).read_text(encoding="utf-8"))
        assets = (doc.get("assets") or {}).values() if isinstance(doc, dict) else ()
    except (OSError, ValueError, AttributeError):
        return None
    for a in assets:
        if not isinstance(a, dict) or not a.get("prelaunch_known"):
            continue
        if addr in ((a.get("born") or {}).get("contract"), a.get("contract")):
            return a
    return None
