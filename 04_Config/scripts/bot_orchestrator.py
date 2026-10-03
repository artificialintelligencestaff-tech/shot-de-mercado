#!/usr/bin/env python3
"""
bot_orchestrator.py — orquestador de los bots de fuentes (doc 34 §8). Cada 10 min (sources_orchestrator.yml;
frecuencia real ~15 min por el desfase del cron de Actions). No genera código.

  1. Lee 04_Config/sources/_bots.yaml y el _state.json de cada bot.
  2. lib_sources_store.merge() → 02_Analisis/sources/_merged.jsonl (48 h) + _index.json.
  3. Salud por bot → 02_Analisis/sources/_health.json (estado, última corrida, último output, errores) + 24 h de
     historial. Estados: ok · vacío (3 corridas sin ítems) · atrasado (> stale_min) · caído (3 fallas) ·
     sin_datos (nunca corrió) · diseño (enabled: false).
  4. Poda los diarios de más de 7 días (siguen en el historial de git).
  5. Bloque automático de _servicios_open_source/_INSTALADOS.md, solo si cambió algún estado.
  6. Grafo de conocimiento de las menciones (lib_knowledge_graph, patrón #7) → 02_Analisis/sources/_graph.json.

Uso: python 04_Config/scripts/bot_orchestrator.py [--dry-run]
"""
import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_audit as audit  # noqa: E402
import lib_knowledge_graph as kg  # noqa: E402
import lib_sources_store as store  # noqa: E402

VERSION = "orch-0.1"
KEEP_DAYS = 7
HISTORY_S = 24 * 3600
EMPTY_RUNS = 3
FAIL_RUNS = 3
AUTO_START, AUTO_END = "<!-- AUTO:sources -->", "<!-- /AUTO:sources -->"


def load_registry(root):
    import yaml
    doc = yaml.safe_load((Path(root) / "04_Config" / "sources" / "_bots.yaml").read_text(encoding="utf-8")) or {}
    bots = doc.get("bots")
    if not isinstance(bots, dict) or not bots:
        raise ValueError("_bots.yaml: falta 'bots'")
    return bots


def read_json(path, default=None):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def bot_health(name, cfg, state, prev, now):
    """Estado de un bot a partir de su _state.json y del registro anterior en _health.json."""
    prev = prev or {}
    if cfg.get("enabled", True) is False:
        return {"status": "diseño"}
    if not isinstance(state, dict) or not state.get("last_run"):
        return {"status": "sin_datos", "errors": ["sin _state.json"]}
    last = int(state["last_run"])
    srcs = state.get("feeds") or state.get("sources") or {}
    errors = sorted(f"{k}: {v.get('status')}" + (f" ({v['parse_error']})" if v.get("parse_error") else "")
                    for k, v in srcs.items() if v.get("status") != 200 or v.get("parse_error"))
    new_run = last != prev.get("last_run")
    items = int(state.get("items_last_run") or 0)
    empty = (prev.get("empty_runs", 0) + 1 if items == 0 else 0) if new_run else prev.get("empty_runs", 0)
    all_down = bool(srcs) and len(errors) == len(srcs)
    fails = (prev.get("fail_runs", 0) + 1 if all_down else 0) if new_run else prev.get("fail_runs", 0)
    if now - last > float(cfg.get("stale_min") or 60) * 60:
        status = "atrasado"
    elif fails >= FAIL_RUNS:
        status = "caído"
    elif empty >= EMPTY_RUNS:
        status = "vacío"
    else:
        status = "ok"
    return {"status": status, "last_run": last, "last_output": items, "sources_ok": len(srcs) - len(errors),
            "sources_total": len(srcs), "errors": errors, "empty_runs": empty, "fail_runs": fails}


def prune(root, now, keep_days=KEEP_DAYS):
    cutoff = datetime.fromtimestamp(now - keep_days * 86400, timezone.utc).strftime("%Y-%m-%d")
    removed = []
    for p in store.sources_dir(root).glob("*/*.jsonl"):
        if p.name[:10] < cutoff:
            p.unlink()
            removed.append(p.name)
    return sorted(removed)


def installed_block(bots_health):
    rows = "\n".join(f"| `{n}` | {h['status']} | {h.get('last_output', '—')} | "
                     f"{h.get('sources_ok', '—')}/{h.get('sources_total', '—')} |" for n, h in sorted(bots_health.items()))
    return (f"{AUTO_START}\n## Bots de fuentes (automático: bot_orchestrator)\n\n"
            f"| Bot | Estado | Ítems última corrida | Fuentes OK |\n|---|---|---|---|\n{rows}\n{AUTO_END}")


def update_installed(path, bots_health):
    """Reescribe solo el bloque AUTO; lo de afuera no se toca. Devuelve True si cambió."""
    path = Path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    block = installed_block(bots_health)
    if AUTO_START in text and AUTO_END in text:
        new = text[:text.index(AUTO_START)] + block + text[text.index(AUTO_END) + len(AUTO_END):]
    else:
        new = text.rstrip("\n") + "\n\n" + block + "\n"
    if new == text:
        return False
    path.write_text(new, encoding="utf-8")
    return True


def run(root, now=None, write=True):
    now = now if now is not None else time.time()
    t_start = time.time()
    base = store.sources_dir(root)
    registry = load_registry(root)
    prev_doc = read_json(base / "_health.json", {}) or {}
    prev = prev_doc.get("bots") or {}
    health = {n: bot_health(n, cfg, read_json(base / n / "_state.json"), prev.get(n), now)
              for n, cfg in registry.items()}
    stats = {}
    merged = store.merge(now, root, stats=stats) if write else len(store.collect(now, store.MERGE_HOURS, root, stats))
    history = [h for h in prev_doc.get("history") or [] if now - h.get("ts", 0) <= HISTORY_S]
    history.append({"ts": int(now), "merged": merged, **{n: h["status"] for n, h in health.items()}})
    doc = {"version": VERSION, "generated_at": int(now), "merged_items": merged, "bots": health,
           "history": history}
    pruned, installed, graph = [], False, None
    if write:
        graph = kg.write_graph(store.read_jsonl(base / "_merged.jsonl"), now, root).to_json()["counts"]
        pruned = prune(root, now)
        (base / "_health.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=True),
                                           encoding="utf-8")
        changed = {n: h["status"] for n, h in health.items()} != {n: (h or {}).get("status") for n, h in prev.items()}
        if changed:
            installed = update_installed(Path(root) / "_servicios_open_source" / "_INSTALADOS.md", health)
    doc["pruned"], doc["installed_updated"], doc["graph"] = pruned, installed, graph
    if write:                                # auto-monitoreo (patrón #15): sources/orchestrator/_audit.jsonl
        active = {n: h for n, h in health.items() if h["status"] != "diseño"}
        problems = sum(1 for h in active.values() if h["status"] in ("caído", "atrasado", "vacío", "sin_datos"))
        line = audit.audit_line("orchestrator", now, stats.get("read", 0), merged, problems, len(active),
                                time.time() - t_start)
        doc["metrics"] = audit.record_run(base / "orchestrator", line, len(active) - problems, len(active))
    return doc


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    doc = run(store.ROOT, write=not args.dry_run)
    print(f"orchestrator: {doc['merged_items']} ítems en _merged (48 h) · podados {len(doc['pruned'])}"
          f" · _INSTALADOS {'actualizado' if doc['installed_updated'] else 'sin cambios'} · grafo {doc['graph']}")
    for n, h in sorted(doc["bots"].items()):
        print(f"  {n:10s} {h['status']:10s} " + "; ".join(h.get("errors") or [])[:200])
    return 0


if __name__ == "__main__":
    sys.exit(main())
