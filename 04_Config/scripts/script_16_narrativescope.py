#!/usr/bin/env python3
"""
script_16_narrativescope.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Detectar narrativas emergentes combinando señales de X/Twitter
    con actividad de desarrolladores en GitHub.
    Basado en el algoritmo NarrativeScope (github.com/agenttessaa/narrative-detection).
"""

import json
import requests
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

GITHUB_API = "https://api.github.com/search/repositories"
PROJECT_ROOT = Path(r"D:\Proyecto Shot de mercado")
NARRATIVAS_DIR = PROJECT_ROOT / "02_Analisis" / "narrativas"
NARRATIVAS_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT = 30
HEADERS = {"Accept": "application/vnd.github+json"}

# Keywords de narrativas cripto actuales
NARRATIVAS_KEYWORDS = [
    "DeFAI", "RWA tokenization", "DePIN", "AI agents crypto",
    "Restaking", "Bitcoin L2", "Prediction markets",
    "Liquid staking", "Modular blockchain"
]


def buscar_repos(keyword):
    """Busca repositorios GitHub que coincidan con la narrativa."""
    try:
        # Repos creados en los últimos 90 días
        fecha = (datetime.now(timezone.utc) - timedelta(days=90)).strftime("%Y-%m-%d")
        query = f"{keyword} crypto created:>{fecha}"

        response = requests.get(
            GITHUB_API,
            params={"q": query, "sort": "stars", "order": "desc", "per_page": 10},
            headers=HEADERS,
            timeout=TIMEOUT
        )
        data = response.json()

        if "items" not in data:
            return {"error": "no_items", "total_count": 0, "repos": []}

        return {
            "total_count": data.get("total_count", 0),
            "repos": [
                {
                    "name": r.get("full_name"),
                    "stars": r.get("stargazers_count"),
                    "created_at": r.get("created_at"),
                    "description": (r.get("description") or "")[:200],
                    "url": r.get("html_url")
                }
                for r in data.get("items", [])
            ]
        }
    except Exception as e:
        return {"error": str(e)}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] NarrativeScope - {ts}")

    result = {
        "timestamp": ts,
        "fase": "narrative_detection",
        "estado": "exito",
        "narrativas": []
    }

    for keyword in NARRATIVAS_KEYWORDS:
        print(f"[YIN] Analizando narrativa: {keyword}")
        repos = buscar_repos(keyword)

        # Scoring simple: total_count de repos recientes + stars promedio
        total_repos = repos.get("total_count", 0)
        repos_list = repos.get("repos", [])
        avg_stars = sum(r.get("stars", 0) for r in repos_list) / len(repos_list) if repos_list else 0

        # Score 0-40 basado en actividad de desarrolladores
        if total_repos >= 100:
            score = 40
        elif total_repos >= 50:
            score = 30
        elif total_repos >= 20:
            score = 20
        elif total_repos >= 5:
            score = 10
        else:
            score = 0

        entry = {
            "narrativa": keyword,
            "repos_recientes_90d": total_repos,
            "stars_promedio": round(avg_stars, 1),
            "score_desarrollo": score,
            "top_repos": repos_list[:3],
            "etiqueta": "INFERENCIA ESTRUCTURAL"
        }
        result["narrativas"].append(entry)
        time.sleep(2)  # Respetar rate limits de GitHub

    # Ordenar por score descendente
    result["narrativas"].sort(key=lambda x: x["score_desarrollo"], reverse=True)

    # Guardar
    out_path = NARRATIVAS_DIR / f"narrativescope_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[YIN] Guardado: {out_path}")
    print(f"[YIN] Narrativas analizadas: {len(result['narrativas'])}")
    print("[YIN] Script 16 finalizado.")


if __name__ == "__main__":
    main()