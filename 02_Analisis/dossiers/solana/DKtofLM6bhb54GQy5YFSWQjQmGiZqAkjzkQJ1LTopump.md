# Diamond Hands (HODL) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003713 · liquidez $159.701 · mcap $3.696.810 (al detectar)  
Detectado el 07/11/2026 09:02 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 09/11/2026 09:02 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HODL

Estudio de cómo se adquiere HODL, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/11/2026 09:02 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/11/2026 09:02 UTC | pumpswap `ANS69UD…QGKR` | $159.701 | 5% | 0,125% | 1,252% | 12,523% | $799 | $2.396 |
| consulta 07/11/2026 09:02 UTC | pumpswap `ANS69UD…QGKR` | $159.994 | 5% | 0,125% | 1,250% | 12,500% | $800 | $2.400 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump`
5. Configurar el slippage: 5% (liquidez $159.994, consulta 07/11/2026 09:02 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump) y el par en DexScreener (https://dexscreener.com/solana/ANS69UDTbMCWbW7ZuCYXLZ4HMCQkvzPMtCW9zjPZQGKR); mint authority / freeze authority: revocada / revocada · holders 9.491 · top-10 3,40% (consulta 07/11/2026 09:02 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump
- Par en DexScreener: https://dexscreener.com/solana/ANS69UDTbMCWbW7ZuCYXLZ4HMCQkvzPMtCW9zjPZQGKR
- Página del lanzamiento (pump.fun): https://pump.fun/coin/DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 9.491 · top-10 3,40% (consulta 07/11/2026 09:02 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Diamond Hands / HODL | registro de la detección (trending) |
| Mint / contrato | `DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `ANS69UDTbMCWbW7ZuCYXLZ4HMCQkvzPMtCW9zjPZQGKR` | DexScreener, al detectar (2 par(es) en la consulta 07/11/2026 09:02 UTC) |
| Deployer | `9NkVW544fKy2kkU5ZxJFa1xy6C7LssPKZAW5XWbK5XG5` | RugCheck `creator` |
| Par creado | 06/11/2026 23:09 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 9,9 h / 9,9 h / 9,9 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/11/2026 09:02 UTC |
| Holders / top-10 | 9.491 / 3,40% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/11/2026 09:02 UTC |
| Holders efectivos del top-10 | 2,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/11/2026 09:02 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 07/11/2026 09:02 UTC |
| Links | DexScreener: https://dexscreener.com/solana/ANS69UDTbMCWbW7ZuCYXLZ4HMCQkvzPMtCW9zjPZQGKR · Solscan: https://solscan.io/token/DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump · pump.fun: https://pump.fun/coin/DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump · web: https://hodlonsol.vip · twitter: https://x.com/hodlonsolvip · telegram: https://t.me/hodlsolsite | consulta 07/11/2026 09:02 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/11/2026 09:02 UTC)
- **Historia:**
  - Par creado el 06/11/2026 23:09 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/11/2026 09:02 UTC, con el par a 9,9 h de creado: precio $0,003713, mcap $3.696.810, liquidez $159.701.
  - Velas de 1 h de GeckoTerminal (11, desde 06/11/2026 23:00 UTC): apertura $0,0003321 · máximo $0,004618 (07/11/2026 08:00 UTC) · mínimo $0,00004915 (06/11/2026 23:00 UTC) · último cierre $0,003726.
  - En la consulta 07/11/2026 09:02 UTC: precio $0,003727, liquidez $159.994, FDV $3.710.771.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/11/2026 09:02 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003713 |
| Liquidez | $159.701 |
| MCap | $3.696.810 |
| Volumen 24 h | $2.345.344 |
| Cambio 24 h | +7.392% |
| Cambio m5 / h1 | -2,2% / -3,5% |
| Volumen m5 / h1 | $4.155 / $93.597 |
| Trades m5 (compras / ventas) | 375 / 263 |
| Edad del par | 9,9 h |
| Score del feed (WS) | 69 |

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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 69 × 0,3 | +20,7 |
| MCap | ≥ $1M | $3.696.810 | +25 |
| Volumen 24 h | ≥ $1M | $2.345.344 | +20 |
| Buy pressure m5 | > 55% (par maduro) | 59% | +15 |
| Volumen m5 | > $1K (par maduro) | $4.155 | +10 |
| Liquidez | ≥ $100K | $159.701 | +15 |
| Cambio 24 h | ≥ +50% | +7.392% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +7.392% · liq/mcap 4,3% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-07T09:02:10+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >55%, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 95 de 46.846 tokens analizados (0,20%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/11/2026 09:02 UTC, hasta 09/11/2026 09:02 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -2,2% · h1 -3,5% · h24 +7.392% · volumen m5/h1 0,04 · edad del par 9,9 h.
- **Precio de entrada** (alerta): $0,003713.
- **Consulta 07/11/2026 09:02 UTC:** $0,003727 (+0,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump_2026-11-07_090220.json` · blob `eff458859d0f63e00e51046d597e88dea00ed6d3` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-07_085708.json` · blob `49f25f2433c6535cdb9f201ab81c99aa1d282e59` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-07_090220`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump · registro · 07/11/2026 09:02 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump · HTTP 200 · 07/11/2026 09:02 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump/report · HTTP 200 · 07/11/2026 09:02 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump · HTTP 200 · 07/11/2026 09:02 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/ANS69UDTbMCWbW7ZuCYXLZ4HMCQkvzPMtCW9zjPZQGKR/ohlcv/hour?limit=1000 · HTTP 200 · 07/11/2026 09:02 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump · HTTP 404 · 07/11/2026 09:02 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HODLUSDT · HTTP 400 · 07/11/2026 09:02 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HODL-USD · HTTP 404 · 07/11/2026 09:02 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $159.994 vs $159.951 → 0,03%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003727 vs $0,003726 → 0,02%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump_2026-11-07_090220.json',encoding='utf-8'));d=d.get('DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump',d);p=mock.patch('time.time',return_value=1794042130);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/11/2026 09:02 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `978f67908bc7c749…`
