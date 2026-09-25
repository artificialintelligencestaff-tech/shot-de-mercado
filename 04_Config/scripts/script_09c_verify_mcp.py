#!/usr/bin/env python3
"""
script_09c_verify_mcp.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Verificacion rigurosa de endpoints MCP.
    Captura la respuesta HTTP cruda SIN parsear ni procesar.
    Compara con la documentacion oficial.
"""

import json
import requests
import socket
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
VERIFY_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "onchain" / "verificacion"
VERIFY_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30

# Endpoints a verificar (solo tools/list, sin procesar)
ENDPOINTS = {
    "swiss_whale": "https://mcp.swisswhaleintelligence.com/mcp",
    "coinlobster": "https://coinlobster.com/mcp",
    "deepblue_alpha_stats": "https://deepbluealpha.io/api/v1/public/stats",
}


def verify_endpoint(name, url):
    """Verificacion cruda sin parseo."""
    print(f"[YIN] Verificando {name}: {url}")

    result = {
        "url": url,
        "timestamp": datetime.now(timezone.utc).isoformat() + "Z"
    }

    # 1. Resolucion DNS
    try:
        hostname = url.split("//")[1].split("/")[0].split(":")[0]
        ip = socket.gethostbyname(hostname)
        result["dns_ip"] = ip
        print(f"[YIN] DNS: {hostname} -> {ip}")
    except Exception as e:
        result["dns_error"] = str(e)

    # 2. Peticion GET simple
    try:
        r_get = requests.get(url, timeout=TIMEOUT)
        result["get_status"] = r_get.status_code
        result["get_headers"] = dict(r_get.headers)
        result["get_body_first_500"] = r_get.text[:500]
    except Exception as e:
        result["get_error"] = str(e)

    # 3. Peticion POST JSON-RPC tools/list
    try:
        payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}
        headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        r_post = requests.post(url, json=payload, headers=headers, timeout=TIMEOUT)
        result["post_status"] = r_post.status_code
        result["post_headers"] = dict(r_post.headers)
        # Guardar el cuerpo ENTERO sin truncar
        result["post_body_full"] = r_post.text
        result["post_body_length"] = len(r_post.text)
    except Exception as e:
        result["post_error"] = str(e)

    return result


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Verificacion MCP - {ts}")

    consolidated = {
        "timestamp": ts,
        "fase": "verify_mcp_endpoints",
        "endpoints": {}
    }

    for name, url in ENDPOINTS.items():
        consolidated["endpoints"][name] = verify_endpoint(name, url)

    out_path = VERIFY_DIR / f"verify_mcp_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(consolidated, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print("[YIN] Script 09c finalizado.")


if __name__ == "__main__":
    main()