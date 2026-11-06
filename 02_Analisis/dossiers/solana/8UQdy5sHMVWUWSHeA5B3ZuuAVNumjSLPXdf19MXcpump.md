# COGE COIN (COGE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003324 · liquidez $150.832 · mcap $3.310.035 (al detectar)  
Detectado el 06/11/2026 10:19 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 08/11/2026 10:19 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir COGE

Estudio de cómo se adquiere COGE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/11/2026 10:19 UTC; CoinGecko sin pares de este contrato en esos exchanges).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/11/2026 10:19 UTC | pumpswap `8GjMy6i…sLqe` | $150.832 | 5% | 0,133% | 1,326% | 13,260% | $754 | $2.262 |
| consulta 06/11/2026 10:19 UTC | pumpswap `8GjMy6i…sLqe` | $150.598 | 5% | 0,133% | 1,328% | 13,280% | $753 | $2.259 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump`
5. Configurar el slippage: 5% (liquidez $150.598, consulta 06/11/2026 10:19 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump) y el par en DexScreener (https://dexscreener.com/solana/8GjMy6ipYsXfMWwRPu9C7ATssorjg6AL88d9xtTZsLqe); mint authority / freeze authority: revocada / revocada · holders 2.450 · top-10 10,08% (consulta 06/11/2026 10:19 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump
- Par en DexScreener: https://dexscreener.com/solana/8GjMy6ipYsXfMWwRPu9C7ATssorjg6AL88d9xtTZsLqe
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.450 · top-10 10,08% (consulta 06/11/2026 10:19 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | COGE COIN / COGE | registro de la detección (trending) |
| Mint / contrato | `8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `8GjMy6ipYsXfMWwRPu9C7ATssorjg6AL88d9xtTZsLqe` | DexScreener, al detectar (3 par(es) en la consulta 06/11/2026 10:19 UTC) |
| Deployer | `4QGjrEmADSUaNgusuERgQCeRFTTc5SWW5ssZfb5e9sZi` | RugCheck `creator` |
| Par creado | 05/11/2026 19:48 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 14,5 h / 14,5 h / 14,5 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/11/2026 10:19 UTC |
| Holders / top-10 | 2.450 / 10,08% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/11/2026 10:19 UTC |
| Holders efectivos del top-10 | 8,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; orca 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/11/2026 10:19 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 06/11/2026 10:19 UTC |
| Links | DexScreener: https://dexscreener.com/solana/8GjMy6ipYsXfMWwRPu9C7ATssorjg6AL88d9xtTZsLqe · Solscan: https://solscan.io/token/8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump · pump.fun: https://pump.fun/coin/8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump · web: https://cogecoin.world · twitter: https://x.com/COGECOINMeme | consulta 06/11/2026 10:19 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** CoinGecko: Solana Ecosystem, Pump.fun Ecosystem
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/11/2026 10:19 UTC)
- **Historia:**
  - Par creado el 05/11/2026 19:48 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/11/2026 10:19 UTC, con el par a 14,5 h de creado: precio $0,003324, mcap $3.310.035, liquidez $150.832.
  - Velas de 1 h de GeckoTerminal (16, desde 05/11/2026 19:00 UTC): apertura $0,0002544 · máximo $0,003507 (06/11/2026 05:00 UTC) · mínimo $0,00004927 (05/11/2026 19:00 UTC) · último cierre $0,003322.
  - En la consulta 06/11/2026 10:19 UTC: precio $0,003313, liquidez $150.598, FDV $3.298.783.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/11/2026 10:19 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003324 |
| Liquidez | $150.832 |
| MCap | $3.310.035 |
| Volumen 24 h | $1.879.918 |
| Cambio 24 h | +6.608% |
| Cambio m5 / h1 | +4,5% / +16,6% |
| Volumen m5 / h1 | $4.621 / $52.148 |
| Trades m5 (compras / ventas) | 341 / 227 |
| Edad del par | 14,5 h |
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
| Score del feed | score WS × 0,3 | WS 71 × 0,3 | +21,4 |
| MCap | ≥ $1M | $3.310.035 | +25 |
| Volumen 24 h | ≥ $1M | $1.879.918 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 60% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +4,5% · h1 +16,6% | +20 |
| Volumen m5 | > $1K (par maduro) | $4.621 | +10 |
| Liquidez | ≥ $100K | $150.832 | +15 |
| Cambio 24 h | ≥ +50% | +6.608% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +6.608% · liq/mcap 4,6% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-06T10:19:10+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 93 de 46.766 tokens analizados (0,20%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/11/2026 10:19 UTC, hasta 08/11/2026 10:19 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +4,5% · h1 +16,6% · h24 +6.608% · volumen m5/h1 0,09 · edad del par 14,5 h.
- **Precio de entrada** (alerta): $0,003324.
- **Consulta 06/11/2026 10:19 UTC:** $0,003313 (-0,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump_2026-11-06_101929.json` · blob `559c05d4f329ba3be5d3a068e5d152b40cdb6f2c` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-06_101407.json` · blob `96e1c474c619e4fcac8410ed74c2309be1420e6d` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-06_101929`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump · registro · 06/11/2026 10:19 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump · HTTP 200 · 06/11/2026 10:19 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump/report · HTTP 200 · 06/11/2026 10:19 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump · HTTP 200 · 06/11/2026 10:19 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/8GjMy6ipYsXfMWwRPu9C7ATssorjg6AL88d9xtTZsLqe/ohlcv/hour?limit=1000 · HTTP 200 · 06/11/2026 10:19 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump · HTTP 200 · 06/11/2026 10:19 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=COGEUSDT · HTTP 400 · 06/11/2026 10:19 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/COGE-USD · HTTP 404 · 06/11/2026 10:19 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $150.598 vs $151.173 → 0,38%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003313 vs $0,003322 → 0,28%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump_2026-11-06_101929.json',encoding='utf-8'));d=d.get('8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump',d);p=mock.patch('time.time',return_value=1793960350);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/11/2026 10:19 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `f250065bcf2f2a32…`
