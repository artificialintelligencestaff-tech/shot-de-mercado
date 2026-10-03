# Digital Oil Trust Fund (DOTF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,004853 · liquidez $199.727 · mcap $4.853.565 (al detectar)  
Detectado el 03/10/2026 02:12 UTC por: MCap > $1M, Volumen decente, Liquidez alta (score 62, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 05/10/2026 02:12 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir DOTF

Estudio de cómo se adquiere DOTF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 03/10/2026 02:42 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 03/10/2026 02:12 UTC | pumpswap `B1A6jwp…wPh5` | $199.727 | 5% | 0,100% | 1,001% | 10,014% | $999 | $2.996 |
| consulta 03/10/2026 02:42 UTC | pumpswap `B1A6jwp…wPh5` | $201.483 | 5% | 0,099% | 0,993% | 9,926% | $1.007 | $3.022 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump`
5. Configurar el slippage: 5% (liquidez $201.483, consulta 03/10/2026 02:42 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump) y el par en DexScreener (https://dexscreener.com/solana/B1A6jwptnaXqvPZ1omj1ph8NAwvC5tuXArCx5fjMwPh5); mint authority / freeze authority: revocada / revocada · holders 3.775 · top-10 10,88% (consulta 03/10/2026 02:42 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump
- Par en DexScreener: https://dexscreener.com/solana/B1A6jwptnaXqvPZ1omj1ph8NAwvC5tuXArCx5fjMwPh5
- Página del lanzamiento (pump.fun): https://pump.fun/coin/RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.775 · top-10 10,88% (consulta 03/10/2026 02:42 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Digital Oil Trust Fund / DOTF | registro de la detección (pumpportal_live) |
| Mint / contrato | `RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `B1A6jwptnaXqvPZ1omj1ph8NAwvC5tuXArCx5fjMwPh5` | DexScreener, al detectar (2 par(es) en la consulta 03/10/2026 02:42 UTC) |
| Deployer | `43GxdWY2HSYzsiiaPKow8ysW3TPv8xwdYYo5Nw5i2dCP` | PumpPortal (evento create), al detectar |
| Par creado | 03/10/2026 02:01 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,1 min / 11,1 min / 40,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 03/10/2026 02:42 UTC |
| Holders / top-10 | 3.775 / 10,88% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 03/10/2026 02:42 UTC |
| Holders efectivos del top-10 | 9,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 03/10/2026 02:42 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 03/10/2026 02:42 UTC |
| Links | DexScreener: https://dexscreener.com/solana/B1A6jwptnaXqvPZ1omj1ph8NAwvC5tuXArCx5fjMwPh5 · Solscan: https://solscan.io/token/RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump · pump.fun: https://pump.fun/coin/RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump · web / Telegram / X: no publicados en DexScreener | consulta 03/10/2026 02:42 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 03/10/2026 02:42 UTC)
- **Historia:**
  - Par creado el 03/10/2026 02:01 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 03/10/2026 02:12 UTC, con el par a 11,1 min de creado: precio $0,004853, mcap $4.853.565, liquidez $199.727.
  - Velas de 1 h de GeckoTerminal (1, desde 03/10/2026 02:00 UTC): apertura $0,0004827 · máximo $0,004937 (03/10/2026 02:00 UTC) · mínimo $0,00004946 (03/10/2026 02:00 UTC) · último cierre $0,004934.
  - En la consulta 03/10/2026 02:42 UTC: precio $0,004936, liquidez $201.483, FDV $4.936.350.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 03/10/2026 02:12 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,004853 |
| Liquidez | $199.727 |
| MCap | $4.853.565 |
| Volumen 24 h | $90.686 |
| Cambio 24 h | +9.703% |
| Cambio m5 / h1 | -0,3% / +9.703,0% |
| Volumen m5 / h1 | $871 / $90.686 |
| Trades m5 (compras / ventas) | 16 / 14 |
| Edad del par | 11,1 min |
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

Desglose no reproducible desde los motivos registrados (suma 60 vs score 62; motivos sin regla: Anticipación (lib_early_signals early-0.2): +2 — liquidity_inflow: liquidez +1% en 8 min → +0.06; holder_accumulation: holders 1619→3776 (+269.6/min) · top10 100.0%→10.9% → +2): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-03T02:12:57+00:00, sin estado previo): **60** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen decente, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.1% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 10 de 9.471 tokens analizados (0,11%) quedan ≥ 56. Con score 60, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 03/10/2026 02:12 UTC, hasta 05/10/2026 02:12 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -0,3% · h1 +9.703,0% · h24 +9.703% · volumen m5/h1 0,01 · edad del par 11,1 min.
- **Precio de entrada** (alerta): $0,004853.
- **Consulta 03/10/2026 02:42 UTC:** $0,004936 (+1,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump_2026-10-03_021257.json` · blob `94bf7e530f00b139324138d4898e8df541dad51b` · commit `a88e882` (2026-10-03T02:35:51Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-03_021257`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump · registro · 03/10/2026 02:12 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump · HTTP 200 · 03/10/2026 02:42 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump/report · HTTP 200 · 03/10/2026 02:42 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump · HTTP 200 · 03/10/2026 02:42 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/B1A6jwptnaXqvPZ1omj1ph8NAwvC5tuXArCx5fjMwPh5/ohlcv/hour?limit=1000 · HTTP 200 · 03/10/2026 02:42 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump · HTTP 404 · 03/10/2026 02:42 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=DOTFUSDT · HTTP 400 · 03/10/2026 02:42 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/DOTF-USD · HTTP 404 · 03/10/2026 02:42 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $201.483 vs $201.532 → 0,02%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,004936 vs $0,004934 → 0,04%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump_2026-10-03_021257.json',encoding='utf-8'));d=d.get('RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump',d);p=mock.patch('time.time',return_value=1790993577);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint RvkFYybWAGhgcsmvkQvFdUgqnVREbcSQhHFUW6Ypump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 03/10/2026 02:42 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `ee841bbf941965ca…`
