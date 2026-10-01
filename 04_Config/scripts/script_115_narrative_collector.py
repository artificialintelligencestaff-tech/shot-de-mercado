#!/usr/bin/env python3
"""
script_115_narrative_collector.py — Colector de menciones (doc 26, Fase 0). SOLO registra: no puntúa ni emite.

Cada 20 min (workflow narrative_collector.yml):
  1. Candidatos: tokens de shadow_v4/_accumulated.json con score >= 40 puntuados en las últimas 48 h. Un token
     que entra se sigue 48 h desde su entrada aunque después baje su score (la Fase 1 necesita la serie completa).
  2. Fuentes: las familias de menciones que la sonda marcó OK desde Actions
     (02_Analisis/diagnostics/narrative_sources_probe.json): Reddit RSS, Telegram t.me/s, 4chan /biz/, HN, RSS de
     noticias. CoinGecko trending se guarda como dato de atención (no son menciones). GDELT queda fuera siempre:
     da volumen agregado de noticias, no menciones de un activo.
  3. De cada ítem se guardan SOLO identificadores: direcciones (base58 / 0x…), cashtags, nombres de candidatos
     encontrados, timestamp, fuente, hash del texto normalizado y hash con sal del autor. Sin textos ni handles.
     El almacén es rodante (26 h) y es el baseline de 24 h de la métrica.
  4. Por candidato: lib_repetition.repetition_snapshot (doc 26 v0.1: intensidad, sorpresa de Poisson, fuentes
     efectivas, diversidad de autores) -> 02_Analisis/narrative/<mint>.json, con historial de 24 h.

No toca script_82, script_97 ni el score. Sin secretos, sin envíos, sin cuentas ni cookies.
Parámetros heurísticos, no calibrados (doc 26 §6).

Uso: python 04_Config/scripts/script_115_narrative_collector.py [--dry-run] [--families reddit_rss,4chan_biz]
                                                                 [--min-score 40] [--track-hours 48]
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import requests

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_repetition as rep  # noqa: E402
import probe_narrative_sources as probe  # noqa: E402

ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
ACCUMULATED_FILE = ROOT / "02_Analisis" / "shadow_v4" / "_accumulated.json"
PROBE_FILE = ROOT / "02_Analisis" / "diagnostics" / "narrative_sources_probe.json"
OUT_DIR = ROOT / "02_Analisis" / "narrative"
ITEMS_NAME, INDEX_NAME = "_items.json", "_index.json"

COLLECTOR_VERSION = "115-1.0"
MIN_SCORE = 40                 # directiva Fase 5: candidatos >= 40 (el umbral de emisión es 56)
TRACK_HOURS = 48               # horizonte de la métrica dual
STORE_HOURS = 26               # baseline 24 h + hora actual + margen
HISTORY_HOURS = 24             # historial por token
RUNS_MAX = 72                  # 24 h de corridas cada 20 min
MAX_TRACKED = 100              # tope de archivos por corrida (por score)
FUTURE_SLACK_S = 600           # ítems con timestamp > ahora + 10 min se descartan
# Solo ASCII: con un User-Agent no ASCII, 4chan y Decrypt respondían 403 [V, 01/10, doc 26 §9].
HEADERS = {"User-Agent": "shot-de-mercado-collector/1.0 (research; repo artificialintelligencestaff-tech/shot-de-mercado)"}
TIMEOUT_S = 20
EXCLUDED_FAMILIES = {"gdelt": "volumen agregado de noticias, no menciones por activo"}
ATTENTION_FAMILIES = {"coingecko_trending"}
JSON_PARSERS = {"4chan", "hn", "coingecko", "gdelt"}
# Cashtags que en las fuentes casi siempre nombran a otro activo (majors, stablecoins, monedas fiat).
CASHTAG_STOPLIST = {"BTC", "ETH", "SOL", "USDC", "USDT", "USD", "EUR", "BNB", "XRP", "DOGE", "ADA", "TRX", "TON",
                    "AVAX", "DOT", "LINK", "LTC", "BCH", "SHIB", "DAI", "WETH", "WSOL", "WBTC"}
# Pseudonimización: sin handles en el repo. Con la sal por defecto (pública) es un seudónimo, no anonimato.
AUTHOR_SALT = os.environ.get("NARRATIVE_AUTHOR_SALT") or "shot-de-mercado/rep-0.1"

BASE58_RE = re.compile(r"(?<![1-9A-HJ-NP-Za-km-z])[1-9A-HJ-NP-Za-km-z]{32,44}(?![1-9A-HJ-NP-Za-km-z])")
EVM_RE = re.compile(r"(?<![0-9A-Za-z])0x[0-9a-fA-F]{40}(?![0-9a-fA-F])")
CASHTAG_RE = re.compile(r"(?<![\w$])\$([A-Za-z][A-Za-z0-9]{0,14})(?!\w)")
SYMBOL_OK = re.compile(r"[A-Za-z][A-Za-z0-9]{1,14}")
SAFE_KEY = re.compile(r"[1-9A-HJ-NP-Za-km-z]{32,44}|0x[0-9a-f]{40}")


# ---------------------------------------------------------------------------
# Identificadores (lo único que se guarda de cada ítem)
# ---------------------------------------------------------------------------

def normalize_address(address):
    """EVM en minúsculas; base58 exacto (distingue mayúsculas). Igual que script_97.normalize_mint."""
    if not isinstance(address, str):
        return ""
    address = address.strip()
    return address.lower() if re.fullmatch(r"0x[0-9a-fA-F]{40}", address) else address


def extract_identifiers(text):
    """Direcciones (base58 de 32-44 caracteres, 0x + 40 hex) y cashtags que aparecen en el texto."""
    text = text or ""
    addresses = set(BASE58_RE.findall(text)) | {a.lower() for a in EVM_RE.findall(text)}
    cashtags = {c.upper() for c in CASHTAG_RE.findall(text)}
    return sorted(addresses), sorted(cashtags)


def name_pattern(name):
    """Mismo criterio que lib_repetition.match_weight: nombre completo, sin letras pegadas, sin mayúsculas."""
    return re.compile(rf"(?<!\w){re.escape(name)}(?!\w)", re.IGNORECASE)


def author_hash(author):
    if not author:
        return None
    return hashlib.sha256(f"{AUTHOR_SALT}|{author.strip().lower()}".encode("utf-8")).hexdigest()[:12]


def item_weight(item, token):
    """Peso de la mención más fuerte del ítem para el token (contrato 1,0 · cashtag 0,5 · nombre 0,25).

    Reproduce lib_repetition.match_weight sobre los identificadores guardados, sin el texto.
    """
    if token["address"] and token["address"] in item.get("a", ()):
        return rep.MATCH_WEIGHTS["ca"]
    if token.get("cashtag") and token["cashtag"] in item.get("c", ()):
        return rep.MATCH_WEIGHTS["cashtag"]
    if token["key"] in item.get("n", ()):
        return rep.MATCH_WEIGHTS["name"]
    return 0.0


# ---------------------------------------------------------------------------
# Candidatos
# ---------------------------------------------------------------------------

def parse_iso(value):
    if not isinstance(value, str) or not value:
        return None
    try:
        dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    return (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).timestamp()


def iso(epoch):
    return datetime.fromtimestamp(epoch, timezone.utc).isoformat(timespec="seconds")


def _token_fields(key, rec):
    tok = rec.get("token") if isinstance(rec.get("token"), dict) else {}
    ms = rec.get("ms_data") if isinstance(rec.get("ms_data"), dict) else {}
    return {"address": normalize_address(tok.get("mint") or rec.get("mint") or key),
            "symbol": (tok.get("symbol") or rec.get("symbol") or ms.get("symbol") or "").strip() or None,
            "name": (tok.get("name") or rec.get("name") or ms.get("name") or "").strip() or None,
            "chain": tok.get("chain") or rec.get("chain") or "solana"}


def name_counts(accumulated):
    """Cuántos tokens del acumulado comparten cada nombre (en minúsculas): un nombre repetido es ambiguo."""
    counts = Counter()
    for key, rec in accumulated.items():
        if isinstance(rec, dict):
            name = _token_fields(key, rec)["name"]
            if name:
                counts[" ".join(name.lower().split())] += 1
    return counts


def describe_token(key, fields, names):
    """Identificadores con los que se cuenta el token, y por qué se excluye cada uno que no aplica."""
    token = {"key": key, "address": fields["address"], "symbol": fields["symbol"], "name": fields["name"],
             "chain": fields["chain"], "cashtag": None, "name_match": None, "excluded": {}}
    sym = fields["symbol"]
    if not sym or not SYMBOL_OK.fullmatch(sym):
        token["excluded"]["cashtag"] = "símbolo vacío, de 1 carácter o con caracteres fuera de [A-Za-z0-9]"
    elif sym.upper() in CASHTAG_STOPLIST:
        token["excluded"]["cashtag"] = f"${sym.upper()} nombra casi siempre a otro activo (lista de exclusión)"
    else:
        token["cashtag"] = sym.upper()
    name = fields["name"]
    if not name or len(name.split()) < 2:
        token["excluded"]["name"] = "nombre de menos de 2 palabras (doc 26 §2)"
    elif names.get(" ".join(name.lower().split()), 0) > 1:
        token["excluded"]["name"] = f"nombre compartido por {names[' '.join(name.lower().split())]} tokens del acumulado"
    else:
        token["name_match"] = name
    return token


def current_scoring_version(accumulated):
    """Versión del scorer vigente = la del registro puntuado más recientemente (se adapta sola al cambiar)."""
    best, version = None, None
    for rec in accumulated.values():
        if isinstance(rec, dict) and rec.get("scoring_version"):
            ts = parse_iso(rec.get("detected_at"))
            if ts is not None and (best is None or ts > best):
                best, version = ts, rec["scoring_version"]
    return version


def select_tracked(accumulated, previous, now, min_score=MIN_SCORE, track_hours=TRACK_HOURS, cap=MAX_TRACKED):
    """Tokens a seguir: los nuevos (score >= min_score con el scorer vigente, puntuados en la ventana) + los que
    siguen en su ventana. Un score de otra versión no cuenta: los 100 de v7.2 eran inflación (doc 20).

    `previous` = {key: {"first_tracked_at": iso, ...}} de la corrida anterior. Devuelve (tracked, stats).
    """
    window = track_hours * 3600
    names = name_counts(accumulated)
    by_key = {normalize_address(k): rec for k, rec in accumulated.items()}
    version = current_scoring_version(accumulated)
    tracked = {}
    stats = {"new": 0, "kept": 0, "expired": 0, "capped": 0, "other_version": 0, "scoring_version": version}
    for key, info in (previous or {}).items():
        since = parse_iso(info.get("first_tracked_at"))
        if since is None or now - since >= window:
            stats["expired"] += 1
            continue
        rec = by_key.get(key) if isinstance(by_key.get(key), dict) else {}
        fields = _token_fields(key, rec) if rec else {k: info.get(k) for k in ("address", "symbol", "name", "chain")}
        token = describe_token(key, fields, names)
        token.update(first_tracked_at=info["first_tracked_at"],
                     score=rec.get("score", info.get("score")),
                     scoring_version=rec.get("scoring_version", info.get("scoring_version")),
                     detected_at=rec.get("detected_at", info.get("detected_at")))
        tracked[key] = token
        stats["kept"] += 1
    fresh = []
    for key, rec in by_key.items():
        if key in tracked or not isinstance(rec, dict):
            continue
        score = rec.get("score")
        detected = parse_iso(rec.get("detected_at"))
        if not isinstance(score, (int, float)) or isinstance(score, bool) or score < min_score:
            continue
        if detected is None or now - detected > window or detected > now + FUTURE_SLACK_S:
            continue
        if rec.get("scoring_version") != version:
            stats["other_version"] += 1
            continue
        if not SAFE_KEY.fullmatch(key):
            continue
        fresh.append((score, key, _token_fields(key, rec), rec))
    fresh.sort(key=lambda x: (-x[0], x[1]))
    room = max(0, cap - len(tracked))
    stats["capped"] = max(0, len(fresh) - room)
    for score, key, fields, rec in fresh[:room]:
        token = describe_token(key, fields, names)
        token.update(first_tracked_at=iso(now), score=score, scoring_version=rec.get("scoring_version"),
                     detected_at=rec.get("detected_at"))
        tracked[token["key"]] = token
        stats["new"] += 1
    return tracked, stats


# ---------------------------------------------------------------------------
# Fuentes
# ---------------------------------------------------------------------------

def select_families(probe_report, requested=None):
    """Familias a consultar: las pedidas, o las que la sonda marcó OK, o todas (sin sonda). GDELT nunca."""
    known = [f for f in probe.SOURCES if f not in EXCLUDED_FAMILIES]
    skipped = dict(EXCLUDED_FAMILIES)
    if requested:
        unknown = [f for f in requested if f not in probe.SOURCES]
        if unknown:
            raise ValueError(f"familias desconocidas: {unknown}")
        used = [f for f in known if f in requested]
        skipped.update({f: "no pedida (--families)" for f in known if f not in requested})
        return used, skipped, "cli"
    fams = (probe_report or {}).get("families") if isinstance(probe_report, dict) else None
    if not isinstance(fams, dict) or not fams:
        return known, skipped, "sin sonda: todas"
    used = [f for f in known if (fams.get(f) or {}).get("ok")]
    skipped.update({f: "la sonda la marcó sin datos" for f in known if f not in used})
    return used, skipped, f"sonda {probe_report.get('runner')} {probe_report.get('generated_at')}"


def fetch(session, url, parser):
    """Una request. Nunca lanza: devuelve (status, payload|None)."""
    try:
        r = session.get(url, headers=HEADERS, timeout=TIMEOUT_S)
    except requests.RequestException as e:
        return f"error {type(e).__name__}", None
    if r.status_code != 200:
        return r.status_code, None
    try:
        return 200, (r.json() if parser in JSON_PARSERS else r.text)
    except ValueError:
        return "error json", None


def collect_items(session, families, sleep=time.sleep):
    """Descarga y parsea las familias. Devuelve (ítems de menciones, filas de estado, trending de CoinGecko)."""
    items, statuses, trending, first = [], [], None, True
    for family in families:
        _, endpoints = probe.SOURCES[family]
        for name, url, parser, pause in endpoints:
            if not first:
                sleep(pause)
            first = False
            status, payload = fetch(session, url, parser)
            row = {"family": family, "name": name, "status": status, "items": 0}
            if status == 200:
                if family in ATTENTION_FAMILIES:
                    trending = coingecko_trending(payload)
                    row["items"] = len(trending)
                else:
                    try:
                        parsed = rep.PARSERS[parser](payload, name)
                    except Exception as e:      # 200 que no se puede leer (HTML en lugar de XML, etc.)
                        row["parse_error"] = f"{type(e).__name__}: {str(e)[:100]}"
                        parsed = []
                    for it in parsed:
                        it["family"] = family
                    items += parsed
                    row["items"] = len(parsed)
            statuses.append(row)
    return items, statuses, trending


def coingecko_trending(data):
    out = []
    for i, c in enumerate((data or {}).get("coins") or [], start=1):
        it = c.get("item") or {}
        out.append({"rank": i, "id": it.get("id"), "symbol": (it.get("symbol") or "").upper() or None,
                    "name": it.get("name"), "market_cap_rank": it.get("market_cap_rank")})
    return out


# ---------------------------------------------------------------------------
# Almacén rodante de 26 h (sin textos ni handles)
# ---------------------------------------------------------------------------

def ingest(store_items, raw_items, tracked, now):
    """Agrega al almacén los ítems con al menos un identificador. Dedup por (fuente, texto normalizado).

    Un ítem ya guardado suma los nombres de candidatos nuevos que lo mencionan (retroactivo mientras el ítem
    siga en el feed). Devuelve {"added", "updated", "seen", "with_ids"}.
    """
    patterns = {k: name_pattern(t["name_match"]) for k, t in tracked.items() if t.get("name_match")}
    by_key = {it["k"]: it for it in store_items}
    stats = {"seen": 0, "with_ids": 0, "added": 0, "updated": 0}
    for raw in raw_items:
        ts = raw.get("ts")
        if not isinstance(ts, (int, float)) or ts > now + FUTURE_SLACK_S or ts <= now - STORE_HOURS * 3600:
            continue
        stats["seen"] += 1
        text = raw.get("text") or ""
        addresses, cashtags = extract_identifiers(text)
        names = sorted(k for k, p in patterns.items() if p.search(text))
        if not (addresses or cashtags or names):
            continue
        stats["with_ids"] += 1
        key = f"{raw.get('source')}|{rep.normalized_hash(text)[:16]}"
        old = by_key.get(key)
        if old is not None:
            merged = sorted(set(old.get("n", [])) | set(names))
            if merged != old.get("n", []):
                old["n"] = merged
                stats["updated"] += 1
            continue
        record = {"k": key, "s": raw.get("source"), "f": raw.get("family"), "ts": float(ts),
                  "a": addresses, "c": cashtags, "n": names, "u": author_hash(raw.get("author"))}
        store_items.append(record)
        by_key[key] = record
        stats["added"] += 1
    return stats


def prune(store_items, now):
    keep = [it for it in store_items if it.get("ts", 0) > now - STORE_HOURS * 3600]
    return keep, len(store_items) - len(keep)


# ---------------------------------------------------------------------------
# Métrica por token
# ---------------------------------------------------------------------------

def token_snapshot(token, store_items, now, sources_total=None):
    """lib_repetition.repetition_snapshot sobre las menciones del token en el almacén + desgloses."""
    found, by_match = [], Counter()
    for it in store_items:
        w = item_weight(it, token)
        if w:
            found.append({"ts": it["ts"], "source": it["s"], "weight": w, "author": it.get("u")})
            by_match[{1.0: "ca", 0.5: "cashtag", 0.25: "name"}[w]] += 1
    snap = rep.repetition_snapshot(found, now, sources_total=sources_total)
    by_source = Counter()
    for m in found:
        if now - 3600 < m["ts"] <= now:
            by_source[m["source"]] += m["weight"]
    snap["by_source_1h"] = dict(sorted(by_source.items()))
    snap["mentions_by_match_26h"] = dict(sorted(by_match.items()))
    snap["mentions_26h"] = len(found)
    return snap


def trending_hit(token, trending):
    """Aparece en el top de búsquedas de CoinGecko con el mismo símbolo Y el mismo nombre (dato de atención)."""
    for t in trending or []:
        if (token.get("symbol") and t.get("symbol") == token["symbol"].upper()
                and (t.get("name") or "").strip().lower() == (token.get("name") or "").strip().lower()):
            return {"rank": t["rank"], "id": t["id"]}
    return None


def token_document(token, snap, previous_doc, now, coverage_h, trending):
    entry = {"at": iso(now), "m_1h": snap["m_1h"], "intensity": round(snap["intensity"], 4),
             "surprise_nats": round(snap["surprise_nats"], 4), "seff_1h": round(snap["seff_1h"], 4),
             "tier": snap["tier"], "signal": snap["signal"]}
    history = [h for h in (previous_doc or {}).get("history") or []
               if (parse_iso(h.get("at")) or 0) > now - HISTORY_HOURS * 3600]
    history.append(entry)
    first = (previous_doc or {}).get("first_snapshot") or dict(entry, baseline_coverage_h=coverage_h)
    return {
        "collector_version": COLLECTOR_VERSION, "metric_version": rep.VERSION, "updated_at": iso(now),
        "token": {k: token.get(k) for k in ("key", "chain", "symbol", "name", "score", "scoring_version",
                                            "detected_at", "first_tracked_at")},
        "identifiers": {"address": token["address"], "cashtag": f"${token['cashtag']}" if token.get("cashtag") else None,
                        "name": token.get("name_match"), "excluded": token.get("excluded") or {}},
        "baseline_coverage_h": coverage_h,
        "snapshot": snap,
        "coingecko_trending": trending_hit(token, trending),
        "first_snapshot": first,
        "history": history,
        "method": "doc 26 v0.1 · parámetros heurísticos no calibrados · solo dato: no modifica el score",
    }


# ---------------------------------------------------------------------------
# Corrida
# ---------------------------------------------------------------------------

def read_json(path, default):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def write_json_atomic(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, path)


def run(session=None, now=None, families=None, min_score=MIN_SCORE, track_hours=TRACK_HOURS, dry_run=False,
        sleep=time.sleep, accumulated_file=None, probe_file=None, out_dir=None):
    """Una corrida completa. Devuelve el índice (lo que se escribe en _index.json)."""
    now = time.time() if now is None else now
    out_dir = Path(out_dir or OUT_DIR)
    accumulated = read_json(accumulated_file or ACCUMULATED_FILE, {})
    if not isinstance(accumulated, dict):
        accumulated = {}
    previous_index = read_json(out_dir / INDEX_NAME, {})
    store = read_json(out_dir / ITEMS_NAME, {})
    store_items = store.get("items") if isinstance(store, dict) and isinstance(store.get("items"), list) else []
    first_run_at = (store.get("first_run_at") if isinstance(store, dict) else None) or iso(now)

    tracked, track_stats = select_tracked(accumulated, previous_index.get("tracked"), now, min_score, track_hours)
    used, skipped, origin = select_families(read_json(probe_file or PROBE_FILE, None), families)
    raw_items, statuses, trending = collect_items(session or requests.Session(), used, sleep=sleep)
    ingest_stats = ingest(store_items, raw_items, tracked, now)
    store_items, pruned = prune(store_items, now)
    coverage_h = round(min(24.0, max(0.0, (now - parse_iso(first_run_at)) / 3600)), 2)
    sources_ok = sorted({r["name"] for r in statuses if r["status"] == 200 and r["family"] not in ATTENTION_FAMILIES})

    summary, docs = [], {}
    for key, token in tracked.items():
        snap = token_snapshot(token, store_items, now, sources_total=len(sources_ok))
        doc = token_document(token, snap, read_json(out_dir / f"{key}.json", None), now, coverage_h, trending)
        docs[key] = doc
        summary.append({"key": key, "symbol": token.get("symbol"), "score": token.get("score"),
                        "m_1h": snap["m_1h"], "mentions_26h": snap["mentions_26h"],
                        "intensity": round(snap["intensity"], 4), "surprise_nats": round(snap["surprise_nats"], 4),
                        "tier": snap["tier"], "signal": snap["signal"]})
    summary.sort(key=lambda s: (-s["intensity"], s["key"]))

    run_row = {"at": iso(now), "sources_ok": len(sources_ok), "sources_total": len(statuses),
               "items_seen": ingest_stats["seen"], "added": ingest_stats["added"], "tracked": len(tracked),
               "signals": sum(s["signal"] for s in summary)}
    index = {
        "collector_version": COLLECTOR_VERSION, "metric_version": rep.VERSION, "generated_at": iso(now),
        "runner": "github-actions" if os.environ.get("GITHUB_ACTIONS") == "true" else "local",
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "params": {"min_score": min_score, "track_hours": track_hours, "store_hours": STORE_HOURS,
                   "alpha": rep.ALPHA, "beta": rep.BETA, "lambda_min": rep.LAMBDA_MIN, "min_mentions": rep.MIN_MENTIONS,
                   "surprise_min_nats": round(rep.SURPRISE_MIN, 3), "seff_min": rep.SEFF_MIN,
                   "authors_min": rep.AUTHORS_MIN, "weights": rep.MATCH_WEIGHTS, "calibrated": False},
        "families": {"used": used, "skipped": skipped, "origin": origin},
        "sources": statuses,
        "store": {"items": len(store_items), "pruned": pruned, "first_run_at": first_run_at,
                  "baseline_coverage_h": coverage_h, **ingest_stats},
        "coingecko_trending": trending,
        "tracking": track_stats,
        "tracked": {k: {f: t.get(f) for f in ("address", "symbol", "name", "chain", "score", "scoring_version",
                                               "detected_at", "first_tracked_at")} for k, t in tracked.items()},
        "summary": summary,
        "runs": ((previous_index.get("runs") or [])[-(RUNS_MAX - 1):]) + [run_row],
    }
    if not dry_run:
        for key, doc in docs.items():
            write_json_atomic(out_dir / f"{key}.json", doc)
        write_json_atomic(out_dir / ITEMS_NAME, {"metric_version": rep.VERSION, "collector_version": COLLECTOR_VERSION,
                                                 "first_run_at": first_run_at, "updated_at": iso(now),
                                                 "items": sorted(store_items, key=lambda it: (it["ts"], it["k"]))})
        write_json_atomic(out_dir / INDEX_NAME, index)
    return index


def main(argv=None):
    ap = argparse.ArgumentParser(description="Colector de menciones (doc 26 Fase 0): registra, no puntúa ni emite.")
    ap.add_argument("--families", default="", help="subconjunto de familias de la sonda (por defecto: las OK)")
    ap.add_argument("--min-score", type=float, default=MIN_SCORE)
    ap.add_argument("--track-hours", type=float, default=TRACK_HOURS)
    ap.add_argument("--dry-run", action="store_true", help="consulta y calcula, sin escribir archivos")
    args = ap.parse_args(argv)
    requested = [f for f in args.families.split(",") if f] or None
    try:
        index = run(families=requested, min_score=args.min_score, track_hours=args.track_hours, dry_run=args.dry_run)
    except ValueError as e:
        ap.error(str(e))
    ok = sum(1 for s in index["sources"] if s["status"] == 200)
    print(f"[115] familias: {', '.join(index['families']['used']) or 'ninguna'} ({index['families']['origin']}) · "
          f"endpoints OK {ok}/{len(index['sources'])}")
    for s in index["sources"]:
        print(f"      {s['family']}/{s['name']}: {s['status']} · ítems {s['items']}"
              f"{' · ' + s['parse_error'] if s.get('parse_error') else ''}")
    st = index["store"]
    print(f"[115] almacén: {st['items']} ítems con identificadores (+{st['added']}, -{st['pruned']}) · "
          f"cobertura del baseline {st['baseline_coverage_h']} h · seguidos {len(index['tracked'])} "
          f"(nuevos {index['tracking']['new']}, vencidos {index['tracking']['expired']})")
    for s in index["summary"][:15]:
        print(f"[115] {s['symbol'] or '?':<12} m_1h {s['m_1h']:.2f} · 26h {s['mentions_26h']} · "
              f"intensidad {s['intensity']:.2f} · sorpresa {s['surprise_nats']:.2f} nats · {s['tier']}"
              f"{' · SEÑAL' if s['signal'] else ''}")
    print("[115] dry-run: sin escritura" if args.dry_run else f"[OK] {OUT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
