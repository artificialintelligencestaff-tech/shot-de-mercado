#!/usr/bin/env python3
"""
bot_runner.py — ejecutor genérico de recetas (Ola 3, D-067; C-005 P5). Una receta YAML = un bot de fuentes sin
código propio. El workflow único sources_runner.yml planifica (--plan) y corre una receta por job de la matriz.

Receta (04_Config/recipes/<nombre>.yaml):
  name: dexpaprika                 [a-z0-9_]{3,33}; no puede pisar la carpeta de otro bot
  kind: json_api                   rss | html_list | json_api | telegram_preview
  url_base: https://...            {secreto} = valor del secret declarado · {subject} / {subjects} = sujetos de eventos
  cadencia_min: 30                 ≥ 10 (el cron corre cada 10 min)
  grupo: a
  src_kind: token                  kind src-1 (news | message | post | repo | tweet | token); default según kind
  extractores:                     dict o lista de {campo: expresión}
    items: "$.results[*]"          JSONPath (json_api) o selector CSS (html_list); rss / telegram: implícito
    id: "$.id"                     campos: id, title, url, ts, author, text (lista), meta.<nombre>
  limite: 50                       máximo de ítems por corrida
  ordenar: {campo: "$.listedAt", desc: true}
  dedup_h: 168
  secreto: HELIUS_API_KEY          (opcional) variable de entorno; sin ella la receta no corre
  sujetos: {tipo: pump_naciente, max: 20, prueba: [...]}   (opcional) sujetos vivos de lib_events

JSONPath soportado (sin dependencias): $ · .campo · ['campo'] · [n] · [*] · .*  (en .* sobre un dict, cada ítem
recibe su clave en `_key`). CSS: "selector", "selector@atributo", "@atributo" (del propio ítem), "." (texto).
Salida: 02_Analisis/sources/<nombre>/<fecha>.jsonl (src-1) + _state.json + _audit.jsonl/_metrics.json (#15).
Habilitación: 04_Config/recipes/_recipes_state.json (dueño: bot_genesis). Un 429 emite `fuente_saturada`.
No guarda cuerpos de texto (src-1): el texto solo se usa para extraer direcciones, cashtags y keywords.
"""
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlsplit

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_audit as audit  # noqa: E402
import lib_events as events  # noqa: E402
import lib_normalize as norm  # noqa: E402
import lib_sources_store as store  # noqa: E402

VERSION = "runner-1.0"
RECIPES_REL = "04_Config/recipes"
STATE_NAME = "_recipes_state.json"
KINDS_RUN = {"rss": "news", "html_list": "post", "json_api": "token", "telegram_preview": "message"}
NAME_RE = re.compile(r"^[a-z0-9_]{3,33}$")         # 33: "runner_" + nombre entra en los 40 de lib_events
RESERVED = {"rss", "telegram", "telegram_b", "orchestrator", "x", "github", "forums", "web", "events"}
CADENCE_MIN = 10
TOLERANCE_S = 120                # el cron no es puntual: vence si faltan menos de 2 min
DEDUP_H = 168
SEEN_MAX = 20000
TIMEOUT_S = 20
HEADERS = {"User-Agent": "ShotDeMercado-runner/1.0 (+public data; contact via repo)"}
FIELDS = ("id", "title", "url", "ts", "author", "text")


def recipes_dir(root=None):
    return Path(root or store.ROOT) / RECIPES_REL


# ---------------------------------------------------------------------------
# Recetas
# ---------------------------------------------------------------------------

def normalize_extractors(ex):
    """Acepta dict o lista de {campo: expresión} (formato de las fichas) y devuelve un dict."""
    if ex is None:
        return {}
    if isinstance(ex, dict):
        return dict(ex)
    if isinstance(ex, list) and all(isinstance(x, dict) and len(x) == 1 for x in ex):
        out = {}
        for x in ex:
            out.update(x)
        return out
    raise ValueError("extractores: dict o lista de {campo: expresión}")


def validate_recipe(r, name_hint=None):
    """Receta normalizada o ValueError con todos los motivos."""
    if not isinstance(r, dict):
        raise ValueError("la receta no es un mapa YAML")
    r = dict(r.get("recipe") or r)
    if name_hint and not r.get("name"):
        r["name"] = name_hint
    errs = []
    name = str(r.get("name") or "")
    if not NAME_RE.match(name):
        errs.append(f"name inválido {name!r}")
    elif name in RESERVED or name.startswith("_"):
        errs.append(f"name {name!r} reservado: es la carpeta de otro bot")
    if r.get("kind") not in KINDS_RUN:
        errs.append(f"kind {r.get('kind')!r} fuera de {sorted(KINDS_RUN)}")
    url = str(r.get("url_base") or "")
    if urlsplit(url).scheme != "https" or not urlsplit(url).netloc:
        errs.append("url_base debe ser https://dominio/...")
    try:
        cad = int(r.get("cadencia_min"))
        if cad < CADENCE_MIN:
            errs.append(f"cadencia_min < {CADENCE_MIN}")
    except (TypeError, ValueError):
        errs.append("cadencia_min no es un entero")
    try:
        r["extractores"] = normalize_extractors(r.get("extractores"))
    except ValueError as e:
        errs.append(str(e))
    else:
        if r.get("kind") in ("json_api", "html_list"):
            for need in ("items", "id"):
                if need not in r["extractores"]:
                    errs.append(f"extractores.{need} es obligatorio para {r.get('kind')}")
    src_kind = r.get("src_kind") or KINDS_RUN.get(r.get("kind"))
    if src_kind not in store.KINDS:
        errs.append(f"src_kind {src_kind!r} fuera de {sorted(store.KINDS)}")
    if r.get("secreto") is not None and not re.match(r"^[A-Z][A-Z0-9_]{2,40}$", str(r["secreto"])):
        errs.append("secreto: nombre de variable de entorno en mayúsculas")
    if ("{secreto}" in url) != bool(r.get("secreto")):
        errs.append("url_base y secreto: {secreto} y la clave `secreto` van juntos")
    suj = r.get("sujetos")
    if ("{subject}" in url or "{subjects}" in url) != bool(suj):
        errs.append("url_base y sujetos: {subject}/{subjects} y la clave `sujetos` van juntos")
    if suj and (not isinstance(suj, dict) or suj.get("tipo") not in events.TYPES):
        errs.append("sujetos.tipo debe ser un tipo de evento de lib_events")
    if errs:
        raise ValueError("; ".join(errs))
    r.update(src_kind=src_kind, cadencia_min=int(r["cadencia_min"]), limite=int(r.get("limite") or 100),
             dedup_h=float(r.get("dedup_h") or DEDUP_H), headers=dict(r.get("headers") or {}))
    return r


def load_recipe(path):
    import yaml
    path = Path(path)
    return validate_recipe(yaml.safe_load(path.read_text(encoding="utf-8")), path.stem)


def load_recipes(root=None):
    out = {}
    for p in sorted(recipes_dir(root).glob("*.yaml")):
        try:
            r = load_recipe(p)
        except Exception:                                       # noqa: BLE001 — la valida bot_genesis
            continue
        out[r["name"]] = r
    return out


def recipes_state(root=None):
    try:
        st = json.loads((recipes_dir(root) / STATE_NAME).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return (st.get("recipes") or {}) if isinstance(st, dict) else {}


def bot_dir(name, root=None):
    return store.sources_dir(root) / name


def load_state(name, root=None):
    try:
        st = json.loads((bot_dir(name, root) / "_state.json").read_text(encoding="utf-8"))
        return st if isinstance(st, dict) else {}
    except (OSError, ValueError):
        return {}


def plan(root=None, now=None):
    """Recetas habilitadas (por bot_genesis) cuya cadencia ya venció."""
    now = now if now is not None else time.time()
    enabled = recipes_state(root)
    due = []
    for name, r in load_recipes(root).items():
        if not (enabled.get(name) or {}).get("enabled"):
            continue
        last = load_state(name, root).get("last_run") or 0
        if now - last >= r["cadencia_min"] * 60 - TOLERANCE_S:
            due.append(name)
    return sorted(due)


# ---------------------------------------------------------------------------
# Extractores
# ---------------------------------------------------------------------------

TOKEN_RE = re.compile(r"\.\*|\[\*\]|\[(\d+)\]|\['([^']+)'\]|\.([A-Za-z_][\w-]*)")


def jsonpath(data, expr):
    """Subconjunto de JSONPath. Devuelve la lista de coincidencias."""
    expr = str(expr).strip()
    if not expr.startswith("$"):
        raise ValueError(f"JSONPath debe empezar con $: {expr!r}")
    pos, nodes = 1, [data]
    while pos < len(expr):
        m = TOKEN_RE.match(expr, pos)
        if not m:
            raise ValueError(f"JSONPath no soportado en {expr[pos:]!r}")
        tok, nxt = m.group(0), []
        for n in nodes:
            if tok in (".*", "[*]"):
                if isinstance(n, list):
                    nxt.extend(n)
                elif isinstance(n, dict):
                    nxt.extend(dict(v, _key=k) if isinstance(v, dict) else v for k, v in n.items())
            elif m.group(1) is not None:
                if isinstance(n, list) and int(m.group(1)) < len(n):
                    nxt.append(n[int(m.group(1))])
            else:
                key = m.group(2) if m.group(2) is not None else m.group(3)
                if isinstance(n, dict) and key in n:
                    nxt.append(n[key])
        nodes, pos = nxt, m.end()
    return nodes


def css(item, expr, base_url):
    expr = str(expr).strip()
    if expr == ".":
        return [item.get_text(" ", strip=True)]
    sel, _, attr = expr.partition("@")
    nodes = [item] if not sel.strip() else item.select(sel.strip())
    out = []
    for n in nodes:
        v = n.get(attr) if attr else n.get_text(" ", strip=True)
        if v:
            out.append(urljoin(base_url, v) if attr in ("href", "src") else v)
    return out


def _first(values):
    for v in values:
        if v not in (None, "", [], {}):
            return v
    return None


def extract_fields(item, ex, kind, base_url):
    get = (lambda e: jsonpath(item, e)) if kind == "json_api" else (lambda e: css(item, e, base_url))
    out, meta = {}, {}
    for field, expr in ex.items():
        if field == "items":
            continue
        exprs = expr if isinstance(expr, list) else [expr]
        values = [v for e in exprs for v in get(e)]
        if field == "text":
            out["text"] = " ".join(str(v) for v in values if isinstance(v, (str, int, float)))
        elif field.startswith("meta."):
            v = _first(values)
            if isinstance(v, (str, int, float, bool)) or v is None:
                meta[field[5:]] = v
        elif field in FIELDS:
            v = _first(values)
            out[field] = v if isinstance(v, (str, int, float)) else None
    out["meta"] = meta
    return out


def parse_payload(recipe, body, base_url):
    """Cuerpo HTTP → [{"id","title","url","ts","author","text","meta"}] según el kind de la receta."""
    kind, ex = recipe["kind"], recipe["extractores"]
    if kind == "rss":
        import bot_rss_news as rss
        return [dict(it, meta={}) for it in rss.parse_items(body)]
    if kind == "telegram_preview":
        import bot_telegram_public as tg
        out = []
        for m in tg.parse_preview(body):
            out.append({"id": m["post"], "title": None, "url": f"https://t.me/{m['post']}", "ts": m["ts"],
                        "author": m["post"].split("/")[0], "text": m["text"], "meta": {"views": m["views"]}})
        return out
    if kind == "json_api":
        items = jsonpath(json.loads(body), ex["items"])
    else:
        from bs4 import BeautifulSoup
        items = BeautifulSoup(body, "html.parser").select(ex["items"])
    out = [extract_fields(it, ex, kind, base_url) for it in items]
    srt = recipe.get("ordenar")
    if kind == "json_api" and isinstance(srt, dict) and srt.get("campo"):
        keyed = [(_first(jsonpath(it, srt["campo"])), o) for it, o in zip(items, out)]
        present = [kv for kv in keyed if kv[0] is not None]
        present.sort(key=lambda kv: (0, kv[0], "") if isinstance(kv[0], (int, float)) else (1, 0, str(kv[0])),
                     reverse=bool(srt.get("desc")))
        out = [o for _, o in present] + [o for k, o in keyed if k is None]      # sin valor: al final
    return [o for o in out if o.get("id")]


# ---------------------------------------------------------------------------
# HTTP y corrida
# ---------------------------------------------------------------------------

def http_fetch(url, headers=None):
    """(estado, texto|None, url final). Nunca lanza."""
    import requests
    try:
        r = requests.get(url, headers={**HEADERS, **(headers or {})}, timeout=TIMEOUT_S)
    except requests.RequestException as e:
        return f"error {type(e).__name__}", None, url
    return r.status_code, (r.text if r.status_code == 200 else None), r.url


def subjects_for(recipe, now, root=None, sample=False):
    suj = recipe.get("sujetos") or {}
    if sample:
        return list(suj.get("prueba") or [])[: int(suj.get("max") or 20)]
    evs = events.read_events(types=suj["tipo"], now=now, root=root)
    seen, out = set(), []
    for e in reversed(evs):                                       # los más nuevos primero
        if e["subject"] not in seen:
            seen.add(e["subject"])
            out.append(e["subject"])
    return out[: int(suj.get("max") or 20)]


def urls_for(recipe, subjects, secret):
    url = recipe["url_base"]
    if secret is not None:
        url = url.replace("{secreto}", secret)
    if "{subjects}" in url:
        return [url.replace("{subjects}", ",".join(subjects))] if subjects else []
    if "{subject}" in url:
        return [url.replace("{subject}", s) for s in subjects]
    return [url]


def collect(recipe, now=None, fetch=http_fetch, root=None, sample_subjects=False):
    """Descarga y parsea sin escribir nada. Devuelve (ítems, {"status", "error", "calls"})."""
    now = now if now is not None else time.time()
    secret = None
    if recipe.get("secreto"):
        secret = os.environ.get(recipe["secreto"])
        if not secret:
            return [], {"status": "sin_secreto", "error": f"falta {recipe['secreto']}", "calls": 0}
    subjects = subjects_for(recipe, now, root, sample_subjects) if recipe.get("sujetos") else []
    urls = urls_for(recipe, subjects, secret)
    if not urls:
        return [], {"status": "sin_sujetos", "error": None, "calls": 0}
    items, status, error = [], None, None
    for url in urls:
        st, body, final = fetch(url, recipe["headers"])
        status = st
        if st != 200 or body is None:
            error = f"HTTP {st}"
            continue
        try:
            items += parse_payload(recipe, body, final or url)
        except Exception as e:                                    # noqa: BLE001 — un parser roto es un error de la receta
            status, error = "parse_error", f"{type(e).__name__}: {e}"[:200]
    return items[: recipe["limite"]], {"status": status, "error": error, "calls": len(urls)}


def run_recipe(recipe, now=None, fetch=http_fetch, root=None, write=True):
    t0 = time.time()
    now = now if now is not None else time.time()
    name = recipe["name"]
    state = load_state(name, root)
    seen = {k: v for k, v in (state.get("seen") or {}).items() if now - v <= recipe["dedup_h"] * 3600}
    items, info = collect(recipe, now, fetch, root)
    records = []
    for it in items:
        key = f"{it['id']}"
        if key in seen:
            continue
        seen[key] = now
        meta = dict(it.get("meta") or {}, grupo=recipe.get("grupo"))
        records.append(store.make_record(name, name, recipe["src_kind"], it.get("text") or "", id=str(it["id"]),
                                         url=it.get("url"), ts=norm.timestamp(it.get("ts")), seen=now,
                                         title=it.get("title"), author=it.get("author"), meta=meta))
    ok = info["status"] in (200, "sin_sujetos") and not info["error"]       # sin sujetos: nada que hacer, no es falla
    if len(seen) > SEEN_MAX:
        seen = dict(sorted(seen.items(), key=lambda kv: kv[1])[-SEEN_MAX:])
    new_state = {"version": VERSION, "recipe": name, "kind": recipe["kind"], "last_run": int(now),
                 "last_ok": int(now) if ok else state.get("last_ok"), "status": info["status"], "error": info["error"],
                 "items": len(items), "new": len(records), "calls": info["calls"],
                 "fails": 0 if ok else int(state.get("fails") or 0) + 1, "seen": seen,
                 "duration_s": round(time.time() - t0, 3)}
    if write:
        folder = bot_dir(name, root)
        store.append_records(name, records, when=now, root=root)
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "_state.json").write_text(json.dumps(new_state, ensure_ascii=False, indent=1, sort_keys=True),
                                            encoding="utf-8")
        line = audit.audit_line(name, now, len(items), len(records), 0 if ok else 1, 1, new_state["duration_s"])
        audit.record_run(folder, line, 1 if ok else 0, 1)
        if info["status"] == 429:
            events.write_event("fuente_saturada", f"recipe/{name}", 1, {"calls": info["calls"]},
                               writer=f"runner_{name}", now=now, root=root)
    return {"name": name, "records": records, "state": new_state}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Ejecutor genérico de recetas (Ola 3)")
    ap.add_argument("--plan", action="store_true", help="lista las recetas que tocan ahora (JSON)")
    ap.add_argument("--github-output", action="store_true", help="con --plan: escribe matrix/any en $GITHUB_OUTPUT")
    ap.add_argument("--recipe", help="nombre de la receta a correr")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    if a.plan:
        due = plan()
        print(json.dumps(due))
        if a.github_output and os.environ.get("GITHUB_OUTPUT"):
            with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
                f.write(f"matrix={json.dumps(due)}\nany={'true' if due else 'false'}\n")
        return 0
    if not a.recipe:
        ap.error("--plan o --recipe <nombre>")
    recipe = load_recipe(recipes_dir() / f"{a.recipe}.yaml")
    out = run_recipe(recipe, write=not a.dry_run)
    st = out["state"]
    print(f"{recipe['name']}: {st['new']} nuevos de {st['items']} · estado {st['status']}"
          + (f" · {st['error']}" if st["error"] else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
