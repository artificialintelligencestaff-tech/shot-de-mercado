---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: VIGENTE (Fase 9, T6)
last_updated: 2026-10-01
version: 1.0
---

# 29 — Protocolo de auto-persistencia por operación

Regla (Dirección, Fase 9): **toda operación significativa deja su resultado en el repo y es recuperable desde él.** Sin excepción.

## 1. Mecanismo

`04_Config/scripts/lib_persist.py` (biblioteca estándar, nunca lanza):

- **`log_operation(op, script, outputs, **contadores)`** agrega una línea a `02_Analisis/operations/<op>.jsonl`. La línea guarda:
  - el momento y el script;
  - cada archivo escrito, con su sha256 corto;
  - los contadores;
  - la referencia `GITHUB_SHA` / `GITHUB_RUN_ID` / `GITHUB_WORKFLOW`.
- **Un archivo por operación:** cada workflow escribe solo el suyo, así que no hay conflictos de rebase entre workflows que commitean en paralelo.
- **Dataset propio:** `02_Analisis/datasets/historical_alerts.jsonl`, append-only.
  - `record_alert`: una línea `alert` por alerta emitida, con clave, símbolo, chain, grupo, versión del scorer, score, motivos, componentes y precio de entrada.
  - `record_outcome`: una línea `outcome` con el precio a 48 h (ventana 48–50 h), el cambio y si cumple la métrica secundaria.
  - Lo escriben `script_97` y `script_98`, que comparten el grupo de concurrencia `repo-write-main` y corren de a uno.

## 2. Operaciones registradas

| Operación (`op`) | Quién | Archivos que deja | Workflow que commitea |
|---|---|---|---|
| `emission_cycle` | `script_97` | `_all_alerts.json`, `alert_*.json`, dossiers, `multichain/_scores.json`, `historical_alerts.jsonl` | `pipeline_t0` |
| `trust_cycle` | `script_98` | `_all_alerts.json`, `trust_*.json`, `historical_alerts.jsonl` (outcome) | `trust_update` |
| `multichain_scan` | `script_114` | `multichain/*.json`, `_history.jsonl`, `_perps.json`, `_governance.json`, `_premarket.json`, `_protocols.json` | `multichain_scanner` |
| `narrative_collect` | `script_115` | `narrative/_index.json`, `_items.json`, `<mint>.json` | `narrative_collector` |
| `dataset_memechain` · `dataset_binance` | `dataset_builder.py` | `01_Datos_Crudos/datasets/…`, `memechain_index.json`, `binance_index.json` | `datasets_build` |
| `dataset_historical_backfill` | `dataset_builder.py` | `historical_alerts.jsonl` | manual (commit de la rama) |

Lo que ya persistía antes de este protocolo sigue igual:
- las detecciones (`01_Datos_Crudos/final_detection/`);
- el acumulado (`shadow_v4/_accumulated.json`);
- las sondas (`diagnostics/*_probe.json`);
- los logs de los bots (`_health_log.json`, etc.).

## 3. Cómo se recupera

- **Qué pasó en una corrida:** `02_Analisis/operations/<op>.jsonl`. Cada línea trae el `run_id` (log de Actions) y el `git_sha` (estado del código).
- **Un archivo exactamente como lo dejó una operación:** con el sha256 corto de la línea se busca en el historial de git el commit cuyo blob coincide.
- **Todas las alertas con su resultado:** `historical_alerts.jsonl`, uniendo por `key` + `timestamp` las líneas `alert` con las `outcome`.
- **Al cierre de cada sesión de Claude Code:** se actualiza el doc 22 (estado, hashes, bitácora). Es la memoria de alto nivel; los JSONL son la de bajo nivel.

## 4. Límites

- El resultado a 48 h se registra solo si el trust loop corre dentro de la ventana de 48 a 50 h. Las alertas que la pierden se miden con velas en `monitor_shadow` (métrica dual completa: la primaria necesita el camino del precio, no solo el cierre).
- Crecimiento estimado: unos cientos de líneas por día entre todas las bitácoras (~100 KB/día). Si hace falta, rotación mensual por archivo.
