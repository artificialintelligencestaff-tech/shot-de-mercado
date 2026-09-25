#!/usr/bin/env python3
"""
script_23_pipeline_maestro.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Pipeline maestro. Ejecuta todas las fuentes en secuencia y genera
    las hojas de salida. Un solo comando ejecuta todo el ciclo.
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
SCRIPTS_DIR = PROJECT_ROOT / "04_Config" / "scripts"
LOG_DIR = PROJECT_ROOT / "03_Informes" / "pipeline_logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Scripts a ejecutar en orden
PIPELINE = [
    # Capa 1-2: Mercado
    ("script_03_coingecko.py", "CoinGecko - precios, trending, top 20"),
    ("script_15b_coinfuty_corregido.py", "Coinfuty - open interest, funding, liquidaciones"),
    # Capa 3: On-chain y ballenas
    ("script_09g_coinlobster_auth.py", "CoinLobster - whale_radar, whale_trades"),
    ("script_09e_deepblue.py", "Deep Blue Alpha - whale_index, top_tokens"),
    # Capa 4-5: Social y narrativas
    ("script_11_apewisdom.py", "ApeWisdom - Reddit trending"),
    ("script_16_narrativescope.py", "NarrativeScope - narrativas GitHub"),
    ("script_04_alpha_mcp.py", "Alpha MCP - 41 topics macro"),
    # Capa 7: Scoring
    ("script_21d_hoja_auditada.py", "Generacion de hojas auditadas"),
    # Capa 8: Comunicacion
    ("script_20b_telegram_fixed.py", "Envio de alerta Telegram"),
    ("script_35b_mcp_analytics.py", "Deficlaw trending + Soliris pairs"),
    ("script_37d_alert_multipart.py", "Alerta Telegram multipart"),
    ("script_38b_tracking_degradacion.py", "Tracking + alerta de degradacion"),
]


def ejecutar_script(script_name, descripcion):
    """Ejecuta un script y captura resultado."""
    script_path = SCRIPTS_DIR / script_name

    if not script_path.exists():
        return {
            "script": script_name,
            "descripcion": descripcion,
            "estado": "SKIP",
            "razon": "No existe"
        }

    print(f"[PIPELINE] Ejecutando: {script_name}")
    print(f"[PIPELINE]   {descripcion}")

    inicio = time.time()
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=120
        )
        duracion = round(time.time() - inicio, 2)
        estado = "OK" if result.returncode == 0 else "ERROR"

        return {
            "script": script_name,
            "descripcion": descripcion,
            "estado": estado,
            "returncode": result.returncode,
            "duracion_seg": duracion,
            "stdout_tail": result.stdout[-300:] if result.stdout else "",
            "stderr_tail": result.stderr[-300:] if result.stderr else ""
        }
    except subprocess.TimeoutExpired:
        return {
            "script": script_name,
            "descripcion": descripcion,
            "estado": "TIMEOUT",
            "razon": "Excedio 120 segundos"
        }
    except Exception as e:
        return {
            "script": script_name,
            "descripcion": descripcion,
            "estado": "ERROR",
            "razon": str(e)
        }


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"\n{'='*60}")
    print(f"[PIPELINE] Ciclo maestro iniciado: {ts}")
    print(f"{'='*60}\n")

    resultados = []
    inicio_ciclo = time.time()

    for script_name, descripcion in PIPELINE:
        resultado = ejecutar_script(script_name, descripcion)
        resultados.append(resultado)

        # Mostrar resumen corto
        estado = resultado.get("estado")
        icono = "[OK]" if estado == "OK" else "[ERR]" if estado == "ERROR" else "[SKIP]"
        print(f"[PIPELINE] {icono} {script_name} - {estado}\n")

        # Pequeña pausa entre scripts para respetar rate limits
        time.sleep(2)

    duracion_total = round(time.time() - inicio_ciclo, 2)

    # Consolidado
    exitosos = sum(1 for r in resultados if r.get("estado") == "OK")
    errores = sum(1 for r in resultados if r.get("estado") == "ERROR")
    skips = sum(1 for r in resultados if r.get("estado") == "SKIP")

    resumen = {
        "timestamp": ts,
        "fase": "pipeline_maestro",
        "duracion_total_seg": duracion_total,
        "total_scripts": len(PIPELINE),
        "exitosos": exitosos,
        "errores": errores,
        "skips": skips,
        "resultados": resultados
    }

    # Guardar log
    log_path = LOG_DIR / f"pipeline_{ts}.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(resumen, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"[PIPELINE] CICLO COMPLETADO")
    print(f"[PIPELINE] Duraccion: {duracion_total} segundos")
    print(f"[PIPELINE] Exitosos: {exitosos}/{len(PIPELINE)}")
    print(f"[PIPELINE] Errores: {errores}")
    print(f"[PIPELINE] Skips: {skips}")
    print(f"[PIPELINE] Log: {log_path}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()