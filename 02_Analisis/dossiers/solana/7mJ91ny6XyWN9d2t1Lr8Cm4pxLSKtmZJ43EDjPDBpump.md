# Fantasy Index 6900 (FIX6900) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00009655 · liquidez $25.602 · mcap $96.553 (al detectar)  
Detectado el 13/10/2026 15:44 UTC por: young-0.4 · edad 17.6 min · pesos info 56 / estructura 22 / precio 22 · info 14.1 · estructura 18.8 · precio/volumen 9.5 · cobertura 84/100, [info] narrative_wave: ola 'index': 22 lanzamientos más en 1 h → +14.1, [estructura] bonding_progress: graduado (pumpswap) → +10.5 (score 42, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 15/10/2026 15:44 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir FIX6900

Estudio de cómo se adquiere FIX6900, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 13/10/2026 16:03 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 13/10/2026 15:44 UTC | pumpswap `3L7nMwL…wiZ4` | $25.602 | 10% | 0,781% | 7,812% | 78,120% | $128 | $384 |
| consulta 13/10/2026 16:03 UTC | pumpswap `3L7nMwL…wiZ4` | $2.140 | 10% | 9,346% | 93,456% | 934,562% | $11 | $32 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump`
5. Configurar el slippage: 10% (liquidez $2.140, consulta 13/10/2026 16:03 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump) y el par en DexScreener (https://dexscreener.com/solana/3L7nMwLotP9PpHLvJkaGXjCioNrYSPzuX8uXoZbZwiZ4); mint authority / freeze authority: revocada / revocada · holders 59 · top-10 99,99% (consulta 13/10/2026 16:03 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump
- Par en DexScreener: https://dexscreener.com/solana/3L7nMwLotP9PpHLvJkaGXjCioNrYSPzuX8uXoZbZwiZ4
- Página del lanzamiento (pump.fun): https://pump.fun/coin/7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 59 · top-10 99,99% (consulta 13/10/2026 16:03 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Fantasy Index 6900 / FIX6900 | registro de la detección (pumpportal_live) |
| Mint / contrato | `7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `3L7nMwLotP9PpHLvJkaGXjCioNrYSPzuX8uXoZbZwiZ4` | DexScreener, al detectar (2 par(es) en la consulta 13/10/2026 16:03 UTC) |
| Deployer | `6xYH2GaTGgHSZe5FSpBCyUsSshhB9LG26ZKmpPLTwPYh` | PumpPortal (evento create), al detectar |
| Par creado | 13/10/2026 15:26 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 17,6 min / 17,6 min / 36,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 13/10/2026 16:03 UTC |
| Holders / top-10 | 59 / 99,99% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 13/10/2026 16:03 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 13/10/2026 16:03 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 13/10/2026 16:03 UTC |
| Links | DexScreener: https://dexscreener.com/solana/3L7nMwLotP9PpHLvJkaGXjCioNrYSPzuX8uXoZbZwiZ4 · Solscan: https://solscan.io/token/7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump · pump.fun: https://pump.fun/coin/7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump · web / Telegram / X: no publicados en DexScreener | consulta 13/10/2026 16:03 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 13/10/2026 16:03 UTC)
- **Historia:**
  - Par creado el 13/10/2026 15:26 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 13/10/2026 15:44 UTC, con el par a 17,6 min de creado: precio $0,00009655, mcap $96.553, liquidez $25.602.
  - Velas de 1 h de GeckoTerminal (1, desde 13/10/2026 15:00 UTC): apertura $0,00004656 · máximo $0,0001402 (13/10/2026 15:00 UTC) · mínimo $0,000002090 (13/10/2026 15:00 UTC) · último cierre $0,000002118.
  - En la consulta 13/10/2026 16:03 UTC: precio $0,000002110, liquidez $2.140, FDV $2.110.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 13/10/2026 15:44 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00009655 |
| Liquidez | $25.602 |
| MCap | $96.553 |
| Volumen 24 h | $1.511 |
| Cambio 24 h | +113% |
| Cambio m5 / h1 | +20,0% / +113,0% |
| Volumen m5 / h1 | $338 / $1.511 |
| Trades m5 (compras / ventas) | 8 / 9 |
| Edad del par | 17,6 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 42; motivos sin regla: young-0.4 · edad 17.6 min · pesos info 56 / estructura 22 / precio 22 · info 14.1 · estructura 18.8 · precio/volumen 9.5 · cobertura 84/100, [info] narrative_wave: ola 'index': 22 lanzamientos más en 1 h → +14.1, [estructura] bonding_progress: graduado (pumpswap) → +10.5, [estructura] holders_struct: holders 421 · top-10 24.9 % → +5.3, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.2, [estructura] holder_to_txn_ratio: holders/txns 421/61 = 6.90 → +0.9, [precio/volumen] volume_acceleration: vol 5 min ×2.7 la tasa horaria (s 0.47), [precio/volumen] liquidity_inflow: liquidez +27% en 8 min (s 0.89), [precio/volumen] holder_accumulation: holders 121→421 (+25.0/min) · top10 44.5%→24.9% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=25601.62, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 42 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-13T15:44:18+00:00, sin estado previo): **25** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen bajo, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 52 de 33.537 tokens analizados (0,16%) quedan ≥ 56. Con score 25, este activo queda en el percentil 97,5 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 13/10/2026 15:44 UTC, hasta 15/10/2026 15:44 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +20,0% · h1 +113,0% · h24 +113% · volumen m5/h1 0,22 · edad del par 17,6 min.
- **Precio de entrada** (alerta): $0,00009655.
- **Consulta 13/10/2026 16:03 UTC:** $0,000002110 (-97,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump_2026-10-13_154418.json` · blob `bc1b08f8b9803d7ba13a1a54a2067e368b6c295b` · commit `0940ff3` (2026-10-13T15:56:50Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-13_154418`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump · registro · 13/10/2026 15:44 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump · HTTP 200 · 13/10/2026 16:03 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump/report · HTTP 200 · 13/10/2026 16:03 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump · HTTP 200 · 13/10/2026 16:03 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/3L7nMwLotP9PpHLvJkaGXjCioNrYSPzuX8uXoZbZwiZ4/ohlcv/hour?limit=1000 · HTTP 200 · 13/10/2026 16:03 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump · HTTP 404 · 13/10/2026 16:03 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=FIX6900USDT · HTTP 400 · 13/10/2026 16:03 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/FIX6900-USD · HTTP 404 · 13/10/2026 16:03 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.140 vs $2.148 → 0,39%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002110 vs $0,000002118 → 0,38%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump_2026-10-13_154418.json',encoding='utf-8'));d=d.get('7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump',d);p=mock.patch('time.time',return_value=1791906258);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 7mJ91ny6XyWN9d2t1Lr8Cm4pxLSKtmZJ43EDjPDBpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 13/10/2026 16:03 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `32dc5492d511f6db…`
