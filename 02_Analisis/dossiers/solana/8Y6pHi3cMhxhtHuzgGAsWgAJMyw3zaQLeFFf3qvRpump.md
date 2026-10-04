# PrintR (PRINTR) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001003 · liquidez $30.244 · mcap $94.826 (al detectar)  
Detectado el 03/10/2026 18:44 UTC por: WS score muy alto, MCap > $50K, Volumen masivo (score 74, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 05/10/2026 18:44 UTC (< 48 h) · vigente: quedan 40,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir PRINTR

Estudio de cómo se adquiere PRINTR, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 04/10/2026 02:20 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 03/10/2026 18:44 UTC | pumpswap `BoiL8W7…fcX7` | $30.244 | 10% | 0,661% | 6,613% | 66,130% | $151 | $454 |
| consulta 04/10/2026 02:20 UTC | pumpswap `BoiL8W7…fcX7` | $29.961 | 10% | 0,668% | 6,675% | 66,753% | $150 | $449 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump`
5. Configurar el slippage: 10% (liquidez $29.961, consulta 04/10/2026 02:20 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump) y el par en DexScreener (https://dexscreener.com/solana/BoiL8W7CfhoGfjr3VHFH34GfKdkmGm7y1YyXbweLfcX7); mint authority / freeze authority: revocada / revocada · holders 6.604 · top-10 34,26% (consulta 04/10/2026 02:20 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump
- Par en DexScreener: https://dexscreener.com/solana/BoiL8W7CfhoGfjr3VHFH34GfKdkmGm7y1YyXbweLfcX7
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 6.604 · top-10 34,26% (consulta 04/10/2026 02:20 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | PrintR / PRINTR | registro de la detección (trending) |
| Mint / contrato | `8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BoiL8W7CfhoGfjr3VHFH34GfKdkmGm7y1YyXbweLfcX7` | DexScreener, al detectar (4 par(es) en la consulta 04/10/2026 02:20 UTC) |
| Deployer | `4WXd8TNVsRKNCam3p8ETDjYnjYYzbPtzmhAPkXXowunb` | RugCheck `creator` |
| Par creado | 03/10/2026 05:28 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 13,3 h / 13,3 h / 20,9 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 04/10/2026 02:20 UTC |
| Holders / top-10 | 6.604 / 34,26% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 04/10/2026 02:20 UTC |
| Holders efectivos del top-10 | 3,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 04/10/2026 02:20 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 04/10/2026 02:20 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BoiL8W7CfhoGfjr3VHFH34GfKdkmGm7y1YyXbweLfcX7 · Solscan: https://solscan.io/token/8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump · pump.fun: https://pump.fun/coin/8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump · web: https://printr.family · twitter: https://x.com/buyprintr | consulta 04/10/2026 02:20 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 04/10/2026 02:20 UTC)
- **Historia:**
  - Par creado el 03/10/2026 05:28 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 03/10/2026 18:44 UTC, con el par a 13,3 h de creado: precio $0,0001003, mcap $94.826, liquidez $30.244.
  - Velas de 1 h de GeckoTerminal (22, desde 03/10/2026 05:00 UTC): apertura $0,00004878 · máximo $0,0009138 (03/10/2026 05:00 UTC) · mínimo $0,00003937 (03/10/2026 05:00 UTC) · último cierre $0,00009571.
  - En la consulta 04/10/2026 02:20 UTC: precio $0,00009704, liquidez $29.961, FDV $91.249.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 03/10/2026 18:44 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001003 |
| Liquidez | $30.244 |
| MCap | $94.826 |
| Volumen 24 h | $2.939.344 |
| Cambio 24 h | +103% |
| Cambio m5 / h1 | -1,2% / -23,6% |
| Volumen m5 / h1 | $500 / $25.326 |
| Trades m5 (compras / ventas) | 13 / 14 |
| Edad del par | 13,3 h |
| Score del feed (WS) | 81 |

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

Desglose reconstruido desde los motivos registrados; suma 74 = score registrado 74 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 81 × 0,3 | +24,4 |
| MCap | ≥ $50K | $94.826 | +10 |
| Volumen 24 h | ≥ $1M | $2.939.344 | +20 |
| Volumen m5 | > $500 (par maduro) | $500 | +5 |
| Liquidez | ≥ $20K | $30.244 | +5 |
| Cambio 24 h | ≥ +50% | +103% | +10 |
| **Total** | recortado a 0–100 |  | **74** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-03T18:44:39+00:00, sin estado previo): **74** · motivos: WS score muy alto, MCap > $50K, Volumen masivo, Volumen moderado m5, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 11 de 10.423 tokens analizados (0,11%) quedan ≥ 56. Con score 74, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 03/10/2026 18:44 UTC, hasta 05/10/2026 18:44 UTC · vigente: quedan 40,4 h.
- **Aceleración al detectar:** cambio m5 -1,2% · h1 -23,6% · h24 +103% · volumen m5/h1 0,02 · edad del par 13,3 h.
- **Precio de entrada** (alerta): $0,0001003.
- **Consulta 04/10/2026 02:20 UTC:** $0,00009704 (-3,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump_2026-10-03_184439.json` · blob `b0a6c20e9fde707335a8ef7bf7f9dbab47586f7c` · commit `297a58b` (2026-10-04T01:37:18Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-03_183847.json` · blob `31d9fed931e020d3b59c9b1b2e10b9265e83b4ae` · commit `297a58b` (2026-10-04T01:37:18Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-03_184439`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump · registro · 03/10/2026 18:44 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump · HTTP 200 · 04/10/2026 02:20 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump/report · HTTP 200 · 04/10/2026 02:20 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump · HTTP 200 · 04/10/2026 02:20 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BoiL8W7CfhoGfjr3VHFH34GfKdkmGm7y1YyXbweLfcX7/ohlcv/hour?limit=1000 · HTTP 200 · 04/10/2026 02:20 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump · HTTP 404 · 04/10/2026 02:20 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=PRINTRUSDT · HTTP 400 · 04/10/2026 02:20 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/PRINTR-USD · HTTP 404 · 04/10/2026 02:20 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $29.961 vs $30.270 → 1,02%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00009704 vs $0,00009571 → 1,37%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump_2026-10-03_184439.json',encoding='utf-8'));d=d.get('8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump',d);p=mock.patch('time.time',return_value=1791053079);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8Y6pHi3cMhxhtHuzgGAsWgAJMyw3zaQLeFFf3qvRpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 04/10/2026 02:20 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `24e2d3040916245a…`
