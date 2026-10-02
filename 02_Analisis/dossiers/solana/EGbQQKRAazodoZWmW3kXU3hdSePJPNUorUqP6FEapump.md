# Nike (Nike) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001013 · liquidez $90.525 · mcap $1.013.373 (al detectar)  
Detectado el 02/10/2026 16:57 UTC por: MCap > $1M, Volumen decente, Liquidez decente (score 56, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 04/10/2026 16:57 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Nike

Estudio de cómo se adquiere Nike, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 17:12 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 16:57 UTC | pumpswap `2My8oz4…3Enm` | $90.525 | 5% | 0,221% | 2,209% | 22,093% | $453 | $1.358 |
| consulta 02/10/2026 17:12 UTC | pumpswap `2My8oz4…3Enm` | $118.922 | 5% | 0,168% | 1,682% | 16,818% | $595 | $1.784 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump`
5. Configurar el slippage: 5% (liquidez $118.922, consulta 02/10/2026 17:12 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump) y el par en DexScreener (https://dexscreener.com/solana/2My8oz4hmAqivPK3UBKgHzbpodntUXuu7KEzAw2Q3Enm); mint authority / freeze authority: revocada / revocada · holders 2.390 · top-10 17,35% (consulta 02/10/2026 17:12 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump
- Par en DexScreener: https://dexscreener.com/solana/2My8oz4hmAqivPK3UBKgHzbpodntUXuu7KEzAw2Q3Enm
- Página del lanzamiento (pump.fun): https://pump.fun/coin/EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.390 · top-10 17,35% (consulta 02/10/2026 17:12 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Nike / Nike | registro de la detección (pumpportal_live) |
| Mint / contrato | `EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `2My8oz4hmAqivPK3UBKgHzbpodntUXuu7KEzAw2Q3Enm` | DexScreener, al detectar (1 par(es) en la consulta 02/10/2026 17:12 UTC) |
| Deployer | `FPjszoHzqYiUhLbuziPk74GaaZHbCNn9h9DaZibnkYkx` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 16:35 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 22,4 min / 22,4 min / 37,0 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 17:12 UTC |
| Holders / top-10 | 2.390 / 17,35% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 17:12 UTC |
| Holders efectivos del top-10 | 1,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 17:12 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 17:12 UTC |
| Links | DexScreener: https://dexscreener.com/solana/2My8oz4hmAqivPK3UBKgHzbpodntUXuu7KEzAw2Q3Enm · Solscan: https://solscan.io/token/EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump · pump.fun: https://pump.fun/coin/EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump · web / Telegram / X: no publicados en DexScreener | consulta 02/10/2026 17:12 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 17:12 UTC)
- **Historia:**
  - Par creado el 02/10/2026 16:35 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 16:57 UTC, con el par a 22,4 min de creado: precio $0,001013, mcap $1.013.373, liquidez $90.525.
  - Velas de 1 h de GeckoTerminal (2, desde 02/10/2026 16:00 UTC): apertura $0,0004081 · máximo $0,001759 (02/10/2026 17:00 UTC) · mínimo $0,00004982 (02/10/2026 16:00 UTC) · último cierre $0,001756.
  - En la consulta 02/10/2026 17:12 UTC: precio $0,001730, liquidez $118.922, FDV $1.730.034.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 16:57 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001013 |
| Liquidez | $90.525 |
| MCap | $1.013.373 |
| Volumen 24 h | $52.806 |
| Cambio 24 h | +1.934% |
| Cambio m5 / h1 | +21,8% / +1.934,0% |
| Volumen m5 / h1 | $6.047 / $52.806 |
| Trades m5 (compras / ventas) | 948 / 1.346 |
| Edad del par | 22,4 min |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 1/2 (50,0%, IC90 12,1%–87,9%) · secundaria 0/1 resueltas (shadow_monitor.json).

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

Desglose no reproducible desde los motivos registrados (suma 55 vs score 56; motivos sin regla: Anticipación (lib_early_signals early-0.2): +1 — liquidity_inflow: liquidez +22% en 8 min → +1.44): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T16:57:36+00:00, sin estado previo): **55** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen decente, Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=8.9% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 9 de 8.158 tokens analizados (0,11%) quedan ≥ 56. Con score 55, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 16:57 UTC, hasta 04/10/2026 16:57 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +21,8% · h1 +1.934,0% · h24 +1.934% · volumen m5/h1 0,11 · edad del par 22,4 min.
- **Precio de entrada** (alerta): $0,001013.
- **Consulta 02/10/2026 17:12 UTC:** $0,001730 (+70,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump_2026-10-02_165736.json` · blob `ffebc1266876413d55c0f220222bddeb69977de9` · commit `cff404a` (2026-10-02T17:03:50Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-02_163314.json` · blob `c5f0adbe2de763894773f50c8b0d6285f984ca38` · commit `cff404a` (2026-10-02T17:03:50Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_165736`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump · registro · 02/10/2026 16:57 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump · HTTP 200 · 02/10/2026 17:12 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump/report · HTTP 200 · 02/10/2026 17:12 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump · HTTP 200 · 02/10/2026 17:12 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/2My8oz4hmAqivPK3UBKgHzbpodntUXuu7KEzAw2Q3Enm/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 17:12 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump · HTTP 404 · 02/10/2026 17:12 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=NIKEUSDT · HTTP 400 · 02/10/2026 17:12 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/NIKE-USD · HTTP 404 · 02/10/2026 17:12 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $118.922 vs $118.624 → 0,25%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001730 vs $0,001756 → 1,50%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump_2026-10-02_165736.json',encoding='utf-8'));d=d.get('EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump',d);p=mock.patch('time.time',return_value=1790960256);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint EGbQQKRAazodoZWmW3kXU3hdSePJPNUorUqP6FEapump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 17:12 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `e38dcebf2350757d…`
