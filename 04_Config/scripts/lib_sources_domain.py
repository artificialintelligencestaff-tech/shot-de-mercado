#!/usr/bin/env python3
"""
lib_sources_domain.py — dominio de fuentes (D-105). Lectura/escritura de los diarios src-1 de un bot
(02_Analisis/sources/<subdir>/) y de sus archivos de estado, sin que el consumidor conozca la ruta.

  sources_dir(root=None) · subdir_path(subdir, root=None)
  read_sources(subdir, days=None, root=None)   ítems src-1 de los diarios <YYYY-MM-DD>*.jsonl (los `days` más nuevos)
  write_sources(subdir, items, when=None, instance=None, root=None)  agrega al diario del día (lib_sources_store)
  read_state(subdir, name="_state.json", default=None, root=None) · write_state(subdir, data, name=..., root=None)
Solo biblioteca estándar (lib_sources_store para el formato src-1).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_paths as P  # noqa: E402

SCHEMA_VERSION = "src-1"
DAY_FILE = re.compile(r"^\d{4}-\d{2}-\d{2}")


def sources_dir(root=None):
    return P.path("sources.dir", root)


def subdir_path(subdir, root=None):
    """Carpeta de un bot; subdir=None = la raíz de sources/ (archivos del orquestador y del reparador)."""
    return sources_dir(root) if subdir is None else P.path("sources.bot", root, bot=subdir)


def read_sources(subdir, days=None, root=None):
    import lib_sources_store as store
    files = sorted((p for p in subdir_path(subdir, root).glob("*.jsonl") if DAY_FILE.match(p.name)),
                   key=lambda p: p.name)
    if days:
        keep = sorted({p.name[:10] for p in files})[-int(days):]
        files = [p for p in files if p.name[:10] in keep]
    out = []
    for p in files:
        out += store.read_jsonl(p)
    return out


def write_sources(subdir, items, when=None, instance=None, root=None):
    import lib_sources_store as store
    return store.append_records(subdir, list(items), when, instance, root)


def read_state(subdir, name="_state.json", default=None, root=None):
    try:
        return json.loads((subdir_path(subdir, root) / name).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def write_state(subdir, data, name="_state.json", root=None):
    p = subdir_path(subdir, root) / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    return p
