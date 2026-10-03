#!/usr/bin/env python3
"""
lib_episodic_memory.py — memoria episódica del sistema (patrón #12, doc 36 §1 paso 8).

Un episodio es un hecho cerrado: qué pasó, con qué, en qué contexto y cómo terminó. Es la memoria que evita
re-probar lo ya descartado y la que permite preguntar "¿esto ya pasó antes?".

  {"v":1, "id", "ts", "timestamp", "tipo", "entidad", "contexto", "resultado", "tags", "writer"}
  tipo ∈ alerta_emitida · feed_caido · bot_reparado · hipotesis_evaluada

Persistencia: 02_Analisis/sources/_episodes.jsonl (append-only). Un escritor de producción (un workflow) escribe en
su propio fragmento _episodes_<writer>.jsonl: dos workflows que agregan líneas al MISMO archivo chocan en el
`pull --rebase`, así que cada fragmento tiene un solo dueño (doc 34). `query_episodes` lee el archivo principal más
todos los fragmentos. Escritores hoy: self_repair (feed_caido, bot_reparado) y method (hipotesis_evaluada).
Dedup por id = hash(ts, tipo, entidad, contexto, resultado): reescribir el mismo episodio no duplica.
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
SOURCES_REL = "02_Analisis/sources"
MAIN_NAME = "_episodes.jsonl"
SCHEMA = 1
TIPOS = ("alerta_emitida", "feed_caido", "bot_reparado", "hipotesis_evaluada")
WRITER_RE = re.compile(r"^[a-z0-9_]{1,32}$")
ENTITY_MAX = 200
DEDUP_TAIL = 2000             # el dedup mira las últimas N líneas del archivo destino


def episodes_path(root=None, writer=None):
    base = Path(root or ROOT) / SOURCES_REL
    if writer is None:
        return base / MAIN_NAME
    if not WRITER_RE.match(writer):
        raise ValueError(f"writer inválido {writer!r}")
    return base / f"_episodes_{writer}.jsonl"


def _entity(value):
    if norm.is_null(value):
        raise ValueError("entidad vacía")
    s = str(value).strip()
    return (norm.address(s) or s)[:ENTITY_MAX]


def _tags(tags):
    out = []
    for t in tags or ():
        k = norm.keyword(t)
        if k and k not in out:
            out.append(k)
    return sorted(out)


def _epoch(value):
    return norm.timestamp(value) if value is not None else None


def make_episode(tipo, entidad, contexto=None, resultado=None, tags=None, now=None, writer=None):
    if tipo not in TIPOS:
        raise ValueError(f"tipo {tipo!r} fuera de {TIPOS}")
    if contexto is not None and not isinstance(contexto, dict):
        raise ValueError("contexto debe ser un dict")
    if resultado is not None and not isinstance(resultado, (str, int, float, dict)):
        raise ValueError("resultado debe ser str, número o dict")
    ts = int(now if now is not None else time.time())
    body = {"ts": ts, "tipo": tipo, "entidad": _entity(entidad), "contexto": contexto or {}, "resultado": resultado}
    json.dumps(body)                                    # falla aquí, no al escribir, si algo no es serializable
    digest = hashlib.sha256(json.dumps(body, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]
    return dict(body, v=SCHEMA, id=digest, tags=_tags(tags), writer=writer,
                timestamp=datetime.fromtimestamp(ts, timezone.utc).isoformat(timespec="seconds"))


def _read(path):
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    out = []
    for line in lines:
        try:
            r = json.loads(line)
        except ValueError:
            continue                                    # línea cortada por un push a medias
        if isinstance(r, dict) and r.get("tipo") in TIPOS:
            out.append(r)
    return out


def write_episodes(episodes, root=None, writer=None):
    """Agrega episodios (ya armados con make_episode) al archivo del escritor. Devuelve los que eran nuevos."""
    path = episodes_path(root, writer)
    seen = {r.get("id") for r in _read(path)[-DEDUP_TAIL:]}
    new = []
    for e in episodes:
        if e["id"] not in seen:
            seen.add(e["id"])
            new.append(e)
    if new:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8", newline="\n") as f:
            for e in new:
                f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
    return new


def write_episode(tipo, entidad, contexto=None, resultado=None, tags=None, now=None, root=None, writer=None):
    """Escribe un episodio. Devuelve el episodio, o None si ya estaba (mismo id)."""
    e = make_episode(tipo, entidad, contexto, resultado, tags, now, writer)
    return e if write_episodes([e], root, writer) else None


def read_episodes(root=None):
    base = Path(root or ROOT) / SOURCES_REL
    paths = [base / MAIN_NAME] + sorted(base.glob("_episodes_*.jsonl"))
    seen, out = set(), []
    for p in paths:
        for r in _read(p):
            if r.get("id") not in seen:
                seen.add(r.get("id"))
                out.append(r)
    out.sort(key=lambda r: (r.get("ts") or 0, r.get("id") or ""))
    return out


def query_episodes(filtro=None, root=None, limit=None):
    """Episodios que cumplen `filtro`, del más viejo al más nuevo (los últimos `limit` si se pide).
    filtro: dict con cualquiera de
      tipo (str o lista) · entidad (exacta, en forma canónica) · tags (todas presentes) · writer
      desde / hasta (epoch o ISO, inclusive) · resultado (igualdad; en un dict, sus claves deben coincidir)
    o una función episodio -> bool."""
    eps = read_episodes(root)
    if callable(filtro):
        out = [e for e in eps if filtro(e)]
    else:
        f = dict(filtro or {})
        tipos = f.get("tipo")
        tipos = {tipos} if isinstance(tipos, str) else set(tipos or ())
        ent = _entity(f["entidad"]) if f.get("entidad") is not None else None
        tags = set(_tags(f.get("tags")))
        desde, hasta = _epoch(f.get("desde")), _epoch(f.get("hasta"))
        res = f.get("resultado")

        def ok(e):
            if tipos and e.get("tipo") not in tipos:
                return False
            if ent is not None and e.get("entidad") != ent:
                return False
            if tags and not tags.issubset(e.get("tags") or ()):
                return False
            if f.get("writer") is not None and e.get("writer") != f["writer"]:
                return False
            if desde is not None and (e.get("ts") or 0) < desde:
                return False
            if hasta is not None and (e.get("ts") or 0) > hasta:
                return False
            if res is not None:
                got = e.get("resultado")
                if isinstance(res, dict):
                    return isinstance(got, dict) and all(got.get(k) == v for k, v in res.items())
                return got == res
            return True
        out = [e for e in eps if ok(e)]
    return out[-limit:] if limit else out


# ---------------------------------------------------------------------------
# Constructores por tipo (los escritores llaman a estos, no arman el dict a mano)
# ---------------------------------------------------------------------------

REPAIRED = {"auto_on", "rerun", "dispatch", "reset_state", "trim_seen", "resolved"}


def repair_episodes(actions, now=None):
    """Acciones de bot_self_repair -> episodios. Solo transiciones: la primera caída de una fuente y cada arreglo
    hecho (no las renovaciones de auto_off ni los intentos fallidos, que ya quedan en _repair_log.jsonl)."""
    out = []
    for a in actions:
        ts = a.get("ts", now)
        if a.get("action") == "auto_off" and a.get("detection") == "fuente caída":
            name = str(a.get("evidence", "")).split(":")[0].strip() or a.get("bot")
            out.append(make_episode("feed_caido", f"{a.get('bot')}/{name}", {"bot": a.get("bot"),
                                    "evidence": a.get("evidence")}, "auto_off", [a.get("bot"), "fuente"], ts,
                                    "self_repair"))
        elif a.get("action") in REPAIRED:
            out.append(make_episode("bot_reparado", a.get("bot") or "desconocido", {"detection": a.get("detection"),
                                    "evidence": a.get("evidence")}, a.get("action"), [a.get("bot"), a.get("action")],
                                    ts, "self_repair"))
    return out


def hypothesis_episode(evaluation, registration):
    r = evaluation.get("result") or {}
    ctx = {"test": registration["prediction"]["test"], "n": r.get("n"), "hash": evaluation.get("hash"),
           "data_hash": evaluation.get("data_hash"), "verdict": evaluation.get("verdict")}
    ctx.update({k: r[k] for k in ("p_value", "diff_pp", "rate", "median") if k in r})
    return make_episode("hipotesis_evaluada", evaluation["id"], ctx, evaluation.get("label"),
                        [registration.get("group") or "sin_grupo", evaluation.get("verdict")], evaluation.get("ts"),
                        "method")


def alert_episode(alert, now=None, writer="alerts"):
    """Alerta emitida -> episodio. Pensado para el emisor (script_97) después de un envío OK; no está cableado
    porque el emisor es producción (se consulta antes de tocarlo)."""
    ent = alert.get("mint") or alert.get("address") or alert.get("symbol")
    ctx = {k: alert.get(k) for k in ("symbol", "chain", "group", "score", "scorer", "age_min_at_alert",
                                     "initial_price") if alert.get(k) is not None}
    return make_episode("alerta_emitida", ent, ctx, "emitida", [alert.get("chain"), alert.get("scorer")],
                        _epoch(alert.get("timestamp")) or now, writer)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Memoria episódica (patrón #12)")
    ap.add_argument("--tipo", action="append")
    ap.add_argument("--entidad")
    ap.add_argument("--desde")
    ap.add_argument("--limit", type=int, default=20)
    a = ap.parse_args(argv)
    f = {k: v for k, v in (("tipo", a.tipo), ("entidad", a.entidad), ("desde", a.desde)) if v}
    for e in query_episodes(f, limit=a.limit):
        print(f"{e['timestamp']}  {e['tipo']:18s} {e['entidad']:40.40s} {json.dumps(e.get('resultado'), ensure_ascii=False)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
