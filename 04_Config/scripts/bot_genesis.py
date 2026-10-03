#!/usr/bin/env python3
"""
bot_genesis.py — bot padre (Ola 3, D-067; C-005 P5). Corre una vez por día (sources_genesis.yml).

1. Lee las fichas _servicios_open_source/*/<nombre>.md. Si una ficha tiene un bloque YAML con la clave `recipe:`,
   genera 04_Config/recipes/<nombre>.yaml con la cabecera GENERATED. Una receta escrita a mano (sin la cabecera)
   nunca se pisa. Una receta generada cuya ficha ya no tiene bloque se retira (se borra: lo que no sirve se elimina).
2. Valida TODAS las recetas (generadas y manuales):
     esquema (bot_runner.validate_recipe) · secret presente si lo declara · dominio no duplicado (contra otras
     recetas, contra los feeds de rss.yaml y contra los canales de telegram.yaml) · fetch en seco · ≥ 5 ítems.
3. Escribe 04_Config/recipes/_recipes_state.json (dueño: este bot):
     pasa → enabled: true · falla → status "probation" con el motivo.
   Una receta ya habilitada pasa a probation recién al segundo día seguido con fallas [H]: un 5xx pasajero no la
   apaga un día entero.
NO escribe código ni crea workflows: solo configuración. Cero IA generativa (doc 34).
Uso: python 04_Config/scripts/bot_genesis.py [--dry-run] [--no-write-recipes]
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlsplit

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import bot_runner as runner  # noqa: E402
import lib_sources_store as store  # noqa: E402

VERSION = "genesis-1.0"
FICHAS_REL = "_servicios_open_source"
GENERATED = "# generado por bot_genesis desde"
MIN_ITEMS = 5
STRIKES_TO_PROBATION = 2
FENCE_RE = re.compile(r"```(?:ya?ml)?[ \t]*\n(.*?)```", re.DOTALL)


def recipe_block(markdown):
    """El primer bloque ```yaml``` de la ficha que es un mapa con la clave `recipe` (o None)."""
    import yaml
    for m in FENCE_RE.finditer(markdown):
        try:
            doc = yaml.safe_load(m.group(1))
        except yaml.YAMLError:
            continue
        if isinstance(doc, dict) and isinstance(doc.get("recipe"), dict):
            return doc["recipe"]
    return None


def fichas(root=None):
    base = Path(root or store.ROOT) / FICHAS_REL
    out = {}
    for p in sorted(base.glob("*/*.md")):
        if p.name.startswith("_") or p.name.lower() == "readme.md":
            continue
        block = recipe_block(p.read_text(encoding="utf-8"))
        if block is not None:
            out[str(block.get("name") or p.stem)] = {"block": block, "source": p.relative_to(base.parent).as_posix()}
    return out


def render(name, block, source):
    import yaml
    body = dict(block, name=name)
    return f"{GENERATED} {source} — se regenera; para editar, cambiar la ficha\n" + \
        yaml.safe_dump(body, allow_unicode=True, sort_keys=False)


def domain_key(recipe):
    """Lo que no se puede duplicar: el dominio, salvo en Telegram (el mismo t.me sirve a canales distintos)."""
    u = urlsplit(recipe["url_base"])
    host = u.netloc.lower().removeprefix("www.")
    if recipe["kind"] == "telegram_preview":
        return f"t.me/{u.path.rstrip('/').split('/')[-1].lower()}"
    return host


def existing_domains(root=None):
    """Dominios ya cubiertos por los bots de código: feeds de rss.yaml y canales de telegram.yaml."""
    import yaml
    base = Path(root or store.ROOT) / "04_Config" / "sources"
    taken = {}
    try:
        for f in (yaml.safe_load((base / "rss.yaml").read_text(encoding="utf-8")) or {}).get("feeds") or []:
            taken.setdefault(urlsplit(str(f.get("url"))).netloc.lower().removeprefix("www."), f"rss:{f.get('name')}")
    except OSError:
        pass
    try:
        for c in (yaml.safe_load((base / "telegram.yaml").read_text(encoding="utf-8")) or {}).get("channels") or []:
            taken.setdefault(f"t.me/{str(c.get('name')).lower()}", f"telegram:{c.get('name')}")
    except OSError:
        pass
    return taken


def sync_recipes(root=None, write=True):
    """Fichas → recetas generadas. Devuelve {nombre: motivo de conflicto} y la lista de retiradas."""
    rdir = runner.recipes_dir(root)
    found = fichas(root)
    conflicts, retired = {}, []
    for name, f in found.items():
        path = rdir / f"{name}.yaml"
        if path.exists() and not path.read_text(encoding="utf-8").startswith(GENERATED):
            conflicts[name] = f"existe una receta manual {path.name}: la ficha {f['source']} no la pisa"
            continue
        text = render(name, f["block"], f["source"])
        if write and (not path.exists() or path.read_text(encoding="utf-8") != text):
            rdir.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    for path in sorted(rdir.glob("*.yaml")):
        if path.read_text(encoding="utf-8").startswith(GENERATED) and path.stem not in found:
            retired.append(path.stem)
            if write:
                path.unlink()
    return conflicts, retired


def load_state(root=None):
    try:
        st = json.loads((runner.recipes_dir(root) / runner.STATE_NAME).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        st = {}
    return st if isinstance(st, dict) else {}


def validate_all(root=None, now=None, fetch=runner.http_fetch, conflicts=None, env=None):
    """Valida cada receta y devuelve el nuevo estado {nombre: fila}."""
    import os
    import yaml
    now = int(now if now is not None else time.time())
    env = env if env is not None else os.environ
    prev = (load_state(root).get("recipes") or {})
    taken = existing_domains(root)
    rows, valid = {}, {}
    for path in sorted(runner.recipes_dir(root).glob("*.yaml")):
        name = path.stem
        text = path.read_text(encoding="utf-8")
        row = {"source": "ficha" if text.startswith(GENERATED) else "manual", "checked_at": now}
        try:
            recipe = runner.validate_recipe(yaml.safe_load(text), name)
            if recipe["name"] != name:
                raise ValueError(f"name {recipe['name']!r} distinto del archivo {path.name}")
        except Exception as e:                                       # noqa: BLE001
            rows[name] = dict(row, ok=False, reason=f"esquema: {e}"[:300])
            continue
        valid[name] = recipe
        rows[name] = dict(row, ok=True, domain=domain_key(recipe))
    # dominio no duplicado: gana el que ya estaba habilitado y, si no, el primero en orden alfabético
    order = sorted(valid, key=lambda n: (not (prev.get(n) or {}).get("enabled"), n))
    for name in order:
        dom = rows[name]["domain"]
        if dom in taken:
            rows[name].update(ok=False, reason=f"dominio duplicado: {dom} ya lo cubre {taken[dom]}")
        else:
            taken[dom] = f"receta:{name}"
    for name in sorted(valid):
        if not rows[name]["ok"]:
            continue
        recipe = valid[name]
        if recipe.get("secreto") and not env.get(recipe["secreto"]):
            rows[name].update(ok=False, reason=f"falta el secret {recipe['secreto']} (lo crea Dirección)")
            continue
        items, info = runner.collect(recipe, now, fetch, root, sample_subjects=True)
        rows[name]["items"] = len(items)
        if info["status"] != 200 or info["error"]:
            rows[name].update(ok=False, reason=f"fetch en seco: {info['error'] or info['status']}")
        elif len(items) < MIN_ITEMS:
            rows[name].update(ok=False, reason=f"fetch en seco: {len(items)} ítems (< {MIN_ITEMS})")
    for name, why in (conflicts or {}).items():                  # la receta manual se juzga sola; queda la nota
        if name in rows:
            rows[name]["note"] = why
        else:
            rows[name] = {"source": "ficha", "checked_at": now, "ok": False, "reason": why}
    state = {}
    for name, row in rows.items():
        old = prev.get(name) or {}
        strikes = 0 if row["ok"] else int(old.get("strikes") or 0) + 1
        keep = not row["ok"] and old.get("enabled") and strikes < STRIKES_TO_PROBATION
        enabled = row["ok"] or bool(keep)
        state[name] = {k: v for k, v in row.items() if k != "ok"}
        state[name].update(enabled=enabled, status="enabled" if enabled else "probation", strikes=strikes,
                           reason=row.get("reason"),
                           since=(old.get("since") if old.get("enabled") else None) or (now if enabled else None))
    return state


def run(root=None, now=None, fetch=runner.http_fetch, write=True, env=None):
    now = int(now if now is not None else time.time())
    conflicts, retired = sync_recipes(root, write)
    recipes = validate_all(root, now, fetch, conflicts, env)
    doc = {"version": VERSION, "updated_at": now, "recipes": recipes,
           "retired": sorted((set(retired) | set(load_state(root).get("retired") or [])) - set(recipes))}
    if write:
        path = runner.recipes_dir(root) / runner.STATE_NAME
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    return doc


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--dry-run", action="store_true", help="no escribe recetas ni estado")
    a = ap.parse_args(argv)
    doc = run(write=not a.dry_run)
    for name, r in sorted(doc["recipes"].items()):
        print(f"{name:22s} {r['status']:10s} ítems={r.get('items', '—')!s:4s} {r.get('reason') or ''}")
    if doc["retired"]:
        print("retiradas:", ", ".join(doc["retired"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
