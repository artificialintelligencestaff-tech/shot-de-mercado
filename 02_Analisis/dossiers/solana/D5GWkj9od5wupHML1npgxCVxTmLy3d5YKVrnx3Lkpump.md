# Super Intelligence Cat (Ollie) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001132 · liquidez $28.493 · mcap $113.227 (al detectar)  
Detectado el 10/10/2026 22:43 UTC por: young-0.4 · edad 10.9 min · pesos info 60 / estructura 20 / precio 20 · info 20.2 · estructura 15.5 · precio/volumen 11.9 · cobertura 93/100, [info] narrative_wave: ola 'cat': 12 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 29 caracteres → +5.3 (score 47, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 12/10/2026 22:43 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Ollie

Estudio de cómo se adquiere Ollie, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 10/10/2026 23:11 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 10/10/2026 22:43 UTC | pumpswap `3wrSvKS…KL5L` | $28.493 | 10% | 0,702% | 7,019% | 70,192% | $142 | $427 |
| consulta 10/10/2026 23:11 UTC | pumpswap `3wrSvKS…KL5L` | $60.263 | 5% | 0,332% | 3,319% | 33,188% | $301 | $904 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump`
5. Configurar el slippage: 5% (liquidez $60.263, consulta 10/10/2026 23:11 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump) y el par en DexScreener (https://dexscreener.com/solana/3wrSvKSY2FTCsevNA1afrK9wz68CDpQGk26WhJmvKL5L); mint authority / freeze authority: revocada / revocada · holders 3.972 · top-10 24,23% (consulta 10/10/2026 23:11 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump
- Par en DexScreener: https://dexscreener.com/solana/3wrSvKSY2FTCsevNA1afrK9wz68CDpQGk26WhJmvKL5L
- Página del lanzamiento (pump.fun): https://pump.fun/coin/D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.972 · top-10 24,23% (consulta 10/10/2026 23:11 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Super Intelligence Cat / Ollie | registro de la detección (pumpportal_live) |
| Mint / contrato | `D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `3wrSvKSY2FTCsevNA1afrK9wz68CDpQGk26WhJmvKL5L` | DexScreener, al detectar (4 par(es) en la consulta 10/10/2026 23:11 UTC) |
| Deployer | `GV5HwG2qWmzSLsQu5xpbztyRddtokKgPtJdF7sXQGrKS` | PumpPortal (evento create), al detectar |
| Par creado | 10/10/2026 22:32 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,9 min / 10,9 min / 38,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 10/10/2026 23:11 UTC |
| Holders / top-10 | 3.972 / 24,23% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 10/10/2026 23:11 UTC |
| Holders efectivos del top-10 | 6,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 10/10/2026 23:11 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 10/10/2026 23:11 UTC |
| Links | DexScreener: https://dexscreener.com/solana/3wrSvKSY2FTCsevNA1afrK9wz68CDpQGk26WhJmvKL5L · Solscan: https://solscan.io/token/D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump · pump.fun: https://pump.fun/coin/D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump · web: https://usepaid.app/token/D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump · twitter: https://x.com/imBilngineer/status/2109052223850184847 | consulta 10/10/2026 23:11 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 10/10/2026 23:11 UTC)
- **Historia:**
  - Par creado el 10/10/2026 22:32 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 10/10/2026 22:43 UTC, con el par a 10,9 min de creado: precio $0,0001132, mcap $113.227, liquidez $28.493.
  - Velas de 1 h de GeckoTerminal (2, desde 10/10/2026 22:00 UTC): apertura $0,00004185 · máximo $0,0004433 (10/10/2026 23:00 UTC) · mínimo $0,00003114 (10/10/2026 22:00 UTC) · último cierre $0,0004012.
  - En la consulta 10/10/2026 23:11 UTC: precio $0,0004215, liquidez $60.263, FDV $409.237.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 10/10/2026 22:43 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001132 |
| Liquidez | $28.493 |
| MCap | $113.227 |
| Volumen 24 h | $207.835 |
| Cambio 24 h | +146% |
| Cambio m5 / h1 | +13,0% / +146,0% |
| Volumen m5 / h1 | $78.625 / $207.835 |
| Trades m5 (compras / ventas) | 733 / 584 |
| Edad del par | 10,9 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 47; motivos sin regla: young-0.4 · edad 10.9 min · pesos info 60 / estructura 20 / precio 20 · info 20.2 · estructura 15.5 · precio/volumen 11.9 · cobertura 93/100, [info] narrative_wave: ola 'cat': 12 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 29 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1962 · top-10 29.7 % → +4.9, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1962/3777 = 0.52 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×4.5 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 56% en 5 min vs 53% en 1 h (s 0.15), [precio/volumen] liquidity_inflow: liquidez +26% en 8 min (s 0.87), [precio/volumen] holder_accumulation: holders 1170→1962 (+132.0/min) · top10 37.3%→29.7% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=28493.39, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 47 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-10T22:43:19+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 45 de 28.052 tokens analizados (0,16%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 10/10/2026 22:43 UTC, hasta 12/10/2026 22:43 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +13,0% · h1 +146,0% · h24 +146% · volumen m5/h1 0,38 · edad del par 10,9 min.
- **Precio de entrada** (alerta): $0,0001132.
- **Consulta 10/10/2026 23:11 UTC:** $0,0004215 (+272,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump_2026-10-10_224319.json` · blob `5368ad6ea51f498dc34452a942f53c3e11627e23` · commit `4607f8a` (2026-10-10T23:03:43Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-10_224319`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump · registro · 10/10/2026 22:43 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump · HTTP 200 · 10/10/2026 23:11 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump/report · HTTP 200 · 10/10/2026 23:11 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump · HTTP 200 · 10/10/2026 23:11 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/3wrSvKSY2FTCsevNA1afrK9wz68CDpQGk26WhJmvKL5L/ohlcv/hour?limit=1000 · HTTP 200 · 10/10/2026 23:11 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump · HTTP 404 · 10/10/2026 23:11 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=OLLIEUSDT · HTTP 400 · 10/10/2026 23:11 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/OLLIE-USD · HTTP 404 · 10/10/2026 23:11 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $60.263 vs $61.515 → 2,04%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0004215 vs $0,0004012 → 4,81%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump_2026-10-10_224319.json',encoding='utf-8'));d=d.get('D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump',d);p=mock.patch('time.time',return_value=1791672199);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint D5GWkj9od5wupHML1npgxCVxTmLy3d5YKVrnx3Lkpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 10/10/2026 23:11 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `29231ae37df50f7c…`
