# Red-Lipped Batfish (Tralalero) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00002490 · liquidez $11.722 · mcap $24.900 (al detectar)  
Detectado el 15/10/2026 10:13 UTC por: young-0.4 · edad 11.3 min · pesos info 59 / estructura 20 / precio 20 · info 20.1 · estructura 13.2 · precio/volumen 8.6 · cobertura 93/100, [info] narrative_wave: ola 'lipped': 8 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +5.3 (score 42, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 17/10/2026 10:13 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Tralalero

Estudio de cómo se adquiere Tralalero, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 15/10/2026 10:26 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 15/10/2026 10:13 UTC | pumpswap `6K9GBZE…fRjT` | $11.722 | 10% | 1,706% | 17,062% | 170,619% | $59 | $176 |
| consulta 15/10/2026 10:25 UTC | pumpswap `6K9GBZE…fRjT` | $8.158 | 10% | 2,452% | 24,517% | 245,170% | $41 | $122 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump`
5. Configurar el slippage: 10% (liquidez $8.158, consulta 15/10/2026 10:25 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump) y el par en DexScreener (https://dexscreener.com/solana/6K9GBZEGSNo8yqtuwU9tusQGy4zqpMuPrmFYSTDfRjT); mint authority / freeze authority: revocada / revocada · holders 1.326 · top-10 55,18% (consulta 15/10/2026 10:25 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump
- Par en DexScreener: https://dexscreener.com/solana/6K9GBZEGSNo8yqtuwU9tusQGy4zqpMuPrmFYSTDfRjT
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.326 · top-10 55,18% (consulta 15/10/2026 10:25 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Red-Lipped Batfish / Tralalero | registro de la detección (pumpportal_live) |
| Mint / contrato | `8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6K9GBZEGSNo8yqtuwU9tusQGy4zqpMuPrmFYSTDfRjT` | DexScreener, al detectar (2 par(es) en la consulta 15/10/2026 10:25 UTC) |
| Deployer | `Aqje5DsN4u2PHmQxGF9PKfpsDGwQRCBhWeLKHCFhSMXk` | PumpPortal (evento create), al detectar |
| Par creado | 15/10/2026 10:02 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,3 min / 11,3 min / 23,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 15/10/2026 10:25 UTC |
| Holders / top-10 | 1.326 / 55,18% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 15/10/2026 10:25 UTC |
| Holders efectivos del top-10 | 2,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 15/10/2026 10:25 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 15/10/2026 10:25 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6K9GBZEGSNo8yqtuwU9tusQGy4zqpMuPrmFYSTDfRjT · Solscan: https://solscan.io/token/8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump · pump.fun: https://pump.fun/coin/8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump · web / Telegram / X: no publicados en DexScreener | consulta 15/10/2026 10:25 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 15/10/2026 10:25 UTC)
- **Historia:**
  - Par creado el 15/10/2026 10:02 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 15/10/2026 10:13 UTC, con el par a 11,3 min de creado: precio $0,00002490, mcap $24.900, liquidez $11.722.
  - Velas de 1 h de GeckoTerminal (1, desde 15/10/2026 10:00 UTC): apertura $0,00004045 · máximo $0,00007413 (15/10/2026 10:00 UTC) · mínimo $0,00001396 (15/10/2026 10:00 UTC) · último cierre $0,00001719.
  - En la consulta 15/10/2026 10:25 UTC: precio $0,00001311, liquidez $8.158, FDV $13.117.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 15/10/2026 10:13 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00002490 |
| Liquidez | $11.722 |
| MCap | $24.900 |
| Volumen 24 h | $163.082 |
| Cambio 24 h | -41% |
| Cambio m5 / h1 | -56,5% / -41,0% |
| Volumen m5 / h1 | $53.874 / $163.082 |
| Trades m5 (compras / ventas) | 979 / 686 |
| Edad del par | 11,3 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 42; motivos sin regla: young-0.4 · edad 11.3 min · pesos info 59 / estructura 20 / precio 20 · info 20.1 · estructura 13.2 · precio/volumen 8.6 · cobertura 93/100, [info] narrative_wave: ola 'lipped': 8 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 1208 · top-10 41.1 % → +2.4, [estructura] dev_wallet: creador compró 8.3 % del supply → +0.5, [estructura] holder_to_txn_ratio: holders/txns 1208/4557 = 0.27 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×4.0 la tasa horaria (s 0.99), [precio/volumen] buy_pressure_shift: compras 59% en 5 min vs 57% en 1 h (s 0.07), [precio/volumen] holder_accumulation: holders 857→1208 (+58.5/min) · top10 39.8%→41.1% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=11721.99, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 42 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-15T10:13:58+00:00, sin estado previo): **10** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 58 de 35.859 tokens analizados (0,16%) quedan ≥ 56. Con score 10, este activo queda en el percentil 93,6 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 15/10/2026 10:13 UTC, hasta 17/10/2026 10:13 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -56,5% · h1 -41,0% · h24 -41% · volumen m5/h1 0,33 · edad del par 11,3 min.
- **Precio de entrada** (alerta): $0,00002490.
- **Consulta 15/10/2026 10:25 UTC:** $0,00001311 (-47,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump_2026-10-15_101358.json` · blob `f3a18961f523be5fdac3bbcb674b2342a871a1eb` · commit `90a3b9f` (2026-10-15T10:19:32Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-15_101358`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump · registro · 15/10/2026 10:13 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump · HTTP 200 · 15/10/2026 10:25 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump/report · HTTP 200 · 15/10/2026 10:25 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump · HTTP 200 · 15/10/2026 10:25 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6K9GBZEGSNo8yqtuwU9tusQGy4zqpMuPrmFYSTDfRjT/ohlcv/hour?limit=1000 · HTTP 200 · 15/10/2026 10:25 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump · HTTP 404 · 15/10/2026 10:25 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=TRALALEROUSDT · HTTP 400 · 15/10/2026 10:25 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/TRALALERO-USD · HTTP 404 · 15/10/2026 10:26 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $8.158 vs $9.608 → 15,10%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00001311 vs $0,00001719 → 23,72%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump_2026-10-15_101358.json',encoding='utf-8'));d=d.get('8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump',d);p=mock.patch('time.time',return_value=1792059238);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8EZDxabmGJxSmefanMBQXqUabCEEPvbjVxQ3bw52pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 15/10/2026 10:26 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `4efac974638bf7dc…`
