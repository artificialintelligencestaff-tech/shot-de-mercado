# Incognito69420 (Incognito) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0008179 · liquidez $87.862 · mcap $811.351 (al detectar)  
Detectado el 11/10/2026 09:40 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 13/10/2026 09:40 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Incognito

Estudio de cómo se adquiere Incognito, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/10/2026 09:56 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 11/10/2026 09:40 UTC | pumpswap `AJZPEX2…8F7u` | $87.862 | 5% | 0,228% | 2,276% | 22,763% | $439 | $1.318 |
| consulta 11/10/2026 09:56 UTC | pumpswap `AJZPEX2…8F7u` | $89.649 | 5% | 0,223% | 2,231% | 22,309% | $448 | $1.345 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump`
5. Configurar el slippage: 5% (liquidez $89.649, consulta 11/10/2026 09:56 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump) y el par en DexScreener (https://dexscreener.com/solana/AJZPEX2nJCdkoXXQ6zExtpZFdbiG2LHGvtjSxV8U8F7u); mint authority / freeze authority: revocada / revocada · holders 11.323 · top-10 20,32% (consulta 11/10/2026 09:56 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump
- Par en DexScreener: https://dexscreener.com/solana/AJZPEX2nJCdkoXXQ6zExtpZFdbiG2LHGvtjSxV8U8F7u
- Página del lanzamiento (pump.fun): https://pump.fun/coin/BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 11.323 · top-10 20,32% (consulta 11/10/2026 09:56 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Incognito69420 / Incognito | registro de la detección (trending) |
| Mint / contrato | `BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `AJZPEX2nJCdkoXXQ6zExtpZFdbiG2LHGvtjSxV8U8F7u` | DexScreener, al detectar (25 par(es) en la consulta 11/10/2026 09:56 UTC) |
| Deployer | `EV7s6mGK6GyZ1zME3pD7c7ha4rcEwZR28s8Hpt2tM2fo` | RugCheck `creator` |
| Par creado | 11/10/2026 05:43 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 3,9 h / 3,9 h / 4,2 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/10/2026 09:56 UTC |
| Holders / top-10 | 11.323 / 20,32% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/10/2026 09:56 UTC |
| Holders efectivos del top-10 | 7,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/10/2026 09:56 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 11/10/2026 09:56 UTC |
| Links | DexScreener: https://dexscreener.com/solana/AJZPEX2nJCdkoXXQ6zExtpZFdbiG2LHGvtjSxV8U8F7u · Solscan: https://solscan.io/token/BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump · pump.fun: https://pump.fun/coin/BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump · twitter: https://x.com/search?q=$Incognito | consulta 11/10/2026 09:56 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/10/2026 09:56 UTC)
- **Historia:**
  - Par creado el 11/10/2026 05:43 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 11/10/2026 09:40 UTC, con el par a 3,9 h de creado: precio $0,0008179, mcap $811.351, liquidez $87.862.
  - Velas de 1 h de GeckoTerminal (5, desde 11/10/2026 05:00 UTC): apertura $0,0005407 · máximo $0,001653 (11/10/2026 06:00 UTC) · mínimo $0,0003986 (11/10/2026 05:00 UTC) · último cierre $0,0008199.
  - En la consulta 11/10/2026 09:56 UTC: precio $0,0008502, liquidez $89.649, FDV $843.386.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 11/10/2026 09:40 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0008179 |
| Liquidez | $87.862 |
| MCap | $811.351 |
| Volumen 24 h | $2.464.703 |
| Cambio 24 h | +1.742% |
| Cambio m5 / h1 | -1,3% / +28,0% |
| Volumen m5 / h1 | $6.958 / $203.233 |
| Trades m5 (compras / ventas) | 37 / 29 |
| Edad del par | 3,9 h |
| Score del feed (WS) | 79 |

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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 79 × 0,3 | +23,8 |
| MCap | ≥ $100K | $811.351 | +15 |
| Volumen 24 h | ≥ $1M | $2.464.703 | +20 |
| Buy pressure m5 | > 55% (par maduro) | 56% | +15 |
| Edge temprano | edad < 4 h (par maduro) | edad 3,9 h | +8 |
| Volumen m5 | > $1K (par maduro) | $6.958 | +10 |
| Liquidez | ≥ $50K | $87.862 | +10 |
| Cambio 24 h | ≥ +50% | +1.742% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.742% · liq/mcap 10,8% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-11T09:40:25+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >55%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=10.8% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 48 de 28.880 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 11/10/2026 09:40 UTC, hasta 13/10/2026 09:40 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -1,3% · h1 +28,0% · h24 +1.742% · volumen m5/h1 0,03 · edad del par 3,9 h.
- **Precio de entrada** (alerta): $0,0008179.
- **Consulta 11/10/2026 09:56 UTC:** $0,0008502 (+3,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump_2026-10-11_094025.json` · blob `69c2777e101cacf3c11e20d7005ad4c9dd884b9d` · commit `9a1c888` (2026-10-11T09:50:08Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-11_093310.json` · blob `a60baf857d110560bf1398a2b9c776fc1598f7cb` · commit `9a1c888` (2026-10-11T09:50:08Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-11_094025`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump · registro · 11/10/2026 09:40 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump · HTTP 200 · 11/10/2026 09:56 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump/report · HTTP 200 · 11/10/2026 09:56 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump · HTTP 200 · 11/10/2026 09:56 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/AJZPEX2nJCdkoXXQ6zExtpZFdbiG2LHGvtjSxV8U8F7u/ohlcv/hour?limit=1000 · HTTP 200 · 11/10/2026 09:56 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump · HTTP 404 · 11/10/2026 09:56 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=INCOGNITOUSDT · HTTP 400 · 11/10/2026 09:56 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/INCOGNITO-USD · HTTP 404 · 11/10/2026 09:56 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $89.649 vs $155.712 → 42,43%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0008502 vs $0,0008199 → 3,56%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump_2026-10-11_094025.json',encoding='utf-8'));d=d.get('BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump',d);p=mock.patch('time.time',return_value=1791711625);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint BBZ3sgY66QVsxcXXBVpuQfDzH2b5Ub8qmfKNQJjBpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/10/2026 09:56 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `a99c33f7cc8fa7db…`
