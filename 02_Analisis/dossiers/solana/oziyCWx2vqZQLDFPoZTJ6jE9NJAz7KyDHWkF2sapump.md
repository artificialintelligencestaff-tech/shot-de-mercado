# XRPN (EVERNORTHX) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1693 · liquidez $1.134.455 · mcap $169.390.689 (al detectar)  
Detectado el 13/10/2026 07:12 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 15/10/2026 07:12 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir EVERNORTHX

Estudio de cómo se adquiere EVERNORTHX, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 13/10/2026 07:21 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 13/10/2026 07:12 UTC | pumpswap `X1NcoXx…nTp8` | $1.134.455 | 1% | 0,018% | 0,176% | 1,763% | $5.672 | $17.017 |
| consulta 13/10/2026 07:21 UTC | pumpswap `X1NcoXx…nTp8` | $1.141.267 | 1% | 0,018% | 0,175% | 1,752% | $5.706 | $17.119 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump`
5. Configurar el slippage: 1% (liquidez $1.141.267, consulta 13/10/2026 07:21 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump) y el par en DexScreener (https://dexscreener.com/solana/X1NcoXxv8cQnyGBpYS6a6yPa5mSyN34AqNpv6kSnTp8); mint authority / freeze authority: revocada / revocada · holders 2.062 · top-10 9,99% (consulta 13/10/2026 07:21 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump
- Par en DexScreener: https://dexscreener.com/solana/X1NcoXxv8cQnyGBpYS6a6yPa5mSyN34AqNpv6kSnTp8
- Página del lanzamiento (pump.fun): https://pump.fun/coin/oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.062 · top-10 9,99% (consulta 13/10/2026 07:21 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | XRPN / EVERNORTHX | registro de la detección (trending) |
| Mint / contrato | `oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `X1NcoXxv8cQnyGBpYS6a6yPa5mSyN34AqNpv6kSnTp8` | DexScreener, al detectar (2 par(es) en la consulta 13/10/2026 07:21 UTC) |
| Deployer | `Bf11fKKRbpQ89HEZYG24MHFvbfqGtrdz2uRsR36KkBAP` | RugCheck `creator` |
| Par creado | 13/10/2026 06:12 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,1 min / 60,1 min / 69,2 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 13/10/2026 07:21 UTC |
| Holders / top-10 | 2.062 / 9,99% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 13/10/2026 07:21 UTC |
| Holders efectivos del top-10 | 1,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 13/10/2026 07:21 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 13/10/2026 07:21 UTC |
| Links | DexScreener: https://dexscreener.com/solana/X1NcoXxv8cQnyGBpYS6a6yPa5mSyN34AqNpv6kSnTp8 · Solscan: https://solscan.io/token/oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump · pump.fun: https://pump.fun/coin/oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump · web / Telegram / X: no publicados en DexScreener | consulta 13/10/2026 07:21 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 13/10/2026 07:21 UTC)
- **Historia:**
  - Par creado el 13/10/2026 06:12 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 13/10/2026 07:12 UTC, con el par a 60,1 min de creado: precio $0,1693, mcap $169.390.689, liquidez $1.134.455.
  - Velas de 1 h de GeckoTerminal (2, desde 13/10/2026 06:00 UTC): apertura $0,1562 · máximo $0,1715 (13/10/2026 07:00 UTC) · mínimo $0,00004500 (13/10/2026 06:00 UTC) · último cierre $0,1707.
  - En la consulta 13/10/2026 07:21 UTC: precio $0,1713, liquidez $1.141.267, FDV $171.376.748.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 13/10/2026 07:12 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1693 |
| Liquidez | $1.134.455 |
| MCap | $169.390.689 |
| Volumen 24 h | $574.653 |
| Cambio 24 h | +377.226% |
| Cambio m5 / h1 | +0,7% / +377.226,0% |
| Volumen m5 / h1 | $3.009 / $574.653 |
| Trades m5 (compras / ventas) | 21 / 9 |
| Edad del par | 60,1 min |
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
| MCap | ≥ $1M | $169.390.689 | +25 |
| Volumen 24 h | ≥ $100K | $574.653 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 70% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,7% · h1 +377.226,0% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,1 min | +8 |
| Volumen m5 | > $1K (par maduro) | $3.009 | +10 |
| Liquidez | ≥ $100K | $1.134.455 | +15 |
| Cambio 24 h | ≥ +50% | +377.226% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +377.226% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-13T07:12:20+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 52 de 32.891 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 13/10/2026 07:12 UTC, hasta 15/10/2026 07:12 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +0,7% · h1 +377.226,0% · h24 +377.226% · volumen m5/h1 0,01 · edad del par 60,1 min.
- **Precio de entrada** (alerta): $0,1693.
- **Consulta 13/10/2026 07:21 UTC:** $0,1713 (+1,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump_2026-10-13_071220.json` · blob `009f7207466176b6085683c6384aefbec9b86c9a` · commit `2016c59` (2026-10-13T07:14:52Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-13_064537.json` · blob `c29e9d120c0e40f0ee0b205d7d31b32e1b739a17` · commit `2016c59` (2026-10-13T07:14:52Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-13_071220`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump · registro · 13/10/2026 07:12 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump · HTTP 200 · 13/10/2026 07:21 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump/report · HTTP 200 · 13/10/2026 07:21 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump · HTTP 200 · 13/10/2026 07:21 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/X1NcoXxv8cQnyGBpYS6a6yPa5mSyN34AqNpv6kSnTp8/ohlcv/hour?limit=1000 · HTTP 200 · 13/10/2026 07:21 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump · HTTP 404 · 13/10/2026 07:21 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=EVERNORTHXUSDT · HTTP 400 · 13/10/2026 07:21 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/EVERNORTHX-USD · HTTP 404 · 13/10/2026 07:21 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.141.267 vs $1.141.605 → 0,03%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1713 vs $0,1707 → 0,34%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump_2026-10-13_071220.json',encoding='utf-8'));d=d.get('oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump',d);p=mock.patch('time.time',return_value=1791875540);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint oziyCWx2vqZQLDFPoZTJ6jE9NJAz7KyDHWkF2sapump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 13/10/2026 07:21 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `6af86cfcff166d97…`
