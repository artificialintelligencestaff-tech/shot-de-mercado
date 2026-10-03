# Plantilla de Auditoría por Bot

## Formato de Archivos

### `_audit.jsonl` (1 línea por corrida)
```json
{"ts": 1790900000, "bot": "rss", "items_in": 581, "items_new": 569, "items_discarded": 12, "errors": 1, "duration_s": 33, "status": "success", "run_id": "37094486268"}
```

**Campos:**
- `ts`: epoch UTC de la corrida
- `bot`: nombre del bot (rss, telegram_a, telegram_b, web, github, x, forums)
- `items_in`: total de ítems recibidos de las fuentes
- `items_new`: ítems que pasan dedup y se guardan
- `items_discarded`: ítems descartados por dedup / sin identificadores / errores de parseo
- `errors`: número de fuentes con error (status != 200 o parse error)
- `duration_s`: duración de la corrida en segundos
- `status`: success / failure / partial
- `run_id`: GitHub Actions run ID

### `_metrics.json` (agregados rodantes)
```json
{
  "runs": 15,
  "items_total": 8415,
  "dedup_rate": 0.021,
  "error_rate": 0.034,
  "availability": 0.967,
  "last_update": 1790900000,
  "avg_items_per_run": 561,
  "avg_duration_s": 28,
  "sources_healthy": 11,
  "sources_total": 12
}
```

**Campos:**
- `runs`: total de corridas registradas
- `items_total`: suma de `items_new` de todas las corridas
- `dedup_rate`: `sum(items_discarded) / sum(items_in)`
- `error_rate`: `sum(errors) / sum(sources_queried)`
- `availability`: corridas exitosas / total corridas
- `last_update`: epoch de la última actualización
- `avg_items_per_run`: `items_total / runs`
- `avg_duration_s`: duración media
- `sources_healthy`: fuentes con status 200 en última corrida
- `sources_total`: total de fuentes configuradas

## Proceso de Actualización

1. **Después de cada corrida exitosa** del bot: append a `_audit.jsonl`
2. **Bot orchestrator** (cada 5 min): recalcula `_metrics.json` desde `_audit.jsonl` de los últimos 30 días
3. **Retención**: 90 días (poda automática por orchestrator)
4. **Ubicación**: `02_Analisis/sources/<bot>/_audit.jsonl` y `_metrics.json`