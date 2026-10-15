# streamoors (STREAM) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001427 · liquidez $107.233 · mcap $1.420.240 (al detectar)  
Detectado el 15/10/2026 01:05 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 17/10/2026 01:05 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir STREAM

Estudio de cómo se adquiere STREAM, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 15/10/2026 01:32 UTC; CoinGecko sin pares de este contrato en esos exchanges).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 15/10/2026 01:05 UTC | pumpswap `D9NCkN3…CHwJ` | $107.233 | 5% | 0,187% | 1,865% | 18,651% | $536 | $1.608 |
| consulta 15/10/2026 01:32 UTC | pumpswap `D9NCkN3…CHwJ` | $126.848 | 5% | 0,158% | 1,577% | 15,767% | $634 | $1.903 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump`
5. Configurar el slippage: 5% (liquidez $126.848, consulta 15/10/2026 01:32 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump) y el par en DexScreener (https://dexscreener.com/solana/D9NCkN3unPTVLtA56Y68J2cXisje9yyYe61gMM2HCHwJ); mint authority / freeze authority: revocada / revocada · holders 5.937 · top-10 7,19% (consulta 15/10/2026 01:32 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump
- Par en DexScreener: https://dexscreener.com/solana/D9NCkN3unPTVLtA56Y68J2cXisje9yyYe61gMM2HCHwJ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.937 · top-10 7,19% (consulta 15/10/2026 01:32 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | streamoors / STREAM | registro de la detección (trending) |
| Mint / contrato | `9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `D9NCkN3unPTVLtA56Y68J2cXisje9yyYe61gMM2HCHwJ` | DexScreener, al detectar (2 par(es) en la consulta 15/10/2026 01:32 UTC) |
| Deployer | `CdPAR8tzwrNb71cjBH4jV6JzybsMbFojW989duqkfUnN` | RugCheck `creator` |
| Par creado | 14/10/2026 19:18 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 5,8 h / 5,8 h / 6,2 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 15/10/2026 01:32 UTC |
| Holders / top-10 | 5.937 / 7,19% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 15/10/2026 01:32 UTC |
| Holders efectivos del top-10 | 3,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 15/10/2026 01:32 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 15/10/2026 01:32 UTC |
| Links | DexScreener: https://dexscreener.com/solana/D9NCkN3unPTVLtA56Y68J2cXisje9yyYe61gMM2HCHwJ · Solscan: https://solscan.io/token/9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump · pump.fun: https://pump.fun/coin/9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump · web: https://streamoors.si/ · twitter: https://x.com/streamoorspad | consulta 15/10/2026 01:32 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** CoinGecko: Solana Ecosystem, Pump.fun Ecosystem
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 15/10/2026 01:32 UTC)
- **Historia:**
  - Par creado el 14/10/2026 19:18 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 15/10/2026 01:05 UTC, con el par a 5,8 h de creado: precio $0,001427, mcap $1.420.240, liquidez $107.233.
  - Velas de 1 h de GeckoTerminal (7, desde 14/10/2026 19:00 UTC): apertura $0,0003634 · máximo $0,002276 (15/10/2026 01:00 UTC) · mínimo $0,00004950 (14/10/2026 22:00 UTC) · último cierre $0,002016.
  - En la consulta 15/10/2026 01:32 UTC: precio $0,001990, liquidez $126.848, FDV $1.980.635.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 15/10/2026 01:05 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001427 |
| Liquidez | $107.233 |
| MCap | $1.420.240 |
| Volumen 24 h | $1.971.121 |
| Cambio 24 h | +2.589% |
| Cambio m5 / h1 | -6,1% / -18,6% |
| Volumen m5 / h1 | $8.186 / $143.495 |
| Trades m5 (compras / ventas) | 106 / 58 |
| Edad del par | 5,8 h |
| Score del feed (WS) | 74 |

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
| Score del feed | score WS × 0,3 | WS 74 × 0,3 | +22,2 |
| MCap | ≥ $1M | $1.420.240 | +25 |
| Volumen 24 h | ≥ $1M | $1.971.121 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 65% | +25 |
| Volumen m5 | > $1K (par maduro) | $8.186 | +10 |
| Liquidez | ≥ $100K | $107.233 | +15 |
| Cambio 24 h | ≥ +50% | +2.589% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +2.589% · liq/mcap 7,6% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-15T01:05:36+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=7.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 59 de 35.539 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 15/10/2026 01:05 UTC, hasta 17/10/2026 01:05 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -6,1% · h1 -18,6% · h24 +2.589% · volumen m5/h1 0,06 · edad del par 5,8 h.
- **Precio de entrada** (alerta): $0,001427.
- **Consulta 15/10/2026 01:32 UTC:** $0,001990 (+39,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump_2026-10-15_010536.json` · blob `6eaa0b808f98fdde12bd9f7ec540ea661a7b5292` · commit `7fcde52` (2026-10-15T01:25:34Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-15_005902.json` · blob `b2373a93ba96f62c9bfd9b98ba15e9f33f7ae112` · commit `7fcde52` (2026-10-15T01:25:34Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-15_010536`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump · registro · 15/10/2026 01:05 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump · HTTP 200 · 15/10/2026 01:32 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump/report · HTTP 200 · 15/10/2026 01:32 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump · HTTP 200 · 15/10/2026 01:32 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/D9NCkN3unPTVLtA56Y68J2cXisje9yyYe61gMM2HCHwJ/ohlcv/hour?limit=1000 · HTTP 200 · 15/10/2026 01:32 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump · HTTP 200 · 15/10/2026 01:32 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=STREAMUSDT · HTTP 400 · 15/10/2026 01:32 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/STREAM-USD · HTTP 404 · 15/10/2026 01:32 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $126.848 vs $105.922 → 16,50%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001990 vs $0,002016 → 1,29%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump_2026-10-15_010536.json',encoding='utf-8'));d=d.get('9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump',d);p=mock.patch('time.time',return_value=1792026336);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 9a98oQHtxfqmr4EyzsP6wfw69uYAK3JbUeVEuNW1pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 15/10/2026 01:32 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `f2e79f66b1bd248e…`
