# TeslaX (TESLAX) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001100 · liquidez $26.880 · mcap $110.036 (al detectar)  
Detectado el 14/10/2026 21:46 UTC por: young-0.4 · edad 11.8 min · pesos info 59 / estructura 20 / precio 20 · info 20.0 · estructura 12.2 · precio/volumen 8.5 · cobertura 88/100, [info] narrative_wave: ola 'teslax': 8 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 1 caracteres → +5.3 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 16/10/2026 21:46 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir TESLAX

Estudio de cómo se adquiere TESLAX, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 14/10/2026 21:58 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 14/10/2026 21:46 UTC | pumpswap `ACetCBp…fFJe` | $26.880 | 10% | 0,744% | 7,441% | 74,406% | $134 | $403 |
| consulta 14/10/2026 21:57 UTC | pumpswap `ACetCBp…fFJe` | $2.145 | 10% | 9,324% | 93,241% | 932,405% | $11 | $32 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump`
5. Configurar el slippage: 10% (liquidez $2.145, consulta 14/10/2026 21:57 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump) y el par en DexScreener (https://dexscreener.com/solana/ACetCBpHKQiWWmNvD7T5HmkhFDe6dEbrMjmVwtexfFJe); mint authority / freeze authority: revocada / revocada · holders n/d · top-10 n/d (consulta 14/10/2026 21:57 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump
- Par en DexScreener: https://dexscreener.com/solana/ACetCBpHKQiWWmNvD7T5HmkhFDe6dEbrMjmVwtexfFJe
- Página del lanzamiento (pump.fun): https://pump.fun/coin/4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders n/d · top-10 n/d (consulta 14/10/2026 21:57 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | TeslaX / TESLAX | registro de la detección (pumpportal_live) |
| Mint / contrato | `4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `ACetCBpHKQiWWmNvD7T5HmkhFDe6dEbrMjmVwtexfFJe` | DexScreener, al detectar (2 par(es) en la consulta 14/10/2026 21:57 UTC) |
| Deployer | `9P18wpFEsbusiDjVnz8BjRoycHpuGyYxWV3nraiaBWfc` | PumpPortal (evento create), al detectar |
| Par creado | 14/10/2026 21:34 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,8 min / 11,8 min / 23,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | GoPlus, consulta 14/10/2026 21:57 UTC |
| Holders / top-10 | n/d / n/d | RugCheck [P: sin consulta] |
| Holders efectivos del top-10 | n/d | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | n/d | RugCheck [P] |
| Etiquetas de RugCheck | n/d | RugCheck [P] |
| Links | DexScreener: https://dexscreener.com/solana/ACetCBpHKQiWWmNvD7T5HmkhFDe6dEbrMjmVwtexfFJe · Solscan: https://solscan.io/token/4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump · pump.fun: https://pump.fun/coin/4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump · web / Telegram / X: no publicados en DexScreener | consulta 14/10/2026 21:57 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (metadata sin consultar [P])
- **Historia:**
  - Par creado el 14/10/2026 21:34 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 14/10/2026 21:46 UTC, con el par a 11,8 min de creado: precio $0,0001100, mcap $110.036, liquidez $26.880.
  - Velas de 1 h de GeckoTerminal (1, desde 14/10/2026 21:00 UTC): apertura $0,00004503 · máximo $0,0001123 (14/10/2026 21:00 UTC) · mínimo $0,000002076 (14/10/2026 21:00 UTC) · último cierre $0,000002076.
  - En la consulta 14/10/2026 21:57 UTC: precio $0,000002081, liquidez $2.145, FDV $2.082.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 14/10/2026 21:46 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001100 |
| Liquidez | $26.880 |
| MCap | $110.036 |
| Volumen 24 h | $113.544 |
| Cambio 24 h | +150% |
| Cambio m5 / h1 | +42,9% / +150,0% |
| Volumen m5 / h1 | $51.288 / $113.544 |
| Trades m5 (compras / ventas) | 2.090 / 1.286 |
| Edad del par | 11,8 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 11.8 min · pesos info 59 / estructura 20 / precio 20 · info 20.0 · estructura 12.2 · precio/volumen 8.5 · cobertura 88/100, [info] narrative_wave: ola 'teslax': 8 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 1 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] dev_wallet: creador compró 2.1 % del supply → +2.4, [precio/volumen] volume_acceleration: vol 5 min ×5.4 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +61% en 8 min (s 1.00), [flag, no suma] tradable=True, liquidity_usd=26879.51, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-14T21:46:15+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 56 de 35.295 tokens analizados (0,16%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 14/10/2026 21:46 UTC, hasta 16/10/2026 21:46 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +42,9% · h1 +150,0% · h24 +150% · volumen m5/h1 0,45 · edad del par 11,8 min.
- **Precio de entrada** (alerta): $0,0001100.
- **Consulta 14/10/2026 21:57 UTC:** $0,000002081 (-98,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump_2026-10-14_214615.json` · blob `7293dfc59106e40a58e59c9e60c26a73c04777d0` · commit `d1adcbc` (2026-10-14T21:48:34Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-14_214615`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump · registro · 14/10/2026 21:46 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump · HTTP 200 · 14/10/2026 21:57 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump/report · HTTP 400 · 14/10/2026 21:57 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump · HTTP 200 · 14/10/2026 21:57 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/ACetCBpHKQiWWmNvD7T5HmkhFDe6dEbrMjmVwtexfFJe/ohlcv/hour?limit=1000 · HTTP 200 · 14/10/2026 21:58 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump · HTTP 404 · 14/10/2026 21:58 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=TESLAXUSDT · HTTP 400 · 14/10/2026 21:58 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/TESLAX-USD · HTTP 404 · 14/10/2026 21:58 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002081 vs $0,000002076 → 0,22%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump_2026-10-14_214615.json',encoding='utf-8'));d=d.get('4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump',d);p=mock.patch('time.time',return_value=1792014375);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 4499DNiLucQXbjXQmbpoxvdeuXJUZHgtBA8o6qJppump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 14/10/2026 21:58 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `5d054f1267b2a2f7…`
