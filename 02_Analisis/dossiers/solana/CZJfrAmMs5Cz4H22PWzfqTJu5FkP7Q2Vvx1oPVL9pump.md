# Agent Cat (AGENTCAT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,01543 · liquidez $385.512 · mcap $15.321.357 (al detectar)  
Detectado el 04/10/2026 22:54 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 66, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 06/10/2026 22:54 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir AGENTCAT

Estudio de cómo se adquiere AGENTCAT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 04/10/2026 23:10 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 04/10/2026 22:54 UTC | pumpswap `HyLTPac…U45o` | $385.512 | 3% | 0,052% | 0,519% | 5,188% | $1.928 | $5.783 |
| consulta 04/10/2026 23:10 UTC | pumpswap `HyLTPac…U45o` | $379.924 | 3% | 0,053% | 0,526% | 5,264% | $1.900 | $5.699 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump`
5. Configurar el slippage: 3% (liquidez $379.924, consulta 04/10/2026 23:10 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump) y el par en DexScreener (https://dexscreener.com/solana/HyLTPacbYR4V8yQw5bbWwAETZkjcsRw9xzCbayMnU45o); mint authority / freeze authority: revocada / revocada · holders 4.141 · top-10 3,82% (consulta 04/10/2026 23:10 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump
- Par en DexScreener: https://dexscreener.com/solana/HyLTPacbYR4V8yQw5bbWwAETZkjcsRw9xzCbayMnU45o
- Página del lanzamiento (pump.fun): https://pump.fun/coin/CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.141 · top-10 3,82% (consulta 04/10/2026 23:10 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Agent Cat / AGENTCAT | registro de la detección (trending) |
| Mint / contrato | `CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HyLTPacbYR4V8yQw5bbWwAETZkjcsRw9xzCbayMnU45o` | DexScreener, al detectar (1 par(es) en la consulta 04/10/2026 23:10 UTC) |
| Deployer | `cJSgF6az6m8pnU45AeBpoDJhbYYz4xqAjbVzGeZoFUw` | RugCheck `creator` |
| Par creado | 03/10/2026 22:52 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 24,0 h / 24,0 h / 24,3 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 04/10/2026 23:10 UTC |
| Holders / top-10 | 4.141 / 3,82% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 04/10/2026 23:10 UTC |
| Holders efectivos del top-10 | 6,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 04/10/2026 23:10 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 04/10/2026 23:10 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HyLTPacbYR4V8yQw5bbWwAETZkjcsRw9xzCbayMnU45o · Solscan: https://solscan.io/token/CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump · pump.fun: https://pump.fun/coin/CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump · web: https://agentcat.lol/ · twitter: https://x.com/AgentCat_Sol | consulta 04/10/2026 23:10 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 04/10/2026 23:10 UTC)
- **Historia:**
  - Par creado el 03/10/2026 22:52 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 04/10/2026 22:54 UTC, con el par a 24,0 h de creado: precio $0,01543, mcap $15.321.357, liquidez $385.512.
  - Velas de 1 h de GeckoTerminal (26, desde 03/10/2026 22:00 UTC): apertura $0,0002612 · máximo $0,01790 (04/10/2026 22:00 UTC) · mínimo $0,00008669 (03/10/2026 22:00 UTC) · último cierre $0,01498.
  - En la consulta 04/10/2026 23:10 UTC: precio $0,01498, liquidez $379.924, FDV $14.873.489.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 04/10/2026 22:54 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,01543 |
| Liquidez | $385.512 |
| MCap | $15.321.357 |
| Volumen 24 h | $4.235.277 |
| Cambio 24 h | +5.541% |
| Cambio m5 / h1 | -4,7% / +9,6% |
| Volumen m5 / h1 | $24.097 / $438.968 |
| Trades m5 (compras / ventas) | 70 / 39 |
| Edad del par | 24,0 h |
| Score del feed (WS) | 89 |

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

Desglose reconstruido desde los motivos registrados; suma 66 = score registrado 66 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 89 × 0,3 | +26,6 |
| MCap | ≥ $1M | $15.321.357 | +25 |
| Volumen 24 h | ≥ $1M | $4.235.277 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 64% | +25 |
| Volumen m5 | > $1K (par maduro) | $24.097 | +10 |
| Par viejo | edad > 24 h | edad 24,0 h | -50 |
| Liquidez | ≥ $100K | $385.512 | +15 |
| Cambio 24 h | ≥ +50% | +5.541% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap < 3% | +5.541% · liq/mcap 2,5% | -15 |
| **Total** | recortado a 0–100 |  | **66** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-04T22:54:02+00:00, sin estado previo): **66** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Par >24h, no nativo pump.fun, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=2.5% <3%.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 13 de 10.912 tokens analizados (0,12%) quedan ≥ 56. Con score 66, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 04/10/2026 22:54 UTC, hasta 06/10/2026 22:54 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -4,7% · h1 +9,6% · h24 +5.541% · volumen m5/h1 0,05 · edad del par 24,0 h.
- **Precio de entrada** (alerta): $0,01543.
- **Consulta 04/10/2026 23:10 UTC:** $0,01498 (-2,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump_2026-10-04_225402.json` · blob `ac8c94dd3140720390f08538af3ae8712459fb91` · commit `6e3fd9b` (2026-10-04T23:04:22Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-04_224801.json` · blob `eff7a5c48d5a77007353dee9ebfe284069c08bc4` · commit `6e3fd9b` (2026-10-04T23:04:22Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-04_225402`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump · registro · 04/10/2026 22:54 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump · HTTP 200 · 04/10/2026 23:10 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump/report · HTTP 200 · 04/10/2026 23:10 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump · HTTP 200 · 04/10/2026 23:10 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HyLTPacbYR4V8yQw5bbWwAETZkjcsRw9xzCbayMnU45o/ohlcv/hour?limit=1000 · HTTP 200 · 04/10/2026 23:10 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump · HTTP 404 · 04/10/2026 23:10 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AGENTCATUSDT · HTTP 400 · 04/10/2026 23:10 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AGENTCAT-USD · HTTP 404 · 04/10/2026 23:10 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $379.924 vs $380.381 → 0,12%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,01498 vs $0,01498 → 0,00%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump_2026-10-04_225402.json',encoding='utf-8'));d=d.get('CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump',d);p=mock.patch('time.time',return_value=1791154442);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint CZJfrAmMs5Cz4H22PWzfqTJu5FkP7Q2Vvx1oPVL9pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 04/10/2026 23:10 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `14c0a5be7d3d9067…`
