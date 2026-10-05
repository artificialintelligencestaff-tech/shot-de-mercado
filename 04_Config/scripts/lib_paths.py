#!/usr/bin/env python3
"""
lib_paths.py — interfaz central de rutas (D-105, doc 38 §6). Ningún módulo de producción arma la ruta física de
otro: todos piden una clave a esta tabla. Mover una carpeta = cambiar UNA línea de PATHS.

  root()                  raíz del repo: SHOT_ROOT (leído en cada llamada, para que los tests la cambien) o la
                          ubicación de este archivo
  path(key, root=None, **fmt)  Path absoluto; KeyError explícito si la clave no existe. Las claves con {campos}
                          se completan con fmt (p. ej. path("alerts.detail", mint=..., ts=...))
  path_str(key, ...)      lo mismo como str
  rel(key, **fmt)         ruta relativa al repo (posix), para listas de `git add`
  register(key, rel, kind="file", pending=False)  un módulo agrega sus rutas propias al importar; re-registrar la
                          misma ruta es idempotente, otra ruta para la misma clave es ValueError
  validate(root=None)     claves sin plantilla que apuntan a algo inexistente y no están marcadas pending
  VERSION                 versión del contrato; cambia cuando cambia una ruta

Solo biblioteca estándar.
"""
import os
from pathlib import Path

VERSION = "paths-1"
_DEFAULT_ROOT = Path(__file__).resolve().parents[2]
A = "02_Analisis"            # única ocurrencia permitida del prefijo de datos (audit_gate rutas)

# clave -> (ruta relativa al repo, "file" | "dir", pending_creation)
PATHS = {
    # alertas y patrimonio de emisión (dueño: script_97 / script_98)
    "alerts.dir": (f"{A}/alerts", "dir", False),
    "alerts.all": (f"{A}/alerts/_all_alerts.json", "file", False),
    "alerts.precision_log": (f"{A}/alerts/_precision_log.json", "file", False),
    "alerts.cycle_log": (f"{A}/alerts/_cycle_log.json", "file", False),
    "alerts.detail": (f"{A}/alerts/alert_{{mint}}_{{ts}}.json", "file", True),
    "alerts.trust": (f"{A}/alerts/trust_{{mint}}.json", "file", True),
    # early watch (script_116 por instancia; early_review el gate)
    "early.dir": (f"{A}/early", "dir", False),
    "early.watch": (f"{A}/early/_watch_{{inst}}.json", "file", True),
    "early.watch_a": (f"{A}/early/_watch_a.json", "file", True),
    "early.watch_b": (f"{A}/early/_watch_b.json", "file", True),
    "early.signals": (f"{A}/early/_signals_{{inst}}.json", "file", True),
    "early.signals_a": (f"{A}/early/_signals_a.json", "file", True),
    "early.signals_b": (f"{A}/early/_signals_b.json", "file", True),
    "early.signals_legacy": (f"{A}/early/_signals.json", "file", True),
    "early.alerts_legacy": (f"{A}/early/_early_alerts.json", "file", True),
    "early.alerts_dir": (f"{A}/early/alerts", "dir", True),
    "early.claim": (f"{A}/early/alerts/{{mint}}.json", "file", True),
    "early.gate": (f"{A}/early/_gate.json", "file", True),
    "early.young_dir": (f"{A}/early/young", "dir", True),
    # multichain (script_114)
    "multichain.dir": (f"{A}/multichain", "dir", False),
    "multichain.categories": (f"{A}/multichain/_categories.json", "file", False),
    "multichain.history": (f"{A}/multichain/_history.jsonl", "file", False),
    "multichain.protocols": (f"{A}/multichain/_protocols.json", "file", False),
    "multichain.perps": (f"{A}/multichain/_perps.json", "file", False),
    "multichain.premarket": (f"{A}/multichain/_premarket.json", "file", False),
    "multichain.governance": (f"{A}/multichain/_governance.json", "file", False),
    "multichain.scores": (f"{A}/multichain/_scores.json", "file", False),
    "multichain.card": (f"{A}/multichain/{{name}}.json", "file", True),
    # narrativa (script_115)
    "narrative.dir": (f"{A}/narrative", "dir", False),
    "narrative.items": (f"{A}/narrative/_items.json", "file", False),
    "narrative.index": (f"{A}/narrative/_index.json", "file", False),
    "narrative.token": (f"{A}/narrative/{{mint}}.json", "file", True),
    # fuentes (bots de fuentes, orquestador, reparador)
    "sources.dir": (f"{A}/sources", "dir", False),
    "sources.bot": (f"{A}/sources/{{bot}}", "dir", True),
    "sources.rss": (f"{A}/sources/rss", "dir", True),
    "sources.telegram": (f"{A}/sources/telegram", "dir", True),
    "sources.x_influencers": (f"{A}/sources/x_influencers", "dir", True),
    "sources.events": (f"{A}/events", "dir", False),
    "sources.orchestrator_state": (f"{A}/sources/_health.json", "file", True),
    "sources.merged": (f"{A}/sources/_merged.jsonl", "file", True),
    "sources.index": (f"{A}/sources/_index.json", "file", True),
    "sources.repair_state": (f"{A}/sources/_repair_state.json", "file", True),
    # eventos (lib_events)
    "events.dir": (f"{A}/events", "dir", False),
    "events.cursors_dir": (f"{A}/events/_cursors", "dir", True),
    "events.writer": (f"{A}/events/{{writer}}", "dir", True),
    # calendario de preventa (bot_prelaunch_calendar)
    "prelaunch.dir": (f"{A}/prelaunch", "dir", False),
    "prelaunch.calendar": (f"{A}/prelaunch/_calendar.json", "file", False),
    "prelaunch.state": (f"{A}/prelaunch/_state.json", "file", False),
    "prelaunch.events_dir": (f"{A}/events/prelaunch_calendar", "dir", True),
    # patrimonio, diagnósticos, shadow, dossiers, datasets, operaciones
    "patrimonio.dir": (f"{A}/patrimonio", "dir", False),
    "patrimonio.inventario": (f"{A}/patrimonio/_inventario.json", "file", False),
    "diagnostics.dir": (f"{A}/diagnostics", "dir", False),
    "diagnostics.latency": (f"{A}/diagnostics/latency_analysis.json", "file", False),
    "diagnostics.inventario_probe": (f"{A}/diagnostics/inventario_probe.json", "file", False),
    "diagnostics.early_review": (f"{A}/diagnostics/early_review.json", "file", True),
    "diagnostics.emission_calibration": (f"{A}/diagnostics/emission_calibration.json", "file", True),
    "shadow_v4.accumulated": (f"{A}/shadow_v4/_accumulated.json", "file", False),
    "dossiers.dir": (f"{A}/dossiers", "dir", False),
    "dossiers.multichain_dir": (f"{A}/dossiers/multichain", "dir", True),
    "datasets.memechain_index": (f"{A}/datasets/memechain_index.json", "file", True),
    "operations.dir": (f"{A}/operations", "dir", True),
    "operations.log": (f"{A}/operations/{{op}}.jsonl", "file", True),
    "analisis.dir": (A, "dir", False),
}


def root():
    """SHOT_ROOT si está definido (se lee en cada llamada), si no la raíz del repo."""
    return Path(os.environ.get("SHOT_ROOT") or _DEFAULT_ROOT)


def _entry(key):
    try:
        return PATHS[key]
    except KeyError:
        raise KeyError(f"lib_paths: clave desconocida {key!r} (registrarla en PATHS o con register)") from None


def rel(key, **fmt):
    """Ruta relativa al repo, en posix."""
    r = _entry(key)[0]
    try:
        return r.format(**fmt) if fmt or "{" in r else r
    except KeyError as e:
        raise KeyError(f"lib_paths: {key!r} necesita el campo {e.args[0]!r}") from None


def path(key, root_dir=None, **fmt):
    return Path(root_dir or root()) / rel(key, **fmt)


def path_str(key, root_dir=None, **fmt):
    return str(path(key, root_dir, **fmt))


def register(key, rel_path, kind="file", pending=False):
    """Un módulo registra sus rutas propias. Misma ruta: idempotente. Otra ruta para la clave: ValueError."""
    if kind not in ("file", "dir"):
        raise ValueError("kind: 'file' o 'dir'")
    rel_path = str(rel_path).replace("\\", "/").strip("/")
    if key in PATHS and PATHS[key][0] != rel_path:
        raise ValueError(f"lib_paths: {key!r} ya apunta a {PATHS[key][0]!r}, no a {rel_path!r}")
    PATHS[key] = (rel_path, kind, bool(pending))
    return key


def validate(root_dir=None):
    """Problemas: claves concretas (sin plantilla) que no existen y no son pending_creation, o de tipo cambiado."""
    base = Path(root_dir or root())
    problems = []
    for key, (r, kind, pending) in sorted(PATHS.items()):
        if "{" in r:
            continue
        p = base / r
        if not p.exists():
            if not pending:
                problems.append(f"{key}: no existe {r}")
        elif (kind == "dir") != p.is_dir():
            problems.append(f"{key}: se esperaba {kind} en {r}")
    return problems


if __name__ == "__main__":
    import sys
    probs = validate()
    print(f"lib_paths {VERSION}: {len(PATHS)} claves · problemas {len(probs)}")
    for p in probs:
        print("  " + p)
    sys.exit(1 if probs else 0)
