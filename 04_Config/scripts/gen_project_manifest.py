#!/usr/bin/env python3
"""
gen_project_manifest.py — genera _project_manifest.json y el catálogo de scripts (doc 04) desde el repo real (D-101).
Nada a mano: workflows (cron, scripts, concurrencia), bots de _bots.yaml, recetas, carpetas de datos de
02_Analisis/patrimonio/_inventario.json con su retención (_retention.yaml, doc 38) y el estado de cada script:
  workflow   lo corre un workflow
  importado  lo importa (directo o transitivo) un script que corre un workflow
  sin_uso    ninguno de los dos (candidato a 04_Config/scripts/_archivo/)

Uso: python 04_Config/scripts/gen_project_manifest.py [--catalog] [--check]
     --catalog  reescribe además "El cerebro de dios/04_SCRIPTS_CATALOG.md"
     --check    no escribe; sale con 1 si _project_manifest.json no coincide con lo generado (sin la fecha)
Solo biblioteca estándar + PyYAML.
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_paths as P  # noqa: E402  D-105: interfaz común de rutas

ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
MANIFEST_REL = "_project_manifest.json"
CATALOG_REL = "El cerebro de dios/04_SCRIPTS_CATALOG.md"
RUN_RE = re.compile(r"python3?\s+(?:-m\s+)?([\w./-]+\.py)")
WORD_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\b")


def _yaml(path):
    import yaml
    try:
        return yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        return {}


def workflows(root):
    out = []
    for p in sorted((Path(root) / ".github" / "workflows").glob("*.yml")):
        doc, text = _yaml(p), p.read_text(encoding="utf-8")
        on = doc.get(True) or doc.get("on") or {}
        crons = [s.get("cron") for s in (on.get("schedule") or []) if isinstance(s, dict)] if isinstance(on, dict) else []
        conc = doc.get("concurrency") or {}
        out.append({"file": p.name, "name": doc.get("name") or p.stem, "cron": crons,
                    "manual": isinstance(on, dict) and "workflow_dispatch" in on,
                    "triggers": sorted(k for k in on) if isinstance(on, dict) else [],
                    "desactivado": "if: ${{ false }}" in text,
                    "scripts": sorted({m for m in RUN_RE.findall(text)}),
                    "concurrency": conc.get("group") if isinstance(conc, dict) else conc})
    return out


def script_states(root, wfs):
    sdir = Path(root) / "04_Config" / "scripts"
    names = {p.stem: p for p in sdir.glob("*.py") if not p.stem.startswith("test_")}
    run = {Path(s).stem for w in wfs if not w["desactivado"] for s in w["scripts"]}
    refs = {}
    for name, p in names.items():
        words = set(WORD_RE.findall(p.read_text(encoding="utf-8", errors="replace")))
        refs[name] = {n for n in words & set(names) if n != name}
    live, stack = set(), [n for n in run if n in names]
    while stack:
        n = stack.pop()
        if n in live:
            continue
        live.add(n)
        stack.extend(refs.get(n, ()))
    by_wf = {}
    for w in wfs:
        for s in w["scripts"]:
            by_wf.setdefault(Path(s).stem, []).append(w["file"])
    out = {}
    for name in sorted(names):
        state = "workflow" if name in run else ("importado" if name in live else "sin_uso")
        out[name] = {"estado": state, "workflows": sorted(by_wf.get(name, []))}
    return out


def retention(root, ruta):
    sys.path.insert(0, str(SCRIPTS))
    import bot_orchestrator as orch
    p = Path(root) / ruta
    return orch.retention_for(p if p.is_dir() else p.parent, root) if p.exists() else None


def data_folders(root):
    try:
        inv = json.loads(P.path("patrimonio.inventario", root).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    out = []
    for e in inv.get("entradas") or []:
        if e.get("estado") == "archivado":
            continue
        row = {k: e.get(k) for k in ("ruta", "categoria", "estado", "dueno")}
        if str(e.get("ruta", "")).startswith(P.rel("sources.dir")):
            row["retencion_dias"] = retention(root, e["ruta"])
        out.append(row)
    sub = P.path("sources.dir", root)
    for r in sorted(sub.glob("*/_retention.yaml")):
        rel = r.parent.relative_to(root).as_posix() + "/"
        out.append({"ruta": rel, "categoria": (_yaml(r).get("categoria")), "estado": "vivo",
                    "dueno": "ver _bots.yaml", "retencion_dias": retention(root, rel)})
    return out


def build(root=None, now=None):
    root = Path(root or ROOT)
    wfs = workflows(root)
    bots = (_yaml(root / "04_Config" / "sources" / "_bots.yaml").get("bots") or {})
    rstate = {}
    try:
        rstate = json.loads((root / "04_Config" / "recipes" / "_recipes_state.json").read_text(encoding="utf-8")).get(
            "recipes") or {}
    except (OSError, ValueError):
        pass
    recipes = {p.stem: {"enabled": bool((rstate.get(p.stem) or {}).get("enabled")),
                        "status": (rstate.get(p.stem) or {}).get("status")}
               for p in sorted((root / "04_Config" / "recipes").glob("*.yaml"))}
    scripts = script_states(root, wfs)
    count = {s: sum(1 for v in scripts.values() if v["estado"] == s) for s in ("workflow", "importado", "sin_uso")}
    return {
        "schema_version": "2.0",
        "generated_at": now or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generated_by": "04_Config/scripts/gen_project_manifest.py (D-101)",
        "plataforma": "GitHub Actions (repo público); sin rutas locales",
        "reglas": ["100% gratis", "un dueño por archivo (git add -- <ruta>)", "sin push forzado ni reset destructivo",
                   "numérico y escrito en archivos separados (doc 38)", "retención por _retention.yaml (doc 38 §2)"],
        "docs": {"indice": "El cerebro de dios/README.md", "lectura": ["35", "38", "34", "32"]},
        "workflows": wfs,
        "bots": {k: {kk: v.get(kk) for kk in ("workflow", "every_min", "stale_min", "backup", "enabled")}
                 for k, v in sorted(bots.items())},
        "recetas": recipes,
        "datos": data_folders(root),
        "scripts_resumen": count,
        "scripts": scripts,
    }


def catalog_md(m):
    rows = {"workflow": [], "importado": [], "sin_uso": []}
    for name, v in m["scripts"].items():
        rows[v["estado"]].append((name, ", ".join(v["workflows"])))
    out = ["---", "owner: Claude1 (generado)", "status: GENERADO por gen_project_manifest.py --catalog (D-101)",
           f"last_updated: {m['generated_at'][:10]}", "---", "", "# 04 — Catálogo de scripts (generado)", "",
           "No se edita a mano: `python 04_Config/scripts/gen_project_manifest.py --catalog`.", "",
           f"Resumen: {m['scripts_resumen']['workflow']} los corre un workflow · {m['scripts_resumen']['importado']} "
           f"los importa uno que corre · {m['scripts_resumen']['sin_uso']} sin uso (candidatos a "
           "`04_Config/scripts/_archivo/`).", ""]
    titles = {"workflow": "Los corre un workflow", "importado": "Importados por scripts vivos",
              "sin_uso": "Sin uso (ni workflow ni importado)"}
    for state in ("workflow", "importado", "sin_uso"):
        out += [f"## {titles[state]} ({len(rows[state])})", "", "| Script | Workflow(s) |", "|---|---|"]
        out += [f"| `{n}.py` | {w or '—'} |" for n, w in rows[state]] + [""]
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Genera _project_manifest.json (y el catálogo de scripts)")
    ap.add_argument("--catalog", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    m = build()
    path = ROOT / MANIFEST_REL
    if a.check:
        try:
            cur = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            cur = {}
        same = {k: v for k, v in cur.items() if k != "generated_at"} == {k: v for k, v in m.items() if k != "generated_at"}
        print("manifest al día" if same else "manifest desactualizado: correr gen_project_manifest.py")
        return 0 if same else 1
    path.write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if a.catalog:
        (ROOT / CATALOG_REL).write_text(catalog_md(m) + "\n", encoding="utf-8")
    print(f"manifest: {len(m['workflows'])} workflows · {len(m['bots'])} bots · {len(m['recetas'])} recetas · "
          f"scripts {m['scripts_resumen']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
