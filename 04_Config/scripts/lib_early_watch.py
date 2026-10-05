#!/usr/bin/env python3
"""
lib_early_watch.py — dominio del early watch (D-105). Archivos por instancia (un dueño por archivo):
_watch_<inst>.json y _signals_<inst>.json; reclamos por mint en early/alerts/<mint>.json; gate en _gate.json.

  read_watch(instance, default=None) · write_watch(instance, data)
  read_signals(instance, default=None) · write_signals(instance, data)
  rel_watch(instance) · rel_signals(instance) · rel_claims() · rel_young() · rel_gate()   (rutas para `git add`)
  claim_rel(mint)
Formato de escritura: el de siempre de script_116 (indent=1, UTF-8, default=str, salto final), atómico.
Solo biblioteca estándar.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_paths as P  # noqa: E402

SCHEMA_VERSION = "early-watch-1"


def _read(p, default):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def _write(p, data):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    os.replace(tmp, p)


def watch_path(instance, root=None):
    return P.path("early.watch", root, inst=instance)


def signals_path(instance, root=None):
    return P.path("early.signals", root, inst=instance)


def read_watch(instance, default=None, root=None):
    return _read(watch_path(instance, root), default)


def write_watch(instance, data, root=None):
    _write(watch_path(instance, root), data)


def read_signals(instance, default=None, root=None):
    return _read(signals_path(instance, root), default)


def write_signals(instance, data, root=None):
    _write(signals_path(instance, root), data)


def rel_watch(instance):
    return P.rel("early.watch", inst=instance)


def rel_signals(instance):
    return P.rel("early.signals", inst=instance)


def rel_claims():
    return P.rel("early.alerts_dir")


def claim_rel(mint):
    return P.rel("early.claim", mint=mint)


def rel_young():
    return P.rel("early.young_dir")


def rel_gate():
    return P.rel("early.gate")
