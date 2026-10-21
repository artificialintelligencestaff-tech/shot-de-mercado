# XTO (XTO) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1946 · liquidez $1.216.255 · mcap $194.634.989 (al detectar)  
Detectado el 21/10/2026 15:18 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 96, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 23/10/2026 15:18 UTC (< 48 h) · vigente: quedan 46,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir XTO

Estudio de cómo se adquiere XTO, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 21/10/2026 16:30 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 21/10/2026 15:18 UTC | pumpswap `61tJRz9…rhhG` | $1.216.255 | 1% | 0,016% | 0,164% | 1,644% | $6.081 | $18.244 |
| consulta 21/10/2026 16:29 UTC | pumpswap `61tJRz9…rhhG` | $1.228.690 | 1% | 0,016% | 0,163% | 1,628% | $6.143 | $18.430 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump`
5. Configurar el slippage: 1% (liquidez $1.228.690, consulta 21/10/2026 16:29 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump) y el par en DexScreener (https://dexscreener.com/solana/61tJRz9remS454LA4HeckNbAixXENFAxt9KL8GGzrhhG); mint authority / freeze authority: revocada / revocada · holders 2.267 · top-10 1,18% (consulta 21/10/2026 16:29 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump
- Par en DexScreener: https://dexscreener.com/solana/61tJRz9remS454LA4HeckNbAixXENFAxt9KL8GGzrhhG
- Página del lanzamiento (pump.fun): https://pump.fun/coin/DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.267 · top-10 1,18% (consulta 21/10/2026 16:29 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | XTO / XTO | registro de la detección (trending) |
| Mint / contrato | `DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `61tJRz9remS454LA4HeckNbAixXENFAxt9KL8GGzrhhG` | DexScreener, al detectar (2 par(es) en la consulta 21/10/2026 16:29 UTC) |
| Deployer | `35eDfqTiCh3pe3gJcr3P49QxwVwpgb1HTaQ9cUU26FLW` | RugCheck `creator` |
| Par creado | 20/10/2026 23:07 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 16,2 h / 16,2 h / 17,4 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 21/10/2026 16:29 UTC |
| Holders / top-10 | 2.267 / 1,18% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 21/10/2026 16:29 UTC |
| Holders efectivos del top-10 | 4,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 21/10/2026 16:29 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 21/10/2026 16:29 UTC |
| Links | DexScreener: https://dexscreener.com/solana/61tJRz9remS454LA4HeckNbAixXENFAxt9KL8GGzrhhG · Solscan: https://solscan.io/token/DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump · pump.fun: https://pump.fun/coin/DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump · web / Telegram / X: no publicados en DexScreener | consulta 21/10/2026 16:29 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 21/10/2026 16:29 UTC)
- **Historia:**
  - Par creado el 20/10/2026 23:07 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 21/10/2026 15:18 UTC, con el par a 16,2 h de creado: precio $0,1946, mcap $194.634.989, liquidez $1.216.255.
  - Velas de 1 h de GeckoTerminal (18, desde 20/10/2026 23:00 UTC): apertura $0,00004427 · máximo $0,1980 (21/10/2026 16:00 UTC) · mínimo $0,00004427 (20/10/2026 23:00 UTC) · último cierre $0,1976.
  - En la consulta 21/10/2026 16:29 UTC: precio $0,1979, liquidez $1.228.690, FDV $197.913.722.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 21/10/2026 15:18 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1946 |
| Liquidez | $1.216.255 |
| MCap | $194.634.989 |
| Volumen 24 h | $964.793 |
| Cambio 24 h | +439.483% |
| Cambio m5 / h1 | +0,2% / +2,5% |
| Volumen m5 / h1 | $1.848 / $25.666 |
| Trades m5 (compras / ventas) | 110 / 9 |
| Edad del par | 16,2 h |
| Score del feed (WS) | 90 |

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

Desglose reconstruido desde los motivos registrados; suma 96 = score registrado 96 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 90 × 0,3 | +27,0 |
| MCap | ≥ $1M | $194.634.989 | +25 |
| Volumen 24 h | ≥ $100K | $964.793 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 92% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,2% · h1 +2,5% | +20 |
| Volumen m5 | > $1K (par maduro) | $1.848 | +10 |
| Liquidez | ≥ $100K | $1.216.255 | +15 |
| Cambio 24 h | ≥ +50% | +439.483% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +439.483% · liq/mcap 0,6% | -50 |
| **Total** | recortado a 0–100 |  | **96** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-21T15:18:39+00:00, sin estado previo): **96** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 74 de 43.106 tokens analizados (0,17%) quedan ≥ 56. Con score 96, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 21/10/2026 15:18 UTC, hasta 23/10/2026 15:18 UTC · vigente: quedan 46,8 h.
- **Aceleración al detectar:** cambio m5 +0,2% · h1 +2,5% · h24 +439.483% · volumen m5/h1 0,07 · edad del par 16,2 h.
- **Precio de entrada** (alerta): $0,1946.
- **Consulta 21/10/2026 16:29 UTC:** $0,1979 (+1,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump_2026-10-21_151839.json` · blob `b8c3ca7aa84c8669fd7619027cc8fb50b72ef48f` · commit `d70e871` (2026-10-21T16:19:37Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-21_151229.json` · blob `18c44c413fb6c112cf7b5bdad30287f6d66c0548` · commit `d70e871` (2026-10-21T16:19:37Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-21_151839`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump · registro · 21/10/2026 15:18 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump · HTTP 200 · 21/10/2026 16:29 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump/report · HTTP 200 · 21/10/2026 16:29 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump · HTTP 200 · 21/10/2026 16:29 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/61tJRz9remS454LA4HeckNbAixXENFAxt9KL8GGzrhhG/ohlcv/hour?limit=1000 · HTTP 200 · 21/10/2026 16:29 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump · HTTP 404 · 21/10/2026 16:29 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=XTOUSDT · HTTP 400 · 21/10/2026 16:30 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/XTO-USD · HTTP 404 · 21/10/2026 16:30 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.228.690 vs $1.229.310 → 0,05%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1979 vs $0,1976 → 0,15%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump_2026-10-21_151839.json',encoding='utf-8'));d=d.get('DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump',d);p=mock.patch('time.time',return_value=1792595919);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint DWbsAe8brNfiSzP1wXYAH6tWdMBJpx6cfkMWv9K1pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 21/10/2026 16:30 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `14896c9921ff65c8…`
