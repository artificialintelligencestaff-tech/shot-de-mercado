#!/usr/bin/env python3
"""
update_doc35_hashes.py — Regenera automáticamente los SHA-256 del doc 35 (35_TRASPASO_CLAUDE.md).

Uso: python 04_Config/scripts/update_doc35_hashes.py
"""

import hashlib
import re
import sys
from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parents[2]  # Project root
DOC35_PATH = ROOT / "El cerebro de dios" / "35_TRASPASO_CLAUDE.md"


def compute_sha256(filepath):
    """Calcula SHA-256 de un archivo."""
    try:
        with open(filepath, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except (OSError, FileNotFoundError):
        return None


def main():
    # Backup
    backup = DOC35_PATH.with_suffix(".md.bak1")
    content = DOC35_PATH.read_text(encoding="utf-8")
    backup.write_text(content, encoding="utf-8")
    print(f"Backup creado: {backup}")

    # Regex para encontrar líneas de la tabla de inventario
    # Formato: | `<ruta>` | `<propósito>` | `<estado>` | `<hash>` |
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

    # Construir nuevo contenido
    new_content = content

    for match in matches:
        filepath_str = match.group(1)
        old_hash = match.group(2)
        checked += 1

        # Resolver ruta absoluta
        filepath = ROOT / filepath_str
        new_hash = compute_sha256(filepath)

        if new_hash is None:
            print(f"  ⚠️  NO ENCONTRADO: {filepath_str}")
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