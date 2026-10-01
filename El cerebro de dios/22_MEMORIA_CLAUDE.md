---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: VIVO (se actualiza al cierre de cada sesión)
last_updated: 2026-10-01
version: 1.1
---

# 22 — Memoria persistente de Claude Code

Rótulos: [V] verificado (comando/archivo/API en esta sesión) · [I] inferido · [H] hipótesis · [P] pendiente.
Regla de uso: **leer este documento al empezar cada sesión** y actualizarlo al cerrarla (secciones 1, 4, 7, 8 como mínimo).
Si algo de acá contradice al repo, **manda el repo**: corregir este documento en la misma sesión.

---

## 1. Estado (cierre de sesión 2026-10-01 ~05:00 UTC)

| Componente | Estado | Rótulo |
|---|---|---|
| Emisión | **FUERA DE SOMBRA desde el 01/10 03:48 UTC**: `SHADOW_MODE: "false"` en `pipeline_t0.yml` (`6ff13c5`, commit del bot/YIN, mensaje "validado v7.2.1"). Decisión de Dirección. **Dato [V] a esa hora:** el monitor registraba para v7.2.1 n = 2 primarias resueltas (1/2, IC90 12–88%) y 50% de alertas en tokens < 60 min; los criterios de §1.1 piden n ≥ 20 y < 20%. Hasta el cierre no hubo alertas nuevas (la última, 30/09 12:48 UTC, en sombra). | [V] |
| Scorer | **v7.2.1** en main desde 2026-09-30 (`SCORING_VERSION = "7.2.1"`, `ACCEL_GATE_MIN_AGE = 60`). Cada token lleva `detected_at` y `scoring_version`. 1.ª corrida de producción (`detection_2026-09-30_055022`): 35/35 tokens con 7.2.1, **≥ 56: 2/35** (vs 19/29 y 23/33 en las dos corridas v7.2 previas). | [V] |
| Filtros de emisión (script_97) | umbral `EMIT_MIN_SCORE = 56` · frescura R1 `CANDIDATE_MAX_AGE_MIN = 60` · **edad mínima del par `EMIT_MIN_AGE_MIN = 30`** (edad desconocida → no emite) · dedup PARASITE. | [V] |
| Plantilla Telegram | **Framing neutral** (`c727ece`, Dirección): el proyecto informa con datos y método; **no juzga, no advierte, no disuade: el usuario decide**. Sin "ADVERTENCIA", sin "plan sugerido", sin "no invertir más de…". Bloques: 🪪 ACTIVO (nombre, chain, mint, creador) · **🛒 CÓMO ADQUIRIRLO primero** (guía por chain: wallets, fondeo, DEX + alternativas, 8 pasos, slippage por liquidez + impacto, verificación; **chain sin guía o sin mint = no se emite**, `acquisition_ready`; `7d77b72`, en main, commit y push de YIN) · 🕒 DETECCIÓN (hora, edad del par, creación del par, ventana < 48 h) · 🎯 PROBABILIDADES (primaria, secundaria y "después de tocar +20%, llegar a ≤ −99%" como **métrica**, no advertencia; "en validación" hasta `validated: true`) · 📊 DATOS · 🔎 motivos · 🔗 FUENTES VERIFICABLES (Solscan, DexScreener, pump.fun) · seguimiento. "n/d" para lo desconocido; Markdown de datos externos escapado (T4 `06fedff`). | [V] |
| Trust loop (script_98) | Solo procesa `status == "active_tracking"` (ignora sombra). | [V] |
| Bots gemelos | `monitor_shadow_bot` (6 h), `health_check_bot` (2 h), `autorepair_bot` (4 h), `daily_summary_bot` (06:00 UTC). Los 4 verificados con workflow_dispatch el 2026-09-30 05:50 UTC (success + commit de su log). | [V] |
| Telegram de operaciones | Los bots escriben SOLO a `TELEGRAM_OPS_CHAT_ID` (grupo "La mano de Dios"). Secret cargado por Dirección el 2026-09-30 06:05 UTC; primer envío (resumen diario por dispatch, run 36677130640) a las 06:13 UTC con `notified: sent`. | [V] API · **recepción confirmada por Dirección** |
| Destinos de Telegram | **Mercado** (alertas `script_97`, trust updates `script_98`, pre-launch `script_99`) → `TELEGRAM_PUBLIC_CHAT_ID`. **Sistema** (4 bots, `lib_ops`) → `TELEGRAM_OPS_CHAT_ID`. Los dos apuntan al grupo privado "La mano de Dios" (solo owner + bot), con prefijos distintos [reportado por Dirección]. **Chat personal (`TELEGRAM_CHAT_ID`) deprecado:** ningún script de producción lo lee y ningún workflow lo pasa. `--test-send` / `telegram_test_send.yml` apuntan solo al grupo. **En main** (push ff `b560a7a..2c44332`). Test-send run 36799931771: **grupo OK**, un solo destino en el log (el chat personal no se intentó). | [V] |
| Resumen diario (ops) | Formato legible por secciones, calidad separada por versión (T1 `7b14a58`); un envío por día UTC con `last_sent_date`, `--force` para reenviar (T2 `dd48a77`). | [V] |
| Scanner multi-chain v0 | `script_114_multichain_scanner.py` (T5 `3694aa8`): grupos h, f, c, g, d, e (CoinGecko sin key) + a (GeckoTerminal: solana, base, eth, blast, monad). Solo recolección + marca de aceleración [H]; sin score, sin emisión, **no enganchado a ningún workflow**. Humo real: 13 llamadas, 0 errores. | [V] |
| Tests | **237/237** corriendo **cada archivo por separado** (16 archivos `04_Config/scripts/test_*.py`, unittest, sin red). Con `unittest discover` falla 1 test preexistente (ver §7). | [V] |
| Dossier por activo | **`script_113` v1.1 en main** (Fase 3: `8bf26f1`). **Fase 4, rama `claude/dossier-envio`, sin push:**<br>• `script_97` arma el dossier de cada alerta: en sombra lo guarda; fuera de sombra lo manda con `sendDocument` al grupo, con caption ≤ 1024 que lleva el 🛒 completo, y con fallback a `sendMessage`.<br>• Ruta CEX confirmada por contrato (CoinGecko + Binance `data-api` + Coinbase) con enlaces sin código de referido; categorías de CoinGecko, scanner y registro de narrativas.<br>• Doc 24 §8. | [V] |
| Alertas acumuladas (`_all_alerts.json` en `3694aa8`) | 35 en total: **26 `shadow`** (de 2026-09-30 03:55 a 12:48 UTC; ninguna más hasta el cierre), **7 `active_tracking`** (la última del 2026-09-29 17:55 UTC, anterior a SHADOW), 2 `DESCARTAR_NOPAR`. `telegram_sent: true` = 0. | [V] |
| Hashes de cierre | Sesión 1: T3 `26ce5b7` · T4 `3ef7b50` · bots `daf9cc4` · docs 22/23 `63a1b95`. Sesión 2: framing `c727ece` (aplicado por Dirección/YIN) · push fast-forward `77b2a1c..3694aa8` con T1 `7b14a58` · T2 `dd48a77` · T3 `ba44f21` + `68953b8` · T4 `06fedff` · T5 `3694aa8`. | [V] |
| Incidente | Dirección reportó el sistema caído y luego **recuperado** ("GitHub Actions funcionando") [reportado]. Verificación propia: `pipeline_t0` y `trust_update` con runs `success` cada ~20 min hasta 23:05 UTC. | [V] |

### 1.1 Criterios de validación de v7.2.1 (Dirección)

- Primaria (toca +20% antes de −30%, 48 h) **≥ 30%** con **IC90 inferior > 15%**, n ≥ 20 (baseline 10,5%).
- Secundaria (cierre ≥ +20% a 48 h) **≥ 5%** con IC90 inferior > 2%, n ≥ 20.
- Exposición a tokens < 60 min **< 20%**.
- Tests 100%.
- **Si la primaria da < 20%** → relajar el gate a 30 min (no a 0).
- El veredicto lo avisa `monitor_shadow_bot` una sola vez (clave `verdicts["shadow_verdict:7.2.1"]` en `_cycle_log.json`). **La decisión de reactivar es de Dirección.**

---

## 2. Arquitectura (lo que necesito tener en la cabeza)

```
GitHub Actions (cron, repo artificialintelligencestaff-tech/shot-de-mercado, rama main)
├── pipeline_t0.yml   */20  → script_82 (detección+score) → script_97 (emisión/sombra) → commit
├── trust_update.yml  */20  → script_98 (trust loop sobre active_tracking) → commit
├── prelaunch.yml     0 */6
├── probe-fuentes.yml       (sondas de fuentes)
│   concurrency: repo-write-main (los 3 de producción)
└── bots gemelos (concurrency propia ops-<workflow>, nunca bloquean al pipeline)
    ├── monitor_shadow_bot.yml  15 */6   → monitor_shadow.py --incremental --max-calls 80
    │                                       + --record-only --cycle-log (reintento sobre origin/main fresco)
    ├── health_check_bot.yml    45 */2   → bot_health_check.py   → 02_Analisis/_health_log.json
    ├── autorepair_bot.yml      30 */4   → bot_autorepair.py     → 02_Analisis/_autorepair_log.json (+ issues)
    └── daily_summary_bot.yml   0 6      → bot_daily_summary.py  → 02_Analisis/_daily_summary.json
```

Archivos de estado clave (todos commiteados por los crons):

| Archivo | Quién escribe | Contenido |
|---|---|---|
| `01_Datos_Crudos/final_detection/detection_*.json` | script_82 | `enriched[mint]` con score, breakdown, `detected_at`, `scoring_version` |
| `02_Analisis/alerts/_accumulated.json` | script_82 | candidatos acumulados |
| `02_Analisis/alerts/_all_alerts.json` | script_97 | alertas (activas y sombra) |
| `02_Analisis/alerts/_cycle_log.json` | script_97 (`dedup_events`) + monitor bot (`shadow_monitor`, `verdicts`) | bitácora de ciclos |
| `02_Analisis/diagnostics/shadow_monitor.json` | monitor bot | métrica dual rolling por versión |
| `02_Analisis/diagnostics/emission_calibration.json` | calibrate_threshold_v72 | probabilidades para la plantilla (solo si `validated: true`) |

Librerías internas: `lib_fusion.py` (Beta priors, log-odds acotado, fixed-share, RRF — Cap. II), `lib_narrative.py` (Cap. VII, capa temática = 0 por ahora), `lib_ops.py` (bots: JSON atómico, logs con tope, Telegram de operaciones, API de GitHub).

Universos: **A** = BTC/ETH/SOL · **B** = UNI/ICP/APT/PSG · **C** = memecoins/Base/Blast/Monad. El pipeline productivo hoy es Solana memecoins (C).

---

## 3. Convenciones

**Proceso**
- Directivas en castellano rioplatense; vienen de YANG (arquitecto/auditor) vía Dirección (humano). Lo que llega **pegado** se confirma con Dirección antes de acciones de producción.
- Formato de reporte fijo: TAREA COMPLETADA / ARCHIVOS CREADOS / MODIFICADOS / DIFF / TESTS EJECUTADOS / EVIDENCIA / LIMITACIONES / RIESGOS / PREGUNTAS ABIERTAS / DEUDAS REGISTRADAS + las secciones extra que pida cada directiva.
- Rótulos [V]/[I]/[H]/[P] en cada afirmación.
- Un commit por entregable; mensajes `feat:` / `fix:` / `docs:` / `data(§N):`.

**Git (nunca negociable)**
- **Nunca** `--force`, `--force-with-lease`, `reset --hard`. Push a main solo con autorización explícita y **solo fast-forward**, con guarda:
  `test "$(git rev-parse origin/main)" = "$(git merge-base origin/main RAMA)"`.
- Ramas de trabajo `claude/<tema>`; rebase sobre `origin/main` justo antes de pushear (los crons commitean cada ~10 min).
- Backups `.bakN` locales antes de modificar archivos canónicos (están en `.gitignore`: `*.bak*`, `*.bak[0-9]*`).
- Nunca commitear `.env` ni credenciales; nunca tocar tokens ni secrets (los carga Dirección).

**Código**
- Python 3.11 en Actions, stdlib + `requests`. Scripts ejecutables con `SHOT_ROOT` (pathlib; nunca rutas Windows).
- Tests `unittest` sin red, un archivo `test_<módulo>.py` por módulo; con mutation testing cuando el test debe discriminar.
- Telegram: **mercado** (alertas, trust updates, pre-launch) = `TELEGRAM_PUBLIC_CHAT_ID`; **sistema** (bots, `lib_ops.send_ops_telegram`) = `TELEGRAM_OPS_CHAT_ID`. `TELEGRAM_CHAT_ID` (chat personal) está **deprecado**: no se lee ni se pasa en ningún workflow.
- **El bot es solo emisor:** solo `sendMessage`; nada de `getUpdates`, webhooks, handlers ni polling. Si algún día hace falta leer comandos, va con whitelist por `chat_id` (solo PUBLIC y OPS). Lo vigila `test_telegram_hardening.py`.

**Prohibido**
- GARCH/EGARCH/ATR/Bollinger/VIX en memecoins (sí aplican al Universo A).
- Telethon / Pyrogram / pyrofork · `lite-api.jup.ag` · `cryptocurrency.cv` · vectorbt / backtesting.py / backtrader / mlfinlab.
- APIs pagas. Todo 100% gratuito.
- Dependencias nuevas sin verificar supply chain (licencia permisiva, último commit < 6 meses, mantenedores, deps transitivas).

**Entorno local (Windows + Git Bash)**
- `MSYS_NO_PATHCONV=1` para `git show rev:ruta`.
- `git ls-tree -z` para nombres con backslash.
- `grep -P` falla por el locale → usar `grep -E` / `-F`.
- Los heredocs de Bash rompen emojis de 4 bytes → escribir scripts con la herramienta Write.
- `PYTHONIOENCODING=utf-8`.
- Python de Windows no ve `/tmp` → usar el scratchpad.
- El repo local está en `D:\Proyecto Shot de mercado`; el remoto se llama `origin`.
- `core.autocrlf=true` en el checkout local: los archivos en disco tienen CRLF. El blob de un archivo se calcula con `git hash-object` (aplica el filtro y coincide con `git ls-tree`), nunca con sha1 de los bytes del disco.
- Batería de tests: **archivo por archivo** (`for f in 04_Config/scripts/test_*.py; do python "$f"; done`). `unittest discover` mezcla el `SHOT_ROOT` que fijan algunos tests al importarse.

---

## 4. Hallazgos (acumulados, con evidencia)

| # | Hallazgo | Rótulo | Doc |
|---|---|---|---|
| H-84 | El **84%** (32/38) de los tokens que tocan +20% caen **≤ −99%** después, dentro de 48 h. Con score ≥ 56: **76,2%** (16/21). Mediana del mínimo post-acierto −99,6%. | [V] | 21 |
| Métrica dual legado | Primaria 50,7% (todos) / 60,0% (≥ 56). Secundaria 4,0% / **8,6%**. La primaria mide "tocó", la secundaria "se sostuvo": la brecha es el rug. | [V] | 19 §4.2 |
| Inundación v7.2 | 88,2% de los tokens ≥ 56 (66% ≥ 70). 182/186 alertas eran tokens < 60 min con m5/h1 ≈ 1 (bonos temporales inflados). v7.2.1 lo lleva a **1,4%**. | [V] | 20 |
| Mensajes con datos inventados | 19/22 snapshots de alertas enviadas no tenían `dx`: la plantilla vieja rellenaba. Corregido: "n/d". | [V] | 17 / plantilla |
| Crash loop | ≥ 8 envíos a Telegram sin registrar (el envío ocurría antes de persistir). Corregido con dedup + persistencia previa. | [V] | 17 |
| Narrativa H1 (GTA/gaming) | Rechazada, n = 75, sin efecto medible. Capa temática = 0. | [V] | 18 |
| Sombra post-R1 | Alertas post-R1 frescas (staleness 0,1 min); 12 pre-R1 viejas excluidas del monitor por defecto. | [V] | shadow_monitor.json |
| VSOF, métrica dual | Primaria **cumplida**: tocó +20% a las 3,86 h; antes, el mínimo fue −0,9% (velas de 15 min, 135 velas, 0 ambiguas). Secundaria pendiente hasta las 17:08 UTC del 01/10. | [V] | 24 §4.6 |
| `bp_delta` inactivo | `_accumulated.json` nunca guarda `buy_pressure` (0 de 4.348 registros), así que la componente "Buy pressure cayendo/subiendo" (±15) de `script_82` no se activa en producción. | [V] | 22 §7 |
| Población v7.2.1 | En `_accumulated.json` (último scoring por mint): 3 de 2.802 tokens ≥ 56 (0,11%). No es comparable con el 1,4% del doc 20, que cuenta todas las corridas. | [V] | 24 §7 |
| Desglose por motivos | Reconstruir el score desde `reasons` coincide con `score_token` en 400 de 400 casos sintéticos (test). Mitiga, sin cerrar, la deuda de `score_breakdown`. | [V] | 24 §7 |
| Herramientas de scraping | `whaleyxbt/patchright` → 404; el repo real es `patchright-enhanced`, sin licencia y orientado a evadir WAF: descartado. Agent-Reach: X y Reddit exigen cookies de cuentas: no. Scrapling: candidata condicional (solo el núcleo). | [V] | 25 |

---

## 5. Herramientas y fuentes (gratuitas, verificadas)

| Herramienta | Uso | Límite observado | Rótulo |
|---|---|---|---|
| GeckoTerminal API v2 (OHLCV minuto) | velas para la métrica dual | 429 frecuentes → intervalo 6,5 s + reintentos con backoff; cache/offline en calibrate | [V] |
| DexScreener | pares, `pairCreatedAt`, m5/h1 | sin key | [V] |
| Jupiter Tokens V2 (`api.jup.ag`) | dev, audit, holders, verificación (Cap. II) | sin key; **no** `lite-api.jup.ag` | [V] |
| CoinGecko `coins/{platform}/contract/{addr}` (sin key) | ficha por contrato: categorías y pares en Binance/Coinbase/Kraken. **Sus `trade_url` de Binance traen código de referido: no se usan** | ~1 request/15 s | [V] |
| Binance `data-api.binance.vision/api/v3/exchangeInfo` · Coinbase `api.exchange.coinbase.com/products/{SYM}-USD` | par existente por símbolo (sin confirmar contrato) | sin key | [V] |
| **User-Agent** | debe ser ASCII: con "investigación" en el UA, 4chan, Cointelegraph, Decrypt y The Block devolvían 403 | — | [V] |
| Wikipedia Pageviews / Wikidata SPARQL | señales de atención (Universo A/B) | sin key | [V] |
| Binance data-api | velas Universo A | público | [V] |
| `gh` CLI / API REST de GitHub | runs, jobs, issues (bots) | GITHUB_TOKEN del workflow | [V] |
| RugCheck `/v1/tokens/<mint>/report` | authorities, holders, top-10, LP bloqueada, etiquetas, descripción (Solana) | sin key | [V] |
| GoPlus `token_security` (Solana y EVM) | mintable / freezable; EVM: honeypot e impuestos | sin key | [V] |
| Reddit RSS `www.reddit.com/r/<sub>/new/.rss` | menciones (doc 26) | 200 Atom; el JSON anónimo da **403** | [V] |
| Telegram `t.me/s/<canal>` (vista web pública) | menciones (doc 26) | 200 HTML, `robots.txt` 404. **Sin Telethon/Pyrogram** | [V] |
| 4chan `a.4cdn.org/biz/catalog.json` · HN Algolia · RSS CoinDesk/Cointelegraph/Decrypt/The Block | menciones (doc 26) | 200 | [V] |
| GDELT DOC 2.0 | volumen de noticias | **429**: "1 request cada 5 s" | [V] |

Scripts de análisis: `calibrate_threshold_v72.py` (métrica dual, Wilson IC90, bootstrap, `--offline`), `monitor_shadow.py` (métrica rolling de sombra), `script_112` (Jupiter V2).

---

## 6. Preguntas abiertas

1. ~~¿Cuándo se carga `TELEGRAM_OPS_CHAT_ID`?~~ Cargado el 2026-09-30 06:05 UTC [V].
2. [P] Con la edad mínima de 30 min y el gate de 60 min, ¿alcanza el volumen para llegar a n ≥ 20 primarias en un plazo razonable? El monitor lo va a mostrar en el DÍA N.
3. [P] ¿La advertencia del 76% se recalcula automáticamente cuando haya calibración v7.2.1, o queda fija con la fuente "histórico v7.1"?
4. [H] ¿El take-profit a +20% debería ser parte de la métrica publicada (tasa de "tocó +20%" = lo que el usuario puede capturar) en lugar de la secundaria?

---

## 7. Deudas registradas

| Deuda | Origen | Prioridad |
|---|---|---|
| ~~Transición v7.2 → v7.2.1~~ Cerrada por tiempo (ventana R1 hasta 06:32 UTC del 30/09). Las 3 alertas de las 05:55 quedan como v7.2 en el monitor. | T1 | — |
| `HISTORICAL_RUG_AFTER_HIT` fijo en código (v7.1) | T4 | P2 |
| `no_alerts_24h` es informativo: con el volumen bajo esperado puede ser ruido | bots | P3 |
| El monitor en Actions no tiene cache persistente de velas (reusa filas definitivas; el tope es 80 llamadas por corrida) | bots | P3 |
| Hallazgo #17 (defaults heurísticos de fusión) sin calibrar | Cap. II | P2 |
| Rutas `signals/{chain}/{mint}.json` multi-chain sin productores | Cap. II | P2 |
| **A-c) Alertas `active_tracking` estando en SHADOW.** Dato [V] (cierre sesión 2): las 7 son anteriores al cambio a SHADOW (la última, 2026-09-29 17:55 UTC); las 4 "de 24 h" del resumen de las 06:13 eran del 29/09 a la tarde. **Ninguna nueva en sombra.** Falta confirmar que el trust loop las sigue procesando bien. | resumen diario 06:13 | P1 (baja de P0) |
| ~~**A-a) Resumen diario duplicado**~~ **Resuelta con T2 (`dd48a77`)**. (Llegó 03:13 y 03:14 hora AR.) Hipótesis de Dirección: reintento sin idempotencia. Dato [V] sin investigar: en main hay dos commits del bot, `22fb807` (06:13:29, dispatch manual) y `9e39038` (06:14:44, [H] el cron de las 06:00 corrido con atraso). Falta decidir si el bot debe saltear el envío cuando ya existe la entrada del día. | resumen diario | P1 |
| **A-b) 83% de las alertas en tokens < 60 min** (`0.8333`). Hay que desagregar por versión del scorer (v7.2 vs v7.2.1). Dato [V]: en el monitor ese 0.8333 corresponde a la fila v7.2 (5/6). Todavía no hay alertas v7.2.1 para medir. **El resumen ya separa la calidad por versión (T1)**; falta la medición con n suficiente. | resumen diario | P1 |
| **A-d) 1343 tokens sin `scoring_version`** en las detecciones de 24 h. Esperado: son anteriores a R1 y se completa en 24 h. (A las 22:47 UTC ya eran 450.) | resumen diario | P3 |
| ~~**Falta el secret `TELEGRAM_PUBLIC_CHAT_ID`**~~ Cargado por Dirección; el test-send llegó a ambos destinos (confirmado por Dirección). | T3 sesión 2 | — |
| Scripts viejos que no corre ningún workflow (`script_20*`, `script_37*`, `script_38b`, `script_40`) siguen leyendo `TELEGRAM_CHAT_ID`: si alguien los corre a mano, escriben al chat personal. | hardening | P3 |
| El paso de detección (`script_82`) recibe `TELEGRAM_BOT_TOKEN` sin usar Telegram (mínimo privilegio: se podría quitar). | hardening | P3 |
| **BotFather (Dirección):** `/setjoingroups` → Disable (nadie puede agregar el bot a otros grupos) y `/setprivacy` → Enable. | hardening | P1 (Dirección) |
| Bug en `script_82.score_token`: el tramo "Venta agresiva (buy_pressure < 30%) −35" está en un `elif` detrás de `< 40%`, así que nunca se alcanza (todo < 30% cae en −20). Encontrado al documentar el Anexo C del doc 24; no se tocó. | doc 24 | P2 |
| `script_82` guarda los motivos del score pero no los puntos: el desglose del dossier se reconstruye. Agregar `score_breakdown`. | doc 24 | P2 |
| Integración multi-chain: diseño en el doc 24 Anexo B (workflow propio, `script_115`, acumulado separado, `script_97` con dos fuentes, veredicto por grupo). Sin implementar. | doc 24 | P2 |
| El scanner multi-chain v0 no corre solo: engancharlo a un workflow requiere consulta. El grupo b (preventa) no tiene fuente gratuita en CoinGecko. | T5 | P2 |
| ~~`script_113` no está enganchado~~ Enganchado en la rama `claude/dossier-envio` (Fase 4). Falta el push (YIN) y verificar la primera alerta real en el grupo (Dirección). | Fase 3 | P1 |
| `bp_delta` inactivo en producción (ver §4): decidir si `script_82` persiste `buy_pressure` o se retira la componente. No tocado. | Fase 3 | P2 |
| La batería con `python -m unittest discover` falla `test_lib_narrative.test_demo_dry_run_three_chains`: `test_bots.py` y `test_script_114_scanner.py` fijan `SHOT_ROOT` al importarse y el demo lee el registro de narrativas desde ese tmp. Preexistente (falla igual en HEAD sin cambios). Por archivo pasa 193/193. | Fase 3 | P3 |
| Dossier: categoría y narrativa `n/d` (CoinGecko `coins/{id}` necesita resolver el id), ruta CEX sin verificar (`tickers`), PDF [P] sin librería verificada. | Fase 3 | P3 |
| Métrica de repetición (doc 26): Fase 0 sin implementar; antes, verificar las fuentes desde Actions. | Fase 3 | P2 |
| Sonda de fuentes desde Actions pendiente: `probe_narrative_sources.yml` es manual y necesita estar en main. Local: 6/6 familias, 14/17 endpoints (Reddit 429 por IP). | Fase 4 | P1 |
| Salida de sombra (`6ff13c5`) sin los criterios de §1.1 cumplidos (n = 2). La decisión es de Dirección; el monitor sigue midiendo por versión. | Fase 4 | P1 (Dirección) |
| El dossier suma ~7 requests (~10–15 s) por alerta antes del envío. Si una API se cuelga, el timeout es de 15 s por request; el peor caso es de ~2 min por alerta, dentro del límite de 15 min del job. | Fase 4 | P3 |

---

## 8. Próximos pasos

1. **Fase 4:** YIN commitea y pushea `claude/dossier-envio`. Después, Dirección verifica la primera alerta con dossier en el grupo y alguien dispara `probe_narrative_sources.yml` (manual) para medir las fuentes desde Actions.
2. **Repetición mediática (doc 26):** con ≥ 3 familias OK desde Actions y aprobación del workflow nuevo → Fase 0 como **colector propio** (doc 26 §9), sin tocar `script_82` / `script_97` ni el score. `lib_repetition.py` ya tiene parsers y fórmula.
3. **Medir la exposición a tokens < 60 min solo sobre alertas v7.2.1 (A-b)** (criterio < 20%). Al cierre, la muestra v7.2.1 era mínima (primaria 0/1) y no hubo alertas nuevas después de las 12:48 UTC.
4. Confirmar que el trust loop procesa bien las 7 `active_tracking` previas a SHADOW (A-c).
5. Dejar correr los bots; leer el DÍA N del monitor en `_cycle_log.json → shadow_monitor`.
6. Con n ≥ 20 primarias resueltas → veredicto automático al chat de operaciones → decisión de Dirección.
7. Si la primaria < 20% → gate a 30 min (rama aparte, sin merge sin validar).
8. Expansión por fases según el doc 23 (Fase 1 = Universo A con `arch`; el scanner v0 de T5 es la base para h/f/c), más las propuestas P1 del doc 23 §8: I-1 rug-después-del-hit en vivo, I-2 enriquecimiento de riesgo en sombra, I-3 guardia de sombra.

---

## Bitácora de sesiones

| Fecha | Sesión | Resultado |
|---|---|---|
| 2026-09-30 | Directiva ampliada (máximo aprovechamiento) | T1 v7.2.1 en main (sombra) · T2 fase2-p1 en main · T3 gate de edad 30 min · T4 advertencia crítica · bots gemelos desplegados y verificados (4/4 success) · 1.ª corrida v7.2.1 verificada (35/35 tokens 7.2.1, ≥56: 2/35) · doc 22 creado · doc 23 (8 grupos, 42 fuentes, 12 propuestas de innovación) · ops chat "La mano de Dios" operativo (confirmado) · 4 anomalías del primer resumen registradas en §7 (A-c P0) |
| 2026-09-30 (noche) | Post-incidente + mejoras operativas | Framing neutral en main (`c727ece`, aplicado por Dirección/YIN) · T1 resumen legible · T2 resumen idempotente · T3 alertas a personal + grupo, `--test-send`, pausa 0,5 s · T4 template con ACTIVO / DETECCIÓN / FUENTES · T5 scanner multi-chain v0 · push ff `77b2a1c..3694aa8` · 151/151 tests · test-send: personal OK, grupo sin secret · A-c: las `active_tracking` son todas previas a SHADOW |
| 2026-10-01 | Redirección exclusiva al grupo + hardening | `script_97`, `script_98` y `script_99` envían solo a `TELEGRAM_PUBLIC_CHAT_ID`; ningún workflow pasa `TELEGRAM_CHAT_ID`; bot solo emisor (sin `getUpdates`/webhooks/polling, verificado y con test de regresión); rama `claude/destino-grupo` sin push |
| 2026-10-01 (cont.) | Cierre de fase: push destinos + dossier | Push ff `b560a7a..2c44332` (destinos solo al grupo + hardening) · test-send: grupo OK · doc 24 (diseño del dossier por activo + anexo multi-chain), ejemplo VSOF con score 95 reproducido con el `script_82` de `be8e7d3` y 45 con v7.2.1 · BotFather pendiente (Dirección) · bug del tramo −35 inalcanzable registrado |
| 2026-10-01 (madrugada) | Fase 3: dossier + herramientas + repetición | Adquisición primero en main (`7d77b72`, YIN) · `script_113_dossier_builder.py` v1.0 (31 tests, 9/9 mutaciones, dry-run VSOF sin red, vivo con 6 fuentes gratuitas) · VSOF primaria cumplida [V] · doc 24 v1.2 (§7 implementación) · doc 25 (Agent-Reach no, Patchright Enhanced descartado — URL 404 y sin licencia, Scrapling condicional) · doc 26 (repetición: fórmula v0 + v0.1 con Poisson, entropía y suavizado; sombra → event study → bonus) · rama `claude/dossier-builder` sin commit (YIN) |
| 2026-10-01 (mañana) | Fase 4: dossier en la emisión + campos + sonda | `script_97` adjunta el dossier (sombra: guarda; real: `sendDocument` con caption que lleva el 🛒 completo y fallback a `sendMessage`); 11 tests + 6/6 mutaciones · `script_113`: ruta CEX confirmada por contrato, sin código de referido, y categorías (12/12 mutaciones) · `lib_repetition` + `probe_narrative_sources` + workflow manual (local 6/6 familias) · T4 sin implementar (falta la sonda desde Actions) · producción salió de sombra en `6ff13c5` (Dirección) · 237/237 tests · rama `claude/dossier-envio` sin push (YIN) |
