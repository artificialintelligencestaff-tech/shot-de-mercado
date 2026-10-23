# Big Titty Coin (BTC) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0008281 · liquidez $81.991 · mcap $822.576 (al detectar)  
Detectado el 22/10/2026 23:55 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 24/10/2026 23:55 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir BTC

Estudio de cómo se adquiere BTC, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Cotiza en exchanges centralizados (blue chip): Binance (https://www.binance.com/en/trade/BTC_USDT) · Coinbase (https://www.coinbase.com/advanced-trade/spot/BTC-USD) · Kraken (https://pro.kraken.com/app/trade/BTC-USD)

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 22/10/2026 23:55 UTC | pumpswap `4UPijxP…DBbH` | $81.991 | 5% | 0,244% | 2,439% | 24,393% | $410 | $1.230 |
| consulta 23/10/2026 00:24 UTC | pumpswap `4UPijxP…DBbH` | $85.226 | 5% | 0,235% | 2,347% | 23,467% | $426 | $1.278 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump`
5. Configurar el slippage: 5% (liquidez $85.226, consulta 23/10/2026 00:24 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump) y el par en DexScreener (https://dexscreener.com/solana/4UPijxPh3AcSHtXzLFHSjbDibZUNnFFYVhzTjpCqDBbH); mint authority / freeze authority: revocada / revocada · holders 5.821 · top-10 7,52% (consulta 23/10/2026 00:24 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump
- Par en DexScreener: https://dexscreener.com/solana/4UPijxPh3AcSHtXzLFHSjbDibZUNnFFYVhzTjpCqDBbH
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.821 · top-10 7,52% (consulta 23/10/2026 00:24 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Big Titty Coin / BTC | registro de la detección (trending) |
| Mint / contrato | `HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `4UPijxPh3AcSHtXzLFHSjbDibZUNnFFYVhzTjpCqDBbH` | DexScreener, al detectar (2 par(es) en la consulta 23/10/2026 00:24 UTC) |
| Deployer | `AyAqvSRQsMF6wt3F7e5GUiYMeLUyg7eFbt5xDCndQkaH` | RugCheck `creator` |
| Par creado | 22/10/2026 20:39 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 3,3 h / 3,3 h / 3,7 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 23/10/2026 00:24 UTC |
| Holders / top-10 | 5.821 / 7,52% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 23/10/2026 00:24 UTC |
| Holders efectivos del top-10 | 2,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 23/10/2026 00:24 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 23/10/2026 00:24 UTC |
| Links | DexScreener: https://dexscreener.com/solana/4UPijxPh3AcSHtXzLFHSjbDibZUNnFFYVhzTjpCqDBbH · Solscan: https://solscan.io/token/HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump · pump.fun: https://pump.fun/coin/HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump · web: https://www.bigtittycoin.lol/ · twitter: https://x.com/BigTittyCoin_S | consulta 23/10/2026 00:24 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo h: blue chips, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 23/10/2026 00:24 UTC)
- **Historia:**
  - Par creado el 22/10/2026 20:39 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 22/10/2026 23:55 UTC, con el par a 3,3 h de creado: precio $0,0008281, mcap $822.576, liquidez $81.991.
  - Velas de 1 h de GeckoTerminal (5, desde 22/10/2026 20:00 UTC): apertura $0,0001982 · máximo $0,001576 (22/10/2026 23:00 UTC) · mínimo $0,00005584 (22/10/2026 20:00 UTC) · último cierre $0,0008781.
  - En la consulta 23/10/2026 00:24 UTC: precio $0,0008901, liquidez $85.226, FDV $884.191.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 22/10/2026 23:55 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0008281 |
| Liquidez | $81.991 |
| MCap | $822.576 |
| Volumen 24 h | $2.391.401 |
| Cambio 24 h | +1.371% |
| Cambio m5 / h1 | -24,7% / +210,0% |
| Volumen m5 / h1 | $63.850 / $756.935 |
| Trades m5 (compras / ventas) | 1.642 / 377 |
| Edad del par | 3,3 h |
| Score del feed (WS) | 68 |

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
| Score del feed | score WS × 0,3 | WS 68 × 0,3 | +20,3 |
| MCap | ≥ $100K | $822.576 | +15 |
| Volumen 24 h | ≥ $1M | $2.391.401 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 81% | +25 |
| Edge temprano | edad < 4 h (par maduro) | edad 3,3 h | +8 |
| Volumen m5 | > $1K (par maduro) | $63.850 | +10 |
| Liquidez | ≥ $50K | $81.991 | +10 |
| Cambio 24 h | ≥ +50% | +1.371% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.371% · liq/mcap 10,0% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-22T23:55:01+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=10.0% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 75 de 44.381 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 22/10/2026 23:55 UTC, hasta 24/10/2026 23:55 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -24,7% · h1 +210,0% · h24 +1.371% · volumen m5/h1 0,08 · edad del par 3,3 h.
- **Precio de entrada** (alerta): $0,0008281.
- **Consulta 23/10/2026 00:24 UTC:** $0,0008901 (+7,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump_2026-10-22_235501.json` · blob `191a3961423e8ff218e457d8e7e4d6d73827c110` · commit `0ccb623` (2026-10-23T00:17:10Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-22_234823.json` · blob `438fde9d2625f8226139853b8707fe53e046badb` · commit `0ccb623` (2026-10-23T00:17:10Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-22_235501`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump · registro · 22/10/2026 23:55 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump · HTTP 200 · 23/10/2026 00:24 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump/report · HTTP 200 · 23/10/2026 00:24 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump · HTTP 200 · 23/10/2026 00:24 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/4UPijxPh3AcSHtXzLFHSjbDibZUNnFFYVhzTjpCqDBbH/ohlcv/hour?limit=1000 · HTTP 200 · 23/10/2026 00:24 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump · HTTP 404 · 23/10/2026 00:24 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BTCUSDT · HTTP 200 · 23/10/2026 00:24 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BTC-USD · HTTP 200 · 23/10/2026 00:24 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $85.226 vs $84.131 → 1,29%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0008901 vs $0,0008781 → 1,35%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump_2026-10-22_235501.json',encoding='utf-8'));d=d.get('HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump',d);p=mock.patch('time.time',return_value=1792713301);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HKh5uh37FyRhRbDPcmPCoTcfByRLdY65RFZj9AvZpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 23/10/2026 00:24 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `6f43cf6c8a715384…`
