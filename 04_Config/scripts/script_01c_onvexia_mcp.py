#!/usr/bin/env python3
"""
script_01e_onvexia_mcp.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Propósito:
    Conectar con Onvexia MCP (remoto, sin API key).
    1. Listar herramientas disponibles.
    2. Guardar la respuesta para diagnóstico de nombres.
    3. Intentar obtener narrativas y sentimiento.
"""

import json
import requests
from datetime import datetime, timezone
from pathlib import Path

ONVEXIA_URL = "https://onvexia.com/mcp"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
SOCIAL_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "social"
DIAG_DIR = SOCIAL_DIR / "diagnostico"
SOCIAL_DIR.mkdir(parents=True, exist_ok=True)
DIAG_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 5


def call_onvexia(method: str, params: dict = None) -> dict:
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
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.post(ONVEXIA_URL, json=payload, headers=headers, timeout=TIMEOUT)
            return {
                "http_status": response.status_code,
                "response_body": response.text
            }
        except requests.exceptions.RequestException as e:
            print(f"[Intento {attempt}/{MAX_RETRIES}] Error: {e}")
            if attempt < MAX_RETRIES:
                import time
                time.sleep(RETRY_DELAY)
            else:
                return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Onvexia MCP Diagnostic — {ts}")

    # 1. tools/list
    print("[YIN] Solicitando tools/list...")
    tools_response = call_onvexia("tools/list", {})
    tools_path = DIAG_DIR / f"onvexia_tools_{ts}.json"
    with open(tools_path, "w", encoding="utf-8") as f:
        json.dump(tools_response, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {tools_path}")

    # 2. Guardar también en formato compatible con parser
    result = {
        "timestamp": ts,
        "fase": "onvexia_diagnostico",
        "tools_response_preview": tools_response.get("response_body", "")[:2000],
        "tools_path": str(tools_path)
    }
    result_path = SOCIAL_DIR / f"onvexia_diagnostic_{ts}.json"
    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Resultado guardado: {result_path}")

    print("[YIN] Script 01e finalizado.")


if __name__ == "__main__":
    main()