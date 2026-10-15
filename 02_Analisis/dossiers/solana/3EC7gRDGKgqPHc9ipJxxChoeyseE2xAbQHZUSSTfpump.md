# Sycamore Core (SYCAMORE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0009959 · liquidez $88.364 · mcap $965.794 (al detectar)  
Detectado el 15/10/2026 11:59 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 17/10/2026 11:59 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SYCAMORE

Estudio de cómo se adquiere SYCAMORE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 15/10/2026 12:27 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 15/10/2026 11:59 UTC | pumpswap `5cX7awH…jYDq` | $88.364 | 5% | 0,226% | 2,263% | 22,634% | $442 | $1.325 |
| consulta 15/10/2026 12:27 UTC | pumpswap `5cX7awH…jYDq` | $77.350 | 5% | 0,259% | 2,586% | 25,857% | $387 | $1.160 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump`
5. Configurar el slippage: 5% (liquidez $77.350, consulta 15/10/2026 12:27 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump) y el par en DexScreener (https://dexscreener.com/solana/5cX7awH9czi1VKK2SFabfCSzyVbytf7KBExiJiP6jYDq); mint authority / freeze authority: revocada / revocada · holders 3.050 · top-10 14,77% (consulta 15/10/2026 12:27 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump
- Par en DexScreener: https://dexscreener.com/solana/5cX7awH9czi1VKK2SFabfCSzyVbytf7KBExiJiP6jYDq
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.050 · top-10 14,77% (consulta 15/10/2026 12:27 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Sycamore Core / SYCAMORE | registro de la detección (trending) |
| Mint / contrato | `3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `5cX7awH9czi1VKK2SFabfCSzyVbytf7KBExiJiP6jYDq` | DexScreener, al detectar (3 par(es) en la consulta 15/10/2026 12:27 UTC) |
| Deployer | `4ksbmVvz7CyhAxG4jnz8SmiRFtRMLTL4yzcP4NvvSZdW` | RugCheck `creator` |
| Par creado | 15/10/2026 07:50 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 4,2 h / 4,2 h / 4,6 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 15/10/2026 12:27 UTC |
| Holders / top-10 | 3.050 / 14,77% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 15/10/2026 12:27 UTC |
| Holders efectivos del top-10 | 5,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 15/10/2026 12:27 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 15/10/2026 12:27 UTC |
| Links | DexScreener: https://dexscreener.com/solana/5cX7awH9czi1VKK2SFabfCSzyVbytf7KBExiJiP6jYDq · Solscan: https://solscan.io/token/3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump · pump.fun: https://pump.fun/coin/3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump · web: https://sycamore.lat/ · twitter: https://x.com/sycamore_hub | consulta 15/10/2026 12:27 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 15/10/2026 12:27 UTC)
- **Historia:**
  - Par creado el 15/10/2026 07:50 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 15/10/2026 11:59 UTC, con el par a 4,2 h de creado: precio $0,0009959, mcap $965.794, liquidez $88.364.
  - Velas de 1 h de GeckoTerminal (6, desde 15/10/2026 07:00 UTC): apertura $0,00005073 · máximo $0,001885 (15/10/2026 11:00 UTC) · mínimo $0,00003673 (15/10/2026 07:00 UTC) · último cierre $0,0007582.
  - En la consulta 15/10/2026 12:27 UTC: precio $0,0007648, liquidez $77.350, FDV $741.637.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 15/10/2026 11:59 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0009959 |
| Liquidez | $88.364 |
| MCap | $965.794 |
| Volumen 24 h | $2.061.748 |
| Cambio 24 h | +1.863% |
| Cambio m5 / h1 | +8,7% / +97,1% |
| Volumen m5 / h1 | $17.570 / $432.291 |
| Trades m5 (compras / ventas) | 63 / 33 |
| Edad del par | 4,2 h |
| Score del feed (WS) | 75 |

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

Desglose no reproducible desde los motivos registrados (suma 100 vs score 100; motivos sin regla: Anticipación (lib_early_signals early-0.2): +1 — buy_pressure_shift: compras 66% en 5 min vs 53% en 1 h → +1.3): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-15T11:59:32+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=9.1% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 59 de 35.960 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 15/10/2026 11:59 UTC, hasta 17/10/2026 11:59 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +8,7% · h1 +97,1% · h24 +1.863% · volumen m5/h1 0,04 · edad del par 4,2 h.
- **Precio de entrada** (alerta): $0,0009959.
- **Consulta 15/10/2026 12:27 UTC:** $0,0007648 (-23,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump_2026-10-15_115932.json` · blob `39cc694ac517ca2d8359bbd3e8acb9a452fd1298` · commit `fa70729` (2026-10-15T12:19:07Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-15_115332.json` · blob `51386d8b7cc7cc32ff3cd1c9362e43262f73de1a` · commit `fa70729` (2026-10-15T12:19:07Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-15_115932`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump · registro · 15/10/2026 11:59 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump · HTTP 200 · 15/10/2026 12:27 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump/report · HTTP 200 · 15/10/2026 12:27 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump · HTTP 200 · 15/10/2026 12:27 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/5cX7awH9czi1VKK2SFabfCSzyVbytf7KBExiJiP6jYDq/ohlcv/hour?limit=1000 · HTTP 200 · 15/10/2026 12:27 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump · HTTP 404 · 15/10/2026 12:27 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SYCAMOREUSDT · HTTP 400 · 15/10/2026 12:27 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SYCAMORE-USD · HTTP 404 · 15/10/2026 12:27 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $77.350 vs $76.298 → 1,36%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0007648 vs $0,0007582 → 0,87%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump_2026-10-15_115932.json',encoding='utf-8'));d=d.get('3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump',d);p=mock.patch('time.time',return_value=1792065572);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 15/10/2026 12:27 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `5ffc8a70cec3947a…`
