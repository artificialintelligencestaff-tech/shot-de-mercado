# Higgspad (HIGGS) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003999 · liquidez $181.996 · mcap $3.996.610 (al detectar)  
Detectado el 06/10/2026 02:53 UTC por: MCap > $1M, Volumen decente, Buy pressure >60% (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 08/10/2026 02:53 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HIGGS

Estudio de cómo se adquiere HIGGS, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 03:12 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 02:53 UTC | pumpswap `5oyKpaX…rA6b` | $181.996 | 5% | 0,110% | 1,099% | 10,989% | $910 | $2.730 |
| consulta 06/10/2026 03:12 UTC | pumpswap `5oyKpaX…rA6b` | $184.167 | 5% | 0,109% | 1,086% | 10,860% | $921 | $2.762 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump`
5. Configurar el slippage: 5% (liquidez $184.167, consulta 06/10/2026 03:12 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump) y el par en DexScreener (https://dexscreener.com/solana/5oyKpaX8hQATpJ86VAMRDAhJxpMMJDjgMEc48Ay7rA6b); mint authority / freeze authority: revocada / revocada · holders 2.333 · top-10 16,07% (consulta 06/10/2026 03:12 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump
- Par en DexScreener: https://dexscreener.com/solana/5oyKpaX8hQATpJ86VAMRDAhJxpMMJDjgMEc48Ay7rA6b
- Página del lanzamiento (pump.fun): https://pump.fun/coin/7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.333 · top-10 16,07% (consulta 06/10/2026 03:12 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Higgspad / HIGGS | registro de la detección (pumpportal) |
| Mint / contrato | `7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `5oyKpaX8hQATpJ86VAMRDAhJxpMMJDjgMEc48Ay7rA6b` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 03:12 UTC) |
| Deployer | `ZXEW1FXj4huSaEBB9syiYkkuDx7U1JxAQCssFfZauGr` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 01:52 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,5 min / 60,5 min / 79,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 03:12 UTC |
| Holders / top-10 | 2.333 / 16,07% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 03:12 UTC |
| Holders efectivos del top-10 | 9,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 03:12 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 03:12 UTC |
| Links | DexScreener: https://dexscreener.com/solana/5oyKpaX8hQATpJ86VAMRDAhJxpMMJDjgMEc48Ay7rA6b · Solscan: https://solscan.io/token/7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump · pump.fun: https://pump.fun/coin/7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump · web / Telegram / X: no publicados en DexScreener | consulta 06/10/2026 03:12 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 03:12 UTC)
- **Historia:**
  - Par creado el 06/10/2026 01:52 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 02:53 UTC, con el par a 60,5 min de creado: precio $0,003999, mcap $3.996.610, liquidez $181.996.
  - Velas de 1 h de GeckoTerminal (3, desde 06/10/2026 01:00 UTC): apertura $0,0003740 · máximo $0,004095 (06/10/2026 03:00 UTC) · mínimo $0,00005009 (06/10/2026 01:00 UTC) · último cierre $0,004049.
  - En la consulta 06/10/2026 03:12 UTC: precio $0,004095, liquidez $184.167, FDV $4.092.941.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 02:53 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003999 |
| Liquidez | $181.996 |
| MCap | $3.996.610 |
| Volumen 24 h | $80.902 |
| Cambio 24 h | +7.876% |
| Cambio m5 / h1 | +1,0% / +43,4% |
| Volumen m5 / h1 | $546 / $14.522 |
| Trades m5 (compras / ventas) | 67 / 27 |
| Edad del par | 60,5 min |
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
| MCap | ≥ $1M | $3.996.610 | +25 |
| Volumen 24 h | ≥ $50K | $80.902 | +10 |
| Buy pressure m5 | > 60% (par maduro) | 71% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +1,0% · h1 +43,4% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,5 min | +8 |
| Volumen m5 | > $500 (par maduro) | $546 | +5 |
| Liquidez | ≥ $100K | $181.996 | +15 |
| Cambio 24 h | ≥ +50% | +7.876% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +7.876% · liq/mcap 4,6% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T02:53:19+00:00, sin estado previo): **100** · motivos: MCap > $1M, Volumen decente, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 17 de 14.032 tokens analizados (0,12%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 02:53 UTC, hasta 08/10/2026 02:53 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +1,0% · h1 +43,4% · h24 +7.876% · volumen m5/h1 0,04 · edad del par 60,5 min.
- **Precio de entrada** (alerta): $0,003999.
- **Consulta 06/10/2026 03:12 UTC:** $0,004095 (+2,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump_2026-10-06_025319.json` · blob `e6f9d69d25563bd92c4d968e094220dfcc1a0e11` · commit `b2da03a` (2026-10-06T03:05:51Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_025319`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump · registro · 06/10/2026 02:53 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump · HTTP 200 · 06/10/2026 03:12 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump/report · HTTP 200 · 06/10/2026 03:12 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump · HTTP 200 · 06/10/2026 03:12 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/5oyKpaX8hQATpJ86VAMRDAhJxpMMJDjgMEc48Ay7rA6b/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 03:12 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump · HTTP 404 · 06/10/2026 03:12 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HIGGSUSDT · HTTP 400 · 06/10/2026 03:12 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HIGGS-USD · HTTP 404 · 06/10/2026 03:12 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $184.167 vs $183.899 → 0,15%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,004095 vs $0,004049 → 1,12%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump_2026-10-06_025319.json',encoding='utf-8'));d=d.get('7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump',d);p=mock.patch('time.time',return_value=1791255199);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 7yeF9pQC5gP1Rrg9kqHonkzaZpGPLaWozkbKtP1qpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 03:12 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `bdd375077a33cdfb…`
