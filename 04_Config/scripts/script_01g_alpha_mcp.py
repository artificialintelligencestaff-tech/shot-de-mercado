#!/usr/bin/env python3
"""
script_01g_alpha_mcp.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Propósito:
    Conectar con Alpha MCP (Mossland) como alternativa a Onvexia.
    Endpoint: https://alpha.moss.land/api/mcp
    Sin API key. Fair use ~1 req/s.
    Formato: Streamable HTTP (JSON-RPC 2.0).
"""

import json
import time
import requests
from datetime import datetime, timezone
from pathlib import Path

ALPHA_MCP_URL = "https://alpha.moss.land/api/mcp"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
SOCIAL_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "social"
DIAG_DIR = SOCIAL_DIR / "diagnostico"
SOCIAL_DIR.mkdir(parents=True, exist_ok=True)
DIAG_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 5


def parse_sse_response(raw_text: str) -> dict:
    """Parsea respuesta SSE o JSON plano."""
    try:
        for line in raw_text.split("\n"):
            line = line.strip()
            if line.startswith("data: "):
                return json.loads(line[len("data: "):])
        return json.loads(raw_text)
    except json.JSONDecodeError as e:
        return {"error": {"message": f"JSONDecodeError: {e}", "raw": raw_text[:500]}}


def call_alpha(method: str, params: dict = None) -> dict:
    """Llama a Alpha MCP vía JSON-RPC POST."""
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
            response = requests.post(ALPHA_MCP_URL, json=payload, headers=headers, timeout=TIMEOUT)
            parsed = parse_sse_response(response.text)
            return {
                "http_status": response.status_code,
                "parsed": parsed,
                "raw_preview": response.text[:1000]
            }
        except requests.exceptions.RequestException as e:
            print(f"[Intento {attempt}/{MAX_RETRIES}] Error de red: {e}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
            else:
                return {"error": str(e)}
        except Exception as e:
            print(f"[Intento {attempt}/{MAX_RETRIES}] Error inesperado: {e}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
            else:
                return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Alpha MCP Extractor — {ts}")

    # 1. tools/list para verificar herramientas disponibles
    print("[YIN] Solicitando tools/list...")
    tools = call_alpha("tools/list", {})
    tools_path = DIAG_DIR / f"alpha_tools_{ts}.json"
    with open(tools_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {tools_path}")

    # 2. list_topics (equivalente a narrativas)
    print("[YIN] Solicitando list_topics...")
    topics = call_alpha("tools/call", {
        "name": "list_topics",
        "arguments": {}
    })
    topics_path = SOCIAL_DIR / f"alpha_topics_{ts}.json"
    with open(topics_path, "w", encoding="utf-8") as f:
        json.dump(topics, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {topics_path}")

    print("[YIN] Script 01g finalizado.")


if __name__ == "__main__":
    main()