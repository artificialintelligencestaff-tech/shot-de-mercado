# Recetas de bots de fuentes (Ola 3, D-067)

Una receta YAML equivale a un bot de fuentes sin código propio.

**Cómo se ejecutan**
- `sources_runner.yml` corre cada 10 min.
- Planifica con `bot_runner.py --plan` y ejecuta cada receta habilitada cuya cadencia venció, un job por receta.

**Quién habilita**
- `bot_genesis.py` (diario) valida cada receta: esquema, fetch en seco, ≥ 5 ítems y dominio no duplicado.
- El resultado queda en `_recipes_state.json`: `enabled: true`, o `probation` con el motivo.
- Una receta sin `enabled: true` no corre.

**Origen de las recetas**
- `bot_genesis.py` las genera desde el bloque `recipe:` de las fichas en `_servicios_open_source/`. Las generadas llevan la cabecera `# generado por bot_genesis`.
- Una receta escrita a mano (sin esa cabecera) no la pisa nadie.

Esquema completo y JSONPath soportado: en el docstring de `04_Config/scripts/bot_runner.py`.

```yaml
name: dexpaprika                # [a-z0-9_]{3,33}; no puede usar la carpeta de otro bot (rss, telegram, ...)
kind: json_api                  # rss | html_list | json_api | telegram_preview
url_base: https://api.dexpaprika.com/networks/solana/pools/search?limit=50&order_by=created_at&sort=desc
cadencia_min: 30                # >= 10
grupo: a
extractores:
  - items: "$.results[*]"       # JSONPath (json_api) o selector CSS (html_list)
  - id: "$.id"
  - title: "$.dex_name"
  - ts: "$.created_at"
  - text: ["$.tokens[*].id", "$.tokens[*].symbol"]   # solo para extraer direcciones/cashtags/keywords
  - meta.volume_usd_24h: "$.volume_usd_24h"
```

La salida va a `02_Analisis/sources/<name>/<fecha>.jsonl` (src-1), junto con `_state.json`, `_audit.jsonl` y `_metrics.json`. El orquestador la incluye en `_merged.jsonl` como a cualquier otro bot.
