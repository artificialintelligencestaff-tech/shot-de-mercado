# Super Agency (AGENCY) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000002734 · liquidez $3.250 · mcap $2.694 (al detectar)  
Detectado el 07/10/2026 01:39 UTC por: WS score muy alto, MCap bajo, Volumen masivo (score 87, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 09/10/2026 01:39 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir AGENCY

Estudio de cómo se adquiere AGENCY, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/10/2026 01:55 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/10/2026 01:39 UTC | pumpswap `2J9Av4L…Cwof` | $3.250 | 10% | 6,154% | 61,542% | 615,424% | $16 | $49 |
| consulta 07/10/2026 01:55 UTC | pumpswap `2J9Av4L…Cwof` | $3.250 | 10% | 6,154% | 61,542% | 615,424% | $16 | $49 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump`
5. Configurar el slippage: 10% (liquidez $3.250, consulta 07/10/2026 01:55 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump) y el par en DexScreener (https://dexscreener.com/solana/2J9Av4LaBNUQRW4fS7W4gSYcDutBuDnfXQaD2F8zCwof); mint authority / freeze authority: revocada / revocada · holders 211 · top-10 100,34% (consulta 07/10/2026 01:55 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump
- Par en DexScreener: https://dexscreener.com/solana/2J9Av4LaBNUQRW4fS7W4gSYcDutBuDnfXQaD2F8zCwof
- Página del lanzamiento (pump.fun): https://pump.fun/coin/CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 211 · top-10 100,34% (consulta 07/10/2026 01:55 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Super Agency / AGENCY | registro de la detección (trending) |
| Mint / contrato | `CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `2J9Av4LaBNUQRW4fS7W4gSYcDutBuDnfXQaD2F8zCwof` | DexScreener, al detectar (2 par(es) en la consulta 07/10/2026 01:55 UTC) |
| Deployer | `EXyWvShEhVbEJB1qLf6Qi2rY7Vgt4H8C5DZqpkZ6RK7h` | RugCheck `creator` |
| Par creado | 06/10/2026 19:15 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 6,4 h / 6,4 h / 6,7 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/10/2026 01:55 UTC |
| Holders / top-10 | 211 / 100,34% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/10/2026 01:55 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/10/2026 01:55 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 07/10/2026 01:55 UTC |
| Links | DexScreener: https://dexscreener.com/solana/2J9Av4LaBNUQRW4fS7W4gSYcDutBuDnfXQaD2F8zCwof · Solscan: https://solscan.io/token/CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump · pump.fun: https://pump.fun/coin/CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump · web: https://superagency.lol · twitter: https://x.com/superagencysol | consulta 07/10/2026 01:55 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/10/2026 01:55 UTC)
- **Historia:**
  - Par creado el 06/10/2026 19:15 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/10/2026 01:39 UTC, con el par a 6,4 h de creado: precio $0,000002734, mcap $2.694, liquidez $3.250.
  - Velas de 1 h de GeckoTerminal (7, desde 06/10/2026 19:00 UTC): apertura $0,00008969 · máximo $0,0002164 (06/10/2026 20:00 UTC) · mínimo $0,000002732 (07/10/2026 01:00 UTC) · último cierre $0,000002732.
  - En la consulta 07/10/2026 01:55 UTC: precio $0,000002734, liquidez $3.250, FDV $2.694.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/10/2026 01:39 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000002734 |
| Liquidez | $3.250 |
| MCap | $2.694 |
| Volumen 24 h | $1.735.589 |
| Cambio 24 h | -97% |
| Cambio m5 / h1 | -1,6% / -0,7% |
| Volumen m5 / h1 | $5 / $5 |
| Trades m5 (compras / ventas) | 1 / 1 |
| Edad del par | 6,4 h |
| Score del feed (WS) | 81 |

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

Desglose no reproducible desde los motivos registrados (suma 84 vs score 87; motivos sin regla: Anticipación (lib_early_signals early-0.2): +3 — volume_acceleration: vol 5 min ×11.4 la tasa horaria → +3): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-07T01:39:51+00:00, sin estado previo): **84** · motivos: WS score muy alto, MCap bajo, Volumen masivo, Volumen acelerado (5m/1h > 50%), Trades acelerados (5m/1h > 50%), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 23 de 17.541 tokens analizados (0,13%) quedan ≥ 56. Con score 84, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/10/2026 01:39 UTC, hasta 09/10/2026 01:39 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -1,6% · h1 -0,7% · h24 -97% · volumen m5/h1 0,95 · edad del par 6,4 h.
- **Precio de entrada** (alerta): $0,000002734.
- **Consulta 07/10/2026 01:55 UTC:** $0,000002734 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump_2026-10-07_013951.json` · blob `54cc6b6bb803238598e3d3d5d3f8cc58cf0b761d` · commit `40d2778` (2026-10-07T01:49:43Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-07_013252.json` · blob `fb01d54fd666d8a18fd369562d5df9fa44054121` · commit `40d2778` (2026-10-07T01:49:43Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-07_013951`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump · registro · 07/10/2026 01:39 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump · HTTP 200 · 07/10/2026 01:55 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump/report · HTTP 200 · 07/10/2026 01:55 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump · HTTP 200 · 07/10/2026 01:55 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/2J9Av4LaBNUQRW4fS7W4gSYcDutBuDnfXQaD2F8zCwof/ohlcv/hour?limit=1000 · HTTP 200 · 07/10/2026 01:55 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump · HTTP 404 · 07/10/2026 01:55 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AGENCYUSDT · HTTP 400 · 07/10/2026 01:55 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AGENCY-USD · HTTP 404 · 07/10/2026 01:55 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.250 vs $3.246 → 0,11%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002734 vs $0,000002732 → 0,09%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump_2026-10-07_013951.json',encoding='utf-8'));d=d.get('CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump',d);p=mock.patch('time.time',return_value=1791337191);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint CsCPttDSDsKxhCiVrYvCpFHtT9A3Uni8tbSfqpDXpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/10/2026 01:55 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `81d9f69a34d964e9…`
