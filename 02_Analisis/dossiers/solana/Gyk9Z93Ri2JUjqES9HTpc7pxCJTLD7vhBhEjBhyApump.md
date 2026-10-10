# Altai the Tiger (Altai) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0002916 · liquidez $48.232 · mcap $291.628 (al detectar)  
Detectado el 10/10/2026 14:04 UTC por: young-0.4 · edad 11.9 min · pesos info 59 / estructura 20 / precio 20 · info 20.3 · estructura 13.4 · precio/volumen 11.3 · cobertura 93/100, [info] narrative_wave: ola 'tiger': 16 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['website'] · descripción 29 caracteres → +2.6 (score 45, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 12/10/2026 14:04 UTC (< 48 h) · vigente: quedan 47,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Altai

Estudio de cómo se adquiere Altai, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 10/10/2026 14:11 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 10/10/2026 14:04 UTC | pumpswap `DMEUT8U…bRHt` | $48.232 | 10% | 0,415% | 4,147% | 41,467% | $241 | $723 |
| consulta 10/10/2026 14:11 UTC | pumpswap `DMEUT8U…bRHt` | $45.493 | 10% | 0,440% | 4,396% | 43,963% | $227 | $682 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump`
5. Configurar el slippage: 10% (liquidez $45.493, consulta 10/10/2026 14:11 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump) y el par en DexScreener (https://dexscreener.com/solana/DMEUT8UV5JX8G7jB7TP9XyfBUrP5z7p6VPLSE2WbbRHt); mint authority / freeze authority: revocada / revocada · holders 2.403 · top-10 29,82% (consulta 10/10/2026 14:11 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump
- Par en DexScreener: https://dexscreener.com/solana/DMEUT8UV5JX8G7jB7TP9XyfBUrP5z7p6VPLSE2WbbRHt
- Página del lanzamiento (pump.fun): https://pump.fun/coin/Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.403 · top-10 29,82% (consulta 10/10/2026 14:11 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Altai the Tiger / Altai | registro de la detección (pumpportal_live) |
| Mint / contrato | `Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DMEUT8UV5JX8G7jB7TP9XyfBUrP5z7p6VPLSE2WbbRHt` | DexScreener, al detectar (3 par(es) en la consulta 10/10/2026 14:11 UTC) |
| Deployer | `Gfsk5ZojnHSLoxRhUBD5vviJELFuTGkyBh9QTqEo7Ehg` | PumpPortal (evento create), al detectar |
| Par creado | 10/10/2026 13:52 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,9 min / 11,9 min / 19,1 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 10/10/2026 14:11 UTC |
| Holders / top-10 | 2.403 / 29,82% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 10/10/2026 14:11 UTC |
| Holders efectivos del top-10 | 6,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 10/10/2026 14:11 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 10/10/2026 14:11 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DMEUT8UV5JX8G7jB7TP9XyfBUrP5z7p6VPLSE2WbbRHt · Solscan: https://solscan.io/token/Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump · pump.fun: https://pump.fun/coin/Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump · web: https://www.facebook.com/groups/ywpphotosandnews/posts/2543749709426668/?comment_id=2543761329425506&reply_comment_id=2543763212758651 · twitter: https://x.com/uncleibbra/status/2108920051885920688 | consulta 10/10/2026 14:11 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 10/10/2026 14:11 UTC)
- **Historia:**
  - Par creado el 10/10/2026 13:52 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 10/10/2026 14:04 UTC, con el par a 11,9 min de creado: precio $0,0002916, mcap $291.628, liquidez $48.232.
  - Velas de 1 h de GeckoTerminal (2, desde 10/10/2026 13:00 UTC): apertura $0,00004554 · máximo $0,0003690 (10/10/2026 13:00 UTC) · mínimo $0,00003442 (10/10/2026 13:00 UTC) · último cierre $0,0002119.
  - En la consulta 10/10/2026 14:11 UTC: precio $0,0002373, liquidez $45.493, FDV $237.398.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 10/10/2026 14:04 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0002916 |
| Liquidez | $48.232 |
| MCap | $291.628 |
| Volumen 24 h | $283.310 |
| Cambio 24 h | +534% |
| Cambio m5 / h1 | -3,7% / +534,0% |
| Volumen m5 / h1 | $157.175 / $283.310 |
| Trades m5 (compras / ventas) | 1.056 / 893 |
| Edad del par | 11,9 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 45; motivos sin regla: young-0.4 · edad 11.9 min · pesos info 59 / estructura 20 / precio 20 · info 20.3 · estructura 13.4 · precio/volumen 11.3 · cobertura 93/100, [info] narrative_wave: ola 'tiger': 16 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['website'] · descripción 29 caracteres → +2.6, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 1279 · top-10 31.3 % → +2.5, [estructura] dev_wallet: creador compró 8.2 % del supply → +0.6, [estructura] holder_to_txn_ratio: holders/txns 1279/3653 = 0.35 → +0.6, [precio/volumen] volume_acceleration: vol 5 min ×6.7 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 54% en 5 min vs 53% en 1 h (s 0.08), [precio/volumen] liquidity_inflow: liquidez +22% en 8 min (s 0.73), [precio/volumen] holder_accumulation: holders 361→1279 (+153.0/min) · top10 37.3%→31.3% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=48231.52, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 45 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-10T14:04:09+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=16.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 44 de 27.235 tokens analizados (0,16%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 10/10/2026 14:04 UTC, hasta 12/10/2026 14:04 UTC · vigente: quedan 47,9 h.
- **Aceleración al detectar:** cambio m5 -3,7% · h1 +534,0% · h24 +534% · volumen m5/h1 0,55 · edad del par 11,9 min.
- **Precio de entrada** (alerta): $0,0002916.
- **Consulta 10/10/2026 14:11 UTC:** $0,0002373 (-18,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump_2026-10-10_140409.json` · blob `f3b04c3b5fa70b0d7aecb6a231d994f09cd60aba` · commit `6094090` (2026-10-10T14:04:35Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-10_140409`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump · registro · 10/10/2026 14:04 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump · HTTP 200 · 10/10/2026 14:11 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump/report · HTTP 200 · 10/10/2026 14:11 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump · HTTP 200 · 10/10/2026 14:11 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DMEUT8UV5JX8G7jB7TP9XyfBUrP5z7p6VPLSE2WbbRHt/ohlcv/hour?limit=1000 · HTTP 200 · 10/10/2026 14:11 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump · HTTP 404 · 10/10/2026 14:11 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ALTAIUSDT · HTTP 400 · 10/10/2026 14:11 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ALTAI-USD · HTTP 404 · 10/10/2026 14:11 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $45.493 vs $50.096 → 9,19%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0002373 vs $0,0002119 → 10,69%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump_2026-10-10_140409.json',encoding='utf-8'));d=d.get('Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump',d);p=mock.patch('time.time',return_value=1791641049);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint Gyk9Z93Ri2JUjqES9HTpc7pxCJTLD7vhBhEjBhyApump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 10/10/2026 14:11 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `0c46fef4082789bc…`
