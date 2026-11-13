# Jensen Huang (Huang) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00008231 · liquidez $24.281 · mcap $79.188 (al detectar)  
Detectado el 13/11/2026 07:18 UTC por: WS score alto, MCap > $50K, Volumen masivo (score 64, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 15/11/2026 07:18 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Huang

Estudio de cómo se adquiere Huang, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 13/11/2026 07:18 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 13/11/2026 07:18 UTC | pumpswap `FJ1Y3dr…CN2u` | $24.281 | 10% | 0,824% | 8,237% | 82,368% | $121 | $364 |
| consulta 13/11/2026 07:18 UTC | pumpswap `FJ1Y3dr…CN2u` | $24.281 | 10% | 0,824% | 8,237% | 82,368% | $121 | $364 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump`
5. Configurar el slippage: 10% (liquidez $24.281, consulta 13/11/2026 07:18 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump) y el par en DexScreener (https://dexscreener.com/solana/FJ1Y3drK5Z715mj8Hk512ekk3rQhTAhgRv6HMhnPCN2u); mint authority / freeze authority: revocada / revocada · holders 8.051 · top-10 29,76% (consulta 13/11/2026 07:18 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump
- Par en DexScreener: https://dexscreener.com/solana/FJ1Y3drK5Z715mj8Hk512ekk3rQhTAhgRv6HMhnPCN2u
- Página del lanzamiento (pump.fun): https://pump.fun/coin/4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 8.051 · top-10 29,76% (consulta 13/11/2026 07:18 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Jensen Huang / Huang | registro de la detección (trending) |
| Mint / contrato | `4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `FJ1Y3drK5Z715mj8Hk512ekk3rQhTAhgRv6HMhnPCN2u` | DexScreener, al detectar (30 par(es) en la consulta 13/11/2026 07:18 UTC) |
| Deployer | `FWcq8yXR6agnDw3mynHnExLbVULL4wgT9qz23o1esGHj` | RugCheck `creator` |
| Par creado | 12/11/2026 14:33 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 16,8 h / 16,8 h / 16,8 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 13/11/2026 07:18 UTC |
| Holders / top-10 | 8.051 / 29,76% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 13/11/2026 07:18 UTC |
| Holders efectivos del top-10 | 3,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; orca 0%; orca 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 13/11/2026 07:18 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 13/11/2026 07:18 UTC |
| Links | DexScreener: https://dexscreener.com/solana/FJ1Y3drK5Z715mj8Hk512ekk3rQhTAhgRv6HMhnPCN2u · Solscan: https://solscan.io/token/4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump · pump.fun: https://pump.fun/coin/4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump · twitter: https://x.com/humanevolvd/status/2120884915298333116?a=u1Fq0pa10onzUmsLl9c&s=46 | consulta 13/11/2026 07:18 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 13/11/2026 07:18 UTC)
- **Historia:**
  - Par creado el 12/11/2026 14:33 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 13/11/2026 07:18 UTC, con el par a 16,8 h de creado: precio $0,00008231, mcap $79.188, liquidez $24.281.
  - Velas de 1 h de GeckoTerminal (18, desde 12/11/2026 14:00 UTC): apertura $0,00003216 · máximo $0,0008228 (12/11/2026 15:00 UTC) · mínimo $0,00001766 (12/11/2026 14:00 UTC) · último cierre $0,00008219.
  - En la consulta 13/11/2026 07:18 UTC: precio $0,00008231, liquidez $24.281, FDV $79.188.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 13/11/2026 07:18 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00008231 |
| Liquidez | $24.281 |
| MCap | $79.188 |
| Volumen 24 h | $3.761.160 |
| Cambio 24 h | +158% |
| Cambio m5 / h1 | -0,5% / -2,5% |
| Volumen m5 / h1 | $333 / $11.380 |
| Trades m5 (compras / ventas) | 7 / 7 |
| Edad del par | 16,8 h |
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

Desglose reconstruido desde los motivos registrados; suma 64 = score registrado 64 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 66 × 0,3 | +19,9 |
| MCap | ≥ $50K | $79.188 | +10 |
| Volumen 24 h | ≥ $1M | $3.761.160 | +20 |
| Liquidez | ≥ $20K | $24.281 | +5 |
| Cambio 24 h | ≥ +50% | +158% | +10 |
| **Total** | recortado a 0–100 |  | **64** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-13T07:18:27+00:00, sin estado previo): **64** · motivos: WS score alto, MCap > $50K, Volumen masivo, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 99 de 47.131 tokens analizados (0,21%) quedan ≥ 56. Con score 64, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 13/11/2026 07:18 UTC, hasta 15/11/2026 07:18 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -0,5% · h1 -2,5% · h24 +158% · volumen m5/h1 0,03 · edad del par 16,8 h.
- **Precio de entrada** (alerta): $0,00008231.
- **Consulta 13/11/2026 07:18 UTC:** $0,00008231 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump_2026-11-13_071837.json` · blob `192cc5938e554ff9d3cdca83efde985eb19f8c22` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-13_071325.json` · blob `82fa3281f4afa8a83977918cdb8e53e11d3e6d5c` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-13_071837`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump · registro · 13/11/2026 07:18 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump · HTTP 200 · 13/11/2026 07:18 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump/report · HTTP 200 · 13/11/2026 07:18 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump · HTTP 200 · 13/11/2026 07:18 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/FJ1Y3drK5Z715mj8Hk512ekk3rQhTAhgRv6HMhnPCN2u/ohlcv/hour?limit=1000 · HTTP 200 · 13/11/2026 07:18 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump · HTTP 404 · 13/11/2026 07:18 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HUANGUSDT · HTTP 400 · 13/11/2026 07:18 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HUANG-USD · HTTP 404 · 13/11/2026 07:18 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $24.281 vs $24.345 → 0,26%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00008231 vs $0,00008219 → 0,14%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump_2026-11-13_071837.json',encoding='utf-8'));d=d.get('4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump',d);p=mock.patch('time.time',return_value=1794554307);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 13/11/2026 07:18 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `80e4a14b784e8f2d…`
