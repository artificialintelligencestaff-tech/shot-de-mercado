# imanuel mucron (mucron) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001696 · liquidez $38.705 · mcap $161.590 (al detectar)  
Detectado el 18/10/2026 22:18 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 20/10/2026 22:18 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir mucron

Estudio de cómo se adquiere mucron, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 18/10/2026 22:48 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 18/10/2026 22:18 UTC | pumpswap `Af7W724…gbFA` | $38.705 | 10% | 0,517% | 5,167% | 51,673% | $194 | $581 |
| consulta 18/10/2026 22:47 UTC | pumpswap `Af7W724…gbFA` | $42.324 | 10% | 0,473% | 4,725% | 47,255% | $212 | $635 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump`
5. Configurar el slippage: 10% (liquidez $42.324, consulta 18/10/2026 22:47 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump) y el par en DexScreener (https://dexscreener.com/solana/Af7W724Kw2A7Z5PbaCAS6RNQ8ubiKEWqiSa715bxgbFA); mint authority / freeze authority: revocada / revocada · holders 12.625 · top-10 30,32% (consulta 18/10/2026 22:47 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump
- Par en DexScreener: https://dexscreener.com/solana/Af7W724Kw2A7Z5PbaCAS6RNQ8ubiKEWqiSa715bxgbFA
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 12.625 · top-10 30,32% (consulta 18/10/2026 22:47 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | imanuel mucron / mucron | registro de la detección (trending) |
| Mint / contrato | `3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Af7W724Kw2A7Z5PbaCAS6RNQ8ubiKEWqiSa715bxgbFA` | DexScreener, al detectar (30 par(es) en la consulta 18/10/2026 22:47 UTC) |
| Deployer | `Aiby3GTyV17PrBLHGYdUHvcb74VRtcoMuRew2aVj4Mh8` | RugCheck `creator` |
| Par creado | 18/10/2026 09:15 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 13,1 h / 13,1 h / 13,5 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 18/10/2026 22:47 UTC |
| Holders / top-10 | 12.625 / 30,32% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 18/10/2026 22:47 UTC |
| Holders efectivos del top-10 | 4,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; manifest 0%; meteoraDlmm 0%; manifest 0%; manifest 0%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 18/10/2026 22:47 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 18/10/2026 22:47 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Af7W724Kw2A7Z5PbaCAS6RNQ8ubiKEWqiSa715bxgbFA · Solscan: https://solscan.io/token/3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump · pump.fun: https://pump.fun/coin/3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump · twitter: https://x.com/i/communities/2023470860154143026 | consulta 18/10/2026 22:47 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 18/10/2026 22:47 UTC)
- **Historia:**
  - Par creado el 18/10/2026 09:15 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 18/10/2026 22:18 UTC, con el par a 13,1 h de creado: precio $0,0001696, mcap $161.590, liquidez $38.705.
  - Velas de 1 h de GeckoTerminal (14, desde 18/10/2026 09:00 UTC): apertura $0,00004303 · máximo $0,001221 (18/10/2026 13:00 UTC) · mínimo $0,00003091 (18/10/2026 09:00 UTC) · último cierre $0,0001952.
  - En la consulta 18/10/2026 22:47 UTC: precio $0,0002002, liquidez $42.324, FDV $190.826.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 18/10/2026 22:18 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001696 |
| Liquidez | $38.705 |
| MCap | $161.590 |
| Volumen 24 h | $4.277.235 |
| Cambio 24 h | +295% |
| Cambio m5 / h1 | +0,8% / -3,5% |
| Volumen m5 / h1 | $1.972 / $31.098 |
| Trades m5 (compras / ventas) | 22 / 21 |
| Edad del par | 13,1 h |
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

Desglose no reproducible desde los motivos registrados (suma 91 vs score 100; motivos sin regla: score de detección 100 (script_82, hace 1 min) > re-score 91: vale el de detección (paridad con script_97)): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-18T22:18:57+00:00, sin estado previo): **91** · motivos: WS score alto, MCap > $100K, Volumen masivo, Momentum corto positivo, Volumen activo m5 (>$1K), Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 65 de 40.192 tokens analizados (0,16%) quedan ≥ 56. Con score 91, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 18/10/2026 22:18 UTC, hasta 20/10/2026 22:18 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +0,8% · h1 -3,5% · h24 +295% · volumen m5/h1 0,06 · edad del par 13,1 h.
- **Precio de entrada** (alerta): $0,0001696.
- **Consulta 18/10/2026 22:47 UTC:** $0,0002002 (+18,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump_2026-10-18_221857.json` · blob `51277bf7c95ecf3e936cfe62c3b35c325c994dfe` · commit `e912c64` (2026-10-18T22:37:49Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-18_221250.json` · blob `75f43ab56e78a4984bcd74d959d618d9ddb87756` · commit `e912c64` (2026-10-18T22:37:49Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-18_221857`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump · registro · 18/10/2026 22:18 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump · HTTP 200 · 18/10/2026 22:47 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump/report · HTTP 200 · 18/10/2026 22:47 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump · HTTP 200 · 18/10/2026 22:47 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Af7W724Kw2A7Z5PbaCAS6RNQ8ubiKEWqiSa715bxgbFA/ohlcv/hour?limit=1000 · HTTP 200 · 18/10/2026 22:47 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump · HTTP 404 · 18/10/2026 22:47 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MUCRONUSDT · HTTP 400 · 18/10/2026 22:48 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MUCRON-USD · HTTP 404 · 18/10/2026 22:48 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $42.324 vs $56.181 → 24,66%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0002002 vs $0,0001952 → 2,48%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump_2026-10-18_221857.json',encoding='utf-8'));d=d.get('3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump',d);p=mock.patch('time.time',return_value=1792361937);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3A3qjns31YZA6Ung91ZpoPD7J3p1bDFbTJ4ANFAPpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 18/10/2026 22:48 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `435885d336cd0a2f…`
