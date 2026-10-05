# Strategic Oil Supply (SOS) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001971 · liquidez $127.640 · mcap $1.969.575 (al detectar)  
Detectado el 05/10/2026 02:37 UTC por: MCap > $1M, Volumen decente, Buy pressure >55% (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 07/10/2026 02:37 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SOS

Estudio de cómo se adquiere SOS, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 05/10/2026 02:56 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 05/10/2026 02:37 UTC | pumpswap `9TDBzRa…dJrN` | $127.640 | 5% | 0,157% | 1,567% | 15,669% | $638 | $1.915 |
| consulta 05/10/2026 02:56 UTC | pumpswap `9TDBzRa…dJrN` | $127.315 | 5% | 0,157% | 1,571% | 15,709% | $637 | $1.910 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump`
5. Configurar el slippage: 5% (liquidez $127.315, consulta 05/10/2026 02:56 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump) y el par en DexScreener (https://dexscreener.com/solana/9TDBzRa6kyEzmuCqs6ZF8iqFANLss3h9DB3ztCEbdJrN); mint authority / freeze authority: revocada / revocada · holders 3.949 · top-10 11,98% (consulta 05/10/2026 02:56 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump
- Par en DexScreener: https://dexscreener.com/solana/9TDBzRa6kyEzmuCqs6ZF8iqFANLss3h9DB3ztCEbdJrN
- Página del lanzamiento (pump.fun): https://pump.fun/coin/fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.949 · top-10 11,98% (consulta 05/10/2026 02:56 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Strategic Oil Supply / SOS | registro de la detección (pumpportal) |
| Mint / contrato | `fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `9TDBzRa6kyEzmuCqs6ZF8iqFANLss3h9DB3ztCEbdJrN` | DexScreener, al detectar (2 par(es) en la consulta 05/10/2026 02:56 UTC) |
| Deployer | `8258CdwAZJ3zEeQyjTgiFLeW8Ewyy2tUmLxEJQfo3h5V` | PumpPortal (evento create), al detectar |
| Par creado | 05/10/2026 01:35 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 61,5 min / 61,5 min / 80,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 05/10/2026 02:56 UTC |
| Holders / top-10 | 3.949 / 11,98% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 05/10/2026 02:56 UTC |
| Holders efectivos del top-10 | 7,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 05/10/2026 02:56 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 05/10/2026 02:56 UTC |
| Links | DexScreener: https://dexscreener.com/solana/9TDBzRa6kyEzmuCqs6ZF8iqFANLss3h9DB3ztCEbdJrN · Solscan: https://solscan.io/token/fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump · pump.fun: https://pump.fun/coin/fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump · web / Telegram / X: no publicados en DexScreener | consulta 05/10/2026 02:56 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 05/10/2026 02:56 UTC)
- **Historia:**
  - Par creado el 05/10/2026 01:35 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 05/10/2026 02:37 UTC, con el par a 61,5 min de creado: precio $0,001971, mcap $1.969.575, liquidez $127.640.
  - Velas de 1 h de GeckoTerminal (2, desde 05/10/2026 01:00 UTC): apertura $0,0003023 · máximo $0,001986 (05/10/2026 02:00 UTC) · mínimo $0,00005030 (05/10/2026 01:00 UTC) · último cierre $0,001984.
  - En la consulta 05/10/2026 02:56 UTC: precio $0,001961, liquidez $127.315, FDV $1.959.680.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 05/10/2026 02:37 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001971 |
| Liquidez | $127.640 |
| MCap | $1.969.575 |
| Volumen 24 h | $59.350 |
| Cambio 24 h | +3.817% |
| Cambio m5 / h1 | +0,8% / +8,3% |
| Volumen m5 / h1 | $526 / $7.692 |
| Trades m5 (compras / ventas) | 10 / 8 |
| Edad del par | 61,5 min |
| Score del feed (WS) | n/d (feed sin score) |

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
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $1M | $1.969.575 | +25 |
| Volumen 24 h | ≥ $50K | $59.350 | +10 |
| Buy pressure m5 | > 55% (par maduro) | 56% | +15 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,8% · h1 +8,3% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 61,5 min | +8 |
| Volumen m5 | > $500 (par maduro) | $526 | +5 |
| Liquidez | ≥ $100K | $127.640 | +15 |
| Cambio 24 h | ≥ +50% | +3.817% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +3.817% · liq/mcap 6,5% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-05T02:37:25+00:00, sin estado previo): **100** · motivos: MCap > $1M, Volumen decente, Buy pressure >55%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=6.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 14 de 11.271 tokens analizados (0,12%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 05/10/2026 02:37 UTC, hasta 07/10/2026 02:37 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +0,8% · h1 +8,3% · h24 +3.817% · volumen m5/h1 0,07 · edad del par 61,5 min.
- **Precio de entrada** (alerta): $0,001971.
- **Consulta 05/10/2026 02:56 UTC:** $0,001961 (-0,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump_2026-10-05_023725.json` · blob `5b4499a35c34e08bac90ae1bfe09d7e5926833f8` · commit `a01852d` (2026-10-05T02:50:26Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-05_023725`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump · registro · 05/10/2026 02:37 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump · HTTP 200 · 05/10/2026 02:56 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump/report · HTTP 200 · 05/10/2026 02:56 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump · HTTP 200 · 05/10/2026 02:56 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/9TDBzRa6kyEzmuCqs6ZF8iqFANLss3h9DB3ztCEbdJrN/ohlcv/hour?limit=1000 · HTTP 200 · 05/10/2026 02:56 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump · HTTP 404 · 05/10/2026 02:56 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SOSUSDT · HTTP 400 · 05/10/2026 02:56 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SOS-USD · HTTP 404 · 05/10/2026 02:56 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $127.315 vs $128.149 → 0,65%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001961 vs $0,001984 → 1,17%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump_2026-10-05_023725.json',encoding='utf-8'));d=d.get('fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump',d);p=mock.patch('time.time',return_value=1791167845);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint fhXqm9Db8U23wiygiy4Ttm7FTEwUfP2Syi8f3irpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 05/10/2026 02:56 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `c2640a88240cbe51…`
