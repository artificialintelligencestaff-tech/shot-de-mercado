#!/usr/bin/env python3
"""
lib_normalize.py — normalización semántica (patrón #19) de los ítems src-1 de los bots de fuentes (doc 34).

Una sola forma canónica para cada cosa que comparan los bots, el almacén, el grafo y los scorers:
  dirección   base58 (Solana) tal cual, validada · EVM 0x en minúsculas · lo demás no es dirección
  cashtag     MAYÚSCULAS sin '$' (1 letra + hasta 14 alfanuméricos)
  keyword     minúsculas, espacios colapsados, sinónimos al término canónico (ALIASES) + grupo a–i
  timestamp   epoch UTC entero; acepta segundos, milisegundos, ISO 8601, RFC 822 y 'YYYY-mm-dd_HHMMSS'
  url         esquema y host en minúsculas, sin fragmento ni parámetros de rastreo (utm_*, ref, fbclid…)
  hash        hex en minúsculas (12–64 caracteres)
  nulos       None, '', 'null', 'none', 'n/a', 'nan' -> None

Se aplica al escribir (lib_sources_store.make_record) y al fusionar (lib_sources_store.collect): cada dueño
normaliza su archivo, nadie reescribe el de otro. `--check` mide cuánto cambiaría sobre los JSONL de sources/.
Solo biblioteca estándar.

Uso: python 04_Config/scripts/lib_normalize.py --check
"""
import json
import re
import sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

VERSION = "norm-0.1"
NULLS = {"", "null", "none", "n/a", "nan", "undefined", "-"}
BASE58 = re.compile(r"[1-9A-HJ-NP-Za-km-z]{32,44}")
EVM = re.compile(r"0x[0-9a-fA-F]{40}")
CASHTAG = re.compile(r"[A-Z][A-Z0-9]{0,14}")
HEX = re.compile(r"[0-9a-f]{12,64}")
TS_MIN, TS_MAX = 946684800, 4102444800          # 2000-01-01 .. 2100-01-01: fuera de eso no es una fecha válida
TRACKING = re.compile(r"^(utm_.*|ref|ref_src|fbclid|gclid|mc_cid|mc_eid|igshid)$", re.IGNORECASE)
# Sinónimos -> término canónico. Las claves y los valores salen de 04_Config/sources/keywords.yaml.
ALIASES = {"meme coin": "memecoin", "meme coins": "memecoin", "memecoins": "memecoin", "pumpfun": "pump.fun",
           "pump fun": "pump.fun", "synthetics": "synthetic", "real world assets": "rwa",
           "real-world assets": "rwa", "tokenized": "tokenization", "listed": "listing", "l2": "layer 2",
           "layer-2": "layer 2", "layer2": "layer 2", "layer-1": "layer 1", "layer1": "layer 1", "l1": "layer 1",
           "perpetuals": "perps", "presales": "presale", "airdrops": "airdrop", "daos": "dao"}


def is_null(value):
    return value is None or (isinstance(value, str) and value.strip().lower() in NULLS)


def address(value):
    """Dirección canónica o None: base58 exacto (32–44, sin 0/O/I/l) o EVM en minúsculas."""
    if is_null(value):
        return None
    s = str(value).strip()
    if EVM.fullmatch(s):
        return s.lower()
    if BASE58.fullmatch(s):
        return s
    return None


def cashtag(value):
    """'$wif' / 'wif' / 'WIF' -> 'WIF'. None si no es un cashtag válido."""
    if is_null(value):
        return None
    s = str(value).strip().lstrip("$").upper()
    return s if CASHTAG.fullmatch(s) else None


def keyword(value):
    """Minúsculas, espacios colapsados, puntuación de los bordes fuera y sinónimo al término canónico."""
    if is_null(value):
        return None
    s = " ".join(str(value).lower().split()).strip(" .,;:!?\"'()[]{}")
    if not s:
        return None
    return ALIASES.get(s, s)


def load_groups(root=None):
    """keyword canónica -> grupo ('a'..'i') desde keywords.yaml. Sin PyYAML o sin archivo: {}."""
    path = Path(root or Path(__file__).resolve().parents[2]) / "04_Config" / "sources" / "keywords.yaml"
    try:
        import yaml
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, ImportError, ValueError):
        return {}
    out = {}
    for group, words in (doc.get("keywords") or {}).items():
        for w in words or []:
            k = keyword(w)
            if k:
                out.setdefault(k, str(group)[:1])
    return out


def keyword_group(word, groups):
    return groups.get(keyword(word) or "")


def timestamp(value):
    """Epoch UTC entero o None. Números > 1e12 se toman como milisegundos."""
    if is_null(value) or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        t = value / 1000 if value > 1e12 else value
    else:
        s = str(value).strip()
        if re.fullmatch(r"\d+(\.\d+)?", s):
            return timestamp(float(s))
        dt = None
        for parse in (lambda x: datetime.strptime(x, "%Y-%m-%d_%H%M%S"),
                      lambda x: datetime.fromisoformat(re.sub(r"(\.\d{6})\d+", r"\1", x).replace("Z", "+00:00")),
                      parsedate_to_datetime):
            try:
                dt = parse(s)
                break
            except (TypeError, ValueError, IndexError):
                continue
        if dt is None:
            return None
        t = (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).timestamp()
    t = int(t)
    return t if TS_MIN <= t <= TS_MAX else None


def url(value):
    """http(s) canónica: esquema y host en minúsculas, sin fragmento, sin parámetros de rastreo, sin '/' final."""
    if is_null(value):
        return None
    s = str(value).strip()
    try:
        parts = urlsplit(s)
    except ValueError:
        return None
    if parts.scheme.lower() not in ("http", "https") or not parts.netloc:
        return None
    query = urlencode([(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if not TRACKING.match(k)])
    path = parts.path.rstrip("/") if parts.path not in ("", "/") else ""
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, query, ""))


def hash_hex(value):
    if is_null(value):
        return None
    s = str(value).strip().lower()
    return s if HEX.fullmatch(s) else None


def _unique(values, fn):
    out = []
    for v in values or []:
        n = fn(v)
        if n and n not in out:
            out.append(n)
    return sorted(out)


def record(r):
    """Copia normalizada de un ítem src-1 (las claves que no conoce quedan igual)."""
    out = dict(r)
    out["a"] = _unique(r.get("a"), address)
    out["c"] = _unique(r.get("c"), cashtag)
    out["k"] = _unique(r.get("k"), keyword)
    out["ts"] = timestamp(r.get("ts"))
    out["seen"] = timestamp(r.get("seen"))
    out["url"] = url(r.get("url"))
    out["h"] = hash_hex(r.get("h"))
    out["au"] = hash_hex(r.get("au"))
    for key in ("id", "title", "src", "bot", "kind"):
        if key in out:
            out[key] = None if is_null(out[key]) else " ".join(str(out[key]).split())
    return out


def check_file(path):
    """Cuántos ítems del JSONL cambiarían al normalizar (no escribe)."""
    total = changed = broken = 0
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError:
        return {"total": 0, "changed": 0, "broken": 0}
    for line in lines:
        try:
            r = json.loads(line)
        except ValueError:
            broken += 1
            continue
        if not isinstance(r, dict):
            broken += 1
            continue
        total += 1
        changed += record(r) != r
    return {"total": total, "changed": changed, "broken": broken}


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description="Normalización semántica de los JSONL de sources/ (solo mide).")
    ap.add_argument("--check", action="store_true", help="cuenta ítems que cambiarían (por defecto)")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parents[2]))
    args = ap.parse_args(argv)
    base = Path(args.root) / "02_Analisis" / "sources"
    tot = {"total": 0, "changed": 0, "broken": 0}
    for path in sorted(base.glob("*/*.jsonl")) + sorted(base.glob("_merged.jsonl")):
        st = check_file(path)
        for k in tot:
            tot[k] += st[k]
        print(f"{path.relative_to(base)}: {st['total']} ítems · cambiarían {st['changed']} · rotos {st['broken']}")
    print(f"TOTAL {tot['total']} ítems · cambiarían {tot['changed']} · rotos {tot['broken']} ({VERSION})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
