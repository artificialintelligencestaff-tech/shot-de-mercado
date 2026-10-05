#!/usr/bin/env python3
"""
audit_gate.py — compuertas deterministas de auditoría para cada pull request (Ola 3, D-067; C-005 P4).
Sin LLM. Lo llama .github/workflows/audit_gate.yml; cada subcomando sale con código 1 si su compuerta falla.

  tests [--no-install]          instala dependencias (install_deps) y corre la batería completa, archivo por archivo,
                                con PYTHONUTF8=1 y REQUIRE_TEST_DEPS=1 (decide por exit code)
  doc35 [--rev R] [--update]    SHA-256 de cada archivo del inventario del doc 35 contra el BLOB de git (LF, el
                                mismo contenido en Windows y en Linux). --update reescribe los hashes desde el blob.
  prohibited --base B           líneas AGREGADAS en el PR: --force / reset --hard en comandos, TELEGRAM_CHAT_ID en
                                código, secretos con forma conocida, archivos .env
                                rutas literales de datos (D-105): cero en MODULOS_AUTONOMOS, ninguna nueva en el resto
  touched --base B              workflows y archivos de producción (doc 35) tocados (informativo)
  bundle --base B --out F       audit_bundle.md: stat + diff de código sin 02_Analisis/ + resultados
Solo biblioteca estándar.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
DOC35_REL = "El cerebro de dios/35_TRASPASO_CLAUDE.md"
DOC35_ROW = re.compile(r"^\| `(.+?)` \| .+? \| (.+?) \| `([a-f0-9]{64})` \|$", re.MULTILINE)
SELF = {"04_Config/scripts/audit_gate.py", "04_Config/scripts/test_audit_gate.py", ".github/workflows/audit_gate.yml"}
DATA_PREFIXES = ("02_Analisis/", "_auditoria/")

# Los patrones se arman por partes para que este archivo no se denuncie a sí mismo si alguien lo saca de SELF.
_F = "--" + "force"
CMD_RULES = [                                   # en .yml / .yaml / .sh / .ps1 / .bat (comandos de shell)
    ("force_push", re.compile(re.escape(_F) + r"(-with-lease)?\b|\bpush\s+-f\b")),
    ("reset_hard", re.compile(r"\breset\s+--hard\b")),
]
PY_RULES = [                                    # en .py, fuera de comentarios: argumentos de subprocess
    ("force_push", re.compile(r"[\"']" + re.escape(_F) + r"(-with-lease)?[\"']|push\s+(-f|" + re.escape(_F) + r")\b")),
    ("reset_hard", re.compile(r"reset\s+--hard|[\"']reset[\"']\s*,\s*[\"']--hard[\"']")),
]
CHAT_RULE = ("telegram_chat_id", re.compile(r"\bTELEGRAM_" + r"CHAT_ID\b"))
SECRET_RULES = [
    ("telegram_bot_token", re.compile(r"\b\d{8,10}:[A-Za-z0-9_-]{35}\b")),
    ("github_token", re.compile(r"\b(gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{22,})\b")),
    ("aws_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("private_key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE " + r"KEY-----")),
    ("slack_token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}")),
    ("llm_api_key", re.compile(r"\bsk-(ant-)?[A-Za-z0-9_-]{24,}")),
    ("secret_assignment", re.compile(r"(?i)\b(api[_-]?key|secret|token|password)\b\s*[:=]\s*[\"'][A-Za-z0-9_\-]{24,}[\"']")),
]


def git(*args, check=True):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and r.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout


def git_blob(rev, path):
    r = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True)
    return r.stdout if r.returncode == 0 else None


# ---------------------------------------------------------------------------
# a) batería
# ---------------------------------------------------------------------------

REQ_FILES = ("requirements-dev.txt", "requirements.txt")              # en la raíz del repo, en este orden
BS4_PINNED = "04_Config/requirements/sources_telegram.txt"            # bs4 + soupsieve + typing-extensions con hash


def _pip(args, run=subprocess.run):
    r = run([sys.executable, "-m", "pip", "install", "--disable-pip-version-check", "-q", *args],
            capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout + r.stderr).strip()[-800:]


def _has_bs4():
    try:
        import bs4  # noqa: F401
        return True
    except ImportError:
        return False


def install_deps(root=None, pip=_pip, has_bs4=_has_bs4):
    """Antes de la batería (D-075): instala el primer archivo de REQ_FILES que exista y, si después sigue faltando
    bs4, el archivo fijado con hashes. Un archivo con `--hash=` se instala con --require-hashes --no-deps (supply
    chain: todo lo que entra está fijado y verificado, incluidas las transitivas).
    Que no exista ningún requirements no es error. Devuelve [{"step", "rc", "detail"}]; rc != 0 = falla."""
    root = Path(root or ROOT)
    steps = []
    req = next((root / f for f in REQ_FILES if (root / f).is_file()), None)
    if req is None:
        steps.append({"step": "requirements", "rc": 0, "detail": f"sin {' ni '.join(REQ_FILES)}: nada que instalar"})
    else:
        hashed = "--hash=" in req.read_text(encoding="utf-8")
        rc, out = pip((["--require-hashes", "--no-deps"] if hashed else []) + ["-r", str(req)])
        steps.append({"step": req.name, "rc": rc, "detail": out or "ok"})
    if not has_bs4():
        pinned = root / BS4_PINNED
        if pinned.is_file():
            rc, out = pip(["--require-hashes", "--no-deps", "-r", str(pinned)])
            steps.append({"step": "bs4 (fijado con hash)", "rc": rc, "detail": out or "ok"})
        else:
            steps.append({"step": "bs4", "rc": 1, "detail": f"falta bs4 y no existe {BS4_PINNED}"})
    return steps


def run_tests(root=None, timeout=600):
    root = Path(root or ROOT)
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8", SHOT_ROOT=str(root), REQUIRE_TEST_DEPS="1")
    results = []
    for f in sorted((root / "04_Config" / "scripts").glob("test_*.py")):
        t0 = time.time()
        try:
            r = subprocess.run([sys.executable, str(f)], cwd=root, capture_output=True, text=True, env=env,
                               timeout=timeout, encoding="utf-8", errors="replace")
            out, rc = r.stdout + r.stderr, r.returncode
        except subprocess.TimeoutExpired:
            out, rc = "TIMEOUT", 124
        ran = re.findall(r"^Ran (\d+) test", out, re.MULTILINE)
        ok = rc == 0 and re.search(r"^OK", out, re.MULTILINE) is not None
        results.append({"file": f.name, "ok": ok, "rc": rc, "tests": int(ran[-1]) if ran else 0,
                        "seconds": round(time.time() - t0, 1), "tail": "" if ok else out[-1500:]})
    return results


# ---------------------------------------------------------------------------
# b) doc 35 contra blobs
# ---------------------------------------------------------------------------

def doc35_rows(text):
    return [{"path": m.group(1), "state": m.group(2).strip(), "sha": m.group(3), "line": m.group(0)}
            for m in DOC35_ROW.finditer(text)]


def check_doc35(text, blob):
    """[{path, expected, actual, problem}] para cada fila con problema; `blob(path)` devuelve bytes o None."""
    bad = []
    for row in doc35_rows(text):
        if row["state"] == "borrado":
            continue
        data = blob(row["path"])
        if data is None:
            bad.append(dict(row, actual=None, problem="no existe en el commit"))
            continue
        actual = hashlib.sha256(data).hexdigest()
        if actual != row["sha"]:
            bad.append(dict(row, actual=actual, problem="hash distinto"))
    return bad


def update_doc35(text, blob):
    for row in check_doc35(text, blob):
        if row["actual"]:
            text = text.replace(row["line"], row["line"].replace(row["sha"], row["actual"]), 1)
    return text


# ---------------------------------------------------------------------------
# c) prohibidos sobre las líneas agregadas
# ---------------------------------------------------------------------------

def added_lines(diff_text):
    """Diff unificado → {ruta: [(n_línea, texto)]} solo con líneas agregadas, más el set de archivos nuevos."""
    out, new_files, path, prev, n = {}, set(), None, None, 0
    for line in diff_text.splitlines():
        if line.startswith("+++ "):
            name = line[4:].strip().strip('"')
            path = None if name == "/dev/null" else name.removeprefix("b/")
            continue
        if line.startswith("--- "):
            prev = line[4:].strip().strip('"')
            continue
        if line.startswith("@@"):
            m = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)", line)
            n = int(m.group(1)) - 1 if m else 0
            if path and prev == "/dev/null":
                new_files.add(path)
            continue
        if path is None:
            continue
        if line.startswith("+"):
            n += 1
            out.setdefault(path, []).append((n, line[1:]))
        elif not line.startswith("-"):
            n += 1
    return out, new_files


def scan(diff_text):
    hits = []
    lines, new_files = added_lines(diff_text)
    for path in sorted(new_files | set(lines)):
        name = path.rsplit("/", 1)[-1]
        if name == ".env" or name.endswith(".env"):
            hits.append({"rule": "env_file", "path": path, "line": 0, "text": name})
    for path, rows in sorted(lines.items()):
        if path in SELF or path.startswith(DATA_PREFIXES):
            continue
        name = path.rsplit("/", 1)[-1]
        is_test = name.startswith("test_")
        ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
        for n, text in rows:
            for rule, rx in SECRET_RULES:                        # secretos: en cualquier archivo
                if rx.search(text):
                    hits.append({"rule": rule, "path": path, "line": n, "text": text.strip()[:160]})
            if ext == "md" or is_test:
                continue
            code = text.strip()
            if ext in ("yml", "yaml", "sh", "ps1", "bat"):
                if code.startswith("#"):
                    continue
                rules = CMD_RULES + [CHAT_RULE]
            elif ext == "py":
                if code.startswith("#"):
                    continue
                rules = PY_RULES + [CHAT_RULE]
            else:
                continue
            for rule, rx in rules:
                if rx.search(text):
                    hits.append({"rule": rule, "path": path, "line": n, "text": code[:160]})
    return hits


# ---------------------------------------------------------------------------
# c2) rutas literales (D-105, doc 38 §6): ningún módulo arma la ruta física de otro; todas salen de lib_paths
# ---------------------------------------------------------------------------

DATA_ROOT = "02_" + "Analisis"            # partido: este archivo no se marca a sí mismo
PATHS_LIB = "04_Config/scripts/lib_paths.py"
# Módulos migrados a lib_paths: CERO rutas literales en todo el archivo (estricto). El resto del código de
# producción tiene trinquete: no puede SUMAR rutas literales en líneas nuevas.
MODULOS_AUTONOMOS = tuple(f"04_Config/scripts/{n}.py" for n in (
    "script_97_emit_alerts", "script_98_trust_scheduler", "script_116_early_watch", "bot_orchestrator",
    "early_review", "bot_prelaunch_calendar", "lib_alerts", "lib_early_watch", "lib_sources_domain",
    "lib_sources_store"))


def literal_paths(source):
    """[(línea, fragmento)] de strings del código (no docstrings ni comentarios) que contienen el prefijo de datos
    o la ruta con barra invertida. Excepción: lib_paths (la tabla) la filtra quien llama."""
    import ast
    import io
    import tokenize
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return [(0, "no parsea")]
    docs = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.body:
            first = node.body[0]
            if isinstance(first, ast.Expr) and isinstance(getattr(first, "value", None), ast.Constant) \
                    and isinstance(first.value.value, str):
                docs.update(range(first.lineno, (first.end_lineno or first.lineno) + 1))
    out = []
    for tok in tokenize.generate_tokens(io.StringIO(source).readline):
        if tok.type == tokenize.STRING and DATA_ROOT in tok.string and tok.start[0] not in docs:
            out.append((tok.start[0], tok.string.strip()[:120]))
    return out


def check_rutas(read, changed_lines=None):
    """read(ruta) -> texto o None. Estricto en MODULOS_AUTONOMOS; trinquete en las líneas agregadas del resto."""
    hits = []
    for path in MODULOS_AUTONOMOS:
        text = read(path)
        for n, frag in literal_paths(text) if text is not None else []:
            hits.append({"rule": "ruta_literal", "path": path, "line": n, "text": frag})
    for path, rows in sorted((changed_lines or {}).items()):
        name = path.rsplit("/", 1)[-1]
        if (not path.endswith(".py") or path in MODULOS_AUTONOMOS or path == PATHS_LIB or name.startswith("test_")
                or path in SELF or path.startswith(DATA_PREFIXES)):
            continue
        text = read(path)
        added = {n for n, _ in rows}
        for n, frag in literal_paths(text) if text is not None else []:
            if n in added:
                hits.append({"rule": "ruta_literal_nueva", "path": path, "line": n, "text": frag})
    return hits


# ---------------------------------------------------------------------------
# d) tocados · e) bundle
# ---------------------------------------------------------------------------

SCRIPT_REF = re.compile(r"04_Config/scripts/([A-Za-z0-9_]+)\.py")
LOCAL_IMPORT = re.compile(r"^\s*(?:import|from)\s+([A-Za-z0-9_]+)", re.MULTILINE)


def workflow_closure(read, list_workflows):
    """Scripts que corre algún workflow más sus imports locales (transitivos): producción de hecho, aunque el
    doc 35 todavía no lo diga. `read(path)` devuelve texto o None; `list_workflows()` las rutas de los .yml."""
    todo = [m for wf in list_workflows() for m in SCRIPT_REF.findall(read(wf) or "")]
    seen = set()
    while todo:
        mod = todo.pop()
        if mod in seen:
            continue
        text = read(f"04_Config/scripts/{mod}.py")
        if text is None:
            continue
        seen.add(mod)
        todo += [m for m in LOCAL_IMPORT.findall(text) if m not in seen]
    return {f"04_Config/scripts/{m}.py" for m in seen}


def touched(changed, doc35_text, closure=()):
    prod = {r["path"] for r in doc35_rows(doc35_text) if r["state"].startswith("producci")} | set(closure)
    return {"workflows": sorted(p for p in changed if p.startswith(".github/workflows/")),
            "production": sorted(p for p in changed if p in prod),
            "data": sorted(p for p in changed if p.startswith(DATA_PREFIXES)),
            "code_docs": sorted(p for p in changed if not p.startswith(DATA_PREFIXES))}


def closure_at(rev):
    def read(path):
        b = git_blob(rev, path)
        return b.decode("utf-8", "replace") if b is not None else None
    wfs = [p for p in git("ls-tree", "-r", "--name-only", rev, ".github/workflows").splitlines() if p.endswith(".yml")]
    return workflow_closure(read, lambda: wfs)


def changed_files(base, head="HEAD"):
    mb = git("merge-base", base, head).strip()
    return mb, [p for p in git("diff", "--name-only", mb, head).splitlines() if p]


def bundle(base, head="HEAD", results=None):
    mb, changed = changed_files(base, head)
    doc35 = (git_blob(head, DOC35_REL) or b"").decode("utf-8", "replace")
    t = touched(changed, doc35, closure_at(head))
    stat = git("diff", "--stat", mb, head, "--", ".", ":(exclude)02_Analisis", ":(exclude)_auditoria")
    diff = git("diff", mb, head, "--", ".", ":(exclude)02_Analisis", ":(exclude)_auditoria")
    parts = [f"# audit_bundle — {head[:12]} contra merge-base {mb[:12]}", "",
             f"Archivos cambiados: {len(changed)} (datos de 02_Analisis/ y _auditoria/ fuera del diff: {len(t['data'])})",
             "", "## Workflows tocados", *(f"- `{p}`" for p in t["workflows"] or ["—"]),
             "", "## Archivos de producción tocados (doc 35 + scripts que corren los workflows y sus imports)", *(f"- `{p}`" for p in t["production"] or ["—"])]
    if results:
        parts += ["", "## Compuertas", "```json", json.dumps(results, ensure_ascii=False, indent=1), "```"]
    parts += ["", "## Stat (código y docs)", "```", stat.rstrip(), "```", "", "## Diff (código y docs)", "```diff",
              diff.rstrip(), "```", ""]
    return "\n".join(parts), t


def main(argv=None):
    ap = argparse.ArgumentParser(description="Compuertas deterministas de auditoría (Ola 3)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("tests")
    t.add_argument("--no-install", action="store_true", help="no instala dependencias antes de la batería")
    d = sub.add_parser("doc35")
    d.add_argument("--rev", default="HEAD")
    d.add_argument("--update", action="store_true")
    for name in ("prohibited", "touched", "bundle"):
        p = sub.add_parser(name)
        p.add_argument("--base", required=True)
        p.add_argument("--head", default="HEAD")
        if name == "bundle":
            p.add_argument("--out", default="audit_bundle.md")
            p.add_argument("--results", help="JSON con los resultados de las otras compuertas")
    a = ap.parse_args(argv)
    if a.cmd == "tests":
        if not a.no_install:
            steps = install_deps()
            for st in steps:
                print(f"deps: {st['step']} → rc={st['rc']} · {st['detail'].splitlines()[-1] if st['detail'] else ''}")
            if any(st["rc"] for st in steps):
                print("::error::la instalación de dependencias falló: la batería no corre con un entorno incompleto")
                return 1
        res = run_tests()
        bad = [r for r in res if not r["ok"]]
        print(f"batería: {sum(r['tests'] for r in res)} tests en {len(res)} archivos · archivos con fallas: {len(bad)}")
        for r in bad:
            print(f"::error::{r['file']} (rc={r['rc']})\n{r['tail']}")
        return 1 if bad else 0
    if a.cmd == "doc35":
        text = (git_blob(a.rev, DOC35_REL) or b"").decode("utf-8")
        if a.update:
            path = ROOT / DOC35_REL
            n = 1
            while Path(f"{path}.bak{n}").exists():
                n += 1
            Path(f"{path}.bak{n}").write_bytes(path.read_bytes())
            new = update_doc35(path.read_text(encoding="utf-8"), lambda p: git_blob(a.rev, p))
            path.write_text(new, encoding="utf-8", newline="\n")
            print(f"doc 35 actualizado desde los blobs de {a.rev} (backup .bak{n})")
            return 0
        bad = check_doc35(text, lambda p: git_blob(a.rev, p))
        print(f"doc 35: {len(doc35_rows(text))} filas · con problemas: {len(bad)}")
        for b in bad:
            print(f"::error::{b['path']}: {b['problem']} (doc {b['sha'][:12]}… · blob {(b['actual'] or '—')[:12]}…)")
        return 1 if bad else 0
    mb, changed = changed_files(a.base, a.head)
    if a.cmd == "prohibited":
        diff = git("diff", "-U0", mb, a.head)
        hits = scan(diff)
        hits += check_rutas(lambda p: (git_blob(a.head, p) or b"").decode("utf-8", "replace") or None,
                            added_lines(diff)[0])           # D-105: rutas literales
        print(f"prohibidos: {len(hits)} hallazgos en {len(changed)} archivos cambiados")
        for h in hits:
            print(f"::error file={h['path']},line={h['line']}::{h['rule']}: {h['text']}")
        return 1 if hits else 0
    if a.cmd == "touched":
        t = touched(changed, (git_blob(a.head, DOC35_REL) or b"").decode("utf-8", "replace"), closure_at(a.head))
        print(json.dumps({k: v for k, v in t.items() if k != "code_docs"}, ensure_ascii=False, indent=1))
        return 0
    results = json.loads(Path(a.results).read_text(encoding="utf-8")) if a.results else None
    text, _ = bundle(a.base, a.head, results)
    Path(a.out).write_text(text, encoding="utf-8")
    print(f"bundle: {a.out} ({len(text)} caracteres)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
