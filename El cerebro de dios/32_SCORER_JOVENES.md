---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: v0.5 (D-027-R) — integrado en la rama, sin merge
last_updated: 2026-10-02
version: 0.5
---

# 32 — Scorer de tokens jóvenes (< 60 min), v0.4: pesos continuos por edad

Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente. Versiones anteriores: v0.1 en
`32_SCORER_JOVENES.md.bak1`, v0.2 en `.bak2`, v0.3 en `.bak3`, v0.4 en `.bak4`.

Decisiones de Dirección que rigen esta versión:
- Para tokens de < 60 min, la fuente primaria es la narrativa informacional.
- P-13: un filtro que no sirve al resultado se saca y se busca otro.
- **Nada en sombra**: emisión real desde el día 1.

## 0. Correcciones de marco (Dirección, D-023-R3)

1. **Los grupos de señales nunca se sustituyen: siempre se combinan.**
2. **La edad ajusta pesos, nunca elimina grupos.** Ningún grupo baja de 15.
3. **En activos maduros, lo informacional también anticipa** (el rumor previo al pump). Para ≥ 60 min el peso
   informacional baja a 40–20, pero no desaparece (ver v7.2.2, §7).
4. **La liquidez inicial no filtra: es un flag informativo** (`initial_liquidity_usd`, peso 0).
5. nkd077 cerró 11 hipótesis sobre **rentabilidad al hold**; nosotros medimos **anticipación de volatilidad**
   (+20 % antes de −30 %). Es otro objetivo: sus negativos no se trasladan.

## 1. Diseño v0.4

### 1.1 Pesos de grupo continuos por edad — `weights_for_age(age_min)`

Hay interpolación lineal entre cortes, ubicados en el **inicio** de cada tramo de la tabla de Dirección. Fuera del
rango, el valor es constante.

| Edad (corte) | Info | Estructural | Precio/volumen |
|---|---|---|---|
| 0 min | 70 | 15 | 15 |
| 10 min | 60 | 20 | 20 |
| 30 min | 50 | 25 | 25 |
| 60 min | 40 | 25 | 35 |
| 6 h | 30 | 25 | 45 |
| ≥ 24 h | 20 | 20 | 60 |

- Ejemplos: 5 min → 65 / 17,5 / 17,5; 20 min → 55 / 22,5 / 22,5; 45 min → 45 / 25 / 30.
- Siempre suma 100 y ningún grupo baja de 15 (test sobre 0–2000 min). El salto máximo es de 1 punto por minuto.
- Ubicar los cortes al inicio de cada tramo es una elección mía: "< 10 min = 70" vale exactamente en 0 y baja
  hasta 60 a los 10 min. La alternativa sería ubicarlos en el punto medio de cada tramo.
- En producción solo se usan las filas de < 60 min (scope de script_116). Las de ≥ 60 min quedan definidas para
  el scorer unificado / v7.2.2.

`score = Σ_grupo W_grupo(edad) × Σ_i w_i·s_i / Σ_i w_i`. Los pesos relativos dentro de cada grupo son fijos.

### 1.2 Grupo informacional (pesos relativos)

`mentions` 15 · `narrative_wave` 15 · `trending_match` 10 · `metadata_socials` 10 · `dex_profile` 5 ·
`github_repo` 5. Definiciones en la v0.2 (§1 de `.bak2`) y en `lib_info_signals`.

### 1.3 Grupo estructural (redistribuido, D-023-R3 T2)

| Componente | Peso relativo (/25) | Fuente | Definición de s |
|---|---|---|---|
| Avance de la curva de bonding | **12** | DexScreener `marketCap` / $69K [H]; graduado = 1 | proporción |
| Holders + concentración top-10 | 6 | RugCheck | holders/300, a la mitad si el top-10 > 30 % |
| Compra inicial del creador | 3 | PumpPortal `initialBuy` | ≤ 2 % = 1 … ≥ 10 % = 0 |
| **S-1** `bonding_curve_velocity` | 1 | Serie propia de la curva (un punto por poll, DexScreener) | Δ% de curva / min en 10 min; 2 %/min = 1 [H]; retroceso = 0 |
| **S-2** `unique_buyer_acceleration` | 1 | PumpPortal `subscribeTokenTrade` | compradores nuevos en los últimos 2 min − compradores de los 2 min previos, por minuto; +5/min = 1 [H] |
| **S-3** `avg_buy_size_trend` | 1 | PumpPortal (trades) | pendiente por mínimos cuadrados del tamaño de compra (SOL) en las últimas 30, como cambio relativo; +100 % = 1 [H]; ≥ 5 compras |
| **S-4** `holder_to_txn_ratio` | 1 | RugCheck holders (o compradores únicos del stream) / txns h1 de DexScreener | 0,5 = 1 [H] |
| Flag `initial_liquidity_usd` | **0** | Primera liquidez vista (serie propia) | informativo, no suma |

La fuente de **S-1 es DexScreener**. pump.fun no tiene una API pública verificada desde acá: su frontend API no se
probó [P].

**S-2 y S-3:** el listener de PumpPortal se suscribe (`subscribeTokenTrade`) a los trades de hasta **100**
mints jóvenes con score ≥ umbral − 25 [H]. Guarda hasta 300 trades por mint y vuelve a suscribir en cada
reconexión. Los campos del evento de trade (`txType`, `traderPublicKey`, `solAmount`) se tomaron como iguales a
los del evento de creación [I]: hay que verificar en el primer log de Actions [P].

### 1.4 Grupo precio/volumen

Las 5 señales de lib_early_signals que existen para un token joven (`volume_acceleration`, `buy_pressure_shift`,
`quiet_accumulation`, `liquidity_inflow`, `holder_accumulation`); s = puntos / 12.

### 1.5 Emisión (D-023-R3 T5)

- Score ≥ **40** **y** subtotal informacional ≥ **5** (antes 10).
- El mínimo es bajo a propósito, para no bloquear regímenes cuantitativos donde la información falta legítimamente.
- Además: edad ≥ edad mínima del early watch (10 min, `_gate.json`) y hay precio y guía de compra.
- Los kill switches cortan el score a 0.

### 1.6 Flag tradability (D-023-R3 T4) — informativo, no bloquea

Cada alerta lleva `tradable` (bool), `liquidity_usd`, `buy_route` e `initial_liquidity_usd`:
- **Early watch** (scorer joven y v7.2.1): `lib_info_signals.tradability`. Una alerta es `tradable` si hay precio
  y (la curva de pump.fun está abierta o el pool tiene ≥ $1K de liquidez). La ruta es "pump.fun (curva de
  bonding)" o "<dex> (AMM) vía Jupiter o el DEX".
- **script_97:**
  - ruta Solana y multi-chain on-chain: lo mismo, sobre el par;
  - ruta CEX: `buy_route = "CEX: Binance, Coinbase…"` (exchanges confirmados) y `tradable` = hay al menos uno.
- El flag también queda en el JSONL (`flags`) y en `_all_alerts.json` por adopción.

## 2. Integración (D-014-R-3, T3 y T4)

**Cambios en v0.4 (D-023-R3).**
- `lib_scoring_young` 0.4: `weights_for_age`, pesos relativos por grupo, `flags=`.
- `lib_info_signals` 0.2: S-1..S-4 y `tradability`.
- `script_116` 116-0.4:
  - el listener suscribe trades (`set_trade_keys`, `trades_snapshot`) y guarda la serie de la curva;
  - `tradability` va en todas las alertas del early watch.
- `script_97`: `tradability_flags` en las rutas Solana y multi-chain.
- El resto de esta sección describe la v0.2/0.3 y sigue vigente.

- **`lib_scoring_young.py` v0.2:**
  - `score_young(token_data, signals, signals_info=None, now_s=None, rug=None, structural=None) -> (score,
    reasons)`;
  - `score_young_detail` devuelve partes, cobertura, filtros, variantes y la decisión;
  - `young_record` + `append_jsonl` para el registro.
- **`lib_info_signals.py`:** las 9 señales informacionales y estructurales, como funciones puras.
- **`script_116` 116-0.3** envuelve `evaluate()`: con par de **< 60 min** llama a `evaluate_young`; con **≥ 60 min**
  sigue v7.2.1 + bono **sin cambios**. En cada poll:
  - `young_info_context` hace 2 llamadas a DexScreener (perfiles y boosts), descarga la metadata IPFS de hasta 40
    lanzamientos nuevos con un tope de 25 s, consulta 1 repo de GitHub y lee los archivos de script_115.
  - RugCheck se pide para los jóvenes con score ≥ umbral − 15.
  - `YOUNG_SCORER=false` (env) apaga el scorer joven.
- **JSONL por token:** `02_Analisis/early/young/<instancia>_<fecha>.jsonl`, un archivo por instancia y día, sin
  conflictos.
  - Se escribe una línea la primera vez, cuando el score cambia ≥ 5 y al emitir (`emitted: true`).
  - Cada línea guarda las s de todas las señales, las partes, la cobertura, los filtros y las variantes. Con eso se
    puede re-puntuar offline y comparar variantes.
  - Se commitea con el estado de la instancia, cada 10 min.
- Las alertas del scorer joven llevan `scoring_version = young-0.2` y `scorer = young`. script_97 las adopta igual
  que las demás.

## 3. P-13 aplicado (criterios con emisión real)

- Primaria: +20 % antes de −30 % en 48 h, con `evaluate_outcome` y velas de GeckoTerminal. Hoy la mide
  `early_review` para las alertas con `gate_min ≤ 10`.
- Con n ≥ 20 resueltas:
  - **tasa ≥ 40 %** → se mantiene;
  - **tasa < 30 %** → se cambia el umbral o el peso de la señal que más contribuyó en los fallos (el JSONL lo
    muestra);
  - **una señal que no separa aciertos de fallos** (mismo s medio en los dos grupos) **se saca y se busca otra**.
- Además se informa el porcentaje de aciertos que después caen ≤ −99 % (H-84).

## 4. Repos open source revisados (Tarea 2)

Datos de la página del repo vía WebFetch y búsqueda web (2026-10-02). La API de GitHub no es accesible desde esta
sesión: estrellas y fechas sin verificar por API [I].

| Repo | ★ | Último commit | Señal que implementa | Licencia | ¿Reusable? |
|---|---|---|---|---|---|
| [t877416676-creator/solana-narrative-radar](https://github.com/t877416676-creator/solana-narrative-radar) | 0 | n/d (5 commits) | Narrativas del ecosistema: DefiLlama, CoinGecko, RPC, GitHub, HN y foro de Solana; corroboración entre fuentes; velocidad por snapshots | MIT | **Parcial**: la idea de exigir ≥ 2 fuentes independientes para promover una narrativa. Escala semanal, no minutos. Stdlib. |
| [BackW00dz/Memecoin-scanner](https://github.com/BackW00dz/Memecoin-scanner) | 0 | n/d (18 commits) | Score 0–100 con volumen, precio, txns, liquidez, edad, **perfiles y boosts de DexScreener** | sin licencia | **Solo la idea** (sin licencia no se copia código). La señal `dex_profile` ya está implementada por nuestra cuenta. |
| [nirholas/pumpfun-claims-bot](https://github.com/nirholas/pumpfun-claims-bot) | 22 | n/d (64 commits) | Credibilidad del creador vía **GitHub social fee claims** de pump.fun, edad de la cuenta, repos, followers, track record | All rights reserved | **No** (propietario). Idea útil para una señal `github_repo` más rica (identidad del creador). Requiere RPC con key. |
| [AtenovD/grokbot-pumpfun](https://github.com/AtenovD/grokbot-pumpfun) | 24 | v1.1 | Agente "narrativa" sobre nombre/símbolo + libro de reputación de creadores (bloqueo tras rug) | MIT | **No para nosotros**: pide una API de LLM paga (Grok) y en realidad indexa hood.fun, no pump.fun. La reputación de creadores es una idea gratis reutilizable [P]. |
| [ian05012/solana-memecoin-dataset](https://github.com/ian05012/solana-memecoin-dataset) | 4 | n/d (4 commits) | **Dataset**: 44.460 snapshots tempranos, 9,5 M trades, ~80 features y etiquetas de retorno a 1 h/6 h/24 h/3 d (junio 2026, GMGN + Helius) | MIT | **Sí, para calibrar** el estructural y el de precio (no trae menciones). Parquet (~2 GB de RAM): lo tiene que bajar YIN o Actions. |
| [aethernet404/rugcheck](https://github.com/aethernet404/rugcheck) | 0 | 2026-08-22 | Mint/freeze authority, top-10, creador, supply; RPC público, stdlib | sin licencia | **No** (sin licencia); ya usamos RugCheck API. |
| [nkd077/solana-memecoin-research](https://github.com/nkd077/solana-memecoin-research) | 0 | n/d (3 commits) | 11 hipótesis sobre 29.814 lanzamientos de pump.fun | sin licencia | **Baseline de calibración** (D-014-R-5): tasas de la población (0,52 % gradúa; retornos de entrada y post-graduación). Su métrica no es la nuestra (+20 % antes de −30 %), así que no refuta las señales [I: autor único]. |
| [ExpertVagabond/solana-narrative-tracker](https://github.com/ExpertVagabond/solana-narrative-tracker) | 0 | n/d (35 commits) | Narrativas desde 8 fuentes gratuitas + síntesis con LLM | MIT | **Parcial**: la recolección es gratis; la síntesis pide la API de Anthropic, que es paga. Escala de ecosistema, no de token. |
| [Figu3/crypto-narrative-tracker](https://github.com/Figu3/crypto-narrative-tracker) | 0 | n/d (32 commits) | Mindshare de 25 narrativas (Google Trends + DefiLlama), semanal | sin licencia | Taxonomía de narrativas como idea [P]; escala semanal. |
| Repos de sentiment (rishikonapure 48★, Drabble 108★, crypto-sentiment 45★…) | 15–108 | viejos | VADER/RoBERTa sobre Twitter y noticias de BTC/ETH | varias | **No**: dependen de la API de Twitter y apuntan a majors, no a tokens de minutos. |

Lo que sale de la revisión: **ningún repo gratuito resuelve las "menciones de un token en sus primeros minutos"**.
- Las fuentes con esa granularidad son X/Twitter, que exige cuenta, cookies o API paga, y los grupos de Telegram
  privados.
- Lo reutilizable es: perfiles y boosts de DexScreener (hecho), corroboración entre fuentes (idea), reputación del
  creador (idea) y un dataset etiquetado para calibrar (MIT).

## 5. Bloqueos y riesgos

1. **`mentions` con poca materia prima: tarea, no bloqueo** (D-014-R-5). Se amplían fuentes con la arquitectura multi-bot del doc 33 [V el diagnóstico]. El almacén de script_115 tiene **43 ítems en 26 h**, y solo 6 con
   dirección. Para un token de 15 minutos va a dar 0 casi siempre. Es el peso más alto del grupo (15/60). Opciones
   para YIN / Dirección:
   - sumar fuentes (más canales de `t.me/s`, subreddits de memecoins como r/SolanaMemeCoins, búsqueda de 4chan por
     dirección);
   - o bajar su peso a favor de `narrative_wave` hasta que haya volumen.
2. **nkd077 como baseline de calibración, no como refutación** (corrección de Dirección, D-014-R-5). Ese trabajo
   mide **graduación** (0,52 % migra al AMM) y retornos de entrada/post-graduación. Nosotros medimos **+20 % antes
   de −30 % en 24–48 h**: son métricas distintas. Lo que aporta: tasas base de la población de pump.fun
   (graduación, distribución de retornos) para comparar la tasa de nuestras alertas contra la población.
3. **Metadata IPFS.** `ipfs.io` puede ser lento o rate-limitar; hay un tope de 25 s por poll. Si falla, la señal
   queda sin dato.
4. **GitHub sin token** (60/h por IP): 1 consulta por poll e instancia.
5. **Contenedor sin red** hacia DexScreener, IPFS, RugCheck y GitHub. Todo lo de red se verifica cuando corre en
   Actions; los tests son sin red. La parte de red la ejecuta YIN o el workflow.
6. **Umbral 50 sin calibrar.** Con emisión real puede dar demasiadas o ninguna alerta: hay que mirar el JSONL de la
   primera hora.

## 6. H-0 pre-registrada (2026-10-02, D-014-R-5)

Registrada **antes** de ver cualquier resultado del scorer joven.

- **Hipótesis:** las señales informacionales no discriminan mejor que las estructurales y de precio/volumen en
  tokens de < 60 min.
- **Predicción:** la tasa primaria de las alertas con `info_score ≥ 20` **no supera** la de las alertas con
  `info_score < 20`, con **n ≥ 40** primarias resueltas en total.
- **Métrica:** primaria (+20 % antes de −30 % en 48 h, desde el precio de la alerta, `evaluate_outcome` con velas
  de 15 min de GeckoTerminal).
- **Población:** alertas emitidas por el scorer joven (`scorer = young`). El grupo sale de `h0_group`, registrado
  al emitir. No se reclasifica después.
- **Prueba:** Fisher exacto a una cola (¿la tasa de `info_ge20` es mayor?), **α = 0,10**. Se decide recién con
  n ≥ 40 y con los dos grupos no vacíos.
- **Decisión:**
  - **p < 0,10** → H-0 rechazada: lo informacional discrimina y se mantienen los pesos 60/25/15.
  - **p ≥ 0,10** → H-0 no rechazada: por P-13 se revisan los pesos o se buscan otras señales informacionales.
- **Implementación:** `early_review.py` → `evaluate_h0`, cada 6 h, en `02_Analisis/diagnostics/early_review.json`
  (campo `h0`). Mientras n < 40, el veredicto es `pendiente`.
- **Riesgo conocido:** el umbral de emisión (40) y el mínimo informacional (10) seleccionan qué tokens llegan a
  ser alertas. La comparación es entre alertas, no entre toda la población.

## 7. v7.2.2 — APROBADO (D-027-R): bono informacional para ≥ 60 min

Por la corrección de marco 3, lo informacional también anticipa en activos maduros. Propuesta:
- **v7.2.2 = v7.2.1 + bono informacional de hasta +10** para tokens de ≥ 60 min.
- Usa las mismas señales informacionales (`lib_info_signals`), ponderadas como en §1.2, escaladas a 10 puntos.
- Se suma al bono anticipatorio (lib_early_signals, tope +8): el total queda en ≤ +18 sobre el score v7.2.1.
- Medirlo con la misma H-0 (§6) separada por edad: `info_score` alto vs. bajo en ≥ 60 min.
- **Alternativa equivalente:** extender `weights_for_age` (filas de 60 min a 24 h) como scorer único para todas las
  edades, en lugar de un bono sobre v7.2.1. Eso reemplazaría v7.2.1 para maduros, y la decisión es de YANG /
  Dirección.
- **Decisión de Dirección (D-027-R): v7.2.2 SÍ; el scorer único extendido, NO.** Fundamento: v7.2.1 se calibró
  con n = 35, y reemplazarlo antes de calibrar el scorer joven sería un retroceso. Las filas de ≥ 60 min de
  `weights_for_age` quedan definidas pero no se usan.
- Estado: **aprobado, pendiente de implementación** (bono informacional de hasta +10 sobre v7.2.1 en script_116
  para ≥ 60 min). Nada cambia hoy para ≥ 60 min hasta que se implemente.

## 8. Arquitectura de trabajo Yin → Claude → Dirección (D-027-R)

| Rol | Hace | No hace |
|---|---|---|
| **YIN** | Investiga servicios open source y los documenta en `_servicios_open_source/` (fichas por categoría, por ejemplo `01_news_mcp/`). Ejecuta lo que necesita red (sondas, verificaciones [P]). Integra a main. | — |
| **Claude** (rama `claude/zealous-tesla-3ua19i`) | Integra en el código lo que YIN investigó: scorers, señales, bots, tests, docs técnicos. Pushea solo a su rama. | No crea archivos en `_servicios_open_source/` (los crea YIN). No pushea a main. |
| **Dirección** | Decide objetivos, umbrales y aprobaciones (por ejemplo, v7.2.2). | No participa técnicamente. |

Flujo: ficha de YIN en `_servicios_open_source/` → Claude la toma, integra y testea en su rama → YIN integra a
main tras la auditoría de YANG.

## 9. Bloqueante P0: bug #148

Reportado por Dirección (D-027-R): YIN creó `_servicios_open_source/` y 3 fichas en `01_news_mcp/`
(`cryptopanic.md`, `coindesk_rss_aggregator.md`, `cryptocontrol.md`) en su main local, pero **no puede pushear por
el bug #148**.

- Verificado del lado de Claude el 03/10: `origin/main` no tiene `_servicios_open_source/` [V].
- Mientras siga así:
  - el flujo Yin → Claude está cortado: Claude no ve las fichas y no integra nada de ellas;
  - las ramas de Claude siguen sin integrarse a main (la rama va 15 commits adelante).
- Claude no tiene el detalle técnico del bug #148 [P: lo documenta YIN]. Hasta que se resuelva, Claude espera las
  fichas y no las recrea.

## 10. Verificaciones de cierre (D-027-R, Tarea 3) [V, 03/10]

| Punto | Estado | Evidencia |
|---|---|---|
| `weights_for_age` con los cortes al **inicio** del tramo | Se mantiene | `AGE_ANCHORS` = (0, 10, 30, 60, 360, 1440 min); test `test_cortes_de_la_tabla` |
| `tradability` en todas las rutas | Sí | Early watch, scorer joven (`evaluate_young`) y v7.2.1 (`evaluate`); script_97 ruta Solana (`alert_record`) y multi-chain on-chain y CEX (`tradability_flags`). Tests `test_joven_usa_trades_y_lleva_tradability`, `test_alerta_v721_tambien_lleva_tradability`, `test_tradability_en_alertas_solana_y_cex` |
| Liquidez inicial = flag informativo, no suma | Sí | `initial_liquidity_usd` va en `flags`, fuera de `STRUCT_WEIGHTS`. Test `test_liquidez_cero_y_flag_informativo`: mismo score con y sin flag |
