# cybercurrency (CYBER) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001127 · liquidez $111.519 · mcap $1.126.631 (al detectar)  
Detectado el 21/10/2026 22:38 UTC por: young-0.4 · edad 11.1 min · pesos info 59 / estructura 20 / precio 20 · info 20.2 · estructura 14.8 · precio/volumen 11.8 · cobertura 93/100, [info] narrative_wave: ola 'cybercurrency': 75 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 47, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 23/10/2026 22:38 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir CYBER

Estudio de cómo se adquiere CYBER, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 21/10/2026 22:57 UTC; CoinGecko sin ficha para este contrato). Binance tiene un par CYBERUSDT, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza.

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 21/10/2026 22:38 UTC | pumpswap `4SMPAuR…iYiG` | $111.519 | 5% | 0,179% | 1,793% | 17,934% | $558 | $1.673 |
| consulta 21/10/2026 22:57 UTC | pumpswap `4SMPAuR…iYiG` | $99.652 | 5% | 0,201% | 2,007% | 20,070% | $498 | $1.495 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump`
5. Configurar el slippage: 5% (liquidez $99.652, consulta 21/10/2026 22:57 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump) y el par en DexScreener (https://dexscreener.com/solana/4SMPAuRkMTMFiMnW1oDcDQdi54CC9R4of9xtr4phiYiG); mint authority / freeze authority: revocada / revocada · holders 9.345 · top-10 17,37% (consulta 21/10/2026 22:57 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump
- Par en DexScreener: https://dexscreener.com/solana/4SMPAuRkMTMFiMnW1oDcDQdi54CC9R4of9xtr4phiYiG
- Página del lanzamiento (pump.fun): https://pump.fun/coin/CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 9.345 · top-10 17,37% (consulta 21/10/2026 22:57 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | cybercurrency / CYBER | registro de la detección (pumpportal_live) |
| Mint / contrato | `CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `4SMPAuRkMTMFiMnW1oDcDQdi54CC9R4of9xtr4phiYiG` | DexScreener, al detectar (30 par(es) en la consulta 21/10/2026 22:57 UTC) |
| Deployer | `F5XvCe4233m6mHRbkkq2ZsFvqrPAnRrDBExeQy2fwagQ` | PumpPortal (evento create), al detectar |
| Par creado | 21/10/2026 22:27 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,1 min / 11,1 min / 30,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 21/10/2026 22:57 UTC |
| Holders / top-10 | 9.345 / 17,37% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 21/10/2026 22:57 UTC |
| Holders efectivos del top-10 | 7,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 21/10/2026 22:57 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 21/10/2026 22:57 UTC |
| Links | DexScreener: https://dexscreener.com/solana/4SMPAuRkMTMFiMnW1oDcDQdi54CC9R4of9xtr4phiYiG · Solscan: https://solscan.io/token/CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump · pump.fun: https://pump.fun/coin/CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump · web / Telegram / X: no publicados en DexScreener | consulta 21/10/2026 22:57 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 21/10/2026 22:57 UTC)
- **Historia:**
  - Par creado el 21/10/2026 22:27 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 21/10/2026 22:38 UTC, con el par a 11,1 min de creado: precio $0,001127, mcap $1.126.631, liquidez $111.519.
  - Velas de 1 h de GeckoTerminal (1, desde 21/10/2026 22:00 UTC): apertura $0,00004419 · máximo $0,001511 (21/10/2026 22:00 UTC) · mínimo $0,00002246 (21/10/2026 22:00 UTC) · último cierre $0,0009759.
  - En la consulta 21/10/2026 22:57 UTC: precio $0,001025, liquidez $99.652, FDV $1.024.056.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 21/10/2026 22:38 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001127 |
| Liquidez | $111.519 |
| MCap | $1.126.631 |
| Volumen 24 h | $2.391.242 |
| Cambio 24 h | +2.430% |
| Cambio m5 / h1 | +316,0% / +2.430,0% |
| Volumen m5 / h1 | $1.776.476 / $2.391.242 |
| Trades m5 (compras / ventas) | 7.176 / 8.259 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 47; motivos sin regla: young-0.4 · edad 11.1 min · pesos info 59 / estructura 20 / precio 20 · info 20.2 · estructura 14.8 · precio/volumen 11.8 · cobertura 93/100, [info] narrative_wave: ola 'cybercurrency': 75 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 2466 · top-10 23.6 % → +4.9, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 2466/24119 = 0.10 → +0.2, [precio/volumen] volume_acceleration: vol 5 min ×8.9 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +369% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 674→2466 (+298.7/min) · top10 39.6%→23.6% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=111518.87, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 47 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-21T22:38:12+00:00, sin estado previo): **70** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen masivo, Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=9.9% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 73 de 43.476 tokens analizados (0,17%) quedan ≥ 56. Con score 70, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 21/10/2026 22:38 UTC, hasta 23/10/2026 22:38 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +316,0% · h1 +2.430,0% · h24 +2.430% · volumen m5/h1 0,74 · edad del par 11,1 min.
- **Precio de entrada** (alerta): $0,001127.
- **Consulta 21/10/2026 22:57 UTC:** $0,001025 (-9,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump_2026-10-21_223812.json` · blob `25e30ca21eaffb9dfb241f27fcd7740fde571e25` · commit `c15ac27` (2026-10-21T22:48:27Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-21_223812`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump · registro · 21/10/2026 22:38 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump · HTTP 200 · 21/10/2026 22:57 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump/report · HTTP 200 · 21/10/2026 22:57 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump · HTTP 200 · 21/10/2026 22:57 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/4SMPAuRkMTMFiMnW1oDcDQdi54CC9R4of9xtr4phiYiG/ohlcv/hour?limit=1000 · HTTP 200 · 21/10/2026 22:57 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump · HTTP 404 · 21/10/2026 22:57 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=CYBERUSDT · HTTP 200 · 21/10/2026 22:57 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/CYBER-USD · HTTP 404 · 21/10/2026 22:57 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $99.652 vs $230.323 → 56,73%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001025 vs $0,0009759 → 4,79%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump_2026-10-21_223812.json',encoding='utf-8'));d=d.get('CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump',d);p=mock.patch('time.time',return_value=1792622292);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint CMo7GfUhSGXuEfnY7qAzv8hhsV2M2P8GpWqmWikhpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 21/10/2026 22:57 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `e57bb3709625db8b…`
