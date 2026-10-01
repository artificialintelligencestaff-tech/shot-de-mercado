---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: VIVO (se actualiza al cierre de cada sesión)
last_updated: 2026-09-30
version: 1.0
---

# 22 — Memoria persistente de Claude Code

Rótulos: [V] verificado (comando/archivo/API en esta sesión) · [I] inferido · [H] hipótesis · [P] pendiente.
Regla de uso: **leer este documento al empezar cada sesión** y actualizarlo al cerrarla (secciones 1, 4, 7, 8 como mínimo).
Si algo de acá contradice al repo, **manda el repo**: corregir este documento en la misma sesión.

---

## 1. Estado (cierre de sesión 2026-10-01 ~00:45 UTC)

| Componente | Estado | Rótulo |
|---|---|---|
| Emisión | **SHADOW** (`SHADOW_MODE: "true"`, `PAUSE_EMISSIONS: "false"` en `pipeline_t0.yml`). Las alertas se registran con `status: "shadow"` y `telegram_sent: false`. **No reactivar emisiones reales sin validar v7.2.1** (criterios en §1.1). | [V] |
| Scorer | **v7.2.1** en main desde 2026-09-30 (`SCORING_VERSION = "7.2.1"`, `ACCEL_GATE_MIN_AGE = 60`). Cada token lleva `detected_at` y `scoring_version`. 1.ª corrida de producción (`detection_2026-09-30_055022`): 35/35 tokens con 7.2.1, **≥ 56: 2/35** (vs 19/29 y 23/33 en las dos corridas v7.2 previas). | [V] |
| Filtros de emisión (script_97) | umbral `EMIT_MIN_SCORE = 56` · frescura R1 `CANDIDATE_MAX_AGE_MIN = 60` · **edad mínima del par `EMIT_MIN_AGE_MIN = 30`** (edad desconocida → no emite) · dedup PARASITE. | [V] |
| Plantilla Telegram | **Framing neutral** (`c727ece`, Dirección): el proyecto informa con datos y método; **no juzga, no advierte, no disuade: el usuario decide**. Sin "ADVERTENCIA", sin "plan sugerido", sin "no invertir más de…". Bloques: 🪪 ACTIVO (nombre, chain, mint, creador) · 🕒 DETECCIÓN (hora, edad del par, creación del par, ventana < 48 h) · 🎯 PROBABILIDADES (primaria, secundaria y "después de tocar +20%, llegar a ≤ −99%" como **métrica**, no advertencia; "en validación" hasta `validated: true`) · 📊 DATOS · 🔎 motivos · 🛒 cómo adquirirlo · 🔗 FUENTES VERIFICABLES (Solscan, DexScreener, pump.fun) · seguimiento. "n/d" para lo desconocido; Markdown de datos externos escapado (T4 `06fedff`). | [V] |
| Trust loop (script_98) | Solo procesa `status == "active_tracking"` (ignora sombra). | [V] |
| Bots gemelos | `monitor_shadow_bot` (6 h), `health_check_bot` (2 h), `autorepair_bot` (4 h), `daily_summary_bot` (06:00 UTC). Los 4 verificados con workflow_dispatch el 2026-09-30 05:50 UTC (success + commit de su log). | [V] |
| Telegram de operaciones | Los bots escriben SOLO a `TELEGRAM_OPS_CHAT_ID` (grupo "La mano de Dios"). Secret cargado por Dirección el 2026-09-30 06:05 UTC; primer envío (resumen diario por dispatch, run 36677130640) a las 06:13 UTC con `notified: sent`. | [V] API · **recepción confirmada por Dirección** |
| Destinos de Telegram | **Mercado** (alertas `script_97`, trust updates `script_98`, pre-launch `script_99`) → `TELEGRAM_PUBLIC_CHAT_ID`. **Sistema** (4 bots, `lib_ops`) → `TELEGRAM_OPS_CHAT_ID`. Los dos apuntan al grupo privado "La mano de Dios" (solo owner + bot), con prefijos distintos [reportado por Dirección]. **Chat personal (`TELEGRAM_CHAT_ID`) deprecado:** ningún script de producción lo lee y ningún workflow lo pasa. `--test-send` / `telegram_test_send.yml` apuntan solo al grupo. Rama `claude/destino-grupo` (`77c441a`, `e69ea5e`, `bbf9d1a`, `5816a1b`), **sin push**. Antes de este cambio, el test-send llegó a ambos destinos (confirmado por Dirección). | [V] código y tests · push [P] |
| Resumen diario (ops) | Formato legible por secciones, calidad separada por versión (T1 `7b14a58`); un envío por día UTC con `last_sent_date`, `--force` para reenviar (T2 `dd48a77`). | [V] |
| Scanner multi-chain v0 | `script_114_multichain_scanner.py` (T5 `3694aa8`): grupos h, f, c, g, d, e (CoinGecko sin key) + a (GeckoTerminal: solana, base, eth, blast, monad). Solo recolección + marca de aceleración [H]; sin score, sin emisión, **no enganchado a ningún workflow**. Humo real: 13 llamadas, 0 errores. | [V] |
| Tests | **151/151** (11 archivos `04_Config/scripts/test_*.py`, unittest, sin red). | [V] |
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

---

## 5. Herramientas y fuentes (gratuitas, verificadas)

| Herramienta | Uso | Límite observado | Rótulo |
|---|---|---|---|
| GeckoTerminal API v2 (OHLCV minuto) | velas para la métrica dual | 429 frecuentes → intervalo 6,5 s + reintentos con backoff; cache/offline en calibrate | [V] |
| DexScreener | pares, `pairCreatedAt`, m5/h1 | sin key | [V] |
| Jupiter Tokens V2 (`api.jup.ag`) | dev, audit, holders, verificación (Cap. II) | sin key; **no** `lite-api.jup.ag` | [V] |
| Wikipedia Pageviews / Wikidata SPARQL | señales de atención (Universo A/B) | sin key | [V] |
| Binance data-api | velas Universo A | público | [V] |
| `gh` CLI / API REST de GitHub | runs, jobs, issues (bots) | GITHUB_TOKEN del workflow | [V] |

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
| El scanner multi-chain v0 no corre solo: engancharlo a un workflow requiere consulta. El grupo b (preventa) no tiene fuente gratuita en CoinGecko. | T5 | P2 |

---

## 8. Próximos pasos

1. **Push de `claude/destino-grupo`** (todo mensaje de mercado solo al grupo + hardening), pendiente de autorización. Después: re-disparar `telegram_test_send` (esperado: grupo OK; el chat personal no recibe nada).
2. **Próxima fase: knowledge sheet / dossier por activo** (Dirección, sesión 2). Diseñar primero el template y después `script_113_dossier_builder.py` (nombre tentativo). Un dossier por alerta con: (1) identificación completa (nombre, symbol, mint, chain, deployer, auditoría); (2) método de detección: datos usados, cálculos, probabilidad; (3) vigencia de la señal; (4) adquisición paso a paso; (5) fuentes verificables; (6) documentación de cálculos para que el usuario audite el método. Información educativa, sin secciones de advertencia.
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
