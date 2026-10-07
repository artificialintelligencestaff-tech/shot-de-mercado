# WSOS (WSOS) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,2147 · liquidez $1.328.135 · mcap $214.788.763 (al detectar)  
Detectado el 07/10/2026 16:42 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 09/10/2026 16:42 UTC (< 48 h) · vigente: quedan 47,3 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir WSOS

Estudio de cómo se adquiere WSOS, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/10/2026 17:22 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/10/2026 16:42 UTC | pumpswap `EVWTNnE…q84S` | $1.328.135 | 1% | 0,015% | 0,151% | 1,506% | $6.641 | $19.922 |
| consulta 07/10/2026 17:22 UTC | pumpswap `EVWTNnE…q84S` | $1.338.163 | 1% | 0,015% | 0,149% | 1,495% | $6.691 | $20.072 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump`
5. Configurar el slippage: 1% (liquidez $1.338.163, consulta 07/10/2026 17:22 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump) y el par en DexScreener (https://dexscreener.com/solana/EVWTNnELZNFTv26LEYT1Ne9AStcA2wm9SLovwCcQq84S); mint authority / freeze authority: revocada / revocada · holders 2.166 · top-10 0,74% (consulta 07/10/2026 17:22 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump
- Par en DexScreener: https://dexscreener.com/solana/EVWTNnELZNFTv26LEYT1Ne9AStcA2wm9SLovwCcQq84S
- Página del lanzamiento (pump.fun): https://pump.fun/coin/qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.166 · top-10 0,74% (consulta 07/10/2026 17:22 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | WSOS / WSOS | registro de la detección (trending) |
| Mint / contrato | `qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `EVWTNnELZNFTv26LEYT1Ne9AStcA2wm9SLovwCcQq84S` | DexScreener, al detectar (2 par(es) en la consulta 07/10/2026 17:22 UTC) |
| Deployer | `EftffTwbWBvDAoYNVM6rCU8Ev91wML4V2JmZ2nVUzG2T` | RugCheck `creator` |
| Par creado | 07/10/2026 13:45 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 3,0 h / 3,0 h / 3,6 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/10/2026 17:22 UTC |
| Holders / top-10 | 2.166 / 0,74% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/10/2026 17:22 UTC |
| Holders efectivos del top-10 | 4,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/10/2026 17:22 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 07/10/2026 17:22 UTC |
| Links | DexScreener: https://dexscreener.com/solana/EVWTNnELZNFTv26LEYT1Ne9AStcA2wm9SLovwCcQq84S · Solscan: https://solscan.io/token/qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump · pump.fun: https://pump.fun/coin/qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump · web / Telegram / X: no publicados en DexScreener | consulta 07/10/2026 17:22 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/10/2026 17:22 UTC)
- **Historia:**
  - Par creado el 07/10/2026 13:45 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/10/2026 16:42 UTC, con el par a 3,0 h de creado: precio $0,2147, mcap $214.788.763, liquidez $1.328.135.
  - Velas de 1 h de GeckoTerminal (5, desde 07/10/2026 13:00 UTC): apertura $0,002899 · máximo $0,2180 (07/10/2026 17:00 UTC) · mínimo $0,00004811 (07/10/2026 13:00 UTC) · último cierre $0,2178.
  - En la consulta 07/10/2026 17:22 UTC: precio $0,2180, liquidez $1.338.163, FDV $218.016.540.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/10/2026 16:42 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,2147 |
| Liquidez | $1.328.135 |
| MCap | $214.788.763 |
| Volumen 24 h | $655.672 |
| Cambio 24 h | +446.398% |
| Cambio m5 / h1 | -0,0% / +7,5% |
| Volumen m5 / h1 | $852 / $25.150 |
| Trades m5 (compras / ventas) | 170 / 4 |
| Edad del par | 3,0 h |
| Score del feed (WS) | 99 |

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

Desglose no reproducible desde los motivos registrados (suma 82 vs score 100; motivos sin regla: score de detección 100 (script_82, hace 1 min) > re-score 82: vale el de detección (paridad con script_97)): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-07T16:42:47+00:00, sin estado previo): **82** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 31 de 19.193 tokens analizados (0,16%) quedan ≥ 56. Con score 82, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/10/2026 16:42 UTC, hasta 09/10/2026 16:42 UTC · vigente: quedan 47,3 h.
- **Aceleración al detectar:** cambio m5 -0,0% · h1 +7,5% · h24 +446.398% · volumen m5/h1 0,03 · edad del par 3,0 h.
- **Precio de entrada** (alerta): $0,2147.
- **Consulta 07/10/2026 17:22 UTC:** $0,2180 (+1,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump_2026-10-07_164247.json` · blob `d0d93ee2d31c19f38be5ca0e83f3bf7bd65c4df5` · commit `53fceb9` (2026-10-07T17:14:48Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-07_163640.json` · blob `6a84ba29159f233a67a2de42650ec0ee1aeb79b6` · commit `53fceb9` (2026-10-07T17:14:48Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-07_164247`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump · registro · 07/10/2026 16:42 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump · HTTP 200 · 07/10/2026 17:22 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump/report · HTTP 200 · 07/10/2026 17:22 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump · HTTP 200 · 07/10/2026 17:22 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/EVWTNnELZNFTv26LEYT1Ne9AStcA2wm9SLovwCcQq84S/ohlcv/hour?limit=1000 · HTTP 200 · 07/10/2026 17:22 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump · HTTP 404 · 07/10/2026 17:22 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=WSOSUSDT · HTTP 400 · 07/10/2026 17:22 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/WSOS-USD · HTTP 404 · 07/10/2026 17:22 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.338.163 vs $1.333.296 → 0,36%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,2180 vs $0,2178 → 0,09%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump_2026-10-07_164247.json',encoding='utf-8'));d=d.get('qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump',d);p=mock.patch('time.time',return_value=1791391367);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint qgheoairGa7UYsMtFhSy2XaWFY5Six1AxULHcCMpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/10/2026 17:22 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `83fca0ce0d61e9a8…`
