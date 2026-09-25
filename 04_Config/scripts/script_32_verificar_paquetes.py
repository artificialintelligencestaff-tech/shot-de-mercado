#!/usr/bin/env python3
"""
script_32_verificar_paquetes.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Verificar existencia de paquetes npm/pip SIN instalarlos.
    Evita cuelgues de npx con paquetes inexistentes.
"""

import subprocess
import json
from datetime import datetime, timezone

# Paquetes a verificar
PAQUETES_NPM = [
    "@three-ws/kol-mcp",
    "@0xprotovox/deficlaw",
    "soliris-mcp",
    "@modelcontextprotocol/server-filesystem",  # Sanity check
]

PAQUETES_PIP = [
    "gloria-mcp",
    "rug-munch-mcp",
    "mcp",  # Sanity check
]


def verificar_npm(paquete):
    try:
        result = subprocess.run(
            ["npm", "view", paquete, "version"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            return {"paquete": paquete, "existe": True, "version": result.stdout.strip()}
        return {"paquete": paquete, "existe": False, "error": result.stderr.strip()[:200]}
    except subprocess.TimeoutExpired:
        return {"paquete": paquete, "existe": False, "error": "TIMEOUT"}
    except Exception as e:
        return {"paquete": paquete, "existe": False, "error": str(e)}


def verificar_pip(paquete):
    try:
        result = subprocess.run(
            ["pip", "index", "versions", paquete],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0 and "Available versions" in result.stdout:
            return {"paquete": paquete, "existe": True, "info": result.stdout.strip()[:200]}
        return {"paquete": paquete, "existe": False, "error": result.stderr.strip()[:200]}
    except subprocess.TimeoutExpired:
        return {"paquete": paquete, "existe": False, "error": "TIMEOUT"}
    except Exception as e:
        return {"paquete": paquete, "existe": False, "error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Verificacion de paquetes - {ts}\n")

    resultados = {"npm": [], "pip": []}

    print("=== NPM ===")
    for p in PAQUETES_NPM:
        r = verificar_npm(p)
        estado = "EXISTE" if r.get("existe") else "NO EXISTE"
        print(f"[YIN] {estado}: {p} {r.get('version', r.get('error', ''))}")
        resultados["npm"].append(r)

    print("\n=== PIP ===")
    for p in PAQUETES_PIP:
        r = verificar_pip(p)
        estado = "EXISTE" if r.get("existe") else "NO EXISTE"
        print(f"[YIN] {estado}: {p}")
        resultados["pip"].append(r)

    # Guardar
    from pathlib import Path
    out_dir = Path(r"D:\Proyecto Shot de mercado\02_Analisis\verificacion_paquetes")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"paquetes_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"timestamp": ts, "resultados": resultados}, f, indent=2, ensure_ascii=False)
    print(f"\n[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()