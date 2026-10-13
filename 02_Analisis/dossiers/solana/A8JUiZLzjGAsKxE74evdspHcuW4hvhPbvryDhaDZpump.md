# Token Battles (FIGHT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0002141 · liquidez $40.728 · mcap $186.898 (al detectar)  
Detectado el 13/10/2026 01:20 UTC por: WS score muy alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 15/10/2026 01:20 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir FIGHT

Estudio de cómo se adquiere FIGHT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 13/10/2026 01:42 UTC; CoinGecko sin ficha para este contrato). Coinbase tiene un par FIGHT-USD, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza.

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 13/10/2026 01:20 UTC | pumpswap `BoW9h5G…DRLZ` | $40.728 | 10% | 0,491% | 4,911% | 49,106% | $204 | $611 |
| consulta 13/10/2026 01:42 UTC | pumpswap `BoW9h5G…DRLZ` | $42.361 | 10% | 0,472% | 4,721% | 47,214% | $212 | $635 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump`
5. Configurar el slippage: 10% (liquidez $42.361, consulta 13/10/2026 01:42 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump) y el par en DexScreener (https://dexscreener.com/solana/BoW9h5GBqdNR55fKE3VHdzNgPLANzmYKY1eiqmx1DRLZ); mint authority / freeze authority: revocada / revocada · holders 6.282 · top-10 21,39% (consulta 13/10/2026 01:42 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump
- Par en DexScreener: https://dexscreener.com/solana/BoW9h5GBqdNR55fKE3VHdzNgPLANzmYKY1eiqmx1DRLZ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 6.282 · top-10 21,39% (consulta 13/10/2026 01:42 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Token Battles / FIGHT | registro de la detección (trending) |
| Mint / contrato | `A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BoW9h5GBqdNR55fKE3VHdzNgPLANzmYKY1eiqmx1DRLZ` | DexScreener, al detectar (2 par(es) en la consulta 13/10/2026 01:42 UTC) |
| Deployer | `BKfaa1iHxUA4Y7ZBWACEVTJEewPukdqfL7n84TdxirMT` | RugCheck `creator` |
| Par creado | 12/10/2026 01:51 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 23,5 h / 23,5 h / 23,9 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 13/10/2026 01:42 UTC |
| Holders / top-10 | 6.282 / 21,39% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 13/10/2026 01:42 UTC |
| Holders efectivos del top-10 | 3,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 13/10/2026 01:42 UTC |
| Etiquetas de RugCheck | «Copycat token» | RugCheck `risks[].name` (texto de la fuente), consulta 13/10/2026 01:42 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BoW9h5GBqdNR55fKE3VHdzNgPLANzmYKY1eiqmx1DRLZ · Solscan: https://solscan.io/token/A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump · pump.fun: https://pump.fun/coin/A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump · web: https://tokenbattles.fun/ · twitter: https://x.com/tokenbattlesfun | consulta 13/10/2026 01:42 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 13/10/2026 01:42 UTC)
- **Historia:**
  - Par creado el 12/10/2026 01:51 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 13/10/2026 01:20 UTC, con el par a 23,5 h de creado: precio $0,0002141, mcap $186.898, liquidez $40.728.
  - Velas de 1 h de GeckoTerminal (25, desde 12/10/2026 01:00 UTC): apertura $0,00004613 · máximo $0,0004822 (12/10/2026 23:00 UTC) · mínimo $0,00004560 (12/10/2026 01:00 UTC) · último cierre $0,0002299.
  - En la consulta 13/10/2026 01:42 UTC: precio $0,0002288, liquidez $42.361, FDV $199.732.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 13/10/2026 01:20 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0002141 |
| Liquidez | $40.728 |
| MCap | $186.898 |
| Volumen 24 h | $1.297.615 |
| Cambio 24 h | +368% |
| Cambio m5 / h1 | +3,8% / +2,8% |
| Volumen m5 / h1 | $12.366 / $55.994 |
| Trades m5 (compras / ventas) | 183 / 103 |
| Edad del par | 23,5 h |
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

Desglose no reproducible desde los motivos registrados (suma 100 vs score 100; motivos sin regla: Anticipación (lib_early_signals early-0.2): +2 — volume_acceleration: vol 5 min ×2.7 la tasa horaria → +1.38; buy_pressure_shift: compras 64% en 5 min vs 62% en 1 h → +0.25; quiet_accumulation: precio quieto (m5 +3.8%) con vol ×2.7 y compras 64% → +0.79): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-13T01:20:27+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 51 de 32.400 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 13/10/2026 01:20 UTC, hasta 15/10/2026 01:20 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +3,8% · h1 +2,8% · h24 +368% · volumen m5/h1 0,22 · edad del par 23,5 h.
- **Precio de entrada** (alerta): $0,0002141.
- **Consulta 13/10/2026 01:42 UTC:** $0,0002288 (+6,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump_2026-10-13_012027.json` · blob `449b6d1595a896a44813d7d7fe9a53825a135ccc` · commit `1cf7aa7` (2026-10-13T01:35:42Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-13_011429.json` · blob `843592758b5be6b94778751b7b88b44e57996273` · commit `1cf7aa7` (2026-10-13T01:35:42Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-13_012027`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump · registro · 13/10/2026 01:20 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump · HTTP 200 · 13/10/2026 01:42 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump/report · HTTP 200 · 13/10/2026 01:42 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump · HTTP 200 · 13/10/2026 01:42 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BoW9h5GBqdNR55fKE3VHdzNgPLANzmYKY1eiqmx1DRLZ/ohlcv/hour?limit=1000 · HTTP 200 · 13/10/2026 01:42 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump · HTTP 404 · 13/10/2026 01:42 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=FIGHTUSDT · HTTP 400 · 13/10/2026 01:42 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/FIGHT-USD · HTTP 200 · 13/10/2026 01:42 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $42.361 vs $42.672 → 0,73%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0002288 vs $0,0002299 → 0,50%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump_2026-10-13_012027.json',encoding='utf-8'));d=d.get('A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump',d);p=mock.patch('time.time',return_value=1791854427);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 13/10/2026 01:42 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `2b469ce90db0ecca…`
