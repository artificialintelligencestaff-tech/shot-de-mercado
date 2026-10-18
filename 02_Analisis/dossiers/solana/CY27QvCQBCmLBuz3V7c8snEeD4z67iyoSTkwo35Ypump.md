# Eternia (Eternia) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0003008 · liquidez $58.008 · mcap $293.807 (al detectar)  
Detectado el 18/10/2026 01:04 UTC por: WS score muy alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 20/10/2026 01:04 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Eternia

Estudio de cómo se adquiere Eternia, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 18/10/2026 01:33 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 18/10/2026 01:04 UTC | pumpswap `ABqXgS5…qQZ2` | $58.008 | 5% | 0,345% | 3,448% | 34,478% | $290 | $870 |
| consulta 18/10/2026 01:33 UTC | pumpswap `ABqXgS5…qQZ2` | $58.521 | 5% | 0,342% | 3,418% | 34,176% | $293 | $878 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump`
5. Configurar el slippage: 5% (liquidez $58.521, consulta 18/10/2026 01:33 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump) y el par en DexScreener (https://dexscreener.com/solana/ABqXgS5c78P8Nix49kqsBTNQjAmMAhCBH2mvjq1zqQZ2); mint authority / freeze authority: revocada / revocada · holders 2.944 · top-10 18,72% (consulta 18/10/2026 01:33 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump
- Par en DexScreener: https://dexscreener.com/solana/ABqXgS5c78P8Nix49kqsBTNQjAmMAhCBH2mvjq1zqQZ2
- Página del lanzamiento (pump.fun): https://pump.fun/coin/CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.944 · top-10 18,72% (consulta 18/10/2026 01:33 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Eternia / Eternia | registro de la detección (trending) |
| Mint / contrato | `CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `ABqXgS5c78P8Nix49kqsBTNQjAmMAhCBH2mvjq1zqQZ2` | DexScreener, al detectar (2 par(es) en la consulta 18/10/2026 01:33 UTC) |
| Deployer | `FTtMrjemM4rm9Vq3MNgtbhbPyAt3tA5aZJpD8YmND52Y` | RugCheck `creator` |
| Par creado | 17/10/2026 02:47 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 22,3 h / 22,3 h / 22,8 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 18/10/2026 01:33 UTC |
| Holders / top-10 | 2.944 / 18,72% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 18/10/2026 01:33 UTC |
| Holders efectivos del top-10 | 3,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 18/10/2026 01:33 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 18/10/2026 01:33 UTC |
| Links | DexScreener: https://dexscreener.com/solana/ABqXgS5c78P8Nix49kqsBTNQjAmMAhCBH2mvjq1zqQZ2 · Solscan: https://solscan.io/token/CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump · pump.fun: https://pump.fun/coin/CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump · web: https://eternialabs.xyz/ · twitter: https://x.com/eternia_sys | consulta 18/10/2026 01:33 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 18/10/2026 01:33 UTC)
- **Historia:**
  - Par creado el 17/10/2026 02:47 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 18/10/2026 01:04 UTC, con el par a 22,3 h de creado: precio $0,0003008, mcap $293.807, liquidez $58.008.
  - Velas de 1 h de GeckoTerminal (24, desde 17/10/2026 02:00 UTC): apertura $0,00004312 · máximo $0,004333 (17/10/2026 09:00 UTC) · mínimo $0,00004286 (17/10/2026 02:00 UTC) · último cierre $0,0003019.
  - En la consulta 18/10/2026 01:33 UTC: precio $0,0003023, liquidez $58.521, FDV $295.239.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 18/10/2026 01:04 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0003008 |
| Liquidez | $58.008 |
| MCap | $293.807 |
| Volumen 24 h | $11.789.936 |
| Cambio 24 h | +603% |
| Cambio m5 / h1 | -30,4% / +37,6% |
| Volumen m5 / h1 | $44.772 / $158.520 |
| Trades m5 (compras / ventas) | 109 / 108 |
| Edad del par | 22,3 h |
| Score del feed (WS) | 80 |

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

Desglose no reproducible desde los motivos registrados (suma 100 vs score 100; motivos sin regla: Anticipación (lib_early_signals early-0.2): +2 — volume_acceleration: vol 5 min ×3.4 la tasa horaria → +2.27): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-18T01:04:47+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $100K, Volumen masivo, Volumen en aceleración (5m/1h > 25%), Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=19.7% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 66 de 39.095 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 18/10/2026 01:04 UTC, hasta 20/10/2026 01:04 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -30,4% · h1 +37,6% · h24 +603% · volumen m5/h1 0,28 · edad del par 22,3 h.
- **Precio de entrada** (alerta): $0,0003008.
- **Consulta 18/10/2026 01:33 UTC:** $0,0003023 (+0,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump_2026-10-18_010447.json` · blob `b6902c8ca4d606a3ae16638e66da388f5338d6b9` · commit `8c696c8` (2026-10-18T01:25:51Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-18_005837.json` · blob `08b693d2ebd4c0f982026f740b798c3314f3991c` · commit `8c696c8` (2026-10-18T01:25:51Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-18_010447`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump · registro · 18/10/2026 01:04 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump · HTTP 200 · 18/10/2026 01:33 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump/report · HTTP 200 · 18/10/2026 01:33 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump · HTTP 200 · 18/10/2026 01:33 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/ABqXgS5c78P8Nix49kqsBTNQjAmMAhCBH2mvjq1zqQZ2/ohlcv/hour?limit=1000 · HTTP 200 · 18/10/2026 01:33 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump · HTTP 404 · 18/10/2026 01:33 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ETERNIAUSDT · HTTP 400 · 18/10/2026 01:33 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ETERNIA-USD · HTTP 404 · 18/10/2026 01:33 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $58.521 vs $58.393 → 0,22%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0003023 vs $0,0003019 → 0,13%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump_2026-10-18_010447.json',encoding='utf-8'));d=d.get('CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump',d);p=mock.patch('time.time',return_value=1792285487);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 18/10/2026 01:33 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `d898736d505e603d…`
