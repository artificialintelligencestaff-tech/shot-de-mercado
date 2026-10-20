# Macrohard xAI (MxAI) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,002285 · liquidez $128.300 · mcap $2.283.742 (al detectar)  
Detectado el 20/10/2026 04:26 UTC por: MCap > $1M, Volumen decente, Volumen en aceleración (5m/1h > 25%) (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 22/10/2026 04:26 UTC (< 48 h) · vigente: quedan 47,2 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir MxAI

Estudio de cómo se adquiere MxAI, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 20/10/2026 05:12 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 20/10/2026 04:26 UTC | pumpswap `6uPz2y2…PwJ8` | $128.300 | 5% | 0,156% | 1,559% | 15,588% | $641 | $1.924 |
| consulta 20/10/2026 05:12 UTC | pumpswap `6uPz2y2…PwJ8` | $128.539 | 5% | 0,156% | 1,556% | 15,559% | $643 | $1.928 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump`
5. Configurar el slippage: 5% (liquidez $128.539, consulta 20/10/2026 05:12 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump) y el par en DexScreener (https://dexscreener.com/solana/6uPz2y2ccmVubdXUjhzwFreTnSLq5Fhnt92rWyyfPwJ8); mint authority / freeze authority: revocada / revocada · holders 3.992 · top-10 3,13% (consulta 20/10/2026 05:12 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump
- Par en DexScreener: https://dexscreener.com/solana/6uPz2y2ccmVubdXUjhzwFreTnSLq5Fhnt92rWyyfPwJ8
- Página del lanzamiento (pump.fun): https://pump.fun/coin/sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.992 · top-10 3,13% (consulta 20/10/2026 05:12 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Macrohard xAI / MxAI | registro de la detección (pumpportal) |
| Mint / contrato | `sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6uPz2y2ccmVubdXUjhzwFreTnSLq5Fhnt92rWyyfPwJ8` | DexScreener, al detectar (2 par(es) en la consulta 20/10/2026 05:12 UTC) |
| Deployer | `AKCbEt5tzQtPJThLiTnejtvCehzvKmLYwC85fSrwpSKh` | PumpPortal (evento create), al detectar |
| Par creado | 20/10/2026 03:25 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 61,4 min / 61,4 min / 107,2 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 20/10/2026 05:12 UTC |
| Holders / top-10 | 3.992 / 3,13% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 20/10/2026 05:12 UTC |
| Holders efectivos del top-10 | 1,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 20/10/2026 05:12 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 20/10/2026 05:12 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6uPz2y2ccmVubdXUjhzwFreTnSLq5Fhnt92rWyyfPwJ8 · Solscan: https://solscan.io/token/sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump · pump.fun: https://pump.fun/coin/sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump · web / Telegram / X: no publicados en DexScreener | consulta 20/10/2026 05:12 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 20/10/2026 05:12 UTC)
- **Historia:**
  - Par creado el 20/10/2026 03:25 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 20/10/2026 04:26 UTC, con el par a 61,4 min de creado: precio $0,002285, mcap $2.283.742, liquidez $128.300.
  - Velas de 1 h de GeckoTerminal (3, desde 20/10/2026 03:00 UTC): apertura $0,0002976 · máximo $0,002307 (20/10/2026 05:00 UTC) · mínimo $0,00004358 (20/10/2026 03:00 UTC) · último cierre $0,002282.
  - En la consulta 20/10/2026 05:12 UTC: precio $0,002299, liquidez $128.539, FDV $2.297.898.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 20/10/2026 04:26 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,002285 |
| Liquidez | $128.300 |
| MCap | $2.283.742 |
| Volumen 24 h | $59.640 |
| Cambio 24 h | +5.140% |
| Cambio m5 / h1 | +5,0% / +11,6% |
| Volumen m5 / h1 | $2.049 / $7.644 |
| Trades m5 (compras / ventas) | 171 / 69 |
| Edad del par | 61,4 min |
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

Desglose no reproducible desde los motivos registrados (suma 100 vs score 100; motivos sin regla: Anticipación (lib_early_signals early-0.2): +2 — volume_acceleration: vol 5 min ×3.2 la tasa horaria → +2.06; liquidity_inflow: liquidez +3% en 8 min → +0.21): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-20T04:26:32+00:00, sin estado previo): **100** · motivos: MCap > $1M, Volumen decente, Volumen en aceleración (5m/1h > 25%), Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=5.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 68 de 41.637 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 20/10/2026 04:26 UTC, hasta 22/10/2026 04:26 UTC · vigente: quedan 47,2 h.
- **Aceleración al detectar:** cambio m5 +5,0% · h1 +11,6% · h24 +5.140% · volumen m5/h1 0,27 · edad del par 61,4 min.
- **Precio de entrada** (alerta): $0,002285.
- **Consulta 20/10/2026 05:12 UTC:** $0,002299 (+0,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump_2026-10-20_042632.json` · blob `ea0ea185091512878e4ce7f9204c2f73bbfb999d` · commit `c9f9c71` (2026-10-20T05:05:37Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-20_042632`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump · registro · 20/10/2026 04:26 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump · HTTP 200 · 20/10/2026 05:12 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump/report · HTTP 200 · 20/10/2026 05:12 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump · HTTP 200 · 20/10/2026 05:12 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6uPz2y2ccmVubdXUjhzwFreTnSLq5Fhnt92rWyyfPwJ8/ohlcv/hour?limit=1000 · HTTP 200 · 20/10/2026 05:12 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump · HTTP 404 · 20/10/2026 05:12 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MXAIUSDT · HTTP 400 · 20/10/2026 05:12 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MXAI-USD · HTTP 404 · 20/10/2026 05:12 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $128.539 vs $128.159 → 0,30%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002299 vs $0,002282 → 0,72%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump_2026-10-20_042632.json',encoding='utf-8'));d=d.get('sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump',d);p=mock.patch('time.time',return_value=1792470392);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint sXjgpebmmGWgo5zNTVk2xEW9djiUoSQiWMEmhwzpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 20/10/2026 05:12 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `78d147ee8bfafafe…`
