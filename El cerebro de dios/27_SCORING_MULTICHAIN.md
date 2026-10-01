---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: IMPLEMENTADO (Fase 7) — lib_scoring_multichain + emisión en script_97; heurísticas no calibradas
last_updated: 2026-10-01
version: 0.2
---

# 27 — Scoring por tipo de activo (multi-chain, grupos a–h)

Rótulos: [V] verificado (archivo del repo, cálculo reproducido o evidencia de un doc anterior con su rótulo) · [I] inferido · [H] hipótesis · [P] pendiente.
**Todas las fórmulas de este documento son heurísticas y no están calibradas.** Los pesos, escalas y umbrales son puntos de partida: se ajustan con la medición de cada grupo (§5.5).

---

## 1. Propósito

El scorer v7.2.1 (`script_82`) está hecho para memecoins de Solana recién lanzadas: edad del par, liquidez, m5/h1, buy pressure. Aplicado a otro tipo de activo, mide otra cosa.

**Caso real [V]: arc (AI Rig Complex), alerta del 01/10 08:40 UTC.**
- Par creado hace 621,7 días, mcap $71,7 M, liquidez $10,3 M, categorías de CoinGecko "AI Agents" e "Infrastructure".
- Puntuó **72** con las reglas de memecoin.
- **De dónde salieron los puntos:** +25 por "buy pressure > 60%" con **5 compras y 0 ventas** en 5 minutos, y +15 por "volumen m5/h1 > 0,25" con **$64 de volumen m5** en un pool de $10,3 M.
- **Lo que pesa ese volumen:** una rotación m5/L de **6,2·10⁻⁶** (§6.1).

Este documento define, para cada grupo del doc 23:
1. cómo se **clasifica** un activo (§2);
2. qué **evento** se mide y con qué **modelos** (§3);
3. una **fórmula de score** con la misma estructura en todos los grupos (§4);
4. cómo se **integra** al pipeline sin tocar la ruta Solana (§5);
5. un **ejemplo trabajado** por tipo (§6).

El proyecto informa y el usuario decide. Toda alerta de cualquier grupo lleva primero el bloque 🛒 de adquisición de su chain (doc 24, regla núcleo).

---

## 2. Categorización de activos por grupo (a–h)

### 2.1 Grupos

| Grupo | Tipo | Ejemplos | Universo (doc 22) |
|---|---|---|---|
| a | Memecoins micro-cap | pump.fun, memes de Base/Monad | C |
| b | Preventa / pre-mercado | TGE próximos, perps pre-lanzamiento, pre-IPO | — |
| c | Gobernanza DeFi | tokens de DEX, lending, protocolos < 90 días | B |
| d | Sintéticos / derivados | perps descentralizados, emisores de sintéticos, stables algorítmicas | — |
| e | DePIN | redes de cómputo, sensores, almacenamiento | — |
| f | L1/L2 emergentes | Base, Arbitrum, Optimism, Blast, Monad (y su token nativo) | B/C |
| g | RWA | plataformas de activos tokenizados (gobernanza), no los activos estables | — |
| h | Blue chips | BTC, ETH, SOL | A |
| i | Establecidos sin grupo | par > 180 días fuera de a–h (arc) | — (solo registro) |

### 2.2 Reglas de clasificación (en orden; gana la primera que aplica)

| # | Regla | Grupo | Fuente |
|---|---|---|---|
| 1 | id de CoinGecko ∈ {bitcoin, ethereum, solana} | h | lista fija |
| 2 | Activo sin listar todavía: TGE en calendario, perp pre-lanzamiento, mercado `pre_ipo` | b | `script_99` (TGEs), Hyperliquid, Aevo [V doc 23] |
| 3 | Stablecoin con `pegMechanism` algorítmico, o categoría CoinGecko `synthetic-issuer` / `decentralized-perpetuals` | d | DefiLlama stablecoins, CoinGecko [V doc 23] |
| 4 | Categoría CoinGecko `real-world-assets-rwa`, o DefiLlama categoría `RWA` | g | ídem |
| 5 | Categoría CoinGecko `depin`, o DefiLlama categoría `DePIN` | e | ídem |
| 6 | Categoría CoinGecko `layer-1` / `layer-2`, o token nativo de una chain de `script_114` | f | ídem + `CHAINS` de T2 |
| 7 | Categoría CoinGecko `governance`, o protocolo DefiLlama con `gecko_id` (DEX, lending, yield) | c | ídem |
| 8 | **Memecoin nueva:** lanzada en un launchpad (pump.fun) **y** par < 7 días, **o** categoría CoinGecko `meme-token` con mcap < $50 M | a | detector + DexScreener `pairCreatedAt` |
| 9 | Ninguna de las anteriores y **par creado hace > 180 días** | **i (establecido sin grupo)** | DexScreener `pairCreatedAt` |
| 10 | Resto | a | por defecto, como hoy |

- **El grupo i es nuevo** (Dirección, Fase 6). Cubre activos maduros que no encajan en a–h (arc: "AI Agents", "Infrastructure"). Scoring propio en §4.10; **se registra y no se emite** hasta definir el scoring completo.
- Un activo de 7 a 180 días que no encaja en a–h cae en la regla 10 (grupo a, como hoy).
- **El origen pump.fun no alcanza para clasificar como memecoin** [V con arc]: arc nació en pump.fun y migró a meteora, pero hoy es un activo de 21 meses con $10 M de liquidez.
- El grupo y la regla que lo asignó se guardan en el registro (`group`, `group_rule`) y en el dossier (🧬 Naturaleza).

---

## 3. Modelos por tipo (con justificación técnica)

### 3.1 Tabla resumen

| Tipo | Grupo | Evento a medir (métrica dual adaptada) [H] | Modelos aplicables | Por qué |
|---|---|---|---|---|
| Blue chips (BTC/ETH/SOL) | h | **Primaria:** tocar +2σ₄₈ antes de −2σ₄₈ (σ₄₈ del pronóstico GARCH). **Secundaria:** cierre a 48 h ≥ +1σ₄₈. Se informa además el +20% absoluto (raro) | **GARCH(1,1)/EGARCH, HAR-RV, ATR, Bollinger**, funding, opciones (DVOL) | Historia diaria desde 2017 [V doc 23]; volatilidad con clustering y asimetría: el caso de uso de GARCH. Hay derivados líquidos (funding, vol implícita) |
| L1/L2 emergentes | f | +20% antes de −15% en 48 h, absoluto y relativo a ETH (EVM) o SOL | Momentum de TVL (crecimiento log y aceleración), volumen DEX/TVL, fees/TVL, momentum relativo del token nativo; staking flows [P] | El valor de una chain se ve en su uso (TVL, volumen, fees) antes que en el precio [H]. GARCH solo con ≥ 365 velas diarias (Monad: 320 días [V doc 23]) |
| Gobernanza DeFi | c | +20% antes de −15% en 48 h; ventana alrededor del cierre de propuestas | Actividad de gobernanza (Snapshot), TVL, fees, mcap/TVL, dilución (FDV/mcap como proxy de unlocks) | Los eventos de gobernanza (fee switch, cambio de emisiones) son discretos y fechados: event study. Unlocks de DefiLlama de pago (402) [V doc 23] → proxy FDV/mcap |
| DePIN | e | +20% antes de −15% en 48 h | Ingresos de red (fees DefiLlama), divergencia precio vs ingresos, tokenomics (FDV/mcap), momentum de categoría | El token es una apuesta a la demanda del servicio. Cantidad de nodos sin API pública (DePINscan 404 ×4 [V doc 23]) → n/d |
| RWA | g | +20% antes de −15% en 48 h, **solo** tokens con vol realizada diaria ≥ 2% | TVL colateral, TVL vs mcap, yield (fees/TVL), categoría | Los activos tokenizados (T-bills) tienen vol ~0: no hay evento que medir; se miden los tokens de las plataformas |
| Memecoins | a | +20% antes de −30% en 48 h (doc 19 §4.2), sin cambios | **Scoring v7.2.1, sin GARCH/ATR/Bollinger** (prohibido) | Sin historia, regímenes que se rompen, 84% de rug después del +20% [V doc 21]: los modelos de volatilidad no aplican |
| Sintéticos | d | Perps: +20% antes de −15%. Stables algorítmicas: evento propio de repeg (§4.7) | Funding, open interest, basis (mark − oráculo), momentum | El precio de un perp lo mueve el posicionamiento: funding y OI miden cuán cargado está un lado |
| Preventa | b | Precio al listar ≥ +20% sobre la referencia previa (pre-mercado o precio de la preventa) | Calendario + narrativa (`lib_narrative`, `script_115`) + señales on-chain del listing | No hay precio previo líquido: lo único medible es el calendario, la atención y las primeras horas del pool |

### 3.2 Notas por modelo

- **GARCH(1,1):** σ²ₜ₊₁ = ω + α·rₜ² + β·σ²ₜ, con ω = σ²_L·(1 − α − β) (variance targeting).
  - Ajuste por máxima verosimilitud sobre retornos log diarios; HAR-RV como alternativa con vol realizada intradía (velas de 4 h).
  - **Librería:** dos opciones. (1) `arch` 8.0.0: NCSA, push 2026-09-27, dependencias BSD [V doc 23]; se instala con pin y hashes. (2) GARCH(1,1) en Python puro con variance targeting y búsqueda en grilla de (α, β): sin dependencias nuevas.
  - **Recomendación:** (2) para arrancar; (1) cuando haga falta EGARCH o HAR.
- **ATR(14) y Bollinger (20, 2σ):** filtros de régimen para h, sobre velas diarias de Binance `data-api` [V doc 23]. El ancho de banda BW = (sup − inf)/media; su percentil sobre 1 año mide la compresión ("squeeze").
- **DVOL − vol realizada:** prima de vol implícita (Deribit DVOL [V doc 23]). Mide energía esperada, no dirección.
- **Momentum de TVL:** crecimiento log g₇ = ln(TVLₜ/TVLₜ₋₇) y aceleración a₇ = g₇ − ln(TVLₜ₋₇/TVLₜ₋₁₄). Implementado en `script_114.tvl_metrics` (T2).
- **Funding:** se usa como contrarian **solo en extremos** (percentil ≥ 95 o ≤ 5 de su propia historia). En el medio no dice nada [H].
- **Event study** (c, b): ventanas fijas alrededor del evento fechado, con placebo (días a más de 7 días de cualquier evento) y walk-forward con purga de 48 h, como `lib_narrative` (doc 18).

---

## 4. Fórmulas propuestas (heurísticas, no calibradas)

### 4.1 Estructura común

Cada componente i se transforma en una señal **sᵢ ∈ [−1, +1]**:
- +1 favorece el evento;
- −1 lo desfavorece;
- 0 es neutro.

Cada componente tiene un peso **wᵢ**, y los pesos del grupo suman 100.

```
A          = componentes con dato (las n/d no cuentan)
cobertura  = Σ_{i∈A} wᵢ / 100
D          = Σ_{i∈A} wᵢ·sᵢ / Σ_{i∈A} wᵢ                    ∈ [−1, +1]
score      = clip(50 + 50·D·M, 0, 100)                     M = multiplicador de energía (solo h; 1 en el resto)
```

- **50 es neutro.** Un score alto dice que las componentes con dato apuntan al evento del grupo.
- **Cobertura mínima 0,6** [H]: con menos, el registro dice "cobertura insuficiente" y no se emite. Una componente n/d **no se rellena** (doc 24: nunca valores por defecto).
- **Escalas de saturación:** las transformaciones usan `clip(x / escala, −1, 1)`. La escala es el valor que se considera "máximo informativo" [H].
- **Equivalente para `lib_fusion`** (preferido a largo plazo, como en el doc 26 §5): LLRᵢ = cᵢ·sᵢ nats, con cᵢ estimado en sombra (ln P(sᵢ | acierto)/P(sᵢ | fallo)), recortado a ±2.

Cada grupo tiene su `scoring_version` (`mc-<grupo>-0.1`), su umbral y su baseline (§5.5).

### 4.2 h — Blue chips

**Dirección (D)**

| Componente | Señal sᵢ | wᵢ | Fuente |
|---|---|---|---|
| Retorno estandarizado | z = r₂₄ₕ / σ_GARCH → `clip(z/2, −1, 1)` | 30 | Binance `data-api` klines diarias [V doc 23] |
| Ruptura de Bollinger con squeeze | percentil de BW ≤ 20% y cierre > banda sup → +1; < banda inf → −1; si no, 0 | 20 | ídem |
| Funding (contrarian en extremos) | percentil ≥ 95 → −1 · ≤ 5 → +1 · resto 0 | 20 | Binance `fapi` (puede dar 451 desde EE.UU. [I]) → fallback Hyperliquid / dYdX [V doc 23] |
| Fear & Greed (contrarian en extremos) | ≤ 20 → +1 · ≥ 80 → −1 · resto 0 | 15 | alternative.me, desde 2018 [V doc 23] |
| Tendencia | precio vs media de 20 días ± 1 ATR(14): arriba → +1, abajo → −1, dentro → 0 | 15 | Binance klines |

**Energía (M)**, sin dirección [H]:
```
M = clip(1 + (DVOL − RV₃₀)/40, 0,5, 1,5)        DVOL y RV₃₀ en puntos de vol anualizada
```
- **Por qué multiplica y no suma:** la vol implícita no dice hacia dónde, dice cuánto. Una prima alta amplifica la dirección que marcan las otras componentes.

**Evento y umbral [H]:**
- σ₄₈ = σ_GARCH·√2.
- Primaria: tocar +2σ₄₈ antes de −2σ₄₈.
- Umbral inicial de emisión: 65.

### 4.3 f — L1/L2 emergentes

| Componente | Señal sᵢ | wᵢ | Fuente (T2) |
|---|---|---|---|
| Momentum de TVL | `clip(g₇ / 0,10, −1, 1)` | 25 | `<chain>.json → tvl.log_growth_7d` |
| Aceleración de TVL | `clip(a₇ / 0,05, −1, 1)` | 15 | `tvl.accel_7d` |
| Actividad (volumen DEX / TVL, 24 h) | `2·pct − 1`, percentil en su propia historia (`_history.jsonl`); hasta tener 30 días, ranking entre las 8 chains | 20 | `dex_volume.total24h / tvl` |
| Uso pagado (fees/TVL anualizado) | ídem | 15 | `derived.fees_tvl_annualized_pct` |
| Momentum relativo del token nativo | r_rel = Δ7d(token) − Δ7d(ETH o SOL) → `clip(r_rel / 20, −1, 1)` | 25 | `native_token.change_7d` (Base: sin token → n/d) |

- Staking flows [P]: sin fuente gratuita verificada.
- Umbral inicial: 65.

### 4.4 c — Gobernanza DeFi

| Componente | Señal sᵢ | wᵢ | Fuente |
|---|---|---|---|
| Crecimiento de fees | ρ = (fees₇d·30/7)/fees₃₀d → `clip(ln ρ / 0,5, −1, 1)` | 25 | DefiLlama fees por protocolo [V doc 23] |
| Valuación vs TVL | `clip(−ln(mcap/TVL) / ln 4, −1, 1)` (mcap/TVL = 0,25 → +1; 1 → 0; 4 → −1) | 20 | CoinGecko + DefiLlama `/protocols` |
| Evento de gobernanza | propuesta de Snapshot que cierra en ≤ 48 h con fee switch / emisiones / buyback → +1; si no, 0 | 20 | Snapshot GraphQL, 100 req/60 s [V doc 23] |
| Dilución (proxy de unlocks) | `−clip(ln(FDV/mcap) / ln 3, 0, 1)` (FDV/mcap ≥ 3 → −1) | 15 | CoinGecko `fully_diluted_valuation` / `market_cap` |
| Momentum vs categoría | `clip((Δ7d − mediana₇d de governance) / 20, −1, 1)` | 20 | `_categories.json → governance.sample` |

- **Unlocks:** sin fuente gratuita (DefiLlama emissions 402 [V doc 23]); el proxy es la dilución FDV/mcap.
- Protocolo < 90 días (`listedAt`): se informa como dato, no puntúa [H a medir].
- Umbral inicial: 65.

### 4.5 e — DePIN

| Componente | Señal sᵢ | wᵢ | Fuente |
|---|---|---|---|
| Crecimiento de ingresos de red | `clip(ln ρ / 0,5, −1, 1)` con ρ de fees, como en c | 30 | DefiLlama fees (solo 9 protocolos DePIN [V doc 23]) |
| Divergencia ingresos vs precio (30 d) | `clip((ln F₃₀ − ln P₃₀) / 0,5, −1, 1)`: ingresos que crecen más que el precio → + | 20 | ídem + CoinGecko |
| Tokenomics (dilución) | igual que c | 20 | CoinGecko |
| Momentum de categoría | Δmcap 24 h de `depin` − Δ del mercado total → `clip(Δ/5, −1, 1)` | 15 | `_categories.json` |
| Momentum vs categoría | igual que c, con la mediana de `depin` | 15 | ídem |

- Nodos activos: n/d, porque DePINscan no tiene API pública [V doc 23].
- Fuera de los 9 protocolos de DefiLlama, la cobertura máxima es 50 (sin las dos primeras componentes) y no llega a 0,6: no se emite hasta tener una fuente de ingresos.
- Umbral inicial: 65.

### 4.6 g — RWA

**Filtro previo:** vol realizada diaria < 2% (T-bills, oro tokenizado) → "RWA estable", sin score.

| Componente | Señal sᵢ | wᵢ | Fuente |
|---|---|---|---|
| Crecimiento del TVL de la plataforma | `clip(g₇ / 0,10, −1, 1)` | 30 | DefiLlama, categoría RWA (181 protocolos [V doc 23]) |
| TVL vs mcap | `clip((g₇,TVL − g₇,mcap) / 0,10, −1, 1)` | 25 | ídem + CoinGecko |
| Yield (fees/TVL) | `2·pct − 1` en la categoría | 15 | DefiLlama fees |
| Momentum de categoría | como e, con `real-world-assets-rwa` | 15 | `_categories.json` |
| Momentum vs categoría | como c | 15 | ídem |

- Umbral inicial: 65.

### 4.7 d — Sintéticos y derivados

**d1 — Perps y tokens de protocolos de derivados**

| Componente | Señal sᵢ | wᵢ | Fuente |
|---|---|---|---|
| Funding (contrarian en extremos) | igual que h | 25 | Hyperliquid `metaAndAssetCtxs`, dYdX v4 [V doc 23] |
| OI que confirma | `clip(ln(OIₜ/OIₜ₋₂₄ₕ) / 0,5, −1, 1)·sign(Δp₂₄ₕ)`: OI creciente con precio subiendo → + | 25 | ídem |
| Basis (mark − oráculo)/oráculo | `clip(basis / 1%, −1, 1)` [H: el signo, demanda o sobrecarga, se mide] | 20 | ídem |
| Momentum | `clip(Δ24h / 20, −1, 1)` | 30 | ídem |

**d2 — Stablecoins algorítmicas (evento propio)**
- **Evento de repeg** [H]: desde un depeg (|p − 1| ≥ 5%), volver a |p − 1| ≤ 1% en 7 días. Desde 0,80, el repeg es +25%: cumple el evento del proyecto.
- **Hazard de espiral:**
  ```
  h = clip(|p − 1|/0,10, 0, 1)·0,5 + clip(−Δcirc₇d/0,20, 0, 1)·0,5
  ```
  Δcirc₇d es la caída semanal del circulante. Se informa como dato, no como score de compra.
- Fuente: DefiLlama stablecoins, 27 algorítmicas [V doc 23]. Hay que normalizar el typo `crytpo-backed` [V doc 23].
- Umbral inicial d1: 65.

### 4.8 b — Preventa / pre-mercado

| Componente | Señal sᵢ | wᵢ | Fuente |
|---|---|---|---|
| Calendario | días al listing ∈ [−14, −1] → +1 (ventana de anticipación, doc 18 H3); listing pasado hace ≤ 2 días → 0,5; resto 0 | 25 | `script_99` (TGEs), Hyperliquid, Aevo |
| Narrativa | `clip(ln(intensity) / ln 10, 0, 1)` si `signal` del doc 26 (p ≤ 0,01); si no, 0 | 25 | `script_115` → `narrative/<mint>.json`; `lib_narrative` para el tema |
| Prima de pre-mercado | `clip(premium / 20%, −1, 1)` sobre la referencia (preventa o pre-market) | 25 | Hyperliquid pre-launch perps; **preventa cripto sin fuente gratuita [V doc 23]** |
| On-chain del listing | liquidez y volumen de la 1.ª hora vs mediana de listings recientes de la misma chain → `2·pct − 1` | 25 | GeckoTerminal `new_pools` (T2: `new_pools.per_hour_est` y página 1) |

- Hasta tener fuente de precio previo, la prima es n/d: la cobertura máxima es 75.
- Umbral inicial: 70.

### 4.9 a — Memecoins

**Scoring v7.2.1 sin cambios** (`script_82`, doc 24 Anexo C). Sin GARCH, ATR ni Bollinger. Propuestas para un v7.3, a medir en sombra antes de cambiar nada [H]:

1. **Rotación mínima para los bonos de aceleración:** vol_h1 / L ≥ 0,1%. En arc fue 0,002% [V] (§6.1).
2. **Buy pressure con cota de Wilson:** el bono > 60% se evalúa sobre la cota inferior del IC90 de compras/(compras + ventas), con n ≥ 10 trades. Con 5/5 la cota es 64,9% [V cálculo]: pasa el umbral, pero con n < 10 no se evalúa.
3. **Repetición mediática** (doc 26 Fase 1): entra como LLR en `lib_fusion` cuando el event study dé efecto con IC90.
4. **Clasificación previa (§2.2):** un activo que no es del grupo a no se puntúa con v7.2.1.
5. **Deudas del doc 22 §7:** el tramo −35 inalcanzable y `bp_delta` inactivo.

---

### 4.10 i — Establecidos sin grupo (Dirección, Fase 6)

**Definición:** par creado hace **> 180 días** que no clasifica en a–h (§2.2, regla 9).
**Estado: se registra, no se emite** hasta definir el scoring completo. Va a `multichain/_accumulated.json` con `status: "registro"`; `script_97` lo ignora.

**Qué no se usa:** ningún bono de memecoin de v7.2.1: edge temprano, buy pressure m5, momentum m5/h1, volumen m5 ni aceleración m5/h1. En un pool maduro y profundo, esas ventanas de 5 minutos miden ruido (caso arc, §6.1).

**Componentes** (estructura de §4.1):

| Componente | Señal sᵢ | wᵢ | Fuente |
|---|---|---|---|
| TVL del protocolo | `clip(g₇ / 0,10, −1, 1)` | 25 | DefiLlama `/protocols` por `gecko_id` (n/d si no es un protocolo) |
| Holders | crecimiento 7d: `clip(ln(Hₜ/Hₜ₋₇) / 0,10, −1, 1)` | 25 | RugCheck `totalHolders` / GoPlus `holder_count`, guardados a diario [P: hoy solo hay foto puntual] |
| Fees | ρ = (fees₇d·30/7)/fees₃₀d → `clip(ln ρ / 0,5, −1, 1)` | 20 | DefiLlama fees por protocolo |
| Volumen sostenido: rotación | `clip(log₁₀((vol₂₄ₕ/L) / 0,05), −1, 1)` (5% diario = neutro) | 20 | DexScreener `volume24h`, `liquidityUsd` |
| Volumen sostenido: persistencia | `clip(ln(vol₂₄ₕ / (vol₇d/7)) / ln 3, −1, 1)` | 10 | DexScreener / GeckoTerminal OHLCV diario |

```
score_i = clip(50 + 50·D, 0, 100) − 10·[edad del par > 365 días]      (cobertura mínima 0,6, como en §4.1)
```

- **Descuento por edad** (Dirección): −10 si el par tiene más de 1 año.

**arc con estas reglas** (datos de la alerta del 01/10 [V]; fórmula [H]):
- **Rotación:** vol₂₄ₕ/L = 6.955/10.333.552 = 6,7·10⁻⁴ → log₁₀(6,7·10⁻⁴/0,05) = −1,87 → s = **−1** (w 20).
- **Resto de componentes:** TVL, holders con historia, fees y persistencia → n/d.
- **Resultado:** cobertura 0,20 < 0,6, así que el score queda parcial: 50 + 50·(−1) = 0, y el descuento por edad (621,7 días) no lo baja de 0. Contra los 72 de v7.2.1, la lectura cambia de "aceleración" a "pool profundo con muy poca rotación".

**Pendiente para emitir [P]:**
1. Holders guardados a diario por token.
2. Mapeo `gecko_id` → protocolo de DefiLlama.
3. Medición en sombra con el evento de f (+20% antes de −15% en 48 h).
4. Decisión de Dirección.
## 5. Cómo integrar al pipeline multi-chain (diseño)

### 5.1 Flujo

```
multichain_scanner.yml (1 h)           narrative_collector.yml (20 min)        [P] universo_a.yml (diario + 4 h)
  script_114 v0.2 (T2)                    script_115 (T1)                          klines Binance, DVOL, funding, F&G
  → multichain/<chain>.json               → narrative/<mint>.json                  → universo_a/*.json
  → multichain/_categories.json
  → multichain/_history.jsonl
            │                                     │                                         │
            └──────────────────────┬──────────────┴─────────────────────────────────────────┘
                                   ▼
            [P] script_116_multichain_score.py  (clasifica §2.2 → puntúa §4 → registra)
                → multichain/_accumulated.json   {key, chain, group, group_rule, scoring_version "mc-<g>-0.1",
                                                  components [{name, s, w, value, source}], coverage, score, detected_at}
                                   │
                                   ▼
            script_97 (sin cambios en la ruta Solana) lee DOS fuentes: shadow_v4/_accumulated.json + multichain/_accumulated.json
                umbral y frescura POR GRUPO · dedup por chain:address · guía de compra por chain (regla núcleo)
                                   │
                                   ▼
            script_113: mismo dossier (🛒 primero) + sección "Modelo del grupo" con la tabla de componentes
```

### 5.2 Qué falta para cada grupo

| Grupo | Ya está (T2, T1) | Falta [P] |
|---|---|---|
| h | precio y cambios (CoinGecko), TVL/DEX/fees de su chain | klines diarias y de 4 h (Binance `data-api`), DVOL (Deribit), funding con fallback, Fear & Greed; GARCH en Python puro o `arch` con pin |
| f | TVL, aceleración, volumen DEX, fees, token nativo, pools nuevos | percentiles con 30 días de `_history.jsonl`; benchmark ETH/SOL Δ7d (ya en el grupo h) |
| c | categoría `governance` (muestra top-25) | DefiLlama `/protocols` (`listedAt`, TVL por protocolo, `gecko_id`), fees por protocolo, Snapshot |
| e | categoría `depin` | fees de los 9 protocolos DePIN de DefiLlama, mapeados a `gecko_id` |
| g | categoría `real-world-assets-rwa` | TVL por protocolo RWA, vol realizada para el filtro |
| d | categorías de perps y sintéticos | Hyperliquid `metaAndAssetCtxs`, dYdX v4, DefiLlama stablecoins |
| b | `script_99` (TGEs), `script_115` (narrativa), `new_pools` | perps pre-lanzamiento de Hyperliquid; fuente de precio de preventa (no existe gratuita) |
| a | todo (producción) | — |
| i | DexScreener (rotación) | holders diarios, mapeo a DefiLlama; solo registro |

### 5.3 Guía de compra por chain (regla núcleo, doc 24 §6.2)

- Guías completas en `script_97` (`guide_for`): Solana, Ethereum, Base y, desde la Fase 6, **Arbitrum, Optimism y Blast** [V tests]. **Monad** tiene wallet pero todavía no DEX: su guía está incompleta y sus activos **no se emiten** hasta agregarlo.
- Para h, y para c, e, f y g cuando el activo cotiza en un exchange centralizado: ruta CEX confirmada por contrato (`script_113.cex_route`, doc 24 §8), sin códigos de referido.

### 5.4 Convivencia

- **`script_82` no cambia.** La ruta Solana sigue siendo la rápida (20 min). La multi-chain corre cada 1 h.
- **Acumulados separados:** sin escrituras cruzadas ni conflictos de rebase.
- **Presupuesto [I]:** el scanner hace ~45 llamadas por corrida (CoinGecko ~10 a 15 s, GeckoTerminal 14 a 6,5 s, DefiLlama ~25 a 1 s).
  - El scoring no suma llamadas: lee archivos.
  - Los colectores nuevos (Universo A, protocolos, perps) van en workflows propios, como T1 y T2.

### 5.5 Medición por grupo

- Cada grupo arranca **en sombra** para tener su primera medición.
  - Se mide con su evento (§3.1), con la métrica dual adaptada, IC90 de Wilson y baseline propio (tasa del evento en todo el universo del grupo, no solo en los alertados).
  - `monitor_shadow.py` suma la dimensión `group`.
- **La salida a emisión de cada grupo la decide Dirección.** No exige n ≥ 20 (corrección de Dirección del 01/10: el destino es el grupo privado); n ≥ 20 es el criterio para declarar calibrada la probabilidad que muestra el mensaje.
- **Calibración de pesos:** con ≥ 20 eventos resueltos por grupo, cada wᵢ se reemplaza por su LLR estimado (§4.1). Walk-forward semanal con purga de 48 h y placebo.

---

## 6. Ejemplos trabajados por tipo

En cada ejemplo, las entradas llevan su rótulo. Los ejemplos **ilustrativos** usan números inventados para mostrar el cálculo: no son activos reales.

### 6.1 a — Memecoin (arc, real [V])

Entradas (alerta del 01/10 08:40 UTC, `alert_61V8vB…_2026-10-01_084036.json`, desglose del dossier `script_113`):

| Componente v7.2.1 | Observado | Puntos |
|---|---|---|
| Score del feed | WS 76 × 0,3 | +22,8 |
| MCap ≥ $1M | $71.693.009 | +25 |
| Volumen 24 h | $6.955 (< $50K) | 0 |
| Volumen m5/h1 > 0,25 | $64,45 / $206,73 = 0,31 | +15 |
| Buy pressure m5 > 60% | 5 compras, 0 ventas = 100% | +25 |
| Momentum m5 > 0 y h1 > 0 | +0,56% / +0,63% | +20 |
| Par > 24 h | 621,7 días | −50 |
| Liquidez ≥ $100K | $10.333.552 | +15 |
| **Total** | | **72** (= registrado) |

**Lectura con este documento:**
- **Clasificación (§2.2):** par de 621,7 días (> 180) con categorías "AI Agents" e "Infrastructure" → la regla 8 no aplica (no es nueva) → regla 9 → **grupo i**.
- **Rotación:** m5/L = 64,45 / 10.333.552 = **6,2·10⁻⁶**; h1/L = **2,0·10⁻⁵**; 24h/L = **6,7·10⁻⁴** [V cálculo].
- **Propuesta 4.9.1:** con un mínimo de rotación h1 de 10⁻³, los bonos de aceleración (+15, +25, +20) no aplican y el score v7.2.1 sería 72 − 60 = 12.
- **Propuesta 4.9.2:** con n = 5 trades (< 10), la buy pressure no se evalúa.
- **En el grupo i** (§4.10) se registra sin emitir. Con los datos de la alerta da cobertura 0,20 y score 0 (detalle en §4.10).

### 6.2 h — Blue chip (BTC, entradas reales del 17/09 [V]; parámetros GARCH ilustrativos)

Entradas: `01_Datos_Crudos/mercados/coingecko_2026-09-17_172455.json`. Precio $76.842, máximo 24 h $77.024, mínimo $75.161, cambio 24 h +1,58%.

1. **Vol de Parkinson del día** [V cálculo]: σ_P = ln(H/L)/√(4 ln 2) = ln(77.024/75.161)/1,6651 = **1,47% diario**.
2. **GARCH(1,1) ilustrativo:** α = 0,08, β = 0,90, vol de largo plazo σ_L = 2,5% diario, σₜ = 2,0%.
   - ω = σ_L²·(1 − α − β) = 1,25·10⁻⁵;
   - σ²ₜ₊₁ = ω + α·r² + β·σ²ₜ = 1,25·10⁻⁵ + 0,08·0,0158² + 0,90·0,02² → **σₜ₊₁ = 1,98%**;
   - σ₄₈ = 1,98%·√2 = **2,80%** → barreras de la primaria: **+5,60% / −5,60%** (±2σ₄₈).
3. **Componentes:**
   - z = 1,58/1,98 = 0,80 → s = 0,40 (w 30);
   - Bollinger, funding, Fear & Greed y tendencia: sin datos en el archivo → n/d (w 70).
4. **Cobertura** = 30/100 = **0,30 < 0,6 → no se emite.** El score parcial sería 50 + 50·0,40 = 70 con M = 1. El ejemplo muestra por qué la regla de cobertura existe: una sola componente no alcanza.

### 6.3 f — L1/L2 (Solana como chain, entradas reales del 28/09 [V])

Entradas: `02_Analisis/macro/_macro_signals.json` (DefiLlama vía `script_110`). TVL US$ 6.576 millones (6.576.390.742), cambio 7d +5,97%, cambio 30d +11,8%, volumen DEX 24 h US$ 1.926 millones.

- g₇ = ln(1,0597) = 0,0580 → s = **0,58** (w 25).
- a₇ aproximada: el archivo no trae TVL de hace 14 días, así que la semana previa se aproxima con el promedio semanal de 30 días: ln(1,118)·7/30 = 0,0260 → a₇ ≈ 0,0580 − 0,0260 = 0,0320 → s = **0,64** (w 15).
- Volumen DEX/TVL 24 h = 1.926/6.576 = **0,293** [V cálculo]. Percentil: n/d (sin historia propia todavía; T2 la empieza a juntar).
- Fees/TVL y momentum relativo de SOL: n/d en el archivo.
- D = (25·0,58 + 15·0,64)/40 = 0,6025 → score parcial **80,1**, pero **cobertura 0,40 < 0,6 → no se emite**.
- **Con T2 en vivo**, la ficha `solana.json` trae fees y token nativo, y la cobertura sube a 0,8. La percentil de actividad llega a los 30 días de `_history.jsonl`.

### 6.4 c — Gobernanza DeFi (ilustrativo)

Protocolo listado hace 45 días. Fees 7d $210 K y 30d $600 K; mcap $40 M, TVL $80 M, FDV $120 M. Propuesta de fee switch que cierra en 30 h. Δ7d del token +12% contra una mediana de categoría de +2%.

| Componente | Cálculo | sᵢ | wᵢ | wᵢ·sᵢ |
|---|---|---|---|---|
| Fees | ρ = (210·30/7)/600 = 1,5 → ln 1,5/0,5 | 0,81 | 25 | 20,3 |
| Valuación | −ln(0,5)/ln 4 | 0,50 | 20 | 10,0 |
| Gobernanza | fee switch en ≤ 48 h | 1,00 | 20 | 20,0 |
| Dilución | FDV/mcap = 3 → −ln 3/ln 3 | −1,00 | 15 | −15,0 |
| Momentum vs categoría | (12 − 2)/20 | 0,50 | 20 | 10,0 |
| | | | **100** | **45,3** |

D = 0,453 → **score 72,6**, cobertura 1,0. Supera el umbral inicial de 65.

### 6.5 e — DePIN (ilustrativo)

Protocolo dentro de los 9 de DefiLlama. ρ de fees = 1,2; fees 30d +40% y precio 30d −5%; FDV/mcap 1,5; categoría `depin` +3,1% en 24 h contra +1,0% del mercado; Δ7d del token +4% contra una mediana de +6%.

| Componente | sᵢ | wᵢ | wᵢ·sᵢ |
|---|---|---|---|
| Ingresos | ln 1,2/0,5 = 0,36 | 30 | 10,9 |
| Divergencia | (ln 1,4 − ln 0,95)/0,5 = 0,77 | 20 | 15,5 |
| Dilución | −ln 1,5/ln 3 = −0,37 | 20 | −7,4 |
| Momentum de categoría | 2,1/5 = 0,42 | 15 | 6,3 |
| Momentum vs categoría | −2/20 = −0,10 | 15 | −1,5 |
| | | **100** | **23,9** |

D = 0,239 → **score 61,9**: por debajo del umbral de 65. Los ingresos crecen más rápido que el precio, pero la dilución y el momentum relativo restan.

### 6.6 g — RWA (ilustrativo)

- **Token de plataforma:** vol realizada 4% diario, así que pasa el filtro.
  - TVL de la plataforma +15% en 7d: g₇ = 0,140 → s = 1.
  - mcap +3% en 7d: (0,140 − 0,030)/0,10 → s = 1.
  - Percentil de yield 0,7 → s = 0,4; categoría plana → s = 0; Δ relativo +5 → s = 0,25.
  - D = (30 + 25 + 6 + 0 + 3,75)/100 = 0,6475 → **score 82,4**.
- **Token de T-bills tokenizados:** vol realizada 0,05% diario < 2% → "RWA estable", sin score. Se informa en el dossier como dato de la categoría.

### 6.7 d — Sintéticos (ilustrativo)

- **d1, perp en Hyperliquid:**
  - funding en el percentil 99 → s = −1 (w 25);
  - OI +35% en 24 h con el precio +8%: ln 1,35/0,5 = 0,60 (w 25);
  - basis +0,4% → 0,40 (w 20);
  - momentum +8%/20 = 0,40 (w 30).
  - D = (−25 + 15 + 8 + 12)/100 = 0,10 → **score 55**: el posicionamiento cargado (funding extremo) compensa el momentum.
- **d2, stable algorítmica:**
  - p = 0,94 y circulante −12% en la semana → h = 0,5·clip(0,06/0,10) + 0,5·clip(0,12/0,20) = 0,30 + 0,30 = **0,60** (dato de espiral).
  - El repeg a 1,00 sería +6,4%, por debajo del +20%: no cumple el evento del proyecto.

### 6.8 b — Preventa (ilustrativo)

Token con TGE en 6 días (ventana de anticipación) → s = 1 (w 25). Intensidad de menciones de 4,2 con `signal` (p ≤ 0,01): ln 4,2/ln 10 = 0,62 (w 25). Prima de pre-mercado y on-chain del listing: n/d.

- D = (25 + 15,6)/50 = 0,81 → score parcial 90,6.
- **Cobertura 0,50 < 0,6 → no se emite.** Queda en sombra y se reevalúa en el listing, cuando entra la componente on-chain y la cobertura sube a 0,75.

---

## 7. Pendientes

1. [P] `script_116_multichain_score.py` (clasificación §2.2 + fórmulas §4) en sombra, empezando por **h** y **f** (orden de Dirección).
2. [P] Colector del Universo A (doc 23 Fase 1): klines de Binance, DVOL, funding con fallback y Fear & Greed. Decidir GARCH en Python puro o `arch` con pin.
3. [P] Filas de guía de compra para Arbitrum, Optimism, Monad y Blast en `script_97` (regla núcleo).
4. [P] Verificar en vivo, desde Actions, las rutas de T2 que este diseño usa:
   - `overview/dexs` por chain: verificada para `solana` en producción por `script_110` [V];
   - `overview/fees` por chain: verificada para `Base` [V doc 23];
   - `coins/categories`: [I].
5. [P] v7.3 en sombra con las propuestas de §4.9 (rotación mínima, Wilson en buy pressure), comparado contra v7.2.1 con la métrica dual.
6. ~~Grupo x~~ → **grupo i** (Dirección, Fase 6): registrar sin emitir. [P] Fuentes de holders con historia (RugCheck / GoPlus diarios por token) y el `scoring_version` `mc-i-0.1` en `script_116`.

---

## 8. Implementación (Fase 7)

**Archivos**
- `lib_scoring_multichain.py`: clasificación §2.2 y un scorer por tipo, cada uno devuelve `(score, reasons, confidence)` con confidence = cobertura. Funciones puras y sin red.
- `script_114` v0.3 (mismo workflow horario): suma las velas diarias de Binance (400), Fear & Greed y el funding/OI de Hyperliquid para BTC/ETH/SOL, más `_protocols.json` con el TVL por protocolo de DefiLlama.
- `script_97`: bloque multi-chain después de la ruta Solana, que no cambia.

**Desvíos respecto de §4** [H]:
- **Umbral:** 56 en todos los grupos (directiva Fase 7) en lugar de 65/70.
- **h:** funding con umbral absoluto (≥ 30% anual → −1; ≤ −10% → +1) hasta tener historia; M = 1 porque DVOL no se colecta.
- **c:** el crecimiento del TVL del protocolo reemplaza al de fees (fees por protocolo sin colectar).
- **e:** la actividad del token (vol/mcap contra la mediana de la categoría) es un proxy de ingresos de red.
- **Bollinger:** squeeze y bandas sobre velas cerradas; el precio actual se compara contra esas bandas.

**Emisión:** score ≥ 56, cobertura ≥ 0,6 y grupo emisor (a, c, e, f, g, h); b, d e i solo se registran.
- **Topes:** 2 alertas por ciclo, 3 por grupo en 24 h, y el mismo activo de nuevo recién pasadas 48 h.
- **Compra:**
  - pools on-chain → guía de su chain;
  - blue chips → Binance, Coinbase y Kraken;
  - resto → exchanges que CoinGecko confirma para ese id (`coins/{id}/tickers`).

  Sin ruta confirmada, el activo no se emite.
- **Registro:** `02_Analisis/multichain/_scores.json` en cada ciclo.

**Primera corrida sobre datos reales** (scan de producción del 01/10 16:39 UTC, v0.2 todavía sin Universo A ni protocolos) [V]:

| Grupo | Activos | Con cobertura ≥ 0,6 | Emitibles |
|---|---|---|---|
| e DePIN | 24 | 24 | 12 (PHA 88, JASMY 88, TRAC 85…) |
| f L1/L2 | 44 | 4 (tokens nativos con ficha) | 1 (MON 64; ARB 46, OP 46, BLAST 27) |
| c gobernanza | 19 | 0 (falta `_protocols.json`, llega con v0.3) | 0 |
| g RWA | 25 (13 estables filtrados) | 0 (ídem) | 0 |
| h blue chips | 3 | 0 (falta el Universo A, llega con v0.3) | 0 |
| a memecoins multi-chain | 32 | 32 | 0 |
| i establecidos | 88 | 0 | registro |
| d sintéticos | 38 | 0 | registro |

### 8.1 Fase 8 — grupos c, d, g, b con datos propios (lib 0.2, scanner v0.4)

| Grupo | Fuente nueva (mismo workflow horario) | Componente que se completa | Estado |
|---|---|---|---|
| c | Snapshot GraphQL (`_governance.json`) + DefiLlama `overview/fees` cruzado con `/protocols` | evento de gobernanza (+1 si una propuesta de fees/emisiones/buyback cierra en ≤ 48 h) y crecimiento de fees ρ (el TVL queda como respaldo) | emite (cobertura hasta 1,0) |
| d | Hyperliquid, todos los perps (`_perps.json` con historial de OI de ~30 h) | funding (contrarian en extremos), OI 24 h × signo del precio, basis (mark − oráculo) | **emite** (sale de "solo registro") |
| g | DefiLlama fees + TVL | yield anualizado (5% = neutro) | emite |
| e | DefiLlama fees (9 protocolos DePIN) | crecimiento de ingresos de red (el proxy vol/mcap queda solo si no hay fees) | emite |
| b | Aevo pre-IPO / pre-lanzamiento (`_premarket.json`) + `script_99` | activos de pre-mercado | registro (sin ruta de compra antes del listing; `script_99` hoy vacío [V]) |
| h | trust loop CEX en `script_98` (`active_tracking_cex`) | seguimiento t+1h/6h/24h con precio de Binance → Coinbase → Kraken | emite (desde Fase 7) |
| i | `script_82.apply_group_i` en el flujo Solana | par > 180 días → grupo i (score §4.10), registro | registro (arc → 0) |

