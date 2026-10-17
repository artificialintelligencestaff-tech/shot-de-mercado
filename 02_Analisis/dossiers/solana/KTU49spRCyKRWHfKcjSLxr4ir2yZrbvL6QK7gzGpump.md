# XTO (XTO) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,4211 · liquidez $1.755.814 · mcap $421.115.553 (al detectar)  
Detectado el 17/10/2026 14:21 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 95, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 19/10/2026 14:21 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir XTO

Estudio de cómo se adquiere XTO, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 17/10/2026 14:48 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 17/10/2026 14:21 UTC | pumpswap `7ix8yMJ…JPy2` | $1.755.814 | 1% | 0,011% | 0,114% | 1,139% | $8.779 | $26.337 |
| consulta 17/10/2026 14:48 UTC | pumpswap `7ix8yMJ…JPy2` | $1.785.078 | 1% | 0,011% | 0,112% | 1,120% | $8.925 | $26.776 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump`
5. Configurar el slippage: 1% (liquidez $1.785.078, consulta 17/10/2026 14:48 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump) y el par en DexScreener (https://dexscreener.com/solana/7ix8yMJsoCYsXgGjRjx7zPCQumGiBVotNUYSoMYuJPy2); mint authority / freeze authority: revocada / revocada · holders 2.907 · top-10 2,23% (consulta 17/10/2026 14:48 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump
- Par en DexScreener: https://dexscreener.com/solana/7ix8yMJsoCYsXgGjRjx7zPCQumGiBVotNUYSoMYuJPy2
- Página del lanzamiento (pump.fun): https://pump.fun/coin/KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.907 · top-10 2,23% (consulta 17/10/2026 14:48 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | XTO / XTO | registro de la detección (trending) |
| Mint / contrato | `KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7ix8yMJsoCYsXgGjRjx7zPCQumGiBVotNUYSoMYuJPy2` | DexScreener, al detectar (1 par(es) en la consulta 17/10/2026 14:48 UTC) |
| Deployer | `antQCwaXM6g7Ag3Sb1XTmsoLKMUbQfLT33VvW7r8vyM` | RugCheck `creator` |
| Par creado | 16/10/2026 02:13 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 36,1 h / 36,1 h / 36,6 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 17/10/2026 14:48 UTC |
| Holders / top-10 | 2.907 / 2,23% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 17/10/2026 14:48 UTC |
| Holders efectivos del top-10 | 2,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 17/10/2026 14:48 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 17/10/2026 14:48 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7ix8yMJsoCYsXgGjRjx7zPCQumGiBVotNUYSoMYuJPy2 · Solscan: https://solscan.io/token/KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump · pump.fun: https://pump.fun/coin/KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump · web / Telegram / X: no publicados en DexScreener | consulta 17/10/2026 14:48 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 17/10/2026 14:48 UTC)
- **Historia:**
  - Par creado el 16/10/2026 02:13 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 17/10/2026 14:21 UTC, con el par a 36,1 h de creado: precio $0,4211, mcap $421.115.553, liquidez $1.755.814.
  - Velas de 1 h de GeckoTerminal (37, desde 16/10/2026 02:00 UTC): apertura $0,1519 · máximo $0,4346 (17/10/2026 14:00 UTC) · mínimo $0,00004377 (16/10/2026 02:00 UTC) · último cierre $0,4346.
  - En la consulta 17/10/2026 14:48 UTC: precio $0,4344, liquidez $1.785.078, FDV $434.487.116.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 17/10/2026 14:21 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,4211 |
| Liquidez | $1.755.814 |
| MCap | $421.115.553 |
| Volumen 24 h | $381.238 |
| Cambio 24 h | +102% |
| Cambio m5 / h1 | +0,6% / +5,9% |
| Volumen m5 / h1 | $3.232 / $39.349 |
| Trades m5 (compras / ventas) | 15 / 4 |
| Edad del par | 36,1 h |
| Score del feed (WS) | 84 |

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

Desglose reconstruido desde los motivos registrados; suma 95 = score registrado 95 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 84 × 0,3 | +25,3 |
| MCap | ≥ $1M | $421.115.553 | +25 |
| Volumen 24 h | ≥ $100K | $381.238 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 79% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,6% · h1 +5,9% | +20 |
| Volumen m5 | > $1K (par maduro) | $3.232 | +10 |
| Par viejo | edad > 24 h | edad 36,1 h | -50 |
| Liquidez | ≥ $100K | $1.755.814 | +15 |
| Cambio 24 h | ≥ +50% | +102% | +10 |
| **Total** | recortado a 0–100 |  | **95** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-17T14:21:07+00:00, sin estado previo): **95** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Par >24h, no nativo pump.fun, Liquidez alta, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 63 de 38.431 tokens analizados (0,16%) quedan ≥ 56. Con score 95, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 17/10/2026 14:21 UTC, hasta 19/10/2026 14:21 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +0,6% · h1 +5,9% · h24 +102% · volumen m5/h1 0,08 · edad del par 36,1 h.
- **Precio de entrada** (alerta): $0,4211.
- **Consulta 17/10/2026 14:48 UTC:** $0,4344 (+3,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump_2026-10-17_142107.json` · blob `66693b173a9c5a6378474db825a6211bdf4fef03` · commit `b294c83` (2026-10-17T14:42:13Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-17_141442.json` · blob `905bde6c332634bce05193bec57c1e5f4892d677` · commit `b294c83` (2026-10-17T14:42:13Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-17_142107`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump · registro · 17/10/2026 14:21 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump · HTTP 200 · 17/10/2026 14:48 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump/report · HTTP 200 · 17/10/2026 14:48 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump · HTTP 200 · 17/10/2026 14:48 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7ix8yMJsoCYsXgGjRjx7zPCQumGiBVotNUYSoMYuJPy2/ohlcv/hour?limit=1000 · HTTP 200 · 17/10/2026 14:48 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump · HTTP 404 · 17/10/2026 14:48 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=XTOUSDT · HTTP 400 · 17/10/2026 14:48 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/XTO-USD · HTTP 404 · 17/10/2026 14:48 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.785.078 vs $1.783.296 → 0,10%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,4344 vs $0,4346 → 0,05%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump_2026-10-17_142107.json',encoding='utf-8'));d=d.get('KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump',d);p=mock.patch('time.time',return_value=1792246867);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint KTU49spRCyKRWHfKcjSLxr4ir2yZrbvL6QK7gzGpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 17/10/2026 14:48 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `a8a2b1d80caf7448…`
