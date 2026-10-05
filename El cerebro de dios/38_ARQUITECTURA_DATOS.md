---
owner: Claude Code (Claude1) — pendiente auditoría YANG
status: DISEÑO + fase 1 (D-101: retención, preventa vs venta, falsos positivos) + módulos autónomos (D-105: lib_paths y libs de dominio)
last_updated: 2026-10-05
version: 0.2
relacionados: doc 34 (sistema multi-bot), doc 34 §17 / 02_Analisis/patrimonio (inventario), doc 35 (traspaso)
---

# 38 — Arquitectura de datos: separación estricta por categoría

Rótulos: [V] verificado en el repo · [I] inferido · [H] hipótesis · [P] pendiente.

Principio de Dirección (D-101): **cada dato vive en una sola categoría, con un solo dueño, y lo numérico no se mezcla
con lo escrito.**

## 1. Las 8 categorías

| Categoría (nombre lógico) | Qué guarda | Retención | Ruta física HOY [V] |
|---|---|---|---|
| `01_datos_crudos_numericos` | Mediciones de mercado: precios, liquidez, volumen, velas, scores y señales numéricas | por carpeta (§2) | `02_Analisis/multichain/`, `early/`, `shadow_v4/`, `datasets/`, `signals/`, `macro/`; crudos en `01_Datos_Crudos/` |
| `02_informacion_escrita` | Lo que se dice de un activo, reducido a identificadores: ítems `src-1` (direcciones, cashtags, keywords, hash, título ≤ 160) | 7 días | `02_Analisis/sources/<bot>/`, `narrative/` |
| `03_patrimonio` | Lo que el sistema hizo y cómo le fue: alertas, dossiers emitidos, resultados, hipótesis, dataset histórico | **sin poda** | `02_Analisis/alerts/`, `dossiers/`, `hypotheses/`, `datasets/historical_alerts.jsonl`, `operations/` |
| `04_tmp` | Estado intermedio y logs de ejecución: `_state.json`, `_audit*.jsonl`, `_merged.jsonl`, `_index.json`, cachés, dumps | 7 días (o tope propio) | dentro de cada carpeta de bot (archivos con `_` adelante) |
| `05_contexto` | Historia larga que un bot necesita para evaluar: publicaciones de X (30 d de ventana), memoria episódica | 35 días | `02_Analisis/sources/x_influencers/` (fix A), `sources/_episodes_*.jsonl` |
| `06_eventos` | Avisos entre bots (`lib_events`), con TTL | 8 días (la poda la hace cada escritor) | `02_Analisis/events/<writer>/` |
| `07_prelaunch` | Activos no nacidos: calendario, precios de preventa y de venta, nacimiento | sin poda del calendario; purga lógica a 72 h / 30 d | `02_Analisis/prelaunch/` |
| `_archivo` | Lo que ya no tiene escritor | sin poda | `02_Analisis/_archivo_2026_Q3/` |

### Por qué no se mueven las carpetas ahora (técnicamente viable, pero no en un solo paso)

Mover las rutas físicas a `01_…/07_…` sí se puede. El riesgo concreto es este:
- Hay ~20 escritores vivos. Early watch corre loops de 40 min y el bot de Telegram también.
- Un job que arrancó **antes** del merge sigue con el código viejo. Al terminar pushea a la ruta vieja, y el `pull --rebase` lo acepta: la carpeta vieja reaparece y los datos quedan partidos en dos lugares.
- Además se mueven estados con memoria (cursores de eventos, `seen`, claims por mint). Si se mueven mal, se pierde el dedup y se re-emiten alertas.

**Alternativa (fase 1, hecha en D-101):**
1. **La categoría es un atributo, no una carpeta.** `_inventario.json` (doc 34 §17) ya asigna cada ruta a una categoría y a un dueño. Este doc fija las 8 categorías y la tabla de §4.
2. **La retención va por archivo `_retention.yaml`** en cada carpeta (§2). Es lo que separa en la práctica "temporal" de "contexto" de "patrimonio", sin mover nada.

**Fase 2 (propuesta, [P] Dirección):** migración física, carpeta por carpeta.
1. Primero, `lib_paths.py`: una sola tabla de rutas que importan todos los scripts. **Hecho en D-105** para los 6 scripts críticos (§6).
2. Después, por cada carpeta, en una ventana con su workflow desactivado:
   - `git mv` de la carpeta;
   - un cambio en `lib_paths`;
   - una corrida manual de prueba;
   - reactivar el workflow.
3. Una carpeta por PR. Nunca todas juntas.

## 2. Retención: `_retention.yaml` por carpeta

```yaml
# 02_Analisis/sources/x_influencers/_retention.yaml
categoria: 05_contexto
keep_days: 35          # cubre historia_dias = 31 del bot (ventana de evaluación de 30 d)
motivo: "ventana de evaluación de cuentas de X (D-089-R/D-091)"
```

| Clave | Uso |
|---|---|
| `keep_days` | entero ≥ 1. Los diarios `<YYYY-MM-DD>*.jsonl` más viejos se podan |
| `keep_days: null` | sin poda (patrimonio, archivo) |
| `categoria`, `motivo` | informativos; los lee `lib_patrimonio` |

**Regla de resolución.** Para cada diario se usa el `_retention.yaml` más cercano, subiendo desde su carpeta hasta
`02_Analisis/`. Si no hay ninguno, rige el default del orquestador (7 días). Lo implementa
`bot_orchestrator.retention_for()` y lo cubren los tests de D-101.

Archivos de retención creados en D-101:
- `02_Analisis/sources/_retention.yaml`: 7 días;
- `02_Analisis/sources/x_influencers/_retention.yaml`: 35 días.

Las carpetas fuera de `sources/` ya tienen su política en el dueño:
- eventos: 8 días, `lib_events.prune`;
- auditoría: 90 días, `lib_audit`;
- patrimonio: nadie poda.

## 3. Reglas

1. **Un solo dueño por archivo.**
   - Un archivo lo escribe un solo workflow. Si hay dos instancias, cada una escribe el suyo (`_a` / `_b`).
   - Un workflow commitea solo sus rutas, con `git add -- <ruta>` y nunca `git add -A`. `audit_gate` debe rechazar el `-A` sin ruta (pendiente de D-072).
   - Excepción conocida [V]: el reparador puede renombrar o recortar el `_state.json` de otro bot. Es el único caso de dos escritores y queda acotado a archivos corruptos o inflados.
2. **Lo numérico y lo escrito nunca van en el mismo archivo.**
   - *Escrito*: texto natural o derivado de texto (título, extracto, keywords, cashtags).
   - *Numérico*: medición de mercado (precio, liquidez, volumen, market cap, variación, score).
   - Los contadores que describen al propio ítem escrito (vistas, likes, respuestas) son metadata del ítem y pueden quedarse.
   - Violación conocida [V]: la receta `dexpaprika` guarda `meta.liquidity_usd` y `meta.price_change_*` en `sources/dexpaprika/` (informativo). Fix propuesto [P]: una clave `salida: numerico` en la receta. El runner separaría los campos de mercado a un archivo hermano `<fecha>.num.jsonl`, o a `multichain/`.
3. **El patrimonio no se poda y no se reescribe.** Solo se agregan líneas o archivos nuevos. Las correcciones van como registro nuevo con `corrige: <id>`.
4. **Toda ruta nueva de primer nivel se anota en `_inventario.json` en el mismo commit.** Lo controla `test_lib_patrimonio` [V].
5. **Lo temporal se nombra con `_` adelante** (`_state`, `_audit`, `_merged`, `_index`, `_cache`). Nunca se lo lee como patrimonio.

## 4. Quién escribe y quién lee

| Ruta (categoría) | Escribe (único) | Lee |
|---|---|---|
| `multichain/` (01) | `multichain_scanner.yml` (script_114) | script_97 (emisión multi-chain), dossier |
| `early/` (01) | early_watch a/b (script_116), early_review (`_gate.json`) | script_97 (hand-off), early_review, young_watch_analysis |
| `shadow_v4/` (01) | pipeline_t0 (script_82) | script_97, script_115, script_116 |
| `datasets/` (01/03) | datasets_build, lib_persist | calibración, latency_analysis |
| `sources/<bot>/` (02) | cada bot de fuentes y recetas del runner | orquestador (merge), script_116 y script_97 vía `lib_sources_store.query` |
| `sources/x_influencers/` (05) | bot_influencer_tracker | el propio bot (evaluación de 30 d), orquestador |
| `sources/_merged.jsonl`, `_index.json`, `_health.json`, `_graph.json` (04) | bot_orchestrator | consumidores de `query()`, reparador |
| `sources/_repair_*`, `_episodes_self_repair.jsonl` (04/05) | bot_self_repair | bots (auto_off), lib_episodic_memory |
| `events/<writer>/` (06) | un escritor por subcarpeta (`lib_events`) | consumidores con cursor propio (`events/_cursors/`) |
| `narrative/` (02) | narrative_collector (script_115) | script_116 (menciones) |
| `prelaunch/` (07) | sources_prelaunch (bot_prelaunch_calendar) | script_97 (`prelaunch_lookup`) |
| `alerts/`, `dossiers/` (03) | pipeline_t0 (script_97, script_113), trust_update (script_98) | script_98, early_review, datasets |
| `hypotheses/` (03) | lib_scientific_method | lib_adversarial_debate, auditoría |
| `operations/`, `diagnostics/` (03/04) | lib_persist y cada bot de diagnóstico, en su archivo | auditoría, daily_summary |

## 5. Los 3 fixes de D-101

### Fix A — Capas temporal / contexto / patrimonio [implementado]

- **Problema [V, D-096 crítico 1].** El orquestador podaba todo `sources/*/<fecha>.jsonl` a los 7 días. Eso incluía `x_influencers/`, cuyo bot necesita 31 días: la métrica de 30 d medía como mucho 7, y los posts de 7 a 30 d se volvían a registrar como nuevos.
- **Fix:**
  - `prune()` pasa a usar la retención resuelta por `_retention.yaml` (§2);
  - `x_influencers` queda en 35 días;
  - el resto de `sources/` sigue en 7.
- **Tests:**
  - el diario de `x_influencers` de 20 d sobrevive y el de `rss` de 20 d se poda;
  - el de 36 d en `x_influencers` se poda;
  - `keep_days: null` no poda;
  - un YAML roto cae al default.

### Fix B — Precio de preventa vs precio de venta [implementado]

| Campo | Fuente | Qué es |
|---|---|---|
| `precio_preventa` | **solo** perps de preventa de Hyperliquid y Aevo | precio de mercado real antes de nacer |
| `precio_venta` | CoinMarketCap, ICO Drops | precio fijo de la ronda (ICO/IDO) |
| `precio_apertura` | primer precio en DEX/CEX después de nacer | apertura |
| `delta_preventa_apertura_pct` | solo si hay `precio_preventa` real | (apertura / preventa − 1) × 100 |
| `delta_venta_apertura_pct` | si hay `precio_venta` | (apertura / venta − 1) × 100. Campo aparte: no se confunde con el anterior |

- **Antes [V]:** si no había perp, el precio de venta se copiaba a `precio_preventa`.
- **Ahora:** nunca se copia.
- **Migración de calendarios viejos:** al cargar, si `precio_preventa_fuente` es CMC o ICO Drops, el valor pasa a `precio_venta` (si faltaba) y `precio_preventa` queda vacío.
- **script_97:** muestra "precio preventa" solo si es real; si solo hay venta, muestra "precio de venta (ICO)".

### Fix C — Filtros de falsos positivos del aporte de cuentas de X [implementado]

| Capa | Regla | Efecto |
|---|---|---|
| 1. Ticker | Un ticker cuenta solo si tiene ≥ 3 caracteres en mayúscula, prefijo `$` o `#`, no es un mayor ni una sigla de la lista de exclusión, y coincide con un activo vigente (calendario, alertas, scanner multi-chain, perps de Hyperliquid, watchlists del early watch). | El tipo "anuncio" deja de contar tickers no vigentes ("launching our podcast ($ABC)" ya no aporta). Costo [V en tests]: "(HNT)" o "HYPE" sin prefijo ya no cuentan, aunque sean vigentes |
| 2. Sector | Una keyword sectorial solo cuenta junto a la mención de un activo vigente en el mismo post | (regla ya presente en D-091; ahora con test explícito) |
| 3. Dedup | sha256 del texto **normalizado** (minúsculas, sin URLs, espacios colapsados): el mismo texto con otro link o mayúsculas es un solo post | Un repost o una publicación cruzada no suma aporte dos veces |

- **Muestra etiquetada:** `02_Analisis/sources/x_influencers/_falsos_positivos.jsonl`. Son casos sintéticos con etiqueta y motivo (12 líneas) y sirven de regresión.
- **Cuándo se cambia:** la muestra real la etiqueta Yang a medida que el bot corre [P]. Los umbrales siguen [H] hasta tener esa muestra.
- **Tests:** 6, dos por capa.

## 6. Módulos autónomos (D-105)

Principio de Dirección: **cada módulo es autónomo; ninguna falla arrastra a otra.** Ningún módulo depende de la ruta
física de otro: todos dependen de una interfaz común.

### Reglas

1. **Ningún módulo arma la ruta de otro.** Todos importan `lib_paths` y piden una clave:
   - `P.path("alerts.all", root)` para leer o escribir;
   - `P.rel("early.watch", inst="a")` para las listas de `git add`.
   La tabla `PATHS` es la única que contiene el prefijo de datos. Mover una carpeta es cambiar una línea de `PATHS`,
   y lo prueban los tests de `test_modulos_autonomos` (§ abajo).
2. **Cada dominio tiene su lib con contrato de esquema.** Los scripts críticos no leen esos archivos con `open()` ni con
   `path()` directo: llaman a la lib. Si cambia el esquema, se cambia la lib y los consumidores no se tocan.

   | Lib | Dominio | API | Contrato |
   |---|---|---|---|
   | `lib_alerts` | `alerts/` | `read_alerts`, `write_alerts`, `write_alert`, `read_detail`, `write_detail`, `write_trust` | `SCHEMA_VERSION = alerts-1`. La lista vive en `_all_alerts.json`. Ilegible → `CorruptAlertsError`: el emisor no pisa el historial |
   | `lib_early_watch` | `early/` | `read_watch`, `write_watch`, `read_signals`, `write_signals`, `rel_*` | `early-watch-1`, un archivo por instancia |
   | `lib_sources_domain` | `sources/` | `read_sources`, `write_sources`, `read_state`, `write_state` | `src-1` (doc 34 §4) |

3. **Ningún test fija rutas literales.** Todos usan una `SHOT_ROOT` temporal y le piden las rutas a `lib_paths`.
   `lib_paths.root()` lee `SHOT_ROOT` en cada llamada (no al importar), y por eso un test puede cambiarla.
4. **Lectura tolerante en los consumidores, estricta en el dueño.**
   - Un consumidor (early watch, early_review) que encuentra un archivo ajeno roto o ausente sigue con vacío.
   - El dueño (script_97 sobre `_all_alerts.json`) se detiene antes de pisar un historial ilegible.

### Interfaz (`04_Config/scripts/lib_paths.py`, `paths-1`)

| Función | Qué hace |
|---|---|
| `root()` | Raíz del repo: `SHOT_ROOT` o la ubicación del archivo |
| `path(key, root=None, **fmt)` | Devuelve un `Path`. Con una clave desconocida o un campo de plantilla faltante, `KeyError` explícito |
| `path_str(key, ...)` | Lo mismo, como `str` |
| `rel(key, **fmt)` | Ruta relativa al repo, para `git add` |
| `register(key, rel, kind, pending)` | Un módulo agrega sus rutas propias. Repetir la misma ruta es idempotente; otra ruta para la misma clave es `ValueError` |
| `validate(root)` | Lista las claves que no existen y no están marcadas `pending_creation`. Hoy, sobre el repo, da 0 |

Dominios cubiertos: alerts, early, multichain, narrative, sources, events, prelaunch, patrimonio, diagnostics,
shadow_v4, dossiers, datasets, operations.

### Estado de la migración [V]

- **Rutas literales con el prefijo de datos fuera de docstrings y comentarios:**
  - en los 6 scripts críticos (script_97, script_98, script_116, bot_orchestrator, early_review, bot_prelaunch_calendar), más las libs de dominio y `lib_sources_store`: **0** (antes, 28 en los 6 scripts);
  - en todo el código de producción: de 146 a 117.
  - Lo que queda está en scripts todavía no migrados; la mayoría no tiene workflow (doc 04).
- **Compuerta:** `audit_gate prohibited` incluye el chequeo de rutas literales.
  - En los módulos migrados (`MODULOS_AUTONOMOS`) exige cero en todo el archivo.
  - En el resto aplica un trinquete: no se pueden **sumar** rutas literales en líneas nuevas.
  - Excepciones: docstrings, comentarios, YAML, tests y `lib_paths.py`.
- **Tests:** `test_modulos_autonomos.py` (12).
  - Cada script crítico corre con `SHOT_ROOT` vacía.
  - Un `_all_alerts.json` roto no frena al early watch ni a early_review.
  - Mover alertas, early watch y fuentes no requiere editar los scripts.
  - La compuerta detecta rutas literales y respeta sus excepciones.

## 7. Pendientes [P]

- Fase 2 de §1: migración física por carpeta (Dirección decide). `lib_paths` ya está (§6).
- Migrar a `lib_paths` los scripts restantes que corren en workflows (script_114, script_115, bot_runner, bots de fuentes, early watch helpers): hoy los ataja el trinquete de la compuerta.
- Regla 2: separar la salida numérica de las recetas (`dexpaprika`).
- `audit_gate`: rechazar `git add -A` sin ruta y gitlinks (D-072, medio 2).
- Muestra real etiquetada de falsos positivos (Yang).
