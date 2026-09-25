---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Índice Central — Proyecto Shot de Mercado

Este archivo es el **punto de entrada** para cualquier humano o agente que necesite entender el proyecto.

## Documentos fundacionales

| Archivo | Qué contiene | Estado |
|---|---|---|
| [_MANIFESTO.md](_MANIFESTO.md) | Fines, principios, filosofía del proyecto | PLANTILLA |
| [_GLOSARIO.md](_GLOSARIO.md) | Términos, mints, símbolos, IDs | PLANTILLA |
| [_OPERATOR_HANDBOOK.md](_OPERATOR_HANDBOOK.md) | Cómo operar el proyecto paso a paso | PLANTILLA |

## Cerebro — arquitectura del sistema

| # | Archivo | Qué contiene | Estado |
|---|---|---|---|
| 00 | [CEREBRO/00_NUCLEO.md](CEREBRO/00_NUCLEO.md) | Propósito raíz del sistema | PLANTILLA |
| 01 | [CEREBRO/01_HISTORIA.md](CEREBRO/01_HISTORIA.md) | Cronología del proyecto | PLANTILLA |
| 02 | [CEREBRO/02_ARQUITECTURA.md](CEREBRO/02_ARQUITECTURA.md) | Las 5 capas del sistema | PLANTILLA |
| 03 | [CEREBRO/03_FLUJOS.md](CEREBRO/03_FLUJOS.md) | Qué hace cada workflow | PLANTILLA |
| 04 | [CEREBRO/04_SCRIPTS_CATALOG.md](CEREBRO/04_SCRIPTS_CATALOG.md) | ~100 scripts explicados | PLANTILLA |
| 05 | [CEREBRO/05_FUENTES.md](CEREBRO/05_FUENTES.md) | APIs, MCPs, fuentes gratuitas | PLANTILLA |
| 06 | [CEREBRO/06_SCORING.md](CEREBRO/06_SCORING.md) | Scoring v7 + versiones | PLANTILLA |
| 07 | [CEREBRO/07_TRUST_UPDATE.md](CEREBRO/07_TRUST_UPDATE.md) | Reglas de confianza 1h/6h/24h | PLANTILLA |
| 08 | [CEREBRO/08_PIPELINE_ACTIVO.md](CEREBRO/08_PIPELINE_ACTIVO.md) | Cuál es el canónico hoy | PLANTILLA |
| 09 | [CEREBRO/09_ALERTAS.md](CEREBRO/09_ALERTAS.md) | Formato Telegram final | PLANTILLA |
| 10 | [CEREBRO/10_ESTADO_ACTUAL.md](CEREBRO/10_ESTADO_ACTUAL.md) | Estado vivo (auto) | PLANTILLA |
| 11 | [CEREBRO/11_ROADMAP.md](CEREBRO/11_ROADMAP.md) | Fases y ciclos | PLANTILLA |
| 12 | [CEREBRO/12_TROUBLESHOOTING.md](CEREBRO/12_TROUBLESHOOTING.md) | Errores conocidos + fix | PLANTILLA |
| 13 | [CEREBRO/13_DECISIONES.md](CEREBRO/13_DECISIONES.md) | Bitácora de decisiones | PLANTILLA |
| 14 | [CEREBRO/14_METRICAS.md](CEREBRO/14_METRICAS.md) | Precisión medida | PLANTILLA |
| 15 | [CEREBRO/15_CONTRIBUCION.md](CEREBRO/15_CONTRIBUCION.md) | Cómo agregar valor | PLANTILLA |

## Skills — entry points para agentes

| Skill | Uso |
|---|---|
| [SKILLS/skill_entender_proyecto.md](../../SKILLS/skill_entender_proyecto.md) | **LEER PRIMERO** si sos agente nuevo |
| [SKILLS/skill_ejecutar_pipeline.md](../../SKILLS/skill_ejecutar_pipeline.md) | Cómo correr el pipeline |
| [SKILLS/skill_agregar_alerta.md](../../SKILLS/skill_agregar_alerta.md) | Cómo emitir una alerta |
| [SKILLS/skill_debuggear.md](../../SKILLS/skill_debuggear.md) | Cómo diagnosticar fallos |
| [SKILLS/skill_contribuir.md](../../SKILLS/skill_contribuir.md) | Cómo proponer mejoras |

## Convenciones

- **Idioma:** español rioplatense.
- **Formato:** Markdown con header YAML obligatorio.
- **Interconexión:** cada archivo termina en "VER TAMBIÉN".
- **Estados:** COMPLETO / PARCIAL / PLANTILLA.
- **Versionado:** cada archivo lleva versión semántica.

## VER TAMBIÉN

- [../../README.md](../../README.md) — entrada raíz
- [../CEREBRO/15_CONTRIBUCION.md](CEREBRO/15_CONTRIBUCION.md) — guía de contribución

## Changelog

- 2026-09-24 — v1.0 — Creación inicial (YANG, Ciclo 17.2)