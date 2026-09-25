#!/usr/bin/env python3
"""
script_33_verificar_registries.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Verificar si un paquete existe en npm o PyPI via HTTP.
    NO requiere npm/pip instalados. Solo requests HTTP.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

NPM_REGISTRY = "https://registry.npmjs.org"
PYPI_REGISTRY = "https://pypi.org/pypi"

PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
VERIFY_DIR = PROJECT_ROOT / "02_Analisis" / "verificacion_paquetes"
VERIFY_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 15

# Paquetes a verificar
PAQUETES_NPM = [
    "@three-ws/kol-mcp",
    "@0xprotovox/deficlaw",
    "soliris-mcp",
    "@modelcontextprotocol/server-filesystem",
    "crypto-data-aggregator",
    "mcp-hive",
]

PAQUETES_PIP = [
    "gloria-mcp",
    "rug-munch-mcp",
    "mcp",
    "crypto-data-aggregator",
    "praw",
    "ccxt",
]


def check_npm(package):
    try:
        url = f"{NPM_REGISTRY}/{package.replace('/', '%2F')}"
        r = requests.get(url, timeout=TIMEOUT)
        if r.status_code == 200:
            data = r.json()
            return {
                "paquete": package,
                "existe": True,
                "version": data.get("dist-tags", {}).get("latest", "unknown"),
                "descripcion": data.get("description", "")[:100]
            }
        return {"paquete": package, "existe": False, "http_status": r.status_code}
    except Exception as e:
        return {"paquete": package, "existe": False, "error": str(e)[:100]}


def check_pypi(package):
    try:
        url = f"{PYPI_REGISTRY}/{package}/json"
        r = requests.get(url, timeout=TIMEOUT)
        if r.status_code == 200:
            data = r.json()
            return {
                "paquete": package,
                "existe": True,
                "version": data.get("info", {}).get("version", "unknown"),
                "descripcion": data.get("info", {}).get("summary", "")[:100]
            }
        return {"paquete": package, "existe": False, "http_status": r.status_code}
    except Exception as e:
        return {"paquete": package, "existe": False, "error": str(e)[:100]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Verificacion via HTTP registries - {ts}\n")

    resultados = {"npm": [], "pip": []}

    print("=== NPM REGISTRY ===")
    for p in PAQUETES_NPM:
        r = check_npm(p)
        estado = "EXISTE" if r.get("existe") else "NO EXISTE"
        extra = r.get("version", r.get("http_status", r.get("error", "")))
        print(f"[YIN] {estado}: {p} | {extra}")
        resultados["npm"].append(r)

    print("\n=== PYPI REGISTRY ===")
    for p in PAQUETES_PIP:
        r = check_pypi(p)
        estado = "EXISTE" if r.get("existe") else "NO EXISTE"
        extra = r.get("version", r.get("http_status", r.get("error", "")))
        print(f"[YIN] {estado}: {p} | {extra}")
        resultados["pip"].append(r)

    # Guardar
    out_path = VERIFY_DIR / f"registries_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"timestamp": ts, "resultados": resultados}, f, indent=2, ensure_ascii=False)
    print(f"\n[YIN] Guardado: {out_path}")

    # Resumen
    total_ok = sum(1 for r in resultados["npm"] + resultados["pip"] if r.get("existe"))
    total = len(PAQUETES_NPM) + len(PAQUETES_PIP)
    print(f"[YIN] Paquetes existentes: {total_ok}/{total}")


if __name__ == "__main__":
    main()