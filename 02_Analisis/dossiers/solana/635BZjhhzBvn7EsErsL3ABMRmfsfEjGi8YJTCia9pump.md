# Solana Intelligence (VECTOR) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0002677 · liquidez $47.217 · mcap $262.404 (al detectar)  
Detectado el 22/10/2026 14:06 UTC por: MCap > $100K, Volumen masivo, Momentum corto+medio positivo (score 89, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 24/10/2026 14:06 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir VECTOR

Estudio de cómo se adquiere VECTOR, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 22/10/2026 14:34 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 22/10/2026 14:06 UTC | pumpswap `92KgVDB…fWA1` | $47.217 | 10% | 0,424% | 4,236% | 42,357% | $236 | $708 |
| consulta 22/10/2026 14:34 UTC | pumpswap `92KgVDB…fWA1` | $31.815 | 10% | 0,629% | 6,286% | 62,863% | $159 | $477 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump`
5. Configurar el slippage: 10% (liquidez $31.815, consulta 22/10/2026 14:34 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump) y el par en DexScreener (https://dexscreener.com/solana/92KgVDBs9TSRBX5XxYJRczFRsawA4sLTaKWnMDAJfWA1); mint authority / freeze authority: revocada / revocada · holders 4.996 · top-10 28,16% (consulta 22/10/2026 14:34 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump
- Par en DexScreener: https://dexscreener.com/solana/92KgVDBs9TSRBX5XxYJRczFRsawA4sLTaKWnMDAJfWA1
- Página del lanzamiento (pump.fun): https://pump.fun/coin/635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.996 · top-10 28,16% (consulta 22/10/2026 14:34 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Solana Intelligence / VECTOR | registro de la detección (pumpportal) |
| Mint / contrato | `635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `92KgVDBs9TSRBX5XxYJRczFRsawA4sLTaKWnMDAJfWA1` | DexScreener, al detectar (22 par(es) en la consulta 22/10/2026 14:34 UTC) |
| Deployer | `4vDQL6RdQWH2F3jn2omShCQTbU2YMHYMVqxeFVEaJKCa` | PumpPortal (evento create), al detectar |
| Par creado | 22/10/2026 13:04 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 61,8 min / 61,8 min / 90,2 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 22/10/2026 14:34 UTC |
| Holders / top-10 | 4.996 / 28,16% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 22/10/2026 14:34 UTC |
| Holders efectivos del top-10 | 3,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 22/10/2026 14:34 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 22/10/2026 14:34 UTC |
| Links | DexScreener: https://dexscreener.com/solana/92KgVDBs9TSRBX5XxYJRczFRsawA4sLTaKWnMDAJfWA1 · Solscan: https://solscan.io/token/635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump · pump.fun: https://pump.fun/coin/635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump · web: https://solana.com/docs/ask?q=test · twitter: https://x.com/NormieCoinCTO/status/2113262057508474918 | consulta 22/10/2026 14:34 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 22/10/2026 14:34 UTC)
- **Historia:**
  - Par creado el 22/10/2026 13:04 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 22/10/2026 14:06 UTC, con el par a 61,8 min de creado: precio $0,0002677, mcap $262.404, liquidez $47.217.
  - Velas de 1 h de GeckoTerminal (2, desde 22/10/2026 13:00 UTC): apertura $0,00004282 · máximo $0,0004771 (22/10/2026 13:00 UTC) · mínimo $0,00001672 (22/10/2026 13:00 UTC) · último cierre $0,0001254.
  - En la consulta 22/10/2026 14:34 UTC: precio $0,0001267, liquidez $31.815, FDV $124.235.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 22/10/2026 14:06 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0002677 |
| Liquidez | $47.217 |
| MCap | $262.404 |
| Volumen 24 h | $1.717.727 |
| Cambio 24 h | +495% |
| Cambio m5 / h1 | +34,5% / +320,0% |
| Volumen m5 / h1 | $34.435 / $1.586.049 |
| Trades m5 (compras / ventas) | 336 / 293 |
| Edad del par | 61,8 min |
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

Desglose no reproducible desde los motivos registrados (suma 88 vs score 89; motivos sin regla: Anticipación (lib_early_signals early-0.2): +1 — liquidity_inflow: liquidez +17% en 8 min → +1.11): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-22T14:06:04+00:00, sin estado previo): **88** · motivos: MCap > $100K, Volumen masivo, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 74 de 43.977 tokens analizados (0,17%) quedan ≥ 56. Con score 88, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 22/10/2026 14:06 UTC, hasta 24/10/2026 14:06 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +34,5% · h1 +320,0% · h24 +495% · volumen m5/h1 0,02 · edad del par 61,8 min.
- **Precio de entrada** (alerta): $0,0002677.
- **Consulta 22/10/2026 14:34 UTC:** $0,0001267 (-52,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump_2026-10-22_140604.json` · blob `ce27f7896ccf0a2c731573b496875d8be4f0a7d1` · commit `48706af` (2026-10-22T14:23:20Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-22_140604`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump · registro · 22/10/2026 14:06 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump · HTTP 200 · 22/10/2026 14:34 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump/report · HTTP 200 · 22/10/2026 14:34 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump · HTTP 200 · 22/10/2026 14:34 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/92KgVDBs9TSRBX5XxYJRczFRsawA4sLTaKWnMDAJfWA1/ohlcv/hour?limit=1000 · HTTP 200 · 22/10/2026 14:34 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump · HTTP 404 · 22/10/2026 14:34 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=VECTORUSDT · HTTP 400 · 22/10/2026 14:34 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/VECTOR-USD · HTTP 404 · 22/10/2026 14:34 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $31.815 vs $34.591 → 8,03%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001267 vs $0,0001254 → 1,05%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump_2026-10-22_140604.json',encoding='utf-8'));d=d.get('635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump',d);p=mock.patch('time.time',return_value=1792677964);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 635BZjhhzBvn7EsErsL3ABMRmfsfEjGi8YJTCia9pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 22/10/2026 14:34 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `041c250a1ef48564…`
