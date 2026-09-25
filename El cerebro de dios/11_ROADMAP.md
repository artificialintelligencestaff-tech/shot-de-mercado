---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Roadmap — Fases y Ciclos del Proyecto

Este archivo describe el plan de evolución del proyecto desde su estado actual (2026-09-24) hasta el cumplimiento pleno de sus fines (bot autónomo 24/7 con precisión medida).

## 1. Principios del roadmap

1. **Un ciclo = un objetivo verificable.** No se dispersa.
2. **Evidencia > documentación.** Sin ejecución verificable, no hay progreso.
3. **Fase cerrada antes de la siguiente.** No se salta.
4. **Prioridad a la funcionalidad sobre la novedad.** Primero lo que ya existe, después lo que falta.
5. **Free-only en todo.** Ninguna dependencia paga.

## 2. Fases del proyecto

### Fase 0 — Fundación documental y migración a serverless

**Objetivo:** dejar el proyecto con cerebro documental completo y listo para migrar a GitHub Actions.

| Ciclo | Objetivo | Estado |
|---|---|---|
| 17.2 | README + Índice + Skill entry point | CERRADO |
| 17.3 | Núcleo + Historia + Arquitectura | CERRADO |
| 17.4 | Flujos + Catálogo de scripts | CERRADO |
| 17.5 | Fuentes + Scoring | CERRADO |
| 17.6 | Trust + Pipeline activo + Alertas | CERRADO |
| 17.7 | Estado + Roadmap + Troubleshooting | EN CURSO |
| 17.8 | Decisiones + Métricas + Contribución | PENDIENTE |
| 17.9 | Manifesto + Glosario + Operator Handbook | PENDIENTE |
| 17.10 | Skills restantes (4) | PENDIENTE |
| 17.11 | Git init + primer push a GitHub | PENDIENTE |
| 17.12 | Workflows GitHub Actions (trust, pipeline, prelaunch) | PENDIENTE |
| 17.13 | Test end-to-end desde GitHub | PENDIENTE |

**Criterio de cierre Fase 0:** el pipeline corre disparado por cron desde GitHub Actions, commitea estado al repo, y emite alerta Telegram sin intervención local.

### Fase 1 — Fix y consolidación

**Objetivo:** dejar el pipeline actual sin bugs y sin redundancias.

| Ciclo | Objetivo | Estado |
|---|---|---|
| 18.1 | Fix bug de baseline del trust scheduler (3 partes) | PENDIENTE |
| 18.2 | Consolidar shadow mode (elegir v5, deprecar v4) | PENDIENTE |
| 18.3 | Archivar scripts deprecados en `_archived/` | PENDIENTE |
| 18.4 | Backfill de initial_price en SI y OURA | PENDIENTE |
| 18.5 | Ejecutar trust scheduler con fix y verificar `price_change_pct != 0.0` | PENDIENTE |
| 18.6 | Fijar veredicto final de SI y OURA | PENDIENTE |

**Criterio de cierre Fase 1:** trust scheduler produce trust updates con cambio real; alertas SI y OURA cerradas con veredicto final; ningún `price_change_pct: 0.0` falso.

### Fase 2 — Autonomía 24/7

**Objetivo:** el bot corre sin intervención humana.

| Ciclo | Objetivo | Estado |
|---|---|---|
| 19.1 | Watchlist automática (script_101) | PENDIENTE |
| 19.2 | Auto-reparación 4 capas (script_100) | PENDIENTE |
| 19.3 | Task Scheduler serverless (cron en workflows) | PENDIENTE |
| 19.4 | Feedback loop automatizado (script_104) | PENDIENTE |
| 19.5 | Pre-launch activo con TGEs reales | PENDIENTE |
| 19.6 | Backup diario automatizado | PENDIENTE |

**Criterio de cierre Fase 2:** 7 días consecutivos de operación sin intervención humana. Logs de GitHub Actions sin fallos.

### Fase 3 — Expansión de fuentes

**Objetivo:** enriquecer el scoring con las fuentes que faltan.

| Ciclo | Objetivo | Estado |
|---|---|---|
| 20.1 | Ingestión de noticias cripto (CryptoPanic, RSS) | PENDIENTE |
| 20.2 | Ingestión social (Reddit JSON, ApeWisdom, free-crypto-news) | PENDIENTE |
| 20.3 | Ingestión académica (arXiv filtrado) | PENDIENTE |
| 20.4 | MCPs integrados (Chainbase, Tavily, Brave) | PENDIENTE |
| 20.5 | Scoring v8 con nuevas señales | PENDIENTE |

**Criterio de cierre Fase 3:** scoring v8 usa al menos 3 fuentes nuevas medidas contra las alertas históricas.

### Fase 4 — Refinamiento predictivo

**Objetivo:** medir y mejorar la precisión real.

| Ciclo | Objetivo | Estado |
|---|---|---|
| 21.1 | Backtesting sobre histórico de alertas | PENDIENTE |
| 21.2 | Ajuste de pesos por evidencia | PENDIENTE |
| 21.3 | Segmentación por tipo de activo | PENDIENTE |
| 21.4 | Calibración de confianza declarada vs real | PENDIENTE |
| 21.5 | Scoring v9 (calibrado) | PENDIENTE |

**Criterio de cierre Fase 4:** precisión medida >55% en muestra >= 20 alertas cerradas.

### Fase 5 — Portabilidad y continuidad

**Objetivo:** que el proyecto sobreviva cambios de operario y de modelo IA.

| Ciclo | Objetivo | Estado |
|---|---|---|
| 22.1 | Manual del operario completo | PENDIENTE |
| 22.2 | Suite de tests por módulo | PENDIENTE |
| 22.3 | Backups automáticos con retención | PENDIENTE |
| 22.4 | Versionado semántico de scripts | PENDIENTE |
| 22.5 | Documentación de contribución | PENDIENTE |

**Criterio de cierre Fase 5:** un operario nuevo puede tomar el proyecto en 1 día leyendo el cerebro.

## 3. Roadmap visual

```
AHORA  → Fase 0: Fundación documental + serverless
   ↓
+1 sem → Fase 1: Fix + consolidación
   ↓
+2-3 sem → Fase 2: Autonomía 24/7
   ↓
+1 mes → Fase 3: Expansión de fuentes
   ↓
+2 meses → Fase 4: Refinamiento predictivo
   ↓
+3 meses → Fase 5: Portabilidad total
```

## 4. Hitos medibles

| Hito | Criterio | Fase |
|---|---|---|
| H1 | Cerebro documental completo (18 archivos) | 0 |
| H2 | Repo GitHub + primer push | 0 |
| H3 | Workflow trust_update corriendo en GitHub Actions | 0 |
| H4 | Bug de baseline corregido + SI/OURA cerradas | 1 |
| H5 | 7 días sin intervención humana | 2 |
| H6 | Precisión medida en muestra >= 10 | 3 |
| H7 | Precisión >55% en muestra >= 20 | 4 |
| H8 | Operario nuevo entiende el proyecto en 1 día | 5 |

## 5. Riesgos del roadmap

| Riesgo | Impacto | Mitigación |
|---|---|---|
| GitHub Actions supera límite free | Alto (privado) | Repo público o migrar a cron-job.org |
| Fuente gratuita desaparece | Medio | Catálogo de fuentes con alternativas VIABLE |
| Modelo IA cambia (YANG o YIN) | Alto | Cerebro documental permite transferencia |
| Precisión real <50% con n>=10 | Alto | Revisar scoring v7, calibrar v8/v9 |
| Telegram cambia API | Bajo | Cliente aislado en `script_20` |

## 6. Decisiones pendientes que impactan el roadmap

| # | Decisión | Responsable | Bloquea |
|---|---|---|---|
| 1 | Repo público o privado | Dirección | Fase 0 |
| 2 | Shadow mode canónico: v4 o v5 | Dirección | Fase 1 |
| 3 | Estrategia de alertas: exploratoria (>=50%) o conservadora (>=70%) | Dirección | Fase 2 |
| 4 | Umbral de ajuste de pesos del scoring | YANG + Dirección | Fase 4 |

## 7. Qué NO está en el roadmap (y por qué)

- **App móvil propia:** Telegram es el canal, no hace falta app.
- **Smart contracts propios:** el proyecto es de predicción, no de ejecución.
- **Integración con exchanges (CEX/DEX) para compra automática:** viola constraint "no ejecutar transacciones".
- **Soporte multi-idioma:** por ahora español rioplatense.
- **Modelos propios de ML:** se usan heurísticas, no se entrena red neuronal propia.

## VER TAMBIÉN

- [00_NUCLEO.md](00_NUCLEO.md) — fines del proyecto
- [10_ESTADO_ACTUAL.md](10_ESTADO_ACTUAL.md) — dónde estamos hoy
- [12_TROUBLESHOOTING.md](12_TROUBLESHOOTING.md) — bugs que bloquean fases
- [13_DECISIONES.md](13_DECISIONES.md) — bitácora de decisiones que impactan el roadmap

## Changelog

- 2026-09-24 — v1.0 — Creación inicial con 6 fases y 8 hitos (YANG, Ciclo 17.7.B)