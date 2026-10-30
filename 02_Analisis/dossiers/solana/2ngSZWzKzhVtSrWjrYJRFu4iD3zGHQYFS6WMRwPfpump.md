# MOTH (MOTH) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000004544 · liquidez $3.980 · mcap $4.478 (al detectar)  
Detectado el 30/10/2026 18:58 UTC por: MCap bajo, Volumen alto, Buy pressure >60% (score 63, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 01/11/2026 18:58 UTC (< 48 h) · vigente: quedan 45,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir MOTH

Estudio de cómo se adquiere MOTH, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 30/10/2026 21:27 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 30/10/2026 18:58 UTC | pumpswap `zFmiMDU…xaPz` | $3.980 | 10% | 5,026% | 50,256% | 502,555% | $20 | $60 |
| consulta 30/10/2026 21:27 UTC | pumpswap `zFmiMDU…xaPz` | $3.434 | 10% | 5,825% | 58,248% | 582,482% | $17 | $52 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump`
5. Configurar el slippage: 10% (liquidez $3.434, consulta 30/10/2026 21:27 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump) y el par en DexScreener (https://dexscreener.com/solana/zFmiMDUyRPs4QXrUamVQMGogGNWgFxFvNPWkGdSxaPz); mint authority / freeze authority: revocada / revocada · holders 873 · top-10 84,57% (consulta 30/10/2026 21:27 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump
- Par en DexScreener: https://dexscreener.com/solana/zFmiMDUyRPs4QXrUamVQMGogGNWgFxFvNPWkGdSxaPz
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 873 · top-10 84,57% (consulta 30/10/2026 21:27 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | MOTH / MOTH | registro de la detección (pumpportal) |
| Mint / contrato | `2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `zFmiMDUyRPs4QXrUamVQMGogGNWgFxFvNPWkGdSxaPz` | DexScreener, al detectar (2 par(es) en la consulta 30/10/2026 21:27 UTC) |
| Deployer | `13JWZY4ApDtHby8uyAwJmTbWpd5JvSTHCwST9iKhfJNu` | PumpPortal (evento create), al detectar |
| Par creado | 30/10/2026 16:51 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 2,1 h / 2,1 h / 4,6 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 30/10/2026 21:27 UTC |
| Holders / top-10 | 873 / 84,57% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 30/10/2026 21:27 UTC |
| Holders efectivos del top-10 | 1,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 30/10/2026 21:27 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 30/10/2026 21:27 UTC |
| Links | DexScreener: https://dexscreener.com/solana/zFmiMDUyRPs4QXrUamVQMGogGNWgFxFvNPWkGdSxaPz · Solscan: https://solscan.io/token/2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump · pump.fun: https://pump.fun/coin/2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump · web: https://mothsolana.webby.fun/ · twitter: https://x.com/mothsolana_?s=11 · telegram: https://t.me/MothonSolana | consulta 30/10/2026 21:27 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 30/10/2026 21:27 UTC)
- **Historia:**
  - Par creado el 30/10/2026 16:51 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 30/10/2026 18:58 UTC, con el par a 2,1 h de creado: precio $0,000004544, mcap $4.478, liquidez $3.980.
  - Velas de 1 h de GeckoTerminal (6, desde 30/10/2026 16:00 UTC): apertura $0,00006593 · máximo $0,0002267 (30/10/2026 17:00 UTC) · mínimo $0,000002431 (30/10/2026 17:00 UTC) · último cierre $0,000003698.
  - En la consulta 30/10/2026 21:27 UTC: precio $0,000003692, liquidez $3.434, FDV $3.638.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 30/10/2026 18:58 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000004544 |
| Liquidez | $3.980 |
| MCap | $4.478 |
| Volumen 24 h | $284.634 |
| Cambio 24 h | -91% |
| Cambio m5 / h1 | +7,7% / +37,5% |
| Volumen m5 / h1 | $75 / $691 |
| Trades m5 (compras / ventas) | 4 / 1 |
| Edad del par | 2,1 h |
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

Desglose reconstruido desde los motivos registrados; suma 63 = score registrado 63 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | < $50K | $4.478 | +0 |
| Volumen 24 h | ≥ $100K | $284.634 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 80% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +7,7% · h1 +37,5% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 2,1 h | +8 |
| Liquidez | < $20K | $3.980 | +0 |
| Cambio 24 h | ≤ −30% | -91% | -5 |
| **Total** | recortado a 0–100 |  | **63** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-30T18:58:00+00:00, sin estado previo): **63** · motivos: MCap bajo, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 83 de 46.328 tokens analizados (0,18%) quedan ≥ 56. Con score 63, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 30/10/2026 18:58 UTC, hasta 01/11/2026 18:58 UTC · vigente: quedan 45,5 h.
- **Aceleración al detectar:** cambio m5 +7,7% · h1 +37,5% · h24 -91% · volumen m5/h1 0,11 · edad del par 2,1 h.
- **Precio de entrada** (alerta): $0,000004544.
- **Consulta 30/10/2026 21:27 UTC:** $0,000003692 (-18,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump_2026-10-30_185800.json` · blob `9a9c848629256680910ec98eb5f5c591843b08a9` · commit `e69fe82` (2026-10-30T21:10:22Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-30_185800`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump · registro · 30/10/2026 18:58 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump · HTTP 200 · 30/10/2026 21:27 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump/report · HTTP 200 · 30/10/2026 21:27 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump · HTTP 200 · 30/10/2026 21:27 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/zFmiMDUyRPs4QXrUamVQMGogGNWgFxFvNPWkGdSxaPz/ohlcv/hour?limit=1000 · HTTP 200 · 30/10/2026 21:27 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump · HTTP 404 · 30/10/2026 21:27 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MOTHUSDT · HTTP 400 · 30/10/2026 21:27 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MOTH-USD · HTTP 404 · 30/10/2026 21:27 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.434 vs $3.442 → 0,23%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000003692 vs $0,000003698 → 0,16%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump_2026-10-30_185800.json',encoding='utf-8'));d=d.get('2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump',d);p=mock.patch('time.time',return_value=1793386680);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2ngSZWzKzhVtSrWjrYJRFu4iD3zGHQYFS6WMRwPfpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 30/10/2026 21:27 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `9fdac68dbd676d11…`
