#!/usr/bin/env python3
"""
script_69_questions_generator.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    YIN genera preguntas para YANG basadas en sus observaciones.
    Las preguntas se envian a YANG para ampliar conocimiento.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
QUESTIONS_DIR = PROJECT_ROOT / "03_Informes" / "questions"
QUESTIONS_DIR.mkdir(parents=True, exist_ok=True)


# Plantillas de preguntas por categoria
PLANTILLAS = {
    "contradiccion": [
        "¿Qué hago cuando {fuente1} dice X y {fuente2} dice Y?",
        "¿Cómo valido {dato} si solo tengo una fuente?",
        "¿Qué peso le doy a {metrica} en el scoring final?",
    ],
    "falta_dato": [
        "¿Cómo obtengo {dato} para {cadena}?",
        "¿Existe una fuente gratuita para {metrica}?",
        "¿Puedo calcular {metrica} con los datos actuales?",
    ],
    "instalacion": [
        "¿Cómo instalo {herramienta} en Windows?",
        "¿Qué API key necesito para {servicio}?",
        "¿{paquete} sigue activo en GitHub?",
    ],
    "validacion": [
        "¿Cómo validó si {score} es confiable?",
        "¿Cuántos casos necesito para calibrar {formula}?",
        "¿Cómo mido el exito de una prediccion?",
    ],
    "ampliacion": [
        "¿Existen fuentes para {categoria} en {idioma}?",
        "¿Puedo integrar {concepto} al pipeline?",
        "¿Qué MCP cubre {gap}?",
    ]
}


def generar_preguntas(contexto):
    """Genera preguntas basadas en el contexto observado."""
    preguntas = []

    for categoria, plantillas in PLANTILLAS.items():
        for plantilla in plantillas[:2]:  # 2 por categoria
            preguntas.append({
                "categoria": categoria,
                "pregunta": plantilla,
                "contexto": contexto
            })

    return preguntas


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] Questions Generator - {ts}")

    # Contexto de ejemplo (YIN lo llenara con observaciones reales)
    contexto = {
        "fuente1": "Early Radar (OP=ALERT 67)",
        "fuente2": "CryptoGuard (OP=TIMEOUT)",
        "metrica": "risk_score",
        "cadena": "Ethereum",
        "herramienta": "airdrop-intel-mcp",
        "servicio": "DropsTab",
        "score": "Early Radar",
        "formula": "scoring_v4",
        "categoria": "KOL tracking",
        "idioma": "japones",
        "concepto": "surge detection",
        "gap": "TGEs fuera de Solana",
        "dato": "top holders distribution",
        "paquete": "@three-ws/kol-mcp"
    }

    preguntas = generar_preguntas(contexto)

    out = {
        "timestamp": ts,
        "fase": "questions_generated",
        "total": len(preguntas),
        "preguntas": preguntas
    }

    out_path = QUESTIONS_DIR / f"questions_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print(f"[YIN] Total preguntas: {len(preguntas)}")

    for p in preguntas[:5]:
        print(f"[YIN]   [{p['categoria']}] {p['pregunta']}")


if __name__ == "__main__":
    main()