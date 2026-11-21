# Cool Dog (LOOSY) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001802 · liquidez $30.703 · mcap $179.515 (al detectar)  
Detectado el 20/11/2026 22:59 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 22/11/2026 22:59 UTC (< 48 h) · vigente: quedan 43,2 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir LOOSY

Estudio de cómo se adquiere LOOSY, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 21/11/2026 03:47 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 20/11/2026 22:59 UTC | pumpswap `Bfiq9ea…4QkY` | $30.703 | 10% | 0,651% | 6,514% | 65,141% | $154 | $461 |
| consulta 21/11/2026 03:47 UTC | pumpswap `Bfiq9ea…4QkY` | $2.146 | 10% | 9,318% | 93,178% | 931,784% | $11 | $32 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump`
5. Configurar el slippage: 10% (liquidez $2.146, consulta 21/11/2026 03:47 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump) y el par en DexScreener (https://dexscreener.com/solana/Bfiq9eaLcMjpEKcgm16GSzzGdedCpcFhRAFvivRP4QkY); mint authority / freeze authority: revocada / revocada · holders 434 · top-10 99,38% (consulta 21/11/2026 03:47 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump
- Par en DexScreener: https://dexscreener.com/solana/Bfiq9eaLcMjpEKcgm16GSzzGdedCpcFhRAFvivRP4QkY
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 434 · top-10 99,38% (consulta 21/11/2026 03:47 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Cool Dog / LOOSY | registro de la detección (trending) |
| Mint / contrato | `HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Bfiq9eaLcMjpEKcgm16GSzzGdedCpcFhRAFvivRP4QkY` | DexScreener, al detectar (2 par(es) en la consulta 21/11/2026 03:47 UTC) |
| Deployer | `FKuanhph5RUqptmrbFDfXLFFiMLuoV6zMkNcBFZQS8Td` | RugCheck `creator` |
| Par creado | 20/11/2026 01:04 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 21,9 h / 21,9 h / 26,7 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 21/11/2026 03:47 UTC |
| Holders / top-10 | 434 / 99,38% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 21/11/2026 03:47 UTC |
| Holders efectivos del top-10 | 1,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 21/11/2026 03:47 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 21/11/2026 03:47 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Bfiq9eaLcMjpEKcgm16GSzzGdedCpcFhRAFvivRP4QkY · Solscan: https://solscan.io/token/HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump · pump.fun: https://pump.fun/coin/HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump · web: https://loosydog.live · twitter: https://x.com/CoolDogLoosy · telegram: https://t.me/CoolDogLoosy | consulta 21/11/2026 03:47 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 21/11/2026 03:47 UTC)
- **Historia:**
  - Par creado el 20/11/2026 01:04 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 20/11/2026 22:59 UTC, con el par a 21,9 h de creado: precio $0,0001802, mcap $179.515, liquidez $30.703.
  - Velas de 1 h de GeckoTerminal (27, desde 20/11/2026 01:00 UTC): apertura $0,00006650 · máximo $0,003041 (20/11/2026 15:00 UTC) · mínimo $0,000001576 (21/11/2026 03:00 UTC) · último cierre $0,000001972.
  - En la consulta 21/11/2026 03:47 UTC: precio $0,000001961, liquidez $2.146, FDV $1.953.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 20/11/2026 22:59 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001802 |
| Liquidez | $30.703 |
| MCap | $179.515 |
| Volumen 24 h | $2.352.792 |
| Cambio 24 h | +350% |
| Cambio m5 / h1 | +4,1% / -21,9% |
| Volumen m5 / h1 | $2.052 / $44.077 |
| Trades m5 (compras / ventas) | 531 / 101 |
| Edad del par | 21,9 h |
| Score del feed (WS) | 71 |

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
| Score del feed | score WS × 0,3 | WS 71 × 0,3 | +21,3 |
| MCap | ≥ $100K | $179.515 | +15 |
| Volumen 24 h | ≥ $1M | $2.352.792 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 84% | +25 |
| Volumen m5 | > $1K (par maduro) | $2.052 | +10 |
| Liquidez | ≥ $20K | $30.703 | +5 |
| Cambio 24 h | ≥ +50% | +350% | +10 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-20T22:59:03+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 109 de 47.510 tokens analizados (0,23%) quedan ≥ 56. Con score 100, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 20/11/2026 22:59 UTC, hasta 22/11/2026 22:59 UTC · vigente: quedan 43,2 h.
- **Aceleración al detectar:** cambio m5 +4,1% · h1 -21,9% · h24 +350% · volumen m5/h1 0,05 · edad del par 21,9 h.
- **Precio de entrada** (alerta): $0,0001802.
- **Consulta 21/11/2026 03:47 UTC:** $0,000001961 (-98,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump_2026-11-20_225903.json` · blob `51b682c54af720a791f933d4c1fbe599eae23f02` · commit `169e633` (2026-11-21T03:36:57Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-20_225241.json` · blob `0318c9564a6c8f6ca80aa5744312dee78af57631` · commit `169e633` (2026-11-21T03:36:57Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-20_225903`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump · registro · 20/11/2026 22:59 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump · HTTP 200 · 21/11/2026 03:47 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump/report · HTTP 200 · 21/11/2026 03:47 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump · HTTP 200 · 21/11/2026 03:47 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Bfiq9eaLcMjpEKcgm16GSzzGdedCpcFhRAFvivRP4QkY/ohlcv/hour?limit=1000 · HTTP 200 · 21/11/2026 03:47 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump · HTTP 404 · 21/11/2026 03:47 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=LOOSYUSDT · HTTP 400 · 21/11/2026 03:47 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/LOOSY-USD · HTTP 404 · 21/11/2026 03:47 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.146 vs $2.150 → 0,19%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000001961 vs $0,000001972 → 0,57%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump_2026-11-20_225903.json',encoding='utf-8'));d=d.get('HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump',d);p=mock.patch('time.time',return_value=1795215543);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 21/11/2026 03:47 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `1c49dce47118c4b8…`
