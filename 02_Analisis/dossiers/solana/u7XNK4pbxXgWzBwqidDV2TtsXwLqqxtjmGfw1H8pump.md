# USDF (USDF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,2857 · liquidez $1.483.103 · mcap $285.735.107 (al detectar)  
Detectado el 10/10/2026 10:37 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 96, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 12/10/2026 10:37 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir USDF

Estudio de cómo se adquiere USDF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 10/10/2026 10:54 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 10/10/2026 10:37 UTC | pumpswap `6FBnZzR…e2md` | $1.483.103 | 1% | 0,013% | 0,135% | 1,349% | $7.416 | $22.247 |
| consulta 10/10/2026 10:54 UTC | pumpswap `6FBnZzR…e2md` | $1.493.531 | 1% | 0,013% | 0,134% | 1,339% | $7.468 | $22.403 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump`
5. Configurar el slippage: 1% (liquidez $1.493.531, consulta 10/10/2026 10:54 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump) y el par en DexScreener (https://dexscreener.com/solana/6FBnZzRtdMrjxEPdLK4UGP9Xm2hsYwLY3xp6EWB1e2md); mint authority / freeze authority: revocada / revocada · holders 3.072 · top-10 0,88% (consulta 10/10/2026 10:54 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump
- Par en DexScreener: https://dexscreener.com/solana/6FBnZzRtdMrjxEPdLK4UGP9Xm2hsYwLY3xp6EWB1e2md
- Página del lanzamiento (pump.fun): https://pump.fun/coin/u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.072 · top-10 0,88% (consulta 10/10/2026 10:54 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | USDF / USDF | registro de la detección (trending) |
| Mint / contrato | `u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6FBnZzRtdMrjxEPdLK4UGP9Xm2hsYwLY3xp6EWB1e2md` | DexScreener, al detectar (3 par(es) en la consulta 10/10/2026 10:54 UTC) |
| Deployer | `8HCj9vivAFwE1YcKPH1mrFDvsfErX2orEAgdMLim6zDf` | RugCheck `creator` |
| Par creado | 10/10/2026 01:22 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 9,3 h / 9,3 h / 9,5 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 10/10/2026 10:54 UTC |
| Holders / top-10 | 3.072 / 0,88% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 10/10/2026 10:54 UTC |
| Holders efectivos del top-10 | 7,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 10/10/2026 10:54 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 10/10/2026 10:54 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6FBnZzRtdMrjxEPdLK4UGP9Xm2hsYwLY3xp6EWB1e2md · Solscan: https://solscan.io/token/u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump · pump.fun: https://pump.fun/coin/u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump · web / Telegram / X: no publicados en DexScreener | consulta 10/10/2026 10:54 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 10/10/2026 10:54 UTC)
- **Historia:**
  - Par creado el 10/10/2026 01:22 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 10/10/2026 10:37 UTC, con el par a 9,3 h de creado: precio $0,2857, mcap $285.735.107, liquidez $1.483.103.
  - Velas de 1 h de GeckoTerminal (10, desde 10/10/2026 01:00 UTC): apertura $0,1578 · máximo $0,2892 (10/10/2026 10:00 UTC) · mínimo $0,00004548 (10/10/2026 01:00 UTC) · último cierre $0,2892.
  - En la consulta 10/10/2026 10:54 UTC: precio $0,2891, liquidez $1.493.531, FDV $289.174.521.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 10/10/2026 10:37 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,2857 |
| Liquidez | $1.483.103 |
| MCap | $285.735.107 |
| Volumen 24 h | $952.562 |
| Cambio 24 h | +627.843% |
| Cambio m5 / h1 | +0,2% / +3,2% |
| Volumen m5 / h1 | $2.100 / $30.562 |
| Trades m5 (compras / ventas) | 8 / 4 |
| Edad del par | 9,3 h |
| Score del feed (WS) | 87 |

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

Desglose reconstruido desde los motivos registrados; suma 96 = score registrado 96 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 87 × 0,3 | +26,2 |
| MCap | ≥ $1M | $285.735.107 | +25 |
| Volumen 24 h | ≥ $100K | $952.562 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 67% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,2% · h1 +3,2% | +20 |
| Volumen m5 | > $1K (par maduro) | $2.100 | +10 |
| Liquidez | ≥ $100K | $1.483.103 | +15 |
| Cambio 24 h | ≥ +50% | +627.843% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +627.843% · liq/mcap 0,5% | -50 |
| **Total** | recortado a 0–100 |  | **96** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-10T10:37:19+00:00, sin estado previo): **96** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 44 de 26.955 tokens analizados (0,16%) quedan ≥ 56. Con score 96, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 10/10/2026 10:37 UTC, hasta 12/10/2026 10:37 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +0,2% · h1 +3,2% · h24 +627.843% · volumen m5/h1 0,07 · edad del par 9,3 h.
- **Precio de entrada** (alerta): $0,2857.
- **Consulta 10/10/2026 10:54 UTC:** $0,2891 (+1,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump_2026-10-10_103719.json` · blob `cce441e650d98583e4d80060649e8404b3a917a7` · commit `92925ee` (2026-10-10T10:48:14Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-10_103059.json` · blob `601793d378cc4386dfe8b511097dc82dd50486e5` · commit `92925ee` (2026-10-10T10:48:14Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-10_103719`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump · registro · 10/10/2026 10:37 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump · HTTP 200 · 10/10/2026 10:54 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump/report · HTTP 200 · 10/10/2026 10:54 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump · HTTP 200 · 10/10/2026 10:54 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6FBnZzRtdMrjxEPdLK4UGP9Xm2hsYwLY3xp6EWB1e2md/ohlcv/hour?limit=1000 · HTTP 200 · 10/10/2026 10:54 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump · HTTP 404 · 10/10/2026 10:54 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=USDFUSDT · HTTP 400 · 10/10/2026 10:54 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/USDF-USD · HTTP 404 · 10/10/2026 10:54 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.493.531 vs $1.493.824 → 0,02%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,2891 vs $0,2892 → 0,04%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump_2026-10-10_103719.json',encoding='utf-8'));d=d.get('u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump',d);p=mock.patch('time.time',return_value=1791628639);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint u7XNK4pbxXgWzBwqidDV2TtsXwLqqxtjmGfw1H8pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 10/10/2026 10:54 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `c72ea9a326695345…`
