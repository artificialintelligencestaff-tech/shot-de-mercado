#!/usr/bin/env python3
"""
script_09b_whale_alternatives.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Probar alternativas gratuitas a Whale Alert y Deep Blue Alpha.
    1. Swiss Whale Intelligence MCP (45 tools, OAuth anonimo)
    2. CoinLobster MCP (17 tools, hosted)
    3. Whalert MCP (ETH + BSC)
    Guarda la respuesta de tools/list de cada uno para diagnostico.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
ONCHAIN_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "onchain"
DIAG_DIR = ONCHAIN_DIR / "diagnostico"
ONCHAIN_DIR.mkdir(parents=True, exist_ok=True)
DIAG_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30

# Endpoints de las alternativas
ENDPOINTS = {
    "swiss_whale": "https://mcp.swisswhaleintelligence.com/mcp",
    "coinlobster": "https://coinlobster.com/mcp"
}


def parse_sse(raw_text):
    try:
        for line in raw_text.split("\n"):
            line = line.strip()
            if line.startswith("data: "):
                return json.loads(line[6:])
        return json.loads(raw_text)
    except json.JSONDecodeError:
        return {"raw": raw_text[:500]}


def call_mcp(url, method, params=None):
    payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params or {}}
    headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=TIMEOUT)
        return {
            "http_status": response.status_code,
            "parsed": parse_sse(response.text),
            "raw_preview": response.text[:1000]
        }
    except Exception as e:
        return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Whale Alternatives Diagnostic - {ts}")

    result = {
        "timestamp": ts,
        "fase": "whale_alternatives_diagnostic",
        "estado": "exito",
        "endpoints": {}
    }

    for name, url in ENDPOINTS.items():
        print(f"[YIN] Probando {name}...")
        tools = call_mcp(url, "tools/list", {})
        result["endpoints"][name] = tools

        # Guardar individualmente
        out_path = DIAG_DIR / f"{name}_tools_{ts}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(tools, f, indent=2, ensure_ascii=False)
        print(f"[YIN] Guardado: {out_path}")

    # Guardar consolidado
    out_path = DIAG_DIR / f"whale_alternatives_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Consolidado: {out_path}")
    print("[YIN] Script 09b finalizado.")


if __name__ == "__main__":
    main()