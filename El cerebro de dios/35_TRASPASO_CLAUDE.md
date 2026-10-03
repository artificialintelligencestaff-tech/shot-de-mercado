---
owner: Claude Code (implementador) — documento de traspaso
status: D-035 · para cualquier LLM o persona que continúe el trabajo de Claude
last_updated: 2026-10-03
version: 1.0
rama: claude/zealous-tesla-3ua19i
---

# 35 — Traspaso de Claude

Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente.

**Estado al cierre.**
- `main` contiene todo lo anterior a D-033: PR #3, scorer joven young-0.4 y early watch.
- En la rama, sin integrar:
  - el sistema de fuentes (D-033 y D-035): `lib_sources_store`, `bot_rss_news`, `bot_orchestrator` y sus 2
    workflows;
  - la conexión de `query()` con script_116 y script_97;
  - los docs 34 y 35.
- Tests: 437/437 en verde al cierre de T1–T2 (`for t in 04_Config/scripts/test_*.py; do python3 "$t"; done`).

## 1. Inventario

Todos los archivos creados o modificados por los commits de Claude en esta sesión: el inventario sale de
`git log --grep=session_01AemScDQoasAvH4sHWEfyrh`. Quedan afuera:
- los datos que escriben los workflows (`02_Analisis/…`);
- los backups `.bak*`;
- este documento, que no puede contener su propio hash.

El SHA-256 corresponde al contenido del archivo en el commit que agrega este documento. Para verificarlo:
`python3 -c "import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())" <ruta>`.

Estados:
- **producción**: está en `main` y lo corre un workflow, o lo importa un script que corre;
- **rama**: implementado y con tests, falta integrarlo a `main`;
- **diseño**: documento sin código;
- **doc**: documentación viva.

| Ruta | Propósito | Estado | SHA-256 |
|---|---|---|---|
| `.github/workflows/datasets_build.yml` | Construye el dataset histórico de alertas (lib_persist) | producción | `4101b68889d2d437473edcc216098c5cc52aee77c68ef332ecf59b55d279d336` |
| `.github/workflows/early_review.yml` | Revisión diaria del early watch: gate de edad 10→15 y H-0 | producción | `7d11d2b84034ed45cfdce5adf43ec537251a4f2e892282f88eade1a3f8b26613` |
| `.github/workflows/early_watch.yml` | Instancia a del early watch (:07/:37, loop de 40 min) | producción | `6bef65848aa3322768aa3e5b2e64e8a5e4374b741b6a2c242db64e0bacb4a970` |
| `.github/workflows/early_watch_b.yml` | Instancia b del early watch (:22/:52) | producción | `4b4f037ce80cdbe76411154bb4ecd885cdb071cba4d6faa73bd9063c52752e4a` |
| `.github/workflows/latency_analysis.yml` | Mide el desfase de cron y la latencia de detección | producción | `3b71037ac5793ef7f4a73d5a735642537fbd3a1025a3dc4a8d61e5e5b7c37d20` |
| `.github/workflows/multichain_scanner.yml` | Corre script_114 (scanner multi-chain) | producción | `60647848c621fcf5bacca471ec975f118dee1734efd9bd7381573db47f7e006d` |
| `.github/workflows/narrative_collector.yml` | Corre script_115 cada 20 min | producción | `09f0bbf4122036a11ea9d9e860925dcef47cece641338ac5eee177c24940d06c` |
| `.github/workflows/pipeline_t0.yml` | Pipeline principal (82 → 97 → 98); hand-off con early watch | producción | `45cf37f7d450b15793ab80b0a37708a4acb23a86cc888709304377dc8174de95` |
| `.github/workflows/probe_inventario.yml` | Sonda del inventario de fuentes | producción | `0196271d691cef0112f5a416a0879d4f0d2b29f58557c650bb967f07702b71fe` |
| `.github/workflows/sources_orchestrator.yml` | Workflow del orquestador de fuentes, cada 10 min | rama | `81604b28e19ae1dc7dcfdbc73442bd86e045f00f692ff2f87c26601e81fe497e` |
| `.github/workflows/sources_rss.yml` | Workflow de bot_rss_news, cada 20 min (plantilla de bots) | rama | `d125d234f755fdf7389b8cc6944fc98288ea13de6d4e798d50bb41c7a925b894` |
| `04_Config/inventario.json` | Inventario de fuentes y estado de cada una | producción | `0d823075337132638ab6e8787759e36d862b2d21c6929c6d5cdeb79f862bb1b0` |
| `04_Config/scripts/bot_orchestrator.py` | Fusiona los diarios de bots, salud, poda y bloque AUTO de _INSTALADOS | rama | `4578df72b1d30e81a9a2abb83b6c1e5900a323afd659a73bb67c492827b71421` |
| `04_Config/scripts/bot_rss_news.py` | Bot RSS: 12 feeds → esquema src-1 | rama | `dbce1ab52913c1d423f9abf5aa3f3535912c115f5bc741ea1c9a69f8968a2180` |
| `04_Config/scripts/dataset_builder.py` | Dataset histórico de alertas con resultado | producción | `e406e35486178078194a6d714f7f18a6f3638780850bdbb5e2114b6251f3db78` |
| `04_Config/scripts/early_review.py` | Evaluación del early watch: primary rate, gate de edad, H-0 (Fisher) | producción | `c11852a02463a10bdb0d3bf38fa373331b3b49fa7ff5e99e12d20b517097cc01` |
| `04_Config/scripts/latency_analysis.py` | Análisis de latencia y desfase de cron | producción | `aac96406c6367c2d919c2624513761fe9d3304e58284e1165a080fb33c9f1f08` |
| `04_Config/scripts/lib_early_signals.py` | 5 señales de precio/volumen de anticipación | producción | `298ee897a84958ce447c23a4031a3dc34b99acc281001fb601a41f1f817067c6` |
| `04_Config/scripts/lib_info_signals.py` | Señales informacionales y estructurales + tradability | producción | `f06fa94d98f8cdd01c00e0578465e418b59f8ad8992c32a2a0060e4b4ac74f6f` |
| `04_Config/scripts/lib_persist.py` | Persistencia: dataset propio y bitácora de operaciones | producción | `cea9a34e13391b95af5591d6ee0120a00839f5ff86faffc9654d5b7d27f4cc4a` |
| `04_Config/scripts/lib_scoring_multichain.py` | Scoring por tipo de activo (grupos b–i) | producción | `f216f81bb76e99adb7454b4b07afca4c74aa7ef076b66c09392ff4fed99098a3` |
| `04_Config/scripts/lib_scoring_young.py` | Scorer joven young-0.4 (<60 min): pesos continuos por edad | producción | `e74f08934d1f0d2532447504b5dadfb92e0399c37bf881f73ff046cc943696b0` |
| `04_Config/scripts/lib_sources_store.py` | Almacén unificado src-1: merge, índice, query, compatibilidad con _items | rama | `c170d941c80546f6755fd4ba1a0c87dc82369a15b23a5f2d23ef58fcc9a72d8e` |
| `04_Config/scripts/probe_inventario.py` | Sonda de disponibilidad de fuentes | producción | `c0446affa69deaa34c6d8a9cdcddbaba711ae82b66bf716114d68003397961bf` |
| `04_Config/scripts/script_113_dossier_builder.py` | Dossier por activo (ruta de compra primero) | producción | `e2a6e6c8cb3c07ba7b0a5635876d0c677a38c6a06ab8cdf49449dec4d4fe1e4a` |
| `04_Config/scripts/script_114_multichain_scanner.py` | Scanner multi-chain v0.2 | producción | `08cd30be1827abfac97333ac770fd05e25c4c42a010c5d5967cd254ca10eb54c` |
| `04_Config/scripts/script_115_narrative_collector.py` | Colector de menciones (solo identificadores) | producción | `59658a198fbb809e8317db022a9e6d12241f56a500135608dbb0ee0707d6a072` |
| `04_Config/scripts/script_116_early_watch.py` | Early watch: PumpPortal WS + scorer joven + claims por mint; usa query() | producción (cambio D-035 en rama) | `d68dd0efce72b3e8cc57bb44adfb05bfce0d15a10b881022bde275096b45c7d0` |
| `04_Config/scripts/script_82_final_detection.py` | Detección final v7.2.1 (grupo i incluido) | producción | `b35c7d14fd2f37889c19e6a557a72e3af7186a5bf9e0158760fc37675e41c5ab` |
| `04_Config/scripts/script_97_emit_alerts.py` | Emisión de alertas Telegram + dossier + hand-off/adopción early | producción (cambio D-035 en rama) | `9cd3e8607931f5f0531b604207dce15e0b5eb9bfce79bbb877e6d14d31db88a2` |
| `04_Config/scripts/script_98_trust_scheduler.py` | Seguimiento de alertas (trust updates) | producción | `74288d4eb3ced1588ef0af4bb2a87e3ffaa3965455d22a54c032ccc20158f309` |
| `04_Config/scripts/test_datasets_persist.py` | Tests de datasets_persist | test | `d957c7f249d3651defae3aa474be1c848d60ae12f7720e25c741638a77986512` |
| `04_Config/scripts/test_early_review.py` | Tests de early_review | test | `0c304d3895d4230956e669e03720aeca931753afbfcf8c6427b329f7d2b04d53` |
| `04_Config/scripts/test_latency_analysis.py` | Tests de latency_analysis | test | `9c7243ed56294316ba3f97edc7c610118f9ef27b3d8349b3a54404bb1506568b` |
| `04_Config/scripts/test_lib_early_signals.py` | Tests de lib_early_signals | test | `e19c09a7a7943d84831cb660825ed91e84b1dc8467f8f7737f87bccab2d52573` |
| `04_Config/scripts/test_lib_info_signals.py` | Tests de lib_info_signals | test | `702923af39ace81f3975a7b1ad0220aab7f8c8f6c31026ea71991e618fc682b7` |
| `04_Config/scripts/test_lib_scoring_multichain.py` | Tests de lib_scoring_multichain | test | `c8cc6a682a5c22b2319f8db3af49ed8d85072298312badbf100f9850d7e784af` |
| `04_Config/scripts/test_lib_scoring_young.py` | Tests de lib_scoring_young | test | `dba368fc6b13e7f371ce2d99ed2f22987304d356c30394edb45832b3c3638403` |
| `04_Config/scripts/test_probe_inventario.py` | Tests de probe_inventario | test | `5567f6e384ada8f7869c53963a72267ce510c330b6c2af2bd0b82e8ae3927850` |
| `04_Config/scripts/test_script_114_scanner.py` | Tests de script_114_scanner | test | `af914c0b9e117db219408d208d0d59e51b00b9376f6d6651a96c189161b090d4` |
| `04_Config/scripts/test_script_115_collector.py` | Tests de script_115_collector | test | `b031bd6055e5dea9b8b9d59f64e125a40d0c581db5bbb2c4b5439bcdbe97d27b` |
| `04_Config/scripts/test_script_116_early_watch.py` | Tests de script_116_early_watch | test | `43283ce722628e7ea645813cc9cd0c093363197cd42b06be56217040bfcdd096` |
| `04_Config/scripts/test_script_82_group_i.py` | Tests de script_82_group_i | test | `e514536690d59371eab7b650c1d085defe0872b27e4bde59f537d1397d2b241f` |
| `04_Config/scripts/test_script_97_early.py` | Tests de script_97_early | test | `91a73103cf3313b9cd8f8dcb579cbfab8cdcc4afb0c39ea9a6d7a00e04c75070` |
| `04_Config/scripts/test_script_97_guias.py` | Tests de script_97_guias | test | `c7cd77257737243118508681fd0fe29269a00f82cca1b7602f25ddec0aeffa9e` |
| `04_Config/scripts/test_script_97_multichain.py` | Tests de script_97_multichain | test | `69da53a2f341dd157e51d3dd7a5d58e54268fd7545e6d0b0d6887ed2b6136d37` |
| `04_Config/scripts/test_script_98_shadow.py` | Tests de script_98_shadow | test | `a784b25a6dfa76dc7fc9debb8ee5c752d6d933887a1fb7b0167e324d204fb939` |
| `04_Config/scripts/test_sources_bots.py` | Tests de sources_bots | test | `a36cf586939b4d7ea6774ef3340a5987565d343c4d7902fb69b5ff87c3faec25` |
| `04_Config/scripts/test_sources_orchestrator.py` | Tests de sources_orchestrator | test | `0576b027198e16c293e456717b932d8296994ef8ee0152d6106fcbdc4fdf4228` |
| `04_Config/scripts/test_telegram_template.py` | Tests de telegram_template | test | `86b3e576e89fe4a83f06d170f332bfd63b99004330b9d91dd41bf1f93d94d10e` |
| `04_Config/scripts/test_young_watch_analysis.py` | Tests de young_watch_analysis | test | `21aff87d75859c913b1cb15090b0c714d19bcbfa37502004fd5d79afd2443f68` |
| `04_Config/scripts/young_watch_analysis.py` | Análisis de los logs JSONL del scorer joven | producción | `e7677e13d1dcadcdaedb5ef0e9bdb8cf0d44cc9046264fe3c099ec368ceb11ba` |
| `04_Config/sources/_bots.yaml` | Registro de bots: workflow, cadencia, stale, respaldo | rama | `9524f71e394e4976c70e73c88ade949c61e08b0102767f719c44ea409719b671` |
| `04_Config/sources/keywords.yaml` | Palabras clave por grupo a–i | rama | `37ba02cf8f82cbacce9bf6701a7a82cfa3192174abd46e0f6cf51c1e1d3d8e6f` |
| `04_Config/sources/rss.yaml` | Los 12 feeds de bot_rss_news | rama | `f96569544270b8ac871fdc06b3a4f3d237322d1c22623664a90e113642e0d5d7` |
| `El cerebro de dios/22_MEMORIA_CLAUDE.md` | Memoria de Claude: una fila por directiva | doc | `ce45961d739c1c41f3a0666a9ea81b2cb404f137fbf2cd9a0322f2ed19279f71` |
| `El cerebro de dios/24_DOSSIER_POR_ACTIVO.md` | Diseño del dossier por activo | doc | `db128d3ad8b27469ce0a16232f2f94c41cb4af6acb8026c3ae89f13cf87e4c21` |
| `El cerebro de dios/26_METRICA_REPETICION.md` | Métrica de repetición de menciones (rep-0.1) | doc | `b55d49cef4bcccf1b53ea0e8989621b303dc4574e8ae455436a5de20e45218b2` |
| `El cerebro de dios/27_SCORING_MULTICHAIN.md` | Scoring por tipo, grupo i, caso arc | doc | `3816a9a8cadc8e6ed102570fcefe9552e403138b00c486cd2c51ecfcd2cefc23` |
| `El cerebro de dios/28_INVENTARIO_COMPLETO.md` | Inventario completo de fuentes | doc | `088cf61c8365121545e6683cf98cff6a6cbb0f3f7103c0098f20d61c701f8979` |
| `El cerebro de dios/29_PROTOCOLO_PERSISTENCIA.md` | — | borrado | — |
| `El cerebro de dios/31_DETECCION_TEMPRANA.md` | Early watch: diseño, hand-off, claims, gate | doc | `e9385fe9a3d5f9f18af4ce4d22e684af3b112e729fd745477ae61fdd29ba47d3` |
| `El cerebro de dios/32_SCORER_JOVENES.md` | Scorer joven v0.5, H-0, v7.2.2 aprobado, arquitectura Yin-Claude | doc | `af3fd1533292401ad0797a1e35a70aca2b893cc45a6a2aa531cc6fb82a3139a9` |
| `El cerebro de dios/33_ARQUITECTURA_MULTIBOT.md` | Investigación de fuentes (RSS, MCP, Reddit, Nitter) | doc (diseño reemplazado por 34) | `50131aa522f8c1a81be690f4091da85854b9b3bc4a1425eb328a167e7398090c` |
| `El cerebro de dios/34_SISTEMA_MULTIBOT.md` | Sistema multi-bot: 7 bots + store + self-repair + coparticipación | diseño | `0ecc5ca04379336a78c725289bbafdb040caf817a5342e1227e9cfbed9c8af5d` |

## 2. Lógica por archivo

### Detección temprana (Fase 10 / 10b; doc 31)

**`script_116_early_watch.py`**
- **Problema.** El pipeline por cron llega tarde a los lanzamientos de pump.fun: el cron se desfasa ~11,9 min
  [V].
- **Decisiones.**
  - El websocket de PumpPortal escucha `newToken` y los trades (`subscribeTokenTrade`, máx. 100 claves).
  - Cada job es un loop de 40 min con poll cada 2 min. Corren 2 instancias desfasadas 15 min, para cubrir el
    desfase y la caída de una.
  - El mint se reclama en git (`02_Analisis/early/alerts/<mint>.json` vía `Git.claim`) para que dos instancias
    no emitan el mismo token.
  - Los tokens de menos de 60 min se puntúan con el scorer joven; los de 60 min o más, con v7.2.1.
  - D-035: las menciones combinan `_items.json` (script_115) con `lib_sources_store`.
- **Descartado.**
  - Un proceso persistente: Actions no lo permite.
  - Telethon y Pyrogram: restricción del proyecto.
  - Lock por archivo local: no sirve entre runners.

**`script_97_emit_alerts.py`** (cambios de esta sesión)
- **Hand-off.**
  - Si early watch está activo (consulta a la API de Actions), la ruta Solana se cede y script_97 adopta las
    alertas de `_early_alerts.json` y de los claims, con dossier.
  - Si early watch no está activo, emite como siempre, sin duplicar mints ya reclamados.
- **Flags.** `tradability_flags`: flag informativo, presente en todas las rutas.
- **D-035.** `source_mentions()` agrega `sources_mentions_1h`, `sources_mentions_24h` y `sources_feeds` a cada
  alerta (Solana y multi-chain). **No suma puntos**: el bono de v7.2.2 está aprobado pero no implementado.
- **Descartado.** Que script_97 consulte las fuentes en vivo: le sumaría latencia y fallas de red a la emisión.

**`early_review.py`**
- Revisión cada 24 h:
  - si el primary rate es menor a 40 %, sube la edad mínima de 10 a 15 min en `_gate.json`;
  - mide la cobertura de PumpPortal.
- H-0 preregistrada: Fisher exacto unilateral con α = 0,10, n ≥ 40.
- **Descartado.** Ajustar el umbral en caliente: sería p-hacking.

**`latency_analysis.py`**: midió el desfase del cron. Es la base de todas las decisiones de cadencia.

**`young_watch_analysis.py`**: lee los JSONL del scorer joven para calibrar a futuro.

### Scorer joven (doc 32)

**`lib_scoring_young.py` (young-0.4)**
- **Problema.** v7.2.1 se calibró con tokens maduros (n = 35). Para un token de 5 min no hay historia de precio;
  lo único disponible es información.
- **Decisiones.**
  - Pesos por grupo que dependen de la edad, interpolados linealmente entre anclas puestas al inicio de cada
    tramo (0/10/30/60/360/1440 min). Cada fila suma 100 y ningún grupo baja de 15.
  - Umbral 40, con un mínimo informacional de 5.
  - Kill switches que llevan el score a 0.
  - Liquidez 0 aceptada.
  - Flags que no suman puntos.
- **Descartado.**
  - Escalones discretos: generaban saltos de score al cruzar un corte.
  - Un scorer único extendido: Dirección eligió v7.2.2 (bono +10 sobre v7.2.1).
  - GARCH, ATR y Bollinger en memecoins: restricción del proyecto.

**`lib_info_signals.py` (info-0.2)**
- Señales informacionales: `mentions`, `narrative_wave`, `trending_match`, `metadata_socials`, `dex_profile`,
  `github_repo`.
- Señales estructurales: `bonding_progress`, `holders_struct`, `dev_wallet` y S-1..S-4.
- `tradability`.
- Cada señal devuelve `{"name", "s" ∈ [0, 1], "detail"}`. `None` significa sin cobertura, que es distinto de 0.

**`lib_early_signals.py`**: 5 señales de precio y volumen (máx. 12 puntos) y el bono anticipatorio multi-chain.

### Sistema de fuentes (docs 33 y 34)

**`lib_sources_store.py`**
- **Problema.** Hay 7 bots con formatos distintos y un solo consumidor.
- **Decisiones.**
  - Esquema único `src-1` (§3) sin cuerpo de texto. Guarda los identificadores (direcciones, cashtags,
    keywords) y un hash; es la misma política que script_115 y deja el repo en 1–4 MB/día [H].
  - Dedup global por (`src`, `ts`, `h`).
  - `load()` usa `_merged.jsonl` si tiene menos de 15 min; si no, reconstruye en memoria. No hay dependencia
    dura del orquestador.
  - `safe_load()` nunca lanza.
  - `to_items_store()` y `mention_items()` reutilizan `lib_info_signals.mentions` sin modificarla.
- **Corrección hecha.** La regex base58 tomaba la cola de una dirección `0x…` como si fuera una dirección de
  Solana. Se corrigió acá; en script_115 sigue igual (§7).
- **Descartado.**
  - SQLite: un binario en git no se puede mergear.
  - Guardar el texto completo: crecimiento del repo.
  - Indexar con un servicio externo: no es 100 % gratis o requiere cuenta.

**`bot_rss_news.py`**
- Parser propio de RSS 2.0 y Atom: separa el título, cosa que `lib_repetition.parse_feed` no hace. Las fechas y
  el HTML se procesan con `lib_repetition`.
- Dedup por título + URL durante 72 h.
- Salud por feed en `_state.json`.
- **Descartado.** `feedparser` (BSD): una dependencia más, cuando la biblioteca estándar alcanza.

**`bot_orchestrator.py`**
- Es el dueño único de `_merged.jsonl`, `_index.json` y `_health.json`.
- Estados posibles: `ok`, `vacío`, `atrasado`, `caído`, `sin_datos`, `diseño`.
- Los contadores de corridas vacías y de fallas solo avanzan con una corrida nueva (`last_run` distinto).
- Poda los diarios de más de 7 días.
- Reescribe el bloque AUTO de `_INSTALADOS.md` solo si cambió algún estado, para no commitear cada 10 min.
- **Descartado.** Que instancie workflows: el `GITHUB_TOKEN` no puede escribir `.github/workflows` [V].

**Workflows `sources_*.yml`**
- Cada uno commitea solo su carpeta y usa `pull --rebase` con 4 reintentos.
- Minutos de cron elegidos para no coincidir con los demás workflows.
- Nunca `--force`.

**Configs YAML** (`04_Config/sources/*.yaml`)
- Sumar una fuente es sumar una línea.
- `enabled: false` saca una fuente sin borrarla.

## 3. Esquema de datos unificado (`src-1`)

```json
{"v": "src-1", "bot": "rss", "src": "cointelegraph_solana", "kind": "news|message|post|repo|tweet",
 "id": "…", "url": "…", "ts": 1790900000, "seen": 1790900420, "title": "≤160 car. (null en message/tweet)",
 "a": ["direcciones"], "c": ["CASHTAGS"], "k": ["keywords de keywords.yaml"],
 "h": "sha256[:16] del texto normalizado", "au": "sha256[:12] con sal del autor | null", "m": {}}
```

**Archivos**

| Archivo | Contenido |
|---|---|
| `02_Analisis/sources/<bot>/<YYYY-MM-DD>[_<inst>].jsonl` | diario de cada bot |
| `<bot>/_state.json` | `last_run`, `items_last_run`, `feeds` o `sources` con `status`, `items`, `new`, `fails`, `last_ok`, y las claves vistas en `seen` |
| `_merged.jsonl` | todos los bots, últimas 48 h, sin duplicados, más reciente primero |
| `_index.json` | `{"generated_at", "count", "a": {dir: [fila]}, "c": {...}, "k": {...}}` |
| `_health.json` | `{"bots": {nombre: {status, last_run, last_output, sources_ok, sources_total, errors, empty_runs, fail_runs}}, "history": [24 h]}` |

**Consulta**
- `query("9BB6…pump")`: por dirección (EVM sin distinguir mayúsculas).
- `query("$WIF")`: por cashtag.
- `query("wif")`: por cashtag, keyword o palabra en el título.
- `query(..., since=epoch, limit=n)`: acotada.

## 4. Cómo continuar

**Orden de lectura**
1. `_MANIFESTO.md` y `_GLOSARIO.md`.
2. `22_MEMORIA_CLAUDE.md`: la última fila es el estado.
3. `32_SCORER_JOVENES.md`.
4. `34_SISTEMA_MULTIBOT.md`.
5. Este documento.
6. El código, en el orden de §2.

**Archivos críticos.** Un error en cualquiera de ellos corta la emisión:
- `script_82_final_detection.py`
- `script_97_emit_alerts.py`
- `script_116_early_watch.py`
- `lib_scoring_young.py`
- `.github/workflows/pipeline_t0.yml`
- `.github/workflows/early_watch*.yml`

**Antes de modificar**
1. `git fetch origin main && git merge origin/main`, nunca rebase ni force.
2. Correr la batería completa (437 tests, sin red, ~1 min).
3. Para cada script que se toque, su test: `test_script_97_*`, `test_script_116_early_watch`,
   `test_lib_scoring_young`, `test_sources_*`.
4. Backup `.bakN` de cualquier doc antes de editarlo.
5. Agregar una fila en el doc 22.

**Siguiente trabajo, en orden**
1. YIN integra la rama a `main`.
2. Primera corrida de `sources_rss.yml` para verificar los 12 feeds en `_state.json`.
3. Bono v7.2.2: +10 sobre v7.2.1 para ≥ 60 min, a partir de `sources_mentions_*` y de las señales
   informacionales.
4. `bot_forum_scraper` y `bot_telegram_public` reutilizando los parsers de `lib_repetition`.
5. `bot_self_repair` (doc 34 §11).

## 5. Alternativas que consideré y no implementé

1. **Orden de compra de PumpPortal (`trade-local`) como sonda de tradabilidad.** Arma una transacción sin
   firmarla: si se arma, el token se puede comprar. Daría `tradable` verificado en lugar de inferido. No se
   hizo por alcance.
2. **Websocket de DexScreener** (el que usa su web) en lugar del poll cada 2 min. Bajaría la latencia del
   precio a segundos. No está documentado y es frágil [H].
3. **Bloom filter del dedup en `_state.json`.** Con varios bots grandes, `seen` crece; un bloom de 64 KB
   cubre 100 000 claves con 1 % de falsos positivos. No hizo falta todavía.
4. **Branch de datos aparte** (`data/sources`) para que los commits de los bots no ensucien `main`. Requiere que
   los consumidores hagan `git fetch` de esa rama (script_97 ya lo hace con `origin/main`). Por alcance.
5. **Firma de contenido** (`h` = simhash en lugar de sha256). Detectaría la misma noticia reescrita por varios
   medios, que es una señal de ola narrativa más fuerte que el conteo bruto.
6. **Matriz única de workflow** (`strategy.matrix` sobre `_bots.yaml`) en lugar de un workflow por bot. Se
   descartó porque cada bot necesita su propia cadencia, y el cron es por workflow.

## 6. Cinco propuestas para ir más allá

1. **Latencia por fuente como peso.** `seen − ts` por fuente ya está en `src-1`. Con 2 semanas de datos se puede
   ponderar cada fuente según cuánto se adelanta, en promedio, al movimiento de precio. Es medible con el
   dataset histórico de alertas, sin supuestos.
2. **Velocidad de menciones en lugar de conteo.** Hoy `mentions` cuenta en ventanas de 1 h y 26 h. La métrica
   de repetición (doc 26, sorpresa de Poisson) aplicada sobre `_merged.jsonl` daría una aceleración. La
   hipótesis del proyecto es aceleración vertical, y las menciones deberían medirse igual.
3. **Grafo de co-mención.** Dos tokens que aparecen en los mismos ítems comparten narrativa. Si un token del
   cluster se acelera, los demás son candidatos tempranos. Se arma con `_index.json` sin datos nuevos.
4. **Calibración bayesiana del scorer joven.** Con n ≥ 40 resultados, los pesos de grupo se pueden estimar como
   una posterior (beta-binomial por señal) en lugar de fijarlos a mano. Va después de H-0 y no la contamina,
   porque usa datos posteriores.
5. **Contrafactual automático.** Por cada token que se aceleró (+20 %) y no fue alertado, registrar qué señales
   tenía y en qué minuto. Es la mejor fuente de nuevas señales y de umbrales mal puestos. `dataset_builder.py`
   ya tiene la mitad.

## 7. Advertencias técnicas

**No tocar sin tests y sin el doc correspondiente**
- Los claims por mint (`Git.claim`): sin ellos, 2 instancias emiten el mismo token.
- `early_watch_active` en script_97: si devuelve `False` cuando early watch está activo, hay emisión doble; si
  devuelve `True` cuando no lo está, se pierde la ruta Solana.
- Los pesos `AGE_ANCHORS`, `STRUCT_WEIGHTS` e `INFO_WEIGHTS`: cambiarlos invalida la H-0 preregistrada.

**Qué rompe la cadena**
- Renombrar `_early_alerts.json`, `_items.json`, `_merged.jsonl` o los campos de `src-1`. Hay consumidores en
  otros scripts.
- Un workflow que haga `git add .` en lugar de su carpeta: genera conflictos de rebase con los demás bots.
- Sacar `concurrency` de los workflows: corridas superpuestas del mismo bot.

**Frágil**
- Nitter y X: las instancias mueren cada pocas semanas.
- Reddit: bloquea las IP de datacenter [I].
- Telegram `t.me/s`: si Telegram cambia las clases `tgme_widget_message`, el parser devuelve 0 ítems.
  `bot_self_repair` lo detecta como "vacío anómalo".
- El cron de Actions: desfase ~12 min. Puede saltear corridas en horas pico.

**Bugs conocidos**
- La regex base58 de `script_115_narrative_collector.py` (`BASE58_RE`) toma la cola de una dirección `0x…`
  como una dirección de Solana falsa. El fix es de una línea: el lookbehind `(?<![0-9A-Za-z])`, como en
  `lib_sources_store`.

## 8. Glosario

| Término | Significado |
|---|---|
| Aceleración vertical | +20 % antes de −30 %, dentro de 24–48 h: el objetivo de detección |
| Grupos a–i | a memecoins · b presale · c governance DeFi · d sintéticos · e DePIN · f L1/L2 · g RWA · h blue chips · i establecidos sin grupo |
| v7.2.1 | Scorer de producción para ≥ 60 min, calibrado con n = 35 |
| v7.2.2 | v7.2.1 + bono informacional de hasta +10. Aprobado en D-027-R, sin implementar |
| young-0.4 | Scorer joven para tokens de menos de 60 min (doc 32) |
| Early watch | script_116: vigilancia de lanzamientos en vivo, 2 instancias (a, b) |
| Hand-off | script_97 cede la ruta Solana cuando early watch está activo y adopta sus alertas |
| Claim | Archivo por mint en git que reserva la emisión para una sola instancia |
| Gate | Edad mínima del token para el early watch (10 min; 15 si el primary rate es menor a 40 %) |
| Primary rate | Proporción de alertas que cumplen la aceleración vertical |
| H-0 | Hipótesis preregistrada: info ≥ 20 no supera a info < 20 en primary rate (Fisher, α = 0,10, n ≥ 40) |
| Kill switch | Condición que lleva el score a 0 (autoridad de mint, concentración, initial buy enorme) |
| Flag informativo | Campo de la alerta que no suma puntos (`tradable`, `liquidity_usd`, `buy_route`, `sources_mentions_*`) |
| src-1 | Esquema unificado de ítems de los bots de fuentes |
| Bloque AUTO | Sección de `_INSTALADOS.md` que reescribe un bot; lo de afuera no se toca |
| Bot de respaldo | El bot que suma fuentes equivalentes cuando otro está caído (doc 34 §12) |
| NADA EN SOMBRA | Emisión real desde el día 1 |
| P-13 | Un filtro que no sirve al resultado se saca y se reemplaza |
| YIN / YANG / Dirección | YIN investiga e integra a `main` · YANG audita · Dirección decide |
| [V]/[I]/[H]/[P] | verificado / inferido / hipótesis / pendiente |
