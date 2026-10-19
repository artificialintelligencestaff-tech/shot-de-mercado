# startupSI (startupSI) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,004464 · liquidez $191.696 · mcap $4.447.232 (al detectar)  
Detectado el 19/10/2026 00:27 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 21/10/2026 00:27 UTC (< 48 h) · vigente: quedan 47,3 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir startupSI

Estudio de cómo se adquiere startupSI, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 19/10/2026 01:10 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 19/10/2026 00:27 UTC | pumpswap `AscPffy…QD2R` | $191.696 | 5% | 0,104% | 1,043% | 10,433% | $958 | $2.875 |
| consulta 19/10/2026 01:10 UTC | pumpswap `AscPffy…QD2R` | $189.784 | 5% | 0,105% | 1,054% | 10,538% | $949 | $2.847 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump`
5. Configurar el slippage: 5% (liquidez $189.784, consulta 19/10/2026 01:10 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump) y el par en DexScreener (https://dexscreener.com/solana/AscPffyZxMnHHFHqQWawtcrmasgUzCJtwyu6oS6CQD2R); mint authority / freeze authority: revocada / revocada · holders n/d · top-10 n/d (consulta 19/10/2026 01:10 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump
- Par en DexScreener: https://dexscreener.com/solana/AscPffyZxMnHHFHqQWawtcrmasgUzCJtwyu6oS6CQD2R
- Página del lanzamiento (pump.fun): https://pump.fun/coin/EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders n/d · top-10 n/d (consulta 19/10/2026 01:10 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | startupSI / startupSI | registro de la detección (trending) |
| Mint / contrato | `EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `AscPffyZxMnHHFHqQWawtcrmasgUzCJtwyu6oS6CQD2R` | DexScreener, al detectar (2 par(es) en la consulta 19/10/2026 01:10 UTC) |
| Deployer | n/d | n/d (fuente: RugCheck `creator`) |
| Par creado | 18/10/2026 18:34 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 5,9 h / 5,9 h / 6,6 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | GoPlus, consulta 19/10/2026 01:10 UTC |
| Holders / top-10 | n/d / n/d | RugCheck [P: sin consulta] |
| Holders efectivos del top-10 | n/d | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | n/d | RugCheck [P] |
| Etiquetas de RugCheck | n/d | RugCheck [P] |
| Links | DexScreener: https://dexscreener.com/solana/AscPffyZxMnHHFHqQWawtcrmasgUzCJtwyu6oS6CQD2R · Solscan: https://solscan.io/token/EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump · pump.fun: https://pump.fun/coin/EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump · web: https://startupsi.org/ · twitter: https://x.com/startupsipad | consulta 19/10/2026 01:10 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (metadata sin consultar [P])
- **Historia:**
  - Par creado el 18/10/2026 18:34 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 19/10/2026 00:27 UTC, con el par a 5,9 h de creado: precio $0,004464, mcap $4.447.232, liquidez $191.696.
  - Velas de 1 h de GeckoTerminal (8, desde 18/10/2026 18:00 UTC): apertura $0,0004548 · máximo $0,005098 (19/10/2026 00:00 UTC) · mínimo $0,00005865 (18/10/2026 18:00 UTC) · último cierre $0,004344.
  - En la consulta 19/10/2026 01:10 UTC: precio $0,004336, liquidez $189.784, FDV $4.320.280.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 19/10/2026 00:27 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,004464 |
| Liquidez | $191.696 |
| MCap | $4.447.232 |
| Volumen 24 h | $2.969.530 |
| Cambio 24 h | +7.456% |
| Cambio m5 / h1 | -10,9% / +21,2% |
| Volumen m5 / h1 | $21.501 / $252.392 |
| Trades m5 (compras / ventas) | 330 / 101 |
| Edad del par | 5,9 h |
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
| Score del feed | score WS × 0,3 | WS 74 × 0,3 | +22,3 |
| MCap | ≥ $1M | $4.447.232 | +25 |
| Volumen 24 h | ≥ $1M | $2.969.530 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 77% | +25 |
| Volumen m5 | > $1K (par maduro) | $21.501 | +10 |
| Liquidez | ≥ $100K | $191.696 | +15 |
| Cambio 24 h | ≥ +50% | +7.456% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +7.456% · liq/mcap 4,3% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-19T00:27:00+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 67 de 40.300 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 19/10/2026 00:27 UTC, hasta 21/10/2026 00:27 UTC · vigente: quedan 47,3 h.
- **Aceleración al detectar:** cambio m5 -10,9% · h1 +21,2% · h24 +7.456% · volumen m5/h1 0,09 · edad del par 5,9 h.
- **Precio de entrada** (alerta): $0,004464.
- **Consulta 19/10/2026 01:10 UTC:** $0,004336 (-2,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump_2026-10-19_002700.json` · blob `dfc8c3b5cefadf07bf8f7f723b3d17b761e43490` · commit `b485946` (2026-10-19T01:03:53Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-19_001953.json` · blob `56282a99afcea90a533349af878fc1147b2d886e` · commit `b485946` (2026-10-19T01:03:53Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-19_002700`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump · registro · 19/10/2026 00:27 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump · HTTP 200 · 19/10/2026 01:10 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump/report · error ConnectionError · 19/10/2026 01:10 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump · HTTP 200 · 19/10/2026 01:10 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/AscPffyZxMnHHFHqQWawtcrmasgUzCJtwyu6oS6CQD2R/ohlcv/hour?limit=1000 · HTTP 200 · 19/10/2026 01:10 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump · HTTP 404 · 19/10/2026 01:10 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=STARTUPSIUSDT · HTTP 400 · 19/10/2026 01:10 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/STARTUPSI-USD · HTTP 404 · 19/10/2026 01:10 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,004336 vs $0,004344 → 0,19%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump_2026-10-19_002700.json',encoding='utf-8'));d=d.get('EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump',d);p=mock.patch('time.time',return_value=1792369620);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 19/10/2026 01:10 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `5630e51f2f290e04…`
