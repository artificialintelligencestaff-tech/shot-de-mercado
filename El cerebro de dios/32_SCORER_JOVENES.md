---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: v0.2 (D-014-R-3) — integrado en la rama, sin merge
last_updated: 2026-10-02
version: 0.2
---

# 32 — Scorer de tokens jóvenes (< 60 min), v0.2: informacional primero

Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente. La v0.1 está en
`32_SCORER_JOVENES.md.bak1`.

Decisiones de Dirección que rigen esta versión:
- Para tokens de < 60 min, la fuente primaria es la narrativa informacional.
- P-13: un filtro que no sirve al resultado se saca y se busca otro.
- **Nada en sombra**: emisión real desde el día 1.

## 1. Diseño: señales y pesos

`score = Σ peso × s`, con s ∈ [0, 1], en una escala de 0 a 100. Una señal sin dato vale 0 y baja la cobertura, que
se registra.

| Grupo (peso) | Señal | Peso | Fuente (gratis) | En el contenedor |
|---|---|---|---|---|
| **Informacional (60)** | `mentions`: menciones por dirección (peso 1) o cashtag (0,25) en la última hora | 15 | `narrative/_items.json` de script_115 (Reddit RSS, Telegram `t.me/s`, 4chan, HN, RSS) | Sin red: es un archivo del repo. |
| | `narrative_wave`: cuántos otros lanzamientos de la última hora comparten palabra clave (8 = máx.) | 15 | Stream de PumpPortal (el watch) | Sin red. |
| | `trending_match`: mismo símbolo que un trending (1,0) o palabra compartida (0,6) | 10 | `narrative/_index.json` (CoinGecko trending, script_115) | Sin red. |
| | `metadata_socials`: twitter, telegram y website (0,8) + descripción ≥ 40 caracteres (0,2) | 10 | IPFS `uri` del evento de PumpPortal | Red: Actions. |
| | `dex_profile`: perfil pago en DexScreener (0,6) + boost (0,4 con 500) | 5 | `token-profiles/latest/v1` [V 200 desde Actions] y `token-boosts/latest/v1` | Red: Actions. |
| | `github_repo`: repo enlazado en la metadata, log10(1 + estrellas) / 2 | 5 | `api.github.com/repos` sin token, 1 por poll | Red: Actions. |
| **Estructural (25)** | `bonding_progress`: mcap / $69K [H]; graduado = 1 | 10 | DexScreener (`dexId`, `marketCap`) | Ya disponible. |
| | `holders_struct`: holders / 300, a la mitad si el top-10 > 30 % | 8 | RugCheck (para jóvenes con score ≥ umbral − 15) | Red: Actions. |
| | `dev_wallet`: compra inicial del creador ≤ 2 % = 1, ≥ 10 % = 0 | 7 | PumpPortal `initialBuy` | Ya disponible. |
| | **Kill switches** (cortan el score a 0, no ponderan) | — | script_82 (< 5 min con +10.000 %), RugCheck (mint o freeze authority, top-10 > 50 %, holders < 50), creador > 10 % | |
| **Precio/volumen (15)** | `volume_acceleration` (3), `buy_pressure_shift` (2), `quiet_accumulation` (3), `liquidity_inflow` (2), `holder_accumulation` (2): 15 × puntos / 12 | 15 | lib_early_signals | Ya disponible. |

**Liquidez 0 aceptada.** Se saca el filtro de $20K por P-13: dejaba afuera al 95,6 % de los lanzamientos (§4 de
la v0.1).

**Regla de emisión.** Se emite si:
- `score ≥ YOUNG_THRESHOLD` (50 [H], configurable por env);
- **subtotal informacional ≥ 20**: sin evidencia informacional no hay alerta, aunque la estructura y el precio
  sumen hasta 40;
- edad ≥ edad mínima del early watch (10 min, `_gate.json`);
- hay precio y guía de compra.

**Por qué 50.** Exige información y además otra cosa. Con info 20 (por ejemplo, trending + metadata) hacen falta
30 más entre estructura y precio, que rara vez llegan juntos al máximo (25 + 15 = 40). Con info ≥ 35 alcanza con
estructura media. **No está calibrado**: P-13 lo revisa con los resultados (§3).

**Variantes registradas** (flag): A, B y C sobre precio/volumen (como en la v0.1) e `I_ge2_info` (≥ 2 señales
informacionales activas). Cada línea del JSONL lleva `variant = young-0.2`.

## 2. Integración (D-014-R-3, T3 y T4)

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
| [nkd077/solana-memecoin-research](https://github.com/nkd077/solana-memecoin-research) | 0 | n/d (3 commits) | 11 hipótesis sobre 29.814 lanzamientos de pump.fun | sin licencia | **Como evidencia**: informa que **ninguna señal social, de metadata, de dev o de holders dio ventaja**; solo el 0,52 % gradúa; la mediana post-graduación es −75 % a −95 % [I: autor único, sin revisión]. |
| [ExpertVagabond/solana-narrative-tracker](https://github.com/ExpertVagabond/solana-narrative-tracker) | 0 | n/d (35 commits) | Narrativas desde 8 fuentes gratuitas + síntesis con LLM | MIT | **Parcial**: la recolección es gratis; la síntesis pide la API de Anthropic, que es paga. Escala de ecosistema, no de token. |
| [Figu3/crypto-narrative-tracker](https://github.com/Figu3/crypto-narrative-tracker) | 0 | n/d (32 commits) | Mindshare de 25 narrativas (Google Trends + DefiLlama), semanal | sin licencia | Taxonomía de narrativas como idea [P]; escala semanal. |
| Repos de sentiment (rishikonapure 48★, Drabble 108★, crypto-sentiment 45★…) | 15–108 | viejos | VADER/RoBERTa sobre Twitter y noticias de BTC/ETH | varias | **No**: dependen de la API de Twitter y apuntan a majors, no a tokens de minutos. |

Lo que sale de la revisión: **ningún repo gratuito resuelve las "menciones de un token en sus primeros minutos"**.
- Las fuentes con esa granularidad son X/Twitter, que exige cuenta, cookies o API paga, y los grupos de Telegram
  privados.
- Lo reutilizable es: perfiles y boosts de DexScreener (hecho), corroboración entre fuentes (idea), reputación del
  creador (idea) y un dataset etiquetado para calibrar (MIT).

## 5. Bloqueos y riesgos

1. **`mentions` casi sin materia prima** [V]. El almacén de script_115 tiene **43 ítems en 26 h**, y solo 6 con
   dirección. Para un token de 15 minutos va a dar 0 casi siempre. Es el peso más alto del grupo (15/60). Opciones
   para YIN / Dirección:
   - sumar fuentes (más canales de `t.me/s`, subreddits de memecoins como r/SolanaMemeCoins, búsqueda de 4chan por
     dirección);
   - o bajar su peso a favor de `narrative_wave` hasta que haya volumen.
2. **Evidencia externa en contra** (nkd077, [I]). En 29.814 lanzamientos, las señales sociales y de metadata no
   dieron ventaja. Con emisión real desde el día 1, P-13 tiene que mirar el JSONL temprano.
3. **Metadata IPFS.** `ipfs.io` puede ser lento o rate-limitar; hay un tope de 25 s por poll. Si falla, la señal
   queda sin dato.
4. **GitHub sin token** (60/h por IP): 1 consulta por poll e instancia.
5. **Contenedor sin red** hacia DexScreener, IPFS, RugCheck y GitHub. Todo lo de red se verifica cuando corre en
   Actions; los tests son sin red. La parte de red la ejecuta YIN o el workflow.
6. **Umbral 50 sin calibrar.** Con emisión real puede dar demasiadas o ninguna alerta: hay que mirar el JSONL de la
   primera hora.
