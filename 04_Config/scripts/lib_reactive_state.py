#!/usr/bin/env python3
"""
lib_reactive_state.py — estado reactivo por polling (patrón #3). Sin webhooks: cada consumidor mira los archivos
clave de la pizarra cuando corre y reacciona a lo que cambió desde la última vez.

  rs = ReactiveState(consumer="orchestrator")
  rs.subscribe("02_Analisis/sources/*/_state*.json", on_change, name="estados", keys=["feeds", "channels"])
  events = rs.poll()          # llama on_change(event) por cada archivo creado, modificado o borrado; guarda el estado

Evento: {"subscriber", "path" (relativa al repo), "change": created|modified|deleted, "sha", "prev_sha", "ts",
         "data" (JSON ya parseado si el archivo es .json; None si no)}

- Cambio = cambió el CONTENIDO (sha256), no el mtime: en Actions cada checkout reescribe los mtime. (size, mtime)
  iguales se usan solo como atajo para no re-hashear.
- `keys` (opcional): reaccionar solo si cambian esas claves del JSON (rutas con punto: "feeds.messari.status").
  Un _state.json cambia en cada corrida por `last_run`; con keys=["feeds"] solo dispara cuando cambia una fuente.
- Primera vez que se ve una suscripción: registra la línea de base sin disparar (fire_initial=True para disparar).
- Al menos una vez: si el callback lanza una excepción, esa huella no avanza y el evento se repite en el próximo
  poll; las demás suscripciones siguen. Un JSON a medio escribir (no parsea) se saltea sin avanzar.
- Persistencia: 02_Analisis/sources/_reactive_state.json (consumidor "default"); un consumidor de producción usa
  _reactive_state_<consumer>.json (un dueño por archivo, doc 34).
Solo biblioteca estándar.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
SOURCES_REL = "02_Analisis/sources"
SCHEMA = 1
CONSUMER_RE = re.compile(r"^[a-z0-9_]{1,32}$")
DATA_MAX_BYTES = 5 * 1024 * 1024        # no se parsea para el evento un JSON más grande que esto
RACY_NS = 2_000_000_000


def state_path(root=None, consumer="default"):
    if not CONSUMER_RE.match(consumer):
        raise ValueError(f"consumer inválido {consumer!r}")
    name = "_reactive_state.json" if consumer == "default" else f"_reactive_state_{consumer}.json"
    return Path(root or ROOT) / SOURCES_REL / name


def dig(data, dotted):
    for part in dotted.split("."):
        if not isinstance(data, dict):
            return None
        data = data.get(part)
    return data


class ReactiveState:
    def __init__(self, root=None, consumer="default", now=None, write=True):
        self.root = Path(root or ROOT)
        self.consumer, self.write = consumer, write
        self.path = state_path(self.root, consumer)
        self.now = now
        self.subs = {}
        try:
            prev = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            prev = {}
        self.saved = (prev.get("subscriptions") or {}) if isinstance(prev, dict) else {}

    # -- suscripción ------------------------------------------------------------------------------------------
    def subscribe(self, path, callback, name=None, keys=None, fire_initial=False):
        """`path`: archivo o glob relativo a la raíz del repo. `name` identifica la suscripción entre corridas."""
        name = name or f"{getattr(callback, '__module__', 'cb')}.{getattr(callback, '__qualname__', 'cb')}:{path}"
        prev = self.saved.get(name) or {}
        same = prev.get("pattern") == path and prev.get("keys") == (list(keys) if keys else None)
        self.subs[name] = {"pattern": path, "callback": callback, "keys": list(keys) if keys else None,
                           "files": dict(prev.get("files") or {}) if same else {},
                           "initialized": bool(same and prev.get("initialized")), "fire_initial": fire_initial}
        return name

    def unsubscribe(self, name):
        self.subs.pop(name, None)
        self.saved.pop(name, None)

    # -- huellas ----------------------------------------------------------------------------------------------
    def _matches(self, pattern):
        p = Path(pattern)
        if any(ch in pattern for ch in "*?["):
            return sorted(x for x in self.root.glob(pattern) if x.is_file())
        full = p if p.is_absolute() else self.root / p
        return [full] if full.is_file() else []

    def _rel(self, path):
        try:
            return path.resolve().relative_to(self.root.resolve()).as_posix()
        except ValueError:
            return path.as_posix()

    def _fingerprint(self, path, keys, old):
        st = path.stat()
        if old and not old.get("racy") and old.get("size") == st.st_size and old.get("mtime_ns") == st.st_mtime_ns:
            return dict(old), None, False                         # atajo: mismo tamaño y mtime, sin re-hashear
        raw = path.read_bytes()
        data = None
        if path.suffix == ".json" and len(raw) <= DATA_MAX_BYTES:
            try:
                data = json.loads(raw.decode("utf-8"))
            except ValueError:
                return None, None, True                           # a medio escribir: se saltea sin avanzar
        if keys:
            if data is None:
                return None, None, True
            raw = json.dumps({k: dig(data, k) for k in keys}, ensure_ascii=False, sort_keys=True).encode("utf-8")
        # "racy": escrito hace < 2 s; otra escritura del mismo tamaño en el mismo tic de reloj no movería el mtime,
        # así que esa huella no habilita el atajo (mismo criterio que el índice de git)
        racy = st.st_mtime_ns >= time.time_ns() - RACY_NS
        return {"sha": hashlib.sha256(raw).hexdigest()[:16], "size": st.st_size, "mtime_ns": st.st_mtime_ns,
                "racy": racy}, data, False

    # -- ciclo ------------------------------------------------------------------------------------------------
    def poll(self):
        now = int(self.now if self.now is not None else time.time())
        events = []
        for name, sub in self.subs.items():
            seen = set()
            for path in self._matches(sub["pattern"]):
                rel = self._rel(path)
                seen.add(rel)
                old = sub["files"].get(rel)
                try:
                    fp, data, skip = self._fingerprint(path, sub["keys"], old)
                except OSError:
                    continue
                if skip:
                    continue
                if old and fp["sha"] == old["sha"]:
                    sub["files"][rel] = dict(fp, seen_at=old.get("seen_at", now))      # mtime nuevo, mismo contenido
                    continue
                change = "modified" if old else "created"
                if not old and not sub["initialized"] and not sub["fire_initial"]:
                    sub["files"][rel] = dict(fp, seen_at=now)                     # línea de base, sin disparar
                    continue
                ev = {"subscriber": name, "path": rel, "change": change, "sha": fp["sha"],
                      "prev_sha": (old or {}).get("sha"), "ts": now, "data": data}
                if self._fire(sub, ev):
                    sub["files"][rel] = dict(fp, seen_at=now)
                events.append(ev)
            for rel in sorted(set(sub["files"]) - seen):
                ev = {"subscriber": name, "path": rel, "change": "deleted", "sha": None,
                      "prev_sha": sub["files"][rel].get("sha"), "ts": now, "data": None}
                if self._fire(sub, ev):
                    del sub["files"][rel]
                events.append(ev)
            sub["initialized"] = True
        if self.write:
            self.save(now)
        return events

    @staticmethod
    def _fire(sub, ev):
        try:
            sub["callback"](ev)
            return True
        except Exception as exc:                                  # noqa: BLE001 — un consumidor roto no frena al resto
            ev["error"] = f"{type(exc).__name__}: {exc}"[:300]
            return False

    def save(self, now=None):
        subs = dict(self.saved)
        subs.update({name: {"pattern": s["pattern"], "keys": s["keys"], "files": s["files"],
                            "initialized": s["initialized"]} for name, s in self.subs.items()})
        doc = {"version": SCHEMA, "consumer": self.consumer, "updated_at": int(now or time.time()),
               "subscriptions": subs}
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = Path(str(self.path) + ".tmp")
        tmp.write_text(json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
        tmp.replace(self.path)

    def watch(self, interval_s, max_polls, sleep=time.sleep):
        """Para un job largo (p. ej. las instancias de Telegram de 40 min): poll cada `interval_s`."""
        out = []
        for i in range(max_polls):
            out += self.poll()
            if i < max_polls - 1:
                sleep(interval_s)
        return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="Estado reactivo por polling (patrón #3)")
    ap.add_argument("pattern", nargs="?", default=f"{SOURCES_REL}/*/_state*.json")
    ap.add_argument("--keys", nargs="*")
    ap.add_argument("--consumer", default="default")
    ap.add_argument("--dry-run", action="store_true", help="no guarda el estado")
    a = ap.parse_args(argv)
    rs = ReactiveState(consumer=a.consumer, write=not a.dry_run)
    rs.subscribe(a.pattern, lambda ev: None, name=f"cli:{a.pattern}", keys=a.keys)
    for ev in rs.poll():
        print(f"{ev['change']:9s} {ev['path']}  {ev['prev_sha']} -> {ev['sha']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
