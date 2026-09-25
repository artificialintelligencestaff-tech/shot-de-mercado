#!/usr/bin/env python3
"""
script_01b_diagnostic_tops.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Propósito:
    Guardar la respuesta CRUDA del Tops MCP para inspeccionar su estructura.
    No filtra. No procesa. Solo guarda lo que el API devuelve.
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
        "response_headers": dict(response.headers),
        "response_body": response.text
    }


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Diagnostic Tops MCP — {ts}")

    # 1. Llamada a list_trending_topics
    print("[YIN] Llamando list_trending_topics...")
    diag_topics = call_raw("tools/call", {
        "name": "list_trending_topics",
        "arguments": {"language": LANGUAGE}
    })

    topics_path = DIAG_DIR / f"diag_list_trending_topics_{ts}.json"
    with open(topics_path, "w", encoding="utf-8") as f:
        json.dump(diag_topics, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {topics_path}")

    # 2. Llamada a tools/list para saber qué tools expone el MCP
    print("[YIN] Llamando tools/list...")
    diag_tools = call_raw("tools/list", {})
    tools_path = DIAG_DIR / f"diag_tools_list_{ts}.json"
    with open(tools_path, "w", encoding="utf-8") as f:
        json.dump(diag_tools, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {tools_path}")

    print("[YIN] Diagnóstico finalizado.")


if __name__ == "__main__":
    main()