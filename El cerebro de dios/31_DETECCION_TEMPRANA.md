---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: VIVO
last_updated: 2026-10-01
version: 0.1
---

# 31 — Detección temprana (Fase 10)

Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente.
Objetivo de la fase: **anticipar**. Cada minuto entre el inicio del pump y la alerta es precio que el grupo no captura.

## 1. Latencia actual (T1)

Archivo: `02_Analisis/diagnostics/latency_analysis.json` · script: `04_Config/scripts/latency_analysis.py` ·
workflow manual: `latency_analysis.yml`.

Alcance: las **últimas 20 alertas** de `_all_alerts.json` en `origin/main` `7f8a001`, sin contar las descartadas.
Son 12 on-chain (Solana) y 8 multi-chain por CEX.

### 1.1 Lo que se midió sin velas [V]

| Medida | Valor |
|---|---|
| Gap inicio del pump → emisión, acotado por el snapshot de detección (4 tokens con h1 ≥ +5 % y par < 60 min: e/acc, Insect, SPR, 1M X) | **entre 39,6 y 43,3 min** (medias de cota inferior y superior) |
| Detección (`detected_at`) → emisión, tokens nuevos | mediana **38,4 min** (23,5–41,6) |
| Edad del par al detectar | mediana **4,5 min** (script_82 ve el lanzamiento a tiempo) |
| Edad del par al emitir | mediana **44,2 min** |
| Precio ya movido ≥ +100 % en el snapshot con el que se emitió | 5 de 12 (e/acc +811 %, SPR +4054 %, 1M X +7243 %, AIRPAD h24 +988 %, DEGEN h24 +890 %) |
| Retraso del scheduler de Actions sobre la grilla `*/20` (30 corridas de `pipeline_t0`, 09:33–19:06 UTC) | media **11,9 min**, mediana 11,4, máx 19,6 |
| Duración de una corrida de `pipeline_t0` | **5,8 min** (incluye 5 min de escucha de PumpPortal) |

Las alertas CEX (JASMY, TRAC, PHA, MON, BTC, LDO, CVX, SOL) no tienen datos intradía en su registro. Su gap sale
recién con las velas de Binance.

### 1.2 De dónde sale la latencia [V/I]

1. **La edad mínima de emisión** (`EMIT_MIN_AGE_MIN = 30`, calibración v7.2.1). script_82 detecta el token a los
   ~4 min de edad. script_97 no lo puede emitir antes de los 30 min. Es el piso del diseño [V].
2. **La cadencia del chequeo.** El primer chequeo después de los 30 min llega en promedio 10 min tarde (cron
   `*/20`). Piso teórico: 30 + 20/2 = **40 min**; lo observado es 42–46 [V].
3. **La escucha de PumpPortal dura solo 5 min por corrida.** Sobre ~20 min entre corridas, ~75 % de los
   lanzamientos no se ven nunca [I: 5 min de 20].
4. **El retraso del scheduler** (~12 min de media). Desplaza todas las corridas. No suma al piso de un token ya
   detectado, pero sí a un activo que acelera entre corridas (ruta CEX, tokens viejos) [I].

### 1.3 Gap medido con velas [P]

`latency_analysis.yml` (manual) hace el cálculo completo con velas de 1 min:
- on-chain: GeckoTerminal, pool = `dexscreener.pairAddress`;
- CEX: Binance data-api, `{SYMBOL}USDT`.

El inicio del pump es el primer minuto con un cierre ≥ +5 % sobre el cierre de 5 min antes. Si el pool tiene
menos de 5 min, la referencia es la apertura de la primera vela. El gap es emisión − inicio, y un valor negativo
significa que la alerta fue anticipada.

El contenedor de Claude no llega a esas APIs, así que la corrida queda para cuando el workflow esté en main.

## 2. Señales anticipatorias (T2) — `lib_early_signals.py` (`early-0.1`)

Funciones puras con tests sobre datos sintéticos. Cada señal da `s ∈ [0,1]` y aporta `points = POINTS·s`. El bono
es `floor(Σ points)` con **tope 8**. **Solo suma**: ninguna señal resta, y una señal en contra da 0.

| # | Señal | Fuente | Puntos máx. | Qué anticipa |
|---|---|---|---|---|
| 1 | `volume_acceleration` | DexScreener (volumen m5 vs. tasa media de h1) | 3 | Entra volumen antes que precio |
| 2 | `buy_pressure_shift` | DexScreener (txns m5 vs. h1) | 2 | Giro a compras |
| 3 | `quiet_accumulation` | DexScreener: vol ×≥2 + compras ≥60 % + \|m5\| < 5 % | 3 | **La firma previa al pump**: se acumula con el precio quieto |
| 4 | `liquidity_inflow` | serie propia de liquidez del pool (polls de 2 min) | 2 | Entra liquidez (+30 % en 10 min = máx.) |
| 5 | `orderbook_imbalance` | Hyperliquid `l2Book` / dYdX v4 (±2 % del mid) | 3 | Muro comprador |
| 6 | `holder_accumulation` | RugCheck (`totalHolders`, top-10) | 2 | Holders nuevos por minuto sin que suba la concentración |
| 7 | `social_velocity` | script_115 (doc 26: sorpresa de Poisson, m_1h vs. m_prev_1h) + CoinGecko trending | 3 | La atención sube antes que el precio |
| 8 | `funding_squeeze` | Hyperliquid `metaAndAssetCtxs` (serie propia) | 2 | Funding z ≤ −1,5 con OI que no baja: setup de squeeze |
| 9 | `fear_greed_extreme` | alternative.me (vía script_114) | 1 | Extremo de miedo (contrarian) |

Parámetros heurísticos [H]. Se calibran con `historical_alerts.jsonl` cuando haya n suficiente; cada alerta
temprana guarda `early.active` y `early.reasons` para eso.

Integración:
- **Solana:** `script_116` re-puntúa con v7.2.1 sin cambios y suma el bono (señales 1–4, 6, 7).
- **Multi-chain:** `lib_scoring_multichain.evaluate(..., early=)` (`apply_early`) suma el bono de
  `02_Analisis/early/_signals.json` (señales 5, 8, 9) si tiene menos de 20 min. Lo hace en `script_97`, grupos
  emitibles; b e i siguen siendo solo registro.

## 3. Polling ≤ 10 min (T3) — `script_116_early_watch.py` + `early_watch.yml`

**Método.** Un job largo:
- arranca con cron `7,37 * * * *` (minutos fuera del pico, que es donde el scheduler más se atrasa);
- hace **un poll cada 120 s** durante 40 min;
- la concurrencia `early-watch` encola la corrida siguiente, así la cobertura sigue continua aunque el scheduler
  se atrase.

El repo es **público**, así que los minutos de Actions en runners estándar no tienen límite [V: `visibility: public`].

**Intervalo efectivo: 2 min** (antes 20 + ~12 de retraso).

Cada poll:
1. **PumpPortal en continuo** (hilo con reconexión, `subscribeNewToken`, mismo filtro que script_82). Se ve el
   ~100 % de los lanzamientos, no el ~25 %.
2. Watchlist = esos lanzamientos (hasta 3 h) + `_accumulated.json` (score ≥ 40, últimas 6 h, no alertados).
3. DexScreener en lotes de 30 (`tokens/v1/solana/...`). Se re-puntúa con `script_82.score_token`. Paridad con
   script_97: dentro de los 60 min de la detección vale el score de detección si es mayor. Después se suma el bono.
4. Se emite si:
   - `score + bono ≥ 56`;
   - edad ≥ `EARLY_MIN_AGE_MIN` (por defecto = `EMIT_MIN_AGE_MIN` = 30, configurable por env);
   - hay guía de compra;
   - el par tiene menos de 180 días (grupo i: no se emite).

   Máximo 3 por poll.
5. Registro **antes** de enviar (`02_Analisis/early/_early_alerts.json`, push inmediato). Después Telegram, con el
   mensaje de script_97 (🛒 primero).
6. RugCheck para hasta 8 tokens por poll que el bono puede llevar al umbral, cada 5 min por token.
7. Multi-chain: order book + funding/OI para los 25 activos puntuados con perp → `_signals.json`.

**Sin doble emisión.**
- Mientras `early_watch` tiene una corrida en curso, `script_97.early_watch_active()` (API de Actions con
  `actions: read`) cede la ruta Solana.
- En todos los casos, script_97 **adopta** las alertas tempranas en `_all_alerts.json`: script_98 las sigue y el
  dataset las registra. También les adjunta el dossier (doc 24) como documento aparte.
- Sin early watch activo, script_97 lee `_early_alerts.json` de `origin/main` recién traído (`git fetch`) antes de
  elegir. Así no repite lo que se pusheó después de su checkout.
- `EARLY_HANDOFF=false` desactiva el hand-off.

**Piso nuevo** con gate 30 y poll de 2 min: edad al emitir ≈ **31 min** (antes ~44) [I: 30 + 2/2].
El gate de 30 min es una calibración de v7.2.1 y no lo toqué. Con `EARLY_MIN_AGE_MIN` se baja sin cambiar código.
Con gate G, el piso es G + 1 min.

## 4. Order book (T4)

- **Hyperliquid `l2Book`**: principal. Gratis, sin key, todos los perps listados en `_perps.json`.
- **dYdX v4** (`indexer.dydx.trade/v4/orderbooks/perpetualMarket/{T}-USD`): respaldo para los que no están en
  Hyperliquid.
- **GMX:** no tiene libro (es un pool contra oráculo). No aplica.
- **Jupiter:** la API gratuita sin key es `lite-api.jup.ag`, que está **prohibida** por directiva. La liquidez de
  Solana se mide por la serie de `liquidityUsd` del pool (señal 4).

## 5. On-chain (T5)

- **RugCheck** (`/v1/tokens/{mint}/report`): sin key. Da `totalHolders`, `topHolders[].pct` e `insider`.
  `rugcheck_snapshot` guarda holders, top-10 e insiders, y `holder_accumulation` mide holders/min.
- **Solscan:** la API pública pide key Pro. No se usa.
- **MadeOnSol:** hay secret (`MADEONSOL_API_KEY`), pero no está verificado qué endpoint da holders. Queda en [P].

## 6. Social (T6)

- **script_115** (doc 26) ya produce por token: `m_1h`, `m_prev_1h`, `surprise_nats`, `seff_1h` y el hit de
  CoinGecko trending. `social_velocity` los convierte en bono.
- **X/Twitter:** no hay fuente gratuita sin cuenta. Lo visto en doc 25: Agent-Reach exige cookies de cuentas, y las
  instancias de Nitter no son estables. Fuera.
- La cadencia del colector sigue en 20 min, así que la señal social llega con hasta 20 min de retraso.

## 7. Archivos

| Archivo | Rol |
|---|---|
| `04_Config/scripts/latency_analysis.py` + `test_latency_analysis.py` (7) | T1 |
| `04_Config/scripts/lib_early_signals.py` + `test_lib_early_signals.py` (17) | T2 |
| `04_Config/scripts/script_116_early_watch.py` + `test_script_116_early_watch.py` (12) | T3–T6 |
| `04_Config/scripts/script_97_emit_alerts.py` (hand-off, adopción, bono multi-chain) + `test_script_97_early.py` (6) | integración |
| `04_Config/scripts/lib_scoring_multichain.py` (`apply_early`, `early=`) | integración |
| `.github/workflows/early_watch.yml` (nuevo), `latency_analysis.yml` (nuevo), `pipeline_t0.yml` (+`actions: read`, `GITHUB_TOKEN`) | workflows |
| `02_Analisis/early/{_watch.json,_early_alerts.json,_signals.json}` | estado de script_116 (solo él los escribe) |

## 8. Métricas de éxito de la Fase 10

| Métrica | Objetivo | Estado |
|---|---|---|
| Latencia media < 10 min | gap inicio → emisión | **[P]**. Con gate 30, el piso para un token que bombea desde el lanzamiento es ~31 min. Para un pump que arranca después de los 30 min de edad (o en tokens viejos y CEX), el poll de 2 min deja el gap en ~1–3 min. La medición sale con `latency_analysis.yml` después de 24–48 h de early watch. |
| ≥ 3 señales anticipatorias | implementadas | **9** [V] |
| Polling ≤ 10 min | intervalo | **2 min** [V código, P producción] |
| ≥ 30 % de alertas dentro de los primeros 5 min del pump | `within_5min_pct` | [P] misma medición |
