# XTO (XTO) — dossier

🎴 n/d en Solana · precio $0,005456 · liquidez $178.609 · mcap $5.456.562 (al detectar)  
Detectado el 14/10/2026 02:24 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 16/10/2026 02:24 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir XTO

Estudio de cómo se adquiere XTO, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **meteora**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 14/10/2026 02:56 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 14/10/2026 02:24 UTC | meteora `4pBedyg…PJ7o` | $178.609 | 5% | 0,112% | 1,120% | 11,198% | $893 | $2.679 |
| consulta 14/10/2026 02:56 UTC | meteora `4pBedyg…PJ7o` | $181.504 | 5% | 0,110% | 1,102% | 11,019% | $908 | $2.723 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en meteora
4. Pegar el mint y verificar que coincide carácter por carácter: `XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt`
5. Configurar el slippage: 5% (liquidez $181.504, consulta 14/10/2026 02:56 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt) y el par en DexScreener (https://dexscreener.com/solana/4pBedygxZVUVR94sgTJC6C5CX7nMGBdnv1x8ac9oPJ7o); mint authority / freeze authority: revocada / revocada · holders 1.012 · top-10 13,42% (consulta 14/10/2026 02:56 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt
- Par en DexScreener: https://dexscreener.com/solana/4pBedygxZVUVR94sgTJC6C5CX7nMGBdnv1x8ac9oPJ7o
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.012 · top-10 13,42% (consulta 14/10/2026 02:56 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | XTO / XTO | registro de la detección (trending) |
| Mint / contrato | `XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt` | registro de la detección |
| Chain / DEX / par | Solana / meteora / `4pBedygxZVUVR94sgTJC6C5CX7nMGBdnv1x8ac9oPJ7o` | DexScreener, al detectar (6 par(es) en la consulta 14/10/2026 02:56 UTC) |
| Deployer | `CyzYoSZ6pcxjhtb8zcXFEwmGtD5nSTj4myrjJ2kauJ1G` | RugCheck `creator` |
| Par creado | 13/10/2026 22:01 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 4,4 h / 4,4 h / 4,9 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 14/10/2026 02:56 UTC |
| Holders / top-10 | 1.012 / 13,42% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 14/10/2026 02:56 UTC |
| Holders efectivos del top-10 | 9,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | meteora_damm_v2 100%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 14/10/2026 02:56 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 14/10/2026 02:56 UTC |
| Links | DexScreener: https://dexscreener.com/solana/4pBedygxZVUVR94sgTJC6C5CX7nMGBdnv1x8ac9oPJ7o · Solscan: https://solscan.io/token/XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt · web: https://XTruthOil.com · twitter: https://x.com/xtruthoil | consulta 14/10/2026 02:56 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** n/d
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 14/10/2026 02:56 UTC)
- **Historia:**
  - Par creado el 13/10/2026 22:01 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 14/10/2026 02:24 UTC, con el par a 4,4 h de creado: precio $0,005456, mcap $5.456.562, liquidez $178.609.
  - Velas de 1 h de GeckoTerminal (5, desde 13/10/2026 22:00 UTC): apertura $0,00007174 · máximo $0,007397 (13/10/2026 23:00 UTC) · mínimo $0,00007174 (13/10/2026 22:00 UTC) · último cierre $0,005600.
  - En la consulta 14/10/2026 02:56 UTC: precio $0,005634, liquidez $181.504, FDV $5.634.881.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 14/10/2026 02:24 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,005456 |
| Liquidez | $178.609 |
| MCap | $5.456.562 |
| Volumen 24 h | $1.092.021 |
| Cambio 24 h | +7.503% |
| Cambio m5 / h1 | +4,3% / +7,4% |
| Volumen m5 / h1 | $3.182 / $18.830 |
| Trades m5 (compras / ventas) | 9 / 12 |
| Edad del par | 4,4 h |
| Score del feed (WS) | 84 |

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
| Score del feed | score WS × 0,3 | WS 84 × 0,3 | +25,1 |
| MCap | ≥ $1M | $5.456.562 | +25 |
| Volumen 24 h | ≥ $1M | $1.092.021 | +20 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +4,3% · h1 +7,4% | +20 |
| Volumen m5 | > $1K (par maduro) | $3.182 | +10 |
| Liquidez | ≥ $100K | $178.609 | +15 |
| Cambio 24 h | ≥ +50% | +7.503% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +7.503% · liq/mcap 3,3% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-14T02:24:41+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=3.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 54 de 34.354 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 14/10/2026 02:24 UTC, hasta 16/10/2026 02:24 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +4,3% · h1 +7,4% · h24 +7.503% · volumen m5/h1 0,17 · edad del par 4,4 h.
- **Precio de entrada** (alerta): $0,005456.
- **Consulta 14/10/2026 02:56 UTC:** $0,005634 (+3,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt_2026-10-14_022441.json` · blob `bc562dee23e060c2769233659ad7401aecf73223` · commit `ad1f5bb` (2026-10-14T02:49:49Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-14_021822.json` · blob `55ad726754c5a072e09f23d31a390d82d2870395` · commit `ad1f5bb` (2026-10-14T02:49:49Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-14_022441`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt · registro · 14/10/2026 02:24 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt · HTTP 200 · 14/10/2026 02:56 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt/report · HTTP 200 · 14/10/2026 02:56 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt · HTTP 200 · 14/10/2026 02:56 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/4pBedygxZVUVR94sgTJC6C5CX7nMGBdnv1x8ac9oPJ7o/ohlcv/hour?limit=1000 · HTTP 200 · 14/10/2026 02:56 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt · HTTP 404 · 14/10/2026 02:56 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=XTOUSDT · HTTP 400 · 14/10/2026 02:56 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/XTO-USD · HTTP 404 · 14/10/2026 02:56 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $181.504 vs $176.174 → 2,94%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,005634 vs $0,005600 → 0,61%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt_2026-10-14_022441.json',encoding='utf-8'));d=d.get('XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt',d);p=mock.patch('time.time',return_value=1791944681);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 14/10/2026 02:56 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `b937009f27183afe…`
