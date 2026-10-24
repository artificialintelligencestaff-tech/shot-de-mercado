# You Missed Bitches (YMB) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0004267 · liquidez $70.911 · mcap $425.256 (al detectar)  
Detectado el 24/10/2026 04:26 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 26/10/2026 04:26 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir YMB

Estudio de cómo se adquiere YMB, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 24/10/2026 04:57 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 24/10/2026 04:26 UTC | pumpswap `BcbQfEr…wpsU` | $70.911 | 5% | 0,282% | 2,820% | 28,204% | $355 | $1.064 |
| consulta 24/10/2026 04:56 UTC | pumpswap `BcbQfEr…wpsU` | $63.230 | 5% | 0,316% | 3,163% | 31,631% | $316 | $948 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump`
5. Configurar el slippage: 5% (liquidez $63.230, consulta 24/10/2026 04:56 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump) y el par en DexScreener (https://dexscreener.com/solana/BcbQfEr3NKp8tJfbCmveqSS1o87npjfSbxuuLDSHwpsU); mint authority / freeze authority: revocada / revocada · holders 17.660 · top-10 21,89% (consulta 24/10/2026 04:56 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump
- Par en DexScreener: https://dexscreener.com/solana/BcbQfEr3NKp8tJfbCmveqSS1o87npjfSbxuuLDSHwpsU
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 17.660 · top-10 21,89% (consulta 24/10/2026 04:56 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | You Missed Bitches / YMB | registro de la detección (trending) |
| Mint / contrato | `2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BcbQfEr3NKp8tJfbCmveqSS1o87npjfSbxuuLDSHwpsU` | DexScreener, al detectar (30 par(es) en la consulta 24/10/2026 04:56 UTC) |
| Deployer | `C5Fezjsn6xV1M6x316tH7s8BNeSUxZtFunr1wTkvYm7W` | RugCheck `creator` |
| Par creado | 23/10/2026 19:01 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 9,4 h / 9,4 h / 9,9 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 24/10/2026 04:56 UTC |
| Holders / top-10 | 17.660 / 21,89% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 24/10/2026 04:56 UTC |
| Holders efectivos del top-10 | 4,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; raydium_clmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; orca 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 24/10/2026 04:56 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 24/10/2026 04:56 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BcbQfEr3NKp8tJfbCmveqSS1o87npjfSbxuuLDSHwpsU · Solscan: https://solscan.io/token/2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump · pump.fun: https://pump.fun/coin/2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump · web: https://youtu.be/70K8WWdAkfo?t=4 · twitter: https://x.com/imBilngineer/status/2113708554435612825?s=20 | consulta 24/10/2026 04:56 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 24/10/2026 04:56 UTC)
- **Historia:**
  - Par creado el 23/10/2026 19:01 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 24/10/2026 04:26 UTC, con el par a 9,4 h de creado: precio $0,0004267, mcap $425.256, liquidez $70.911.
  - Velas de 1 h de GeckoTerminal (10, desde 23/10/2026 19:00 UTC): apertura $0,0006446 · máximo $0,002716 (23/10/2026 19:00 UTC) · mínimo $0,0003182 (24/10/2026 04:00 UTC) · último cierre $0,0003303.
  - En la consulta 24/10/2026 04:56 UTC: precio $0,0003409, liquidez $63.230, FDV $339.771.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 24/10/2026 04:26 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0004267 |
| Liquidez | $70.911 |
| MCap | $425.256 |
| Volumen 24 h | $12.371.907 |
| Cambio 24 h | +818% |
| Cambio m5 / h1 | +17,0% / -3,0% |
| Volumen m5 / h1 | $7.742 / $54.670 |
| Trades m5 (compras / ventas) | 56 / 47 |
| Edad del par | 9,4 h |
| Score del feed (WS) | 71 |

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

Desglose no reproducible desde los motivos registrados (suma 96 vs score 100; motivos sin regla: score de detección 100 (script_82, hace 1 min) > re-score 96: vale el de detección (paridad con script_97)): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-24T04:26:24+00:00, sin estado previo): **96** · motivos: WS score alto, MCap > $100K, Volumen masivo, Momentum corto positivo, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=16.7% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 76 de 45.562 tokens analizados (0,17%) quedan ≥ 56. Con score 96, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 24/10/2026 04:26 UTC, hasta 26/10/2026 04:26 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +17,0% · h1 -3,0% · h24 +818% · volumen m5/h1 0,14 · edad del par 9,4 h.
- **Precio de entrada** (alerta): $0,0004267.
- **Consulta 24/10/2026 04:56 UTC:** $0,0003409 (-20,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump_2026-10-24_042624.json` · blob `ee49e33e17fda1535c1925cd1758aa133ff41e60` · commit `efb3225` (2026-10-24T04:48:40Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-24_042022.json` · blob `4a5f71c706e05fbc73da21c688c08d783f8629f6` · commit `efb3225` (2026-10-24T04:48:40Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-24_042624`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump · registro · 24/10/2026 04:26 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump · HTTP 200 · 24/10/2026 04:56 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump/report · HTTP 200 · 24/10/2026 04:56 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump · HTTP 200 · 24/10/2026 04:56 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BcbQfEr3NKp8tJfbCmveqSS1o87npjfSbxuuLDSHwpsU/ohlcv/hour?limit=1000 · HTTP 200 · 24/10/2026 04:57 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump · HTTP 404 · 24/10/2026 04:57 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=YMBUSDT · HTTP 400 · 24/10/2026 04:57 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/YMB-USD · HTTP 404 · 24/10/2026 04:57 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $63.230 vs $332.172 → 80,96%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0003409 vs $0,0003303 → 3,12%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump_2026-10-24_042624.json',encoding='utf-8'));d=d.get('2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump',d);p=mock.patch('time.time',return_value=1792815984);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2TKDNLwVTbhVVy7jCvSDz6ic4REAqQshZ9n9ZTxmpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 24/10/2026 04:57 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `c5fe5c6eefc2303f…`
