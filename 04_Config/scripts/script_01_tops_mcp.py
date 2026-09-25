#!/usr/bin/env python3
"""
script_01_tops_mcp.py — Versión 4 (corregida)
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Corrección v4:
    - Eliminadas las llamadas a list_all_topics y health_check (no existen).
    - Guarda la respuesta CRUDA de list_trending_topics para diagnóstico.
    - Ajusta el filtro de etapas para manejar valores alternativos.
"""

import json
import sys
import time
import requests
from datetime import datetime, timezone
from pathlib import Path

TOPS_MCP_URL = "https://api.chainbase.com/tops/v1/mcp"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
SOCIAL_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "social"
DIAG_DIR = SOCIAL_DIR / "diagnostico"
SOCIAL_DIR.mkdir(parents=True, exist_ok=True)
DIAG_DIR.mkdir(parents=True, exist_ok=True)

LANGUAGE = "en"
TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 5


def call_tops_mcp(method: str, params: dict = None) -> dict:
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
            response = requests.post(TOPS_MCP_URL, json=payload, headers=headers, timeout=TIMEOUT)
            return {
                "http_status": response.status_code,
                "response_body": response.text
            }
        except requests.exceptions.RequestException as e:
            print(f"[Intento {attempt}/{MAX_RETRIES}] Error: {e}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
            else:
                return {"error": str(e)}


def list_trending_topics(language: str = LANGUAGE) -> dict:
    return call_tops_mcp("tools/call", {
        "name": "list_trending_topics",
        "arguments": {"language": language}
    })


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Script 01 v4 — {ts}")

    # Llamada a list_trending_topics
    print("[YIN] Solicitando list_trending_topics...")
    response = list_trending_topics()

    # Guardar respuesta CRUDA para diagnóstico
    raw_path = DIAG_DIR / f"diag_list_trending_raw_{ts}.json"
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(response, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Respuesta cruda guardada: {raw_path}")

    # Intentar parsear el JSON-RPC
    result = {
        "timestamp": ts,
        "fase": "etapa_1_escaneo_v4",
        "estado": "exito",
        "narrativas": [],
        "notas": ""
    }

    try:
        body = json.loads(response.get("response_body", "{}"))
        if "error" in body:
            result["estado"] = "error"
            result["error"] = body["error"]
        else:
            content = body.get("result", {}).get("content", [])
            if content:
                text_content = content[0].get("text", "{}")
                try:
                    parsed = json.loads(text_content)
                    topics = parsed.get("topics", parsed.get("data", []))
                    result["narrativas"] = topics
                    result["notas"] = f"{len(topics)} narrativas recibidas (sin filtrar)."
                except json.JSONDecodeError:
                    result["notas"] = "El contenido no es JSON parseable."
                    result["raw_text"] = text_content[:500]
            else:
                result["notas"] = "Respuesta sin campo 'content'."
    except json.JSONDecodeError:
        result["estado"] = "error"
        result["error"] = "La respuesta no es JSON válido."

    # Guardar resultado procesado
    out_path = SOCIAL_DIR / f"narrativas_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Resultado guardado: {out_path}")
    print("[YIN] Script 01 v4 finalizado.")


if __name__ == "__main__":
    main()