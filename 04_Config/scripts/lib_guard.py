#!/usr/bin/env python3
"""
lib_guard.py — compuerta de seguridad pre-push.

Detecta:
- gitlinks (entradas modo 160000)
- secretos hardcodeados
- rutas literales '02_Analisis/' en .py fuera de lib_paths.py
- número excesivo de archivos modificados (posible 'git add -A' sin ruta)

Uso:
    from lib_guard import check
    result = check()
    if not result["ok"]:
        for issue in result["issues"]:
            print(f"{issue['tipo']}: {issue['detalle']} ({issue['ruta']})")
"""
import os
import re
import subprocess
from pathlib import Path
from typing import Optional

# Secretos conocidos (patrones que no deben aparecer en código)
SECRET_PATTERNS = [
    (re.compile(r"HELIUS_API_KEY\s*=\s*['\"][^'\"]+['\"]"), "HELIUS_API_KEY"),
    (re.compile(r"TELEGRAM_BOT_TOKEN\s*=\s*['\"][^'\"]+['\"]"), "TELEGRAM_BOT_TOKEN"),
    (re.compile(r"TELEGRAM_CHAT_ID\s*=\s*['\"][^'\"]+['\"]"), "TELEGRAM_CHAT_ID"),
    (re.compile(r"BIRDEYE_API_KEY\s*=\s*['\"][^'\"]+['\"]"), "BIRDEYE_API_KEY"),
    (re.compile(r"COINLOBBER_API_KEY\s*=\s*['\"][^'\"]+['\"]"), "COINLOBBER_API_KEY"),
    (re.compile(r"ADANOS_API_KEY\s*=\s*['\"][^'\"]+['\"]"), "ADANOS_API_KEY"),
    (re.compile(r"SANTIMENT_API_KEY\s*=\s*['\"][^'\"]+['\"]"), "SANTIMENT_API_KEY"),
    (re.compile(r"CHAINBASE_API_KEY\s*=\s*['\"][^'\"]+['\"]"), "CHAINBASE_API_KEY"),
    (re.compile(r"MADEONSOL_API_KEY\s*=\s*['\"][^'\"]+['\"]"), "MADEONSOL_API_KEY"),
    (re.compile(r"APEWISDOM_API_KEY\s*=\s*['\"][^'\"]+['\"]"), "APEWISDOM_API_KEY"),
    # Patrones genéricos
    (re.compile(r"['\"]?(?:api[_-]?key|secret|token|password)['\"]?\s*[:=]\s*['\"][A-Za-z0-9_\-]{20,}['\"]"), "GENERIC_SECRET"),
]

# Excepciones de archivos que pueden tener secretos (ej: .env, config)
SECRET_EXEMPT = {".env", ".env.example", "config.yaml", "config.yml", "secrets.yaml", "secrets.yml"}

# Rutas que están permitidas (lib_paths.py, tests, docs)
LITERAL_PATH_EXEMPT = {"lib_paths.py", "lib_guard.py"}


def check_gitlinks(cwd: Optional[str] = None) -> list[dict]:
    """Detecta entradas modo 160000 en git ls-tree -r HEAD."""
    issues = []
    try:
        result = subprocess.run(
            ["git", "ls-tree", "-r", "HEAD"],
            capture_output=True, text=True, timeout=30,
            cwd=cwd,
        )
        for line in result.stdout.splitlines():
            if line.startswith("160000"):
                parts = line.split()
                if len(parts) >= 4:
                    ruta = parts[3]
                    issues.append({
                        "tipo": "gitlink",
                        "detalle": "Submódulo/gitlink detectado (modo 160000)",
                        "ruta": ruta,
                    })
    except Exception as e:
        issues.append({
            "tipo": "gitlink",
            "detalle": f"Error al ejecutar git ls-tree: {e}",
            "ruta": "",
        })
    return issues


def check_rutas_literales(files: Optional[list[str]] = None, cwd: Optional[str] = None) -> list[dict]:
    """Detecta rutas literales '02_Analisis/' en archivos .py que no sean lib_paths.py."""
    issues = []
    target_files = files or []

    # Si no se pasan archivos, usar git diff --cached --name-only
    if not target_files:
        try:
            result = subprocess.run(
                ["git", "diff", "--cached", "--name-only"],
                capture_output=True, text=True, timeout=30,
                cwd=cwd,
            )
            target_files = [f.strip() for f in result.stdout.splitlines() if f.strip()]
        except Exception:
            pass

    literal_re = re.compile(r"['\"]02_Analisis/[^'\"]*['\"]")

    for f in target_files:
        # Solo archivos .py
        if not f.endswith(".py"):
            continue
        # Excepciones
        fname = os.path.basename(f)
        if any(fname.startswith(ex) for ex in LITERAL_PATH_EXEMPT):
            continue
        if fname == "lib_paths.py":
            continue

        # Resolver ruta relativa a cwd si se proporciona
        fpath = Path(f) if cwd is None else Path(cwd) / f

        try:
            with open(fpath, "r", encoding="utf-8") as fh:
                content = fh.read()
            for match in literal_re.finditer(content):
                line_num = content[:match.start()].count("\n") + 1
                issues.append({
                    "tipo": "ruta_literal",
                    "detalle": f"Ruta literal '02_Analisis/' en línea {line_num}: {match.group()}",
                    "ruta": f,
                })
        except Exception:
            pass
    return issues


def check_secretos_fuera_dominio(files: Optional[list[str]] = None, env: Optional[dict] = None, cwd: Optional[str] = None) -> list[dict]:
    """Detecta si algún secreto aparece hardcodeado en código."""
    issues = []
    target_files = files or []

    if not target_files:
        try:
            result = subprocess.run(
                ["git", "diff", "--cached", "--name-only"],
                capture_output=True, text=True, timeout=30,
                cwd=cwd,
            )
            target_files = [f.strip() for f in result.stdout.splitlines() if f.strip()]
        except Exception:
            pass

    for f in target_files:
        fname = os.path.basename(f)
        if fname in SECRET_EXEMPT:
            continue

        # Resolver ruta relativa a cwd si se proporciona
        fpath = Path(f) if cwd is None else Path(cwd) / f

        try:
            with open(fpath, "r", encoding="utf-8") as fh:
                content = fh.read()
        except Exception:
            continue

        for pattern, name in SECRET_PATTERNS:
            for match in pattern.finditer(content):
                line_num = content[:match.start()].count("\n") + 1
                # Verificar si es una asignación desde os.environ/env
                context = content[max(0, match.start()-50):match.end()+50]
                if "os.environ" in context or "os.getenv" in context or "env.get" in context:
                    continue  # Es lectura desde entorno, OK
                issues.append({
                    "tipo": "secreto_hardcodeado",
                    "detalle": f"Secreto {name} detectado en línea {line_num}",
                    "ruta": f,
                })
    return issues


def check_excesivos_archivos(files: Optional[list[str]] = None, cwd: Optional[str] = None) -> list[dict]:
    """Detecta si hay demasiados archivos modificados (posible git add -A)."""
    issues = []
    target_files = files or []

    if not target_files:
        try:
            result = subprocess.run(
                ["git", "diff", "--cached", "--name-only"],
                capture_output=True, text=True, timeout=30,
                cwd=cwd,
            )
            target_files = [f.strip() for f in result.stdout.splitlines() if f.strip()]
        except Exception:
            pass

    # Umbral: más de 20 archivos modificados en un solo commit
    if len(target_files) > 20:
        issues.append({
            "tipo": "muchos_archivos",
            "detalle": f"{len(target_files)} archivos modificados en un commit (posible 'git add -A' sin ruta)",
            "ruta": "",
        })
    return issues


def check(files: Optional[list[str]] = None, env: Optional[dict] = None, cwd: Optional[str] = None) -> dict:
    """
    Función principal de verificación.

    files: lista opcional de rutas a verificar (default: git diff --cached --name-only).
    env: dict opcional (default: os.environ).

    Retorna: {"ok": bool, "issues": [{"tipo": str, "detalle": str, "ruta": str}]}
    """
    all_issues = []

    all_issues.extend(check_gitlinks(cwd))
    all_issues.extend(check_rutas_literales(files, cwd))
    all_issues.extend(check_secretos_fuera_dominio(files, env, cwd))
    all_issues.extend(check_excesivos_archivos(files, cwd))

    return {
        "ok": len(all_issues) == 0,
        "issues": all_issues,
    }


if __name__ == "__main__":
    # CLI simple para pruebas
    result = check()
    if result["ok"]:
        print("OK: No issues found")
    else:
        for issue in result["issues"]:
            print(f"[{issue['tipo']}] {issue['detalle']} ({issue['ruta']})")
        exit(1)