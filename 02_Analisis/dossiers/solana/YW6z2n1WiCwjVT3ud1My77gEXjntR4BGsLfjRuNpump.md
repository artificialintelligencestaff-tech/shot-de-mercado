# ARROW (ARROW) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003371 · liquidez $167.323 · mcap $3.368.804 (al detectar)  
Detectado el 06/10/2026 16:33 UTC por: MCap > $1M, Volumen decente, Buy pressure >55% (score 88, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 08/10/2026 16:33 UTC (< 48 h) · vigente: quedan 47,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ARROW

Estudio de cómo se adquiere ARROW, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 16:41 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 16:33 UTC | pumpswap `77YL5my…ueQh` | $167.323 | 5% | 0,120% | 1,195% | 11,953% | $837 | $2.510 |
| consulta 06/10/2026 16:40 UTC | pumpswap `77YL5my…ueQh` | $166.607 | 5% | 0,120% | 1,200% | 12,004% | $833 | $2.499 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump`
5. Configurar el slippage: 5% (liquidez $166.607, consulta 06/10/2026 16:40 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump) y el par en DexScreener (https://dexscreener.com/solana/77YL5myqdVRwQC1n8XM1g4pANagHtw9wxCDbwhsKueQh); mint authority / freeze authority: revocada / revocada · holders 4.044 · top-10 11,28% (consulta 06/10/2026 16:40 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump
- Par en DexScreener: https://dexscreener.com/solana/77YL5myqdVRwQC1n8XM1g4pANagHtw9wxCDbwhsKueQh
- Página del lanzamiento (pump.fun): https://pump.fun/coin/YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.044 · top-10 11,28% (consulta 06/10/2026 16:40 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | ARROW / ARROW | registro de la detección (pumpportal) |
| Mint / contrato | `YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `77YL5myqdVRwQC1n8XM1g4pANagHtw9wxCDbwhsKueQh` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 16:40 UTC) |
| Deployer | `2Rwue8sBkX6jR3bNUoZjjfDvsbjwcVsytJ2BSRAWWPU4` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 15:33 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,1 min / 60,1 min / 67,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 16:40 UTC |
| Holders / top-10 | 4.044 / 11,28% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 16:40 UTC |
| Holders efectivos del top-10 | 8,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 16:40 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 16:40 UTC |
| Links | DexScreener: https://dexscreener.com/solana/77YL5myqdVRwQC1n8XM1g4pANagHtw9wxCDbwhsKueQh · Solscan: https://solscan.io/token/YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump · pump.fun: https://pump.fun/coin/YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump · web / Telegram / X: no publicados en DexScreener | consulta 06/10/2026 16:40 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 16:40 UTC)
- **Historia:**
  - Par creado el 06/10/2026 15:33 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 16:33 UTC, con el par a 60,1 min de creado: precio $0,003371, mcap $3.368.804, liquidez $167.323.
  - Velas de 1 h de GeckoTerminal (2, desde 06/10/2026 15:00 UTC): apertura $0,003185 · máximo $0,003400 (06/10/2026 16:00 UTC) · mínimo $0,00005046 (06/10/2026 15:00 UTC) · último cierre $0,003384.
  - En la consulta 06/10/2026 16:40 UTC: precio $0,003354, liquidez $166.607, FDV $3.352.732.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 16:33 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003371 |
| Liquidez | $167.323 |
| MCap | $3.368.804 |
| Volumen 24 h | $79.703 |
| Cambio 24 h | +6.580% |
| Cambio m5 / h1 | -0,7% / +5,4% |
| Volumen m5 / h1 | $691 / $7.509 |
| Trades m5 (compras / ventas) | 12 / 9 |
| Edad del par | 60,1 min |
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

Desglose reconstruido desde los motivos registrados; suma 88 = score registrado 88 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $1M | $3.368.804 | +25 |
| Volumen 24 h | ≥ $50K | $79.703 | +10 |
| Buy pressure m5 | > 55% (par maduro) | 57% | +15 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,1 min | +8 |
| Volumen m5 | > $500 (par maduro) | $691 | +5 |
| Liquidez | ≥ $100K | $167.323 | +15 |
| Cambio 24 h | ≥ +50% | +6.580% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +6.580% · liq/mcap 5,0% | +0 |
| **Total** | recortado a 0–100 |  | **88** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T16:33:45+00:00, sin estado previo): **88** · motivos: MCap > $1M, Volumen decente, Buy pressure >55%, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=5.0% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 21 de 15.947 tokens analizados (0,13%) quedan ≥ 56. Con score 88, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 16:33 UTC, hasta 08/10/2026 16:33 UTC · vigente: quedan 47,9 h.
- **Aceleración al detectar:** cambio m5 -0,7% · h1 +5,4% · h24 +6.580% · volumen m5/h1 0,09 · edad del par 60,1 min.
- **Precio de entrada** (alerta): $0,003371.
- **Consulta 06/10/2026 16:40 UTC:** $0,003354 (-0,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump_2026-10-06_163345.json` · blob `0c46966c7ca99ae0418c808be8d55de0605473f2` · commit `9a0135d` (2026-10-06T16:34:08Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_163345`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump · registro · 06/10/2026 16:33 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump · HTTP 200 · 06/10/2026 16:40 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump/report · HTTP 200 · 06/10/2026 16:40 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump · HTTP 200 · 06/10/2026 16:40 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/77YL5myqdVRwQC1n8XM1g4pANagHtw9wxCDbwhsKueQh/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 16:40 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump · HTTP 404 · 06/10/2026 16:40 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ARROWUSDT · HTTP 400 · 06/10/2026 16:40 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ARROW-USD · HTTP 404 · 06/10/2026 16:40 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $166.607 vs $167.435 → 0,49%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003354 vs $0,003384 → 0,88%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump_2026-10-06_163345.json',encoding='utf-8'));d=d.get('YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump',d);p=mock.patch('time.time',return_value=1791304425);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint YW6z2n1WiCwjVT3ud1My77gEXjntR4BGsLfjRuNpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 16:41 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `6e74c5e35d449387…`
