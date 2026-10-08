# Organisme (Organisme) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00007264 · liquidez $23.885 · mcap $69.728 (al detectar)  
Detectado el 08/10/2026 09:41 UTC por: WS score alto, MCap > $50K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 10/10/2026 09:41 UTC (< 48 h) · vigente: quedan 47,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Organisme

Estudio de cómo se adquiere Organisme, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/10/2026 10:14 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/10/2026 09:41 UTC | pumpswap `52Qg1oP…yCbT` | $23.885 | 10% | 0,837% | 8,373% | 83,735% | $119 | $358 |
| consulta 08/10/2026 10:14 UTC | pumpswap `52Qg1oP…yCbT` | $3.369 | 10% | 5,937% | 59,370% | 593,697% | $17 | $51 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump`
5. Configurar el slippage: 10% (liquidez $3.369, consulta 08/10/2026 10:14 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump) y el par en DexScreener (https://dexscreener.com/solana/52Qg1oPv3YUScwK8Z4887fwuRWRGr1H2XtcpvETfyCbT); mint authority / freeze authority: revocada / revocada · holders 647 · top-10 97,79% (consulta 08/10/2026 10:14 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump
- Par en DexScreener: https://dexscreener.com/solana/52Qg1oPv3YUScwK8Z4887fwuRWRGr1H2XtcpvETfyCbT
- Página del lanzamiento (pump.fun): https://pump.fun/coin/7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 647 · top-10 97,79% (consulta 08/10/2026 10:14 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Organisme / Organisme | registro de la detección (trending) |
| Mint / contrato | `7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `52Qg1oPv3YUScwK8Z4887fwuRWRGr1H2XtcpvETfyCbT` | DexScreener, al detectar (2 par(es) en la consulta 08/10/2026 10:14 UTC) |
| Deployer | `5jCTasCvZhBo1RpEngrBWdJgYRggahwYXZfcWFuMSfsb` | RugCheck `creator` |
| Par creado | 08/10/2026 06:58 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 2,7 h / 2,7 h / 3,3 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/10/2026 10:14 UTC |
| Holders / top-10 | 647 / 97,79% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/10/2026 10:14 UTC |
| Holders efectivos del top-10 | 1,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/10/2026 10:14 UTC |
| Etiquetas de RugCheck | «Creator history of rugged tokens», «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 08/10/2026 10:14 UTC |
| Links | DexScreener: https://dexscreener.com/solana/52Qg1oPv3YUScwK8Z4887fwuRWRGr1H2XtcpvETfyCbT · Solscan: https://solscan.io/token/7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump · pump.fun: https://pump.fun/coin/7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump · web: https://organisme.xyz/ · twitter: https://x.com/organisme_trade | consulta 08/10/2026 10:14 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/10/2026 10:14 UTC)
- **Historia:**
  - Par creado el 08/10/2026 06:58 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/10/2026 09:41 UTC, con el par a 2,7 h de creado: precio $0,00007264, mcap $69.728, liquidez $23.885.
  - Velas de 1 h de GeckoTerminal (5, desde 08/10/2026 06:00 UTC): apertura $0,00004658 · máximo $0,0003382 (08/10/2026 08:00 UTC) · mínimo $0,000002818 (08/10/2026 09:00 UTC) · último cierre $0,000003141.
  - En la consulta 08/10/2026 10:14 UTC: precio $0,000003140, liquidez $3.369, FDV $3.014.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/10/2026 09:41 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00007264 |
| Liquidez | $23.885 |
| MCap | $69.728 |
| Volumen 24 h | $1.109.626 |
| Cambio 24 h | +56% |
| Cambio m5 / h1 | -17,4% / -50,2% |
| Volumen m5 / h1 | $29.503 / $401.095 |
| Trades m5 (compras / ventas) | 125 / 96 |
| Edad del par | 2,7 h |
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
| MCap | ≥ $50K | $69.728 | +10 |
| Volumen 24 h | ≥ $1M | $1.109.626 | +20 |
| Buy pressure m5 | > 55% (par maduro) | 57% | +15 |
| Edge temprano | edad < 4 h (par maduro) | edad 2,7 h | +8 |
| Volumen m5 | > $1K (par maduro) | $29.503 | +10 |
| Liquidez | ≥ $20K | $23.885 | +5 |
| Cambio 24 h | ≥ +50% | +56% | +10 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-08T09:41:24+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $50K, Volumen masivo, Buy pressure >55%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 36 de 21.355 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/10/2026 09:41 UTC, hasta 10/10/2026 09:41 UTC · vigente: quedan 47,4 h.
- **Aceleración al detectar:** cambio m5 -17,4% · h1 -50,2% · h24 +56% · volumen m5/h1 0,07 · edad del par 2,7 h.
- **Precio de entrada** (alerta): $0,00007264.
- **Consulta 08/10/2026 10:14 UTC:** $0,000003140 (-95,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump_2026-10-08_094124.json` · blob `eaedc8359b1f1aff0af3c5c56b63c88896332408` · commit `9a3c2d7` (2026-10-08T10:08:38Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-08_093513.json` · blob `bcfa335675b297b10ef089c017cf84f801b11ae7` · commit `9a3c2d7` (2026-10-08T10:08:38Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-08_094124`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump · registro · 08/10/2026 09:41 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump · HTTP 200 · 08/10/2026 10:14 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump/report · HTTP 200 · 08/10/2026 10:14 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump · HTTP 200 · 08/10/2026 10:14 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/52Qg1oPv3YUScwK8Z4887fwuRWRGr1H2XtcpvETfyCbT/ohlcv/hour?limit=1000 · HTTP 200 · 08/10/2026 10:14 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump · HTTP 404 · 08/10/2026 10:14 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ORGANISMEUSDT · HTTP 400 · 08/10/2026 10:14 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ORGANISME-USD · HTTP 404 · 08/10/2026 10:14 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.369 vs $3.372 → 0,08%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000003140 vs $0,000003141 → 0,05%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump_2026-10-08_094124.json',encoding='utf-8'));d=d.get('7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump',d);p=mock.patch('time.time',return_value=1791452484);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 7fxxzRh3Sotcto3qduvjFv6jyR3doPRd8vpDeQiUpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/10/2026 10:14 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `8823cf94bfb45b9e…`
