# Switched Games (SWITCHED) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0004895 · liquidez $63.681 · mcap $489.532 (al detectar)  
Detectado el 10/10/2026 05:29 UTC por: young-0.4 · edad 26.7 min · pesos info 52 / estructura 24 / precio 24 · info 11.6 · estructura 18.2 · precio/volumen 11.4 · cobertura 85/100, [info] narrative_wave: ola 'switched': 4 lanzamientos más en 1 h → +6.5, [info] dex_profile: perfil pago en DexScreener → +2.6 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 12/10/2026 05:29 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SWITCHED

Estudio de cómo se adquiere SWITCHED, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 10/10/2026 05:55 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 10/10/2026 05:29 UTC | pumpswap `BFWTFa7…WaKt` | $63.681 | 5% | 0,314% | 3,141% | 31,406% | $318 | $955 |
| consulta 10/10/2026 05:55 UTC | pumpswap `BFWTFa7…WaKt` | $66.731 | 5% | 0,300% | 2,997% | 29,971% | $334 | $1.001 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump`
5. Configurar el slippage: 5% (liquidez $66.731, consulta 10/10/2026 05:55 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump) y el par en DexScreener (https://dexscreener.com/solana/BFWTFa7QR4knm3AwpdicA7uNytnw1wi13LHQT9TCWaKt); mint authority / freeze authority: revocada / revocada · holders 5.229 · top-10 23,26% (consulta 10/10/2026 05:55 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump
- Par en DexScreener: https://dexscreener.com/solana/BFWTFa7QR4knm3AwpdicA7uNytnw1wi13LHQT9TCWaKt
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.229 · top-10 23,26% (consulta 10/10/2026 05:55 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Switched Games / SWITCHED | registro de la detección (pumpportal_live) |
| Mint / contrato | `8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BFWTFa7QR4knm3AwpdicA7uNytnw1wi13LHQT9TCWaKt` | DexScreener, al detectar (10 par(es) en la consulta 10/10/2026 05:55 UTC) |
| Deployer | `DJQwtiowTJmAvAu4vhCaFgPiS3nnKD5r5agZgBQEdHK2` | PumpPortal (evento create), al detectar |
| Par creado | 10/10/2026 05:02 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 26,7 min / 26,7 min / 52,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 10/10/2026 05:55 UTC |
| Holders / top-10 | 5.229 / 23,26% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 10/10/2026 05:55 UTC |
| Holders efectivos del top-10 | 7,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 10/10/2026 05:55 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 10/10/2026 05:55 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BFWTFa7QR4knm3AwpdicA7uNytnw1wi13LHQT9TCWaKt · Solscan: https://solscan.io/token/8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump · pump.fun: https://pump.fun/coin/8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump · web: https://webibag.com · twitter: https://x.com/search?q=$SWITCHED | consulta 10/10/2026 05:55 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 10/10/2026 05:55 UTC)
- **Historia:**
  - Par creado el 10/10/2026 05:02 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 10/10/2026 05:29 UTC, con el par a 26,7 min de creado: precio $0,0004895, mcap $489.532, liquidez $63.681.
  - Velas de 1 h de GeckoTerminal (1, desde 10/10/2026 05:00 UTC): apertura $0,00004350 · máximo $0,0006616 (10/10/2026 05:00 UTC) · mínimo $0,00004103 (10/10/2026 05:00 UTC) · último cierre $0,0004706.
  - En la consulta 10/10/2026 05:55 UTC: precio $0,0005129, liquidez $66.731, FDV $499.861.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 10/10/2026 05:29 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0004895 |
| Liquidez | $63.681 |
| MCap | $489.532 |
| Volumen 24 h | $691.185 |
| Cambio 24 h | +1.025% |
| Cambio m5 / h1 | +31,8% / +1.025,0% |
| Volumen m5 / h1 | $165.308 / $691.185 |
| Trades m5 (compras / ventas) | 944 / 1.116 |
| Edad del par | 26,7 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 26.7 min · pesos info 52 / estructura 24 / precio 24 · info 11.6 · estructura 18.2 · precio/volumen 11.4 · cobertura 85/100, [info] narrative_wave: ola 'switched': 4 lanzamientos más en 1 h → +6.5, [info] dex_profile: perfil pago en DexScreener → +2.6, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +2.6, [estructura] bonding_progress: graduado (pumpswap) → +11.6, [estructura] holders_struct: holders 3651 · top-10 22.4 % → +5.8, [estructura] dev_wallet: creador compró 9.6 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 3651/10560 = 0.35 → +0.7, [precio/volumen] volume_acceleration: vol 5 min ×2.9 la tasa horaria (s 0.55), [precio/volumen] liquidity_inflow: liquidez +52% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 2871→3651 (+130.0/min) · top10 24.7%→22.4% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=63681.43, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-10T05:29:37+00:00, sin estado previo): **50** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=13.0% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 43 de 26.507 tokens analizados (0,16%) quedan ≥ 56. Con score 50, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 10/10/2026 05:29 UTC, hasta 12/10/2026 05:29 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +31,8% · h1 +1.025,0% · h24 +1.025% · volumen m5/h1 0,24 · edad del par 26,7 min.
- **Precio de entrada** (alerta): $0,0004895.
- **Consulta 10/10/2026 05:55 UTC:** $0,0005129 (+4,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump_2026-10-10_052937.json` · blob `6281816e26dabbb9d0e7948d17a62d3e456939cb` · commit `aa3ad44` (2026-10-10T05:49:07Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-10_052937`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump · registro · 10/10/2026 05:29 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump · HTTP 200 · 10/10/2026 05:55 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump/report · HTTP 200 · 10/10/2026 05:55 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump · HTTP 200 · 10/10/2026 05:55 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BFWTFa7QR4knm3AwpdicA7uNytnw1wi13LHQT9TCWaKt/ohlcv/hour?limit=1000 · HTTP 200 · 10/10/2026 05:55 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump · HTTP 404 · 10/10/2026 05:55 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SWITCHEDUSDT · HTTP 400 · 10/10/2026 05:55 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SWITCHED-USD · HTTP 404 · 10/10/2026 05:55 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $66.731 vs $113.091 → 40,99%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0005129 vs $0,0004706 → 8,24%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump_2026-10-10_052937.json',encoding='utf-8'));d=d.get('8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump',d);p=mock.patch('time.time',return_value=1791610177);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8vYJgiQPkpDtbWkDy1wyYDcUq3D9fUXVJUtt6aNEpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 10/10/2026 05:55 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `7648f9350c009952…`
