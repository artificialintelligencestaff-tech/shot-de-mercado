#!/usr/bin/env python3
"""
script_04_alpha_mcp.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Conectar con Alpha MCP (Mossland) y extraer narrativas macro.
    Traducir los labels coreanos a espanol usando LibreTranslate (gratuito).
    Alpha MCP: 12 herramientas, sin API key.
"""

import json
import requests
import time
from datetime import datetime, timezone
from pathlib import Path

ALPHA_MCP_URL = "https://alpha.moss.land/api/mcp"
LIBRETRANSLATE_URL = "https://libretranslate.com/translate"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
SOCIAL_DIR = PROJECT_ROOT / "01_Datos_Crudos" / "social"
SOCIAL_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
MAX_RETRIES = 3


def parse_sse(raw_text):
    try:
        for line in raw_text.split("\n"):
            line = line.strip()
            if line.startswith("data: "):
                return json.loads(line[6:])
        return json.loads(raw_text)
    except json.JSONDecodeError as e:
        return {"error": {"message": f"JSONDecodeError: {e}"}}


def call_alpha(method, params=None):
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
            return {
                "http_status": response.status_code,
                "parsed": parse_sse(response.text),
                "raw_preview": response.text[:500]
            }
        except Exception as e:
            if attempt < MAX_RETRIES:
                time.sleep(5)
            else:
                return {"error": str(e)}


def translate_to_spanish(text):
    """Traduce texto coreano o ingles a espanol via LibreTranslate."""
    if not text:
        return text
    try:
        response = requests.post(
            LIBRETRANSLATE_URL,
            json={"q": text, "source": "ko", "target": "es", "format": "text"},
            timeout=15
        )
        if response.status_code == 200:
            return response.json().get("translatedText", text)
    except Exception:
        pass
    return text


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Alpha MCP - {ts}")

    result = {
        "timestamp": ts,
        "fase": "alpha_mcp",
        "estado": "exito",
        "topics": [],
        "brief": None,
        "pulses": None
    }

    # 1. list_topics
    print("[YIN] Solicitando list_topics...")
    topics_response = call_alpha("tools/call", {
        "name": "list_topics",
        "arguments": {}
    })

    parsed = topics_response.get("parsed", {})
    content = parsed.get("result", {}).get("content", [])
    if content and len(content) > 0:
        text_content = content[0].get("text", "{}")
        try:
            topics_data = json.loads(text_content)
            raw_topics = topics_data.get("topics", [])

            # Traducir cada label
            print(f"[YIN] Traduciendo {len(raw_topics)} topics al espanol...")
            for topic in raw_topics:
                label_kr = topic.get("label", "")
                label_es = translate_to_spanish(label_kr)
                result["topics"].append({
                    "id": topic.get("id"),
                    "label_kr": label_kr,
                    "label_es": label_es,
                    "videoCount": topic.get("videoCount"),
                    "url": topic.get("url")
                })
                time.sleep(0.5)
        except json.JSONDecodeError:
            result["estado"] = "parcial"
            result["raw_topics"] = text_content[:500]

    # 2. get_today_brief
    print("[YIN] Solicitando today_brief...")
    brief_response = call_alpha("tools/call", {
        "name": "get_today_brief",
        "arguments": {}
    })
    result["brief"] = brief_response.get("parsed", {})

    # 3. get_active_pulses
    print("[YIN] Solicitando active_pulses...")
    pulses_response = call_alpha("tools/call", {
        "name": "get_active_pulses",
        "arguments": {}
    })
    result["pulses"] = pulses_response.get("parsed", {})

    # Guardar
    out_path = SOCIAL_DIR / f"alpha_mcp_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print(f"[YIN] Topics traducidos: {len(result['topics'])}")
    print("[YIN] Script 04 finalizado.")


if __name__ == "__main__":
    main()