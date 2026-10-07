# Texas Institute of Technology S (TITS) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001132 · liquidez $28.599 · mcap $113.207 (al detectar)  
Detectado el 07/10/2026 16:52 UTC por: young-0.4 · edad 11.2 min · pesos info 59 / estructura 20 / precio 20 · info 20.5 · estructura 17.3 · precio/volumen 12.9 · cobertura 93/100, [info] narrative_wave: ola 'tits': 13 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.6 (score 51, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 09/10/2026 16:52 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir TITS

Estudio de cómo se adquiere TITS, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/10/2026 17:22 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/10/2026 16:52 UTC | pumpswap `FeHPV6c…44Hq` | $28.599 | 10% | 0,699% | 6,993% | 69,933% | $143 | $429 |
| consulta 07/10/2026 17:22 UTC | pumpswap `FeHPV6c…44Hq` | $2.278 | 10% | 8,779% | 87,789% | 877,894% | $11 | $34 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump`
5. Configurar el slippage: 10% (liquidez $2.278, consulta 07/10/2026 17:22 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump) y el par en DexScreener (https://dexscreener.com/solana/FeHPV6c7vC8vXr6NsDvHiimTcMoRGNvpyyXPdBti44Hq); mint authority / freeze authority: revocada / revocada · holders 166 · top-10 99,86% (consulta 07/10/2026 17:22 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump
- Par en DexScreener: https://dexscreener.com/solana/FeHPV6c7vC8vXr6NsDvHiimTcMoRGNvpyyXPdBti44Hq
- Página del lanzamiento (pump.fun): https://pump.fun/coin/DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 166 · top-10 99,86% (consulta 07/10/2026 17:22 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Texas Institute of Technology S / TITS | registro de la detección (pumpportal_live) |
| Mint / contrato | `DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `FeHPV6c7vC8vXr6NsDvHiimTcMoRGNvpyyXPdBti44Hq` | DexScreener, al detectar (2 par(es) en la consulta 07/10/2026 17:22 UTC) |
| Deployer | `8DiRaZNZoTRc4HPwiJZ4oLAbCSxAR29oxES566UoucWr` | PumpPortal (evento create), al detectar |
| Par creado | 07/10/2026 16:41 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,2 min / 11,2 min / 40,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/10/2026 17:22 UTC |
| Holders / top-10 | 166 / 99,86% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/10/2026 17:22 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/10/2026 17:22 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 07/10/2026 17:22 UTC |
| Links | DexScreener: https://dexscreener.com/solana/FeHPV6c7vC8vXr6NsDvHiimTcMoRGNvpyyXPdBti44Hq · Solscan: https://solscan.io/token/DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump · pump.fun: https://pump.fun/coin/DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump · web / Telegram / X: no publicados en DexScreener | consulta 07/10/2026 17:22 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/10/2026 17:22 UTC)
- **Historia:**
  - Par creado el 07/10/2026 16:41 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/10/2026 16:52 UTC, con el par a 11,2 min de creado: precio $0,0001132, mcap $113.207, liquidez $28.599.
  - Velas de 1 h de GeckoTerminal (2, desde 07/10/2026 16:00 UTC): apertura $0,00005498 · máximo $0,0001775 (07/10/2026 16:00 UTC) · mínimo $0,000002239 (07/10/2026 16:00 UTC) · último cierre $0,000002243.
  - En la consulta 07/10/2026 17:22 UTC: precio $0,000002246, liquidez $2.278, FDV $2.246.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/10/2026 16:52 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001132 |
| Liquidez | $28.599 |
| MCap | $113.207 |
| Volumen 24 h | $66.576 |
| Cambio 24 h | +133% |
| Cambio m5 / h1 | +67,8% / +133,0% |
| Volumen m5 / h1 | $29.779 / $66.576 |
| Trades m5 (compras / ventas) | 1.551 / 516 |
| Edad del par | 11,2 min |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 1/2 (50,0%, IC90 12,1%–87,9%) · secundaria 0/2 resueltas (shadow_monitor.json).

Histórico (legado v7.1, score ≥ 56 (docs 19 §4.2 y 21)):

| Métrica (histórico) | k/n | Tasa | IC90 |
|---|---|---|---|
| Primaria: tocar +20% antes de caer −30% (≤ 48 h) | 21/35 | 60,0% | 46,1%–72,4% |
| Secundaria: cierre ≥ +20% a las 48 h | 3/35 | 8,6% | 3,5%–19,6% |
| Después de tocar +20%, llegar a ≤ −99% (≤ 48 h) | 16/21 | 76,2% | 58,5%–87,9% |

**IC90 de Wilson** (z = 1,645): p̂ = k/n · centro = (p̂ + z²/2n)/(1 + z²/n) · radio = z·√(p̂(1−p̂)/n + z²/4n²)/(1 + z²/n).
**Métrica dual:** velas de 15 min de GeckoTerminal del mismo pool, orden intra-vela conservador open → low → high → close; si una vela toca −30% y +20%, cuenta primero la caída.
**Estudio de liquidez:** prima de ejecución = 2Δ/L (sección 1.1).

---

## 🎯 5. Fundamento de la detección

Desglose no reproducible desde los motivos registrados (suma 0 vs score 51; motivos sin regla: young-0.4 · edad 11.2 min · pesos info 59 / estructura 20 / precio 20 · info 20.5 · estructura 17.3 · precio/volumen 12.9 · cobertura 93/100, [info] narrative_wave: ola 'tits': 13 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.6, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1954 · top-10 28.1 % → +4.9, [estructura] dev_wallet: creador compró 3.5 % del supply → +2.0, [estructura] holder_to_txn_ratio: holders/txns 1954/4757 = 0.41 → +0.7, [precio/volumen] volume_acceleration: vol 5 min ×5.4 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 75% en 5 min vs 69% en 1 h (s 0.32), [precio/volumen] liquidity_inflow: liquidez +56% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1120→1954 (+139.0/min) · top10 31.0%→28.1% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=28598.88, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 51 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-07T16:52:47+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen decente, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 31 de 19.193 tokens analizados (0,16%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/10/2026 16:52 UTC, hasta 09/10/2026 16:52 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +67,8% · h1 +133,0% · h24 +133% · volumen m5/h1 0,45 · edad del par 11,2 min.
- **Precio de entrada** (alerta): $0,0001132.
- **Consulta 07/10/2026 17:22 UTC:** $0,000002246 (-98,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump_2026-10-07_165247.json` · blob `510d99375f8fd7a94e36230724fd6d04a031de80` · commit `53fceb9` (2026-10-07T17:14:48Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-07_163640.json` · blob `6a84ba29159f233a67a2de42650ec0ee1aeb79b6` · commit `53fceb9` (2026-10-07T17:14:48Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-07_165247`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump · registro · 07/10/2026 16:52 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump · HTTP 200 · 07/10/2026 17:22 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump/report · HTTP 200 · 07/10/2026 17:22 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump · HTTP 200 · 07/10/2026 17:22 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/FeHPV6c7vC8vXr6NsDvHiimTcMoRGNvpyyXPdBti44Hq/ohlcv/hour?limit=1000 · HTTP 200 · 07/10/2026 17:22 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump · HTTP 404 · 07/10/2026 17:22 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=TITSUSDT · HTTP 400 · 07/10/2026 17:22 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/TITS-USD · HTTP 404 · 07/10/2026 17:22 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.278 vs $2.275 → 0,13%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002246 vs $0,000002243 → 0,11%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump_2026-10-07_165247.json',encoding='utf-8'));d=d.get('DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump',d);p=mock.patch('time.time',return_value=1791391967);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint DGGdESpe4QfhEfcG3Xn5imQdS8qNpAB9EZm7DgxZpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/10/2026 17:22 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `6b9165f10c578eca…`
