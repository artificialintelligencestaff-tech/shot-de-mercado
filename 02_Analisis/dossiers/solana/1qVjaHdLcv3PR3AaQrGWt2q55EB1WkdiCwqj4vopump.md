# Xpose The Trenches (XPOSE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003624 · liquidez $161.274 · mcap $3.622.760 (al detectar)  
Detectado el 15/10/2026 01:21 UTC por: MCap > $1M, Volumen decente, Buy pressure >60% (score 93, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 17/10/2026 01:21 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir XPOSE

Estudio de cómo se adquiere XPOSE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 15/10/2026 01:32 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 15/10/2026 01:21 UTC | pumpswap `4qwdqNJ…1TJX` | $161.274 | 5% | 0,124% | 1,240% | 12,401% | $806 | $2.419 |
| consulta 15/10/2026 01:32 UTC | pumpswap `4qwdqNJ…1TJX` | $161.622 | 5% | 0,124% | 1,237% | 12,375% | $808 | $2.424 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump`
5. Configurar el slippage: 5% (liquidez $161.622, consulta 15/10/2026 01:32 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump) y el par en DexScreener (https://dexscreener.com/solana/4qwdqNJ1mn9MxBmbhifDesmrf3yxHU2yu71r3JhW1TJX); mint authority / freeze authority: revocada / revocada · holders 2.296 · top-10 5,53% (consulta 15/10/2026 01:32 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump
- Par en DexScreener: https://dexscreener.com/solana/4qwdqNJ1mn9MxBmbhifDesmrf3yxHU2yu71r3JhW1TJX
- Página del lanzamiento (pump.fun): https://pump.fun/coin/1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.296 · top-10 5,53% (consulta 15/10/2026 01:32 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Xpose The Trenches / XPOSE | registro de la detección (pumpportal) |
| Mint / contrato | `1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `4qwdqNJ1mn9MxBmbhifDesmrf3yxHU2yu71r3JhW1TJX` | DexScreener, al detectar (2 par(es) en la consulta 15/10/2026 01:32 UTC) |
| Deployer | `GY9xKzRRvLeBMCgJRHJHDDzFGkwefCFfKVUeTnGMgVXc` | PumpPortal (evento create), al detectar |
| Par creado | 15/10/2026 00:20 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,7 min / 60,7 min / 71,5 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 15/10/2026 01:32 UTC |
| Holders / top-10 | 2.296 / 5,53% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 15/10/2026 01:32 UTC |
| Holders efectivos del top-10 | 2,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 15/10/2026 01:32 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 15/10/2026 01:32 UTC |
| Links | DexScreener: https://dexscreener.com/solana/4qwdqNJ1mn9MxBmbhifDesmrf3yxHU2yu71r3JhW1TJX · Solscan: https://solscan.io/token/1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump · pump.fun: https://pump.fun/coin/1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump · web / Telegram / X: no publicados en DexScreener | consulta 15/10/2026 01:32 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 15/10/2026 01:32 UTC)
- **Historia:**
  - Par creado el 15/10/2026 00:20 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 15/10/2026 01:21 UTC, con el par a 60,7 min de creado: precio $0,003624, mcap $3.622.760, liquidez $161.274.
  - Velas de 1 h de GeckoTerminal (2, desde 15/10/2026 00:00 UTC): apertura $0,00004335 · máximo $0,003672 (15/10/2026 01:00 UTC) · mínimo $0,00004335 (15/10/2026 00:00 UTC) · último cierre $0,003644.
  - En la consulta 15/10/2026 01:32 UTC: precio $0,003640, liquidez $161.622, FDV $3.638.507.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 15/10/2026 01:21 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003624 |
| Liquidez | $161.274 |
| MCap | $3.622.760 |
| Volumen 24 h | $73.707 |
| Cambio 24 h | +8.256% |
| Cambio m5 / h1 | -0,9% / +7,0% |
| Volumen m5 / h1 | $225 / $3.936 |
| Trades m5 (compras / ventas) | 7 / 4 |
| Edad del par | 60,7 min |
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

Desglose reconstruido desde los motivos registrados; suma 93 = score registrado 93 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $1M | $3.622.760 | +25 |
| Volumen 24 h | ≥ $50K | $73.707 | +10 |
| Buy pressure m5 | > 60% (par maduro) | 64% | +25 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,7 min | +8 |
| Liquidez | ≥ $100K | $161.274 | +15 |
| Cambio 24 h | ≥ +50% | +8.256% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +8.256% · liq/mcap 4,5% | +0 |
| **Total** | recortado a 0–100 |  | **93** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-15T01:21:36+00:00, sin estado previo): **93** · motivos: MCap > $1M, Volumen decente, Buy pressure >60%, Edge temprano (<4h), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 59 de 35.539 tokens analizados (0,17%) quedan ≥ 56. Con score 93, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 15/10/2026 01:21 UTC, hasta 17/10/2026 01:21 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -0,9% · h1 +7,0% · h24 +8.256% · volumen m5/h1 0,06 · edad del par 60,7 min.
- **Precio de entrada** (alerta): $0,003624.
- **Consulta 15/10/2026 01:32 UTC:** $0,003640 (+0,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump_2026-10-15_012136.json` · blob `941a38bb93505d367e824893ebb5db20bb0406c5` · commit `7fcde52` (2026-10-15T01:25:34Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-15_012136`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump · registro · 15/10/2026 01:21 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump · HTTP 200 · 15/10/2026 01:32 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump/report · HTTP 200 · 15/10/2026 01:32 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump · HTTP 200 · 15/10/2026 01:32 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/4qwdqNJ1mn9MxBmbhifDesmrf3yxHU2yu71r3JhW1TJX/ohlcv/hour?limit=1000 · HTTP 200 · 15/10/2026 01:32 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump · HTTP 404 · 15/10/2026 01:32 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=XPOSEUSDT · HTTP 400 · 15/10/2026 01:32 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/XPOSE-USD · HTTP 404 · 15/10/2026 01:32 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $161.622 vs $161.460 → 0,10%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003640 vs $0,003644 → 0,10%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump_2026-10-15_012136.json',encoding='utf-8'));d=d.get('1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump',d);p=mock.patch('time.time',return_value=1792027296);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 1qVjaHdLcv3PR3AaQrGWt2q55EB1WkdiCwqj4vopump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 15/10/2026 01:32 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `dcf74b44de886b7a…`
