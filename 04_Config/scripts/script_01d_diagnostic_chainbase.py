#!/usr/bin/env python3
"""

Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Propósito:
    Verificar funcionalidad del MCP Chainbase Tops.
    Llamar a list_all_topics y health_check para confirmar que el servidor está operativo.
    Guardar respuestas crudas en 01_Datos_Crudos/social/diagnostico/.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

TOPS_MCP_URL = "https://api.chainbase.com/tops/v1/mcp"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
DIAG_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "social" / "diagnostico"
DIAG_DIR.mkdir(parents=True, exist_ok=True)

LANGUAGE = "en"
TIMEOUT = 30


def call_raw(method: str, params: dict = None) -> dict:
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params or {}
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    response = requests.post(TOPS_MCP_URL, json=payload, headers=headers, timeout=TIMEOUT)
    return {
        "http_status": response.status_code,
        "response_body": response.text
    }


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Diagnostic Chainbase — {ts}")

    # 1. list_all_topics
    print("[YIN] Llamando list_all_topics...")
    diag_all = call_raw("tools/call", {
        "name": "list_all_topics",
        "arguments": {}
    })
    all_path = DIAG_DIR / f"diag_list_all_topics_{ts}.json"
    with open(all_path, "w", encoding="utf-8") as f:
        json.dump(diag_all, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {all_path}")

    # 2. health_check
    print("[YIN] Llamando health_check...")
    diag_health = call_raw("tools/call", {
        "name": "health_check",
        "arguments": {}
    })
    health_path = DIAG_DIR / f"diag_health_check_{ts}.json"
    with open(health_path, "w", encoding="utf-8") as f:
        json.dump(diag_health, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {health_path}")

    print("[YIN] Diagnóstico Chainbase finalizado.")


if __name__ == "__main__":
    main()