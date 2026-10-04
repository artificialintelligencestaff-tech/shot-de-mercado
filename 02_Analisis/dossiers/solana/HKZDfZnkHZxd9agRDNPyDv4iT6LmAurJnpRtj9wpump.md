# Make No Mistakes (MISTAKE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,006930 · liquidez $293.787 · mcap $6.673.860 (al detectar)  
Detectado el 04/10/2026 15:04 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 69, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 06/10/2026 15:04 UTC (< 48 h) · vigente: quedan 44,1 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir MISTAKE

Estudio de cómo se adquiere MISTAKE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 04/10/2026 18:57 UTC; CoinGecko sin pares de este contrato en esos exchanges).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 04/10/2026 15:04 UTC | pumpswap `867dKva…BdAD` | $293.787 | 3% | 0,068% | 0,681% | 6,808% | $1.469 | $4.407 |
| consulta 04/10/2026 18:57 UTC | pumpswap `867dKva…BdAD` | $282.044 | 3% | 0,071% | 0,709% | 7,091% | $1.410 | $4.231 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump`
5. Configurar el slippage: 3% (liquidez $282.044, consulta 04/10/2026 18:57 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump) y el par en DexScreener (https://dexscreener.com/solana/867dKvaCcyRrUDP66bqNXbujXfjaxsNB9wTpc4CmBdAD); mint authority / freeze authority: revocada / revocada · holders 30.790 · top-10 7,44% (consulta 04/10/2026 18:57 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump
- Par en DexScreener: https://dexscreener.com/solana/867dKvaCcyRrUDP66bqNXbujXfjaxsNB9wTpc4CmBdAD
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 30.790 · top-10 7,44% (consulta 04/10/2026 18:57 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Make No Mistakes / MISTAKE | registro de la detección (trending) |
| Mint / contrato | `HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `867dKvaCcyRrUDP66bqNXbujXfjaxsNB9wTpc4CmBdAD` | DexScreener, al detectar (1 par(es) en la consulta 04/10/2026 18:57 UTC) |
| Deployer | `HCaSn7L2LJSbSviN7vp2HXLc7v9Gost83ZSy8u5ekbhR` | RugCheck `creator` |
| Par creado | 11/09/2026 02:19 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 23,5 días / 23,5 días / 23,7 días | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 04/10/2026 18:57 UTC |
| Holders / top-10 | 30.790 / 7,44% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 04/10/2026 18:57 UTC |
| Holders efectivos del top-10 | 6,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 04/10/2026 18:57 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 04/10/2026 18:57 UTC |
| Links | DexScreener: https://dexscreener.com/solana/867dKvaCcyRrUDP66bqNXbujXfjaxsNB9wTpc4CmBdAD · Solscan: https://solscan.io/token/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump · pump.fun: https://pump.fun/coin/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump · web: https://mistakes.fun/ · twitter: https://x.com/nomistakesfun | consulta 04/10/2026 18:57 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** CoinGecko: Solana Ecosystem, Meme, Solana Meme, Pump.fun Ecosystem
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 04/10/2026 18:57 UTC)
- **Historia:**
  - Par creado el 11/09/2026 02:19 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 04/10/2026 15:04 UTC, con el par a 23,5 días de creado: precio $0,006930, mcap $6.673.860, liquidez $293.787.
  - Velas de 1 h de GeckoTerminal (569, desde 11/09/2026 02:00 UTC): apertura $0,00005736 · máximo $0,02603 (04/10/2026 06:00 UTC) · mínimo $0,00004042 (11/09/2026 02:00 UTC) · último cierre $0,006430.
  - En la consulta 04/10/2026 18:57 UTC: precio $0,006379, liquidez $282.044, FDV $6.143.716.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 04/10/2026 15:04 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,006930 |
| Liquidez | $293.787 |
| MCap | $6.673.860 |
| Volumen 24 h | $11.970.545 |
| Cambio 24 h | +69% |
| Cambio m5 / h1 | -3,1% / -12,8% |
| Volumen m5 / h1 | $46.895 / $308.534 |
| Trades m5 (compras / ventas) | 62 / 43 |
| Edad del par | 23,5 días |
| Score del feed (WS) | 80 |

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

Desglose no reproducible desde los motivos registrados (suma 68 vs score 69; motivos sin regla: Anticipación (lib_early_signals early-0.2): +1 — volume_acceleration: vol 5 min ×1.8 la tasa horaria → +0.39; buy_pressure_shift: compras 59% en 5 min vs 47% en 1 h → +0.9): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-04T15:04:56+00:00, sin estado previo): **68** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >55%, Volumen activo m5 (>$1K), Par >24h, no nativo pump.fun, Liquidez alta, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 13 de 10.601 tokens analizados (0,12%) quedan ≥ 56. Con score 68, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 04/10/2026 15:04 UTC, hasta 06/10/2026 15:04 UTC · vigente: quedan 44,1 h.
- **Aceleración al detectar:** cambio m5 -3,1% · h1 -12,8% · h24 +69% · volumen m5/h1 0,15 · edad del par 23,5 días.
- **Precio de entrada** (alerta): $0,006930.
- **Consulta 04/10/2026 18:57 UTC:** $0,006379 (-8,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump_2026-10-04_150456.json` · blob `46336e452ffd65a28824d226de9571b8c2441334` · commit `281cac2` (2026-10-04T18:50:20Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-04_150456`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump · registro · 04/10/2026 15:04 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump · HTTP 200 · 04/10/2026 18:57 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump/report · HTTP 200 · 04/10/2026 18:57 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump · HTTP 200 · 04/10/2026 18:57 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/867dKvaCcyRrUDP66bqNXbujXfjaxsNB9wTpc4CmBdAD/ohlcv/hour?limit=1000 · HTTP 200 · 04/10/2026 18:57 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump · HTTP 200 · 04/10/2026 18:57 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MISTAKEUSDT · HTTP 400 · 04/10/2026 18:57 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MISTAKE-USD · HTTP 404 · 04/10/2026 18:57 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $282.044 vs $283.555 → 0,53%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,006379 vs $0,006430 → 0,80%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump_2026-10-04_150456.json',encoding='utf-8'));d=d.get('HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump',d);p=mock.patch('time.time',return_value=1791126296);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 04/10/2026 18:57 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `46dd326f62dde87a…`
