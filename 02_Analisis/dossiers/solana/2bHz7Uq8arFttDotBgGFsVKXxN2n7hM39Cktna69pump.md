# Human Interaction Model (HIM) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00002158 · liquidez $12.154 · mcap $21.133 (al detectar)  
Detectado el 02/10/2026 22:04 UTC por: MCap bajo, Volumen masivo, Buy pressure >60% (score 60, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 04/10/2026 22:04 UTC (< 48 h) · vigente: quedan 47,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HIM

Estudio de cómo se adquiere HIM, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 22:11 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 22:04 UTC | pumpswap `HaGMjHT…u9c2` | $12.154 | 10% | 1,646% | 16,455% | 164,550% | $61 | $182 |
| consulta 02/10/2026 22:11 UTC | pumpswap `HaGMjHT…u9c2` | $11.806 | 10% | 1,694% | 16,941% | 169,412% | $59 | $177 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump`
5. Configurar el slippage: 10% (liquidez $11.806, consulta 02/10/2026 22:11 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump) y el par en DexScreener (https://dexscreener.com/solana/HaGMjHTjfy7f3DN54RHix2RCWvaMZbRKszkFGXPmu9c2); mint authority / freeze authority: revocada / revocada · holders 3.545 · top-10 65,56% (consulta 02/10/2026 22:11 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump
- Par en DexScreener: https://dexscreener.com/solana/HaGMjHTjfy7f3DN54RHix2RCWvaMZbRKszkFGXPmu9c2
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.545 · top-10 65,56% (consulta 02/10/2026 22:11 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Human Interaction Model / HIM | registro de la detección (pumpportal) |
| Mint / contrato | `2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HaGMjHTjfy7f3DN54RHix2RCWvaMZbRKszkFGXPmu9c2` | DexScreener, al detectar (5 par(es) en la consulta 02/10/2026 22:11 UTC) |
| Deployer | `BJdhYodGkFLFV2rYsyBsAyZmAYcfEAQcJZX44yvTtBPi` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 20:30 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 93,6 min / 93,6 min / 100,3 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 22:11 UTC |
| Holders / top-10 | 3.545 / 65,56% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 22:11 UTC |
| Holders efectivos del top-10 | 3,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 22:11 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 22:11 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HaGMjHTjfy7f3DN54RHix2RCWvaMZbRKszkFGXPmu9c2 · Solscan: https://solscan.io/token/2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump · pump.fun: https://pump.fun/coin/2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump · web: https://himtoken.fun/ · twitter: https://x.com/HIM_Token | consulta 02/10/2026 22:11 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 22:11 UTC)
- **Historia:**
  - Par creado el 02/10/2026 20:30 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 22:04 UTC, con el par a 93,6 min de creado: precio $0,00002158, mcap $21.133, liquidez $12.154.
  - Velas de 1 h de GeckoTerminal (3, desde 02/10/2026 20:00 UTC): apertura $0,00004849 · máximo $0,0005129 (02/10/2026 20:00 UTC) · mínimo $0,00001550 (02/10/2026 20:00 UTC) · último cierre $0,00002064.
  - En la consulta 02/10/2026 22:11 UTC: precio $0,00002054, liquidez $11.806, FDV $20.116.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 22:04 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00002158 |
| Liquidez | $12.154 |
| MCap | $21.133 |
| Volumen 24 h | $1.445.168 |
| Cambio 24 h | -56% |
| Cambio m5 / h1 | -8,4% / -71,2% |
| Volumen m5 / h1 | $1.667 / $78.462 |
| Trades m5 (compras / ventas) | 23 / 15 |
| Edad del par | 93,6 min |
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

Desglose no reproducible desde los motivos registrados (suma 58 vs score 60; motivos sin regla: Anticipación (lib_early_signals early-0.2): +2 — buy_pressure_shift: compras 61% en 5 min vs 51% en 1 h → +0.99; holder_accumulation: holders 3021→3611 (+8.8/min) · top10 33.4%→62.8% → +1.75): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T22:04:35+00:00, sin estado previo): **58** · motivos: MCap bajo, Volumen masivo, Buy pressure >60%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 10 de 8.967 tokens analizados (0,11%) quedan ≥ 56. Con score 58, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 22:04 UTC, hasta 04/10/2026 22:04 UTC · vigente: quedan 47,9 h.
- **Aceleración al detectar:** cambio m5 -8,4% · h1 -71,2% · h24 -56% · volumen m5/h1 0,02 · edad del par 93,6 min.
- **Precio de entrada** (alerta): $0,00002158.
- **Consulta 02/10/2026 22:11 UTC:** $0,00002054 (-4,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump_2026-10-02_220435.json` · blob `05fbcdbc24d5620905eb4921b8c97972468e40b6` · commit `e7c2b9d` (2026-10-02T22:04:41Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_220435`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump · registro · 02/10/2026 22:04 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump · HTTP 200 · 02/10/2026 22:11 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump/report · HTTP 200 · 02/10/2026 22:11 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump · HTTP 200 · 02/10/2026 22:11 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HaGMjHTjfy7f3DN54RHix2RCWvaMZbRKszkFGXPmu9c2/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 22:11 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump · HTTP 404 · 02/10/2026 22:11 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HIMUSDT · HTTP 400 · 02/10/2026 22:11 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HIM-USD · HTTP 404 · 02/10/2026 22:11 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $11.806 vs $11.809 → 0,03%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00002054 vs $0,00002064 → 0,49%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump_2026-10-02_220435.json',encoding='utf-8'));d=d.get('2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump',d);p=mock.patch('time.time',return_value=1790978675);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2bHz7Uq8arFttDotBgGFsVKXxN2n7hM39Cktna69pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 22:11 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `7f92c917a65d90b0…`
