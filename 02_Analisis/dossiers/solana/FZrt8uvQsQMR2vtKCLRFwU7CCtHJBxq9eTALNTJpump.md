# World Oil Fund Institution🔥 (WOFI) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,008085 · liquidez $257.930 · mcap $8.085.240 (al detectar)  
Detectado el 02/10/2026 23:50 UTC por: MCap > $1M, Volumen alto, Liquidez alta (score 65, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 04/10/2026 23:50 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir WOFI

Estudio de cómo se adquiere WOFI, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 03/10/2026 00:13 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 23:50 UTC | pumpswap `qyUJB5V…sz5R` | $257.930 | 3% | 0,078% | 0,775% | 7,754% | $1.290 | $3.869 |
| consulta 03/10/2026 00:13 UTC | pumpswap `qyUJB5V…sz5R` | $258.759 | 3% | 0,077% | 0,773% | 7,729% | $1.294 | $3.881 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump`
5. Configurar el slippage: 3% (liquidez $258.759, consulta 03/10/2026 00:13 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump) y el par en DexScreener (https://dexscreener.com/solana/qyUJB5V7pRdDUQ7bhGSgUQeXjyLJFDjXdxYDLiusz5R); mint authority / freeze authority: revocada / revocada · holders 2.038 · top-10 3,88% (consulta 03/10/2026 00:13 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump
- Par en DexScreener: https://dexscreener.com/solana/qyUJB5V7pRdDUQ7bhGSgUQeXjyLJFDjXdxYDLiusz5R
- Página del lanzamiento (pump.fun): https://pump.fun/coin/FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.038 · top-10 3,88% (consulta 03/10/2026 00:13 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | World Oil Fund Institution🔥 / WOFI | registro de la detección (pumpportal_live) |
| Mint / contrato | `FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `qyUJB5V7pRdDUQ7bhGSgUQeXjyLJFDjXdxYDLiusz5R` | DexScreener, al detectar (2 par(es) en la consulta 03/10/2026 00:13 UTC) |
| Deployer | `6CnZJDv8M8qY32fEHnUA4DLo3A99yN5U1rKJPU7qVYE1` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 23:39 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,6 min / 10,6 min / 34,0 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 03/10/2026 00:13 UTC |
| Holders / top-10 | 2.038 / 3,88% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 03/10/2026 00:13 UTC |
| Holders efectivos del top-10 | 4,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 03/10/2026 00:13 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 03/10/2026 00:13 UTC |
| Links | DexScreener: https://dexscreener.com/solana/qyUJB5V7pRdDUQ7bhGSgUQeXjyLJFDjXdxYDLiusz5R · Solscan: https://solscan.io/token/FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump · pump.fun: https://pump.fun/coin/FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump · web / Telegram / X: no publicados en DexScreener | consulta 03/10/2026 00:13 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 03/10/2026 00:13 UTC)
- **Historia:**
  - Par creado el 02/10/2026 23:39 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 23:50 UTC, con el par a 10,6 min de creado: precio $0,008085, mcap $8.085.240, liquidez $257.930.
  - Velas de 1 h de GeckoTerminal (2, desde 02/10/2026 23:00 UTC): apertura $0,007783 · máximo $0,008194 (03/10/2026 00:00 UTC) · mínimo $0,00004926 (02/10/2026 23:00 UTC) · último cierre $0,008194.
  - En la consulta 03/10/2026 00:13 UTC: precio $0,008139, liquidez $258.759, FDV $8.139.112.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 23:50 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,008085 |
| Liquidez | $257.930 |
| MCap | $8.085.240 |
| Volumen 24 h | $119.612 |
| Cambio 24 h | +16.310% |
| Cambio m5 / h1 | +0,1% / +16.310,0% |
| Volumen m5 / h1 | $804 / $119.612 |
| Trades m5 (compras / ventas) | 432 / 16 |
| Edad del par | 10,6 min |
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

Desglose reconstruido desde los motivos registrados; suma 65 = score registrado 65 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| Gate de edad v7.2.1 | edad < 60 min o desconocida: sin bonos temporales | edad 10,6 min | +0 |
| MCap | ≥ $1M | $8.085.240 | +25 |
| Volumen 24 h | ≥ $100K | $119.612 | +15 |
| Liquidez | ≥ $100K | $257.930 | +15 |
| Cambio 24 h | ≥ +50% | +16.310% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +16.310% · liq/mcap 3,2% | +0 |
| **Total** | recortado a 0–100 |  | **65** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T23:50:29+00:00, sin estado previo): **65** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen alto, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=3.2% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 11 de 9.188 tokens analizados (0,12%) quedan ≥ 56. Con score 65, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 23:50 UTC, hasta 04/10/2026 23:50 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +0,1% · h1 +16.310,0% · h24 +16.310% · volumen m5/h1 0,01 · edad del par 10,6 min.
- **Precio de entrada** (alerta): $0,008085.
- **Consulta 03/10/2026 00:13 UTC:** $0,008139 (+0,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump_2026-10-02_235029.json` · blob `da81438601748b2e1e9c77a07748eca9a7c9cc5a` · commit `72cff47` (2026-10-03T00:03:30Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_235029`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump · registro · 02/10/2026 23:50 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump · HTTP 200 · 03/10/2026 00:13 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump/report · HTTP 200 · 03/10/2026 00:13 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump · HTTP 200 · 03/10/2026 00:13 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/qyUJB5V7pRdDUQ7bhGSgUQeXjyLJFDjXdxYDLiusz5R/ohlcv/hour?limit=1000 · HTTP 200 · 03/10/2026 00:13 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump · HTTP 404 · 03/10/2026 00:13 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=WOFIUSDT · HTTP 400 · 03/10/2026 00:13 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/WOFI-USD · HTTP 404 · 03/10/2026 00:13 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $258.759 vs $258.897 → 0,05%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,008139 vs $0,008194 → 0,67%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump_2026-10-02_235029.json',encoding='utf-8'));d=d.get('FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump',d);p=mock.patch('time.time',return_value=1790985029);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint FZrt8uvQsQMR2vtKCLRFwU7CCtHJBxq9eTALNTJpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 03/10/2026 00:13 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `3ed997d32c60e5ce…`
