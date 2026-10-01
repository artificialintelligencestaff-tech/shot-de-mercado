---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: DISEÑO + IMPLEMENTADO en script_113 v1.0 (sin enganchar al pipeline ni al envío)
last_updated: 2026-10-01
version: 1.2
---

# 24 — Dossier por activo (diseño) + integración multi-chain

Rótulos: [V] verificado (archivo del repo, cálculo reproducido o consulta HTTP en esta sesión) · [I] inferido · [H] hipótesis · [P] pendiente.

---

## 1. Propósito

Que cada alerta llegue con un documento que, **antes que nada, enseñe cómo adquirir el activo paso a paso**, y que además permita entender qué es, por qué el sistema lo detectó, con qué datos y cálculos, durante cuánto tiempo aplica la señal y cómo auditar cada número: **material educativo y documentación científica, no asesoría financiera.** El dossier informa; no juzga, no advierte, no recomienda. El lector decide.

**Regla núcleo (Dirección, 01/10):** la adquisición es el núcleo del producto y es lo primero que se ve, en el dossier y en la alerta. **Si el bloque de compra no está completo para la chain del activo, ni la alerta ni el dossier se emiten.**

**Formato de entrega**
- Archivo Markdown, uno por activo: `02_Analisis/dossiers/<chain>/<mint>.md`, más `<mint>.json` con el dict completo y sus datos de entrada (directiva Fase 3; reemplaza el nombre `dossier_<SYMBOL>_<mint8>_<ts>.md` de la v1.1). Lo genera `script_113` (§7).
- [P] Va adjunto con `sendDocument` al grupo (`TELEGRAM_PUBLIC_CHAT_ID`), con un caption de ≤ 1024 caracteres: nombre, chain, wallet + DEX, slippage sugerido y ventana. Sin implementar: requiere enganchar `script_113` a `script_97` (workflow de producción, consultar antes).
- Lo desconocido se escribe `n/d` con la fuente que lo resolvería. **Nunca** se rellena con valores por defecto.
- Cada dato lleva su **fuente** y su **momento**: "al detectar" (archivo de detección) o "consulta del <fecha>" (dato actual).

---

## 2. Estructura del dossier

Orden fijo: **presentación → 🛒 adquisición → todo lo demás.**

```
🎴 PRESENTACIÓN                 ← portada de 4-6 líneas
🛒 CÓMO ADQUIRIR ESTE ACTIVO    ← SIEMPRE PRIMERO (estudio de adquisición)
📊 IDENTIFICACIÓN DEL ACTIVO
🧬 NATURALEZA DEL ACTIVO
🔬 MÉTODO CIENTÍFICO
🎯 FUNDAMENTO DE LA DETECCIÓN
⏱️ VIGENCIA DE LA SEÑAL
📚 FUENTES Y TRAZABILIDAD
```

### 🎴 Presentación (portada)

Cuatro a seis líneas para ubicar al lector antes de la compra:
- nombre (symbol), chain y tipo de activo;
- precio, liquidez y market cap al detectar;
- qué lo disparó, en una línea (score + señal principal);
- ventana de la señal (< 48 h, con fecha y hora de vencimiento).

### 🛒 Sección 1 — Cómo adquirir este activo (estudio de adquisición)

No es una lista genérica: es el estudio de **cómo se compra este activo en particular**, con los datos de su par.

**1.1 Ruta por chain** (wallet → fondeo → DEX). Enlaces a los sitios oficiales [I: dominios oficiales, no verificados por HTTP en esta sesión].

| Chain | Wallet | DEX / agregador | Fondear con | Exchange centralizado |
|---|---|---|---|---|
| Solana | Phantom (https://phantom.app) · Solflare (https://solflare.com) | Jupiter (https://jup.ag, agregador) · Raydium (https://raydium.io) · Orca (https://www.orca.so) | SOL o USDC en Solana | para comprar SOL/USDC: Binance, Coinbase, Kraken |
| Ethereum | MetaMask (https://metamask.io) · Rabby (https://rabby.io) | Uniswap (https://app.uniswap.org) · 1inch (https://app.1inch.io) | ETH o USDC/USDT en Ethereum | ídem |
| Base | MetaMask · Coinbase Wallet (https://www.coinbase.com/wallet) | Aerodrome (https://aerodrome.finance) · Uniswap | ETH o USDC en la red Base | ídem |
| Blast, Monad y otras | wallet nativa de la red | **sin guía verificada** | — | — |

Si la chain no tiene guía verificada, la regla núcleo aplica: **no se emite** hasta agregar su fila.

Si el activo cotiza en un exchange centralizado (siempre en blue chips; en el resto se verifica con CoinGecko `coins/{id}/tickers` [P]), se agrega esa ruta: Binance, Coinbase o Kraken, comprando el par contra USDT/USD directamente.

**1.2 Estudio de liquidez del par** (dato propio, calculado al armar el dossier)

| Dato | Cómo se obtiene |
|---|---|
| Pool principal | DexScreener `dexId` + `pairAddress` (el de mayor liquidez, igual que `script_82`) |
| Liquidez del pool (L) | DexScreener `liquidityUsd` |
| Impacto estimado de una compra de Δ USD | pool de producto constante sin comisiones, con la mitad de L del lado cotizado: **impacto ≈ 2Δ / L** (prima del precio promedio de ejecución sobre el precio spot) [H: aproximación; un agregador como Jupiter puede repartir la orden y lograr menos impacto; no aplica a la bonding curve de pump.fun antes de migrar, donde DexScreener informa L = 0] |
| Slippage sugerido | por tramo de L (tabla de abajo) [H: a calibrar con datos de ejecución, que hoy no se registran] |

| Liquidez del par (L) | Slippage sugerido | Impacto de $1.000 con esa L |
|---|---|---|
| < $50.000 | 10% | > 4% |
| $50.000 – $250.000 | 5% | 0,8% – 4% |
| $250.000 – $1.000.000 | 3% | 0,2% – 0,8% |
| ≥ $1.000.000 | 1% | < 0,2% |
| desconocida (bonding curve, L = 0) | 5–10% (el monto exacto lo muestra el DEX) | n/d |

El dossier muestra el impacto estimado para **$100, $1.000 y $10.000**.

**1.3 Pasos exactos**
1. Instalar la wallet de la chain (enlace directo de la tabla 1.1).
2. Fondearla con el activo nativo (SOL / ETH) o con una stablecoin (USDC / USDT), comprados en un exchange y enviados a la dirección de la wallet. Dejar un resto del nativo para pagar las comisiones de red.
3. Conectar la wallet al DEX (enlace directo).
4. Pegar el mint / contrato y verificar que coincide **carácter por carácter** con el del dossier.
5. Configurar el slippage sugerido por el estudio de liquidez (1.2).
6. Verificar el contrato en el explorador (Solscan / Etherscan / BaseScan) y el par en DexScreener (enlaces de 1.4).
7. Ejecutar el swap.
8. Confirmar la transacción en el explorador. Si el token no aparece en la wallet, agregarlo pegando el mint / contrato.

**1.4 Verificación previa**
- Contrato en el explorador: enlace directo con el mint.
- Par en DexScreener: enlace directo con el `pairAddress`.
- Mint / freeze authority, holders y top-10: los datos de la Sección 2 (Identificación) en la misma línea, para comparar sin cambiar de pantalla.

**1.5 Enlaces de swap con el par precargado** [P]
- Propuesta: un enlace que abra el DEX con el par ya cargado (SOL → token), para no tener que pegar el mint.
- No se pudo verificar en esta sesión (cargar la página de swap quedó bloqueado por el clasificador del entorno).
- **Dirección verifica a mano el formato de cada DEX antes de usarlo.** Hasta entonces, solo enlaces a los sitios oficiales más el mint para pegar.

### 📊 Sección 2 — Identificación del activo

| Campo | Fuente (gratuita, sin key) | Estado hoy |
|---|---|---|
| Nombre, symbol, mint/contrato | `token` del detector (PumpPortal / trending) · DexScreener `baseToken` | [V] en el archivo de detección |
| Chain | pipeline (`solana`) · DexScreener `chainId` · `token.chain` (multi-chain) | [V] |
| DEX principal y par principal | DexScreener `dexId`, `pairAddress` | [V] |
| Deployer (wallet) | `token.traderPublicKey` (PumpPortal create) · RugCheck `creator` | [V] / [V] consulta |
| Fecha de creación del par, edad al detectar y actual | DexScreener `pairCreatedAt` (ms) vs `detected_at` | [V] (desde v7.2) |
| Mint / freeze authority | GoPlus Solana `mintable` / `freezable` · RugCheck `mintAuthority` / `freezeAuthority` · (EVM: GoPlus `is_mintable`, `owner_address`, Honeypot.is) | [P] consulta al armar el dossier |
| Holders y concentración top-10 | RugCheck `totalHolders`, suma de `topHolders[].pct` de los 10 primeros, `insider` | [P] ídem |
| Liquidez bloqueada | RugCheck `markets[].lp.lpLockedPct` (cruzar con el resumen: pueden diferir) | [P] ídem |
| Links | DexScreener (par), explorador, página del launchpad (pump.fun), web / Telegram / X desde DexScreener `info` o la metadata del token (`token.uri`) | [V] los de DexScreener y explorador |

### 🧬 Sección 3 — Naturaleza del activo

| Campo | Cómo se obtiene |
|---|---|
| ¿Qué es? (memecoin, DeFi, L1, L2, RWA, DePIN, sintético) | Pipeline Solana pump.fun → memecoin (por el origen del lanzamiento). Multi-chain → grupo `a..h` del doc 23 + categorías de CoinGecko (`coins/{id}` → `categories`). |
| ¿A qué pertenece? (categoría, narrativa) | Categorías de CoinGecko; para memes, la capa narrativa (`lib_narrative`, Cap. VII). La capa temática hoy vale 0: se informa la etiqueta, no se puntúa. |
| ¿Qué promete? / ¿Qué representa? | Descripción oficial citada **textual y atribuida** (`description` de la metadata o web oficial). Si no existe: "sin descripción publicada". |
| Historia breve | Creación del par, migración (bonding curve de pump.fun → AMM), máximo y mínimo desde el lanzamiento (OHLCV de GeckoTerminal). |

### 🔬 Sección 4 — Método científico

1. **Fórmula del score** (scorer vigente v7.2.1, `script_82.score_token`): suma de componentes, recortada a 0–100 (Anexo C).
2. **Datos de entrada**: precio, liquidez, mcap, volumen 24 h, m5/h1 (volumen, trades, compras/ventas, cambio de precio), edad del par y score del feed (WS / trending). Cada uno con su valor y su fuente.
3. **Probabilidades** (definiciones del doc 19):
   - **Primaria**: tocar +20% antes de caer −30% desde la entrada, dentro de 48 h (velas OHLC en orden conservador open → low → high → close).
   - **Secundaria**: cierre ≥ +20% a las 48 h.
   - **Post +20%**: fracción de los que tocaron +20% y después llegaron a ≤ −99% dentro de las 48 h (métrica, doc 21).
   - Se publican con **IC90 de Wilson**. Mientras `emission_calibration.json` no tenga `validated: true`: "en validación" + la cifra histórica rotulada con su versión y su n.
4. **IC90 de Wilson**, con z = 1,645:
   `p̂ = k/n`
   `centro = (p̂ + z²/(2n)) / (1 + z²/n)`
   `radio = z·√(p̂(1−p̂)/n + z²/(4n²)) / (1 + z²/n)`
   `IC90 = [centro − radio, centro + radio]` (reproduce 58,5–87,9 para 16/21, doc 21 [V])
5. **Cómo auditarlo**: archivo de detección (ruta + blob git + commit), versión del scorer y comando que recalcula el score con el código del repo (ejemplo en §4). Mismo archivo + misma versión = mismo resultado.
6. **Fórmula del estudio de liquidez** (Sección 1.2): `impacto ≈ 2Δ / L`, con sus supuestos.

### 🎯 Sección 5 — Fundamento de la detección

- **Score final con desglose**: cada componente con su condición, el valor observado y los puntos (+/−). Hoy `script_82` guarda los motivos (`reasons`), no los puntos. El desglose se reconstruye con la tabla del Anexo C.
  - [P] Agregar `score_breakdown` en `script_82` para no depender de la reconstrucción.
- **Señales activadas** con sus valores numéricos. Ejemplo: "MCap $172.160.515 ≥ $1M → +25".
- **Comparación con el baseline poblacional**:
  - fracción de tokens analizados que superó el umbral (v7.2.1: 1,4% ≥ 56, doc 20);
  - baseline de la primaria: 10,5% (doc 22 §1.1);
  - cifras históricas por tramo de score (docs 19 y 21).

### ⏱️ Sección 6 — Vigencia de la señal

- **Ventana operativa: < 48 h** desde la detección (horizonte de la métrica dual), con fecha y hora de vencimiento.
- **Velocidad de la aceleración**: cambio de precio m5 / h1 / h24, volumen m5/h1, trades m5/h1, edad del par al detectar.
- **Duración histórica de eventos similares**: muestra legado v7.1, aciertos primarios n = 38 de 75 tokens con datos [V]:

  | Medida | Mediana |
  |---|---|
  | Máximo | +113% |
  | Mínimo posterior | −99,6% |
  | Último precio a 48 h | −99,5% |

  [P] **Tiempo hasta el +20%** y **tiempo desde el +20% hasta el mínimo**: se calculan con las velas de `calibrate_threshold_v72.CandleSource` (primer índice con `high ≥ 1,2·entrada`; primer índice posterior con `low ≤ 0,01·entrada`) y se publican como mediana con IQR.

### 📚 Sección 7 — Fuentes y trazabilidad

- Todas las URLs consultadas, con su momento.
- Timestamp de la detección (`detected_at`) y de la alerta.
- Archivo de detección: ruta + **blob git** (`git hash-object`) + commit.
- Versión del scorer (`scoring_version`) y del dossier.
- Comandos para recalcular el score y para medir la métrica dual del activo.

---

## 3. Template vacío

```markdown
# {{NOMBRE}} ({{SYMBOL}}) — dossier
🎴 {{TIPO}} en {{CHAIN}} · precio {{PRECIO}} · liquidez {{LIQUIDEZ}} · mcap {{MCAP}}
Detectado {{DETECTADO_UTC}} por {{SEÑAL_PRINCIPAL}} (score {{SCORE}}, scorer v{{SCORING_VERSION}})
Ventana de la señal: hasta {{VENCE_UTC}} (< 48 h)
Material educativo y documentación del método. No es asesoría financiera.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
**Ruta en {{CHAIN}}:** {{WALLET_1}} ({{URL_WALLET_1}}) o {{WALLET_2}} ({{URL_WALLET_2}}) → fondear con {{FONDEO}} → {{DEX_1}} ({{URL_DEX_1}}) · alternativas: {{DEX_ALT}}
{{RUTA_CEX_SI_COTIZA}}

**Estudio de liquidez del par**
| Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 |
|---|---|---|---|---|---|
| {{DEX_ID}} `{{PAIR}}` | {{L}} | {{SLIPPAGE}} | {{I100}} | {{I1000}} | {{I10000}} |
Impacto ≈ 2Δ/L (producto constante, sin comisiones).

**Pasos**
1. Instalar {{WALLET_1}}: {{URL_WALLET_1}}
2. Fondear con {{FONDEO}} (dejar un resto de {{NATIVO}} para comisiones)
3. Conectar la wallet a {{DEX_1}}: {{URL_DEX_1}}
4. Pegar el {{MINT_O_CONTRATO}} y verificar coincidencia exacta: `{{MINT}}`
5. Slippage: {{SLIPPAGE}}
6. Verificar: contrato {{URL_EXPLORER}} · par {{URL_DEXSCREENER}} · mint/freeze authority {{AUTH}} · holders {{HOLDERS}} (top-10 {{TOP10}})
7. Ejecutar el swap
8. Confirmar la transacción en {{EXPLORER}}

## 📊 Identificación
| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | {{NOMBRE}} / {{SYMBOL}} | {{FUENTE}} |
| Mint / contrato | `{{MINT}}` | {{FUENTE}} |
| Chain / DEX / par | {{CHAIN}} / {{DEX_ID}} / `{{PAIR}}` | DexScreener, al detectar |
| Deployer | `{{DEPLOYER}}` | {{FUENTE}} |
| Par creado · edad al detectar · edad actual | {{PAR_CREADO_UTC}} · {{EDAD_DETECCION}} · {{EDAD_ACTUAL}} | DexScreener pairCreatedAt |
| Mint / freeze authority | {{MINT_AUTH}} / {{FREEZE_AUTH}} | GoPlus / RugCheck, consulta {{FECHA}} |
| Holders / top-10 / LP bloqueada | {{HOLDERS}} / {{TOP10_PCT}} / {{LP_LOCKED}} | RugCheck, consulta {{FECHA}} |
| Links | {{DEXSCREENER_URL}} · {{EXPLORER_URL}} · {{LAUNCHPAD_URL}} · {{WEB}} · {{TELEGRAM}} · {{X}} | — |

## 🧬 Naturaleza
- Tipo: {{TIPO}} (grupo {{GRUPO}}, doc 23) · categoría / narrativa: {{CATEGORIAS}}
- Qué promete / qué representa: {{DESCRIPCION_OFICIAL_TEXTUAL}} — fuente: {{FUENTE_DESCRIPCION}}
- Historia: {{HISTORIA}}

## 🔬 Método
- Score: componentes de `script_82.score_token` v{{SCORING_VERSION}} (Anexo C del doc 24)
- Datos de entrada (al detectar): {{TABLA_INPUTS}}
- Primaria (tocar +20% antes de −30%, ≤48 h): {{P1}} (IC90 {{P1_IC}}, n={{P1_N}})
- Secundaria (cierre ≥ +20% a 48 h): {{P2}} (IC90 {{P2_IC}}, n={{P2_N}})
- Después de tocar +20%, llegar a ≤ −99% (≤48 h): {{P3}} (IC90 {{P3_IC}}, n={{P3_N}})

## 🎯 Fundamento
| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
{{FILAS_DESGLOSE}}
| **Total** | recortado a 0–100 | | **{{SCORE}}** |
- Población: {{BASELINE}}

## ⏱️ Vigencia
- Ventana: < 48 h desde {{DETECTADO_UTC}} (hasta {{VENCE_UTC}})
- Aceleración al detectar: m5 {{PC_M5}} · h1 {{PC_H1}} · h24 {{PC_H24}} · vol m5/h1 {{VOL_RATIO}} · trades m5/h1 {{TRADES_RATIO}}
- Histórico de eventos similares: {{DURACION_HISTORICA}}

## 📚 Fuentes y trazabilidad
- Detección: `{{ARCHIVO_DETECCION}}` · blob {{BLOB}} · commit {{COMMIT}}
- Fuentes: {{LISTA_URLS_CON_MOMENTO}}
- Auditar el score: {{COMANDO_RECALCULO}}
```

---

## 4. Ejemplo completo — VSOF (activo real del repo)

Datos al detectar tomados de `02_Analisis/alerts/alert_6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump_2026-09-29_171330.json`, `_all_alerts.json` y `detection_2026-09-29_170818.json`. Consultas actuales del 2026-10-01 ~00:50 UTC. Todo [V] salvo lo marcado.

> # VSOF (VSOF) — dossier
> 🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1721 · liquidez $1.195.184 · mcap $172.160.515
> Detectado el 29/09 a las 17:08 UTC por el feed trending: score WS 100, mcap > $1M y volumen alto (score 95, scorer v7.2 previo a R1).
> Ventana de la señal: hasta el 01/10 a las 17:13 UTC (< 48 h desde la alerta).
> Material educativo y documentación del método. No es asesoría financiera.

### 🛒 4.1 Cómo adquirir VSOF

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so). La liquidez principal está en **pumpswap**; Jupiter enruta hacia ese pool. Ruta por exchange centralizado: n/d (no se verificó si cotiza).

**Estudio de liquidez del par** (impacto ≈ 2Δ/L) [V cálculo; H modelo]

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 |
|---|---|---|---|---|---|---|
| Al detectar (29/09) | pumpswap `5pav7s4…RGdx` | $1.195.184 | 1% | 0,017% | 0,167% | 1,673% |
| Consulta 01/10 | ídem (único par) | $2.120.738 | 1% | 0,009% | 0,094% | 0,943% |

**Pasos**
1. Instalar Phantom: https://phantom.app (o Solflare: https://solflare.com).
2. Fondear con SOL o USDC en Solana, dejando un resto de SOL para comisiones.
3. Conectar la wallet a Jupiter: https://jup.ag
4. Pegar el mint y verificar coincidencia exacta: `6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump`
5. Slippage: 1% (liquidez ≥ $1M).
6. Verificar:
   - contrato: https://solscan.io/token/6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump
   - par: https://dexscreener.com/solana/5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx
   - mint y freeze authority revocadas; 2.813 holders, top-10 10,02% (consulta 01/10).
7. Ejecutar el swap.
8. Confirmar la transacción en Solscan. Si VSOF no aparece en la wallet, agregarlo pegando el mint.

### 📊 4.2 Identificación

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | VSOF / VSOF | feed trending (ventana 1h, score WS 100), al detectar |
| Mint | `6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump` | detección |
| Chain / DEX / par | Solana / pumpswap / `5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx` | DexScreener, al detectar (único par en la consulta del 01/10) |
| Deployer | `BYBkmcyrsF2ZADiTJyGYuYvXhuGFitLiBnCAoiBDAm56` | RugCheck `creator`, consulta 01/10 (el feed trending no trae `traderPublicKey`) |
| Par creado | 2026-09-29 17:06:53 UTC | DexScreener `pairCreatedAt` = 1790701613000 (RugCheck `detectedAt` 17:06:54) |
| Edad al detectar / al alertar | ~1,4 min (corrida 17:08:18) / ~6,6 min (alerta 17:13:30) | cálculo |
| Mint / freeze authority | revocadas / revocadas · metadata inmutable | GoPlus (`mintable`, `freezable`, `metadata_mutable` en status 0) y RugCheck (`mintAuthority` = `freezeAuthority` = null), consulta 01/10 |
| Holders / top-10 | 2.813 / 10,02% (cada uno de los 10 figura con 1,00%; 0 marcados como insider) | RugCheck report, consulta 01/10 |
| Liquidez bloqueada | **inconsistente entre endpoints**: `report/summary` → `lpLockedPct` 0; `report` → mercado `pump_fun_amm` con `lpLockedPct` 100 | RugCheck, consulta 01/10 |
| Señales que lista RugCheck | "High market cap per holder", "High holder correlation" (`score_normalised` 54) | RugCheck summary, consulta 01/10 |
| Links | https://dexscreener.com/solana/5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx · https://solscan.io/token/6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump · https://pump.fun/coin/6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump · web / Telegram / X: **no publicados** (DexScreener `info` vacío) | consulta 01/10 |

### 🧬 4.3 Naturaleza

- **Tipo:** memecoin (lanzamiento en el launchpad pump.fun, migrado a su AMM pumpswap). Grupo **a** del doc 23.
- **Categoría / narrativa:** `n/d` (sin categoría de CoinGecko verificada para este mint; capa narrativa sin etiqueta) [P].
- **Qué promete / representa:** sin descripción publicada en DexScreener. [P] Falta leer `description` de la metadata del token.
- **Historia:**
  - Par creado el 29/09 a las 17:06:53 UTC.
  - Detectado ~1,4 min después, ya con mcap de $172 M. El `priceChange24h` de +350.628% refleja el salto desde la bonding curve.
  - Al 01/10, liquidez de $2.120.738 y FDV de $540,2 M.

### 🔬 4.4 Método

**Datos de entrada (al detectar):**

| Dato | Valor |
|---|---|
| Precio | $0,1721 |
| Liquidez | $1.195.183,55 |
| MCap | $172.160.515 |
| Volumen 24 h | $586.622,08 |
| Cambio 24 h | +350.628% |
| Score WS (trending) | 100 |

Los campos m5/h1 y `pairCreatedAt` no existían en el registro de esa versión. Las derivadas quedan en 0 y la edad en `n/d`.

**Probabilidades:** **en validación** para v7.2.1. Histórico (legado v7.1, score ≥ 56) [V]:

| Métrica | Valor | n |
|---|---|---|
| Primaria | 60,0% | 35 |
| Secundaria | 8,6% | 35 |
| Después de tocar +20%, llegar a ≤ −99% | 76,2% (IC90 58,5–87,9) | 21 |

Fuentes: doc 19 §4.2 y doc 21.

### 🎯 4.5 Fundamento (desglose reproducido)

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | WS × 0,3 | 100 × 0,3 | +30 |
| MCap | ≥ $1M | $172.160.515 | +25 |
| Volumen 24 h | ≥ $100K (< $1M) | $586.622 | +15 |
| Liquidez | ≥ $100K | $1.195.184 | +15 |
| Cambio 24 h | ≥ +50% | +350.628% | +10 |
| **Total (scorer de ese momento)** | | | **95** = score registrado [V] |

- **Recalculado con el scorer vigente v7.2.1** sobre los mismos datos: **45** [V].
  - Se suma **SOBRECOMPRA EXTREMA (> 50.000%) −50**.
  - Los bonos temporales se omiten porque la edad no se conoce.
  - Hoy no superaría el umbral de 56. La edad del par (~1,4 min < 30 min) también lo excluiría.
- El mismo dato da scores distintos según la versión: por eso el dossier fija `scoring_version` y el archivo exacto.
- **Población:** con v7.2.1, el 1,4% de los tokens analizados queda ≥ 56 (doc 20). Baseline de la primaria: 10,5% (doc 22 §1.1).

### ⏱️ 4.6 Vigencia

- **Ventana:** < 48 h desde las 17:13 UTC del 29/09, o sea hasta las 17:13 UTC del 01/10.
- **Seguimiento registrado** (trust loop, precio contra la entrada de $0,1721) [V]:

  | Momento | Precio | Cambio | Registro |
  |---|---|---|---|
  | t+1h | $0,1819 | +5,69% | |
  | t+6h | $0,2303 | +33,82% | |
  | t+24h | $0,4448 | +158,45% | `final_verdict` NEUTRAL |

- **Consulta del 01/10 (~31,5 h):** $0,5401 (+213,8%).
- **Métrica dual de VSOF** (velas de 15 min de GeckoTerminal, entrada $0,1721 a las 17:08 UTC del 29/09, consulta del 01/10 02:46 UTC, `script_113`):
  - Primaria: **se cumplió** [V]. Tocó +20% a las 3,86 h; antes, el mínimo fue −0,9% (nunca se acercó a −30%). 135 velas, 0 ambiguas.
  - Secundaria: [P] se resuelve a las 17:08 UTC del 01/10 (48 h desde la detección).
- **Velocidad de la aceleración:** m5 / h1 `n/d` (no se guardaban en esa versión).

### 📚 4.7 Fuentes y trazabilidad

- **Detección:**
  - archivo `01_Datos_Crudos/final_detection/detection_2026-09-29_170818.json`;
  - blob `3eae871029a40334fee5b69efe8e4adeeea15068`;
  - commit `be8e7d3` (2026-09-29 17:13:31 UTC).
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-09-29_171330`, `status: active_tracking`, `confidence` 64.
- **Consultas (01/10):**
  - `api.dexscreener.com/latest/dex/tokens/<mint>`
  - `api.rugcheck.xyz/v1/tokens/<mint>/report` y `/report/summary`
  - `api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=<mint>`
- **Auditar el score** desde la raíz del repo:

  ```bash
  python -c "import json,importlib.util as u;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump_2026-09-29_171330.json'));print(m.SCORING_VERSION, m.score_token(d['token'], d['dexscreener']))"
  ```

  Con el código de hoy devuelve `7.2.1 (45, …)` [V]. Para reproducir el 95, mismo comando con el `script_82` del commit de la detección (`git show be8e7d3:04_Config/scripts/script_82_final_detection.py > s82_be8e7d3.py`): devuelve `(95, ['WS score muy alto', 'MCap > $1M', 'Volumen alto', 'Liquidez alta', 'Pump 24h'])` [V, reproducido el 01/10].

---

## 5. Anexo A — Checklist de campos por sección

**Regla de emisión:** si cualquier campo **obligatorio de la Sección 1 (adquisición)** falta, **no se emite ni la alerta ni el dossier**. En las demás secciones, lo que falta se marca `n/d`.

| Sección | Campo | Obligatorio | Si falta |
|---|---|---|---|
| 🛒 1 | chain con guía verificada (fila en la tabla 1.1) | **sí** | **no se emite** |
| 🛒 1 | mint / contrato | **sí** | **no se emite** |
| 🛒 1 | wallet(s) con enlace oficial | **sí** | **no se emite** |
| 🛒 1 | DEX / agregador con enlace oficial | **sí** | **no se emite** |
| 🛒 1 | activo para fondear (nativo o stablecoin) | **sí** | **no se emite** |
| 🛒 1 | los 8 pasos | **sí** | **no se emite** |
| 🛒 1 | slippage sugerido (por tramo de liquidez o "5–10%" si L desconocida) | **sí** | **no se emite** |
| 🛒 1 | enlaces de verificación: explorador + DexScreener | **sí** | **no se emite** |
| 🛒 1 | pool principal, L e impactos $100 / $1.000 / $10.000 | sí | `n/d` con motivo (p. ej., bonding curve) |
| 🛒 1 | ruta por exchange centralizado | no (sí en blue chips) | "no verificado" |
| 🎴 | portada (tipo, precio, liquidez, señal, ventana) | sí | `n/d` por campo |
| 📊 2 | nombre, symbol, chain | sí | no se emite |
| 📊 2 | DEX y par principal, `pairCreatedAt` | sí | `n/d` + motivo |
| 📊 2 | deployer | sí | `n/d` (fuente: RugCheck `creator`) |
| 📊 2 | mint / freeze authority, holders, top-10, LP bloqueada | sí | `n/d` + fuente |
| 📊 2 | web / Telegram / X | no | "no publicados" |
| 🧬 3 | tipo y grupo (doc 23) | sí | — |
| 🧬 3 | categoría / narrativa, descripción oficial | no | `n/d` / "sin descripción publicada" |
| 🔬 4 | versión del scorer + tabla de componentes | sí | no se emite |
| 🔬 4 | datos de entrada con valor y fuente | sí | `n/d` por campo |
| 🔬 4 | primaria / secundaria / post +20% con IC90 y n | sí | "en validación" + histórico rotulado |
| 🎯 5 | desglose que suma el score registrado | sí | "desglose no reproducible" → no se publica |
| ⏱️ 6 | ventana y vencimiento | sí | — |
| ⏱️ 6 | derivadas m5 / h1 / h24 | sí | `n/d` |
| 📚 7 | archivo de detección + blob + commit, URLs con momento, comando de recálculo | sí | no se emite |

---

## 6. Anexo B — Integración multi-chain (diseño, sin implementar)

### 6.1 Estado actual

- **Ruta rápida Solana** (`pipeline_t0`, cada 20 min): `script_82` (PumpPortal + trending → score v7.2.1) → `shadow_v4/_accumulated.json` → `script_97` (emisión; en sombra).
- **Scanner multi-chain v0** (`script_114`, en main desde `3694aa8`):
  - fuentes: CoinGecko sin key para los grupos h, f, c, g, d, e y GeckoTerminal para a (solana, base, eth, blast, monad);
  - solo recolecta y marca aceleración [H];
  - no está enganchado a ningún workflow.

### 6.2 Regla de adquisición por chain (Dirección, 01/10)

**Ningún activo se alerta sin su guía de compra específica para su chain.**

| Tipo / chain | Guía mínima obligatoria |
|---|---|
| Solana | Phantom (+ Solflare) · Jupiter (+ Raydium, Orca) · SOL o USDC |
| Ethereum / EVM | MetaMask (+ Rabby) · Uniswap (+ 1inch) · ETH o USDC/USDT |
| Base | MetaMask (+ Coinbase Wallet) · Aerodrome (+ Uniswap) · ETH o USDC en Base |
| Blue chips (BTC / ETH / SOL) | además, **exchanges centralizados**: Binance, Coinbase, Kraken (par contra USDT/USD), y la ruta on-chain de su red |
| Blast, Monad y otras | sin guía verificada → **no se alertan** hasta agregarla |

`script_97` ya aplica esta regla (`acquisition_ready`): una chain sin guía o un candidato sin mint no se emite.

### 6.3 Arquitectura propuesta

```
multichain_scan.yml  (cron cada 30–60 min; concurrency propia; commitea solo sus archivos)
   script_114 → 02_Analisis/multichain/scan_latest.json (+ histórico diario comprimido)
   script_115_multichain_score.py (tentativo) → 02_Analisis/multichain/_accumulated.json
        cada candidato: universe, group (a–h), chain, address, scoring_version "mc-<grupo>-x.y", detected_at
pipeline_t0.yml (sin cambios en la ruta Solana)
   script_97 lee DOS fuentes de candidatos: shadow_v4/_accumulated.json (Solana) y multichain/_accumulated.json
        umbral, edad mínima y frescura POR GRUPO · dedup por chain:address · guía de compra por chain obligatoria
        status "shadow" con campo `group` hasta validar cada grupo por separado
monitor_shadow.py → métrica dual POR GRUPO (y por versión) · el veredicto por grupo habilita la emisión de ese grupo
```

Cómo convive con `script_82`:
- **No lo toca.** La ruta Solana sigue siendo la rápida (20 min). La multi-chain es lenta (30–60 min), porque CoinGecko sin key admite ~1 request cada 15 s [V doc 23].
- **Acumulados separados**: no hay escrituras cruzadas ni conflictos de rebase entre workflows.
- **Un solo emisor** (`script_97`) y un solo formato de alerta y de dossier, con la guía de compra por chain.
- **Memes EVM** (grupo a en Base): misma lógica que Solana (edad, liquidez, volumen, m5/h1), alimentada por GeckoTerminal `new_pools` / `trending_pools`. Blast sin actividad: 0 pools nuevos [V doc 23].

### 6.4 Orden de activación (prioridad de Dirección)

| Paso | Grupo | Fuentes | Requisito para pasar al siguiente |
|---|---|---|---|
| 1 | **h** blue chips (BTC/ETH/SOL) | Binance data-api (velas desde 2017), Coinbase / Kraken (cruce), Deribit DVOL, Fear & Greed, funding (fallback Hyperliquid / dYdX si Binance devuelve 451 desde Actions) | acceso verificado **desde Actions**; walk-forward con purga; ≥ 20 eventos resueltos en sombra |
| 2 | **f** L1/L2 emergentes | CoinGecko layer-1 / layer-2, DefiLlama (TVL y fees por cadena), growthepie, L2BEAT | ídem |
| 3 | **c** gobernanza DeFi | CoinGecko governance, DefiLlama `/protocols` (`listedAt` < 90 días), Snapshot | ídem |
| 4 | **e / g** DePIN y RWA | CoinGecko depin / real-world-assets-rwa, DefiLlama (fees, TVL, categoría RWA) | ídem |
| 5 | **b / d** preventa y sintéticos | Hyperliquid (premium, OI, HIP-3), Aevo (pre-IPO), DefiLlama stablecoins, dYdX v4, GMX | ídem; preventa cripto sin fuente gratuita estable [V doc 23] |
| — | **a** memes EVM | GeckoTerminal por red | después de que la ruta Solana valide v7.2.1 |

### 6.5 Scoring por tipo de activo [H, a validar grupo por grupo]

| Grupo | Evento a medir (métrica dual adaptada) | Señales del score | Modelos permitidos |
|---|---|---|---|
| h | tocar +kσ antes de −kσ (σ diaria GARCH), k a calibrar; en blue chips un +20% en 48 h es raro | z de retorno vs σ GARCH, DVOL − vol realizada, funding en percentil extremo, Fear & Greed ≤ 20 / ≥ 80, ruptura de Bollinger con volumen, ATR | **GARCH / EGARCH / HAR-RV, ATR, Bollinger** (permitidos en Universo A; `arch`, NCSA) |
| f | +20% en 48 h relativo a ETH/SOL | momentum relativo, aceleración de TVL, fees/TVL en percentil alto, protocolos nuevos por semana | GARCH solo con ≥ 365 velas |
| c | +20% en 48 h alrededor del cierre de propuestas | protocolo < 90 días, fees en ascenso, mcap/TVL bajo, propuestas de emisiones o fee switch | event study + placebo |
| e / g | +20% en 48 h | divergencia precio vs fees 30 d, FDV/mcap, TVL creciendo más rápido que el mcap (RWA) | event study |
| b | convergencia del premium al listar | premium mark/oracle, crecimiento de OI | sin GARCH (no hay historia) |
| d | desvío del peg y su reversión | \|precio − 1\|, caída del circulante semanal, funding extremo | reversión a la media (OU) [H] |
| a | +20% antes de −30% (igual que Solana) | edad, liquidez, volumen, m5/h1; datos de GoPlus / Honeypot como **dato del dossier**, no del score, hasta testearlos (propuesta I-2) | **sin GARCH / ATR / Bollinger** (prohibido en memecoins) |

**Reglas comunes:**
- Cada grupo tiene su `scoring_version`, su umbral y su veredicto en sombra con n ≥ 20, IC90 de Wilson y baseline propio.
- Ningún grupo emite fuera de sombra sin decisión de Dirección.
- Todos usan la misma estructura de dossier, con 🛒 primero.

### 6.6 Presupuesto y riesgos

- **Una corrida del scanner:** ~13 llamadas en ~2,5 min. Cada 30 min son ~620 llamadas/día a CoinGecko sin key, con espaciado de 15 s [I: el límite diario sin key no está documentado; si aparecen 429 persistentes, bajar a cada 60 min].
- **IP de los runners de EE.UU.:** Binance derivados puede devolver 451. Cada fuente se verifica desde Actions antes de depender de ella.
- **Fuentes que pasan a pago** (ya pasó con DefiLlama: 402): las detecta la sonda de deriva de fuentes (propuesta I-5 del doc 23).

---

## Anexo C — Componentes del score v7.2.1 (`script_82.score_token`) [V, leído del código]

| Componente | Condición | Puntos |
|---|---|---|
| Score del feed | `ws_score × 0,3` | 0 a +30 |
| MCap | ≥ $1M / ≥ $100K / ≥ $50K / menor | +25 / +15 / +10 / 0 |
| Volumen 24 h | ≥ $1M / ≥ $100K / ≥ $50K / menor | +20 / +15 / +10 / 0 |
| Liquidez | ≥ $100K / ≥ $50K / ≥ $20K / menor | +15 / +10 / +5 / 0 |
| Cambio 24 h | ≥ +50% / ≥ +20% / ≤ −30% | +10 / +5 / −5 |
| Buy pressure dinámica (`bp_delta` vs la corrida anterior) | ≤ −0,10 / ≥ +0,10 (solo par maduro) | −15 / +15 |
| **Solo par maduro (edad ≥ 60 min, gate v7.2.1):** | | |
| · Volumen m5/h1 | > 0,5 / > 0,25 | +25 / +15 |
| · Trades m5/h1 | > 0,5 / > 0,25 | +20 / +10 |
| · Buy pressure m5 | > 60% / > 55% | +25 / +15 |
| · Momentum | m5 > 0 y h1 > 0 / m5 > 0 y h1 > −5% | +20 / +10 |
| · Edge temprano | edad < 4 h | +8 |
| · Volumen m5 | > $1K / > $500 | +10 / +5 |
| Detección tardía | sin volumen m5 y edad > 4 h | −30 |
| Par viejo | edad > 24 h | −50 |
| Venta dominante | buy pressure < 40% con volumen m5 | −20 (el tramo < 30%, −35, está detrás del de < 40% y no se alcanza: bug registrado en el doc 22, P2) [V] |
| Sobrecompra | cambio 24 h > 50.000% | −50 |
| | > 5.000% con liq/mcap < 1% / < 3% | −50 / −15 |
| | > 500% con liq/mcap < 1% / < 3% | −30 / −10 |
| Kill switch | edad < 5 min y cambio 24 h > 10.000% | −50 |
| **Final** | `min(100, max(0, int(suma)))` | 0–100 |

Filtros de emisión (`script_97`):
- score ≥ 56;
- scoring de los últimos 60 min (R1);
- edad del par ≥ 30 min (edad desconocida = no emite);
- **guía de compra completa para la chain**;
- dedup por mint.

---

## 7. Implementación — `script_113_dossier_builder.py` (v1.0)

**Funciones** (`04_Config/scripts/script_113_dossier_builder.py`):

| Función | Qué hace |
|---|---|
| `load_alert_data(mint, chain)` | Junta el registro exacto de la alerta (`alerts/alert_<mint>_<ts>.json`; si no hay, el del acumulado), la entrada de `_all_alerts.json`, las señales on-chain (`signals/[<chain>/]<mint>.json`), las trazas git, la población del scorer, la calibración y la sombra |
| `fetch_live(mint, chain, …)` | DexScreener, RugCheck (Solana), GoPlus (Solana y EVM), GeckoTerminal (velas de 1 h y de 15 min). Cada llamada queda registrada con URL, estado y momento |
| `build_dossier(mint, chain, alert_data, live=None, now=None)` | Dict con la portada y las 7 secciones, más `missing` y `emitible` (checklist del Anexo A) |
| `render_markdown(dossier)` | Markdown con 🛒 primero |
| `save_dossier(dossier, path=None)` | `02_Analisis/dossiers/<chain>/<mint>.md` + `.json`. Si no es emitible, no escribe nada |
| `generate_pdf(dossier)` | [P] No hay librería liviana instalada y no se agregan dependencias sin verificar su supply chain |

**Uso:** `--dry-run` (VSOF con datos fijos, sin red) · `--mint <MINT> [--chain] [--offline] [--stdout] [--out]`.

**Reutiliza, sin duplicar definiciones:**
- de `script_97`: guías de compra, slippage, impacto, exploradores;
- de `calibrate_threshold_v72`: métrica dual, Wilson, velas de 15 min y carga del scorer.

**Agregados al diseño (precisión del método):**
- **Desglose verificado contra el scorer.** Se reconstruye desde los motivos registrados (sin reloj ni estado) y solo se publica si la suma coincide con el score guardado. Un test lo compara con `script_82.score_token` en 400 casos sintéticos.
- **Recálculo con el scorer vigente**, con el reloj fijado en la detección. VSOF: 95 → 45 [V].
- **Métrica dual del activo** con las mismas velas y reglas que la calibración, más el **tiempo hasta +20%**. Resuelve el [P] de §4.6.
- **Tamaño de orden con prima 1% / 3%**: Δ = x·L/2. Es la capacidad del pool, al lado de los impactos de $100, $1.000 y $10.000.
- **Holders efectivos del top-10**: (Σp)²/Σp², la inversa del Herfindahl. VSOF: 10,0 (diez holders de ~1% cada uno).
- **Percentil del score en la población** del scorer vigente (`_accumulated.json`). VSOF: 3 de 2.802 tokens quedan ≥ 56 (0,11%) [V].
- **Consistencia entre fuentes**: diferencia relativa de la liquidez entre DexScreener y RugCheck y del precio entre DexScreener y GeckoTerminal. VSOF: 0,09% y 0,09%.
- **Huella SHA-256** de los datos de entrada: el `.json` contiene `inputs` y cualquiera puede verificar que el dossier salió de esos datos.
- **Blob con `git hash-object`**: coincide con `git ls-tree` aunque el checkout use CRLF (autocrlf en Windows).

**Límites:**
- No está enganchado al pipeline ni a `sendDocument`. Engancharlo toca un workflow de producción: consultar antes.
- Categoría y narrativa: `n/d` [P]. CoinGecko `coins/{id}` necesita resolver el id del contrato.
- Jupiter en vivo no se consulta: `lite-api.jup.ag` está prohibido y `api.jup.ag` requiere key [I]. Se usa el archivo de señales del repo si existe.
- Los registros de alerta sin `scoring_version` (21 de las 35 de `_all_alerts.json` [V]) se rotulan `7.2-preR1` (convención de `monitor_shadow`).
