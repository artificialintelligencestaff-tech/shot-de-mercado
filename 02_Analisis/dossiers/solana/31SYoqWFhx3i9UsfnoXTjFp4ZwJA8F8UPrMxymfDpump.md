# Project Sphere (SPHERE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001196 · liquidez $28.558 · mcap $119.219 (al detectar)  
Detectado el 04/11/2026 00:27 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 06/11/2026 00:27 UTC (< 48 h) · vigente: quedan 41,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SPHERE

Estudio de cómo se adquiere SPHERE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 04/11/2026 06:47 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 04/11/2026 00:27 UTC | pumpswap `HmcVp73…NUok` | $28.558 | 10% | 0,700% | 7,003% | 70,032% | $143 | $428 |
| consulta 04/11/2026 06:46 UTC | pumpswap `HmcVp73…NUok` | $3.561 | 10% | 5,616% | 56,163% | 561,631% | $18 | $53 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump`
5. Configurar el slippage: 10% (liquidez $3.561, consulta 04/11/2026 06:46 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump) y el par en DexScreener (https://dexscreener.com/solana/HmcVp73ePenjn2JDHQBws6sYN56aBCmPuGDGouqzNUok); mint authority / freeze authority: revocada / revocada · holders 856 · top-10 94,39% (consulta 04/11/2026 06:46 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump
- Par en DexScreener: https://dexscreener.com/solana/HmcVp73ePenjn2JDHQBws6sYN56aBCmPuGDGouqzNUok
- Página del lanzamiento (pump.fun): https://pump.fun/coin/31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 856 · top-10 94,39% (consulta 04/11/2026 06:46 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Project Sphere / SPHERE | registro de la detección (trending) |
| Mint / contrato | `31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HmcVp73ePenjn2JDHQBws6sYN56aBCmPuGDGouqzNUok` | DexScreener, al detectar (2 par(es) en la consulta 04/11/2026 06:46 UTC) |
| Deployer | `HN9YV4zbrsSjGwrLkr17ebbmCv99U34j7FuRcDtHjtZ9` | RugCheck `creator` |
| Par creado | 03/11/2026 02:15 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 22,2 h / 22,2 h / 28,5 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 04/11/2026 06:46 UTC |
| Holders / top-10 | 856 / 94,39% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 04/11/2026 06:46 UTC |
| Holders efectivos del top-10 | 1,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0%; orca 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 04/11/2026 06:46 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 04/11/2026 06:46 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HmcVp73ePenjn2JDHQBws6sYN56aBCmPuGDGouqzNUok · Solscan: https://solscan.io/token/31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump · pump.fun: https://pump.fun/coin/31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump · web: https://projectsphere.world · twitter: https://x.com/ProjSphereWorld | consulta 04/11/2026 06:46 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 04/11/2026 06:46 UTC)
- **Historia:**
  - Par creado el 03/11/2026 02:15 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 04/11/2026 00:27 UTC, con el par a 22,2 h de creado: precio $0,0001196, mcap $119.219, liquidez $28.558.
  - Velas de 1 h de GeckoTerminal (29, desde 03/11/2026 02:00 UTC): apertura $0,0003138 · máximo $0,001657 (03/11/2026 02:00 UTC) · mínimo $0,000002367 (04/11/2026 02:00 UTC) · último cierre $0,000003483.
  - En la consulta 04/11/2026 06:46 UTC: precio $0,000003479, liquidez $3.561, FDV $3.466.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 04/11/2026 00:27 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001196 |
| Liquidez | $28.558 |
| MCap | $119.219 |
| Volumen 24 h | $2.602.729 |
| Cambio 24 h | +137% |
| Cambio m5 / h1 | +0,9% / +3,4% |
| Volumen m5 / h1 | $1.300 / $25.001 |
| Trades m5 (compras / ventas) | 495 / 88 |
| Edad del par | 22,2 h |
| Score del feed (WS) | 73 |

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
| Score del feed | score WS × 0,3 | WS 73 × 0,3 | +21,8 |
| MCap | ≥ $100K | $119.219 | +15 |
| Volumen 24 h | ≥ $1M | $2.602.729 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 85% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,9% · h1 +3,4% | +20 |
| Volumen m5 | > $1K (par maduro) | $1.300 | +10 |
| Liquidez | ≥ $20K | $28.558 | +5 |
| Cambio 24 h | ≥ +50% | +137% | +10 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-04T00:27:34+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 90 de 46.634 tokens analizados (0,19%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 04/11/2026 00:27 UTC, hasta 06/11/2026 00:27 UTC · vigente: quedan 41,7 h.
- **Aceleración al detectar:** cambio m5 +0,9% · h1 +3,4% · h24 +137% · volumen m5/h1 0,05 · edad del par 22,2 h.
- **Precio de entrada** (alerta): $0,0001196.
- **Consulta 04/11/2026 06:46 UTC:** $0,000003479 (-97,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump_2026-11-04_002734.json` · blob `98eee759269957ea0a0727e036478359fa5faad8` · commit `949a175` (2026-11-04T06:25:01Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-04_002002.json` · blob `6f02dc1d908dca291b7f71835922afcd7f52aa42` · commit `949a175` (2026-11-04T06:25:01Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-04_002734`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump · registro · 04/11/2026 00:27 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump · HTTP 200 · 04/11/2026 06:46 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump/report · HTTP 200 · 04/11/2026 06:46 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump · HTTP 200 · 04/11/2026 06:46 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HmcVp73ePenjn2JDHQBws6sYN56aBCmPuGDGouqzNUok/ohlcv/hour?limit=1000 · HTTP 200 · 04/11/2026 06:47 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump · HTTP 404 · 04/11/2026 06:47 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SPHEREUSDT · HTTP 400 · 04/11/2026 06:47 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SPHERE-USD · HTTP 404 · 04/11/2026 06:47 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.561 vs $3.577 → 0,44%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000003479 vs $0,000003483 → 0,13%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump_2026-11-04_002734.json',encoding='utf-8'));d=d.get('31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump',d);p=mock.patch('time.time',return_value=1793752054);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 04/11/2026 06:47 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `a0ce50a87b79c0ea…`
