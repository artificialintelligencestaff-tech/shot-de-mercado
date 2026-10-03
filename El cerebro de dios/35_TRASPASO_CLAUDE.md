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
| `.github/workflows/datasets_build.yml` | Construye el dataset histórico de alertas (lib_persist) | producción | `f3d5da654599e21162728dce3e8922da86985272751657d5dbf5431c0949827e` |
| `.github/workflows/early_review.yml` | Revisión diaria del early watch: gate de edad 10→15 y H-0 | producción | `866ad220e9ac6e01f8f232b5f71e824d14a4789f6efbaab005613f2cd69e5268` |
| `.github/workflows/early_watch.yml` | Instancia a del early watch (:07/:37, loop de 40 min) | producción | `991ee94f1a0c5fce20c6ccf353a94fb7cf354714ea50441c07f8169e7bfdcd76` |
| `.github/workflows/early_watch_b.yml` | Instancia b del early watch (:22/:52) | producción | `8ca276cc88939b3838f3e59857eadece8d4e2a7728a12d50b3fe5e2cffc3c2fd` |
| `.github/workflows/latency_analysis.yml` | Mide el desfase de cron y la latencia de detección | producción | `3fc665fcd06afbd9272be188cb51ee51bae26e77cde2c7d94e4c3e08b6deda29` |
| `.github/workflows/multichain_scanner.yml` | Corre script_114 (scanner multi-chain) | producción | `45d3c98449df1d6134778dee1411012f9a01e7030c5829730734180912ee06cd` |
| `.github/workflows/narrative_collector.yml` | Corre script_115 cada 20 min | producción | `f61ae51350ee615cf76ee94b94ee2300b556d22ecba976f5ddae7519570a11b2` |
| `.github/workflows/pipeline_t0.yml` | Pipeline principal (82 → 97 → 98); hand-off con early watch | producción | `9388533c944dc2adb8153dc1395dd19f693caf530aab0e19a662ee028b208412` |
| `.github/workflows/probe_inventario.yml` | Sonda del inventario de fuentes | producción | `ca721858989e13563bd6337bbcd675987a33bd478986ab6aa241686fe774bc4e` |
| `.github/workflows/sources_orchestrator.yml` | Workflow del orquestador de fuentes, cada 10 min | rama | `adec6c3829edc98a7dc6634acf39054b57cde3360f1b063e3f7526e1ec7e097d` |
| `.github/workflows/sources_rss.yml` | Workflow de bot_rss_news, cada 20 min (plantilla de bots) | rama | `8733f22376a05fa79600a54b078ef75944388a4ced532c441bec1557797137e8` |
| `04_Config/inventario.json` | Inventario de fuentes y estado de cada una | producción | `22e4d70357fa281a756168aea483a331f8b1569a740946afad2c9f355ad7c87a` |
| `04_Config/scripts/bot_orchestrator.py` | Fusiona los diarios de bots, salud, poda y bloque AUTO de _INSTALADOS | rama | `b30c7edaa06ada84417559aabc735b187f3ba240bae426e9b4c695fe2ed9c895` |
| `04_Config/scripts/bot_rss_news.py` | Bot RSS: 12 feeds → esquema src-1 | rama | `8758f82be8057b6097e53e4e2c11cea0438b9492c6724ee9f882187f86032a6e` |
| `04_Config/scripts/dataset_builder.py` | Dataset histórico de alertas con resultado | producción | `4ff46283688d21762834652335f4b78206c9b611f84fac20c6a92fc2c783aa97` |
| `04_Config/scripts/early_review.py` | Evaluación del early watch: primary rate, gate de edad, H-0 (Fisher) | producción | `7a86ad79467ca09e57a3bf64d37ef166f84d12350b51bcdd5bf8c5ae0be2bc87` |
| `04_Config/scripts/latency_analysis.py` | Análisis de latencia y desfase de cron | producción | `522901f043297edba421f20e60ae5792f2207f65fa4c40bb27ea5cb667a95e7d` |
| `04_Config/scripts/lib_early_signals.py` | 5 señales de precio/volumen de anticipación | producción | `d62093a707a1c8d36ec9f85a5633ea1b27f389867ba2c0223ad9d8919d7c9a5e` |
| `04_Config/scripts/lib_info_signals.py` | Señales informacionales y estructurales + tradability | producción | `1501b1ef9ed94961edd11caedd0f9f1bc7e421076de46360818db6cf9cc962c6` |
| `04_Config/scripts/lib_persist.py` | Persistencia: dataset propio y bitácora de operaciones | producción | `ceb3c18fce11e8ed9d18bd76313f60b7ee67f68559975a3f13178eb37ce12f9c` |
| `04_Config/scripts/lib_scoring_multichain.py` | Scoring por tipo de activo (grupos b–i) | producción | `40411722bc7bfb742b4d1c8ee6763ebe88ba9f402679753aed675b7de0cd2010` |
| `04_Config/scripts/lib_scoring_young.py` | Scorer joven young-0.4 (<60 min): pesos continuos por edad | producción | `0b258ae077b07c918101f7be7348de10168c2ecc49966c89fe2fdf1d8d9a9d13` |
| `04_Config/scripts/lib_sources_store.py` | Almacén unificado src-1: merge, índice, query, compatibilidad con _items | rama | `ac8c97b6e10a0bb51308c726c7ad28af5c4a8851f28b64a946b7c16751b5ba1a` |
| `04_Config/scripts/probe_inventario.py` | Sonda de disponibilidad de fuentes | producción | `191eaffb88f67f2dbdee621edb70c7a34de0afd5d2a683f401ed963a31806ba7` |
| `04_Config/scripts/script_113_dossier_builder.py` | Dossier por activo (ruta de compra primero) | producción | `e5b7a6bb88ba174caecd469bdff29e59ce1ed1b3ffb4a08a085903821d80a087` |
| `04_Config/scripts/script_114_multichain_scanner.py` | Scanner multi-chain v0.2 | producción | `9d59ca1c08b9301ffe6ba22c398e37be39467aab89bd579e5d49a500d9b27e30` |
| `04_Config/scripts/script_115_narrative_collector.py` | Colector de menciones (solo identificadores) | producción | `93b221531316d22b0f38562bf4f37ee1fc47c73c2e3090df2e8efefbc4368977` |
| `04_Config/scripts/script_116_early_watch.py` | Early watch: PumpPortal WS + scorer joven + claims por mint; usa query() | producción (cambio D-035 en rama) | `05664190a2a7c406ec97c7e98924d69e033b4b0652333e82a72ea2a6a8f3cd3f` |
| `04_Config/scripts/script_82_final_detection.py` | Detección final v7.2.1 (grupo i incluido) | producción | `ee2d5ff729b9d8f4cc746970deeb4e15ebbc2f2594e9aef2bcc830d656d1cddd` |
| `04_Config/scripts/script_97_emit_alerts.py` | Emisión de alertas Telegram + dossier + hand-off/adopción early | producción (cambio D-035 en rama) | `0b03b792cb24d395d9bac0740e0ac8c3fe33ff6ad174a65beb401b57d6c311fd` |
| `04_Config/scripts/script_98_trust_scheduler.py` | Seguimiento de alertas (trust updates) | producción | `aae851c79efa6ca1555c9a054c33ae3b95e1f5f95ff19fb58f113720c1d80594` |
| `04_Config/scripts/test_datasets_persist.py` | Tests de datasets_persist | test | `a101537e077cc13a1e95ca8df7522bd17892504a3270c5de54098c5cce5f5b14` |
| `04_Config/scripts/test_early_review.py` | Tests de early_review | test | `249a3af367fdffdc5de94cde9025a59a95d18b5987580e902c35365ddb7c5cb2` |
| `04_Config/scripts/test_latency_analysis.py` | Tests de latency_analysis | test | `15df25c0cd55e869ec28bbff55e6318fe592b0e4d3217f638d5fb260f7dc44df` |
| `04_Config/scripts/test_lib_early_signals.py` | Tests de lib_early_signals | test | `3a8089974e7cbb8e627681e8d4d95b255485ffeb22531f01af2081ea68159bce` |
| `04_Config/scripts/test_lib_info_signals.py` | Tests de lib_info_signals | test | `e802d81d01a366a5023be3beb1b28a60ed73489439da4a23825c0f80778242cd` |
| `04_Config/scripts/test_lib_scoring_multichain.py` | Tests de lib_scoring_multichain | test | `60eb1f00687174a8baf4dc938fd5696916c75a1c704f34c7a7b3a5d7d23bf565` |
| `04_Config/scripts/test_lib_scoring_young.py` | Tests de lib_scoring_young | test | `deacc7a34b4596460b676e2cbf1ee45e6974d8490db6f53887b9a17addeaedcb` |
| `04_Config/scripts/test_probe_inventario.py` | Tests de probe_inventario | test | `65bce852d14d340826bd0020bfec67d42ec73f39e649959f6e7afe1bb8ba490c` |
| `04_Config/scripts/test_script_114_scanner.py` | Tests de script_114_scanner | test | `ed03b4b4e33a0857375185f6086ff45428852107b31154d34e6e9b2ae0eb5c24` |
| `04_Config/scripts/test_script_115_collector.py` | Tests de script_115_collector | test | `b0e338fa486d6f41836eeccb899388b9d724c0229f085fde419c63b9b4cf320f` |
| `04_Config/scripts/test_script_116_early_watch.py` | Tests de script_116_early_watch | test | `f8c0d8e90acb69a46764840a51c4ede8bc22cbb651281b40bc91d2c7852725cd` |
| `04_Config/scripts/test_script_82_group_i.py` | Tests de script_82_group_i | test | `fad7bfa43879f76cc7c0e58d56841a2965c0ec3047ebf391754d74810ef35fcb` |
| `04_Config/scripts/test_script_97_early.py` | Tests de script_97_early | test | `e3e091802bacd7fbe88b599606501d8b83f96506a6c448265106fb235be39bd4` |
| `04_Config/scripts/test_script_97_guias.py` | Tests de script_97_guias | test | `49409de18be3b855a4b8c62c0a9c7e0082beb461146fe74bab17f219d74a613f` |
| `04_Config/scripts/test_script_97_multichain.py` | Tests de script_97_multichain | test | `a200346bb82ed91a0ac4fbe06104bfe0c9f6528e3c0a2fa408a3aa44a93c608e` |
| `04_Config/scripts/test_script_98_shadow.py` | Tests de script_98_shadow | test | `a67915793ec471a9485026523e8c1ba0b0cfdd821b2f48e6c378fff9ef63fd90` |
| `04_Config/scripts/test_sources_bots.py` | Tests de sources_bots | test | `d550ca4b8b5da4cc6f8aae75b3062b703dc7982070933be3b20c81a50254913e` |
| `04_Config/scripts/test_sources_orchestrator.py` | Tests de sources_orchestrator | test | `b58e5e104fccdbb599f0f2b1f191fdc0d5bdd2b55b4939cfd9d9a4aa9cc61aff` |
| `04_Config/scripts/test_telegram_template.py` | Tests de telegram_template | test | `741681ec8ac3358e579dc0f46105dcc8129e068af252e02863b62d71e4a8b5e0` |
| `04_Config/scripts/test_young_watch_analysis.py` | Tests de young_watch_analysis | test | `c47a23ab925aa8acbf6cd23116a2edb34b6c73ef88f2f628be743819b155256f` |
| `04_Config/scripts/young_watch_analysis.py` | Análisis de los logs JSONL del scorer joven | producción | `31da571be326a6d5729ffea292da1d42ae6ea7458c61ebc4933b7b7e44877539` |
| `04_Config/sources/_bots.yaml` | Registro de bots: workflow, cadencia, stale, respaldo | rama | `f69def01a846d6387fa35771b61b1bfc42de95bbe994d70d1d6e6ab497a74607` |
| `04_Config/sources/keywords.yaml` | Palabras clave por grupo a–i | rama | `95c914b62e86f4c275c07a4d164666db03ea407f04415e0228bdbbeeb1ea6409` |
| `04_Config/sources/rss.yaml` | Los 12 feeds de bot_rss_news | rama | `e5a9dbbb3a7e1496e5aaee7b0310d78b2a091d895087547830d57b0392c977bb` |
| `El cerebro de dios/22_MEMORIA_CLAUDE.md` | Memoria de Claude: una fila por directiva | doc | `a3c48e948fdd288bf4ef4f532d3396c3d154703efc6eb918218a0f8c5279e5e5` |
| `El cerebro de dios/24_DOSSIER_POR_ACTIVO.md` | Diseño del dossier por activo | doc | `7857695a74fc43688ec02ad8b30efe0ac95639516a960d47e3a4f724e7d46a20` |
| `El cerebro de dios/26_METRICA_REPETICION.md` | Métrica de repetición de menciones (rep-0.1) | doc | `66f443238fcdf1092464a670c86c8da7f474f87007ca7b73900a61b96831c938` |
| `El cerebro de dios/27_SCORING_MULTICHAIN.md` | Scoring por tipo, grupo i, caso arc | doc | `7c6d3648d1affae0e8d2a15c5ee46ae2a91c31f79ba666efe991944d81c6b116` |
| `El cerebro de dios/28_INVENTARIO_COMPLETO.md` | Inventario completo de fuentes | doc | `a46eaf3b36d5cfff73a139bf6cb4cb219da4d7475e663ac8ff18644274f1a6d3` |
| `El cerebro de dios/29_PROTOCOLO_PERSISTENCIA.md` | — | borrado | — |
| `El cerebro de dios/31_DETECCION_TEMPRANA.md` | Early watch: diseño, hand-off, claims, gate | doc | `a91528059f86411b894e3c809133ac99b7abedf961ed77c0086304f823c033c6` |
| `El cerebro de dios/32_SCORER_JOVENES.md` | Scorer joven v0.5, H-0, v7.2.2 aprobado, arquitectura Yin-Claude | doc | `2661694484534a2ebbd79d16112b930010316115624da18e3aaef709f3562447` |
| `El cerebro de dios/33_ARQUITECTURA_MULTIBOT.md` | Investigación de fuentes (RSS, MCP, Reddit, Nitter) | doc (diseño reemplazado por 34) | `e56ab11c7c742872558d22c8f1f6f17ffccc5cf950182fdc2897bd8aec67c24e` |
| `El cerebro de dios/34_SISTEMA_MULTIBOT.md` | Sistema multi-bot: 7 bots + store + self-repair + coparticipación | diseño | `57140c0277c88725739269bbbd705c0420128ef72b420bcb8ccf2f2d402a6cff` |

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
