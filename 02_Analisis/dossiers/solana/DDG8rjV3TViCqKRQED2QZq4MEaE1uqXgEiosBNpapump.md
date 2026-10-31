# The Super Intelligent Beauty (AgenC) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001008 · liquidez $904.038 · mcap $1.002.861 (al detectar)  
Detectado el 31/10/2026 17:41 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 02/11/2026 17:41 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir AgenC

Estudio de cómo se adquiere AgenC, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 31/10/2026 17:41 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 31/10/2026 17:41 UTC | pumpswap `ABF43sb…buCj` | $904.038 | 3% | 0,022% | 0,221% | 2,212% | $4.520 | $13.561 |
| consulta 31/10/2026 17:41 UTC | pumpswap `ABF43sb…buCj` | $904.038 | 3% | 0,022% | 0,221% | 2,212% | $4.520 | $13.561 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump`
5. Configurar el slippage: 3% (liquidez $904.038, consulta 31/10/2026 17:41 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump) y el par en DexScreener (https://dexscreener.com/solana/ABF43sbqjwKF1GzY8MkHNHR8EJLZgf6V9ASR8LRmbuCj); mint authority / freeze authority: revocada / revocada · holders 729 · top-10 98,62% (consulta 31/10/2026 17:41 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump
- Par en DexScreener: https://dexscreener.com/solana/ABF43sbqjwKF1GzY8MkHNHR8EJLZgf6V9ASR8LRmbuCj
- Página del lanzamiento (pump.fun): https://pump.fun/coin/DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 729 · top-10 98,62% (consulta 31/10/2026 17:41 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | The Super Intelligent Beauty / AgenC | registro de la detección (trending) |
| Mint / contrato | `DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `ABF43sbqjwKF1GzY8MkHNHR8EJLZgf6V9ASR8LRmbuCj` | DexScreener, al detectar (7 par(es) en la consulta 31/10/2026 17:41 UTC) |
| Deployer | `37wUxrAUQ9zV6JAKYYuJHteihBGyJF3R39EXm4oLBCpC` | RugCheck `creator` |
| Par creado | 30/10/2026 18:20 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 23,3 h / 23,3 h / 23,3 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 31/10/2026 17:41 UTC |
| Holders / top-10 | 729 / 98,62% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 31/10/2026 17:41 UTC |
| Holders efectivos del top-10 | 1,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; orca 0%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 31/10/2026 17:41 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 31/10/2026 17:41 UTC |
| Links | DexScreener: https://dexscreener.com/solana/ABF43sbqjwKF1GzY8MkHNHR8EJLZgf6V9ASR8LRmbuCj · Solscan: https://solscan.io/token/DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump · pump.fun: https://pump.fun/coin/DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump · web: https://agencsib.meme · twitter: https://x.com/AgenCSIB | consulta 31/10/2026 17:41 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 31/10/2026 17:41 UTC)
- **Historia:**
  - Par creado el 30/10/2026 18:20 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 31/10/2026 17:41 UTC, con el par a 23,3 h de creado: precio $0,001008, mcap $1.002.861, liquidez $904.038.
  - Velas de 1 h de GeckoTerminal (24, desde 30/10/2026 18:00 UTC): apertura $0,0001861 · máximo $0,002342 (31/10/2026 03:00 UTC) · mínimo $0,000002691 (31/10/2026 16:00 UTC) · último cierre $0,000002793.
  - En la consulta 31/10/2026 17:41 UTC: precio $0,001008, liquidez $904.038, FDV $1.002.861.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 31/10/2026 17:41 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001008 |
| Liquidez | $904.038 |
| MCap | $1.002.861 |
| Volumen 24 h | $4.655.224 |
| Cambio 24 h | +1.849% |
| Cambio m5 / h1 | +0,0% / +34.722,0% |
| Volumen m5 / h1 | $3 / $406 |
| Trades m5 (compras / ventas) | 20 / 0 |
| Edad del par | 23,3 h |
| Score del feed (WS) | 91 |

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
| Score del feed | score WS × 0,3 | WS 91 × 0,3 | +27,3 |
| MCap | ≥ $1M | $1.002.861 | +25 |
| Volumen 24 h | ≥ $1M | $4.655.224 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 100% | +25 |
| Liquidez | ≥ $100K | $904.038 | +15 |
| Cambio 24 h | ≥ +50% | +1.849% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.849% · liq/mcap 90,1% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-31T17:41:20+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=90.1% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 85 de 46.386 tokens analizados (0,18%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 31/10/2026 17:41 UTC, hasta 02/11/2026 17:41 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +0,0% · h1 +34.722,0% · h24 +1.849% · volumen m5/h1 0,01 · edad del par 23,3 h.
- **Precio de entrada** (alerta): $0,001008.
- **Consulta 31/10/2026 17:41 UTC:** $0,001008 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump_2026-10-31_174135.json` · blob `45dc5c30228b2c1ebf968cbb46afffac380fdbb0` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-31_173615.json` · blob `e739bc68863eef99c2d05645cde3056659cc3610` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-31_174135`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump · registro · 31/10/2026 17:41 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump · HTTP 200 · 31/10/2026 17:41 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump/report · HTTP 200 · 31/10/2026 17:41 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump · HTTP 200 · 31/10/2026 17:41 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/ABF43sbqjwKF1GzY8MkHNHR8EJLZgf6V9ASR8LRmbuCj/ohlcv/hour?limit=1000 · HTTP 200 · 31/10/2026 17:41 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump · HTTP 404 · 31/10/2026 17:41 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AGENCUSDT · HTTP 400 · 31/10/2026 17:41 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AGENC-USD · HTTP 404 · 31/10/2026 17:41 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $904.038 vs $3.324 → 99,63%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001008 vs $0,000002793 → 99,72%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump_2026-10-31_174135.json',encoding='utf-8'));d=d.get('DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump',d);p=mock.patch('time.time',return_value=1793468480);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 31/10/2026 17:41 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `600209c8dd7e9ab8…`
