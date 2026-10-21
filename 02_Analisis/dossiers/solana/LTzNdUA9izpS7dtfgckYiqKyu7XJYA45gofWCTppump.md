# American Overwatch Protocol🔥 (AOP) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1731 · liquidez $1.138.664 · mcap $173.162.549 (al detectar)  
Detectado el 21/10/2026 08:33 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 89, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 23/10/2026 08:33 UTC (< 48 h) · vigente: quedan 47,2 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir AOP

Estudio de cómo se adquiere AOP, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 21/10/2026 09:20 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 21/10/2026 08:33 UTC | pumpswap `54LEryi…YWJv` | $1.138.664 | 1% | 0,018% | 0,176% | 1,756% | $5.693 | $17.080 |
| consulta 21/10/2026 09:20 UTC | pumpswap `54LEryi…YWJv` | $1.144.825 | 1% | 0,017% | 0,175% | 1,747% | $5.724 | $17.172 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump`
5. Configurar el slippage: 1% (liquidez $1.144.825, consulta 21/10/2026 09:20 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump) y el par en DexScreener (https://dexscreener.com/solana/54LEryiAAec1WpNUyNQViAeJa8GuytXtQvj8QvY8YWJv); mint authority / freeze authority: revocada / revocada · holders 4.038 · top-10 0,56% (consulta 21/10/2026 09:20 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump
- Par en DexScreener: https://dexscreener.com/solana/54LEryiAAec1WpNUyNQViAeJa8GuytXtQvj8QvY8YWJv
- Página del lanzamiento (pump.fun): https://pump.fun/coin/LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.038 · top-10 0,56% (consulta 21/10/2026 09:20 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | American Overwatch Protocol🔥 / AOP | registro de la detección (trending) |
| Mint / contrato | `LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `54LEryiAAec1WpNUyNQViAeJa8GuytXtQvj8QvY8YWJv` | DexScreener, al detectar (2 par(es) en la consulta 21/10/2026 09:20 UTC) |
| Deployer | `836miveVjDbEqaLotx2FGNcXT9DWQiUeXbYLib39Pugd` | RugCheck `creator` |
| Par creado | 21/10/2026 01:01 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 7,5 h / 7,5 h / 8,3 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 21/10/2026 09:20 UTC |
| Holders / top-10 | 4.038 / 0,56% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 21/10/2026 09:20 UTC |
| Holders efectivos del top-10 | 2,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 21/10/2026 09:20 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 21/10/2026 09:20 UTC |
| Links | DexScreener: https://dexscreener.com/solana/54LEryiAAec1WpNUyNQViAeJa8GuytXtQvj8QvY8YWJv · Solscan: https://solscan.io/token/LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump · pump.fun: https://pump.fun/coin/LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump · web / Telegram / X: no publicados en DexScreener | consulta 21/10/2026 09:20 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 21/10/2026 09:20 UTC)
- **Historia:**
  - Par creado el 21/10/2026 01:01 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 21/10/2026 08:33 UTC, con el par a 7,5 h de creado: precio $0,1731, mcap $173.162.549, liquidez $1.138.664.
  - Velas de 1 h de GeckoTerminal (9, desde 21/10/2026 01:00 UTC): apertura $0,1532 · máximo $0,1754 (21/10/2026 09:00 UTC) · mínimo $0,00004418 (21/10/2026 01:00 UTC) · último cierre $0,1744.
  - En la consulta 21/10/2026 09:20 UTC: precio $0,1744, liquidez $1.144.825, FDV $174.481.171.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 21/10/2026 08:33 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1731 |
| Liquidez | $1.138.664 |
| MCap | $173.162.549 |
| Volumen 24 h | $604.681 |
| Cambio 24 h | +390.694% |
| Cambio m5 / h1 | +0,0% / +0,8% |
| Volumen m5 / h1 | $548 / $6.989 |
| Trades m5 (compras / ventas) | 9 / 5 |
| Edad del par | 7,5 h |
| Score del feed (WS) | 82 |

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

Desglose reconstruido desde los motivos registrados; suma 89 = score registrado 89 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 82 × 0,3 | +24,5 |
| MCap | ≥ $1M | $173.162.549 | +25 |
| Volumen 24 h | ≥ $100K | $604.681 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 64% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,0% · h1 +0,8% | +20 |
| Volumen m5 | > $500 (par maduro) | $548 | +5 |
| Liquidez | ≥ $100K | $1.138.664 | +15 |
| Cambio 24 h | ≥ +50% | +390.694% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +390.694% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **89** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-21T08:33:11+00:00, sin estado previo): **89** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 73 de 42.841 tokens analizados (0,17%) quedan ≥ 56. Con score 89, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 21/10/2026 08:33 UTC, hasta 23/10/2026 08:33 UTC · vigente: quedan 47,2 h.
- **Aceleración al detectar:** cambio m5 +0,0% · h1 +0,8% · h24 +390.694% · volumen m5/h1 0,08 · edad del par 7,5 h.
- **Precio de entrada** (alerta): $0,1731.
- **Consulta 21/10/2026 09:20 UTC:** $0,1744 (+0,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump_2026-10-21_083311.json` · blob `e1bd4f50e1eebd77318cb70750c6840791930d5d` · commit `fff5799` (2026-10-21T09:11:08Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-21_082654.json` · blob `038f4a5961e9165ca26d094d624102477d988dd7` · commit `fff5799` (2026-10-21T09:11:08Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-21_083311`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump · registro · 21/10/2026 08:33 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump · HTTP 200 · 21/10/2026 09:20 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump/report · HTTP 200 · 21/10/2026 09:20 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump · HTTP 200 · 21/10/2026 09:20 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/54LEryiAAec1WpNUyNQViAeJa8GuytXtQvj8QvY8YWJv/ohlcv/hour?limit=1000 · HTTP 200 · 21/10/2026 09:20 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump · HTTP 404 · 21/10/2026 09:20 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AOPUSDT · HTTP 400 · 21/10/2026 09:20 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AOP-USD · HTTP 404 · 21/10/2026 09:20 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.144.825 vs $1.148.033 → 0,28%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1744 vs $0,1744 → 0,00%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump_2026-10-21_083311.json',encoding='utf-8'));d=d.get('LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump',d);p=mock.patch('time.time',return_value=1792571591);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint LTzNdUA9izpS7dtfgckYiqKyu7XJYA45gofWCTppump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 21/10/2026 09:20 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `4fc85c05632aa65f…`
