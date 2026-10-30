# Hyper-Chan (HYPERCHAN) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0009112 · liquidez $83.836 · mcap $907.144 (al detectar)  
Detectado el 30/10/2026 21:26 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 01/11/2026 21:27 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HYPERCHAN

Estudio de cómo se adquiere HYPERCHAN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 30/10/2026 21:27 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 30/10/2026 21:26 UTC | pumpswap `5mxPpt9…KyVY` | $83.836 | 5% | 0,239% | 2,386% | 23,856% | $419 | $1.258 |
| consulta 30/10/2026 21:27 UTC | pumpswap `5mxPpt9…KyVY` | $83.735 | 5% | 0,239% | 2,388% | 23,885% | $419 | $1.256 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump`
5. Configurar el slippage: 5% (liquidez $83.735, consulta 30/10/2026 21:27 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump) y el par en DexScreener (https://dexscreener.com/solana/5mxPpt9pFtDyK624QQ5Lxbw1HfGr4YCqeaFUdKMtKyVY); mint authority / freeze authority: revocada / revocada · holders 8.143 · top-10 5,93% (consulta 30/10/2026 21:27 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump
- Par en DexScreener: https://dexscreener.com/solana/5mxPpt9pFtDyK624QQ5Lxbw1HfGr4YCqeaFUdKMtKyVY
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 8.143 · top-10 5,93% (consulta 30/10/2026 21:27 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Hyper-Chan / HYPERCHAN | registro de la detección (trending) |
| Mint / contrato | `3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `5mxPpt9pFtDyK624QQ5Lxbw1HfGr4YCqeaFUdKMtKyVY` | DexScreener, al detectar (5 par(es) en la consulta 30/10/2026 21:27 UTC) |
| Deployer | `CGyCuvEBcTqFsraAzPefFVxGRtcFdr9eq9pscL4NNHga` | RugCheck `creator` |
| Par creado | 30/10/2026 03:24 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 18,0 h / 18,0 h / 18,1 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 30/10/2026 21:27 UTC |
| Holders / top-10 | 8.143 / 5,93% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 30/10/2026 21:27 UTC |
| Holders efectivos del top-10 | 1,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 30/10/2026 21:27 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 30/10/2026 21:27 UTC |
| Links | DexScreener: https://dexscreener.com/solana/5mxPpt9pFtDyK624QQ5Lxbw1HfGr4YCqeaFUdKMtKyVY · Solscan: https://solscan.io/token/3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump · pump.fun: https://pump.fun/coin/3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump · web: http://hyperchan.lol/ · twitter: https://x.com/hyperchanonx · telegram: https://t.me/hyperchan_tg | consulta 30/10/2026 21:27 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 30/10/2026 21:27 UTC)
- **Historia:**
  - Par creado el 30/10/2026 03:24 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 30/10/2026 21:26 UTC, con el par a 18,0 h de creado: precio $0,0009112, mcap $907.144, liquidez $83.836.
  - Velas de 1 h de GeckoTerminal (19, desde 30/10/2026 03:00 UTC): apertura $0,0003310 · máximo $0,002993 (30/10/2026 19:00 UTC) · mínimo $0,00004767 (30/10/2026 03:00 UTC) · último cierre $0,0009174.
  - En la consulta 30/10/2026 21:27 UTC: precio $0,0009091, liquidez $83.735, FDV $904.990.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 30/10/2026 21:26 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0009112 |
| Liquidez | $83.836 |
| MCap | $907.144 |
| Volumen 24 h | $4.054.154 |
| Cambio 24 h | +1.801% |
| Cambio m5 / h1 | +3,5% / +3,2% |
| Volumen m5 / h1 | $5.199 / $96.834 |
| Trades m5 (compras / ventas) | 638 / 391 |
| Edad del par | 18,0 h |
| Score del feed (WS) | 71 |

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
| Score del feed | score WS × 0,3 | WS 71 × 0,3 | +21,3 |
| MCap | ≥ $100K | $907.144 | +15 |
| Volumen 24 h | ≥ $1M | $4.054.154 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 62% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +3,5% · h1 +3,2% | +20 |
| Volumen m5 | > $1K (par maduro) | $5.199 | +10 |
| Liquidez | ≥ $50K | $83.836 | +10 |
| Cambio 24 h | ≥ +50% | +1.801% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.801% · liq/mcap 9,2% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-30T21:26:51+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=9.2% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 83 de 46.328 tokens analizados (0,18%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 30/10/2026 21:27 UTC, hasta 01/11/2026 21:27 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +3,5% · h1 +3,2% · h24 +1.801% · volumen m5/h1 0,05 · edad del par 18,0 h.
- **Precio de entrada** (alerta): $0,0009112.
- **Consulta 30/10/2026 21:27 UTC:** $0,0009091 (-0,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump_2026-10-30_212702.json` · blob `99d402e3220120b37d73af64cab94c8820f22cec` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-30_212148.json` · blob `7448321b025bc43bc08751dcc86a9d312cbf6038` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-30_212702`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump · registro · 30/10/2026 21:26 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump · HTTP 200 · 30/10/2026 21:27 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump/report · HTTP 200 · 30/10/2026 21:27 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump · HTTP 200 · 30/10/2026 21:27 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/5mxPpt9pFtDyK624QQ5Lxbw1HfGr4YCqeaFUdKMtKyVY/ohlcv/hour?limit=1000 · HTTP 200 · 30/10/2026 21:27 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump · HTTP 404 · 30/10/2026 21:27 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HYPERCHANUSDT · HTTP 400 · 30/10/2026 21:27 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HYPERCHAN-USD · HTTP 404 · 30/10/2026 21:27 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $83.735 vs $83.243 → 0,59%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0009091 vs $0,0009174 → 0,91%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump_2026-10-30_212702.json',encoding='utf-8'));d=d.get('3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump',d);p=mock.patch('time.time',return_value=1793395611);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 30/10/2026 21:27 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `5d996865866c9d83…`
