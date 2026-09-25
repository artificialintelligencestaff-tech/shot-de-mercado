#!/usr/bin/env python3
"""
script_68_react_framework.py
Proyecto: Shot de Mercado
Autor: YANG (Analista Cuantitativo)
Ejecuta: YIN (Agente de Campo)

Proposito:
    Framework ReAct para YIN.
    Reasoning -> Acting -> Observation -> Repeat.
    Permite a YIN razonar antes de actuar y aprender de cada paso.
"""

import json
import asyncio
from datetime import datetime, timezone
from pathlib import Path
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

PROJECT_ROOT = Path(r"D:\Proyecto Shot de Mercado")
REACT_DIR = PROJECT_ROOT / "03_Informes" / "react_logs"
REACT_DIR.mkdir(parents=True, exist_ok=True)


class ReActAgent:
    """Agente que razona antes de actuar."""

    def __init__(self, goal):
        self.goal = goal
        self.history = []
        self.max_steps = 10

    def think(self, observation):
        """Genera razonamiento sobre el estado actual."""
        step = len(self.history) + 1
        razonamiento = {
            "step": step,
            "goal": self.goal,
            "observation": observation,
            "thought": None,
            "action": None
        }

        # Reglas de razonamiento (expandir segun necesidad)
        obs = observation.lower() if isinstance(observation, str) else ""

        if "no hay datos" in obs or "error" in obs:
            razonamiento["thought"] = "El paso anterior fallo. Debo buscar fuente alternativa."
            razonamiento["action"] = "fallback_to_next_source"

        elif "capturados" in obs and "pasan filtros: 0" in obs:
            razonamiento["thought"] = "El filtro es demasiado estricto o el mercado esta plano. Ajustar filtros."
            razonamiento["action"] = "adjust_filters"

        elif "candidatos" in obs and ">0" in obs:
            razonamiento["thought"] = "Hay candidatos. Debo analizarlos en profundidad."
            razonamiento["action"] = "deep_analyze_candidates"

        elif "trending" in obs:
            razonamiento["thought"] = "Datos de trending obtenidos. Cross-check con Metaplex."
            razonamiento["action"] = "validate_with_metaplex"

        else:
            razonamiento["thought"] = "Continuando con el flujo estandar."
            razonamiento["action"] = "continue_pipeline"

        return razonamiento

    def act(self, razonamiento):
        """Ejecuta la accion determinada."""
        # En produccion, aqui se llamarian los scripts correspondientes
        return {
            "action_executed": razonamiento["action"],
            "status": "pending",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    def observe(self, action_result):
        """Observa el resultado de la accion."""
        return f"Resultado de {action_result['action_executed']}: {action_result['status']}"

    def run(self, initial_observation):
        """Ejecuta ciclo ReAct completo."""
        observation = initial_observation

        for _ in range(self.max_steps):
            # 1. Think
            razonamiento = self.think(observation)
            print(f"[YIN] Paso {razonamiento['step']}:")
            print(f"[YIN]   Thought: {razonamiento['thought']}")
            print(f"[YIN]   Action: {razonamiento['action']}")

            # 2. Act
            action_result = self.act(razonamiento)

            # 3. Observe
            observation = self.observe(action_result)
            print(f"[YIN]   Observation: {observation}")

            self.history.append({
                "step": razonamiento["step"],
                "thought": razonamiento["thought"],
                "action": razonamiento["action"],
                "observation": observation
            })

            # Terminar si se alcanzo el objetivo
            if "completado" in observation.lower():
                break

        return self.history


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    print(f"[YIN] ReAct Framework - {ts}")

    # Ejemplo de uso: detectar oportunidades
    agent = ReActAgent(goal="Detectar 3 oportunidades con score > 70")

    # Observacion inicial
    initial_obs = "Sistema iniciado. Consultando PumpPortal y Metaplex."

    history = agent.run(initial_obs)

    out = {
        "timestamp": ts,
        "fase": "react_framework",
        "goal": agent.goal,
        "total_steps": len(history),
        "history": history
    }

    out_path = REACT_DIR / f"react_{ts}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\n[YIN] Guardado: {out_path}")


if __name__ == "__main__":
    main()