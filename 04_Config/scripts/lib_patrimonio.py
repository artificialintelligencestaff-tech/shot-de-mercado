#!/usr/bin/env python3
"""
lib_patrimonio.py — índice del patrimonio de datos (D-087, doc 34 §17). No es un bot: valida y resume
02_Analisis/patrimonio/_inventario.json, la tabla de qué hay dónde.

  load()      el inventario
  check()     problemas: esquema, rutas que deberían existir y no existen, y carpetas o archivos de primer nivel
              de 02_Analisis/ que no figuran en el inventario (una ruta nueva obliga a anotarla)
  resumen()   por categoría: entradas, estados, archivos y bytes en disco

Solo biblioteca estándar. Uso: python 04_Config/scripts/lib_patrimonio.py   (sale con 1 si hay problemas)
"""
import json
import os
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
ANALISIS_REL = "02_Analisis"
INVENTARIO_REL = "02_Analisis/patrimonio/_inventario.json"
CATEGORIAS = ("cuantitativo", "informativo", "calendario", "resultados")
ESTADOS = ("vivo", "manual", "futuro", "legado")
CAMPOS = ("ruta", "categoria", "estado", "dueno", "formato", "que")
IGNORADOS = re.compile(r"^\.|\.bak\d*$|\.corrupt-")


def load(root=None):
    return json.loads((Path(root or ROOT) / INVENTARIO_REL).read_text(encoding="utf-8"))


def top_level(root=None):
    """Carpetas y archivos de primer nivel de 02_Analisis/ (sin ocultos ni backups)."""
    base = Path(root or ROOT) / ANALISIS_REL
    return sorted(p.name for p in base.iterdir() if not IGNORADOS.search(p.name)) if base.is_dir() else []


def _covers(ruta, name):
    r = ruta.rstrip("/")
    return r == f"{ANALISIS_REL}/{name}" or r.startswith(f"{ANALISIS_REL}/{name}/")


def check(root=None, doc=None, names=None):
    """Lista de problemas (vacía = inventario consistente con el disco)."""
    root = Path(root or ROOT)
    try:
        doc = doc if doc is not None else load(root)
    except (OSError, ValueError) as e:
        return [f"inventario ilegible: {type(e).__name__}: {e}"]
    problems = []
    if sorted((doc.get("categorias") or {}).keys()) != sorted(CATEGORIAS):
        problems.append(f"categorias debe ser exactamente {list(CATEGORIAS)}")
    entries = doc.get("entradas")
    if not isinstance(entries, list) or not entries:
        return problems + ["sin 'entradas'"]
    seen = set()
    for i, e in enumerate(entries):
        where = (e or {}).get("ruta") if isinstance(e, dict) else f"entrada {i}"
        missing = [c for c in CAMPOS if not isinstance(e, dict) or not str(e.get(c) or "").strip()]
        if missing:
            problems.append(f"{where}: faltan {missing}")
            continue
        if not e["ruta"].startswith(f"{ANALISIS_REL}/"):
            problems.append(f"{where}: la ruta tiene que estar dentro de {ANALISIS_REL}/")
        if e["categoria"] not in CATEGORIAS:
            problems.append(f"{where}: categoría desconocida {e['categoria']!r}")
        if e["estado"] not in ESTADOS:
            problems.append(f"{where}: estado desconocido {e['estado']!r}")
        key = e["ruta"].rstrip("/")
        if key in seen:
            problems.append(f"{where}: ruta repetida")
        seen.add(key)
        if e["estado"] != "futuro" and not (root / key).exists():
            problems.append(f"{where}: estado {e['estado']} pero la ruta no existe (¿futuro?)")
    rutas = [e["ruta"] for e in entries if isinstance(e, dict) and e.get("ruta")]
    for name in (names if names is not None else top_level(root)):
        if not any(_covers(r, name) for r in rutas):
            problems.append(f"{ANALISIS_REL}/{name}: no figura en el inventario")
    return problems


def _disk(path):
    if path.is_file():
        return 1, path.stat().st_size
    files = [p for p in path.rglob("*") if p.is_file()] if path.is_dir() else []
    return len(files), sum(p.stat().st_size for p in files)


def resumen(root=None, doc=None):
    """{categoria: {"entradas", "estados": {estado: n}, "archivos", "bytes"}} con lo que hay hoy en disco."""
    root = Path(root or ROOT)
    doc = doc if doc is not None else load(root)
    out = {c: {"entradas": 0, "estados": {}, "archivos": 0, "bytes": 0} for c in CATEGORIAS}
    for e in doc.get("entradas") or []:
        row = out.get(e.get("categoria"))
        if row is None:
            continue
        row["entradas"] += 1
        row["estados"][e.get("estado")] = row["estados"].get(e.get("estado"), 0) + 1
        n, size = _disk(root / e["ruta"].rstrip("/"))
        row["archivos"] += n
        row["bytes"] += size
    return out


def main(argv=None):
    problems = check()
    for cat, r in resumen().items():
        estados = ", ".join(f"{k} {v}" for k, v in sorted(r["estados"].items()))
        print(f"{cat:13s} {r['entradas']:3d} entradas ({estados}) · {r['archivos']:5d} archivos · "
              f"{r['bytes'] / 1e6:8.1f} MB")
    for p in problems:
        print(f"  PROBLEMA: {p}")
    print(f"patrimonio: {len(problems)} problemas")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
