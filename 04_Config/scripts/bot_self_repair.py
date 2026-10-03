#!/usr/bin/env python3
"""
bot_self_repair.py — bot reparador de los bots de fuentes (patrón #20; doc 34 §11). Cada 30 min
(sources_self_repair.yml). Solo reglas explícitas: cero IA generativa. Lo que no está en la tabla lo escala.

  Detección                                 Fix (idempotente, reversible)                   Escala si
  fuente caída: fails >= 3 seguidas          auto_off 6 h en _repair_state.json (el bot      sigue caída 24 h después
                                             la salta y después reintenta una vez)
  workflow de bot: >= 2 fallas seguidas      1 rerun de los jobs fallidos (una vez por run)  > 3 fallas seguidas
  otro workflow: > 3 fallas seguidas         ninguno (no se relanza producción)              de inmediato
  bot atrasado (_health.json)                1 workflow_dispatch                              atraso repetido en 24 h
  salida vacía                               ninguno (un parser roto no se arregla con reglas) > 24 h sin ítems, o vacío
                                                                                             con todas las fuentes OK
  _state.json / _health.json que no parsea   se renombra a .corrupt-<ts> (el dueño lo recrea) más de 1 por día
  _state.json inflado (seen > 50.000)        recorta seen a la ventana de dedup              —

Archivos propios (un dueño por archivo): 02_Analisis/sources/_repair_state.json y _repair_log.jsonl (7 días),
_episodes_self_repair.jsonl (memoria episódica #12: feed_caido y bot_reparado, solo transiciones), más el
bloque <!-- AUTO:repair --> de _servicios_open_source/_INSTALADOS.md (una fila por problema abierto; se borra
sola al resolverse). Toca el _state.json de un bot solo para renombrarlo si está corrupto o recortar `seen`.
No toca código, YAML de configuración, score ni emisión.

Uso: python 04_Config/scripts/bot_self_repair.py [--dry-run]   (sin GITHUB_TOKEN: detecta y escala, no actúa)
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_episodic_memory as episodes  # noqa: E402
import lib_sources_store as store  # noqa: E402

VERSION = "repair-0.1"
FAIL_RUNS = 3                 # fuente: fallas seguidas para apagarla
AUTO_OFF_S = 6 * 3600
SOURCE_ESCALATE_S = 24 * 3600
WF_RERUN_AT = 2               # workflow de bot: fallas seguidas para relanzar
WF_ESCALATE_ABOVE = 3         # workflow: más de 3 fallas seguidas -> escala
DISPATCH_WINDOW_S = 24 * 3600
EMPTY_ESCALATE_S = 24 * 3600
SEEN_MAX = 50_000
STATE_MAX_BYTES = 5 * 1024 * 1024
LOG_KEEP_S = 7 * 86400
AUTO_START, AUTO_END = "<!-- AUTO:repair -->", "<!-- /AUTO:repair -->"
API = "https://api.github.com"


class GitHub:
    """API de Actions con el GITHUB_TOKEN del workflow. Sin token, las acciones no se ejecutan."""

    def __init__(self, token=None, repo=None, http=None):
        self.token, self.repo = token, repo
        self.http = http

    @property
    def enabled(self):
        return bool(self.token and self.repo)

    def _req(self, method, path, body=None):
        import requests
        http = self.http or requests
        headers = {"Authorization": f"Bearer {self.token}", "Accept": "application/vnd.github+json",
                   "X-GitHub-Api-Version": "2022-11-28"}
        r = http.request(method, f"{API}/repos/{self.repo}{path}", headers=headers, json=body, timeout=20)
        return r.status_code, (r.json() if r.content and r.status_code < 300 else None)

    def runs(self, workflow, per_page=10):
        """Corridas terminadas, de la más nueva a la más vieja: [{id, conclusion, html_url, created_at}]. """
        status, data = self._req("GET", f"/actions/workflows/{workflow}/runs?per_page={per_page}&status=completed")
        return [{k: r.get(k) for k in ("id", "conclusion", "html_url", "created_at")}
                for r in (data or {}).get("workflow_runs") or []] if status == 200 else None

    def workflows(self):
        status, data = self._req("GET", "/actions/workflows?per_page=100")
        if status != 200:
            return None
        return [Path(w["path"]).name for w in (data or {}).get("workflows") or [] if w.get("state") == "active"]

    def rerun_failed(self, run_id):
        return self._req("POST", f"/actions/runs/{run_id}/rerun-failed-jobs")[0] in (201, 204)

    def dispatch(self, workflow, ref="main"):
        return self._req("POST", f"/actions/workflows/{workflow}/dispatches", {"ref": ref})[0] == 204


def read_json(path):
    """(dato, estado): estado 'ok', 'missing' o 'corrupt'."""
    try:
        return json.loads(Path(path).read_text(encoding="utf-8")), "ok"
    except FileNotFoundError:
        return None, "missing"
    except (OSError, ValueError):
        return None, "corrupt"


def consecutive_failures(runs):
    n = 0
    for r in runs or []:
        if r.get("conclusion") in ("failure", "timed_out"):
            n += 1
        elif r.get("conclusion") in ("cancelled", "skipped"):
            continue
        else:
            break
    return n


def bot_sources(state):
    return (state or {}).get("feeds") or (state or {}).get("sources") or (state or {}).get("channels") or {}


class Repair:
    def __init__(self, root, registry, gh, now=None, write=True):
        self.root, self.registry, self.gh = Path(root), registry, gh
        self.now = now if now is not None else time.time()
        self.write = write
        self.base = store.sources_dir(root)
        prev, _ = read_json(self.base / "_repair_state.json")
        prev = prev if isinstance(prev, dict) else {}
        self.state = {"version": VERSION, "auto_off": prev.get("auto_off") or {}, "reruns": prev.get("reruns") or {},
                      "dispatches": prev.get("dispatches") or {}, "last_nonempty": prev.get("last_nonempty") or {},
                      "corrupt": prev.get("corrupt") or {}, "escalations": prev.get("escalations") or {}}
        self.open = set()          # escaladas vigentes en esta corrida
        self.actions = []

    # -- registro ---------------------------------------------------------------------------------------------
    def act(self, bot, detection, action, evidence):
        self.actions.append({"ts": int(self.now), "bot": bot, "detection": detection, "action": action,
                             "evidence": evidence})

    def escalate(self, key, bot, detection, evidence):
        self.open.add(key)
        esc = self.state["escalations"].get(key)
        if not esc:
            self.state["escalations"][key] = {"since": int(self.now), "bot": bot, "detection": detection,
                                              "evidence": evidence}
            self.act(bot, detection, "escalate", evidence)
        else:
            esc["evidence"] = evidence

    # -- reglas -----------------------------------------------------------------------------------------------
    def check_states(self):
        for bot, cfg in self.registry.items():
            if cfg.get("enabled", True) is False:
                continue
            for path in sorted((self.base / bot).glob("_state*.json")):
                if ".corrupt-" in path.name:
                    continue
                state, status = read_json(path)
                if status == "corrupt":
                    self.reset_corrupt(bot, path)
                    continue
                if status == "ok":
                    self.check_sources(bot, state)
                    self.trim_seen(bot, path, state, cfg)

    def reset_corrupt(self, bot, path):
        day = datetime.fromtimestamp(self.now, timezone.utc).strftime("%Y-%m-%d")
        key = f"{path.name}|{day}"
        count = self.state["corrupt"].get(key, 0) + 1
        self.state["corrupt"] = {k: v for k, v in self.state["corrupt"].items() if k.endswith(day)} | {key: count}
        target = path.with_name(f"{path.name}.corrupt-{int(self.now)}")
        if self.write:
            path.rename(target)
        self.act(bot, "archivo corrupto", "reset_state", f"{path.name} -> {target.name}")
        if count > 1:
            self.escalate(f"corrupt:{bot}:{path.name}", bot, "archivo corrupto repetido",
                          f"{path.name}: {count} veces hoy")

    def check_sources(self, bot, state):
        offs = self.state["auto_off"].setdefault(bot, {})
        sources = bot_sources(state)
        for name, row in sources.items():
            fails = int((row or {}).get("fails") or 0)
            healthy = (row or {}).get("status") == 200 and not (row or {}).get("parse_error") and fails == 0
            key = f"source:{bot}:{name}"
            if healthy:
                if name in offs:
                    self.act(bot, "fuente recuperada", "auto_on", name)
                offs.pop(name, None)
                continue
            if fails < FAIL_RUNS:
                continue
            off = offs.get(name)
            if not off:
                offs[name] = {"first_seen": int(self.now), "until": int(self.now + AUTO_OFF_S)}
                self.act(bot, "fuente caída", "auto_off", f"{name}: {row.get('status')} x{fails}")
            elif self.now >= off["until"]:
                # Fix: solo renovar si el bot consultó la fuente DESPUÉS de que venció el apagado anterior.
                # last_run del bot (si existe) > off["until"] = el bot corrió después del vencimiento y falló.
                # Si no corrió, NO renovar: dejar que el bot intente en su próxima corrida.
                bot_last_run = 0
                for path in (self.base / bot).glob("_state*.json"):
                    if ".corrupt-" in path.name:
                        continue
                    state, status = read_json(path)
                    if status == "ok" and isinstance(state.get("last_run"), (int, float)):
                        bot_last_run = max(bot_last_run, state["last_run"])
                if bot_last_run > off["until"]:
                    off["until"] = int(self.now + AUTO_OFF_S)
                    self.act(bot, "fuente sigue caída", "auto_off", f"{name}: {row.get('status')} x{fails}")
                else:
                    # bot no corrió tras el vencimiento: no renovar, que intente en su próxima corrida
                    self.act(bot, "fuente sigue caída", "auto_off_sin_renovar",
                             f"{name}: bot no corrió tras vencimiento, reintenta en próxima")
            if offs.get(name) and self.now - offs[name]["first_seen"] >= SOURCE_ESCALATE_S:
                self.escalate(key, bot, "fuente caída 24 h (P-13: reemplazar)", f"{name}: {row.get('status')} x{fails}")
        for name in list(offs):
            if name not in sources:                     # la fuente se sacó del YAML: no queda nada abierto
                offs.pop(name)
        if not offs:
            self.state["auto_off"].pop(bot, None)

    def trim_seen(self, bot, path, state, cfg):
        seen = state.get("seen") or {}
        too_big = path.stat().st_size > STATE_MAX_BYTES if path.exists() else False
        if len(seen) <= SEEN_MAX and not too_big:
            return
        keep_s = float(cfg.get("dedup_hours") or 72) * 3600
        state["seen"] = {k: t for k, t in seen.items() if isinstance(t, (int, float)) and self.now - t <= keep_s}
        if self.write:
            path.write_text(json.dumps(state, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
        self.act(bot, "estado inflado", "trim_seen", f"{path.name}: seen {len(seen)} -> {len(state['seen'])}")

    def check_health(self):
        health, status = read_json(self.base / "_health.json")
        if status == "corrupt":
            target = self.base / f"_health.json.corrupt-{int(self.now)}"
            if self.write:
                (self.base / "_health.json").rename(target)
            self.act("orchestrator", "archivo corrupto", "reset_state", f"_health.json -> {target.name}")
            return
        bots = (health or {}).get("bots") or {}
        for bot, cfg in self.registry.items():
            h = bots.get(bot) or {}
            if cfg.get("enabled", True) is False or h.get("status") in (None, "diseño", "sin_datos"):
                continue
            if (h.get("last_output") or 0) > 0:
                self.state["last_nonempty"][bot] = int(h.get("last_run") or self.now)
            last = self.state["last_nonempty"].setdefault(bot, int(self.now))
            if h.get("status") in ("ok", "vacío") and self.now - last > EMPTY_ESCALATE_S:   # corre, pero sin ítems
                self.escalate(f"empty:{bot}", bot, "sin ítems hace más de 24 h", f"último ítem: {_fmt(last)}")
            if h.get("status") == "vacío" and h.get("sources_total") and h.get("sources_ok") == h.get("sources_total"):
                self.escalate(f"parser:{bot}", bot, "vacío con todas las fuentes OK (¿cambió el formato?)",
                              f"{h.get('empty_runs')} corridas sin ítems")
            if h.get("status") == "atrasado":
                self.handle_late(bot, cfg, h)

    def handle_late(self, bot, cfg, h):
        recent = [t for t in self.state["dispatches"].get(bot) or [] if self.now - t <= DISPATCH_WINDOW_S]
        if recent:
            self.escalate(f"late:{bot}", bot, "atraso repetido en 24 h", f"última corrida: {_fmt(h.get('last_run'))}")
        elif self.gh.enabled and cfg.get("workflow"):
            ok = self.write and self.gh.dispatch(cfg["workflow"])
            recent.append(int(self.now))
            self.act(bot, "bot atrasado", "dispatch" if ok else "dispatch_failed", cfg["workflow"])
        else:
            self.act(bot, "bot atrasado", "sin_token", cfg.get("workflow") or "—")
        self.state["dispatches"][bot] = recent

    def check_workflows(self):
        if not self.gh.enabled:
            return
        bot_wf = {cfg.get("workflow"): bot for bot, cfg in self.registry.items()
                  if cfg.get("workflow") and cfg.get("enabled", True) is not False}
        for wf in self.gh.workflows() or sorted(bot_wf):
            runs = self.gh.runs(wf)
            if not runs:
                continue
            n = consecutive_failures(runs)
            owner = bot_wf.get(wf, "workflow")
            failed = next((r for r in runs if r.get("conclusion") in ("failure", "timed_out")), None)
            if n >= WF_RERUN_AT and wf in bot_wf and failed and str(failed["id"]) not in self.state["reruns"]:
                ok = self.write and self.gh.rerun_failed(failed["id"])
                self.state["reruns"][str(failed["id"])] = int(self.now)
                self.act(owner, f"workflow con {n} fallas seguidas", "rerun" if ok else "rerun_failed",
                         failed.get("html_url") or str(failed["id"]))
            if n > WF_ESCALATE_ABOVE:
                self.escalate(f"workflow:{wf}", owner, f"workflow {wf} con {n} fallas seguidas",
                              failed.get("html_url") if failed else "—")
        self.state["reruns"] = {k: t for k, t in self.state["reruns"].items() if self.now - t <= LOG_KEEP_S}

    # -- salida -----------------------------------------------------------------------------------------------
    def finish(self):
        resolved = [k for k in self.state["escalations"] if k not in self.open]
        for k in resolved:
            esc = self.state["escalations"].pop(k)
            self.act(esc["bot"], esc["detection"], "resolved", k)
        self.state["last_run"] = int(self.now)
        self.state["open"] = len(self.state["escalations"])
        if self.write:
            self.base.mkdir(parents=True, exist_ok=True)
            (self.base / "_repair_state.json").write_text(
                json.dumps(self.state, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
            append_log(self.base / "_repair_log.jsonl", self.actions, self.now)
            episodes.write_episodes(episodes.repair_episodes(self.actions, self.now), self.root, "self_repair")
            update_installed(self.root / "_servicios_open_source" / "_INSTALADOS.md", self.state["escalations"])
        return {"actions": self.actions, "escalations": self.state["escalations"]}

    def run(self):
        self.check_states()
        self.check_health()
        self.check_workflows()
        return self.finish()


def _fmt(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d %H:%M UTC") if ts else "n/d"


def append_log(path, actions, now):
    rows = [r for r in store.read_jsonl(path) if now - (r.get("ts") or 0) <= LOG_KEEP_S] + list(actions)
    tmp = Path(str(path) + ".tmp")
    tmp.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
    tmp.replace(path)


def repair_block(escalations):
    rows = "\n".join(f"- [P] {_fmt(e['since'])[:10]} `{e['bot']}` {e['detection']} — {e['evidence']}"
                     for _, e in sorted(escalations.items(), key=lambda kv: (kv[1]["since"], kv[0])))
    return (f"{AUTO_START}\n## Reparaciones escaladas (automático: bot_self_repair)\n\n"
            f"{rows or '- Sin problemas abiertos.'}\n{AUTO_END}")


def update_installed(path, escalations):
    """Reescribe solo el bloque AUTO:repair; el resto (incluido AUTO:sources) no se toca. True si cambió."""
    path = Path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    block = repair_block(escalations)
    if AUTO_START in text and AUTO_END in text:
        new = text[:text.index(AUTO_START)] + block + text[text.index(AUTO_END) + len(AUTO_END):]
    else:
        new = text.rstrip("\n") + "\n\n" + block + "\n"
    if new == text:
        return False
    path.write_text(new, encoding="utf-8")
    return True


def load_registry(root):
    import yaml
    doc = yaml.safe_load((Path(root) / "04_Config" / "sources" / "_bots.yaml").read_text(encoding="utf-8")) or {}
    return doc.get("bots") or {}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    gh = GitHub(os.environ.get("GITHUB_TOKEN"), os.environ.get("GITHUB_REPOSITORY"))
    out = Repair(store.ROOT, load_registry(store.ROOT), gh, write=not args.dry_run).run()
    print(f"self_repair: {len(out['actions'])} acciones · {len(out['escalations'])} problemas abiertos"
          + ("" if gh.enabled else " · sin GITHUB_TOKEN: solo detección"))
    for a in out["actions"]:
        print(f"  {a['bot']:12s} {a['action']:14s} {a['detection']} — {a['evidence']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
