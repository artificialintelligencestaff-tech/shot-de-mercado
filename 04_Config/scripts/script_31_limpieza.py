#!/usr/bin/env python3
"""
script_31_limpieza.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Borrar scripts y archivos que no funcionaron.
    Aplicar regla: lo que no sirve se borra.
"""

import os
from pathlib import Path
from datetime import datetime, timezone

PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")

# Scripts a borrar (fallidos o redundantes)
SCRIPTS_A_BORRAR = [
    "script_24_elfa_ai.py",           # Endpoint no existe
    "script_25_kol_mcp.py",           # Endpoint local no funciona
    "script_26_free_crypto_news.py",  # Endpoint no existe
    "script_27_rug_munch.py",         # Endpoint 502
    "script_28_gmgn_skills.py",       # Endpoint local no funciona
    "script_29_verify_endpoints_v2.py", # Ya cumplio su funcion
    "script_12_onvexia.py",           # Fallo previo
    "script_13_bykaranteli.py",       # Fallo previo
    "script_14_signalstack.py",       # Fallo previo
    "script_17_fin_data_mcp.py",      # Fallo previo
    "script_17b_fin_data_local.py",   # Fallo previo
    "script_19_honest_risk.py",       # Fallo previo
    "script_19c_zarq.py",             # Fallo previo
]

# Directorios de datos fallidos a borrar
DIRS_A_BORRAR = [
    "01_Datos_Crudos/verificacion_v2",
    "01_Datos_Crudos/social/elfa_ai",
    "01_Datos_Crudos/social/kol_mcp",
    "01_Datos_Crudos/social/free_crypto_news",
    "01_Datos_Crudos/social/rug_munch",
    "01_Datos_Crudos/social/gmgn_skills",
    "01_Datos_Crudos/mercados/signalstack",
    "01_Datos_Crudos/mercados/fin_data",
    "02_Analisis/riesgo/quantoracle",  # Conservar solo si funciona
]


def borrar_archivo(path):
    try:
        if path.exists():
            size = path.stat().st_size
            path.unlink()
            return f"BORRADO: {path.name} ({size} bytes)"
        return f"NO EXISTE: {path.name}"
    except Exception as e:
        return f"ERROR borrando {path.name}: {e}"


def borrar_directorio(path):
    try:
        if path.exists() and path.is_dir():
            import shutil
            shutil.rmtree(path)
            return f"BORRADO: {path.name}/"
        return f"NO EXISTE: {path.name}/"
    except Exception as e:
        return f"ERROR borrando {path.name}/: {e}"


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Limpieza del proyecto - {ts}")
    print(f"[YIN] Regla: lo que no sirve se borra\n")

    # 1. Borrar scripts fallidos
    print("=== SCRIPTS A BORRAR ===")
    scripts_dir = PROJECT_ROOT / "04_Config" / "scripts"
    for script in SCRIPTS_A_BORRAR:
        resultado = borrar_archivo(scripts_dir / script)
        print(f"[YIN] {resultado}")

    # 2. Borrar directorios de datos fallidos
    print("\n=== DIRECTORIOS A BORRAR ===")
    for dir_rel in DIRS_A_BORRAR:
        resultado = borrar_directorio(PROJECT_ROOT / dir_rel)
        print(f"[YIN] {resultado}")

    print("\n[YIN] Limpieza completada.")


if __name__ == "__main__":
    main()