---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: DISEÑO COMPLETO (D-033, D-035) — implementado: lib_sources_store, bot_rss_news, bot_orchestrator, query() en script_116/script_97; D-041: lib_normalize, bot_self_repair, lib_knowledge_graph, auditoría por bot, bot_telegram_public
last_updated: 2026-10-03
version: 0.3
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
| `bot_influencer_tracker` | 50 cuentas de X de `04_Config/influencers.yaml`: FxEmbed (primario) y syndication (respaldo), sin login (§18) | 30 min (`12,42 * * * *`) | `sources/x_influencers/<fecha>.jsonl` + eventos | red | `sources_x_influencers.yml` **[implementado, D-087]** |
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
channels: [whale_alert_io, cointelegraph, WatcherGuru, pumpfun, BinanceKillers, crypto, binance_announcements,
           CoinDeskGlobal, BitcoinNews, dexscreener_trending, Cryptoquant_official, unfolded, DegenerateNews,
           CoinMarketCapAnnouncements, OKXAnnouncements]
# D-041: 15 con vista previa verificada el 03/10 [V]. Fuera (redirigen): SolanaNews, DexToolsAlerts, CryptoCom,
# PepeWorld, coin_alert. 'memecoins' es alias de 'crypto'. Archivo real: 04_Config/sources/telegram.yaml

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

## 11. bot_self_repair (D-035 diseño; **implementado en D-041**: `bot_self_repair.py` + `sources_self_repair.yml`)

> D-041: el auto_off vive en `_repair_state.json` (dueño: el reparador) y los bots lo leen; el reparador no edita el `_state.json` de un bot salvo para renombrarlo si está corrupto o recortar `seen`. Reruns solo en workflows de bots de fuentes; producción solo se escala.

**Qué hace.** Corre cada 30 min (`19,49 * * * *`). Lee `_health.json`, el `_state.json` de cada bot y las
últimas corridas de cada workflow (API de Actions, `GITHUB_TOKEN` con `actions: write`). Solo aplica reglas
explícitas: **cero IA generativa en producción**. Lo que no está en la tabla no lo toca: lo escala.

|| Detección | Señal | Fix conocido | Límite |
||---|---|---|---|
|| Feed o fuente caída | `status != 200` en 3 corridas seguidas [H] | `enabled: auto_off` en `_state.json`; el bot la salta 6 h [H] y después reintenta una vez. **No edita el YAML**: el YAML es de Claude y YIN. | Si 24 h [H] después sigue caída: escala [P] (P-13: reemplazarla) |
|| Workflow fallido recurrente | ≥2 fallas seguidas (`conclusion: failure`) | 1 re-run del job fallido (`POST /actions/runs/{id}/rerun-failed-jobs`) | 1 re-run por falla; la 2.ª falla se escala con el log del paso |
|| Bot atrasado | `atrasado` en `_health.json` | 1 `workflow_dispatch` | 1 por atraso; un atraso repetido en 24 h [H] se escala |
|| Archivo corrupto | `_state.json` o `_health.json` que no parsea; JSONL con líneas que no parsean | `_state.json`: se renombra a `.corrupt-<ts>` y el bot arranca con estado vacío (solo pierde el dedup de 72 h). JSONL: se reescribe sin las líneas rotas, y las rotas se guardan en `.rejected`. | Más de 1 por día en el mismo archivo: escala |
|| Output vacío anómalo | `vacío` con fuentes OK: los feeds responden 200 pero el parser da 0 ítems en 3 corridas [H] (cambió el formato) | Ninguno: un parser roto no se repara con reglas | Escala de inmediato |
|| Caché o estado inflado | `seen` con más de 50.000 [H] claves, o `_state.json` de más de 5 MB [H] | Recorta `seen` a la ventana `dedup_hours` | — |

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

## 14. audit_gate — auditoría CI determinista (D-067; dependencias D-075)

`.github/workflows/audit_gate.yml` corre en cada pull request a `main`. No usa LLM ni secretos y es de solo lectura. La lógica vive en `04_Config/scripts/audit_gate.py`, para poder testearla y correrla en local.

| Check | Comando | Falla si |
|---|---|---|
| tests | `python 04_Config/scripts/audit_gate.py tests` | algún archivo `test_*.py` sale con código ≠ 0 o no imprime `OK` |
| doc35 | `audit_gate.py doc35 --rev HEAD` | el SHA-256 de una fila del doc 35 no coincide con el **blob** de git (LF) |
| prohibited | `audit_gate.py prohibited --base <sha>` | una línea agregada trae `--force` / `reset --hard` en un comando, `TELEGRAM_CHAT_ID` en código, un secreto con forma conocida o un `.env` |
| touched / bundle | `audit_gate.py touched` / `bundle` | nunca (informativo): workflows y producción tocados, `audit_bundle.md` como artifact |

**Dependencias (D-075) [V].** Antes de la batería, `tests` ejecuta `install_deps()`:
1. Instala el primer archivo que exista entre `requirements-dev.txt` y `requirements.txt` (en la raíz). Un archivo con `--hash=` se instala con `--require-hashes --no-deps`. Que no exista ninguno no es error.
2. Si después sigue faltando bs4, instala `04_Config/requirements/sources_telegram.txt` (fijado con hash).
3. Si alguna instalación falla, la batería **no corre**: un entorno incompleto daba fallas engañosas.
4. Corre los tests con `REQUIRE_TEST_DEPS=1`. Con esa variable, un test que depende de bs4 falla si bs4 falta, en vez de saltarse. En local, sin la variable, se salta con el motivo a la vista.
5. `--no-install` saltea la instalación.

**Origen.** Las 2 fallas de `test_bot_runner` en el entorno de YIN venían de que bs4 no estaba instalado, no de un bug del parser ni de los mocks. `bot_runner.collect()` atrapaba el `ImportError` como `parse_error` con 0 ítems; ahora el `ImportError` sube.

**Bloqueo real del merge.** El workflow marca el check en rojo, pero para que eso **bloquee** el merge, la protección de rama de `main` tiene que exigir los checks `audit_gate / tests`, `audit_gate / doc35` y `audit_gate / prohibited`. Es una configuración del repo: [P] Dirección.

## 15. Calendario de activos no nacidos (D-079; diseño D-078)

`bot_prelaunch_calendar.py` + `sources_prelaunch.yml` (cada 6 h). Sigue activos **anunciados pero no nacidos** hasta que nacen y mide `delta_preventa_apertura_pct`, una señal medible para el doc 36.

| Estado | Entra cuando | Sale cuando |
|---|---|---|
| anunciado | lo ve 1 fuente | ≥ 2 fuentes → confirmado · 30 d sin nacer → purgado `no_nacido` |
| confirmado | ≥ 2 fuentes independientes coinciden | nace → seguimiento · 30 d → `no_nacido` |
| seguimiento | nació (emite `prelaunch_nacido`; `prelaunch_known: true`) | 72 h → memoria episódica `prelaunch_cerrado` |

**Fuentes** (verificadas en vivo el 2026-10-03; las 6 respondieron 200 desde fuera de EE. UU.) [V]:
- Hyperliquid `metaAndAssetCtxs`, Aevo `/markets`, Polymarket `public-search` («FDV one day after launch»), Bybit `announcements` (new_crypto), Bitcointalk board 159.
- Binance CMS (catálogo 48). Desde runners de EE. UU. puede dar 451: se registra con la nota «[P] bloqueado desde runners US» y la corrida sigue.
- **D-089-R** (verificadas el 2026-10-04; 200 sin key ni Cloudflare) [V]:
  - **CoinMarketCap:** calendario ICO por `__NEXT_DATA__`; toma las ventas `ongoing` y `upcoming` con `icoPriceUsd`, etapa, fechas, meta y launchpad. Tiene poca cobertura: hoy, 1 venta (CON a $0,007).
  - **ICO Drops:** la lista "upcoming" (50 proyectos, con ronda, valuación previa y fecha) no trae ticker ni precio. Por eso se pide la página de cada proyecto nuevo, hasta `detalle_max` (15) por corrida, con caché de 7 días en `_state.json` (`icodrops_cache`). De ahí sale el ticker del título y el primer "Price" de una ronda.
  - Sin venta pública no hay precio; sin ticker publicado, el activo entra por nombre (`name:…`).
  - Pidiendo todas las páginas de detalle: 50 filas, 38 con ticker y 35 con precio de venta (CHIMP $1,5, CLIX $0,1, SPWAY $0,12, GNOT $0,0645…). Con el tope de 15 por corrida, la cobertura se completa en unas 4 corridas (un día).
- **Precio de preventa:** manda el último precio de un perp (Hyperliquid/Aevo, `precio_preventa_fuente`). Si no hay perp, se usa el precio de la venta (CMC/ICO Drops), que además queda en `precio_venta`. Es el precio que muestra la línea PRE-LANZAMIENTO de script_97 (§16) y la base del `delta_preventa_apertura_pct`.
- **Colisión de ticker [V]:** CRED (Credible) y CON (ConConAI) no entran, porque ya hay pares DEX con ese símbolo y ≥ 100 000 USD de liquidez, y el filtro de "ya nacido" los toma como nacidos. Es el mismo criterio de antes para todas las fuentes [H].

**"No nacido" [H].** Ni Hyperliquid ni Aevo marcan la preventa en la API.
- Regla: el símbolo no tiene spot en Bybit, OKX, Binance ni Hyperliquid, **ni** un par DEX con ≥ 100 000 USD de liquidez (DexScreener, también por nombre del token).
- Origen de la regla: la doc de Hyperliquid dice que una hyperp pasa a perp normal cuando el token lista spot en Binance, OKX o Bybit.
- Hoy no hay perps de preventa vivos [V]. El calendario real del 2026-10-03 tiene Jumper (Polymarket) y BLOZ (Bitcointalk).

**Emparejamiento al nacer.**
- **Por contrato:** coincidencia exacta. Es alertable.
- **Por símbolo + nombre + chain:** exige ≥ 2 fuentes. Queda como candidato, **no alertable**.
- Los nacimientos llegan por dos vías: el evento `token_nacido` y la observación propia (el símbolo aparece en spot o en DEX).
- `token_nacido` lo emiten `script_116` y `script_114` desde D-082 (§16).

**Archivos** (un dueño por archivo): `02_Analisis/prelaunch/_calendar.json` y `_state.json`, `events/prelaunch_calendar/`, `events/_cursors/prelaunch_calendar.json` y `sources/_episodes_prelaunch.jsonl`. El workflow commitea esas rutas explícitas y nunca usa `git add -A`.

**Deprecado: `script_99_prelaunch.py` + `prelaunch.yml`.**
- Se conservan como histórico: el workflow quedó sin cron y con el job en `if: false`; el script lleva una cabecera DEPRECADO.
- Motivos del reemplazo:
  - mandaba mensajes al grupo sin método de emparejamiento;
  - sus fuentes (Metaplex, Clawnch) no estaban verificadas;
  - commiteaba con `git add -A` y compartía el grupo de concurrencia `repo-write-main` con otros workflows.
- Reemplazo: el calendario de arriba, que **no envía** mensajes. La alerta de un token que el calendario siguió desde antes de nacer lleva la línea PRE-LANZAMIENTO de script_97 (D-082, §16).

## 16. Integración preventa ↔ producción (D-082)

Autorizado por Dirección en D-082. Las tres conexiones **agregan** información y no cambian puntajes, gates ni la decisión de emitir.

**Flujo:**
1. **Anuncio:** Hyperliquid, Aevo, Polymarket, Bybit, Binance o Bitcointalk.
2. **Calendario:** `bot_prelaunch_calendar`, cada 6 h; el activo queda anunciado → confirmado.
3. **Nacimiento:** llega el evento `token_nacido`, o el calendario lo observa en spot o en DEX. Se emite `prelaunch_nacido`, el activo pasa a seguimiento con `prelaunch_known: true`, y se registran el precio de preventa, el de apertura y el delta.
4. **Alerta:** cuando script_97 alerta ese contrato por sus propios criterios, el mensaje suma la línea PRE-LANZAMIENTO.

| Conexión | Dónde | Qué hace | Commit |
|---|---|---|---|
| `token_nacido` desde el early watch | `script_116.emit_births()`, después de evaluar | candidato del scorer joven con edad ≤ 30 min y liquidez > 0 → evento con mint, símbolo y nombre del lanzamiento, chain `solana`, precio, liquidez y pool. Escritor `early_watch_<inst>`; un set por loop evita reintentos y lib_events deduplica por mint y día entre a y b | la carpeta `events/early_watch_<inst>/` entra en los paths que ya commitea el script |
| `token_nacido` desde el scanner | `script_114.emit_births()`, después de escribir | pools en tendencia de GeckoTerminal creados hace ≤ 24 h → evento con contrato, símbolo, red y precio. Escritor `multichain_scanner` | `multichain_scanner.yml` suma `events/multichain_scanner/` |
| Línea en la alerta | `script_97.prelaunch_line()` dentro de `format_alert_message` (alertas principales y del early watch) | `lib_sources_store.prelaunch_lookup(mint)` busca en el calendario **por contrato exacto** y devuelve «🆕 PRE-LANZAMIENTO: precio preventa $X, delta vs apertura +Y%». Si el nacimiento se emparejó por símbolo, agrega «(candidato por símbolo)». Sin calendario, o si está corrupto: no agrega nada y el mensaje queda idéntico | — |

**Garantías.**
- **Ningún evento frena a su emisor:** `emit_births` nunca lanza; si falla, imprime un aviso.
- **Eficiencia:** `lib_events.write_events` escribe en lote y carga los ids conocidos una vez por poll, porque el early watch evalúa cientos de candidatos.
- **TTL de `token_nacido`: 24 h.** Con 6 h igualaba la cadencia del calendario y un evento podía vencerse sin que nadie lo leyera.

**Cuándo es alertable.** El calendario nunca alerta: solo marca. La línea se agrega a alertas que script_97 ya decidió emitir. Un nacimiento emparejado por contrato se muestra limpio; uno por símbolo, como candidato.

**Tests:** `test_d082_token_nacido.py` (2) y `test_d082_prelaunch_alerta.py` (1). Las suites existentes de 116 (26), 114 (19) y 97 siguen verdes.


## 17. Patrimonio de datos (D-087)

`02_Analisis/patrimonio/` es el **índice de qué hay dónde**. No es una mudanza: cada bot sigue escribiendo en su ruta (un dueño por archivo) y `_inventario.json` la apunta. Mover datos rompería a productores y consumidores en producción.

**Árbol:**

```
02_Analisis/patrimonio/
  README.md          reglas
  _inventario.json   índice: una entrada por carpeta o archivo de primer nivel de 02_Analisis/
  cuantitativo/      series nuevas sin dueño previo (p. ej. lead-lag por cuenta de X)
  informativo/       snapshots diarios de portales sin bot (rwa/, depin/: fichas 07_portales)
  calendario/        fuentes extra del calendario que no escriba bot_prelaunch_calendar
  resultados/        resultados agregados (precisión por fuente, por cuenta, por narrativa)
```

| Categoría | Qué guarda | Rutas reales vivas |
|---|---|---|
| cuantitativo | precios, liquidez, volumen, scores, señales, datasets | `multichain/`, `early/`, `datasets/`, `shadow_v4/` |
| informativo | fuentes src-1, eventos, narrativa, X, dossiers | `sources/` (incluye `x_influencers/`), `events/`, `narrative/`, `dossiers/` |
| calendario | activos no nacidos y su seguimiento | `prelaunch/` |
| resultados | alertas, operación, diagnósticos, hipótesis | `alerts/`, `operations/`, `diagnostics/`, `hypotheses/`, logs `_*.json` de los bots del pipeline |

**Entrada del inventario:** `{ruta, categoria, estado, dueno, formato, que}` más, si aplica, `consumidores`, `retencion` y `doc`. Estados:
- `vivo`: lo escribe un workflow activo;
- `manual`: corridas a mano o bibliotecas sin workflow (`signals/`, `macro/`, `hypotheses/`);
- `futuro`: ruta reservada que crea su dueño en la primera corrida (las 4 subcarpetas de `patrimonio/`);
- `legado`: sin escritor, todavía en su lugar;
- `archivado`: movido a `02_Analisis/_archivo_2026_Q3/` (D-089-R), con `archivado.desde`.

**Estado al 2026-10-04 [V]:** 60 entradas.

| Categoría | Entradas | Archivos | Tamaño |
|---|---|---|---|
| cuantitativo | 24 | 163 | 34,4 MB |
| informativo | 11 | 212 | 3,8 MB |
| calendario | 5 | 7 | 0 MB |
| resultados | 20 | 241 | 1,6 MB |

**Archivo (D-089-R, 2026-10-04).** Las 38 entradas `legado` (detection_v3–v6, shadow_v2/v3/v5, deep_dive_*, panorama…) se movieron con `git mv` a `02_Analisis/_archivo_2026_Q3/`: 91 archivos, 1,1 MB, con la historia conservada (`git log --follow`).
- El README del archivo dice qué es cada una, quién la escribía y por qué se archivó: sin escritor activo y sin lector en producción. El criterio es el aporte al fin, no la fecha.
- En el inventario conservan su categoría, con `estado: archivado` y `archivado.desde`. No se borró nada.
- `events/` y `prelaunch/` pasaron de `futuro` a `vivo`, porque ya existen en main.

**Única lectura en producción encontrada:** `script_97.load_multichain_extras()` lee `pre_launch/_prelaunch_accumulated.json`, el insumo del grupo b de `lib_scoring_multichain`.
- Antes de moverlo, ese archivo tenía las tres listas vacías; el grupo b es solo de registro (`REGISTER_ONLY`) y su escritor (script_99) está deprecado desde D-079.
- Sin el archivo, `_read_json_file` devuelve `None`: el mismo resultado que con listas vacías.
- [P] Si Dirección quiere el grupo b vivo, la fuente natural es `prelaunch/_calendar.json`, pero eso es un cambio en script_97 que hay que autorizar.

**Guardia.** `lib_patrimonio.check()` falla si una entrada no cumple el esquema, si una ruta vivo/manual/legado no existe, o si una carpeta o archivo de primer nivel de `02_Analisis/` no figura en el inventario. `test_lib_patrimonio` corre en `audit_gate tests`: una ruta nueva de un bot se anota en el mismo PR. `python 04_Config/scripts/lib_patrimonio.py` imprime el resumen.

## 18. bot_influencer_tracker — cuentas de X (D-087)

`bot_influencer_tracker.py` + `sources_x_influencers.yml` (cada 30 min, minutos :12 y :42; concurrency `sources-x-influencers-write`). Lee las cuentas de `04_Config/influencers.yaml` (`{cuenta, categoria, prioridad}`): 50 activas y 16 candidatas apagadas, todas verificadas el 2026-10-04.

**Mecanismos sin login (medidos el 2026-10-04) [V]:**
- **Primario: FxEmbed** `api.fxtwitter.com/2/profile/<cuenta>/statuses`. Trae ~20 publicaciones frescas para casi todas las cuentas activas, con likes, reposts, respuestas y vistas. En ~120 requests no apareció ningún límite.
- **Respaldo: syndication** (el widget de inserción). Límite de 30 requests cada 15 min por cliente. De 8 cuentas probadas, solo 2 vinieron frescas: 3 congeladas (la publicación más nueva era de hace ~330 días) y 3 vacías. Por eso no puede ser el único mecanismo, como suponía la ficha de D-079.
- El siguiente mecanismo se usa si el anterior falla, viene vacío o trae solo publicaciones de más de `stale_dias` (7).
- FxEmbed da **404 pasajeros**: el 2026-10-04, OnchainLens y hivemapper dieron 404 y un minuto después 200 [V]. Por eso un 404 de FxEmbed se reintenta una vez antes de contar como falla (D-089-R).

**Flujo por corrida:**
1. Elige las cuentas al día. Una cuenta `vivo` se consulta en todas las corridas; `lento`, cada 6 h; `congelado` y `vacio`, cada 24 h. Primero van las de prioridad 1.
2. Pide las publicaciones, con 1 s entre requests reales.
3. Registra las publicaciones de los últimos 30 días (`max_age_h: 720`, la ventana de evaluación) cuyo id no esté en los diarios de los últimos 31 días (`historia_dias`) ni en `seen`. Hasta D-089-R la ventana era de 48 h.
4. Emite eventos para las de las últimas 2 h.

**Salida:**
- **Diario:** `sources/x_influencers/<fecha>.jsonl` (src-1, kind `tweet`).
  - `src` = la cuenta.
  - **Texto (D-089-R):** se guardan solo `m.sha` (sha256 del texto original) y `m.ext` (extracto de hasta 200 caracteres, con los espacios colapsados).
    - El extracto se centra en lo primero que se detecta: un contrato, un $cashtag o una palabra clave. Si no hay nada, toma el comienzo.
    - Pesa ~250 bytes por post: medido en vivo, 249 de promedio.
  - **Casi-duplicados:**
    - Detección: mismo sha256, o Jaccard ≥ `dup_umbral` (0,7) de 5-gramas de caracteres de los extractos sin URLs ni puntuación, contra los posts de las últimas `dup_horas` (72).
    - Marca: el post queda con `m.dup_de` (id) y `m.dup_cuenta`.
    - Si la que se repite es la misma cuenta, no se emite `tweet_influencer`. Una copia de otra cuenta sí avisa, porque el eco es señal.
  - `m` lleva categoría, prioridad, mecanismo, repost, métricas, URLs (sin t.co) y `tok` (contratos sacados de URLs de token, de "CA:" o de sufijos `pump`/`bonk`; las wallets de exploradores no cuentan).
- **Estado:** `sources/x_influencers/_state.json` con:
  - `seen` (72 h);
  - `rate_limit` por mecanismo;
  - `sources`, la salud por cuenta: estado HTTP, mecanismo, frescura, fallas seguidas, `next_check`, `auto_off_until` tras 3 fallas (6 h) y la evaluación (abajo);
  - `mecanismos`, `evaluar` y `vigentes` (abajo), y `reporte_semana`.

**Evaluación (D-089-R): señales para Yang, nunca acciones automáticas.**
- **Por cuenta:**
  - `ultimo_post_ts` y `dias_desde_ultimo_post`: el post más nuevo visto, aunque sea más viejo que la ventana o la última consulta haya fallado;
  - `frescura_score`: 1,0 con < 7 días, 0,5 de 7 a 30 días, 0,2 con > 30 días o sin posts;
  - `posts_30d` y `aporte_estimado`, sobre los diarios de 30 días más la corrida, cada post por id una sola vez.
- **Aporte** = post que nombra un contrato, o el cashtag de un **activo vigente** que no sea mayor [H].
  - Activo vigente = lo que el sistema sigue hoy: calendario de preventa sin purgar, alertas de 30 días, scan multichain (grupos, on-chain, acelerando), perps de Hyperliquid (kPEPE y 1000BONK se cuentan como PEPE y BONK) y watchlists del early watch.
  - El 2026-10-04: 449 símbolos y 223 contratos.
- **`evaluar: true`** si `dias_desde_ultimo_post` > 30 (o nunca se vio un post), o si `aporte_estimado` = 0 con > 10 posts en 30 días. `evaluar_motivo` dice cuál.
  - Una cuenta que todavía no se consultó no se juzga.
  - El bot **no** cambia `next_check` ni `auto_off_until`, y no edita `influencers.yaml`: una cuenta marcada se sigue consultando en su turno normal. Lo verifica `test_d089_influencer_evaluacion` (test 4).
- **Por mecanismo:** posts de los últimos 30 días / posts devueltos, por día, en una ventana de 30 días. `marginal: true` si el cociente es < 0,10. Solo marca: el orden de `mecanismos` no cambia solo.
  - Syndication se consulta solo cuando FxEmbed falla o trae lo viejo, así que su muestra está sesgada.
- **Reporte semanal:** en la primera corrida de cada semana ISO (o con `--reporte`) se reescribe `sources/x_influencers/_evaluar_semanal.md` y se agrega una línea a `_evaluar_log.jsonl`. Contiene la tabla de cuentas a evaluar con sus datos y los mecanismos marginales. Yang decide.
- **Primera medición en vivo (2026-10-04, sin diarios todavía; `posts_30d` sale de los últimos ~20 posts):** 25 de 50 cuentas marcadas.
  - 2 por `sin_post_30d`: cobie (30,4 días) y hivemapper (67).
  - 23 por `sin_aporte`: cuentas que publican sin cashtags ni contratos, sobre todo CEX, fundadores y cuentas de sector.
  - FxEmbed 843/937 = 0,90, no marginal.
- **Eventos** (`events/x_influencers/`, lib_events):

| Tipo | Subject | Severidad | TTL / ventana |
|---|---|---|---|
| `tweet_influencer` | id de la publicación | 2 si prioridad 1 y nombra un cashtag o contrato; 1 si prioridad ≤ 2; 0 si no | 6 h / 1 día |
| `mencion_token` | `$CASHTAG` o contrato | 0 para los mayores (BTC, ETH, SOL…); 1 + (≥ 2 cuentas o prioridad 1) + (≥ 3 cuentas), máximo 3 | 3 h / 1 h |
| `keyword_narrativa` | palabra clave de `keywords.yaml` | 0 con 1 cuenta, 1 con 2–3, 2 con ≥ 4 | 4 h / 1 h |

**Límites de tasa:**
- Un 429 guarda el `x-rate-limit-reset` (o 15 min) y ese mecanismo no se vuelve a usar hasta entonces.
- Un `x-rate-limit-remaining` ≤ 1 corta el mecanismo sin esperar el 429.
- Syndication tiene un cupo de 20 por corrida.
- Si todos los mecanismos están limitados, la corrida termina y las cuentas pendientes quedan sin falla para la próxima.

**Efecto en producción [V].** Los registros entran al almacén fusionado (§4, §6), como RSS y Telegram, así que por diseño (D-035) suman menciones por mint y `$símbolo` al componente informacional del scorer joven de script_116 y a las menciones informativas de script_97. Es la vía prevista para todo bot de fuentes; no se tocó código de scorers.

**Registro.** `x_influencers` en `_bots.yaml` (cadencia 30 min, atrasado a los 90): lo vigilan el orquestador y self_repair.

**Tests:**
- `test_bot_influencer_tracker.py` (8): parsing de los dos mecanismos y extracción, dedup (por diarios), falla aislada con auto_off, rate limit, frescura con respaldo, eventos, configuración real, corrida completa con escritura (extracto y no texto completo).
- `test_d089_influencer_evaluacion.py` (5): frescura, aporte y activos vigentes, marcado `evaluar` + `marginal` + reporte, NO eliminación automática, y sha256 + extracto que detectan casi-duplicados.
