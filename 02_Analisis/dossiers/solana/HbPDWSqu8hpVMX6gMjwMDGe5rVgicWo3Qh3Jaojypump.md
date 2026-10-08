# Frank Ashford (Frank) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0007686 · liquidez $88.422 · mcap $730.671 (al detectar)  
Detectado el 08/10/2026 12:48 UTC por: WS score muy alto, MCap > $100K, Volumen masivo (score 84, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 10/10/2026 12:48 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Frank

Estudio de cómo se adquiere Frank, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/10/2026 13:18 UTC; CoinGecko sin pares de este contrato en esos exchanges).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/10/2026 12:48 UTC | pumpswap `745ATaS…dNBi` | $88.422 | 5% | 0,226% | 2,262% | 22,619% | $442 | $1.326 |
| consulta 08/10/2026 13:18 UTC | pumpswap `745ATaS…dNBi` | $89.493 | 5% | 0,223% | 2,235% | 22,348% | $447 | $1.342 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump`
5. Configurar el slippage: 5% (liquidez $89.493, consulta 08/10/2026 13:18 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump) y el par en DexScreener (https://dexscreener.com/solana/745ATaSSWxvry5qt1XVv9eXuG884hDvNJfvA2o82dNBi); mint authority / freeze authority: revocada / revocada · holders 7.324 · top-10 26,20% (consulta 08/10/2026 13:18 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump
- Par en DexScreener: https://dexscreener.com/solana/745ATaSSWxvry5qt1XVv9eXuG884hDvNJfvA2o82dNBi
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 7.324 · top-10 26,20% (consulta 08/10/2026 13:18 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Frank Ashford / Frank | registro de la detección (trending) |
| Mint / contrato | `HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `745ATaSSWxvry5qt1XVv9eXuG884hDvNJfvA2o82dNBi` | DexScreener, al detectar (3 par(es) en la consulta 08/10/2026 13:18 UTC) |
| Deployer | `5J8KZ6YAEv35ZZsaXxnrpp88uTarrLQUWSRCUtkLnoMR` | RugCheck `creator` |
| Par creado | 04/10/2026 22:15 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 3,6 días / 3,6 días / 3,6 días | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/10/2026 13:18 UTC |
| Holders / top-10 | 7.324 / 26,20% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/10/2026 13:18 UTC |
| Holders efectivos del top-10 | 8,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/10/2026 13:18 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 08/10/2026 13:18 UTC |
| Links | DexScreener: https://dexscreener.com/solana/745ATaSSWxvry5qt1XVv9eXuG884hDvNJfvA2o82dNBi · Solscan: https://solscan.io/token/HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump · pump.fun: https://pump.fun/coin/HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump · twitter: https://x.com/Frankdeg0dsAI · telegram: https://t.me/frankashford · tiktok: https://www.tiktok.com/@frankashford2026?_r=1&_t=ZT-9AK1YaedAo1 | consulta 08/10/2026 13:18 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** CoinGecko: Artificial Intelligence (AI), Entertainment, Solana Ecosystem, Pump.fun Ecosystem · scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/10/2026 13:18 UTC)
- **Historia:**
  - Par creado el 04/10/2026 22:15 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/10/2026 12:48 UTC, con el par a 3,6 días de creado: precio $0,0007686, mcap $730.671, liquidez $88.422.
  - Velas de 1 h de GeckoTerminal (88, desde 04/10/2026 22:00 UTC): apertura $0,00005063 · máximo $0,001027 (08/10/2026 03:00 UTC) · mínimo $0,00003302 (04/10/2026 22:00 UTC) · último cierre $0,0008020.
  - En la consulta 08/10/2026 13:18 UTC: precio $0,0007873, liquidez $89.493, FDV $748.388.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/10/2026 12:48 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0007686 |
| Liquidez | $88.422 |
| MCap | $730.671 |
| Volumen 24 h | $1.522.182 |
| Cambio 24 h | +229% |
| Cambio m5 / h1 | +0,5% / +11,2% |
| Volumen m5 / h1 | $5.255 / $68.518 |
| Trades m5 (compras / ventas) | 142 / 84 |
| Edad del par | 3,6 días |
| Score del feed (WS) | 82 |

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

Desglose reconstruido desde los motivos registrados; suma 84 = score registrado 84 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 82 × 0,3 | +24,5 |
| MCap | ≥ $100K | $730.671 | +15 |
| Volumen 24 h | ≥ $1M | $1.522.182 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 63% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,5% · h1 +11,2% | +20 |
| Volumen m5 | > $1K (par maduro) | $5.255 | +10 |
| Par viejo | edad > 24 h | edad 3,6 días | -50 |
| Liquidez | ≥ $50K | $88.422 | +10 |
| Cambio 24 h | ≥ +50% | +229% | +10 |
| **Total** | recortado a 0–100 |  | **84** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-08T12:48:50+00:00, sin estado previo): **84** · motivos: WS score muy alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Par >24h, no nativo pump.fun, Liquidez decente, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 37 de 21.709 tokens analizados (0,17%) quedan ≥ 56. Con score 84, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/10/2026 12:48 UTC, hasta 10/10/2026 12:48 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +0,5% · h1 +11,2% · h24 +229% · volumen m5/h1 0,08 · edad del par 3,6 días.
- **Precio de entrada** (alerta): $0,0007686.
- **Consulta 08/10/2026 13:18 UTC:** $0,0007873 (+2,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump_2026-10-08_124850.json` · blob `217cb5750e779197f76f5ab22220e6b1c2365fe0` · commit `9d24b54` (2026-10-08T13:09:18Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-08_124209.json` · blob `9c03a119a1be87b821c912fcd1ba7a6d61ab3531` · commit `9d24b54` (2026-10-08T13:09:18Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-08_124850`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump · registro · 08/10/2026 12:48 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump · HTTP 200 · 08/10/2026 13:18 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump/report · HTTP 200 · 08/10/2026 13:18 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump · HTTP 200 · 08/10/2026 13:18 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/745ATaSSWxvry5qt1XVv9eXuG884hDvNJfvA2o82dNBi/ohlcv/hour?limit=1000 · HTTP 200 · 08/10/2026 13:18 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump · HTTP 200 · 08/10/2026 13:18 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=FRANKUSDT · HTTP 400 · 08/10/2026 13:18 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/FRANK-USD · HTTP 404 · 08/10/2026 13:18 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $89.493 vs $89.179 → 0,35%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0007873 vs $0,0008020 → 1,84%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump_2026-10-08_124850.json',encoding='utf-8'));d=d.get('HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump',d);p=mock.patch('time.time',return_value=1791463730);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HbPDWSqu8hpVMX6gMjwMDGe5rVgicWo3Qh3Jaojypump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/10/2026 13:18 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `4f2cd614b9625211…`
