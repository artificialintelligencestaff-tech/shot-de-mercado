---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: INVESTIGACIÓN (sin código productivo)
last_updated: 2026-09-30
version: 1.0
---

# 23 — Investigación de los 8 grupos de activos

Rótulos: [V] verificado en esta sesión (HTTP / `gh api` / archivo) · [I] inferido · [H] hipótesis · [P] pendiente.
Evidencia cruda: `02_Analisis/diagnostics/grupos_activos_probe.json` (42 fuentes). Se reproduce con
`python 04_Config/scripts/probe_grupos_activos.py` (con `--no-burst` para no medir límites).

Grupos: **a** memes micro-cap · **b** presale / pre-market · **c** DeFi de gobernanza nueva · **d** sintéticos y derivados algorítmicos · **e** DePIN · **f** L1/L2 emergentes · **g** RWA especulativo · **h** blue chips.
Orden de prioridad (directiva): **h → f, e, c → g, b, d → a**.

---

## 0. Resumen ejecutivo

| Grupo | Fuentes gratis verificadas (200, sin key) | Hueco principal | ¿GARCH/ATR/Bollinger? | Fase |
|---|---|---|---|---|
| h blue chips | 9/9: Binance, Coinbase, Kraken, Deribit DVOL, Fear & Greed, CoinPaprika, mempool, CoinGecko sin key, funding Binance | Funding de Binance probablemente bloqueado desde runners de EE.UU. [I] | **Sí** (Universo A) | 1 |
| f L1/L2 | 7/7: DefiLlama chains/TVL/fees, growthepie, L2BEAT, GeckoTerminal networks | Historia corta en L1 nuevas (Monad: 320 días) [V] | Solo con ≥ 1 año de velas [H] | 2 |
| e DePIN | 2/3: CoinGecko categoría `depin` + lista de 1040 categorías; DefiLlama categoría `DePIN` (9 protocolos) | DePINscan sin API pública (4 rutas → 404) [V] | Solo mid-caps con historia [H] | 2 |
| c DeFi gobernanza | 3/5: Snapshot GraphQL, DefiLlama protocols (`listedAt`), DefiLlama fees | Tally pide key; unlocks de DefiLlama son de pago (402) [V] | No (event studies) | 2 |
| g RWA | 2/3: CoinGecko categoría RWA, DefiLlama categoría `RWA` (181 protocolos) | rwa.xyz no es accesible sin key [V] | No | 3 |
| b pre-market | 3/4: Hyperliquid meta + ctxs, HIP-3 perpDexs (10), Aevo (tipo `pre_ipo`: 2) | Sin fuente gratuita de preventas cripto; CoinGecko "new coins" es de pago [V] | No (sin historia) | 3 |
| d sintéticos | 4/5: DefiLlama stablecoins (`pegMechanism`), dYdX v4, GMX tickers, Hyperliquid | Overview de derivados de DefiLlama pasó a pago (402) [V] | Solo perps de majors | 3 |
| a memes micro-cap | 8/8: GoPlus (EVM + Solana), RugCheck, Honeypot.is, DexScreener, GeckoTerminal new_pools (Base, Blast, Monad) | Blast: 0 pools nuevos [V] → despriorizar | **No** (prohibido) | 3 (ya en producción) |

Conclusión [V]: con fuentes 100% gratuitas y sin key se pueden cubrir los 8 grupos. Los tres agujeros reales son:
1. token unlocks (de pago);
2. preventas cripto antes de listar (no hay fuente abierta estable);
3. DePIN a nivel red, con métricas de nodos/ingresos por proyecto (sin API pública).

---

## 1. Método

- **Fecha y lugar:** 2026-09-30 05:55-06:01 UTC, desde el equipo local (IP de Argentina) [V]. **No se midió desde GitHub Actions** (runners en EE.UU.) [P]. Esto importa para Binance (derivados) y CoinGecko sin key (IP compartida).
- **Por fuente:** 1 request con status, latencia, headers de rate limit, esquema de campos, bytes y, cuando aplica, cobertura temporal (primer dato disponible).
- **Ráfaga** en las fuentes clave: 8 requests seguidos sin pausa → cantidad de 429. Si aparece un 429, cooldown de 70 s antes de la próxima fuente para no contaminar la medición.
- **Licencias:**
  - repos con `gh api repos/<r>` y, si GitHub dice `NOASSERTION`, lectura del archivo LICENSE [V];
  - paquetes con PyPI JSON (`license_expression`, `requires_dist`) [V].
- **MCPs:** búsqueda `gh api search/repositories` (`<fuente> mcp`) y verificación de licencia, fecha del último push y organización dueña [V].
- **Papers:** alphaXiv, publicados desde 2025-10 [V] (títulos y resúmenes; no se leyeron completos [P]).
- **Límites del método:**
  - Una sola corrida: la latencia varía (DefiLlama `/v2/chains`: 5276 ms en frío vs 136 ms en caliente) [V].
  - Los headers de rate limit solo muestran lo que cada proveedor expone.
  - Una ráfaga de 8 no encuentra el techo real: **"0 × 429 en 8" es una cota inferior**, no el límite.

---

## 2. Matriz de fuentes (evidencia del probe)

| Grupo | Fuente | Status | Rate limit medido | Cobertura / tamaño |
|---|---|---|---|---|
| h | Binance `data-api.binance.vision` klines | 200 | peso 2 por llamada (`x-mbx-used-weight-1m`); ráfaga 0/8 × 429 | BTCUSDT diario desde **2017-08-17** |
| h | Binance `fapi` fundingRate | 200 | sin headers | desde **2019-09-10** |
| h | Coinbase Exchange candles | 200 | ráfaga 0/8 | 350 velas por request (diarias) |
| h | Kraken OHLC | 200 | — | hasta 720 velas por request [I] |
| h | Deribit DVOL (vol implícita) | 200 | — | paginado de a 1000 filas (`continuation`); la 1.ª página llega a 2024-01-05 [V]; la historia completa [P] |
| h | alternative.me Fear & Greed | 200 | — | **3160 días desde 2018-02-01** |
| h | CoinPaprika ticker | 200 | `ratelimit-limit: 20000` (ventana larga [I]); ráfaga 0/8 | `first_data_at`, `beta_value` |
| h | mempool.space fees | 200 | — | tiempo real |
| h | CoinGecko simple (sin key) | 200 | **ráfaga 4/8 × 429** → ~4-5 req por ráfaga | tiempo real |
| f | DefiLlama `/v2/chains` | 200 | ráfaga 0/8, sin headers | 467 cadenas |
| f | DefiLlama TVL histórico Base | 200 | — | 1734 días desde 2022-01-01 (TVL actual 6,25 B) |
| f | DefiLlama TVL histórico Monad | 200 | — | 320 días desde **2025-10-25** (TVL 1,03 B) |
| f | DefiLlama fees por cadena (Base) | 200 | — | 473 protocolos con fees 24 h/7 d/30 d/1 a |
| f | growthepie `master.json` | 200 | — | métricas y lista de L2 (arbitrum, base, celo, …) |
| f | L2BEAT `/api/scaling/summary` | 200 | — | `projects` + `chart` (274 KB) |
| f | GeckoTerminal `/networks` | 200 | — | 3 páginas × 100 redes; incluye `monad` [V] |
| e | CoinGecko `coins/markets?category=depin` | 200 | comparte el límite sin key | 20 por página |
| e | CoinGecko `coins/categories/list` | 200 | ídem | 1040 categorías |
| e | DePINscan (4 rutas probadas) | **404** | — | sin API pública encontrada |
| c | Snapshot GraphQL | 200 | **100 req / 60 s** (`ratelimit-policy`); ráfaga 0/8 | propuestas activas, votos, `scores_total` |
| c | DefiLlama `/protocols` | 200 | — | 8421 protocolos; **536 listados en los últimos 90 días**; categorías: Derivatives 449, Launchpad 309, RWA 181, Prediction Market 126, Algo-Stables 123, Synthetics 44, Governance Incentives 15, DePIN 9 |
| c | DefiLlama fees overview | 200 | — | 2796 protocolos |
| c | Tally GraphQL | **401** | "api key required" | — |
| c | DefiLlama emissions (unlocks) | **402** | de pago | — |
| g | CoinGecko categoría `real-world-assets-rwa` | 200 | límite sin key | 20 por página |
| g | rwa.xyz API | **404** sin key | — | — |
| b | Hyperliquid `info` metaAndAssetCtxs | 200 | ráfaga 0/8 | 234 perps (56 deslistados); funding, OI, premium, markPx, oraclePx |
| b | Hyperliquid `perpDexs` (HIP-3) | 200 | — | 10 DEX de terceros (xyz: 123 activos: acciones, commodities) |
| b | Aevo markets | 200 | — | 102 mercados; tipos crypto 55, equity 32, **pre_ipo 2 (ANTHROPIC, OPENAI)** |
| b | CoinGecko `coins/list/new` | **401** | de pago | — |
| d | DefiLlama stablecoins | 200 | — | 427 activos; `pegMechanism`: fiat 146, crypto 253 (+1 mal escrito "crytpo-backed"), **algorítmicos 27** |
| d | DefiLlama derivatives overview | **402** | de pago | — |
| d | dYdX v4 indexer perpetualMarkets | 200 | `ratelimit-limit: 100`; ráfaga 0/8 | todos los mercados perp |
| d | GMX Arbitrum tickers | 200 | — | 120 tokens (min/max price) |
| a | GoPlus token_security Base (EVM) | 200 | ráfaga 0/8, sin headers | 39 campos: `is_honeypot`, `buy_tax`/`sell_tax`, `is_mintable`, `hidden_owner`, `lp_holders`, `holder_count`, `creator_percent`, … |
| a | GoPlus token_security Solana | 200 | — | ídem, versión Solana |
| a | RugCheck summary | 200 | `x-rate-limit-limit: 15`; ráfaga 0/8 | `score`, `score_normalised`, `lpLockedPct`, `risks[]` |
| a | Honeypot.is (Base) | 200 | `x-ratelimit-limit: 50` | `honeypotResult`, `simulationResult` (taxes), `flags` |
| a | DexScreener token-profiles/latest | 200 | ráfaga 0/8 | 30 perfiles (`chainId`, `cto`, links) |
| a | GeckoTerminal new_pools Base / Blast / Monad | 200 | (429 conocidos del pipeline: 6,5 s entre llamadas) | **Base 20 · Blast 0 · Monad 5** pools nuevos en la 1.ª página |

---

## 3. Grupos (en orden de prioridad)

### 3.h Blue chips (BTC, ETH, SOL — Universo A)

**Fuentes [V]**
- Velas: Binance data-api (principal); Coinbase y Kraken como verificación cruzada del precio.
- Volatilidad implícita: Deribit DVOL (el análogo cripto del VIX).
- Sentimiento: Fear & Greed diario.
- Derivados: funding de Binance.
- Red: fees de mempool.space.

**Cobertura temporal [V]:** diario desde 2017 (Binance), sentimiento desde 2018, funding desde 2019. Es la única clase con historia suficiente para modelos clásicos.

**Multi-chain:** no aplica; son precios de exchange.

**Integración:** `script_1xx_universo_a.py` con `requests` + cache JSON, cron diario/horario en Actions. Sin keys.

**Modelos clásicos (sí aplican):**
- GARCH(1,1) / EGARCH y HAR-RV sobre retornos diarios;
- ATR y Bollinger como filtros de régimen;
- DVOL como vol implícita: el spread DVOL − vol realizada es una señal de prima de riesgo [H].

**Librería:** `arch` 8.0.0 [V].
- Licencia **NCSA**, permisiva tipo BSD (verificada en el LICENSE, porque GitHub la reporta como NOASSERTION).
- Último push 2026-09-27; 1581 ★.
- Dependencias: numpy, pandas, scipy, statsmodels, packaging (todas BSD) [V].
- **Instalar solo cuando se implemente la Fase 1**, con pin de versión.

**Señales de scoring [H]:**
- z-score de vol realizada vs GARCH esperado;
- DVOL − RV;
- funding extremo (percentil 95 de su historia);
- Fear & Greed en extremos (≤ 20 / ≥ 80) como contrarian;
- ruptura de Bollinger con volumen.

**Papers 2026:**
- *Loss Choice or Model Choice? … Cryptocurrency Volatility Forecasting* (arXiv 2609.27024): el nivel del pronóstico importa tanto como el modelo.
- *Fear Moves Markets: Sentiment-Augmented POMP* (2609.23250): sentimiento + volatilidad de BTC.
- *Do Prediction Markets Forecast Cryptocurrency Volatility?* (2604.01431): Kalshi macro → vol realizada.
- *The Quarter-Hour Effect* (2607.09426): estacionalidad intradía en perps de Binance.

**MCPs:**
- `coingecko/coingecko-typescript`, paquete `@coingecko/coingecko-mcp` 8.2.0: Apache-2.0, push 2026-09-28, organización oficial [V].
- No hace falta para el pipeline, que usa HTTP directo [I].

**Riesgos:**
- [I] Los runners de Actions están en EE.UU. y `fapi.binance.com` suele devolver 451 a IPs de EE.UU. Verificarlo con una corrida en Actions [P]. Fallback: funding de Hyperliquid o dYdX [V ambas 200].
- [V] CoinGecko sin key: 4 de cada 8 requests en ráfaga dan 429. Espaciar a ≥ 15 s o usar Binance/Coinbase.

### 3.f L1/L2 emergentes (Monad, Base, Berachain, …)

**Fuentes [V]:**
- DefiLlama: TVL histórico por cadena, fees por cadena y protocolo, lista de cadenas;
- growthepie `master.json`: métricas L2;
- L2BEAT summary: riesgo y TVS de L2;
- GeckoTerminal networks: qué cadenas tienen DEX indexados.

**Cobertura [V]:** Base desde 2022-01; **Monad desde 2025-10-25 (320 días)**.

**Multi-chain:** es el grupo multi-chain por definición. GeckoTerminal ya indexa `monad` [V].

**Integración:** un colector diario por cadena (TVL, fees, cantidad de protocolos nuevos) y el token nativo vía Binance/Coinbase si lista.

**Licencias y actividad [V]:**
- `l2beat/l2beat`: MIT, push 2026-09-29.
- `growthepie/gtp-backend`: MIT, push 2026-09-29.
- `DefiLlama/DefiLlama-Adapters`: **sin licencia declarada**. Se consume la API; no se copia código.

**Modelos:**
- momentum relativo vs ETH/SOL;
- crecimiento log de TVL y fees;
- fees/TVL como "uso real";
- GARCH solo para tokens con ≥ 365 velas diarias [H]. Monad todavía no llega.

**Señales [H]:**
- aceleración de TVL (2.ª derivada 7 d);
- ratio fees/TVL en percentil alto;
- protocolos nuevos por semana (DefiLlama `listedAt` filtrado por cadena).

**MCPs:** `DefiLlama/defillama-skills`, de la organización oficial [V]. Queda descartado:
- último push 2026-03-26, más de 6 meses;
- sin licencia.

**Riesgos:**
- TVL inflado por doble conteo [I];
- cadenas "fantasma" con TVL incentivado: Blast tiene 0 pools nuevos en GeckoTerminal [V], señal de actividad agotada.

### 3.e DePIN

**Fuentes [V]:**
- CoinGecko: categoría `depin` (mercado) y `categories/list` (1040 categorías, para mapear ids);
- DefiLlama: categoría `DePIN`, solo 9 protocolos [V] (cobertura baja).

**Fuente buscada sin éxito:** DePINscan. 4 rutas de API → 404 [V], así que no hay API pública utilizable.

**Cobertura:** la de CoinGecko (series de precio por id; sin key hay límite).

**Multi-chain:** Solana (Helium, Hivemapper, Render), Ethereum, IoTeX, etc. Se mapea por `id` de CoinGecko, no por cadena.

**Integración:** colector diario de la categoría (precio, mcap, FDV, volumen) + fees de DefiLlama para los 9 protocolos con datos.

**Modelos:** valoración fees/FDV y momentum de categoría; GARCH solo para mid-caps con historia [H].

**Señales [H]:**
- divergencia precio vs fees 30 d;
- FDV/mcap alto = presión de unlocks. Los unlocks no tienen fuente gratuita (DefiLlama emissions **402**) [V].

**MCPs:** ninguno específico encontrado [V: búsqueda sin resultados relevantes].

**Riesgos:**
- métricas de red (nodos, ingresos reales) dependen de cada proyecto;
- sin DePINscan, la comparación entre proyectos es pobre [I].

### 3.c DeFi de gobernanza nueva

**Fuentes [V]:**
- Snapshot GraphQL, **100 req / 60 s** medido: propuestas activas, votos, `scores_total`;
- DefiLlama `/protocols`, 8421 protocolos: `listedAt` permite detectar **nuevos (536 en 90 días)**, más categoría, cadenas, `gecko_id`, `mcap`;
- DefiLlama fees overview (2796 protocolos).

**Descartadas [V]:**
- Tally: 401, pide key;
- DefiLlama emissions/unlocks: 402, de pago.

**Multi-chain:** DefiLlama trae `chains` por protocolo. Snapshot cubre todo EVM y otras.

**Integración:**
- cruce diario "protocolo nuevo con `gecko_id`" → serie de precio;
- propuestas Snapshot de esos espacios como eventos.

**Licencias y actividad [V]:** `snapshot-labs/snapshot-hub` es MIT pero **archivado** (push 2026-05-07). La API pública (`hub.snapshot.org`) respondió 200. Riesgo de continuidad [I].

**Modelos:** event study alrededor del cierre de propuestas; fees/mcap; participación (votos / holders).

**Señales [H]:**
- protocolo < 90 días con fees en ascenso y mcap/TVL bajo;
- propuestas con cambio de emisiones o fee switch.

**MCPs:** ninguno viable. Los encontrados tienen 0-3 ★ y no declaran licencia [V].

**Riesgos:**
- gobernanza capturada por whales;
- sin datos de unlocks gratis, no se ve la dilución [V].

### 3.g RWA especulativo

**Fuentes [V]:**
- CoinGecko categoría `real-world-assets-rwa`;
- DefiLlama categoría `RWA`, **181 protocolos** (TVL, fees).

**Descartada:** rwa.xyz (404 / requiere key) [V].

**Multi-chain:** Ethereum, Solana, Polygon, etc., vía DefiLlama `chains`.

**Integración:** colector diario de la categoría + TVL por protocolo.

**Modelos:**
- prima o descuento mcap/TVL;
- en tokens de tesorería tokenizada la vol es ~0: **no** hay que modelar precio, sino flujos (TVL).

**Señales [H]:** tokens de gobernanza de plataformas RWA con TVL creciendo más rápido que el mcap.

**MCPs:** ninguno encontrado.

**Riesgos:**
- mezcla de activos estables (T-bills) con tokens especulativos: hay que filtrar por volatilidad antes de puntuar [I];
- riesgo regulatorio.

### 3.b Presale / pre-market

**Fuentes [V]:**
- Hyperliquid metaAndAssetCtxs (234 perps: funding, OI, premium, oracle vs mark);
- Hyperliquid `perpDexs`: **10 DEX HIP-3** desplegados por terceros, por ejemplo `xyz` con 123 activos (acciones, commodities);
- Aevo: 102 mercados, 2 de tipo **`pre_ipo`** (ANTHROPIC, OPENAI).

**Hallazgo [V]:** hoy los "pre-market" gratuitos observables son **pre-IPO de acciones**, no preventas cripto. Aevo no expone un flag de pre-launch cripto activo. CoinGecko "new coins" es de pago (401).

**Multi-chain:** no aplica (perps off-chain / L1 propia).

**Integración:** snapshot horario de Hyperliquid y Aevo con `requests`. **Solo lectura, sin cuentas ni firmas.**

**Licencias y actividad [V]:**
- `hyperliquid-dex/hyperliquid-python-sdk`: MIT, push 2026-06-04. No hace falta: la API `info` es un POST simple.

**Modelos:** no hay historia, así que nada de GARCH. Convergencia premium → 0 al listar; funding como termómetro de demanda.

**Señales [H]:** premium mark/oracle alto + OI creciente antes de un listing spot.

**MCPs [V]:**
- `hypurrquant/perp-cli` (MIT, push 2026-09-04, CLI + MCP multi-DEX): activo, pero orientado a operar. **No usar** para trading; solo como referencia de lectura.
- `caiovicentino/hyperliquid-mcp-server`: MIT, pero sin push desde 2025-11 (más de 6 meses) → descartado.

**Riesgos:** mercados pre-IPO sin subyacente líquido; manipulación con OI bajo; delistings (56 de 234 perps deslistados en Hyperliquid) [V].

### 3.d Sintéticos y derivados algorítmicos

**Fuentes [V]:**
- DefiLlama stablecoins: `pegMechanism` (**27 algorítmicos**: USDN, FRAX, BEAN, USDR, …), `price`, circulante día/semana/mes;
- dYdX v4 indexer: todos los perps, límite 100 medido;
- GMX tickers (120);
- Hyperliquid (funding / OI).

**Descartada:** DefiLlama derivatives overview → 402 de pago [V].

**Multi-chain:** stablecoins por cadena (`chainCirculating`, 210 cadenas) [V].

**Integración:** colector horario de desvío de peg y funding.

**Licencias [V]:**
- dYdX v4-chain / v4-clients: **licencia propietaria de dYdX Trading** (no permisiva);
- GMX synthetics: **BUSL-1.1**;
- conclusión: se consumen **solo las APIs HTTP**, nunca su código.

**Modelos:**
- distancia al peg `|price − 1|` con reversión a la media (Ornstein-Uhlenbeck) [H];
- hazard de depeg por caída del circulante [H];
- GARCH solo para perps de majors.

**Señales [H]:**
- caída de circulante > X% semanal + desvío > 1% → riesgo de espiral;
- funding extremo en perps sintéticos.

**MCPs:** ninguno específico viable.

**Riesgos:**
- errores de datos en la fuente: `"crytpo-backed"` mal escrito en DefiLlama [V] (normalizar);
- stablecoins muertas que siguen listadas (FEI) [V].

### 3.a Memes micro-cap (Solana en producción; Base, Blast y Monad en el Universo C)

**Fuentes [V]:**
- las del pipeline actual (DexScreener, GeckoTerminal, Jupiter V2);
- **GoPlus** token_security EVM y Solana (39 campos de riesgo);
- **RugCheck** (Solana; `score`, `lpLockedPct`, `risks[]`; límite 15 por header);
- **Honeypot.is** (EVM; simulación de compra/venta; límite 50);
- GeckoTerminal new_pools por red: **Base 20 · Blast 0 · Monad 5** [V].

**Multi-chain:** GoPlus cubre EVM (por `chain_id`) y Solana. Honeypot.is solo EVM. RugCheck solo Solana.

**Integración:** enriquecimiento por token ya candidato (≤ 1 llamada por token por proveedor), no barridos. Respetar el límite 15 de RugCheck.

**Licencias y actividad [V]:**
- `GoPlusSecurity/goplus-sdk-python`: Apache-2.0, push 2026-08-21. No hace falta, es HTTP GET.
- `GoPlusSecurity/goplus-mcp`: Apache-2.0 pero **sin push desde 2025-05** → descartado.
- `goplus/mcp`: **falso positivo** (es el lenguaje XGo, no GoPlus Security) [V].

**Modelos:** **NO** GARCH/EGARCH/ATR/Bollinger/VIX (prohibido). Sirven:
- event study;
- métrica dual (doc 19);
- Wilson/bootstrap;
- features de riesgo de rug.

**Señales [H], dirigidas al hallazgo H-84** (76% cae −99% después de +20%):
- `is_honeypot`, `sell_tax` > 10%;
- `is_mintable`, `hidden_owner`, `owner_change_balance`;
- `lpLockedPct` bajo;
- concentración `creator_percent` + top holders;
- `risks[]` de RugCheck.

Hipótesis a testear: **estas features predicen el "rug después del hit"** y bajan el 76%.

**Papers 2026:**
- *Catching the Rug: Early Prediction of Fraudulent Memecoins on Solana* (2608.20271);
- *From Hype to Collapse: Rug Pull Scams on Solana* (2603.24625);
- *MELT: Behavioral Trace Dataset for High-Risk Memecoin Launch Detection* (2602.13480);
- *Coordinated Sniper Cohorts on Pump.fun* (2607.02795);
- *Meme Coin Factories … pump.fun* (2609.10246, EPFL/ETH/CMU);
- *Measuring Memecoin Fragility* (2512.00377);
- *How To Cook The Fragmented Rug Pull?* (2511.15463): rugs en varias ventas pequeñas, relevante para la caída −99%.

**Riesgos:**
- los proveedores de seguridad pueden cambiar límites sin aviso;
- RugCheck score "101" en BONK con solo "Mutable metadata" [V]: calibrar su escala antes de usarla;
- Blast sin actividad [V].

---

## 4. Estrategia de expansión en 3 fases

| Fase | Grupos | Entregable | Criterio de salida | Esfuerzo [I] |
|---|---|---|---|---|
| **1** | h | `script_1xx_universo_a.py` (Binance + Coinbase, DVOL, F&G, funding con fallback a Hyperliquid/dYdX) + `arch` (GARCH/HAR) + tests + modo sombra + monitor dual adaptado a Universo A | Verificar el acceso desde Actions (Binance fapi 451?); walk-forward con purga; IC90 de la métrica elegida por encima del baseline | 1 sesión |
| **2** | f, e, c | Colector DefiLlama (chains, fees, protocols nuevos) + growthepie/L2BEAT + CoinGecko categorías (espaciado ≥ 15 s + cache) + Snapshot (eventos) | Tabla diaria estable 14 días sin 429; señales [H] evaluadas con event study y placebo | 1-2 sesiones |
| **3** | g, b, d | RWA (DefiLlama/CoinGecko), pre-market (Hyperliquid/Aevo), sintéticos (stablecoins, dYdX, GMX) | Peg/funding monitoreados; ninguna señal pasa a emisión sin validación | 1-2 sesiones |
| **a** (continuo) | a | Enriquecimiento de riesgo GoPlus/RugCheck/Honeypot sobre candidatos ≥ 56 (solo registro, **sin cambiar el score**) → test de la hipótesis anti-H-84 | Después del veredicto v7.2.1; features medidas contra "rug después del hit" con n suficiente | 1 sesión |

**Reglas comunes:**
- todo en sombra primero;
- una rama por fase;
- nada de emisión real sin validación;
- sin keys;
- cache JSON por fuente;
- tope de llamadas por corrida (como `--max-calls` del monitor);
- los bots gemelos cubren la salud de los nuevos workflows.

---

## 5. Fuentes y repos descartados (y por qué)

| Candidato | Motivo | Rótulo |
|---|---|---|
| Tally API | pide API key | [V] 401 |
| DefiLlama emissions / derivatives overview | de pago | [V] 402 |
| CoinGecko `coins/list/new` | de pago | [V] 401 |
| rwa.xyz | sin acceso sin key | [V] 404 |
| DePINscan | sin API pública | [V] 404 × 4 |
| `GoPlusSecurity/goplus-mcp` | inactivo > 6 meses | [V] |
| `goplus/mcp` | no es GoPlus Security | [V] |
| `DefiLlama/defillama-skills` | inactivo > 6 meses, sin licencia | [V] |
| `caiovicentino/hyperliquid-mcp-server` | inactivo > 6 meses | [V] |
| `vibeforge1111/dexscreener-cli-mcp-tool` | sin licencia | [V] |
| `snapshot-labs/snapshot-hub` (código) | archivado (la API sigue viva) | [V] |
| código de dYdX / GMX / mempool | licencia propietaria / BUSL / AGPL: solo APIs | [V] |

---

## 6. Riesgos transversales

1. **Geografía del runner** [I]: Actions corre en EE.UU. Binance derivados y otras APIs pueden bloquear por IP. Cada fuente nueva se verifica **desde Actions** antes de depender de ella [P].
2. **Límites de IP compartida** [I]: CoinGecko sin key en runners compartidos puede estar agotado de antemano. Siempre con fallback.
3. **Cambios de plan** [V]: DefiLlama movió al menos dos endpoints a pago (402). Toda fuente necesita su sonda en `probe-fuentes` o en el health check.
4. **Calidad de datos** [V]: typos de categoría, activos muertos listados, escalas de score no documentadas (RugCheck). Normalizar y documentar.
5. **Sesgo de supervivencia** [I]: las listas por categoría muestran lo vivo. Para backtests hay que guardar snapshots propios desde el día 1.

---

## 7. Deudas y preguntas

- [P] Correr `probe_grupos_activos.py --no-burst` **desde Actions** (workflow_dispatch) para medir el acceso real desde EE.UU. Requiere agregar un workflow o un paso a `probe-fuentes.yml`: **consultar antes** (es un workflow).
- [P] Paginar Deribit DVOL completo (`continuation`) para fijar la cobertura real.
- [P] Leer completos los papers de §3.a y §3.h antes de adoptar features.
- [P] Revisar los ToS de cada API (uso comercial, atribución); este documento solo verificó acceso técnico.
- Pregunta: ¿el Universo A (Fase 1) emite al mismo chat público o a uno separado? Decide Dirección.

---

## 8. Innovación abierta (§6 de la directiva)

Propuestas, no implementadas. Las que tocan archivos canónicos o workflows requieren autorización.
Prioridad: P1 = próxima sesión · P2 = con la fase correspondiente · P3 = cuando haya espacio.

| # | Tipo | Propuesta | URL | Licencia / actividad [V] | Riesgos | Prioridad |
|---|---|---|---|---|---|---|
| I-1 | Métrica | **"Rug después del hit" en vivo**: en `monitor_shadow`, la fracción de primarias acertadas que luego caen ≤ −99%, por versión. Sería H-84 medido sobre v7.2.1 y permitiría actualizar la cifra de la ADVERTENCIA CRÍTICA con datos propios. | — (código propio) | sin dependencias | n chico al principio (usar Wilson IC90) | **P1** |
| I-2 | Bot / señal | **Enriquecimiento de riesgo en sombra**: GoPlus + RugCheck + Honeypot.is sobre candidatos ≥ 56, registrado aparte **sin tocar el score**, para testear si predicen el rug después del hit (anti-H-84). | api.gopluslabs.io · api.rugcheck.xyz · api.honeypot.is | APIs gratis sin key (200 medido); SDK `GoPlusSecurity/goplus-sdk-python` Apache-2.0, push 2026-08-21 (no hace falta) | límites (RugCheck 15, Honeypot 50); ToS [P]; escala de score de RugCheck sin documentar | **P1** |
| I-3 | Guardia de sombra | El health check debería marcar problema si aparece `telegram_sent: true` en una alerta posterior al cambio a SHADOW_MODE. Es el invariante "sombra = 0 envíos" vigilado cada 2 h. | — | sin dependencias | falso positivo si Dirección reactiva a propósito (leer el modo del workflow, como hace el resumen diario) | **P1** |
| I-4 | Refactor | `script_97`: descartar candidatos cuyo `scoring_version` no sea el vigente. Evidencia [V]: después del deploy de v7.2.1, el run de las 05:55 emitió en sombra 3 alertas puntuadas por v7.2 a las 05:13 (siguen "frescas" por R1 hasta 60 min). | — | toca archivo canónico → requiere autorización | ninguno relevante (hoy en sombra) | P2 |
| I-5 | Bot | **Sonda de deriva de fuentes** semanal en Actions: `probe_grupos_activos.py --no-burst` detecta 401/402/404 nuevos (DefiLlama ya movió 2 endpoints a pago) y bloqueos por IP de EE.UU. | — | workflow nuevo → consultar | ruido si un proveedor tiene un mal día (alertar solo si falla 2 semanas seguidas) | P2 |
| I-6 | Modelo (Universo A) | GARCH/EGARCH/HAR-RV con `arch`. Paper: *Loss Choice or Model Choice?* (2609.27024): calibrar el nivel del pronóstico, no solo elegir modelo. | https://github.com/bashtage/arch | NCSA (permisiva), push 2026-09-27, ★1581; deps BSD | peso de numpy/scipy/statsmodels en Actions (tiempo de instalación) | P2 (Fase 1) |
| I-7 | Métrica (Universo A) | Intervalos **conformales** para vol/retornos: cobertura garantizada sin supuestos de distribución. Paper: *Retrieval-Corrected Conformal Prediction for Time Series* (2608.10553). | https://github.com/scikit-learn-contrib/MAPIE · https://github.com/henrikbostrom/crepes | MAPIE BSD-3, push 2026-09-25, ★1596 · crepes BSD-3, push 2026-07-08, ★584 | MAPIE arrastra scikit-learn; crepes es más liviano | P2 (Fase 1) |
| I-8 | Papers memes | Leer y extraer features compatibles con datos gratis: 2608.20271 (predicción temprana de fraude en Solana), 2603.24625 (rugs en Solana), 2607.02795 (cohortes de snipers en pump.fun), 2511.15463 (rug fragmentado: explica caídas −99% en varias ventas), 2609.10246 (fábricas de memecoins). | alphaxiv.org/abs/<id> | papers (lectura) | no leídos completos todavía [P]; riesgo de features que exigen datos de pago | P2 |
| I-9 | Dataset | MELT (trazas de lanzamientos de alto riesgo) como referencia de etiquetas. | https://github.com/git-disl/MELT | **CC BY-NC 4.0** (no comercial → no cumple el criterio de licencia permisiva), push 2026-05-21 | **no integrar datos**; solo leer la metodología | P3 |
| I-10 | Métrica de calidad | Brier score + diagrama de confiabilidad de `emission_calibration.json` cuando pase a `validated: true` (las probabilidades del mensaje tienen que estar calibradas, no solo ordenadas). | — | sin dependencias | ninguno | P3 |
| I-11 | Refactor | Unificar el parseo de timestamps duplicado (`bot_health_check.parse_ts`, `bot_daily_summary.ts`) en `lib_ops`. | — | — | ninguno | P3 |
| I-12 | MCP (opcional) | MCP oficial de CoinGecko para consultas manuales de investigación (no para el pipeline). | https://github.com/coingecko/coingecko-typescript (paquete `@coingecko/coingecko-mcp` 8.2.0) | Apache-2.0, push 2026-09-28, organización oficial | el MCP remoto puede pedir key para ciertos endpoints [I] | P3 |
