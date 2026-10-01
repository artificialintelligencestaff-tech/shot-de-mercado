# silent market (silent) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000003259 · liquidez $3.332 · mcap $3.209 (al detectar)  
Detectado el 01/10/2026 22:45 UTC por: MCap bajo, Volumen alto, Volumen en aceleración (5m/1h > 25%) (score 58, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 03/10/2026 22:45 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir silent

Estudio de cómo se adquiere silent, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 01/10/2026 22:54 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 01/10/2026 22:45 UTC | pumpswap `2bzfurG…vBYS` | $3.332 | 10% | 6,003% | 60,028% | 600,280% | $17 | $50 |
| consulta 01/10/2026 22:54 UTC | pumpswap `2bzfurG…vBYS` | $3.320 | 10% | 6,024% | 60,242% | 602,421% | $17 | $50 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump`
5. Configurar el slippage: 10% (liquidez $3.320, consulta 01/10/2026 22:54 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump) y el par en DexScreener (https://dexscreener.com/solana/2bzfurGrmWhEXHpLggzGoJmt4hjHu7EQubtByVrdvBYS); mint authority / freeze authority: revocada / revocada · holders 1.750 · top-10 93,19% (consulta 01/10/2026 22:54 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump
- Par en DexScreener: https://dexscreener.com/solana/2bzfurGrmWhEXHpLggzGoJmt4hjHu7EQubtByVrdvBYS
- Página del lanzamiento (pump.fun): https://pump.fun/coin/ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.750 · top-10 93,19% (consulta 01/10/2026 22:54 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | silent market / silent | registro de la detección (pumpportal) |
| Mint / contrato | `ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `2bzfurGrmWhEXHpLggzGoJmt4hjHu7EQubtByVrdvBYS` | DexScreener, al detectar (3 par(es) en la consulta 01/10/2026 22:54 UTC) |
| Deployer | `ETovJryEDLbk4jt7a48hkE8TgCoxJPnPRXvK58qMbYV4` | PumpPortal (evento create), al detectar |
| Par creado | 01/10/2026 18:40 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 4,1 h / 4,1 h / 4,2 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 01/10/2026 22:54 UTC |
| Holders / top-10 | 1.750 / 93,19% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 01/10/2026 22:54 UTC |
| Holders efectivos del top-10 | 1,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 01/10/2026 22:54 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 01/10/2026 22:54 UTC |
| Links | DexScreener: https://dexscreener.com/solana/2bzfurGrmWhEXHpLggzGoJmt4hjHu7EQubtByVrdvBYS · Solscan: https://solscan.io/token/ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump · pump.fun: https://pump.fun/coin/ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump · web: https://silentmarket.lol · twitter: https://x.com/silentmrkt | consulta 01/10/2026 22:54 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 01/10/2026 22:54 UTC)
- **Historia:**
  - Par creado el 01/10/2026 18:40 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 01/10/2026 22:45 UTC, con el par a 4,1 h de creado: precio $0,000003259, mcap $3.209, liquidez $3.332.
  - Velas de 1 h de GeckoTerminal (5, desde 01/10/2026 18:00 UTC): apertura $0,00005225 · máximo $0,0003042 (01/10/2026 18:00 UTC) · mínimo $0,000003248 (01/10/2026 21:00 UTC) · último cierre $0,000003253.
  - En la consulta 01/10/2026 22:54 UTC: precio $0,000003247, liquidez $3.320, FDV $3.197.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 01/10/2026 22:45 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000003259 |
| Liquidez | $3.332 |
| MCap | $3.209 |
| Volumen 24 h | $711.509 |
| Cambio 24 h | -93% |
| Cambio m5 / h1 | +0,2% / +0,2% |
| Volumen m5 / h1 | $4 / $9 |
| Trades m5 (compras / ventas) | 1 / 1 |
| Edad del par | 4,1 h |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 1/1 (100,0%, IC90 27,0%–100,0%) · secundaria 0/0 resueltas (shadow_monitor.json).

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

Desglose no reproducible desde los motivos registrados (suma 55 vs score 58; motivos sin regla: Anticipación (lib_early_signals early-0.2): +3 — volume_acceleration: vol 5 min ×5.7 la tasa horaria → +3; liquidity_inflow: liquidez +0% en 8 min → +0.01): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-01T22:45:03+00:00, sin estado previo): **55** · motivos: MCap bajo, Volumen alto, Volumen en aceleración (5m/1h > 25%), Trades en aceleración (5m/1h > 25%), Momentum corto+medio positivo, Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 6 de 6.152 tokens analizados (0,10%) quedan ≥ 56. Con score 55, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 01/10/2026 22:45 UTC, hasta 03/10/2026 22:45 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +0,2% · h1 +0,2% · h24 -93% · volumen m5/h1 0,47 · edad del par 4,1 h.
- **Precio de entrada** (alerta): $0,000003259.
- **Consulta 01/10/2026 22:54 UTC:** $0,000003247 (-0,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump_2026-10-01_224503.json` · blob `5ddeca25acd46d9d9cccb82c7be9a7b88affe3af` · commit `b1cab79` (2026-10-01T22:47:41Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-01_224503`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump · registro · 01/10/2026 22:45 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump · HTTP 200 · 01/10/2026 22:54 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump/report · HTTP 200 · 01/10/2026 22:54 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump · HTTP 200 · 01/10/2026 22:54 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/2bzfurGrmWhEXHpLggzGoJmt4hjHu7EQubtByVrdvBYS/ohlcv/hour?limit=1000 · HTTP 200 · 01/10/2026 22:54 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump · HTTP 404 · 01/10/2026 22:54 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SILENTUSDT · HTTP 400 · 01/10/2026 22:54 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SILENT-USD · HTTP 404 · 01/10/2026 22:54 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.320 vs $3.327 → 0,22%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000003247 vs $0,000003253 → 0,17%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump_2026-10-01_224503.json',encoding='utf-8'));d=d.get('ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump',d);p=mock.patch('time.time',return_value=1790894703);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint ELEnRRcKCuuPJBJPeTTGCRocjkBCwbd3R3f8nyg8pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 01/10/2026 22:54 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `5d07e96a63aba53f…`
