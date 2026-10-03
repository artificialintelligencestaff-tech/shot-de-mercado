---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: DISEÑO COMPLETO (D-033, D-035) — implementado: lib_sources_store, bot_rss_news, bot_orchestrator, 2 workflows, query() en script_116/script_97
last_updated: 2026-10-03
version: 0.2
reemplaza: doc 33 §2–§5 (el doc 33 queda como investigación de fuentes)
---

# 34 — Sistema multi-bot de fuentes: 7 bots + lib_sources_store

Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente (lo verifica YIN o una corrida en Actions).

Objetivo: alimentar las señales informacionales del scorer joven (doc 32: `mentions`, `narrative_wave`,
`trending_match`) y del bono v7.2.2 con un solo almacén consultable. Hoy la única materia prima es
`02_Analisis/narrative/_items.json` de script_115 (Reddit RSS, 4 canales de Telegram, 4chan, HN, 4 RSS).

## 1. Imposibilidades técnicas reales (no de riesgo)

| # | Lo pedido | Por qué no se puede tal cual | Cómo queda en el diseño |
|---|---|---|---|
| 1 | El orquestador "instancia workflows desde plantilla" | El `GITHUB_TOKEN` de Actions no puede crear ni modificar archivos en `.github/workflows/` (le falta el permiso `workflows`, y no se puede otorgar desde el YAML) [V, documentación de GitHub]. | La plantilla se instancia **una vez, al autorar** (`make_source_workflow.py`, lo corre Claude y se commitea). Sumar una **fuente** = una línea en el YAML del bot, sin workflow nuevo. Sumar un **bot** nuevo = un commit con su workflow. El orquestador solo dispara (`workflow_dispatch` vía API, permitido con `actions: write`). |
| 2 | Orquestador "cada 5 min" | El cron de Actions acepta `*/5`, pero es best-effort: el desfase medido en este repo es ~11,9 min [V, latency_analysis]. | Cron `*/5`; frecuencia real esperada 10–15 min. Ninguna lógica depende de que sean 5. |
| 3 | Telegram "job largo, no cron" | Algo tiene que arrancar el job. Actions no tiene procesos persistentes; un job dura como máximo 6 h. | Igual que early watch: 2 instancias (a, b) arrancadas por cron, cada una con un loop de 40 min. Se solapan 10 min: cubren el desfase. |
| 4 | 4chan /biz/ vía `archive.4plebs.org` | 4plebs no archiva /biz/ (archiva /pol/, /tv/, /x/, /tg/, /sp/, /s4s/, /adv/, /f/, /hr/, /o/, /trv/) [I]. El archivo de /biz/ es `warosu.org/biz` [I]. | Fuente principal: la API oficial `a.4cdn.org/biz/catalog.json` (ya da 200 desde Actions [V, sonda 01/10]). Warosu solo para backfill histórico. |
| 5 | DEXTools comments, Solscan comments | DEXTools está detrás de Cloudflare con desafío JS y los comentarios se cargan por una API interna autenticada [H]. Solscan no tiene comentarios públicos de tokens que se puedan leer sin login [H]. Sin navegador real no se leen. | Quedan en el YAML con `enabled: false` y `requires_js: true`. Verificación [P] para YIN. Si se confirma, se reemplazan (P-13) por `frontend-api.pump.fun/replies/<mint>` [P] y Bitcointalk. |
| 6 | Canales `solana` y `dexscreener` de Telegram | No tienen vista previa pública: `t.me/s/<canal>` redirige [V, sonda 01/10]. | Fuera de la lista inicial. Los 15 canales pasan por la sonda; el que no da vista previa se desactiva solo y se reporta. |
| 7 | Reddit por RSSHub público | RSSHub corre en datacenter: Reddit lo bloquea igual que a Actions [I]. | Queda como 3.ª opción tras PullPush y Arctic Shift (doc 33 §8). La única fuente estable sigue siendo OAuth oficial (necesita 2 secrets de Dirección) [P]. |

Lo demás es factible tal como está pedido.

## 2. Diagrama de flujo

```
                          04_Config/sources/*.yaml  (1 config por bot; sumar fuente = sumar línea)
                                        │
   ┌───────────────┬───────────────┬────┴──────────┬───────────────┬───────────────┐
   ▼               ▼               ▼               ▼               ▼               ▼
bot_rss_news  bot_telegram_   bot_web_       bot_github_     bot_x_nitter   bot_forum_
 (20 min)     public a/b      scraper         trending        (20 min)       scraper
              (loop 40 min)   (30 min)        (6 h)                          (1 h)
   │               │               │               │               │               │
   ▼               ▼               ▼               ▼               ▼               ▼
sources/rss/  sources/telegram/ sources/web/  sources/github/ sources/x/   sources/forums/
<fecha>.jsonl <fecha>_<a|b>.jsonl <fecha>.jsonl <fecha>.jsonl <fecha>.jsonl <fecha>.jsonl
   + _state.json por bot (dedup local, cursores, salud de cada fuente)
   └───────────────┴───────────────┴───────┬───────┴───────────────┴───────────────┘
                                           ▼
                     bot_orchestrator (cada 5 min; frecuencia real 10–15 min)
                     ├─ lib_sources_store.merge() → sources/_merged.jsonl (48 h) + _index.json
                     ├─ salud por bot → sources/_health.json  (+ dispatch de recuperación)
                     ├─ poda: borra <fecha>.jsonl con más de 7 días (queda en el historial de git)
                     └─ _servicios_open_source/_INSTALADOS.md (bloque automático, solo si cambia)
                                           │
                                           ▼
                     lib_sources_store.query(keyword) ──► script_116 (scorer joven: mentions,
                                                          narrative_wave) · v7.2.2 (bono +10)
```

## 3. Tabla de bots

| Bot | Fuente | Cadencia (cron) | Output | Depende de | Workflow |
|---|---|---|---|---|---|
| `bot_rss_news` | 12 feeds: Bitcoin Magazine, CryptoSlate, BeInCrypto, DL News, Blockworks, Messari, Cointelegraph tag memecoin y tag solana, Google News ×4 | 20 min (`3,23,43 * * * *`) | `sources/rss/<fecha>.jsonl` | red | `sources_rss.yml` **[implementado]** |
| `bot_telegram_public` | 15 canales vía `t.me/s/<canal>` | 2 instancias, loop de 40 min, poll cada 4 min (a `5 * * * *`, b `35 * * * *`) | `sources/telegram/<fecha>_<inst>.jsonl` | red; sonda de vista previa | `sources_telegram_a.yml`, `_b.yml` |
| `bot_web_scraper` | Plantilla YAML: Bitcointalk; DEXTools y Solscan desactivados (§1 #5) | 30 min (`11,41 * * * *`) | `sources/web/<fecha>.jsonl` | red; `beautifulsoup4` (MIT) | `sources_web.yml` |
| `bot_github_trending` | `github.com/trending` (HTML) + Search API por topic: crypto, solana, defi, memecoin, depin, rwa | 6 h (`17 */6 * * *`) | `sources/github/<fecha>.jsonl` | red; `GITHUB_TOKEN` (30 req/min en búsqueda) | `sources_github.yml` |
| `bot_x_nitter` | Pool de instancias de Nitter elegido desde `status.d420.de`; cuentas en YAML | 20 min (`9,29,49 * * * *`) | `sources/x/<fecha>.jsonl` | red; health check | `sources_x.yml` |
| `bot_forum_scraper` | API oficial de 4chan /biz/; Reddit: PullPush → Arctic Shift → RSSHub | 1 h (`25 * * * *`) | `sources/forums/<fecha>.jsonl` | red | `sources_forums.yml` |
| `bot_orchestrator` | Lee `_bots.yaml`, el `_state.json` de cada bot y las corridas de Actions | 10 min (`*/10 * * * *`, real ~15; D-035) | `sources/_merged.jsonl`, `_index.json`, `_health.json`, bloque en `_INSTALADOS.md` | **todos los bots** + `lib_sources_store` | `sources_orchestrator.yml` **[implementado]** |
| `lib_sources_store` (librería) | Todos los `sources/*/<fecha>*.jsonl` | la llama el orquestador; consulta bajo demanda | `_merged.jsonl`, `_index.json` | outputs de los bots | — **[implementado]** |

Minutos de cron elegidos para no coincidir con el pipeline ni con early watch (`:07/:37`, `:22/:52`), ni con
script_115 (`:07/:27/:47`). El repo es público: los minutos de Actions no tienen tope [V].

## 4. Esquema de datos unificado (`src-1`)

Una línea JSON por ítem, igual para los 7 bots:

```json
{"v": "src-1", "bot": "rss", "src": "cointelegraph_solana", "kind": "news",
 "id": "https://cointelegraph.com/news/…", "url": "https://cointelegraph.com/news/…",
 "ts": 1790900000, "seen": 1790900420,
 "title": "Solana memecoin … (≤160 caracteres)",
 "a": ["9BB6…pump"], "c": ["WIF"], "k": ["memecoin", "solana"],
 "h": "3f2a9c1e0b7d4a55", "au": null, "m": {}}
```

| Campo | Contenido |
|---|---|
| `v` | versión del esquema |
| `bot` / `src` | bot que lo generó / fuente dentro del bot (nombre del YAML) |
| `kind` | `news` · `message` (Telegram) · `post` (foros, web) · `repo` (GitHub) · `tweet` (X) |
| `id`, `url` | id nativo y enlace |
| `ts` | publicación (epoch UTC); `null` si la fuente no la da |
| `seen` | momento en que el bot lo leyó; mide la latencia de cada fuente |
| `title` | titular, asunto del hilo o nombre del repo, ≤160 caracteres. En `message` y `tweet`: `null`. |
| `a`, `c`, `k` | direcciones (base58 / 0x), cashtags y palabras clave de `04_Config/sources/keywords.yaml` encontradas en el texto |
| `h` | hash del texto normalizado (16 hex) |
| `au` | hash con sal del autor (la misma sal que script_115), o `null` |
| `m` | metadatos propios del bot: `stars` y `pushed_at` en GitHub, `instance` en Nitter, `channel_views` en Telegram |

**El cuerpo del texto no se guarda.** Se queda solo con lo que el scorer consume: identificadores, palabras clave
y hash. Es la misma política de script_115 (doc 26) y mantiene acotado el crecimiento del repo:
- ~150–250 bytes por ítem;
- estimado [H]: 5.000–15.000 ítems/día entre los 7 bots, o sea 1–4 MB/día;
- con la poda a 7 días, ≤30 MB en el árbol de trabajo.

Compatibilidad: `to_items_store()` convierte a la forma de `_items.json` (`{"ts", "a", "c", "f"}`). Así
`lib_info_signals.mentions` lo lee sin cambios.

## 5. Config YAML por bot

Todos los configs en `04_Config/sources/`. Claves comunes en todas las fuentes:
- `name`: único dentro del bot;
- `enabled`;
- `url`;
- `kind`;
- `pause_s`: pausa antes de la request.

El bot ignora claves que no conoce.

```yaml
# rss.yaml  [implementado]
bot: rss
dedup_hours: 72
feeds:
  - {name: cointelegraph_solana, url: "https://cointelegraph.com/rss/tag/solana", enabled: true}
  - {name: gnews_pumpfun, url: "https://news.google.com/rss/search?q=pump.fun&hl=en-US&gl=US&ceid=US:en"}

# telegram.yaml
bot: telegram
loop_minutes: 40
poll_minutes: 4
channels: [whale_alert_io, cointelegraph, WatcherGuru, pumpfun, SolanaNews, DexToolsAlerts, BinanceKillers,
           CryptoCom, memecoins, PepeWorld, coin_alert]   # + 2 que verifica YIN; solana/dexscreener fuera (§1 #6)

# web.yaml — la plantilla clave: sumar fuente = sumar un bloque
bot: web
sources:
  - name: bitcointalk_altcoins
    url: "https://bitcointalk.org/index.php?board=159.0"     # Announcements (Altcoins)
    item: "td.windowbg span[id^=msg_] a"                     # selector CSS de cada ítem
    fields: {title: "text", url: "href"}
    kind: post
    pause_s: 2
  - {name: dextools_comments, url: "https://www.dextools.io/…", enabled: false, requires_js: true}
  - {name: solscan_comments, url: "https://solscan.io/…", enabled: false, requires_js: true}

# github.yaml
bot: github
topics: [crypto, solana, defi, memecoin, depin, rwa]
min_stars: 50
max_commit_age_days: 30
trending_page: true

# x.yaml
bot: x
status_page: "https://status.d420.de/"
max_instances: 3
accounts: []            # configurable por Dirección / YIN
stale_hours: 24         # si ninguna instancia da contenido fresco en 24 h: no escribe y lo reporta

# forums.yaml
bot: forums
sources:
  - {name: 4chan_biz, url: "https://a.4cdn.org/biz/catalog.json", parser: 4chan}
  - {name: pullpush_solana, url: "https://api.pullpush.io/reddit/search/submission/?subreddit=solana&size=100", parser: pullpush}
  - {name: arcticshift_solana, url: "https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=solana&limit=100", parser: arcticshift}
  - {name: rsshub_solana, url: "https://rsshub.app/reddit/subreddit/solana", parser: feed, enabled: false}

# _bots.yaml (lo lee el orquestador)
bots:
  rss:      {workflow: sources_rss.yml,        every_min: 20,  stale_min: 60}
  telegram: {workflow: sources_telegram_a.yml, every_min: 30,  stale_min: 90}
  web:      {workflow: sources_web.yml,        every_min: 30,  stale_min: 120}
  github:   {workflow: sources_github.yml,     every_min: 360, stale_min: 780}
  x:        {workflow: sources_x.yml,          every_min: 20,  stale_min: 1440}
  forums:   {workflow: sources_forums.yml,     every_min: 60,  stale_min: 180}
```

Las palabras clave están en `keywords.yaml` (grupos a–i: memecoin, presale, governance, synthetic, depin, l1/l2,
rwa…). Las comparten todos los bots y `query()`.

## 6. Storage por bot (un dueño por archivo)

| Ruta | Dueño | Retención |
|---|---|---|
| `02_Analisis/sources/<bot>/<YYYY-MM-DD>.jsonl` | ese bot (append) | 7 días; poda el orquestador |
| `02_Analisis/sources/telegram/<fecha>_<a\|b>.jsonl` | cada instancia | 7 días |
| `02_Analisis/sources/<bot>/_state.json` | ese bot | rodante: claves vistas de 72 h y salud de cada fuente |
| `02_Analisis/sources/_merged.jsonl`, `_index.json` | orquestador (vía `lib_sources_store`) | 48 h rodantes |
| `02_Analisis/sources/_health.json` | orquestador | última corrida + historial de 24 h |

Cada workflow commitea **solo su carpeta**, con el loop `pull --rebase` + 4 reintentos de los workflows actuales.
Como ningún archivo tiene dos dueños, el rebase no puede chocar. Tampoco hay `--force`.

## 7. Dependencias

- **Bots de captura:** no dependen entre sí, solo de la red y de su YAML. Si uno se cae, los demás siguen.
- **`lib_sources_store`:** depende solo de los archivos de los bots. Si `_merged.jsonl` tiene más de 15 min,
  `query()` lo reconstruye en memoria desde los diarios (no depende del orquestador para responder).
- **`bot_orchestrator`:** depende de todos. Es el único que escribe `_merged.jsonl`, `_index.json` y
  `_health.json`.
- **Consumidores:**
  - `script_116` (scorer joven) usa `query()` además de `_items.json` de script_115;
  - v7.2.2 usa `query()` para el bono informacional;
  - script_115 sigue igual hasta que el almacén nuevo lo cubra (después se decide si se retira, P-13).

## 8. Orquestador: salud y recuperación

- **Por bot**, desde su `_state.json`:
  - `last_run`, `items_last_run`, fuentes OK / fallidas.
- **Estado**, comparando contra `_bots.yaml`:
  - `ok`: corrió dentro de `stale_min` y trajo ítems;
  - `vacío`: corrió sin ítems 3 veces seguidas;
  - `atrasado`: no corre desde hace más de `stale_min`;
  - `caído`: 3 fallas seguidas.
- **Recuperación ante `atrasado`** (no está en orch-0.1; la hace `bot_self_repair` §11): una sola corrida por `workflow_dispatch`, con `actions: write`.
  - El intento queda registrado en `_health.json`.
  - No reintenta en loop: un segundo atraso solo se reporta.
- **`_INSTALADOS.md`:** el orquestador reescribe solo el bloque entre `<!-- AUTO:sources -->` y
  `<!-- /AUTO:sources -->`, y solo si cambió algún estado. Así no commitea cada 5 min. Lo que escribe YIN fuera
  del bloque no se toca.
- **No genera código.**

## 9. Plan de tests (todos sin red; fixtures sintéticos)

| Componente | Tests |
|---|---|
| `lib_sources_store` | esquema `make_record` (campos, truncado del título, extracción de a/c/k); dedup global (`src`, `ts`, `h`); merge con ventana de 48 h; índice; `query` por dirección, cashtag y palabra clave, ordenado por recencia; reconstrucción con `_merged` viejo; `to_items_store` compatible con `lib_info_signals.mentions` **[hecho]** |
| `bot_rss_news` | parseo RSS y Atom; dedup por título + URL dentro de la corrida y entre corridas; fuente caída que no corta las demás; `_state` con salud por feed; config inválida; `--dry-run` no escribe **[hecho]** |
| `bot_telegram_public` | parser de la vista previa (reutiliza `lib_repetition.parse_telegram_preview`); canal sin vista previa → se desactiva; cursor por `data-post`; dos instancias que no duplican en el merge |
| `bot_web_scraper` | plantilla: selector, campos y `requires_js` → saltada; fuente nueva solo por YAML (test que agrega una fuente sin tocar código) |
| `bot_github_trending` | filtros de estrellas >50 y commit <30 días; parser de la página trending; respeto del límite de requests |
| `bot_x_nitter` | parser de `status.d420.de`; selección de instancias sanas; regla de 24 h sin datos frescos → no escribe y reporta |
| `bot_forum_scraper` | parsers de 4chan, PullPush, Arctic Shift y feed; cadena de respaldo de Reddit |
| `bot_orchestrator` | estados ok / vacío / atrasado / caído con reloj falso; un solo dispatch por atraso; bloque AUTO de `_INSTALADOS.md` idempotente; poda a 7 días |
| Workflows | cada YAML carga; el cron es válido; el script existe; `git add` solo de su carpeta |

## 10. Orden de implementación

1. `lib_sources_store` + `bot_rss_news` + `sources_rss.yml` **[hecho en D-033]**.
2. `bot_orchestrator` **[hecho en D-035]**.
3. `bot_forum_scraper` y `bot_telegram_public`: reutilizan los parsers de `lib_repetition`, con poco código nuevo.
4. `bot_github_trending`, `bot_web_scraper`, `bot_x_nitter`: este último es el más frágil.
5. `query()` en `script_116` (`mentions`) y en `script_97` (campos informativos `sources_mentions_*` para tokens ≥ 60 min) **[hecho en D-035]**. Falta que el bono de v7.2.2 los use.
6. `bot_self_repair` (§11).

## 11. bot_self_repair (D-035, diseño; sin implementar)

**Qué hace.** Corre cada 30 min (`19,49 * * * *`). Lee `_health.json`, el `_state.json` de cada bot y las
últimas corridas de cada workflow (API de Actions, `GITHUB_TOKEN` con `actions: write`). Solo aplica reglas
explícitas: **cero IA generativa en producción**. Lo que no está en la tabla no lo toca: lo escala.

| Detección | Señal | Fix conocido | Límite |
|---|---|---|---|
| Feed o fuente caída | `status != 200` en 3 corridas seguidas | `enabled: auto_off` en `_state.json`; el bot la salta 6 h y después reintenta una vez. **No edita el YAML**: el YAML es de Claude y YIN. | Si 24 h después sigue caída: escala [P] (P-13: reemplazarla) |
| Workflow fallido recurrente | ≥2 fallas seguidas (`conclusion: failure`) | 1 re-run del job fallido (`POST /actions/runs/{id}/rerun-failed-jobs`) | 1 re-run por falla; la 2.ª falla se escala con el log del paso |
| Bot atrasado | `atrasado` en `_health.json` | 1 `workflow_dispatch` | 1 por atraso; un atraso repetido en 24 h se escala |
| Archivo corrupto | `_state.json` o `_health.json` que no parsea; JSONL con líneas que no parsean | `_state.json`: se renombra a `.corrupt-<ts>` y el bot arranca con estado vacío (solo pierde el dedup de 72 h). JSONL: se reescribe sin las líneas rotas, y las rotas se guardan en `.rejected`. | Más de 1 por día en el mismo archivo: escala |
| Output vacío anómalo | `vacío` con fuentes OK: los feeds responden 200 pero el parser da 0 ítems en 3 corridas (cambió el formato) | Ninguno: un parser roto no se repara con reglas | Escala de inmediato |
| Caché o estado inflado | `seen` con más de 50.000 claves, o `_state.json` de más de 5 MB | Recorta `seen` a la ventana `dedup_hours` | — |

**Escalado.** Una fila en el bloque `<!-- AUTO:repair -->` de `_INSTALADOS.md` con el formato
`[P] <fecha> <bot> <detección> <evidencia>`. Una fila por problema abierto: si el problema persiste, no se
duplica; cuando se resuelve, se borra sola. Su propia bitácora va a `02_Analisis/sources/_repair_log.jsonl`
(rodante, 7 días).

**Por qué no repara más.** Los fixes son idempotentes y se pueden revertir (renombrar, re-run, dispatch, recortar).
Ninguno toca código, YAML de configuración, score ni emisión.

## 12. Coparticipación entre bots (D-035)

Detecta, repara y reporta son roles distintos, y cada uno lo hace un solo bot:

```
bots de captura ──escriben──► _state.json ──lee──► bot_orchestrator (DETECTA: _health.json)
                                                        │
                                                        ▼ lee
                                                  bot_self_repair (REPARA reglas §11 / ESCALA)
                                                        │ escribe
                                                        ▼
                                       _INSTALADOS.md (REPORTA: AUTO:sources y AUTO:repair) ──► YIN / Dirección
```

**Sin ciclos:**
- los datos fluyen de captura a orquestador, de orquestador a reparador y de reparador al reporte;
- el reparador **no** escribe nada que lea el orquestador para decidir un estado, salvo el `_state.json` de un
  bot: ese es un input de captura, y el bot lo reescribe en su corrida siguiente;
- el orquestador no lee nada del reparador.

**Bot de respaldo** (`backup` en `_bots.yaml`, implementado como campo).
- **Cuándo se activa.** Cuando un bot está `caído` o `atrasado` más de `stale_min`.
- **Qué hace el bot de respaldo.** En su próxima corrida suma las fuentes equivalentes que declara
  `fallback_sources` en su propio YAML. Por ejemplo, si cae `telegram`, `rss` suma los feeds de Cointelegraph
  y Whale Alert.
- **Qué no hace.** No copia código del bot caído.

El mapa no tiene ciclos de respaldo activos al mismo tiempo: si el respaldo también está caído, no se encadena,
se escala.

| Bot | Respaldo | Por qué |
|---|---|---|
| rss | forums | Si caen los feeds de noticias, los foros dan menciones del mismo evento |
| telegram | rss | Los canales de noticias (cointelegraph, whale_alert) tienen feed RSS |
| web | forums | Bitcointalk y 4chan cubren el mismo tipo de hilo |
| github | rss | Los anuncios de repos salen en los medios |
| x | telegram | Las cuentas de X de los proyectos espejan en sus canales |
| forums | rss | — |

```yaml
# 04_Config/sources/_bots.yaml (implementado; backup ya declarado)
rss: {workflow: sources_rss.yml, every_min: 20, stale_min: 60, backup: forums, enabled: true}
# 04_Config/sources/rss.yaml (diseño): fuentes que rss suma cuando respalda a telegram
fallback_sources:
  telegram:
    - {name: whale_alert_rss, url: "https://whale-alert.io/feed"}   # [P] URL a verificar
```

## 13. Pendientes [P] para YIN

- Verificar desde Actions los 12 feeds RSS (la primera corrida de `sources_rss.yml` deja la salud de cada feed en
  `sources/rss/_state.json`).
- Vista previa de los 15 canales de Telegram, más los 2 que faltan nombrar.
- DEXTools y Solscan: confirmar si son imposibles sin navegador (§1 #5).
- Frescura de PullPush y Arctic Shift.
- Secrets OAuth de Reddit, si Dirección los crea.
