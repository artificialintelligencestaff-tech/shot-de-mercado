# El cerebro de dios — índice

Documentación del proyecto **Shot de Mercado**. Índice regenerado en D-101 (2026-10-05). La entrada al repo es el
[`README.md` de la raíz](../README.md).

**Orden de lectura para un agente nuevo:**
1. 35 (traspaso)
2. 38 (datos)
3. 34 (bots de fuentes)
4. 32 (scorer joven)
5. 31 (early watch)
6. 36 (método)
7. 37 (autonomía)
8. 22 (memoria: la última fila es el estado)

Estados:
- **vigente**: describe el sistema actual;
- **referencia**: válido pero de una fase anterior;
- **histórico**: reemplazado, en `_historico/`;
- **bitácora**: se agregan filas.

## Vigentes (sistema actual)

| # | Doc | Qué cubre | Estado |
|---|---|---|---|
| 22 | [22_MEMORIA_CLAUDE.md](22_MEMORIA_CLAUDE.md) | Memoria de Claude: una fila por directiva | bitácora |
| 24 | [24_DOSSIER_POR_ACTIVO.md](24_DOSSIER_POR_ACTIVO.md) | Dossier por activo (script_113), ruta de compra primero | vigente |
| 26 | [26_METRICA_REPETICION.md](26_METRICA_REPETICION.md) | Métrica de repetición de menciones (script_115) | vigente |
| 27 | [27_SCORING_MULTICHAIN.md](27_SCORING_MULTICHAIN.md) | Scoring por tipo de activo, grupos a–i | vigente |
| 30 | [30_PROTOCOLO_PERSISTENCIA.md](30_PROTOCOLO_PERSISTENCIA.md) | Auto-persistencia por operación (lib_persist) | vigente |
| 31 | [31_DETECCION_TEMPRANA.md](31_DETECCION_TEMPRANA.md) | Early watch (script_116), hand-off, claims, gate | vigente |
| 32 | [32_SCORER_JOVENES.md](32_SCORER_JOVENES.md) | Scorer joven (< 60 min), H-0 preregistrada, v7.2.2 aprobado | vigente |
| 34 | [34_SISTEMA_MULTIBOT.md](34_SISTEMA_MULTIBOT.md) | Bots de fuentes, orquestador, reparador, eventos, recetas, calendario de preventa, X | vigente |
| 35 | [35_TRASPASO_CLAUDE.md](35_TRASPASO_CLAUDE.md) | Traspaso: inventario con SHA-256, lógica, cómo continuar | vigente |
| 36 | [36_METODO_POR_GRUPO.md](36_METODO_POR_GRUPO.md) | Método científico por grupo, debate adversario, Dossier v2 | vigente |
| 37 | [37_BOTS_AUTONOMIA.md](37_BOTS_AUTONOMIA.md) | Bots de autonomía (scout, evaluator, integrator, auditor) | diseño |
| 38 | [38_ARQUITECTURA_DATOS.md](38_ARQUITECTURA_DATOS.md) | Categorías de datos, retención por carpeta, dueños, fixes D-101 | vigente |

## Referencia (fases anteriores; válidos pero no al día)

| # | Doc | Qué cubre |
|---|---|---|
| 00 | [00_NUCLEO.md](00_NUCLEO.md) | Propósito raíz |
| 01 | [01_HISTORIA.md](01_HISTORIA.md) | Cronología hasta el 24/09 |
| 03 | [03_FLUJOS.md](03_FLUJOS.md) | Workflows (antes de los bots de fuentes) |
| 04 | [04_SCRIPTS_CATALOG.md](04_SCRIPTS_CATALOG.md) | Catálogo de scripts (regenerado en D-101: qué corre y qué no) |
| 05 | [05_FUENTES.md](05_FUENTES.md) | Fuentes gratuitas (ver también `_servicios_open_source/`) |
| 06, 07, 09 | [06_SCORING.md](06_SCORING.md), [07_TRUST_UPDATE.md](07_TRUST_UPDATE.md), [09_ALERTAS.md](09_ALERTAS.md) | Scoring v7, trust update, formato de alertas |
| 12–15 | [12_TROUBLESHOOTING.md](12_TROUBLESHOOTING.md), [13_DECISIONES.md](13_DECISIONES.md), [14_METRICAS.md](14_METRICAS.md), [15_CONTRIBUCION.md](15_CONTRIBUCION.md) | Errores, decisiones, métricas, contribución |
| 16–21 | [16](16_CAPITULO_II_MULTIMODAL.md) · [17](17_FIX_DEDUP_SCRIPT97.md) · [18](18_CAPITULO_VII_NARRATIVA.md) · [19](19_CALIBRACION_V72.md) · [20](20_V72_1_GATE.md) · [21](21_INSIGHT_84_RUG.md) | Capítulos y hallazgos de Fase 7–8 (calibración v7.2, gate, insight del 84 %) |
| 23, 25 | [23_GRUPOS_ACTIVOS_INVESTIGACION.md](23_GRUPOS_ACTIVOS_INVESTIGACION.md), [25_HERRAMIENTAS_SCRAPING.md](25_HERRAMIENTAS_SCRAPING.md) | Investigación de grupos y herramientas de scraping |
| 29, 39 | [29_MEMORIA_YIN.md](29_MEMORIA_YIN.md), [39_CEREBRO_OPERATIVO_YIN.md](39_CEREBRO_OPERATIVO_YIN.md) | Memoria y cerebro operativo de YIN (el 39 era el segundo "13", renumerado en D-101) |
| 99 | [99_MASTER_PROMPT.md](99_MASTER_PROMPT.md) | Master prompt original |
| — | [_MANIFESTO.md](_MANIFESTO.md), [_GLOSARIO.md](_GLOSARIO.md), [_OPERATOR_HANDBOOK.md](_OPERATOR_HANDBOOK.md), `SKILLS_*.md` | Fundacionales y guías |
| — | [00_Directivas_INDEX.md](00_Directivas_INDEX.md) | Índice viejo (24/09); reemplazado por este archivo |

## Histórico (`_historico/`, movidos con `git mv` en D-101)

| Doc | Reemplazado por |
|---|---|
| [_historico/02_ARQUITECTURA.md](_historico/02_ARQUITECTURA.md) | 34 + 38 |
| [_historico/08_PIPELINE_ACTIVO.md](_historico/08_PIPELINE_ACTIVO.md) | 31 + 34 (pipeline actual: pipeline_t0 + early watch + bots) |
| [_historico/10_ESTADO_ACTUAL.md](_historico/10_ESTADO_ACTUAL.md) | 22 (última fila) + 35 |
| [_historico/11_ROADMAP.md](_historico/11_ROADMAP.md) | 35 §4 (siguiente trabajo) + 37 |
| [_historico/28_INVENTARIO_COMPLETO.md](_historico/28_INVENTARIO_COMPLETO.md) | `_servicios_open_source/` + `02_Analisis/patrimonio/_inventario.json` |
| [_historico/33_ARQUITECTURA_MULTIBOT.md](_historico/33_ARQUITECTURA_MULTIBOT.md) | 34 (el 33 queda como investigación de fuentes) |
