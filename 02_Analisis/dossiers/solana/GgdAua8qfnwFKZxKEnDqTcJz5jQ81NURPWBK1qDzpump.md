# Purrsword (PURRSWORD) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0004124 · liquidez $63.628 · mcap $408.676 (al detectar)  
Detectado el 04/10/2026 02:21 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 06/10/2026 02:21 UTC (< 48 h) · vigente: quedan 46,1 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir PURRSWORD

Estudio de cómo se adquiere PURRSWORD, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 04/10/2026 04:14 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 04/10/2026 02:21 UTC | pumpswap `6LPvVdH…qkn7` | $63.628 | 5% | 0,314% | 3,143% | 31,433% | $318 | $954 |
| consulta 04/10/2026 04:14 UTC | pumpswap `6LPvVdH…qkn7` | $59.968 | 5% | 0,334% | 3,335% | 33,351% | $300 | $900 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump`
5. Configurar el slippage: 5% (liquidez $59.968, consulta 04/10/2026 04:14 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump) y el par en DexScreener (https://dexscreener.com/solana/6LPvVdHuSFBfgC5Dtx6QKUgzo6d9brJhqNhCBpQZqkn7); mint authority / freeze authority: revocada / revocada · holders 14.259 · top-10 11,11% (consulta 04/10/2026 04:14 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump
- Par en DexScreener: https://dexscreener.com/solana/6LPvVdHuSFBfgC5Dtx6QKUgzo6d9brJhqNhCBpQZqkn7
- Página del lanzamiento (pump.fun): https://pump.fun/coin/GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 14.259 · top-10 11,11% (consulta 04/10/2026 04:14 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Purrsword / PURRSWORD | registro de la detección (trending) |
| Mint / contrato | `GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6LPvVdHuSFBfgC5Dtx6QKUgzo6d9brJhqNhCBpQZqkn7` | DexScreener, al detectar (2 par(es) en la consulta 04/10/2026 04:14 UTC) |
| Deployer | `EmC1au79VPDxYBAasP51yJ45cErExubm9HhwfE3t5CXr` | RugCheck `creator` |
| Par creado | 03/10/2026 14:21 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 12,0 h / 12,0 h / 13,9 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 04/10/2026 04:14 UTC |
| Holders / top-10 | 14.259 / 11,11% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 04/10/2026 04:14 UTC |
| Holders efectivos del top-10 | 1,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 04/10/2026 04:14 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 04/10/2026 04:14 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6LPvVdHuSFBfgC5Dtx6QKUgzo6d9brJhqNhCBpQZqkn7 · Solscan: https://solscan.io/token/GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump · pump.fun: https://pump.fun/coin/GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump · web: https://www.purrsword.site · twitter: https://x.com/purrsword | consulta 04/10/2026 04:14 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 04/10/2026 04:14 UTC)
- **Historia:**
  - Par creado el 03/10/2026 14:21 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 04/10/2026 02:21 UTC, con el par a 12,0 h de creado: precio $0,0004124, mcap $408.676, liquidez $63.628.
  - Velas de 1 h de GeckoTerminal (15, desde 03/10/2026 14:00 UTC): apertura $0,0001431 · máximo $0,001205 (03/10/2026 20:00 UTC) · mínimo $0,00006608 (03/10/2026 14:00 UTC) · último cierre $0,0003530.
  - En la consulta 04/10/2026 04:14 UTC: precio $0,0003560, liquidez $59.968, FDV $352.805.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 04/10/2026 02:21 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0004124 |
| Liquidez | $63.628 |
| MCap | $408.676 |
| Volumen 24 h | $3.755.171 |
| Cambio 24 h | +524% |
| Cambio m5 / h1 | -3,0% / -30,1% |
| Volumen m5 / h1 | $11.977 / $192.409 |
| Trades m5 (compras / ventas) | 576 / 242 |
| Edad del par | 12,0 h |
| Score del feed (WS) | 77 |

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
| Score del feed | score WS × 0,3 | WS 77 × 0,3 | +23,1 |
| MCap | ≥ $100K | $408.676 | +15 |
| Volumen 24 h | ≥ $1M | $3.755.171 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 70% | +25 |
| Volumen m5 | > $1K (par maduro) | $11.977 | +10 |
| Liquidez | ≥ $50K | $63.628 | +10 |
| Cambio 24 h | ≥ +50% | +524% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +524% · liq/mcap 15,6% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-04T02:21:48+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=15.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 11 de 10.473 tokens analizados (0,11%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 04/10/2026 02:21 UTC, hasta 06/10/2026 02:21 UTC · vigente: quedan 46,1 h.
- **Aceleración al detectar:** cambio m5 -3,0% · h1 -30,1% · h24 +524% · volumen m5/h1 0,06 · edad del par 12,0 h.
- **Precio de entrada** (alerta): $0,0004124.
- **Consulta 04/10/2026 04:14 UTC:** $0,0003560 (-13,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump_2026-10-04_022148.json` · blob `9ef80b2669f717c47cd613bce36e90b6d095e806` · commit `0223049` (2026-10-04T04:03:55Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-04_021510.json` · blob `9aa7dfadca12573ace7e83b541515fb3e0201a47` · commit `0223049` (2026-10-04T04:03:55Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-04_022148`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump · registro · 04/10/2026 02:21 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump · HTTP 200 · 04/10/2026 04:14 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump/report · HTTP 200 · 04/10/2026 04:14 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump · HTTP 200 · 04/10/2026 04:14 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6LPvVdHuSFBfgC5Dtx6QKUgzo6d9brJhqNhCBpQZqkn7/ohlcv/hour?limit=1000 · HTTP 200 · 04/10/2026 04:14 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump · HTTP 404 · 04/10/2026 04:14 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=PURRSWORDUSDT · HTTP 400 · 04/10/2026 04:14 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/PURRSWORD-USD · HTTP 404 · 04/10/2026 04:14 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $59.968 vs $59.362 → 1,01%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0003560 vs $0,0003530 → 0,83%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump_2026-10-04_022148.json',encoding='utf-8'));d=d.get('GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump',d);p=mock.patch('time.time',return_value=1791080508);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint GgdAua8qfnwFKZxKEnDqTcJz5jQ81NURPWBK1qDzpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 04/10/2026 04:14 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `d86fbbd3779c7a0f…`
