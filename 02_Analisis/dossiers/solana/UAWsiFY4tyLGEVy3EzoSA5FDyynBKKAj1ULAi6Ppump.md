# United States Dividend Fund (USDF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,4457 · liquidez $1.864.850 · mcap $445.784.625 (al detectar)  
Detectado el 09/10/2026 12:24 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 11/10/2026 12:24 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir USDF

Estudio de cómo se adquiere USDF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 09/10/2026 12:44 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 09/10/2026 12:24 UTC | pumpswap `7fjBkq9…JyxN` | $1.864.850 | 1% | 0,011% | 0,107% | 1,072% | $9.324 | $27.973 |
| consulta 09/10/2026 12:44 UTC | pumpswap `7fjBkq9…JyxN` | $1.864.014 | 1% | 0,011% | 0,107% | 1,073% | $9.320 | $27.960 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump`
5. Configurar el slippage: 1% (liquidez $1.864.014, consulta 09/10/2026 12:44 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump) y el par en DexScreener (https://dexscreener.com/solana/7fjBkq99Ewk3czfWXi9Vj8jQcwRnnHaexszp7Pj1JyxN); mint authority / freeze authority: revocada / revocada · holders 3.025 · top-10 0,69% (consulta 09/10/2026 12:44 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump
- Par en DexScreener: https://dexscreener.com/solana/7fjBkq99Ewk3czfWXi9Vj8jQcwRnnHaexszp7Pj1JyxN
- Página del lanzamiento (pump.fun): https://pump.fun/coin/UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.025 · top-10 0,69% (consulta 09/10/2026 12:44 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | United States Dividend Fund / USDF | registro de la detección (trending) |
| Mint / contrato | `UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7fjBkq99Ewk3czfWXi9Vj8jQcwRnnHaexszp7Pj1JyxN` | DexScreener, al detectar (2 par(es) en la consulta 09/10/2026 12:44 UTC) |
| Deployer | `DkNsC93UQdPStqHp6vZhcjDEK32Eb42Ft2ZT6Qa4mkMz` | RugCheck `creator` |
| Par creado | 09/10/2026 11:24 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,8 min / 60,8 min / 80,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 09/10/2026 12:44 UTC |
| Holders / top-10 | 3.025 / 0,69% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 09/10/2026 12:44 UTC |
| Holders efectivos del top-10 | 6,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 09/10/2026 12:44 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 09/10/2026 12:44 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7fjBkq99Ewk3czfWXi9Vj8jQcwRnnHaexszp7Pj1JyxN · Solscan: https://solscan.io/token/UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump · pump.fun: https://pump.fun/coin/UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump · web / Telegram / X: no publicados en DexScreener | consulta 09/10/2026 12:44 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 09/10/2026 12:44 UTC)
- **Historia:**
  - Par creado el 09/10/2026 11:24 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 09/10/2026 12:24 UTC, con el par a 60,8 min de creado: precio $0,4457, mcap $445.784.625, liquidez $1.864.850.
  - Velas de 1 h de GeckoTerminal (2, desde 09/10/2026 11:00 UTC): apertura $0,00004564 · máximo $0,4492 (09/10/2026 12:00 UTC) · mínimo $0,00004564 (09/10/2026 11:00 UTC) · último cierre $0,4483.
  - En la consulta 09/10/2026 12:44 UTC: precio $0,4468, liquidez $1.864.014, FDV $446.863.566.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 09/10/2026 12:24 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,4457 |
| Liquidez | $1.864.850 |
| MCap | $445.784.625 |
| Volumen 24 h | $1.125.605 |
| Cambio 24 h | +975.468% |
| Cambio m5 / h1 | +0,3% / +11,2% |
| Volumen m5 / h1 | $2.648 / $254.817 |
| Trades m5 (compras / ventas) | 269 / 6 |
| Edad del par | 60,8 min |
| Score del feed (WS) | 91 |

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
| Score del feed | score WS × 0,3 | WS 91 × 0,3 | +27,2 |
| MCap | ≥ $1M | $445.784.625 | +25 |
| Volumen 24 h | ≥ $1M | $1.125.605 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 98% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,3% · h1 +11,2% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,8 min | +8 |
| Volumen m5 | > $1K (par maduro) | $2.648 | +10 |
| Liquidez | ≥ $100K | $1.864.850 | +15 |
| Cambio 24 h | ≥ +50% | +975.468% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +975.468% · liq/mcap 0,4% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-09T12:24:54+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 41 de 24.594 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 09/10/2026 12:24 UTC, hasta 11/10/2026 12:24 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +0,3% · h1 +11,2% · h24 +975.468% · volumen m5/h1 0,01 · edad del par 60,8 min.
- **Precio de entrada** (alerta): $0,4457.
- **Consulta 09/10/2026 12:44 UTC:** $0,4468 (+0,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump_2026-10-09_122454.json` · blob `a133522dcc86737d851c489506234f4a6079115b` · commit `2a7b0e4` (2026-10-09T12:37:37Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-09_113159.json` · blob `0cb28029c6693badede63f854ed3c5465e934dd3` · commit `2a7b0e4` (2026-10-09T12:37:37Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-09_122454`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump · registro · 09/10/2026 12:24 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump · HTTP 200 · 09/10/2026 12:44 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump/report · HTTP 200 · 09/10/2026 12:44 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump · HTTP 200 · 09/10/2026 12:44 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7fjBkq99Ewk3czfWXi9Vj8jQcwRnnHaexszp7Pj1JyxN/ohlcv/hour?limit=1000 · HTTP 200 · 09/10/2026 12:44 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump · HTTP 404 · 09/10/2026 12:44 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=USDFUSDT · HTTP 400 · 09/10/2026 12:44 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/USDF-USD · HTTP 404 · 09/10/2026 12:44 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.864.014 vs $1.865.537 → 0,08%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,4468 vs $0,4483 → 0,33%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump_2026-10-09_122454.json',encoding='utf-8'));d=d.get('UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump',d);p=mock.patch('time.time',return_value=1791548694);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint UAWsiFY4tyLGEVy3EzoSA5FDyynBKKAj1ULAi6Ppump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 09/10/2026 12:44 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `04620b9750b80b44…`
