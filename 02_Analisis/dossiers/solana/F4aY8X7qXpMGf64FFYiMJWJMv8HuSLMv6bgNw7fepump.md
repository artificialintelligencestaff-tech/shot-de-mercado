# mini baton (MINIBATON) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0007326 · liquidez $79.897 · mcap $730.008 (al detectar)  
Detectado el 08/10/2026 23:36 UTC por: MCap > $100K, Volumen masivo, Buy pressure >60% (score 99, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 10/10/2026 23:36 UTC (< 48 h) · vigente: quedan 47,3 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir MINIBATON

Estudio de cómo se adquiere MINIBATON, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 09/10/2026 00:15 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/10/2026 23:36 UTC | pumpswap `8KxF1PC…KWSh` | $79.897 | 5% | 0,250% | 2,503% | 25,032% | $399 | $1.198 |
| consulta 09/10/2026 00:15 UTC | pumpswap `8KxF1PC…KWSh` | $2.954 | 10% | 6,771% | 67,713% | 677,133% | $15 | $44 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump`
5. Configurar el slippage: 10% (liquidez $2.954, consulta 09/10/2026 00:15 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump) y el par en DexScreener (https://dexscreener.com/solana/8KxF1PCfWkS82uarKVhrkm2cycCoooxjz7JvabmLKWSh); mint authority / freeze authority: revocada / revocada · holders 1.939 · top-10 97,54% (consulta 09/10/2026 00:15 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump
- Par en DexScreener: https://dexscreener.com/solana/8KxF1PCfWkS82uarKVhrkm2cycCoooxjz7JvabmLKWSh
- Página del lanzamiento (pump.fun): https://pump.fun/coin/F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.939 · top-10 97,54% (consulta 09/10/2026 00:15 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | mini baton / MINIBATON | registro de la detección (pumpportal) |
| Mint / contrato | `F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `8KxF1PCfWkS82uarKVhrkm2cycCoooxjz7JvabmLKWSh` | DexScreener, al detectar (2 par(es) en la consulta 09/10/2026 00:15 UTC) |
| Deployer | `5CsaTuNYFkCxPdnyaeDZJufgAPxtf6BG3Hc2FckFVsMJ` | PumpPortal (evento create), al detectar |
| Par creado | 08/10/2026 22:36 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,1 min / 60,1 min / 99,2 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 09/10/2026 00:15 UTC |
| Holders / top-10 | 1.939 / 97,54% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 09/10/2026 00:15 UTC |
| Holders efectivos del top-10 | 1,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 09/10/2026 00:15 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 09/10/2026 00:15 UTC |
| Links | DexScreener: https://dexscreener.com/solana/8KxF1PCfWkS82uarKVhrkm2cycCoooxjz7JvabmLKWSh · Solscan: https://solscan.io/token/F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump · pump.fun: https://pump.fun/coin/F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump · web: https://www.minibaton.com · twitter: https://x.com/i/communities/1952967635538460677 · telegram: https://t.me/minibaton_memes | consulta 09/10/2026 00:15 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 09/10/2026 00:15 UTC)
- **Historia:**
  - Par creado el 08/10/2026 22:36 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/10/2026 23:36 UTC, con el par a 60,1 min de creado: precio $0,0007326, mcap $730.008, liquidez $79.897.
  - Velas de 1 h de GeckoTerminal (3, desde 08/10/2026 22:00 UTC): apertura $0,00006965 · máximo $0,0009290 (08/10/2026 22:00 UTC) · mínimo $0,000002639 (09/10/2026 00:00 UTC) · último cierre $0,000002639.
  - En la consulta 09/10/2026 00:15 UTC: precio $0,000002664, liquidez $2.954, FDV $2.655.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/10/2026 23:36 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0007326 |
| Liquidez | $79.897 |
| MCap | $730.008 |
| Volumen 24 h | $2.433.702 |
| Cambio 24 h | +953% |
| Cambio m5 / h1 | -8,2% / +80,9% |
| Volumen m5 / h1 | $66.548 / $2.360.815 |
| Trades m5 (compras / ventas) | 17.942 / 2.387 |
| Edad del par | 60,1 min |
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

Desglose no reproducible desde los motivos registrados (suma 98 vs score 99; motivos sin regla: Anticipación (lib_early_signals early-0.2): +1 — buy_pressure_shift: compras 88% en 5 min vs 85% en 1 h → +0.36; liquidity_inflow: liquidez +14% en 8 min → +0.95): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-08T23:36:46+00:00, sin estado previo): **98** · motivos: MCap > $100K, Volumen masivo, Buy pressure >60%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=10.9% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 40 de 23.599 tokens analizados (0,17%) quedan ≥ 56. Con score 98, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/10/2026 23:36 UTC, hasta 10/10/2026 23:36 UTC · vigente: quedan 47,3 h.
- **Aceleración al detectar:** cambio m5 -8,2% · h1 +80,9% · h24 +953% · volumen m5/h1 0,03 · edad del par 60,1 min.
- **Precio de entrada** (alerta): $0,0007326.
- **Consulta 09/10/2026 00:15 UTC:** $0,000002664 (-99,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump_2026-10-08_233646.json` · blob `096c87e54c1fabca371c2decd9e721883d0f7366` · commit `0deaff5` (2026-10-09T00:08:07Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-08_233646`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump · registro · 08/10/2026 23:36 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump · HTTP 200 · 09/10/2026 00:15 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump/report · HTTP 200 · 09/10/2026 00:15 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump · HTTP 200 · 09/10/2026 00:15 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/8KxF1PCfWkS82uarKVhrkm2cycCoooxjz7JvabmLKWSh/ohlcv/hour?limit=1000 · HTTP 200 · 09/10/2026 00:15 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump · HTTP 404 · 09/10/2026 00:15 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MINIBATONUSDT · HTTP 400 · 09/10/2026 00:15 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MINIBATON-USD · HTTP 404 · 09/10/2026 00:15 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.954 vs $2.933 → 0,71%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002664 vs $0,000002639 → 0,94%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump_2026-10-08_233646.json',encoding='utf-8'));d=d.get('F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump',d);p=mock.patch('time.time',return_value=1791502606);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint F4aY8X7qXpMGf64FFYiMJWJMv8HuSLMv6bgNw7fepump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 09/10/2026 00:15 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `33fb45aa58a5a463…`
