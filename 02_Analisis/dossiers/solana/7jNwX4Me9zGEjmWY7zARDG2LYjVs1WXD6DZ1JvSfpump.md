# Humphrey Reserve (HUMPH) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,004067 · liquidez $183.073 · mcap $4.049.469 (al detectar)  
Detectado el 13/10/2026 01:43 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 15/10/2026 01:43 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HUMPH

Estudio de cómo se adquiere HUMPH, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 13/10/2026 02:00 UTC; CoinGecko sin pares de este contrato en esos exchanges).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 13/10/2026 01:43 UTC | pumpswap `9pQRnaH…HLJz` | $183.073 | 5% | 0,109% | 1,092% | 10,925% | $915 | $2.746 |
| consulta 13/10/2026 02:00 UTC | pumpswap `9pQRnaH…HLJz` | $173.594 | 5% | 0,115% | 1,152% | 11,521% | $868 | $2.604 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump`
5. Configurar el slippage: 5% (liquidez $173.594, consulta 13/10/2026 02:00 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump) y el par en DexScreener (https://dexscreener.com/solana/9pQRnaHbKjD61KyS2K4FEnLCpvAi5hu5jbMbEsunHLJz); mint authority / freeze authority: revocada / revocada · holders 3.786 · top-10 4,39% (consulta 13/10/2026 02:00 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump
- Par en DexScreener: https://dexscreener.com/solana/9pQRnaHbKjD61KyS2K4FEnLCpvAi5hu5jbMbEsunHLJz
- Página del lanzamiento (pump.fun): https://pump.fun/coin/7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.786 · top-10 4,39% (consulta 13/10/2026 02:00 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Humphrey Reserve / HUMPH | registro de la detección (trending) |
| Mint / contrato | `7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `9pQRnaHbKjD61KyS2K4FEnLCpvAi5hu5jbMbEsunHLJz` | DexScreener, al detectar (2 par(es) en la consulta 13/10/2026 02:00 UTC) |
| Deployer | `Ac4ca1WdbjCNSEjtUrSSDeMRwbteuUNE9UWXZtm69Cze` | RugCheck `creator` |
| Par creado | 12/10/2026 10:54 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 14,8 h / 14,8 h / 15,1 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 13/10/2026 02:00 UTC |
| Holders / top-10 | 3.786 / 4,39% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 13/10/2026 02:00 UTC |
| Holders efectivos del top-10 | 3,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 13/10/2026 02:00 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 13/10/2026 02:00 UTC |
| Links | DexScreener: https://dexscreener.com/solana/9pQRnaHbKjD61KyS2K4FEnLCpvAi5hu5jbMbEsunHLJz · Solscan: https://solscan.io/token/7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump · pump.fun: https://pump.fun/coin/7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump · web: https://www.humph.fun · twitter: https://x.com/humph_sol | consulta 13/10/2026 02:00 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** CoinGecko: Solana Ecosystem, Pump.fun Ecosystem
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 13/10/2026 02:00 UTC)
- **Historia:**
  - Par creado el 12/10/2026 10:54 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 13/10/2026 01:43 UTC, con el par a 14,8 h de creado: precio $0,004067, mcap $4.049.469, liquidez $183.073.
  - Velas de 1 h de GeckoTerminal (17, desde 12/10/2026 10:00 UTC): apertura $0,0004393 · máximo $0,004358 (13/10/2026 01:00 UTC) · mínimo $0,00007774 (12/10/2026 10:00 UTC) · último cierre $0,003643.
  - En la consulta 13/10/2026 02:00 UTC: precio $0,003651, liquidez $173.594, FDV $3.635.825.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 13/10/2026 01:43 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,004067 |
| Liquidez | $183.073 |
| MCap | $4.049.469 |
| Volumen 24 h | $2.977.099 |
| Cambio 24 h | +5.121% |
| Cambio m5 / h1 | +1,6% / +19,8% |
| Volumen m5 / h1 | $17.304 / $206.772 |
| Trades m5 (compras / ventas) | 256 / 150 |
| Edad del par | 14,8 h |
| Score del feed (WS) | 83 |

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
| Score del feed | score WS × 0,3 | WS 83 × 0,3 | +24,9 |
| MCap | ≥ $1M | $4.049.469 | +25 |
| Volumen 24 h | ≥ $1M | $2.977.099 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 63% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +1,6% · h1 +19,8% | +20 |
| Volumen m5 | > $1K (par maduro) | $17.304 | +10 |
| Liquidez | ≥ $100K | $183.073 | +15 |
| Cambio 24 h | ≥ +50% | +5.121% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +5.121% · liq/mcap 4,5% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-13T01:43:58+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 52 de 32.424 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 13/10/2026 01:43 UTC, hasta 15/10/2026 01:43 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +1,6% · h1 +19,8% · h24 +5.121% · volumen m5/h1 0,08 · edad del par 14,8 h.
- **Precio de entrada** (alerta): $0,004067.
- **Consulta 13/10/2026 02:00 UTC:** $0,003651 (-10,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump_2026-10-13_014358.json` · blob `74f36851b3f4d591cbee8bba3f3e6e454a38bf61` · commit `16ed44a` (2026-10-13T01:54:12Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-13_013706.json` · blob `01da778afc25c3cc1999d832e2ade85a0d1ed64b` · commit `16ed44a` (2026-10-13T01:54:12Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-13_014358`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump · registro · 13/10/2026 01:43 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump · HTTP 200 · 13/10/2026 02:00 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump/report · HTTP 200 · 13/10/2026 02:00 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump · HTTP 200 · 13/10/2026 02:00 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/9pQRnaHbKjD61KyS2K4FEnLCpvAi5hu5jbMbEsunHLJz/ohlcv/hour?limit=1000 · HTTP 200 · 13/10/2026 02:00 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump · HTTP 200 · 13/10/2026 02:00 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HUMPHUSDT · HTTP 400 · 13/10/2026 02:00 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HUMPH-USD · HTTP 404 · 13/10/2026 02:00 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $173.594 vs $173.804 → 0,12%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003651 vs $0,003643 → 0,23%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump_2026-10-13_014358.json',encoding='utf-8'));d=d.get('7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump',d);p=mock.patch('time.time',return_value=1791855838);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 7jNwX4Me9zGEjmWY7zARDG2LYjVs1WXD6DZ1JvSfpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 13/10/2026 02:00 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `080e42fcfc5318de…`
