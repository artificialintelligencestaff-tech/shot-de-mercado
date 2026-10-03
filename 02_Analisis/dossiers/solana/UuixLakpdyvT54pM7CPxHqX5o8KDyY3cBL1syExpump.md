# ConConAI (ConConAI) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,002061 · liquidez $129.533 · mcap $2.059.130 (al detectar)  
Detectado el 03/10/2026 08:52 UTC por: MCap > $1M, Volumen decente, Buy pressure >55% (score 88, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 05/10/2026 08:52 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ConConAI

Estudio de cómo se adquiere ConConAI, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 03/10/2026 09:13 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 03/10/2026 08:52 UTC | pumpswap `Cmz6J5q…W87a` | $129.533 | 5% | 0,154% | 1,544% | 15,440% | $648 | $1.943 |
| consulta 03/10/2026 09:13 UTC | pumpswap `Cmz6J5q…W87a` | $129.853 | 5% | 0,154% | 1,540% | 15,402% | $649 | $1.948 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump`
5. Configurar el slippage: 5% (liquidez $129.853, consulta 03/10/2026 09:13 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump) y el par en DexScreener (https://dexscreener.com/solana/Cmz6J5q9j9bbbn7P7j6UnL5RaTBcx7Vnq4z8PJ8qW87a); mint authority / freeze authority: revocada / revocada · holders 3.993 · top-10 11,89% (consulta 03/10/2026 09:13 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump
- Par en DexScreener: https://dexscreener.com/solana/Cmz6J5q9j9bbbn7P7j6UnL5RaTBcx7Vnq4z8PJ8qW87a
- Página del lanzamiento (pump.fun): https://pump.fun/coin/UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.993 · top-10 11,89% (consulta 03/10/2026 09:13 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | ConConAI / ConConAI | registro de la detección (pumpportal) |
| Mint / contrato | `UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Cmz6J5q9j9bbbn7P7j6UnL5RaTBcx7Vnq4z8PJ8qW87a` | DexScreener, al detectar (2 par(es) en la consulta 03/10/2026 09:13 UTC) |
| Deployer | `GWQkDp5m9e4HcE3EpVhEBAsCtvYDmQ98vxCkeZhEcCpC` | PumpPortal (evento create), al detectar |
| Par creado | 03/10/2026 07:52 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,1 min / 60,1 min / 81,1 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 03/10/2026 09:13 UTC |
| Holders / top-10 | 3.993 / 11,89% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 03/10/2026 09:13 UTC |
| Holders efectivos del top-10 | 7,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 03/10/2026 09:13 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 03/10/2026 09:13 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Cmz6J5q9j9bbbn7P7j6UnL5RaTBcx7Vnq4z8PJ8qW87a · Solscan: https://solscan.io/token/UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump · pump.fun: https://pump.fun/coin/UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump · web / Telegram / X: no publicados en DexScreener | consulta 03/10/2026 09:13 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 03/10/2026 09:13 UTC)
- **Historia:**
  - Par creado el 03/10/2026 07:52 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 03/10/2026 08:52 UTC, con el par a 60,1 min de creado: precio $0,002061, mcap $2.059.130, liquidez $129.533.
  - Velas de 1 h de GeckoTerminal (3, desde 03/10/2026 07:00 UTC): apertura $0,0003095 · máximo $0,002091 (03/10/2026 09:00 UTC) · mínimo $0,00004958 (03/10/2026 07:00 UTC) · último cierre $0,002068.
  - En la consulta 03/10/2026 09:13 UTC: precio $0,002068, liquidez $129.853, FDV $2.066.452.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 03/10/2026 08:52 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,002061 |
| Liquidez | $129.533 |
| MCap | $2.059.130 |
| Volumen 24 h | $61.544 |
| Cambio 24 h | +4.054% |
| Cambio m5 / h1 | -1,0% / +7,4% |
| Volumen m5 / h1 | $757 / $8.290 |
| Trades m5 (compras / ventas) | 13 / 10 |
| Edad del par | 60,1 min |
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

Desglose reconstruido desde los motivos registrados; suma 88 = score registrado 88 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $1M | $2.059.130 | +25 |
| Volumen 24 h | ≥ $50K | $61.544 | +10 |
| Buy pressure m5 | > 55% (par maduro) | 57% | +15 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,1 min | +8 |
| Volumen m5 | > $500 (par maduro) | $757 | +5 |
| Liquidez | ≥ $100K | $129.533 | +15 |
| Cambio 24 h | ≥ +50% | +4.054% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +4.054% · liq/mcap 6,3% | +0 |
| **Total** | recortado a 0–100 |  | **88** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-03T08:52:55+00:00, sin estado previo): **88** · motivos: MCap > $1M, Volumen decente, Buy pressure >55%, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=6.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 9 de 10.140 tokens analizados (0,09%) quedan ≥ 56. Con score 88, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 03/10/2026 08:52 UTC, hasta 05/10/2026 08:52 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -1,0% · h1 +7,4% · h24 +4.054% · volumen m5/h1 0,09 · edad del par 60,1 min.
- **Precio de entrada** (alerta): $0,002061.
- **Consulta 03/10/2026 09:13 UTC:** $0,002068 (+0,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump_2026-10-03_085255.json` · blob `c647dc6ba35ac748c954a66664d905bdaa12738c` · commit `fce2ca1` (2026-10-03T09:07:20Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-03_085255`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump · registro · 03/10/2026 08:52 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump · HTTP 200 · 03/10/2026 09:13 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump/report · HTTP 200 · 03/10/2026 09:13 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump · HTTP 200 · 03/10/2026 09:13 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Cmz6J5q9j9bbbn7P7j6UnL5RaTBcx7Vnq4z8PJ8qW87a/ohlcv/hour?limit=1000 · HTTP 200 · 03/10/2026 09:13 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump · HTTP 404 · 03/10/2026 09:13 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=CONCONAIUSDT · HTTP 400 · 03/10/2026 09:13 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/CONCONAI-USD · HTTP 404 · 03/10/2026 09:13 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $129.853 vs $130.684 → 0,64%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002068 vs $0,002068 → 0,01%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump_2026-10-03_085255.json',encoding='utf-8'));d=d.get('UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump',d);p=mock.patch('time.time',return_value=1791017575);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint UuixLakpdyvT54pM7CPxHqX5o8KDyY3cBL1syExpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 03/10/2026 09:13 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `d8e5b8272a92cfc6…`
