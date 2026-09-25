#!/usr/bin/env python3
"""
script_39c_extractor_robusto.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Extractor robusto multi-fuente. NO filtra. Muestra TODOS los activos.
    Lee multiples archivos mcp_analytics. Extrae direcciones con
    parser flexible.
"""

import json
import glob
import re
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
DATA_DIR = PROJECT_ROOT / "01_Datos_Crudos"
PANORAMA_DIR = PROJECT_ROOT / "02_Analisis" / "panorama"
PANORAMA_DIR.mkdir(parents=True, exist_ok=True)


def extraer_addresses_flexible(data):
    """Extrae direcciones con matching flexible."""
    direcciones = []

    def recorrer(obj, fuente=""):
        if isinstance(obj, dict):
            # Buscar campos de direccion con nombres alternativos
            addr = None
            for key in ["address", "tokenAddress", "mint", "contract", "mintAddress", "token_address", "pairAddress"]:
                if key in obj and isinstance(obj[key], str) and len(obj[key]) > 30:
                    addr = obj[key]
                    break

            symbol = None
            for key in ["symbol", "name", "token", "ticker"]:
                if key in obj and isinstance(obj[key], str):
                    symbol = obj[key]
                    break

            if addr:
                direcciones.append({
                    "address": addr,
                    "symbol": symbol or "?",
                    "fuente": fuente,
                    "datos": {k: v for k, v in obj.items() if k not in ["address", "tokenAddress"]}
                })

            for key, value in obj.items():
                recorrer(value, fuente or key)

        elif isinstance(obj, list):
            for item in obj:
                recorrer(item, fuente)

        elif isinstance(obj, str):
            # Si es string, intentar parsear como JSON anidado
            if obj.strip().startswith("[") or obj.strip().startswith("{"):
                try:
                    parsed = json.loads(obj)
                    recorrer(parsed, fuente)
                except json.JSONDecodeError:
                    pass

    recorrer(data)
    return direcciones


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Extractor robusto - {ts}")

    todos_candidatos = []
    archivos_procesados = 0

    # Buscar en TODOS los directorios de datos
    patrones = [
        "01_Datos_Crudos/mcp_analytics/*.json",
        "01_Datos_Crudos/mcp_analytics/coingecko/*.json",
        "01_Datos_Crudos/social/apewisdom/*.json",
        "01_Datos_Crudos/onchain/*.json",
    ]

    for patron in patrones:
        archivos = sorted(glob.glob(str(PROJECT_ROOT / patron)), reverse=True)
        for archivo in archivos[:3]:  # Ultimos 3 por fuente
            try:
                with open(archivo, "r", encoding="utf-8") as f:
                    data = json.load(f)
                candidatos = extraer_addresses_flexible(data)
                for c in candidatos:
                    c["archivo_origen"] = Path(archivo).name
                todos_candidatos.extend(candidatos)
                archivos_procesados += 1
                print(f"[YIN] {Path(archivo).name}: {len(candidatos)} direcciones")
            except Exception as e:
                print(f"[YIN] ERROR {archivo}: {e}")

    # Deduplicar por address
    unicos = {}
    for c in todos_candidatos:
        if c["address"] not in unicos:
            unicos[c["address"]] = c
        else:
            # Combinar fuentes
            unicos[c["address"]]["fuente"] += f" + {c['fuente']}"

    resultado = {
        "timestamp": ts,
        "fase": "extractor_robusto",
        "archivos_procesados": archivos_procesados,
        "total_encontrados": len(todos_candidatos),
        "total_unicos": len(unicos),
        "candidatos": list(unicos.values())
    }

    out_path = PANORAMA_DIR / f"candidatos_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[YIN] Guardado: {out_path}")
    print(f"[YIN] Total unicos: {len(unicos)}")

    # Mostrar resumen por fuente
    print(f"\n[YIN] === DIRECCIONES UNICAS ===")
    for i, (addr, c) in enumerate(list(unicos.items())[:30], 1):
        print(f"[YIN] {i}. {c['symbol']:15} | {addr[:20]}... | {c['fuente'][:40]}")


if __name__ == "__main__":
    main()