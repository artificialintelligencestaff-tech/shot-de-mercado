# TrenchBrain (TRENCHBRAIN) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00007171 · liquidez $21.987 · mcap $71.715 (al detectar)  
Detectado el 09/10/2026 15:13 UTC por: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 23.2 · estructura 12.9 · precio/volumen 10.0 · cobertura 93/100, [info] narrative_wave: ola 'trenchbrain': 13 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 1 caracteres → +5.3 (score 46, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 11/10/2026 15:13 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir TRENCHBRAIN

Estudio de cómo se adquiere TRENCHBRAIN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 09/10/2026 15:39 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 09/10/2026 15:13 UTC | pumpswap `E1RtTMJ…jvCJ` | $21.987 | 10% | 0,910% | 9,096% | 90,963% | $110 | $330 |
| consulta 09/10/2026 15:39 UTC | pumpswap `E1RtTMJ…jvCJ` | $7.984 | 10% | 2,505% | 25,052% | 250,515% | $40 | $120 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump`
5. Configurar el slippage: 10% (liquidez $7.984, consulta 09/10/2026 15:39 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump) y el par en DexScreener (https://dexscreener.com/solana/E1RtTMJ5wsZnGJfHbW7Wq7TjnzdyidFWB9JUMMFpjvCJ); mint authority / freeze authority: revocada / revocada · holders 1.924 · top-10 65,32% (consulta 09/10/2026 15:39 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump
- Par en DexScreener: https://dexscreener.com/solana/E1RtTMJ5wsZnGJfHbW7Wq7TjnzdyidFWB9JUMMFpjvCJ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.924 · top-10 65,32% (consulta 09/10/2026 15:39 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | TrenchBrain / TRENCHBRAIN | registro de la detección (pumpportal_live) |
| Mint / contrato | `BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `E1RtTMJ5wsZnGJfHbW7Wq7TjnzdyidFWB9JUMMFpjvCJ` | DexScreener, al detectar (3 par(es) en la consulta 09/10/2026 15:39 UTC) |
| Deployer | `AvcWA3ngM55sSpjh1FZthmqA7V6BHo4f555a8w3Wv3ij` | PumpPortal (evento create), al detectar |
| Par creado | 09/10/2026 15:02 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,4 min / 10,4 min / 37,1 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 09/10/2026 15:39 UTC |
| Holders / top-10 | 1.924 / 65,32% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 09/10/2026 15:39 UTC |
| Holders efectivos del top-10 | 2,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 09/10/2026 15:39 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 09/10/2026 15:39 UTC |
| Links | DexScreener: https://dexscreener.com/solana/E1RtTMJ5wsZnGJfHbW7Wq7TjnzdyidFWB9JUMMFpjvCJ · Solscan: https://solscan.io/token/BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump · pump.fun: https://pump.fun/coin/BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump · web / Telegram / X: no publicados en DexScreener | consulta 09/10/2026 15:39 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 09/10/2026 15:39 UTC)
- **Historia:**
  - Par creado el 09/10/2026 15:02 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 09/10/2026 15:13 UTC, con el par a 10,4 min de creado: precio $0,00007171, mcap $71.715, liquidez $21.987.
  - Velas de 1 h de GeckoTerminal (1, desde 09/10/2026 15:00 UTC): apertura $0,00004501 · máximo $0,00008929 (09/10/2026 15:00 UTC) · mínimo $0,00001107 (09/10/2026 15:00 UTC) · último cierre $0,00001214.
  - En la consulta 09/10/2026 15:39 UTC: precio $0,00001214, liquidez $7.984, FDV $11.740.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 09/10/2026 15:13 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00007171 |
| Liquidez | $21.987 |
| MCap | $71.715 |
| Volumen 24 h | $135.695 |
| Cambio 24 h | +56% |
| Cambio m5 / h1 | -13,6% / +56,0% |
| Volumen m5 / h1 | $54.663 / $135.695 |
| Trades m5 (compras / ventas) | 753 / 531 |
| Edad del par | 10,4 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 46; motivos sin regla: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 23.2 · estructura 12.9 · precio/volumen 10.0 · cobertura 93/100, [info] narrative_wave: ola 'trenchbrain': 13 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 1 caracteres → +5.3, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1519 · top-10 33.7 % → +2.4, [estructura] dev_wallet: creador compró 9.6 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1519/3334 = 0.46 → +0.7, [precio/volumen] volume_acceleration: vol 5 min ×4.8 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +14% en 8 min (s 0.48), [precio/volumen] holder_accumulation: holders 537→1519 (+163.7/min) · top10 36.7%→33.7% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=21986.95, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 46 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-09T15:13:01+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 40 de 24.991 tokens analizados (0,16%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 09/10/2026 15:13 UTC, hasta 11/10/2026 15:13 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 -13,6% · h1 +56,0% · h24 +56% · volumen m5/h1 0,40 · edad del par 10,4 min.
- **Precio de entrada** (alerta): $0,00007171.
- **Consulta 09/10/2026 15:39 UTC:** $0,00001214 (-83,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump_2026-10-09_151301.json` · blob `8ec08491dc00685dc3596afa91e1ab207fd628a2` · commit `c552614` (2026-10-09T15:33:22Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-09_145633.json` · blob `fd062d16e10510c47fd4778900b45fdaff27214a` · commit `c552614` (2026-10-09T15:33:22Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-09_151301`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump · registro · 09/10/2026 15:13 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump · HTTP 200 · 09/10/2026 15:39 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump/report · HTTP 200 · 09/10/2026 15:39 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump · HTTP 200 · 09/10/2026 15:39 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/E1RtTMJ5wsZnGJfHbW7Wq7TjnzdyidFWB9JUMMFpjvCJ/ohlcv/hour?limit=1000 · HTTP 200 · 09/10/2026 15:39 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump · HTTP 404 · 09/10/2026 15:39 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=TRENCHBRAINUSDT · HTTP 400 · 09/10/2026 15:39 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/TRENCHBRAIN-USD · HTTP 404 · 09/10/2026 15:39 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $7.984 vs $7.985 → 0,01%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00001214 vs $0,00001214 → 0,03%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump_2026-10-09_151301.json',encoding='utf-8'));d=d.get('BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump',d);p=mock.patch('time.time',return_value=1791558781);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint BSjxk551K959ukmXUHwEY1qcWChvxPFetFf6HWGEpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 09/10/2026 15:39 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `d3b8fc2e31a02dbe…`
