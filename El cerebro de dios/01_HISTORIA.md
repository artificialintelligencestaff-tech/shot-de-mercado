---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Historia — Cronología del Proyecto Shot de Mercado

## Fase fundacional (semanas previas al 12 de septiembre de 2026)

**Objetivo:** explorar el dominio cripto, relevar fuentes gratuitas, entender qué señales preceden a movimientos verticales.

**Producto:** ~50 scripts exploratorios (script_01 a script_50), cada uno probando una fuente o enfoque distinto:
- Tops MCP, Alpha MCP, Onvexia
- CoinGecko, DeFiLlama, Alternative.me
- Santiment, ApeWisdom
- Telegram alerts (script_20, 20b)
- News aggregators, holders analysis, volume anomaly

**Resultado:** mapa de fuentes gratuitas viables vs. descartadas. El proyecto aprende qué es útil.

## Fase de pipeline (12-17 de septiembre de 2026)

**Objetivo:** construir un pipeline coherente que combine las fuentes en un flujo único.

**Producto:**
- Scripts 51-99: pre-launch (Metaplex, three.ws, Clawnch, PumpPortal), filtros, enrich, scoring, alertas, trust scheduler.
- `script_81_pipeline_final.py`, `script_82_final_detection.py`: intentos de consolidación.
- `script_95_shadow_v4.py` a `script_96_shadow_v5.py`: modos shadow en paralelo.
- `script_97_emit_alerts.py`: emisión de alertas Telegram.
- `script_98_trust_scheduler.py`: scheduler de confianza.
- `script_99_prelaunch.py`: pre-lanzamiento.

**Hito 12 de septiembre:** primer Ciclo completo del pipeline v4 (Quality Gate + Priority Queue). 400+ tokens capturados, 25 calls a MadeOnSol, 9 tokens validados, 2 en WATCH REAL (SI, OURA).

## Fase de alertas reales (14-15 de septiembre de 2026)

**Objetivo:** emitir las primeras alertas reales.

**Producto:** 2 alertas emitidas:
- **SI:** 56% confianza → -95.7% en 0.6h → **FALSO POSITIVO**
- **OURA:** 56% confianza → +17,178% en 0.6h → **ACIERTO EXTRAORDINARIO**

**Precisión:** 50% (1 de 2). Muestra insuficiente pero informativa.

**Aprendizaje:** el sistema detecta tokens de ALTO riesgo y ALTO potencial. La precisión real vendrá del trust update, no del scoring inicial.

## Fase de auditoría (23-24 de septiembre de 2026)

**Objetivo:** auditar el sistema para identificar bugs y consolidar arquitectura.

**Producto:**
- Identificación del bug del trust scheduler: `prev_price = current_price` en primera pasada → `price_change_pct: 0.0` falso.
- Confirmación de que el script 98 **sí consulta Dexscreener** (no es stub, es bug).
- Inventario real del proyecto: ~100 scripts, bot Telegram funcional, 3 shadow modes coexistiendo.
- Primer árbol neurocerebral documental.
- Migración en curso a arquitectura serverless (GitHub Actions).

## Errores aprendidos (registrados para no repetir)

| # | Error | Aprendizaje |
|---|---|---|
| 1 | Documentar arquitectura sin implementarla (scripts 100-104) | Evidencia > documentación |
| 2 | Múltiples versiones del mismo script sin consolidar (95, 98, 98b) | Un script canónico por módulo |
| 3 | Trust scheduler corriendo sin persistir baseline | Comparar contra precio de emisión, no contra sí mismo |
| 4 | Comunicación por narrativa larga → truncamiento | Micro-mensajes atómicos de ≤2KB |
| 5 | Evidencia por retype manual → hashes fabricados | Base64 byte-exacto obligatorio |
| 6 | Path ambiguo entre ciclos → FILE_NOT_FOUND | Path canónico declarado en `_project_manifest.json` |

## Estado actual (2026-09-24)

- Bot Telegram operativo.
- ~100 scripts, sin consolidar.
- Shadow modes v4 y v5 activos.
- Git no inicializado.
- GitHub Actions no existe.
- Fase 0 (migración serverless) en curso.

## VER TAMBIÉN

- [00_NUCLEO.md](00_NUCLEO.md) — propósito raíz
- [02_ARQUITECTURA.md](02_ARQUITECTURA.md) — arquitectura actual
- [11_ROADMAP.md](11_ROADMAP.md) — próximas fases
- [13_DECISIONES.md](13_DECISIONES.md) — bitácora de decisiones

## Changelog

- 2026-09-24 — v1.0 — Creación inicial (YANG, Ciclo 17.3)