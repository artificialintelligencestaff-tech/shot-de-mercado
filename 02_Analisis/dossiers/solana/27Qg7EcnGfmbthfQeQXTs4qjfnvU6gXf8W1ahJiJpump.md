# President 2028 (ELON2028) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0003750 · liquidez $55.414 · mcap $372.861 (al detectar)  
Detectado el 27/10/2026 10:45 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 29/10/2026 10:45 UTC (< 48 h) · vigente: quedan 42,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ELON2028

Estudio de cómo se adquiere ELON2028, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 27/10/2026 16:06 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 27/10/2026 10:45 UTC | pumpswap `6jEdE2E…yPDg` | $55.414 | 5% | 0,361% | 3,609% | 36,092% | $277 | $831 |
| consulta 27/10/2026 16:06 UTC | pumpswap `6jEdE2E…yPDg` | $26.699 | 10% | 0,749% | 7,491% | 74,910% | $133 | $400 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump`
5. Configurar el slippage: 10% (liquidez $26.699, consulta 27/10/2026 16:06 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump) y el par en DexScreener (https://dexscreener.com/solana/6jEdE2E3c6J7snnq9vTbLLuz2WsYi7rX5oVvWy8HyPDg); mint authority / freeze authority: revocada / revocada · holders 3.754 · top-10 19,15% (consulta 27/10/2026 16:06 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump
- Par en DexScreener: https://dexscreener.com/solana/6jEdE2E3c6J7snnq9vTbLLuz2WsYi7rX5oVvWy8HyPDg
- Página del lanzamiento (pump.fun): https://pump.fun/coin/27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.754 · top-10 19,15% (consulta 27/10/2026 16:06 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | President 2028 / ELON2028 | registro de la detección (trending) |
| Mint / contrato | `27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6jEdE2E3c6J7snnq9vTbLLuz2WsYi7rX5oVvWy8HyPDg` | DexScreener, al detectar (7 par(es) en la consulta 27/10/2026 16:06 UTC) |
| Deployer | `C8wzzZYVmGoPNj2nJFsc5K3ykgSDgfkWmAKm8xP4watx` | RugCheck `creator` |
| Par creado | 27/10/2026 00:06 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,6 h / 10,6 h / 16,0 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 27/10/2026 16:06 UTC |
| Holders / top-10 | 3.754 / 19,15% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 27/10/2026 16:06 UTC |
| Holders efectivos del top-10 | 1,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; raydium_clmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 27/10/2026 16:06 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 27/10/2026 16:06 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6jEdE2E3c6J7snnq9vTbLLuz2WsYi7rX5oVvWy8HyPDg · Solscan: https://solscan.io/token/27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump · pump.fun: https://pump.fun/coin/27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump · web: https://elon2028.fun · twitter: https://x.com/President2028X | consulta 27/10/2026 16:06 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 27/10/2026 16:06 UTC)
- **Historia:**
  - Par creado el 27/10/2026 00:06 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 27/10/2026 10:45 UTC, con el par a 10,6 h de creado: precio $0,0003750, mcap $372.861, liquidez $55.414.
  - Velas de 1 h de GeckoTerminal (17, desde 27/10/2026 00:00 UTC): apertura $0,0003216 · máximo $0,002293 (27/10/2026 01:00 UTC) · mínimo $0,00001801 (27/10/2026 00:00 UTC) · último cierre $0,00008897.
  - En la consulta 27/10/2026 16:06 UTC: precio $0,00008739, liquidez $26.699, FDV $86.886.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 27/10/2026 10:45 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0003750 |
| Liquidez | $55.414 |
| MCap | $372.861 |
| Volumen 24 h | $4.196.884 |
| Cambio 24 h | +576% |
| Cambio m5 / h1 | -8,5% / -7,6% |
| Volumen m5 / h1 | $12.988 / $150.899 |
| Trades m5 (compras / ventas) | 464 / 188 |
| Edad del par | 10,6 h |
| Score del feed (WS) | 70 |

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
| Score del feed | score WS × 0,3 | WS 70 × 0,3 | +21,1 |
| MCap | ≥ $100K | $372.861 | +15 |
| Volumen 24 h | ≥ $1M | $4.196.884 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 71% | +25 |
| Volumen m5 | > $1K (par maduro) | $12.988 | +10 |
| Liquidez | ≥ $50K | $55.414 | +10 |
| Cambio 24 h | ≥ +50% | +576% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +576% · liq/mcap 14,9% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-27T10:45:05+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=14.9% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 79 de 46.077 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 27/10/2026 10:45 UTC, hasta 29/10/2026 10:45 UTC · vigente: quedan 42,6 h.
- **Aceleración al detectar:** cambio m5 -8,5% · h1 -7,6% · h24 +576% · volumen m5/h1 0,09 · edad del par 10,6 h.
- **Precio de entrada** (alerta): $0,0003750.
- **Consulta 27/10/2026 16:06 UTC:** $0,00008739 (-76,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump_2026-10-27_104505.json` · blob `1ede777f64a1d26526dc7ee2294a1678dc21921e` · commit `38d707a` (2026-10-27T15:35:52Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-27_103904.json` · blob `bd6dbfee3a55c3e826cfdc6cc9d1115a60c575b2` · commit `38d707a` (2026-10-27T15:35:52Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-27_104505`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump · registro · 27/10/2026 10:45 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump · HTTP 200 · 27/10/2026 16:06 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump/report · HTTP 200 · 27/10/2026 16:06 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump · HTTP 200 · 27/10/2026 16:06 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6jEdE2E3c6J7snnq9vTbLLuz2WsYi7rX5oVvWy8HyPDg/ohlcv/hour?limit=1000 · HTTP 200 · 27/10/2026 16:06 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump · HTTP 404 · 27/10/2026 16:06 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ELON2028USDT · HTTP 400 · 27/10/2026 16:06 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ELON2028-USD · HTTP 404 · 27/10/2026 16:06 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $26.699 vs $27.152 → 1,67%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00008739 vs $0,00008897 → 1,77%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump_2026-10-27_104505.json',encoding='utf-8'));d=d.get('27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump',d);p=mock.patch('time.time',return_value=1793097905);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 27/10/2026 16:06 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `39584efcd56bb149…`
