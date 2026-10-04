---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: VIVO (se actualiza al cierre de cada sesión)
last_updated: 2026-10-01
version: 1.4
---

# 22 — Memoria persistente de Claude Code

Rótulos: [V] verificado (comando/archivo/API en esta sesión) · [I] inferido · [H] hipótesis · [P] pendiente.
Regla de uso: **leer este documento al empezar cada sesión** y actualizarlo al cerrarla (secciones 1, 4, 7, 8 como mínimo).
Si algo de acá contradice al repo, **manda el repo**: corregir este documento en la misma sesión.

---

## 1. Estado (sesión 2026-10-01 tarde, ~15:00 UTC)

`origin/main` = `8b1c62b` (commits de los crons encima de `a537c08`, que cierra la Fase 4) [V].

| Componente | Estado | Rótulo |
|---|---|---|
| **D-023-R3, rama** | Scorer joven 0.4: pesos continuos por edad (70/15/15 → 20/20/60, mínimo 15), estructural 12/6/3 + S-1..S-4 (velocidad de curva, aceleración de compradores únicos, tendencia del tamaño de compra, holders/txns); umbral 40, info mínima 5. Liquidez inicial = flag. `tradability` en todas las alertas (early watch y script_97). El listener de PumpPortal suscribe trades de ≤ 100 jóvenes (campos del evento [I]). Doc 32 v0.4 (marco + v7.2.2 propuesto), doc 33 v0.2 (Reddit: 403 por bloqueo a datacenter → OAuth oficial gratis recomendado; RSS con URLs; Nitter: 1–6 instancias vivas, `status.d420.de`). | [V] tests · [P] producción |
| **D-014-R-5, rama** | Scorer joven v0.3: umbral 40, mínimo informacional 10; cada alerta registra `info_score` / `struct_score` / `pv_score` / `h0_group`. H-0 pre-registrada (doc 32 §6; Fisher exacto a una cola, α 0,10, n ≥ 40), evaluada por `early_review`. Doc 33: arquitectura multi-bot (sin implementar), 12 feeds RSS [P] y tabla de MCP servers. nkd077 = baseline de calibración, no refutación (mide graduación). | [V] tests · [P] fuentes |
| **Scorer joven v0.2 (D-014-R-3), rama** | < 60 min: 60 % informacional (menciones, ola de nombres, trending, metadata IPFS, perfil DexScreener, repo GitHub) / 25 % estructural (curva, holders, dev; kill switches a 0) / 15 % precio-volumen. Emite con score ≥ 50 e info ≥ 20, liquidez 0 aceptada, sin sombra. script_116 116-0.3 lo envuelve (≥ 60 min sigue v7.2.1). JSONL por token en `02_Analisis/early/young/`. Bloqueo: el almacén de menciones tiene 43 ítems en 26 h. Doc 32 v0.2. | [V] tests · [P] producción |
| **Fase 12 MVP (D-014-R), rama** | Diseño en doc 32 + `lib_scoring_young.py` aislado (sin integrar) + `young_watch_analysis.py`. Datos [V] de 4 h de watch: 5 de 9 señales aplican a tokens jóvenes; las ≥ 3 activas son el mismo trío de flujo (16 mints); el 95,6 % de los jóvenes tiene liquidez 0 en DexScreener. Sin outcomes, la discriminación no se conoce: hace falta un registro en sombra por token (pendiente de aprobación). | [V] datos · [P] outcome |
| **Fase 11 — base real (main 407da0e)** | La Fase 10b está en main y corriendo. Early watch: 3 alertas (HOOKED, silent, Nike). **Nike salió con 55+1 a los 25 min y cayó −99,8 % a t+1h.** El mínimo de 10 min no limita: con v7.2.1 los lanzamientos casi no llegan a 56 (máx. 49 en 20 polls). 2 bugs propios corregidos en la rama: estado leído antes del pull (checkout del SHA encolado) y stdout bufferizado. Doc 31 §10. | [V] |
| **Fase 10b** (rama, sin merge) | La edad mínima del early watch baja a **10 min** (Dirección). `early_review.yml` (cada 6 h) la sube a 15 si la primaria de las alertas con gate 10 da < 40 % tras 24 h. Hay **dos early watch** desfasados (a :07/:37, b :22/:52) con reclamo por mint vía git (`early/alerts/<mint>.json`): sin doble emisión y con cobertura de PumpPortal medida (`listener_intervals`). Order book en Solana: Raydium CLMM (`clmm_imbalance`) y Phoenix como 3.er respaldo de perps. Workers: factible con Durable Object, no implementado (doc 31 §9). | [V] código/tests · [P] producción |
| **Fase 10 — detección temprana** (rama, sin merge) | **Latencia medida:** gap inicio del pump → emisión de **39,6–43,3 min**, acotado por el snapshot (4 alertas con pump desde el lanzamiento). Detección → emisión: mediana 38,4 min. Scheduler de Actions: +11,9 min de media sobre `*/20`. Escucha de PumpPortal: 5 de cada 20 min. **Nuevo:** `script_116_early_watch` + `early_watch.yml`, con poll **cada 2 min** dentro de un job de 40 min, PumpPortal en continuo, re-scoring v7.2.1 + bono anticipatorio (`lib_early_signals`, 9 señales, tope +8, solo suma) y order book de Hyperliquid/dYdX para multi-chain. `script_97` le cede la ruta Solana mientras corre y adopta sus alertas. Doc 31. | [V] código/tests · [P] producción |
| Emisión | **Emisiones reales activas desde `6ff13c5`** (01/10 03:48 UTC): `SHADOW_MODE: "false"` en `pipeline_t0.yml`, destino **grupo privado** "La mano de Dios". Decisión de Dirección. Desde entonces `script_97` registró **2 alertas `active_tracking`**: DEGEN (`4vEX32…pump`, 04:12 UTC, score 100) y arc (`61V8vB…pump`, 08:40 UTC, score 72, con dossier). | [V] |
| Entrega a Telegram | **Resuelta** (Dirección, 01/10 15:32 UTC): el grupo había migrado a supergrupo y los envíos daban 400. Secrets actualizados y `telegram_test_send` OK [reportado]. Detalle en §1.2. DEGEN y arc quedaron sin entregar. | [V] log · [reportado] fix |
| Scorer | **v7.2.1** en main desde 2026-09-30 (`SCORING_VERSION = "7.2.1"`, `ACCEL_GATE_MIN_AGE = 60`). Cada token lleva `detected_at` y `scoring_version`. 1.ª corrida de producción (`detection_2026-09-30_055022`): 35/35 tokens con 7.2.1, **≥ 56: 2/35** (vs 19/29 y 23/33 en las dos corridas v7.2 previas). | [V] |
| Filtros de emisión (script_97) | umbral `EMIT_MIN_SCORE = 56` · frescura R1 `CANDIDATE_MAX_AGE_MIN = 60` · **edad mínima del par `EMIT_MIN_AGE_MIN = 30`** (edad desconocida → no emite) · dedup PARASITE. | [V] |
| Plantilla Telegram | **Framing neutral** (`c727ece`, Dirección): el proyecto informa con datos y método; **no juzga, no advierte, no disuade: el usuario decide**. Sin "ADVERTENCIA", sin "plan sugerido", sin "no invertir más de…". Bloques: 🪪 ACTIVO (nombre, chain, mint, creador) · **🛒 CÓMO ADQUIRIRLO primero** (guía por chain: wallets, fondeo, DEX + alternativas, 8 pasos, slippage por liquidez + impacto, verificación; **chain sin guía o sin mint = no se emite**, `acquisition_ready`; `7d77b72`, en main, commit y push de YIN) · 🕒 DETECCIÓN (hora, edad del par, creación del par, ventana < 48 h) · 🎯 PROBABILIDADES (primaria, secundaria y "después de tocar +20%, llegar a ≤ −99%" como **métrica**, no advertencia; "en validación" hasta `validated: true`) · 📊 DATOS · 🔎 motivos · 🔗 FUENTES VERIFICABLES (Solscan, DexScreener, pump.fun) · seguimiento. "n/d" para lo desconocido; Markdown de datos externos escapado (T4 `06fedff`). | [V] |
| Trust loop (script_98) | Solo procesa `status == "active_tracking"` (ignora sombra). | [V] |
| Bots gemelos | `monitor_shadow_bot` (6 h), `health_check_bot` (2 h), `autorepair_bot` (4 h), `daily_summary_bot` (06:00 UTC). Los 4 verificados con workflow_dispatch el 2026-09-30 05:50 UTC (success + commit de su log). | [V] |
| Telegram de operaciones | Los bots escriben SOLO a `TELEGRAM_OPS_CHAT_ID` (grupo "La mano de Dios"). Secret cargado por Dirección el 2026-09-30 06:05 UTC; primer envío (resumen diario por dispatch, run 36677130640) a las 06:13 UTC con `notified: sent`. | [V] API · **recepción confirmada por Dirección** |
| Destinos de Telegram | **Mercado** (alertas `script_97`, trust updates `script_98`, pre-launch `script_99`) → `TELEGRAM_PUBLIC_CHAT_ID`. **Sistema** (4 bots, `lib_ops`) → `TELEGRAM_OPS_CHAT_ID`. Los dos apuntan al grupo privado "La mano de Dios" (solo owner + bot), con prefijos distintos [reportado por Dirección]. **Chat personal (`TELEGRAM_CHAT_ID`) deprecado:** ningún script de producción lo lee y ningún workflow lo pasa. `--test-send` / `telegram_test_send.yml` apuntan solo al grupo. **En main** (push ff `b560a7a..2c44332`). Test-send run 36799931771: **grupo OK**, un solo destino en el log (el chat personal no se intentó). | [V] |
| Resumen diario (ops) | Formato legible por secciones, calidad separada por versión (T1 `7b14a58`); un envío por día UTC con `last_sent_date`, `--force` para reenviar (T2 `dd48a77`). | [V] |
| Scanner multi-chain v0 | `script_114_multichain_scanner.py` (T5 `3694aa8`): grupos h, f, c, g, d, e (CoinGecko sin key) + a (GeckoTerminal: solana, base, eth, blast, monad). Solo recolección + marca de aceleración [H]; sin score, sin emisión, **no enganchado a ningún workflow**. Humo real: 13 llamadas, 0 errores. | [V] |
| Tests | **302/302** (Fase 7: + lib 19, multi-chain 9, scanner 1) · **273/273** (Fase 6: + `test_script_97_guias.py` 6/6) · antes **267/267** corriendo **cada archivo por separado** (17 archivos `04_Config/scripts/test_*.py`, unittest, sin red): 237 previos + 20 de `script_115` + 10 nuevos de `script_114`. Mutation testing: `script_115` 10/10, `script_114` 12/12. Con `unittest discover` falla 1 test preexistente (ver §7). | [V] |
| Dossier por activo | **En producción, adjunto a cada alerta** (Fase 4 en main: `15e9d1a` envío, `547c288` ruta CEX + categorías). `script_97` arma el dossier (`script_113` v1.1) y lo manda con `sendDocument` al grupo, con caption ≤ 1024 que lleva el 🛒 completo y fallback a `sendMessage`. Primer dossier real: arc, `02_Analisis/dossiers/solana/61V8vB…pump.md` (08:40 UTC), guardado pero no entregado por la migración a supergrupo. Doc 24 §8–§9. | [V] |
| Alertas acumuladas (`_all_alerts.json` en `8b1c62b`) | 37 en total: **26 `shadow`**, **9 `active_tracking`** (7 previas a SHADOW + DEGEN y arc), 2 `DESCARTAR_NOPAR`. `telegram_sent: true` = 0. | [V] |
| Sonda de fuentes de menciones | **Disparada desde Actions** (run `36818939038`, 05:17 UTC): **5/6 familias OK** (Reddit RSS, Telegram `t.me/s`, 4chan, HN, RSS de noticias; falla GDELT) y **12/17 endpoints**. `phase0_enabled_by_probe: true` → **Fase 0 del doc 26 habilitada**. | [V] |
| Colector de menciones (T1, Fase 5) | `script_115_narrative_collector.py` + `narrative_collector.yml` (cada 20 min, minutos 7/27/47). Rama `claude/zealous-tesla-3ua19i`; YIN integra. Doc 26 §10. | [V] rama |
| Scanner multi-chain (T2, Fase 5) | `script_114` v0.2 reescrito desde la v0.1 de main: fichas por chain, `_categories.json`, `_history.jsonl`; `scan_latest.json` sin cambios de esquema. Workflow `multichain_scanner.yml` cada 1 h. Misma rama. | [V] rama |
| Scoring multi-chain | **Fase 7:** `lib_scoring_multichain.py` (9 tipos) + emisión multi-chain en `script_97` después de la ruta Solana (umbral 56, cobertura ≥ 0,6, 2 por ciclo, 3 por grupo/24 h, ventana 48 h; compra por guía de chain o CEX confirmado por CoinGecko). `script_114` v0.3 con Universo A y TVL por protocolo. Workflows verificados: `narrative_collector` runs 36888458264 y 36891676219 success; `multichain_scanner` run 36893644532 (dispatch) success, 8 fichas y 7 categorías completas. Doc 27 §8. | [V] |
| Hashes de cierre | **Sesión Fase 5 (rama `claude/zealous-tesla-3ua19i`, sin merge):** docs 22/24 `b317bb0` · T1 `cc69b00` · T2 `44eba49` · doc 27 `784b4ec` · cierre (doc 22) en el commit siguiente. Sesión 1: T3 `26ce5b7` · T4 `3ef7b50` · bots `daf9cc4` · docs 22/23 `63a1b95`. Sesión 2: framing `c727ece` (aplicado por Dirección/YIN) · push fast-forward `77b2a1c..3694aa8` con T1 `7b14a58` · T2 `dd48a77` · T3 `ba44f21` + `68953b8` · T4 `06fedff` · T5 `3694aa8`. | [V] |
| Incidente | Dirección reportó el sistema caído y luego **recuperado** ("GitHub Actions funcionando") [reportado]. Verificación propia: `pipeline_t0` y `trust_update` con runs `success` cada ~20 min hasta 23:05 UTC. | [V] |

### 1.1 Criterios de calibración de v7.2.1 (métrica, no condición de emisión)

Corrección de Dirección (01/10): el destino es el **grupo privado**, así que estos umbrales **no condicionan la emisión**. Exigir n ≥ 20 antes de emitir era un sesgo sobreextendido y se retira. Siguen siendo la vara con la que el monitor mide el scorer y con la que `emission_calibration.json` pasa a `validated: true` (las probabilidades del mensaje dejan de decir "en validación").

- Primaria (toca +20% antes de −30%, 48 h) **≥ 30%** con **IC90 inferior > 15%** (baseline 10,5%).
- Secundaria (cierre ≥ +20% a 48 h) **≥ 5%** con IC90 inferior > 2%.
- Exposición a tokens < 60 min **< 20%**.
- Tests 100%.
- **Si la primaria da < 20%** → relajar el gate a 30 min (no a 0).
- El veredicto lo avisa `monitor_shadow_bot` una sola vez (clave `verdicts["shadow_verdict:7.2.1"]` en `_cycle_log.json`).


### 1.2 Incidente 01/10 — Migración del grupo a supergrupo

| Campo | Detalle | Rótulo |
|---|---|---|
| Síntoma | Telegram devolvía `400 "Bad Request: group chat was upgraded to a supergroup chat"` con `parameters.migrate_to_chat_id`, tanto en `sendDocument` como en el fallback `sendMessage` (job `110287433551`, run `36837216844`, 08:40 UTC). | [V] log |
| Causa | "La mano de Dios" migró de grupo a supergrupo y el `chat_id` cambió. Los secrets apuntaban al ID viejo. | [V] |
| Afectados | DEGEN (`4vEX32…pump`, 04:12 UTC) y arc (`61V8vB…pump`, 08:40 UTC): no entregados; quedaron `telegram_sent: false` y no se reenvían (dedup por mint). Resumen diario del 01/10 (06:22 UTC): `notified: error:HTTPError`. | [V] registros · [I] el resumen, misma causa |
| Nuevo `chat_id` | `-1004390468812` (el `migrate_to_chat_id` del log). | [V] log |
| Fix aplicado | 3 secrets actualizados por Dirección, 01/10 15:32 UTC. | [reportado] |
| Verificación | `telegram_test_send` OK. | [reportado] |
| Prevención [P] | Cuando se reactive, `health_check_bot` detecta el error: (a) busca `upgraded to a supergroup` / `migrate_to_chat_id` en los logs de `pipeline_t0` y de los bots; (b) marca alertas `active_tracking` recientes con `telegram_sent: false`. Avisa una vez al chat de operaciones con el ID nuevo. Si el chat de operaciones es el mismo grupo, el aviso tampoco llega: hace falta un issue de GitHub como canal de respaldo (como `autorepair_bot`). | — |

---

## 2. Arquitectura (lo que necesito tener en la cabeza)

```
GitHub Actions (cron, repo artificialintelligencestaff-tech/shot-de-mercado, rama main)
├── pipeline_t0.yml   */20  → script_82 (detección+score) → script_97 (emisión/sombra) → commit
├── trust_update.yml  */20  → script_98 (trust loop sobre active_tracking) → commit
├── prelaunch.yml     0 */6
├── probe-fuentes.yml       (sondas de fuentes)
│   concurrency: repo-write-main (los 3 de producción)
├── narrative_collector.yml 7,27,47 * * * * → script_115 (menciones, doc 26 Fase 0) → commit solo 02_Analisis/narrative/
├── multichain_scanner.yml  35 * * * *     → script_114 v0.2 (fichas por chain + categorías) → commit solo 02_Analisis/multichain/
│   (los dos con concurrency propia ops-<workflow>; sin secretos; sin envíos; no tocan el score)
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
- **Sesiones en la nube (Claude Code remoto):** Linux, clon nuevo, rama asignada por la sesión (hoy `claude/zealous-tesla-3ua19i`). Se pushea solo a esa rama, sin `--force`; YIN integra a main tras la auditoría de YANG. El contenedor no tiene salida a las APIs del proyecto: los tests son sin red y la verificación en vivo es un `workflow_dispatch`. Los logs de Actions se leen con las herramientas de GitHub de la sesión.

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
| Grupo migrado a supergrupo | Telegram rechaza los envíos al ID viejo con 400 "group chat was upgraded to a supergroup chat" y devuelve `migrate_to_chat_id`. Ninguna de las 2 alertas reales del 01/10 llegó. | [V] | 22 §1 |
| arc puntuado como memecoin | Activo de 621,7 días ($10,3 M de liquidez, categorías AI/Infra) sacó 72 con v7.2.1: +25 de buy pressure con 5 compras / 0 ventas y +15 de aceleración con $64 de volumen m5 (rotación m5/L 6,2·10⁻⁶). El origen pump.fun no alcanza para clasificar. | [V] | 27 §2, §6.1 |
| Candidatos ≥ 40 por versión | En 48 h hay 59 tokens ≥ 40, pero 45 tienen score de v7.2 (inflado); con el scorer vigente (7.2.1) quedan 14. El colector filtra por versión. | [V] | 26 §10 |
| Latencia estructural | Las alertas Solana salen con el par en ~44 min de edad (mediana) aunque script_82 las ve a los ~4,5 min. El piso es gate 30 + media cadencia 10. En 5 de 12 alertas, el snapshot con el que se emitió ya mostraba ≥ +100 %. El scheduler de Actions atrasa `*/20` 11,9 min de media (máx 19,6). | [V] | 31 §1 |
| `score_token` relee 11 MB | `script_82.score_token` abre y parsea `_accumulated.json` (10,9 MB, 6.956 registros) **en cada llamada** para un `buy_pressure` que nunca existe (0/6.956). Inocuo en pipeline_t0 (pocas llamadas); en el early watch se evita llamándolo desde un cwd vacío (mismo resultado, test de paridad). | [V] | 31 §3 |
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
2. [P] Con la edad mínima de 30 min y el gate de 60 min, ¿alcanza el volumen para que el monitor llegue a n ≥ 20 primarias (veredicto de calibración) en un plazo razonable? Desde la salida de sombra hubo 2 alertas en ~11 h. El monitor lo va a mostrar en el DÍA N.
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
| ~~`script_113` no está enganchado~~ **En main** (`15e9d1a`). Primer dossier real generado (arc, 08:40 UTC); la entrega quedó bloqueada por la migración a supergrupo (ver la fila siguiente). | Fase 3 | — |
| ~~**Grupo migrado a supergrupo**~~ **Resuelta** (Dirección, 01/10 15:32 UTC; §1.2). Queda la prevención: el health check detecta el 400 de migración (`migrate_to_chat_id`). | Fase 5 | P2 (prevención) |
| `script_97` no reintenta con `migrate_to_chat_id`: si el chat vuelve a migrar, las alertas se registran con `telegram_sent: false` y no se reenvían. Opción: el health check marca `telegram_sent: false` en alertas `active_tracking` recientes (invariante "emisión real = enviada"). | Fase 5 | P2 |
| `bp_delta` inactivo en producción (ver §4): decidir si `script_82` persiste `buy_pressure` o se retira la componente. No tocado. | Fase 3 | P2 |
| La batería con `python -m unittest discover` falla `test_lib_narrative.test_demo_dry_run_three_chains`: `test_bots.py` y `test_script_114_scanner.py` fijan `SHOT_ROOT` al importarse y el demo lee el registro de narrativas desde ese tmp. Preexistente (falla igual en HEAD sin cambios). Por archivo pasa 193/193. | Fase 3 | P3 |
| Dossier: categoría y narrativa `n/d` (CoinGecko `coins/{id}` necesita resolver el id), ruta CEX sin verificar (`tickers`), PDF [P] sin librería verificada. | Fase 3 | P3 |
| ~~Métrica de repetición (doc 26): Fase 0 sin implementar~~ Implementada como colector propio (`script_115`, T1 Fase 5), en la rama hasta que YIN integre. El dossier todavía no lee `02_Analisis/narrative/<mint>.json`. | Fase 3 | P2 |
| ~~Sonda de fuentes desde Actions pendiente~~ **Disparada** (run `36818939038`): 5/6 familias, 12/17 endpoints; falla GDELT; Reddit 1/5. | Fase 4 | — |
| ~~Salida de sombra sin los criterios de §1.1 (n = 2)~~ **Retirada** (Dirección, 01/10): el destino es el grupo privado; n ≥ 20 es criterio de calibración (§1.1), no de emisión. | Fase 4 | — |
| El contenedor en la nube de Claude Code no tiene salida a las APIs del proyecto (DefiLlama, CoinGecko, GeckoTerminal, Reddit, 4chan…: el proxy responde 403 a `CONNECT`). Las pruebas de T1/T2 se hicieron sin red; la verificación en vivo es el primer `workflow_dispatch` en Actions. Se habilita en la configuración de red del entorno. | Fase 5 | P3 |
| El dossier suma ~7 requests (~10–15 s) por alerta antes del envío. Si una API se cuelga, el timeout es de 15 s por request; el peor caso es de ~2 min por alerta, dentro del límite de 15 min del job. | Fase 4 | P3 |

---

## 8. Próximos pasos

0. **Fase 10b:**
   - Integrar y disparar `early_watch.yml` y `early_watch_b.yml`.
   - A las 24 h, `early_review.yml`: cobertura (union) y decisión de la edad mínima.
   - `latency_analysis.yml` para el gap con velas.
   - Workers solo si la cobertura < ~95 %.
   **Fase 10:**
   - YIN integra la rama.
   - `workflow_dispatch` de `early_watch.yml`: mirar `02_Analisis/early/_watch.json` (watch_size, listener_seen, top).
   - A las 24–48 h, `latency_analysis.yml` para el gap con velas de 1 min y el % de alertas dentro de los 5 min.
   - Decisión de Dirección/YANG: `EARLY_MIN_AGE_MIN` (gate 30 de v7.2.1). Es el piso que queda; con gate G la
     latencia mínima es G + 1 min.
1. ~~**P0 (Dirección):** secrets del supergrupo~~ **Hecho** (§1.2). Fase 6: guías de compra de Arbitrum, Optimism y Blast en `script_97` (Monad sin DEX: no emite) y grupo i en el doc 27.
2. **YIN integra `claude/zealous-tesla-3ua19i`** (T1, T2, T3, docs 22/24/26) tras la auditoría de YANG. Después, `workflow_dispatch` de `narrative_collector.yml` y `multichain_scanner.yml` para la verificación en vivo desde Actions (primer uso real de las rutas de DefiLlama `overview/dexs` y `overview/fees` por chain, y de CoinGecko `coins/categories`).
3. **Dossier ← colector:** `script_113` lee `02_Analisis/narrative/<mint>.json` y lo muestra en 🔬 Método / ⏱️ Vigencia como dato (sin tocar el score).
4. **Fase 1 del doc 26:** event study de la intensidad al detectar contra la métrica dual, cuando haya ≥ 20 tokens por tramo.
5. **Doc 27 → implementación por grupo** en el orden h → f → c → e/g → b/d, cada uno con su `scoring_version` y su medición propia.
6. **Medir la exposición a tokens < 60 min solo sobre alertas v7.2.1 (A-b)** (criterio < 20%).
7. Confirmar que el trust loop procesa bien las `active_tracking` (A-c), incluidas DEGEN y arc.
8. Dejar correr los bots; leer el DÍA N del monitor en `_cycle_log.json → shadow_monitor`. Con n ≥ 20 primarias resueltas → veredicto de calibración al chat de operaciones.
9. Si la primaria < 20% → gate a 30 min (rama aparte).
10. Propuestas P1 del doc 23 §8: I-1 rug-después-del-hit en vivo, I-2 enriquecimiento de riesgo, I-3 guardia de sombra (adaptarla: hoy aplica "emisión real = `telegram_sent: true`").

---

## Bitácora de sesiones

| Fecha | Sesión | Resultado |
|---|---|---|
| 2026-10-01 (noche, Fase 10b) | Ajustes post-integración | T1: edad mínima 10 (`script_116`), `_gate.json` + `early_review.py`/`.yml` (primaria < 40 % tras 24 h → 15) · T2: `early_watch_b.yml` (:22/:52), reclamos por mint (`Git.claim`), archivos por instancia, hand-off y adopción de las dos instancias en script_97, cobertura por `listener_intervals` · T3: Workers explorado (CPU de 10 ms en cron; Durable Object con WebSocket ≈ 10.800 de 13.000 GB-s/día; requiere port a JS y cuenta) · T4: Raydium CLMM integrado, Phoenix de respaldo, Orca/Meteora encontrados [P], OpenBook sin REST · 386/386 |
| 2026-10-01 (noche, Fase 10) | Detección temprana | T1 `latency_analysis.py` + `.json`: gap 39,6–43,3 min [V snapshot], scheduler +11,9 min, escucha 5/20 min · T2 `lib_early_signals` (9 señales, bono ≤ 8, solo suma; 17 tests) · T3 `script_116` + `early_watch.yml` (poll 2 min, PumpPortal continuo, paridad con script_97; 12 tests) · T4 Hyperliquid l2Book + dYdX (GMX sin libro, Jupiter lite prohibida) · T5 RugCheck holders/top-10 · T6 script_115 → `social_velocity` (X sin fuente gratuita) · script_97 hand-off + adopción + bono multi-chain (6 tests) · 370/370 · doc 31 |
| 2026-09-30 | Directiva ampliada (máximo aprovechamiento) | T1 v7.2.1 en main (sombra) · T2 fase2-p1 en main · T3 gate de edad 30 min · T4 advertencia crítica · bots gemelos desplegados y verificados (4/4 success) · 1.ª corrida v7.2.1 verificada (35/35 tokens 7.2.1, ≥56: 2/35) · doc 22 creado · doc 23 (8 grupos, 42 fuentes, 12 propuestas de innovación) · ops chat "La mano de Dios" operativo (confirmado) · 4 anomalías del primer resumen registradas en §7 (A-c P0) |
| 2026-09-30 (noche) | Post-incidente + mejoras operativas | Framing neutral en main (`c727ece`, aplicado por Dirección/YIN) · T1 resumen legible · T2 resumen idempotente · T3 alertas a personal + grupo, `--test-send`, pausa 0,5 s · T4 template con ACTIVO / DETECCIÓN / FUENTES · T5 scanner multi-chain v0 · push ff `77b2a1c..3694aa8` · 151/151 tests · test-send: personal OK, grupo sin secret · A-c: las `active_tracking` son todas previas a SHADOW |
| 2026-10-01 | Redirección exclusiva al grupo + hardening | `script_97`, `script_98` y `script_99` envían solo a `TELEGRAM_PUBLIC_CHAT_ID`; ningún workflow pasa `TELEGRAM_CHAT_ID`; bot solo emisor (sin `getUpdates`/webhooks/polling, verificado y con test de regresión); rama `claude/destino-grupo` sin push |
| 2026-10-01 (cont.) | Cierre de fase: push destinos + dossier | Push ff `b560a7a..2c44332` (destinos solo al grupo + hardening) · test-send: grupo OK · doc 24 (diseño del dossier por activo + anexo multi-chain), ejemplo VSOF con score 95 reproducido con el `script_82` de `be8e7d3` y 45 con v7.2.1 · BotFather pendiente (Dirección) · bug del tramo −35 inalcanzable registrado |
| 2026-10-01 (madrugada) | Fase 3: dossier + herramientas + repetición | Adquisición primero en main (`7d77b72`, YIN) · `script_113_dossier_builder.py` v1.0 (31 tests, 9/9 mutaciones, dry-run VSOF sin red, vivo con 6 fuentes gratuitas) · VSOF primaria cumplida [V] · doc 24 v1.2 (§7 implementación) · doc 25 (Agent-Reach no, Patchright Enhanced descartado — URL 404 y sin licencia, Scrapling condicional) · doc 26 (repetición: fórmula v0 + v0.1 con Poisson, entropía y suavizado; sombra → event study → bonus) · rama `claude/dossier-builder` sin commit (YIN) |
| 2026-10-01 (noche, Fase 9) | Datasets + inventario 174 + persistencia | `dataset_builder.py` + `datasets_build.yml`: MemeChain (Zenodo, solo CSV; índice de tasas base por chain/narrativa → umbral del grupo a multi-chain [H]) y Binance diario completo (BTC/ETH/SOL + GARCH) · inventario 91 → 174 (22 MCP nuevos, Pumpfun Corpus de HF como P0) · `lib_persist`: bitácora por operación (`02_Analisis/operations/`) y dataset propio `historical_alerts.jsonl` (backfill 37 alertas; outcome 48–50 h desde `script_98`) · doc 30 (protocolo; el 29 es la memoria de YIN) · Zenodo bloqueado en el contenedor: el índice real sale de la primera corrida en Actions |
| 2026-10-01 (noche, Fase 8) | Inventario + activación de grupos | Doc 28 (91 servicios, 68 con endpoint, 9/9 grupos) + `probe_inventario.yml` (manual) · trust loop CEX (`active_tracking_cex`: Binance → Coinbase → Kraken) · `script_114` v0.4: Snapshot, fees por protocolo, todos los perps de Hyperliquid con historial de OI, Aevo pre-mercado · lib 0.2: c con fees + Snapshot, e con ingresos de red, g con yield, d emite con funding/OI/basis, b registra · grupo i en el flujo Solana (`script_82.apply_group_i`: par > 180 días → registro; arc → 0) · `main` todavía sin la Fase 7 (YIN) |
| 2026-10-01 (noche, cont.) | Fase 7: cobertura multi-chain | Workflows verificados en Actions (colector 2/2 success, scanner disparado: success) · `lib_scoring_multichain` (19 tests) · `script_114` v0.3 · emisión multi-chain en `script_97` (9 tests, mutación 7/7) · humo con el scan real: 273 activos, 13 emitibles · 302/302 tests |
| 2026-10-03 (D-041) | Enjambre: normalización, reparador, grafo, auditoría, Telegram, método por grupo | T1 `lib_normalize` (#19; en escritura y fusión; 208/731 ítems cambiarían) · T2 `bot_self_repair` + `sources_self_repair.yml` (#20; auto_off 6 h, 1 rerun solo en bots de fuentes, 1 dispatch, escalado en AUTO:repair) · Messari eliminado (404) · T3 `lib_knowledge_graph` → `_graph.json` vía orquestador (#7) · T4 `lib_audit` (#15; `_audit.jsonl` + `_metrics.json` en rss y orquestador) · T5 `bot_telegram_public` (15 canales [V], 2 instancias de 40 min, bs4 con hash; corrida real 15/15, 267 ítems) · T6/T7 doc 36 (método por grupo a–i + Dossier v2, diseño) · bug corregido: `--once` (loop 0) caía en 40 min · batería 470/470 (con PYTHONUTF8=1, como Linux) · rama `claude/d041-enjambre`, sin push |
| 2026-10-03 (D-055) | Ola 2 del enjambre + investigación de servicios | T1: 11 fichas en `_servicios_open_source/` 03–06 con endpoints probados en vivo (GoPlus y DexPaprika sin key; `pump.fun /coins` sin key; `/replies` y KOTH → 404; Solscan 401/404; Birdeye 401; DEXTools web = SPA; VADER cubre 3/19 términos cripto) + descartes con motivo en `_PENDIENTES` · T2 `lib_scientific_method` (#2; registro append-only `02_Analisis/hypotheses/_registry.jsonl`; H-0 migrada como referencia y reproduce `early_review.evaluate_h0`) · T3 `lib_episodic_memory` (#12; `_episodes.jsonl` + fragmento por escritor; cableado en `bot_self_repair` y `evaluate_hypothesis`; `alerta_emitida` sin cablear en script_97, que es producción) · T4 `lib_adversarial_debate` (#8; advocate/challenger con reglas; doc 36 §4.1) · T5 `lib_reactive_state` (#3; polling por sha256 con protección "racy") · 490/490 · rama `claude/ola2-enjambre`, sin push (lo hace YIN) |
| 2026-10-03 (D-058) | Fix del debate (auditoría Claude1) | C4/C7 exigen significancia en contra; C5 con test exacto placebo vs real (hipergeométrico); C9 exige inversión; A6/C6 eliminadas (= Fisher); veredicto `inconclusa` · `calibrate()` como test permanente: reales refutados 34→8/200 (n = 102) y 67→12/200 (n = 42), nulos aceptados 7 % / 5,5 % · pesos [H] en doc 36 §4.1 · 495/495 · `2c8f1db7` (en main) |
| 2026-10-03 (D-067) | Ola 3: eventos, recetas, bot padre, auditoría CI | T1 `lib_events` (id = sha16(type, subject, bucket); archivo por escritor y día; cursor por líneas por archivo) · T2 `bot_runner` + `sources_runner.yml` (recetas rss / html_list / json_api / telegram_preview; JSONPath propio; matriz por receta; kind src-1 `token`) · T3 `bot_genesis` + `sources_genesis.yml` (fichas → recetas; valida esquema, secret, dominio, fetch en seco, ≥ 5 ítems; 2 strikes [H]) · T4 `audit_gate.py` + `audit_gate.yml` (tests, doc 35 contra blobs LF, prohibidos en líneas agregadas, tocados, bundle; 0 falsos positivos en 198 archivos de historia) · T5 bloques `recipe:` en 5 fichas: validación en vivo 4 habilitadas + helius en probation (sin secret); GoPlus Solana = 1 resultado por llamada [V] · 519/519 · rama `claude/ola3-enjambre`, sin push |
| 2026-10-03 (D-075) | Fallas del audit_gate en el entorno de YIN | Causa raíz única: faltaba bs4. `bot_runner.collect()` tragaba el `ImportError` como `parse_error` con 0 ítems ("0 != 3", "not enough values to unpack"): ahora sube · tests con `requires_bs4` (salto explícito en local; falla con `REQUIRE_TEST_DEPS=1`) · `audit_gate tests` instala `requirements-dev.txt` (hash, `--no-deps`) y bs4 fijado antes de la batería · `requirements-dev.txt` (bs4 4.15.0, soupsieve 2.9.2 + typing-extensions 4.16.0, obligatoria de bs4) · doc 34 §14 · 524/524 · misma rama, sin push |
| 2026-10-03 (D-079) | Calendario de activos no nacidos + retiro de script_99 + X sin login | T1 `bot_prelaunch_calendar` + `sources_prelaunch.yml` (anunciado → confirmado (≥2 fuentes) → nacido → seguimiento 72 h → memoria episódica; 30 d → `no_nacido`; 6 fuentes, cada una falla sola; "no nacido" [H] = sin spot en Bybit/OKX/Binance/HL ni DEX ≥ 100k; emparejamiento por contrato = alertable, por símbolo con ≥2 fuentes = candidato; corrida real: 6/6 fuentes 200, calendario Jumper + BLOZ; hoy no hay hyperps vivas [V]) · T2 `prelaunch.yml` sin cron y job `if: false`, `script_99` DEPRECADO, doc 34 §15 · T3 X sin login: syndication timeline, FxEmbed, react-tweet (3 fichas [V]); Nitter AGPL y archivado, twscrape/twikit con cuentas; búsqueda en X sin login: no existe · rama `claude/d079-prelaunch` sobre ola3, sin push |
| 2026-10-04 (D-082) | Preventa conectada a producción (autorizado por Dirección) | T1 `token_nacido`: `script_116.emit_births` (jóvenes ≤ 30 min con liquidez, escritor `early_watch_<inst>`, carpeta en sus paths de commit) y `script_114.emit_births` (pools en tendencia ≤ 24 h, `multichain_scanner.yml` suma la carpeta); `lib_events.write_events` en lote; TTL de token_nacido 24 h · T2 `lib_sources_store.prelaunch_lookup` (solo contrato exacto) + `script_97.prelaunch_line` en `format_alert_message`: «🆕 PRE-LANZAMIENTO: precio preventa $X, delta vs apertura +Y%», «candidato por símbolo» si no fue por contrato; sin calendario = mensaje idéntico · T3 doc 34 §16 · ninguna conexión cambia puntajes ni la decisión de emitir · rama `claude/d082-conexiones` sobre d079, sin push |
| 2026-10-04 (D-087) | Cuentas de X + portales + patrimonio | T1 `bot_influencer_tracker` + `sources_x_influencers.yml` (:12/:42) + `04_Config/influencers.yaml` (50 activas + 16 apagadas, verificadas; 8 handles de la lista corregidos: toly, pumpfun, mert, ondo, rendernetwork, dydxfoundation, tayvano_, arkham; spotonchain no es la oficial) · **hallazgo: syndication no alcanza** (30 req/15 min; de 8 cuentas, 3 congeladas ~330 d y 3 vacías) → FxEmbed `/2/profile/<c>/statuses` primario, syndication de respaldo · dedup por id, src-1 sin texto, auto_off tras 3 fallas, límites por mecanismo, frescura vivo/lento/congelado/vacio · eventos `tweet_influencer`, `mencion_token`, `keyword_narrativa` · registrado en `_bots.yaml` · T2 11 fichas `07_portales/` (CMC con precio de preventa e ICO Drops P1; CoinGecko, RWA.xyz y DePINscan P2; Tokenomist P3; descartadas CryptoRank (CF 403), Binance Research (WAF), Dune (API paga), Flipside (sin DNS), DePIN Ninja (estacionado)), sin `recipe:` · T3 `02_Analisis/patrimonio/` + `_inventario.json` (60 entradas, 38 legado) + `lib_patrimonio` + doc 34 §17–18 · 545/545 · rama `claude/d087-influencers` sobre main `cf1e4e88`, sin push |
| 2026-10-04 (D-089-R) | Umbrales = señales para Yang · extracto · archivo · CMC/ICO Drops | T1 evaluación por cuenta en `_state.json` (`dias_desde_ultimo_post`, `frescura_score` 1.0/0.5/0.2, `posts_30d`, `aporte_estimado` = posts con contrato o cashtag de activo vigente [H]: calendario, alertas 30 d, multichain, perps HL, early watch) · `evaluar: true` (> 30 d sin post, o aporte 0 con > 10 posts) y `marginal` por mecanismo (< 0.10) · **nunca saca ni apaga cuentas** · reporte semanal `_evaluar_semanal.md` · medición en vivo: 25/50 marcadas (2 sin post 30 d: cobie, hivemapper; 23 sin aporte: publican sin cashtags) · FxEmbed 404 pasajeros → 1 reintento · T2 `m.sha` + `m.ext` (200 chars, ~249 B/post), casi-duplicados por Jaccard de 5-gramas (`dup_de`); ventana de registro 30 d con dedup por diarios · T3 38 legado → `02_Analisis/_archivo_2026_Q3/` con `git mv` (91 archivos), README, inventario `archivado`; única lectura en producción (script_97 → `pre_launch/`) con listas vacías y grupo b solo registro · T4 `coinmarketcap` + `icodrops` en `bot_prelaunch_calendar` (ICO Drops: 38/50 con ticker, 35 con precio; perp manda sobre precio de venta) · 553/553 · rama `claude/d089-evaluacion` sobre d087 + `origin/main`, sin push |
| 2026-10-04 (D-091) | Aporte ampliado · no eliminación · bots de autonomía (principio 6) | T1 `calculate_aporte(post, activos_vigentes) -> int` con 5 tipos: $cashtag, contrato, (TICKER)/#TICKER, keyword sectorial + activo vigente (ticker, contrato o nombre), anuncio (list/listing/launch/TGE) + ticker explícito · señales del texto completo en `m.sg` al registrar, recalificadas contra los vigentes de cada corrida · nombres de activos con `NAME_STOP` (falsos positivos medidos: bitcoin→BCH, blockchain→BCAP, soon, MVNO, TOP10) · en vivo: 5 de las 25 marcadas pasan a aporte > 0 (BinanceWallet, ethena, ondo, rajgokal, tayvano_), quedan 20 · T2 > 60 d sin post → `inactiva_60d_decide_yang` + `revision_yang` + sección en el reporte; política de no eliminación en `evaluar_cuentas` · T3 doc 37: bot_scout, bot_evaluator, bot_integrator, bot_auditor (+ `lib_guard` pre-push; gitlink real de `bfa6907d`); única decisión humana: `aprobaciones.yaml` de Yang · 559/559 · rama `claude/d091-autonomia` sobre d089 + `origin/main`, sin push |
| 2026-10-03 (cierre) | D-035: orquestador, query(), traspaso | `bot_orchestrator` + `sources_orchestrator.yml` (merge, health, poda, bloque AUTO de `_INSTALADOS.md`) · `query()` conectada en script_116 (menciones del scorer joven) y script_97 (`sources_mentions_*`, informativo hasta v7.2.2) · 8 tests (5 + 3) · 437/437 · doc 34 v0.2 (§11 `bot_self_repair`, §12 coparticipación + `backup` en `_bots.yaml`) · **doc 35 traspaso con SHA-256 por archivo** |
| 2026-10-03 | D-033: sistema multi-bot | Doc 34 v0.1: diseño completo de 7 bots + `lib_sources_store`, con esquema src-1, YAML por bot, storage, dependencias y plan de tests · 7 imposibilidades técnicas documentadas (el `GITHUB_TOKEN` no puede escribir workflows; 4plebs no archiva /biz/; DEXTools/Solscan necesitan JS) · implementados `lib_sources_store`, `bot_rss_news` (12 feeds), `sources_rss.yml` y 9 tests · rama sincronizada con main (fast-forward) |
| 2026-10-01 (noche) | Fase 6: guías multi-chain + grupo i + incidente | Guías de compra Arbitrum / Optimism / Blast (Monad sin DEX, no emite) con `guide_for` como regla única para alerta y dossier; bloque 🛒 con 1 wallet; 6 tests nuevos + mutación 5/5 · doc 27 v0.2 (grupo i: > 180 días, registro sin emisión) · §1.2 incidente supergrupo · rama `claude/zealous-tesla-3ua19i` (merge de `origin/main` sin force) |
| 2026-10-01 (tarde) | Fase 5: T1, T2, T3 + docs | Docs 22/24 al estado real (sonda 5/6 disparada, Fase 4 en main, emisiones activas, n ≥ 20 deja de ser condición de emisión) · **hallazgo P0: grupo migrado a supergrupo, las 2 alertas reales con `telegram_sent: false`** · T1 `script_115` + `narrative_collector.yml` (20 tests, 10/10 mutaciones) · T2 `script_114` v0.2 + `multichain_scanner.yml` (15 tests, 12/12 mutaciones) · doc 27 (scoring por tipo, grupo x, caso arc) · doc 26 §10 · 267/267 tests · rama `claude/zealous-tesla-3ua19i` pusheada (YIN integra) |
| 2026-10-01 (mañana) | Fase 4: dossier en la emisión + campos + sonda | `script_97` adjunta el dossier (sombra: guarda; real: `sendDocument` con caption que lleva el 🛒 completo y fallback a `sendMessage`); 11 tests + 6/6 mutaciones · `script_113`: ruta CEX confirmada por contrato, sin código de referido, y categorías (12/12 mutaciones) · `lib_repetition` + `probe_narrative_sources` + workflow manual (local 6/6 familias) · T4 sin implementar (falta la sonda desde Actions) · producción salió de sombra en `6ff13c5` (Dirección) · 237/237 tests · rama `claude/dossier-envio` sin push (YIN) |
