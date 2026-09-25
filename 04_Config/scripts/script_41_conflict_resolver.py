#!/usr/bin/env python3
"""
script_41_conflict_resolver.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Protocolo de resolucion de conflictos para YIN.
    Detecta, intenta resolver, documenta y reporta.
"""

import json
import socket
import requests
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
LOG_DIR = PROJECT_ROOT / "03_Informes" / "conflictos"
LOG_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 10


def check_dns(host):
    try:
        ip = socket.gethostbyname(host)
        return {"host": host, "dns_ok": True, "ip": ip}
    except Exception as e:
        return {"host": host, "dns_ok": False, "error": str(e)}


def check_http(url):
    try:
        r = requests.get(url, timeout=TIMEOUT)
        return {"url": url, "http_status": r.status_code, "ok": r.status_code < 500}
    except Exception as e:
        return {"url": url, "http_status": None, "ok": False, "error": str(e)[:100]}


def check_package_npm(package):
    try:
        r = requests.get(f"https://registry.npmjs.org/{package.replace('/', '%2F')}", timeout=TIMEOUT)
        return {"package": package, "existe": r.status_code == 200}
    except Exception as e:
        return {"package": package, "existe": False, "error": str(e)[:100]}


def check_package_pypi(package):
    try:
        r = requests.get(f"https://pypi.org/pypi/{package}/json", timeout=TIMEOUT)
        return {"package": package, "existe": r.status_code == 200}
    except Exception as e:
        return {"package": package, "existe": False, "error": str(e)[:100]}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Conflict Resolver - {ts}")

    # Endpoints a verificar
    endpoints = [
        "https://coinlobster.com/mcp",
        "https://mcp.deepwiki.com/mcp",
        "https://api.coingecko.com/api/v3/ping",
        "https://api.dexscreener.com/latest/dex/tokens",
    ]

    # Paquetes a verificar
    packages_npm = ["@three-ws/kol-mcp", "soliris-mcp", "@0xprotovox/deficlaw"]
    packages_pypi = ["rug-munch-mcp", "gloria-mcp", "fastmcp"]

    reporte = {
        "timestamp": ts,
        "endpoints": [],
        "packages_npm": [],
        "packages_pypi": []
    }

    print("[YIN] Verificando endpoints...")
    for url in endpoints:
        host = url.split("//")[1].split("/")[0]
        dns = check_dns(host)
        http = check_http(url) if dns["dns_ok"] else {"ok": False, "error": "DNS failed"}
        reporte["endpoints"].append({"url": url, "dns": dns, "http": http})
        print(f"[YIN]   {host}: DNS {'OK' if dns['dns_ok'] else 'FAIL'} | HTTP {http.get('http_status', 'FAIL')}")

    print("[YIN] Verificando paquetes npm...")
    for pkg in packages_npm:
        r = check_package_npm(pkg)
        reporte["packages_npm"].append(r)
        print(f"[YIN]   {pkg}: {'EXISTE' if r['existe'] else 'NO EXISTE'}")

    print("[YIN] Verificando paquetes PyPI...")
    for pkg in packages_pypi:
        r = check_package_pypi(pkg)
        reporte["packages_pypi"].append(r)
        print(f"[YIN]   {pkg}: {'EXISTE' if r['existe'] else 'NO EXISTE'}")

    # Guardar
    out_path = LOG_DIR / f"conflict_resolution_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(reporte, f, indent=2, ensure_ascii=False)
    print(f"\n[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()