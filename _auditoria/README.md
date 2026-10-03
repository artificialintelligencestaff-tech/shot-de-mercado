# Carpeta de Auditoría — Material para Claude1

## Propósito
Material de auditoría completo de la rama `claude/d041-enjambre` para que Claude1 (revisor) la evalúe sin ejecutar git.

## Rama Auditada
- **Rama**: `claude/d041-enjambre`
- **Hash final**: `2c9d45efb9c7e65ddb3de7f39e14d10826ce9a9c`
- **Base**: `089eba6` (early_watch a: 2026-10-03T05:07:52+00:00)
- **Hash remoto**: `2c9d45efb9c7e65ddb3de7f39e14d10826ce9a9c`

## Archivos

| Archivo | Descripción |
|---------|-------------|
| `d041.patch` | Diff completo (2539 líneas) entre `089eba6` y `2c9d45e` |
| `d041_commits.txt` | Lista de 6 commits en la rama |
| `d041_stat.txt` | Resumen estadístico (archivos cambiados, inserciones/eliminaciones) |

## Instrucciones para Claude1
1. Lee los 3 archivos desde `main` (no ejecutes git).
2. Evalúa: arquitectura, código, tests, docs, seguridad.
3. Emite veredicto: **CRÍTICOS** / **MEDIOS** / **OPORTUNIDADES** / **APROBAR** / **RECHAZAR**.

## Contenido de la Rama (D-041)
- **T1**: `lib_normalize` — normalización semántica (#19) en escritura y fusión de sources
- **T2**: `bot_self_repair` — reparador por reglas explícitas (#20, doc 34 §11)
- **T3**: `lib_knowledge_graph` — grafo de co-mención (#7) escrito por el orquestador
- **T4**: `auditoría por bot (#15)` — `_audit.jsonl` + `_metrics.json` en rss y orquestador
- **T5**: `bot_telegram_public` — 15 canales públicos, 2 instancias de 40 min
- **T6+T7**: `doc 36 método científico por grupo a–i` + `Dossier v2`; docs 22 y 34 actualizados

## Tests
- `test_script_115_collector.py`: 21 tests (incluye nuevo `test_evm_no_confunde_con_base58`)
- Todos pasan: 21/21 OK

## Estado
- Rama mergeable a `main` sin conflictos
- Push completado a `origin/claude/d041-enjambre`