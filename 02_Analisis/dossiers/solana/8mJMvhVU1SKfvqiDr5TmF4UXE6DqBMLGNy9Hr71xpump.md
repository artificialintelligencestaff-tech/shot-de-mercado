# United States Dividend Fund (USDF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1805 · liquidez $1.182.850 · mcap $180.562.169 (al detectar)  
Detectado el 10/10/2026 20:38 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 96, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 12/10/2026 20:38 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir USDF

Estudio de cómo se adquiere USDF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 10/10/2026 20:55 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 10/10/2026 20:38 UTC | pumpswap `9BaXguK…RB4z` | $1.182.850 | 1% | 0,017% | 0,169% | 1,691% | $5.914 | $17.743 |
| consulta 10/10/2026 20:55 UTC | pumpswap `9BaXguK…RB4z` | $1.186.583 | 1% | 0,017% | 0,169% | 1,686% | $5.933 | $17.799 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump`
5. Configurar el slippage: 1% (liquidez $1.186.583, consulta 10/10/2026 20:55 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump) y el par en DexScreener (https://dexscreener.com/solana/9BaXguKEacyU48V2zg68v2ou91NakEbxAWWkmxHJRB4z); mint authority / freeze authority: revocada / revocada · holders 2.434 · top-10 0,78% (consulta 10/10/2026 20:55 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump
- Par en DexScreener: https://dexscreener.com/solana/9BaXguKEacyU48V2zg68v2ou91NakEbxAWWkmxHJRB4z
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.434 · top-10 0,78% (consulta 10/10/2026 20:55 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | United States Dividend Fund / USDF | registro de la detección (trending) |
| Mint / contrato | `8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `9BaXguKEacyU48V2zg68v2ou91NakEbxAWWkmxHJRB4z` | DexScreener, al detectar (2 par(es) en la consulta 10/10/2026 20:55 UTC) |
| Deployer | `8Dz6oFSNR3p4dQcVuBQ6BeckCXnJjPcJ4mRTsWfw9nBB` | RugCheck `creator` |
| Par creado | 10/10/2026 11:30 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 9,1 h / 9,1 h / 9,4 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 10/10/2026 20:55 UTC |
| Holders / top-10 | 2.434 / 0,78% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 10/10/2026 20:55 UTC |
| Holders efectivos del top-10 | 4,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 10/10/2026 20:55 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 10/10/2026 20:55 UTC |
| Links | DexScreener: https://dexscreener.com/solana/9BaXguKEacyU48V2zg68v2ou91NakEbxAWWkmxHJRB4z · Solscan: https://solscan.io/token/8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump · pump.fun: https://pump.fun/coin/8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump · web / Telegram / X: no publicados en DexScreener | consulta 10/10/2026 20:55 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 10/10/2026 20:55 UTC)
- **Historia:**
  - Par creado el 10/10/2026 11:30 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 10/10/2026 20:38 UTC, con el par a 9,1 h de creado: precio $0,1805, mcap $180.562.169, liquidez $1.182.850.
  - Velas de 1 h de GeckoTerminal (10, desde 10/10/2026 11:00 UTC): apertura $0,1575 · máximo $0,1815 (10/10/2026 20:00 UTC) · mínimo $0,00004551 (10/10/2026 11:00 UTC) · último cierre $0,1815.
  - En la consulta 10/10/2026 20:55 UTC: precio $0,1814, liquidez $1.186.583, FDV $181.482.695.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 10/10/2026 20:38 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1805 |
| Liquidez | $1.182.850 |
| MCap | $180.562.169 |
| Volumen 24 h | $820.430 |
| Cambio 24 h | +396.675% |
| Cambio m5 / h1 | +0,1% / +1,1% |
| Volumen m5 / h1 | $2.475 / $31.151 |
| Trades m5 (compras / ventas) | 51 / 10 |
| Edad del par | 9,1 h |
| Score del feed (WS) | 89 |

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
| Score del feed | score WS × 0,3 | WS 89 × 0,3 | +26,8 |
| MCap | ≥ $1M | $180.562.169 | +25 |
| Volumen 24 h | ≥ $100K | $820.430 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 84% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,1% · h1 +1,1% | +20 |
| Volumen m5 | > $1K (par maduro) | $2.475 | +10 |
| Liquidez | ≥ $100K | $1.182.850 | +15 |
| Cambio 24 h | ≥ +50% | +396.675% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +396.675% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **96** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-10T20:38:06+00:00, sin estado previo): **96** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 45 de 27.926 tokens analizados (0,16%) quedan ≥ 56. Con score 96, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 10/10/2026 20:38 UTC, hasta 12/10/2026 20:38 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +0,1% · h1 +1,1% · h24 +396.675% · volumen m5/h1 0,08 · edad del par 9,1 h.
- **Precio de entrada** (alerta): $0,1805.
- **Consulta 10/10/2026 20:55 UTC:** $0,1814 (+0,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump_2026-10-10_203806.json` · blob `339867a44424ce79a43c953a3d97ca44304387c2` · commit `4f7de7e` (2026-10-10T20:48:52Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-10_203120.json` · blob `9daa9e46fa7616d78d0953347eb89c3463f9d87c` · commit `4f7de7e` (2026-10-10T20:48:52Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-10_203806`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump · registro · 10/10/2026 20:38 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump · HTTP 200 · 10/10/2026 20:55 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump/report · HTTP 200 · 10/10/2026 20:55 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump · HTTP 200 · 10/10/2026 20:55 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/9BaXguKEacyU48V2zg68v2ou91NakEbxAWWkmxHJRB4z/ohlcv/hour?limit=1000 · HTTP 200 · 10/10/2026 20:55 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump · HTTP 404 · 10/10/2026 20:55 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=USDFUSDT · HTTP 400 · 10/10/2026 20:55 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/USDF-USD · HTTP 404 · 10/10/2026 20:55 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.186.583 vs $1.186.672 → 0,01%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1814 vs $0,1815 → 0,04%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump_2026-10-10_203806.json',encoding='utf-8'));d=d.get('8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump',d);p=mock.patch('time.time',return_value=1791664686);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8mJMvhVU1SKfvqiDr5TmF4UXE6DqBMLGNy9Hr71xpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 10/10/2026 20:55 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `506881a7a4641aaf…`
