# Shamonda Virus Coin (SHAVCOIN) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003584 · liquidez $174.352 · mcap $3.533.649 (al detectar)  
Detectado el 23/10/2026 01:58 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 99, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 25/10/2026 01:58 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SHAVCOIN

Estudio de cómo se adquiere SHAVCOIN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 23/10/2026 02:26 UTC; CoinGecko sin pares de este contrato en esos exchanges).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 23/10/2026 01:58 UTC | pumpswap `HfT2fJj…dTDt` | $174.352 | 5% | 0,115% | 1,147% | 11,471% | $872 | $2.615 |
| consulta 23/10/2026 02:25 UTC | pumpswap `HfT2fJj…dTDt` | $169.726 | 5% | 0,118% | 1,178% | 11,784% | $849 | $2.546 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump`
5. Configurar el slippage: 5% (liquidez $169.726, consulta 23/10/2026 02:25 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump) y el par en DexScreener (https://dexscreener.com/solana/HfT2fJjb1SmDsdjHbCkJuvnVdzDSY1525j4rhYXwdTDt); mint authority / freeze authority: revocada / revocada · holders 8.973 · top-10 3,71% (consulta 23/10/2026 02:25 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump
- Par en DexScreener: https://dexscreener.com/solana/HfT2fJjb1SmDsdjHbCkJuvnVdzDSY1525j4rhYXwdTDt
- Página del lanzamiento (pump.fun): https://pump.fun/coin/Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 8.973 · top-10 3,71% (consulta 23/10/2026 02:25 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Shamonda Virus Coin / SHAVCOIN | registro de la detección (trending) |
| Mint / contrato | `Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HfT2fJjb1SmDsdjHbCkJuvnVdzDSY1525j4rhYXwdTDt` | DexScreener, al detectar (2 par(es) en la consulta 23/10/2026 02:25 UTC) |
| Deployer | `9jjtmvTFXCcGhetvXed9vKfYGQ1JxGcnPDnSMenvNMf6` | RugCheck `creator` |
| Par creado | 22/10/2026 11:38 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 14,3 h / 14,3 h / 14,8 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 23/10/2026 02:25 UTC |
| Holders / top-10 | 8.973 / 3,71% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 23/10/2026 02:25 UTC |
| Holders efectivos del top-10 | 2,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 23/10/2026 02:25 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 23/10/2026 02:25 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HfT2fJjb1SmDsdjHbCkJuvnVdzDSY1525j4rhYXwdTDt · Solscan: https://solscan.io/token/Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump · pump.fun: https://pump.fun/coin/Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump · web: https://theshavcoin.site · twitter: https://x.com/theshavcoin | consulta 23/10/2026 02:25 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** CoinGecko: Solana Ecosystem, Pump.fun Ecosystem · scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 23/10/2026 02:25 UTC)
- **Historia:**
  - Par creado el 22/10/2026 11:38 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 23/10/2026 01:58 UTC, con el par a 14,3 h de creado: precio $0,003584, mcap $3.533.649, liquidez $174.352.
  - Velas de 1 h de GeckoTerminal (16, desde 22/10/2026 11:00 UTC): apertura $0,0001438 · máximo $0,004393 (22/10/2026 18:00 UTC) · mínimo $0,00004577 (22/10/2026 11:00 UTC) · último cierre $0,003390.
  - En la consulta 23/10/2026 02:25 UTC: precio $0,003398, liquidez $169.726, FDV $3.350.285.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 23/10/2026 01:58 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003584 |
| Liquidez | $174.352 |
| MCap | $3.533.649 |
| Volumen 24 h | $3.423.011 |
| Cambio 24 h | +7.679% |
| Cambio m5 / h1 | -1,4% / +1,6% |
| Volumen m5 / h1 | $5.506 / $69.965 |
| Trades m5 (compras / ventas) | 40 / 96 |
| Edad del par | 14,3 h |
| Score del feed (WS) | 66 |

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

Desglose no reproducible desde los motivos registrados (suma 79 vs score 99; motivos sin regla: score de detección 99 (script_82, hace 1 min) > re-score 79: vale el de detección (paridad con script_97)): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-23T01:58:14+00:00, sin estado previo): **79** · motivos: WS score alto, MCap > $1M, Volumen masivo, Volumen activo m5 (>$1K), Venta dominante (buy_pressure <40%), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.9% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 75 de 44.469 tokens analizados (0,17%) quedan ≥ 56. Con score 79, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 23/10/2026 01:58 UTC, hasta 25/10/2026 01:58 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -1,4% · h1 +1,6% · h24 +7.679% · volumen m5/h1 0,08 · edad del par 14,3 h.
- **Precio de entrada** (alerta): $0,003584.
- **Consulta 23/10/2026 02:25 UTC:** $0,003398 (-5,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump_2026-10-23_015814.json` · blob `1fb38462ee436b84063e60abe96b2fc011dfc275` · commit `5a28236` (2026-10-23T02:18:13Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-23_015149.json` · blob `823a35f6a1749462b03ae05a440cb51f04c63a24` · commit `5a28236` (2026-10-23T02:18:13Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-23_015814`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump · registro · 23/10/2026 01:58 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump · HTTP 200 · 23/10/2026 02:25 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump/report · HTTP 200 · 23/10/2026 02:25 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump · HTTP 200 · 23/10/2026 02:26 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HfT2fJjb1SmDsdjHbCkJuvnVdzDSY1525j4rhYXwdTDt/ohlcv/hour?limit=1000 · HTTP 200 · 23/10/2026 02:26 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump · HTTP 200 · 23/10/2026 02:26 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SHAVCOINUSDT · HTTP 400 · 23/10/2026 02:26 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SHAVCOIN-USD · HTTP 404 · 23/10/2026 02:26 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $169.726 vs $169.995 → 0,16%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003398 vs $0,003390 → 0,24%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump_2026-10-23_015814.json',encoding='utf-8'));d=d.get('Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump',d);p=mock.patch('time.time',return_value=1792720694);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint Baw61KXAJk4MMnNJPBa87S8F77oNhMy7gQ63S8SLpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 23/10/2026 02:26 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `9ad22f3192bc0a3d…`
