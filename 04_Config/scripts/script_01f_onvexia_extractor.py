#!/usr/bin/env python3
"""
script_01f_onvexia_extractor.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Propósito:
    Conectar con Onvexia MCP y obtener narrativas vía get_topic_rank.
    Implementa parser SSE para manejar el formato de respuesta.
    Guarda narrativas y datos relacionados en formato JSON.
"""

import json
import sys
import time
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


def parse_sse_response(raw_text: str) -> dict:
    """
    Parsea una respuesta SSE y extrae el JSON-RPC subyacente.
    Formato: event: message\r\ndata: {...}
    """
    try:
        # Buscar todas las líneas que empiezan con "data: "
        for line in raw_text.split("\n"):
            line = line.strip()
            if line.startswith("data: "):
                json_str = line[len("data: "):]
                return json.loads(json_str)
        # Si no hay prefijo "data: ", intentar parsear directamente
        return json.loads(raw_text)
    except json.JSONDecodeError as e:
        return {"error": {"message": f"JSONDecodeError: {e}", "raw": raw_text[:500]}}


def call_onvexia(method: str, params: dict = None) -> dict:
    """
    Llama a Onvexia MCP vía JSON-RPC POST.
    Parsea la respuesta SSE para extraer el JSON.
    """
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
    print(f"[YIN] Onvexia Extractor — {ts}")

    # 1. Obtener narrativas rankeadas (get_topic_rank)
    print("[YIN] Solicitando narrativas (get_topic_rank)...")
    narratives = call_onvexia("tools/call", {
        "name": "get_social_dominance",
        "arguments": {"hours": 168}
    })

    # 2. Guardar respuesta cruda
    raw_narratives_path = DIAG_DIR / f"onvexia_topic_rank_raw_{ts}.json"
    with open(raw_narratives_path, "w", encoding="utf-8") as f:
        json.dump(narratives, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Respuesta cruda guardada: {raw_narratives_path}")

    # 3. Procesar narrativas
    result = {
        "timestamp": ts,
        "fase": "etapa_1_escaneo_onvexia",
        "estado": "exito",
        "narrativas": [],
        "notas": ""
    }

    parsed = narratives.get("parsed", {})
    if "error" in parsed:
        result["estado"] = "error"
        result["error"] = parsed["error"]
    else:
        # Extraer narrativas de la estructura de respuesta
        content = parsed.get("result", {}).get("content", [])
        if content and len(content) > 0:
            text_content = content[0].get("text", "{}")
            try:
                parsed_narratives = json.loads(text_content)
                if isinstance(parsed_narratives, list):
                    result["narrativas"] = parsed_narratives
                    result["notas"] = f"{len(parsed_narratives)} narrativas obtenidas de Onvexia."
                elif isinstance(parsed_narratives, dict):
                    topics = parsed_narratives.get("topics", parsed_narratives.get("data", []))
                    result["narrativas"] = topics
                    result["notas"] = f"{len(topics)} narrativas obtenidas de Onvexia."
                else:
                    result["notas"] = "Estructura de narrativas no reconocida."
                    result["raw_content_preview"] = text_content[:500]
            except json.JSONDecodeError:
                result["notas"] = "El contenido no es JSON parseable."
                result["raw_content_preview"] = text_content[:500]
        else:
            result["notas"] = "Respuesta sin campo 'content'."

    # 4. Guardar resultado procesado
    out_path = SOCIAL_DIR / f"onvexia_narrativas_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Resultado procesado guardado: {out_path}")

    # 5. Reportar
    print(f"[YIN] Script 01f finalizado. Narrativas: {len(result['narrativas'])}")


if __name__ == "__main__":
    main()