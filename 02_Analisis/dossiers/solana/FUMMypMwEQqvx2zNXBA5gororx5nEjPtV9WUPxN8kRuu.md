# Elon Coin (ELON) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001676 · liquidez $35.771 · mcap $167.617 (al detectar)  
Detectado el 24/10/2026 00:35 UTC por: young-0.4 · edad 11.7 min · pesos info 59 / estructura 20 / precio 20 · info 12.6 · estructura 14.8 · precio/volumen 12.3 · cobertura 93/100, [info] narrative_wave: ola 'elon': 4 lanzamientos más en 1 h → +7.4, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 40, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 26/10/2026 00:35 UTC (< 48 h) · vigente: quedan 47,3 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ELON

Estudio de cómo se adquiere ELON, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 24/10/2026 01:18 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 24/10/2026 00:35 UTC | pumpswap `ETvPPim…Y4vP` | $35.771 | 10% | 0,559% | 5,591% | 55,911% | $179 | $537 |
| consulta 24/10/2026 01:18 UTC | pumpswap `ETvPPim…Y4vP` | $49.187 | 10% | 0,407% | 4,066% | 40,661% | $246 | $738 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu`
5. Configurar el slippage: 10% (liquidez $49.187, consulta 24/10/2026 01:18 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu) y el par en DexScreener (https://dexscreener.com/solana/ETvPPimBeoPUy5gEpjiQjUpS8f1TsVzZ2MxUErwaY4vP); mint authority / freeze authority: revocada / revocada · holders 5.365 · top-10 25,76% (consulta 24/10/2026 01:18 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu
- Par en DexScreener: https://dexscreener.com/solana/ETvPPimBeoPUy5gEpjiQjUpS8f1TsVzZ2MxUErwaY4vP
- Página del lanzamiento (pump.fun): https://pump.fun/coin/FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.365 · top-10 25,76% (consulta 24/10/2026 01:18 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Elon Coin / ELON | registro de la detección (pumpportal_live) |
| Mint / contrato | `FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `ETvPPimBeoPUy5gEpjiQjUpS8f1TsVzZ2MxUErwaY4vP` | DexScreener, al detectar (30 par(es) en la consulta 24/10/2026 01:18 UTC) |
| Deployer | `rF4LKbHN3KndKUuznN8HHcRFonKJh8mKEAAFkeVAg5T` | PumpPortal (evento create), al detectar |
| Par creado | 24/10/2026 00:23 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,7 min / 11,7 min / 54,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 24/10/2026 01:18 UTC |
| Holders / top-10 | 5.365 / 25,76% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 24/10/2026 01:18 UTC |
| Holders efectivos del top-10 | 5,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 24/10/2026 01:18 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 24/10/2026 01:18 UTC |
| Links | DexScreener: https://dexscreener.com/solana/ETvPPimBeoPUy5gEpjiQjUpS8f1TsVzZ2MxUErwaY4vP · Solscan: https://solscan.io/token/FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu · pump.fun: https://pump.fun/coin/FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu · twitter: https://x.com/flightxbt/status/2113787939964715117 | consulta 24/10/2026 01:18 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 24/10/2026 01:18 UTC)
- **Historia:**
  - Par creado el 24/10/2026 00:23 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 24/10/2026 00:35 UTC, con el par a 11,7 min de creado: precio $0,0001676, mcap $167.617, liquidez $35.771.
  - Velas de 1 h de GeckoTerminal (2, desde 24/10/2026 00:00 UTC): apertura $0,00004289 · máximo $0,0004749 (24/10/2026 01:00 UTC) · mínimo $0,00001202 (24/10/2026 00:00 UTC) · último cierre $0,0002796.
  - En la consulta 24/10/2026 01:18 UTC: precio $0,0002980, liquidez $49.187, FDV $283.476.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 24/10/2026 00:35 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001676 |
| Liquidez | $35.771 |
| MCap | $167.617 |
| Volumen 24 h | $350.711 |
| Cambio 24 h | +294% |
| Cambio m5 / h1 | +69,3% / +294,0% |
| Volumen m5 / h1 | $119.219 / $350.711 |
| Trades m5 (compras / ventas) | 1.372 / 1.050 |
| Edad del par | 11,7 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 40; motivos sin regla: young-0.4 · edad 11.7 min · pesos info 59 / estructura 20 / precio 20 · info 12.6 · estructura 14.8 · precio/volumen 12.3 · cobertura 93/100, [info] narrative_wave: ola 'elon': 4 lanzamientos más en 1 h → +7.4, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 1909 · top-10 30.5 % → +2.5, [estructura] dev_wallet: creador compró 3.1 % del supply → +2.1, [estructura] holder_to_txn_ratio: holders/txns 1909/7146 = 0.27 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×4.1 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 57% en 5 min vs 55% en 1 h (s 0.10), [precio/volumen] liquidity_inflow: liquidez +75% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1113→1909 (+132.7/min) · top10 36.3%→30.5% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=35771.07, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=11273.84, score 40 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-24T00:35:23+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 75 de 45.392 tokens analizados (0,17%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 24/10/2026 00:35 UTC, hasta 26/10/2026 00:35 UTC · vigente: quedan 47,3 h.
- **Aceleración al detectar:** cambio m5 +69,3% · h1 +294,0% · h24 +294% · volumen m5/h1 0,34 · edad del par 11,7 min.
- **Precio de entrada** (alerta): $0,0001676.
- **Consulta 24/10/2026 01:18 UTC:** $0,0002980 (+77,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu_2026-10-24_003523.json` · blob `66c2bfd0bba9bf025c68306c3525e7706842be55` · commit `4ba0ece` (2026-10-24T01:11:16Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-24_002010.json` · blob `f0eb9e9bc9f9f24da1a7cd2a2041cbdfa6d81bc6` · commit `4ba0ece` (2026-10-24T01:11:16Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-24_003523`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu · registro · 24/10/2026 00:35 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu · HTTP 200 · 24/10/2026 01:18 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu/report · HTTP 200 · 24/10/2026 01:18 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu · HTTP 200 · 24/10/2026 01:18 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/ETvPPimBeoPUy5gEpjiQjUpS8f1TsVzZ2MxUErwaY4vP/ohlcv/hour?limit=1000 · HTTP 200 · 24/10/2026 01:18 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu · HTTP 404 · 24/10/2026 01:18 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ELONUSDT · HTTP 400 · 24/10/2026 01:18 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ELON-USD · HTTP 404 · 24/10/2026 01:18 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $49.187 vs $57.917 → 15,07%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0002980 vs $0,0002796 → 6,19%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu_2026-10-24_003523.json',encoding='utf-8'));d=d.get('FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu',d);p=mock.patch('time.time',return_value=1792802123);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint FUMMypMwEQqvx2zNXBA5gororx5nEjPtV9WUPxN8kRuu --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 24/10/2026 01:18 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `8b60a8c43a117231…`
