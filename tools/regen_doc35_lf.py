#!/usr/bin/env python3
"""
regen_doc35_lf.py — Regenera hashes SHA-256 del doc 35 calculándolos sobre
blobs LF de origin/main (no working copy con CRLF).
"""

import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # Project root
DOC35_PATH = ROOT / "El cerebro de dios" / "35_TRASPASO_CLAUDE.md"


def get_blob_hash(filepath_str):
    """Obtiene SHA-256 del blob en origin/main (LF nativo)."""
    try:
        # git cat-file -p origin/main:path
        result = subprocess.run(
            ["git", "cat-file", "-p", f"origin/main:{filepath_str}"],
            capture_output=True,
            check=True,
            cwd=ROOT
        )
        return hashlib.sha256(result.stdout).hexdigest()
    except subprocess.CalledProcessError:
        return None


def main():
    # Backup
    backup = DOC35_PATH.with_suffix(".md.bak2")
    content = DOC35_PATH.read_text(encoding="utf-8")
    backup.write_text(content, encoding="utf-8")
    print(f"Backup creado: {backup}")

    # Regex para encontrar líneas de la tabla de inventario
    pattern = re.compile(
        r"^\| `(.+?)` \| .+? \| .+? \| `([a-f0-9]{64})` \|$",
        re.MULTILINE
    )

    matches = list(pattern.finditer(content))
    print(f"Encontradas {len(matches)} entradas con hash SHA-256")

    checked = 0
    updated = 0
    unchanged = 0
    not_found = 0

    new_content = content

    for match in matches:
        filepath_str = match.group(1)
        old_hash = match.group(2)
        checked += 1

        # Obtener hash del blob LF en origin/main
        new_hash = get_blob_hash(filepath_str)

        if new_hash is None:
            print(f"  ⚠️  NO ENCONTRADO en origin/main: {filepath_str}")
            not_found += 1
            continue

        if new_hash == old_hash:
            unchanged += 1
            continue

        # Actualizar en el contenido
        old_line = match.group(0)
        new_line = old_line.replace(old_hash, new_hash)
        new_content = new_content.replace(old_line, new_line, 1)
        print(f"  ✅ ACTUALIZADO: {filepath_str}")
        print(f"     {old_hash[:16]}... -> {new_hash[:16]}...")
        updated += 1

    # Escribir cambios
    if new_content != content:
        DOC35_PATH.write_text(new_content, encoding="utf-8")
        print(f"\nArchivo actualizado: {DOC35_PATH}")
    else:
        print("\nSin cambios necesarios")

    print(f"\nResumen:")
    print(f"  Revisados: {checked}")
    print(f"  Actualizados: {updated}")
    print(f"  Sin cambios: {unchanged}")
    print(f"  No encontrados: {not_found}")

    return 0


if __name__ == "__main__":
    sys.exit(main())