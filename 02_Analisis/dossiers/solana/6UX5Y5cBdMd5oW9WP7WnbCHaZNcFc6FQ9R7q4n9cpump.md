# Trencher (Trencher) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001416 · liquidez $32.686 · mcap $141.689 (al detectar)  
Detectado el 06/10/2026 19:31 UTC por: young-0.4 · edad 12.8 min · pesos info 59 / estructura 21 / precio 21 · info 12.1 · estructura 17.4 · precio/volumen 13.1 · cobertura 84/100, [info] narrative_wave: ola 'trencher': 5 lanzamientos más en 1 h → +9.2, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +2.9 (score 43, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 08/10/2026 19:31 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Trencher

Estudio de cómo se adquiere Trencher, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 19:55 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 19:31 UTC | pumpswap `FALZ6Br…kLDi` | $32.686 | 10% | 0,612% | 6,119% | 61,189% | $163 | $490 |
| consulta 06/10/2026 19:54 UTC | pumpswap `FALZ6Br…kLDi` | $2.383 | 10% | 8,393% | 83,935% | 839,349% | $12 | $36 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump`
5. Configurar el slippage: 10% (liquidez $2.383, consulta 06/10/2026 19:54 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump) y el par en DexScreener (https://dexscreener.com/solana/FALZ6BrZCB9qGduzb8Cpw7RPt6qaPEb1AxE5q6TKkLDi); mint authority / freeze authority: revocada / revocada · holders 103 · top-10 100,00% (consulta 06/10/2026 19:54 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump
- Par en DexScreener: https://dexscreener.com/solana/FALZ6BrZCB9qGduzb8Cpw7RPt6qaPEb1AxE5q6TKkLDi
- Página del lanzamiento (pump.fun): https://pump.fun/coin/6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 103 · top-10 100,00% (consulta 06/10/2026 19:54 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Trencher / Trencher | registro de la detección (pumpportal_live) |
| Mint / contrato | `6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `FALZ6BrZCB9qGduzb8Cpw7RPt6qaPEb1AxE5q6TKkLDi` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 19:54 UTC) |
| Deployer | `ARwmPUzmHjfxUgWGMJcrEaR687mLE9ZXF34dkyDre3Wc` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 19:18 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 12,8 min / 12,8 min / 36,3 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 19:54 UTC |
| Holders / top-10 | 103 / 100,00% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 19:54 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 19:54 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 19:54 UTC |
| Links | DexScreener: https://dexscreener.com/solana/FALZ6BrZCB9qGduzb8Cpw7RPt6qaPEb1AxE5q6TKkLDi · Solscan: https://solscan.io/token/6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump · pump.fun: https://pump.fun/coin/6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump · web / Telegram / X: no publicados en DexScreener | consulta 06/10/2026 19:54 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 19:54 UTC)
- **Historia:**
  - Par creado el 06/10/2026 19:18 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 19:31 UTC, con el par a 12,8 min de creado: precio $0,0001416, mcap $141.689, liquidez $32.686.
  - Velas de 1 h de GeckoTerminal (1, desde 06/10/2026 19:00 UTC): apertura $0,00005100 · máximo $0,0001611 (06/10/2026 19:00 UTC) · mínimo $0,000002357 (06/10/2026 19:00 UTC) · último cierre $0,000002357.
  - En la consulta 06/10/2026 19:54 UTC: precio $0,000002355, liquidez $2.383, FDV $2.356.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 19:31 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001416 |
| Liquidez | $32.686 |
| MCap | $141.689 |
| Volumen 24 h | $74.205 |
| Cambio 24 h | +183% |
| Cambio m5 / h1 | +65,9% / +183,0% |
| Volumen m5 / h1 | $27.416 / $74.205 |
| Trades m5 (compras / ventas) | 1.417 / 516 |
| Edad del par | 12,8 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 43; motivos sin regla: young-0.4 · edad 12.8 min · pesos info 59 / estructura 21 / precio 21 · info 12.1 · estructura 17.4 · precio/volumen 13.1 · cobertura 84/100, [info] narrative_wave: ola 'trencher': 5 lanzamientos más en 1 h → +9.2, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +2.9, [estructura] bonding_progress: graduado (pumpswap) → +9.9, [estructura] holders_struct: holders 2005 · top-10 25.4 % → +5.0, [estructura] dev_wallet: creador compró 4.1 % del supply → +1.8, [estructura] holder_to_txn_ratio: holders/txns 2005/5068 = 0.40 → +0.7, [precio/volumen] volume_acceleration: vol 5 min ×4.4 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 73% en 5 min vs 67% en 1 h (s 0.30), [precio/volumen] liquidity_inflow: liquidez +73% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1600→2005 (+67.5/min) · top10 32.2%→25.4% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=32685.51, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 43 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T19:31:40+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen decente, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 21 de 16.556 tokens analizados (0,13%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 19:31 UTC, hasta 08/10/2026 19:31 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +65,9% · h1 +183,0% · h24 +183% · volumen m5/h1 0,37 · edad del par 12,8 min.
- **Precio de entrada** (alerta): $0,0001416.
- **Consulta 06/10/2026 19:54 UTC:** $0,000002355 (-98,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump_2026-10-06_193140.json` · blob `ea612eb03de15bc2e419de9820b1c56558b10ba5` · commit `a2ad446` (2026-10-06T19:48:41Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_193140`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump · registro · 06/10/2026 19:31 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump · HTTP 200 · 06/10/2026 19:54 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump/report · HTTP 200 · 06/10/2026 19:54 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump · HTTP 200 · 06/10/2026 19:55 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/FALZ6BrZCB9qGduzb8Cpw7RPt6qaPEb1AxE5q6TKkLDi/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 19:55 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump · HTTP 404 · 06/10/2026 19:55 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=TRENCHERUSDT · HTTP 400 · 06/10/2026 19:55 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/TRENCHER-USD · HTTP 404 · 06/10/2026 19:55 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.383 vs $2.386 → 0,13%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002355 vs $0,000002357 → 0,07%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump_2026-10-06_193140.json',encoding='utf-8'));d=d.get('6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump',d);p=mock.patch('time.time',return_value=1791315100);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 6UX5Y5cBdMd5oW9WP7WnbCHaZNcFc6FQ9R7q4n9cpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 19:55 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `eb57dbcc235bd342…`
