---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
auto_generated: false
---

# Estado Actual — Snapshot Vivo del Proyecto

Este archivo es un **snapshot del estado del proyecto** en un momento dado. A diferencia de los demás archivos del cerebro, este **se actualiza con frecuencia** y eventualmente será **auto-generado** por un script al final de cada ciclo.

**Cómo leerlo:** si la fecha del header (`last_updated`) tiene más de 7 días, el contenido puede estar desactualizado. En ese caso, verificar directamente los archivos de estado en disco.

## 1. Snapshot al 2026-09-24

### 1.1 Estado del pipeline

| Capa | Estado | Notas |
|---|---|---|
| Capa 1 — Pre-launch | PARCIAL | Script 99 corre, 0 TGEs detectados |
| Capa 2 — Detección T+0 | OK | ~400 tokens/ciclo |
| Capa 3 — Enriquecimiento + scoring | OK | Scoring v7 activo |
| Capa 4 — Alert + Trust | PARCIAL | Alertas OK, trust con bug de baseline |
| Capa 5 — Feedback loop | NO IMPLEMENTADO | Pendiente |

### 1.2 Archivos de estado

| Archivo | Path | Tamaño | Última modificación |
|---|---|---|---|
| `_all_alerts.json` | `02_Analisis\alerts\` | 988 B | 2026-09-23 23:48 |
| `_accumulated.json` (v4) | `02_Analisis\shadow_v4\` | 41482 B | 2026-09-23 21:32 |
| `_accumulated.json` (v5) | `02_Analisis\shadow_v5\` | 15129 B | 2026-09-23 21:39 |
| `_accumulated.json` (v2) | `02_Analisis\shadow_v2\` | 2 B | vacío |
| `_precision_log.json` | raíz | 546 B | 2026-09-23 23:48 |
| `_cycle_log.json` | raíz | 261 B | 2026-09-23 23:48 |
| `_project_manifest.json` | raíz | 3451 B | 2026-09-24 00:24 |
| `_state_manifest.json` | raíz | 360 B | 2026-09-23 23:48 |

### 1.3 Alertas activas

| Symbol | Mint | Score | Confianza | Trust updates | Veredicto final |
|---|---|---|---|---|---|
| SI | `DegeC37...pump` | 55 | 56 | 1 (t+1h) | PENDIENTE |
| OURA | `2Kxuxn...pump` | 55 | 56 | 1 (t+1h) | PENDIENTE |

**Total alertas emitidas:** 2.
**Total alertas cerradas:** 0.
**Precisión acumulada:** n/a (ninguna cerrada).

### 1.4 Shadow modes

| Shadow | Estado | Mints rastreados |
|---|---|---|
| shadow_v2 | DEPRECADO | 0 (archivo vacío) |
| shadow_v3 | MISSING | — |
| shadow_v4 | ACTIVO | 5 |
| shadow_v5 | ACTIVO | 4 |

**Decisión pendiente:** consolidar en v5.

### 1.5 Git y GitHub

| Aspecto | Estado |
|---|---|
| Git inicializado | NO |
| Repo remoto en GitHub | NO |
| GitHub Actions | NO |
| Secrets configurados | NO |

### 1.6 Bot Telegram

| Aspecto | Estado |
|---|---|
| Token configurado | SI (`04_Config\.env`) |
| Chat ID configurado | SI |
| API funcional | SI (verificado con getMe en Ciclo 17.1) |
| Último mensaje enviado | 2026-09-17 (test) |

## 2. Archivos del árbol neurocerebral

Total: 13 archivos creados de 18 planificados.

| # | Archivo | Estado |
|---|---|---|
| — | README.md | OK |
| 00a | 00_Directivas_INDEX.md | OK |
| 00b | 00_NUCLEO.md | OK |
| 01 | 01_HISTORIA.md | OK |
| 02 | 02_ARQUITECTURA.md | OK |
| 03 | 03_FLUJOS.md | OK |
| 04 | 04_SCRIPTS_CATALOG.md | OK (PARCIAL) |
| 05 | 05_FUENTES.md | OK |
| 06 | 06_SCORING.md | OK |
| 07 | 07_TRUST_UPDATE.md | OK |
| 08 | 08_PIPELINE_ACTIVO.md | OK |
| 09 | 09_ALERTAS.md | OK |
| 10 | 10_ESTADO_ACTUAL.md | **este archivo** |
| 11 | 11_ROADMAP.md | PENDIENTE |
| 12 | 12_TROUBLESHOOTING.md | PENDIENTE |
| 13 | 13_DECISIONES.md | PENDIENTE |
| 14 | 14_METRICAS.md | PENDIENTE |
| 15 | 15_CONTRIBUCION.md | PENDIENTE |
| — | SKILLS_skill_entender_proyecto.md | OK |
| — | _MANIFESTO.md | PENDIENTE |
| — | _GLOSARIO.md | PENDIENTE |
| — | _OPERATOR_HANDBOOK.md | PENDIENTE |

## 3. Ciclo actual

| Aspecto | Valor |
|---|---|
| Ciclo activo | 17.7 |
| Fase del plan maestro | Fase 0 (migración a serverless) |
| Último ciclo cerrado | 17.6.C |
| Próximo objetivo | Completar los 5 archivos restantes del cerebro |

## 4. Bugs conocidos

| # | Bug | Severidad | Fix planificado |
|---|---|---|---|
| 1 | Trust scheduler: `price_change_pct: 0.0` en primera pasada | ALTA | Ciclo 17.10 |
| 2 | Shadow modes v4 y v5 duplicados | MEDIA | Ciclo 17.10 |
| 3 | ~60 scripts sin consolidar en `_archived/` | BAJA | Ciclo 17.10 |
| 4 | Capa 1 sin TGEs detectados | MEDIA | Fase 3 |
| 5 | Feedback loop no implementado | MEDIA | Fase 2 |

## 5. Mints rastreados

### shadow_v4 (5 mints)
- `6ePFXQ7D8VrnqXCx3XDpzWxa7Hox4oxtKu48DktmUfEm`
- `GPzpoXpD74E2C4CJNayuoyBqPQJEsPtdse3nhntrpump`
- `DegeC37wePGYLFD2RXuc2TNEFK2qCGJsMDxHCpSppump` (SI)
- `2KxuxnmyySXTFU1BZvrKTYwvbAzncSKR6YkAP1Sqpump` (OURA)
- `6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx`

### shadow_v5 (4 mints)
- `3DXM8FETvLSNoi416QsQUMeFA17dEPDX9DvoDboVpump`
- `4LayazawxCAj4ENdvr2TzCTa627kAb8HndFSvmd5pump`
- `DqQ9QbT3SuYkEdt1m7EDeZaGPDbXBH9HKX3wP7fCpump`
- `6vDA6YcAUpttbkLevQL5U93xBVWFpgc6HipRjUuwpump`

## 6. Cómo actualizar este archivo

**Manual (actual):** YANG emite nuevo contenido al cierre de cada bloque de ciclos.

**Automático (futuro):** `script_105_update_state.py` correrá al final de cada ciclo del pipeline y regenerará este archivo desde:
- `_all_alerts.json`
- `_precision_log.json`
- `_cycle_log.json`
- `_project_manifest.json`
- Lista de archivos del cerebro

## 7. Qué hacer si este archivo está desactualizado

1. Verificar `last_updated` del header.
2. Si tiene >7 días, correr manualmente: `python 04_Config\scripts\script_105_update_state.py` (cuando exista).
3. Mientras el script no exista, consultar directamente los archivos de estado listados en sección 1.2.

## VER TAMBIÉN

- [02_ARQUITECTURA.md](02_ARQUITECTURA.md) — arquitectura completa
- [08_PIPELINE_ACTIVO.md](08_PIPELINE_ACTIVO.md) — scripts canónicos
- [11_ROADMAP.md](11_ROADMAP.md) — próximas fases
- [12_TROUBLESHOOTING.md](12_TROUBLESHOOTING.md) — bugs conocidos en detalle

## Changelog

- 2026-09-24 — v1.0 — Snapshot inicial (YANG, Ciclo 17.7.A)