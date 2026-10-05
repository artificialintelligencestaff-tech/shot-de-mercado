# CRAWLNET (CRAWL) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003168 · liquidez $162.159 · mcap $3.166.604 (al detectar)  
Detectado el 05/10/2026 10:21 UTC por: MCap > $1M, Volumen alto, Momentum corto+medio positivo (score 84, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 07/10/2026 10:21 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir CRAWL

Estudio de cómo se adquiere CRAWL, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 05/10/2026 10:40 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 05/10/2026 10:21 UTC | pumpswap `6Bdjnf8…dgTb` | $162.159 | 5% | 0,123% | 1,233% | 12,334% | $811 | $2.432 |
| consulta 05/10/2026 10:39 UTC | pumpswap `6Bdjnf8…dgTb` | $190.707 | 5% | 0,105% | 1,049% | 10,487% | $954 | $2.861 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump`
5. Configurar el slippage: 5% (liquidez $190.707, consulta 05/10/2026 10:39 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump) y el par en DexScreener (https://dexscreener.com/solana/6Bdjnf8RqWedRVmbrEYGLBbMxTZ37wawTm6mmvwYdgTb); mint authority / freeze authority: revocada / revocada · holders 2.346 · top-10 17,33% (consulta 05/10/2026 10:39 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump
- Par en DexScreener: https://dexscreener.com/solana/6Bdjnf8RqWedRVmbrEYGLBbMxTZ37wawTm6mmvwYdgTb
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.346 · top-10 17,33% (consulta 05/10/2026 10:39 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | CRAWLNET / CRAWL | registro de la detección (pumpportal) |
| Mint / contrato | `8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6Bdjnf8RqWedRVmbrEYGLBbMxTZ37wawTm6mmvwYdgTb` | DexScreener, al detectar (2 par(es) en la consulta 05/10/2026 10:39 UTC) |
| Deployer | `ZXEW1FXj4huSaEBB9syiYkkuDx7U1JxAQCssFfZauGr` | PumpPortal (evento create), al detectar |
| Par creado | 05/10/2026 09:13 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 68,0 min / 68,0 min / 86,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 05/10/2026 10:39 UTC |
| Holders / top-10 | 2.346 / 17,33% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 05/10/2026 10:39 UTC |
| Holders efectivos del top-10 | 8,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 05/10/2026 10:39 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 05/10/2026 10:39 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6Bdjnf8RqWedRVmbrEYGLBbMxTZ37wawTm6mmvwYdgTb · Solscan: https://solscan.io/token/8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump · pump.fun: https://pump.fun/coin/8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump · web / Telegram / X: no publicados en DexScreener | consulta 05/10/2026 10:39 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 05/10/2026 10:39 UTC)
- **Historia:**
  - Par creado el 05/10/2026 09:13 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 05/10/2026 10:21 UTC, con el par a 68,0 min de creado: precio $0,003168, mcap $3.166.604, liquidez $162.159.
  - Velas de 1 h de GeckoTerminal (2, desde 05/10/2026 09:00 UTC): apertura $0,002722 · máximo $0,004413 (05/10/2026 10:00 UTC) · mínimo $0,00005018 (05/10/2026 09:00 UTC) · último cierre $0,004373.
  - En la consulta 05/10/2026 10:39 UTC: precio $0,004371, liquidez $190.707, FDV $4.368.511.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 05/10/2026 10:21 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003168 |
| Liquidez | $162.159 |
| MCap | $3.166.604 |
| Volumen 24 h | $110.111 |
| Cambio 24 h | +6.215% |
| Cambio m5 / h1 | +21,1% / +1,3% |
| Volumen m5 / h1 | $8.702 / $40.278 |
| Trades m5 (compras / ventas) | 4 / 18 |
| Edad del par | 68,0 min |
| Score del feed (WS) | n/d (feed sin score) |

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

Desglose no reproducible desde los motivos registrados (suma 83 vs score 84; motivos sin regla: Anticipación (lib_early_signals early-0.2): +1 — volume_acceleration: vol 5 min ×2.6 la tasa horaria → +1.31; liquidity_inflow: liquidez +10% en 9 min → +0.65): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-05T10:21:27+00:00, sin estado previo): **83** · motivos: MCap > $1M, Volumen alto, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Venta dominante (buy_pressure <40%), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=5.1% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 16 de 11.857 tokens analizados (0,13%) quedan ≥ 56. Con score 83, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 05/10/2026 10:21 UTC, hasta 07/10/2026 10:21 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +21,1% · h1 +1,3% · h24 +6.215% · volumen m5/h1 0,22 · edad del par 68,0 min.
- **Precio de entrada** (alerta): $0,003168.
- **Consulta 05/10/2026 10:39 UTC:** $0,004371 (+38,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump_2026-10-05_102127.json` · blob `7b73cdf1a123fdb37296887e9e07ae1df10365b2` · commit `20f39ee` (2026-10-05T10:33:49Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-05_102127`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump · registro · 05/10/2026 10:21 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump · HTTP 200 · 05/10/2026 10:39 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump/report · HTTP 200 · 05/10/2026 10:40 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump · HTTP 200 · 05/10/2026 10:40 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6Bdjnf8RqWedRVmbrEYGLBbMxTZ37wawTm6mmvwYdgTb/ohlcv/hour?limit=1000 · HTTP 200 · 05/10/2026 10:40 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump · HTTP 404 · 05/10/2026 10:40 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=CRAWLUSDT · HTTP 400 · 05/10/2026 10:40 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/CRAWL-USD · HTTP 404 · 05/10/2026 10:40 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $190.707 vs $191.784 → 0,56%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,004371 vs $0,004373 → 0,05%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump_2026-10-05_102127.json',encoding='utf-8'));d=d.get('8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump',d);p=mock.patch('time.time',return_value=1791195687);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8VRh4LNmSZxEANDhEX1uD58xbiKbUQVVm16Rs5jVpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 05/10/2026 10:40 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `604061feac214d3b…`
