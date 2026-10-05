# ore (ore) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0002480 · liquidez $45.905 · mcap $248.032 (al detectar)  
Detectado el 05/10/2026 14:51 UTC por: young-0.4 · edad 10.0 min · pesos info 60 / estructura 20 / precio 20 · info 18.0 · estructura 17.2 · precio/volumen 12.3 · cobertura 83/100, [info] narrative_wave: ola 'ore': 10 lanzamientos más en 1 h → +15.0, [info] dex_profile: perfil pago en DexScreener → +3.0 (score 48, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 07/10/2026 14:51 UTC (< 48 h) · vigente: quedan 47,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ore

Estudio de cómo se adquiere ore, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 05/10/2026 15:00 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 05/10/2026 14:51 UTC | pumpswap `7LKLcSi…86AR` | $45.905 | 10% | 0,436% | 4,357% | 43,568% | $230 | $689 |
| consulta 05/10/2026 15:00 UTC | pumpswap `7LKLcSi…86AR` | $44.821 | 10% | 0,446% | 4,462% | 44,622% | $224 | $672 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump`
5. Configurar el slippage: 10% (liquidez $44.821, consulta 05/10/2026 15:00 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump) y el par en DexScreener (https://dexscreener.com/solana/7LKLcSiDQw9zEpM6hXekDwWqxEkw4jUcGcGVR28s86AR); mint authority / freeze authority: revocada / revocada · holders 3.919 · top-10 26,23% (consulta 05/10/2026 15:00 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump
- Par en DexScreener: https://dexscreener.com/solana/7LKLcSiDQw9zEpM6hXekDwWqxEkw4jUcGcGVR28s86AR
- Página del lanzamiento (pump.fun): https://pump.fun/coin/76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.919 · top-10 26,23% (consulta 05/10/2026 15:00 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | ore / ore | registro de la detección (pumpportal_live) |
| Mint / contrato | `76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7LKLcSiDQw9zEpM6hXekDwWqxEkw4jUcGcGVR28s86AR` | DexScreener, al detectar (4 par(es) en la consulta 05/10/2026 15:00 UTC) |
| Deployer | `F81TYBXJQTuaSk7oSM7Eb2bwRatoPZsLRic62yUDXGVt` | PumpPortal (evento create), al detectar |
| Par creado | 05/10/2026 14:41 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,0 min / 10,0 min / 18,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 05/10/2026 15:00 UTC |
| Holders / top-10 | 3.919 / 26,23% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 05/10/2026 15:00 UTC |
| Holders efectivos del top-10 | 5,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 05/10/2026 15:00 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 05/10/2026 15:00 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7LKLcSiDQw9zEpM6hXekDwWqxEkw4jUcGcGVR28s86AR · Solscan: https://solscan.io/token/76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump · pump.fun: https://pump.fun/coin/76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump · web: https://useore.fun/ · twitter: https://x.com/useorefun | consulta 05/10/2026 15:00 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 05/10/2026 15:00 UTC)
- **Historia:**
  - Par creado el 05/10/2026 14:41 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 05/10/2026 14:51 UTC, con el par a 10,0 min de creado: precio $0,0002480, mcap $248.032, liquidez $45.905.
  - Velas de 1 h de GeckoTerminal (2, desde 05/10/2026 14:00 UTC): apertura $0,00004972 · máximo $0,0003965 (05/10/2026 14:00 UTC) · mínimo $0,00002923 (05/10/2026 14:00 UTC) · último cierre $0,0002219.
  - En la consulta 05/10/2026 15:00 UTC: precio $0,0002311, liquidez $44.821, FDV $231.157.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 05/10/2026 14:51 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0002480 |
| Liquidez | $45.905 |
| MCap | $248.032 |
| Volumen 24 h | $913.123 |
| Cambio 24 h | +402% |
| Cambio m5 / h1 | -26,0% / +402,0% |
| Volumen m5 / h1 | $407.444 / $913.123 |
| Trades m5 (compras / ventas) | 2.693 / 2.013 |
| Edad del par | 10,0 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 48; motivos sin regla: young-0.4 · edad 10.0 min · pesos info 60 / estructura 20 / precio 20 · info 18.0 · estructura 17.2 · precio/volumen 12.3 · cobertura 83/100, [info] narrative_wave: ola 'ore': 10 lanzamientos más en 1 h → +15.0, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 3005 · top-10 28.6 % → +4.8, [estructura] dev_wallet: creador compró 2.0 % del supply → +2.4, [estructura] holder_to_txn_ratio: holders/txns 3005/11561 = 0.26 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×5.4 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 57% en 5 min vs 54% en 1 h (s 0.18), [precio/volumen] liquidity_inflow: liquidez +82% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1554→3005 (+241.8/min) · top10 36.3%→28.6% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=45904.93, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=25218.59, score 48 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-05T14:51:55+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 16 de 12.388 tokens analizados (0,13%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 05/10/2026 14:51 UTC, hasta 07/10/2026 14:51 UTC · vigente: quedan 47,9 h.
- **Aceleración al detectar:** cambio m5 -26,0% · h1 +402,0% · h24 +402% · volumen m5/h1 0,45 · edad del par 10,0 min.
- **Precio de entrada** (alerta): $0,0002480.
- **Consulta 05/10/2026 15:00 UTC:** $0,0002311 (-6,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump_2026-10-05_145155.json` · blob `a32424f80af24c43132b610ef0891680d4700fe2` · commit `8210e92` (2026-10-05T14:53:33Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-05_143745.json` · blob `620778747a81cb25554e4a9732be8e4d5d9c14b9` · commit `8210e92` (2026-10-05T14:53:33Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-05_145155`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump · registro · 05/10/2026 14:51 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump · HTTP 200 · 05/10/2026 15:00 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump/report · HTTP 200 · 05/10/2026 15:00 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump · HTTP 200 · 05/10/2026 15:00 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7LKLcSiDQw9zEpM6hXekDwWqxEkw4jUcGcGVR28s86AR/ohlcv/hour?limit=1000 · HTTP 200 · 05/10/2026 15:00 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump · HTTP 404 · 05/10/2026 15:00 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=OREUSDT · HTTP 400 · 05/10/2026 15:00 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ORE-USD · HTTP 404 · 05/10/2026 15:00 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $44.821 vs $51.553 → 13,06%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0002311 vs $0,0002219 → 3,98%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump_2026-10-05_145155.json',encoding='utf-8'));d=d.get('76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump',d);p=mock.patch('time.time',return_value=1791211915);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 76fvXLL5hPsr6CQUs6PrXTY7VgdyY5tPidjPrpaepump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 05/10/2026 15:00 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `de0fb76755ebfd1d…`
