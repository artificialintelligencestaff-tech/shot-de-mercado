# Anti Inu (AI) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00006291 · liquidez $22.583 · mcap $61.726 (al detectar)  
Detectado el 02/10/2026 15:37 UTC por: MCap > $50K, Volumen masivo, Buy pressure >55% (score 75, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 04/10/2026 15:37 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir AI

Estudio de cómo se adquiere AI, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 15:57 UTC; CoinGecko sin ficha para este contrato). Binance tiene un par AIUSDT, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza. Coinbase tiene un par AI-USD, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza.

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 15:37 UTC | pumpswap `HMA4mob…6pGQ` | $22.583 | 10% | 0,886% | 8,856% | 88,563% | $113 | $339 |
| consulta 02/10/2026 15:57 UTC | pumpswap `HMA4mob…6pGQ` | $16.055 | 10% | 1,246% | 12,457% | 124,569% | $80 | $241 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS`
5. Configurar el slippage: 10% (liquidez $16.055, consulta 02/10/2026 15:57 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS) y el par en DexScreener (https://dexscreener.com/solana/HMA4mobg9tRvT1tQvgkv2EGXRBFCkx1Huje4DPhN6pGQ); mint authority / freeze authority: revocada / revocada · holders 3.167 · top-10 48,85% (consulta 02/10/2026 15:57 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS
- Par en DexScreener: https://dexscreener.com/solana/HMA4mobg9tRvT1tQvgkv2EGXRBFCkx1Huje4DPhN6pGQ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.167 · top-10 48,85% (consulta 02/10/2026 15:57 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Anti Inu / AI | registro de la detección (pumpportal) |
| Mint / contrato | `HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HMA4mobg9tRvT1tQvgkv2EGXRBFCkx1Huje4DPhN6pGQ` | DexScreener, al detectar (4 par(es) en la consulta 02/10/2026 15:57 UTC) |
| Deployer | `9jwfZT1V4rvG8ZRdfR8gQfu9yYKSmZeejBEhmpPgYtPv` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 14:36 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 61,3 min / 61,3 min / 81,0 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 15:57 UTC |
| Holders / top-10 | 3.167 / 48,85% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 15:57 UTC |
| Holders efectivos del top-10 | 2,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 15:57 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 15:57 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HMA4mobg9tRvT1tQvgkv2EGXRBFCkx1Huje4DPhN6pGQ · Solscan: https://solscan.io/token/HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS · pump.fun: https://pump.fun/coin/HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS · web: https://x.com/SnowHimbo/status/2105797935975862685?s=20 · twitter: https://x.com/Infinitidigits/status/2106034173563502593?s=20 | consulta 02/10/2026 15:57 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 15:57 UTC)
- **Historia:**
  - Par creado el 02/10/2026 14:36 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 15:37 UTC, con el par a 61,3 min de creado: precio $0,00006291, mcap $61.726, liquidez $22.583.
  - Velas de 1 h de GeckoTerminal (2, desde 02/10/2026 14:00 UTC): apertura $0,00004911 · máximo $0,0002542 (02/10/2026 14:00 UTC) · mínimo $0,00002443 (02/10/2026 15:00 UTC) · último cierre $0,00003236.
  - En la consulta 02/10/2026 15:57 UTC: precio $0,00003392, liquidez $16.055, FDV $33.279.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 15:37 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00006291 |
| Liquidez | $22.583 |
| MCap | $61.726 |
| Volumen 24 h | $1.217.666 |
| Cambio 24 h | +28% |
| Cambio m5 / h1 | +14,0% / -30,8% |
| Volumen m5 / h1 | $19.647 / $1.120.166 |
| Trades m5 (compras / ventas) | 148 / 117 |
| Edad del par | 61,3 min |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 1/2 (50,0%, IC90 12,1%–87,9%) · secundaria 0/1 resueltas (shadow_monitor.json).

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

Desglose no reproducible desde los motivos registrados (suma 73 vs score 75; motivos sin regla: Anticipación (lib_early_signals early-0.2): +2 — buy_pressure_shift: compras 56% en 5 min vs 55% en 1 h → +0.12; liquidity_inflow: liquidez +12% en 8 min → +0.78; holder_accumulation: holders 3083→3155 (+12.0/min) · top10 31.4%→31.1% → +2): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T15:37:53+00:00, sin estado previo): **73** · motivos: MCap > $50K, Volumen masivo, Buy pressure >55%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez mínima, Subida 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 10 de 7.933 tokens analizados (0,13%) quedan ≥ 56. Con score 73, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 15:37 UTC, hasta 04/10/2026 15:37 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +14,0% · h1 -30,8% · h24 +28% · volumen m5/h1 0,02 · edad del par 61,3 min.
- **Precio de entrada** (alerta): $0,00006291.
- **Consulta 02/10/2026 15:57 UTC:** $0,00003392 (-46,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS_2026-10-02_153753.json` · blob `9f97023c4c725441caf5cb5830fb9058cf2d1797` · commit `af0c9e5` (2026-10-02T15:51:12Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_153753`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS · registro · 02/10/2026 15:37 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS · HTTP 200 · 02/10/2026 15:57 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS/report · HTTP 200 · 02/10/2026 15:57 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS · HTTP 200 · 02/10/2026 15:57 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HMA4mobg9tRvT1tQvgkv2EGXRBFCkx1Huje4DPhN6pGQ/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 15:57 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS · HTTP 404 · 02/10/2026 15:57 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AIUSDT · HTTP 200 · 02/10/2026 15:57 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AI-USD · HTTP 200 · 02/10/2026 15:57 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $16.055 vs $15.619 → 2,72%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00003392 vs $0,00003236 → 4,59%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS_2026-10-02_153753.json',encoding='utf-8'));d=d.get('HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS',d);p=mock.patch('time.time',return_value=1790955473);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HvRdz7YWW1ksGU9gAH4TzfHccjAoajXg2Rp4GXhsdMCS --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 15:57 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `cda43b8eef1a7c0a…`
