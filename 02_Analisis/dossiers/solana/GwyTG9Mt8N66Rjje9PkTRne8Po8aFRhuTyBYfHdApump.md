# French Goku Hero (PIERRE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00008058 · liquidez $23.243 · mcap $80.589 (al detectar)  
Detectado el 18/10/2026 20:44 UTC por: young-0.4 · edad 12.2 min · pesos info 59 / estructura 21 / precio 21 · info 17.3 · estructura 12.8 · precio/volumen 12.4 · cobertura 93/100, [info] narrative_wave: ola 'french': 26 lanzamientos más en 1 h → +14.7, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.6 (score 43, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 20/10/2026 20:44 UTC (< 48 h) · vigente: quedan 47,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir PIERRE

Estudio de cómo se adquiere PIERRE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 18/10/2026 21:19 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 18/10/2026 20:44 UTC | pumpswap `Aj8fhav…pcyo` | $23.243 | 10% | 0,860% | 8,605% | 86,049% | $116 | $349 |
| consulta 18/10/2026 21:19 UTC | pumpswap `Aj8fhav…pcyo` | $16.166 | 10% | 1,237% | 12,371% | 123,713% | $81 | $242 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump`
5. Configurar el slippage: 10% (liquidez $16.166, consulta 18/10/2026 21:19 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump) y el par en DexScreener (https://dexscreener.com/solana/Aj8fhavw2WhvBZrhFppHgXrgnJB5wSWroAAoJ8Ahpcyo); mint authority / freeze authority: revocada / revocada · holders 2.396 · top-10 46,59% (consulta 18/10/2026 21:19 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump
- Par en DexScreener: https://dexscreener.com/solana/Aj8fhavw2WhvBZrhFppHgXrgnJB5wSWroAAoJ8Ahpcyo
- Página del lanzamiento (pump.fun): https://pump.fun/coin/GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.396 · top-10 46,59% (consulta 18/10/2026 21:19 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | French Goku Hero / PIERRE | registro de la detección (pumpportal_live) |
| Mint / contrato | `GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Aj8fhavw2WhvBZrhFppHgXrgnJB5wSWroAAoJ8Ahpcyo` | DexScreener, al detectar (2 par(es) en la consulta 18/10/2026 21:19 UTC) |
| Deployer | `9mB1kqCLfb4CvG8sWihkJBhZ7WREKQ9VdjFGvDmwJBgy` | PumpPortal (evento create), al detectar |
| Par creado | 18/10/2026 20:32 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 12,2 min / 12,2 min / 46,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 18/10/2026 21:19 UTC |
| Holders / top-10 | 2.396 / 46,59% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 18/10/2026 21:19 UTC |
| Holders efectivos del top-10 | 3,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 18/10/2026 21:19 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 18/10/2026 21:19 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Aj8fhavw2WhvBZrhFppHgXrgnJB5wSWroAAoJ8Ahpcyo · Solscan: https://solscan.io/token/GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump · pump.fun: https://pump.fun/coin/GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump · twitter: https://x.com/oogwaychain/status/2111917619217678441 | consulta 18/10/2026 21:19 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 18/10/2026 21:19 UTC)
- **Historia:**
  - Par creado el 18/10/2026 20:32 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 18/10/2026 20:44 UTC, con el par a 12,2 min de creado: precio $0,00008058, mcap $80.589, liquidez $23.243.
  - Velas de 1 h de GeckoTerminal (2, desde 18/10/2026 20:00 UTC): apertura $0,00004085 · máximo $0,0001030 (18/10/2026 20:00 UTC) · mínimo $0,00001477 (18/10/2026 21:00 UTC) · último cierre $0,00003499.
  - En la consulta 18/10/2026 21:19 UTC: precio $0,00003896, liquidez $16.166, FDV $37.164.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 18/10/2026 20:44 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00008058 |
| Liquidez | $23.243 |
| MCap | $80.589 |
| Volumen 24 h | $427.340 |
| Cambio 24 h | +92% |
| Cambio m5 / h1 | +20,8% / +92,2% |
| Volumen m5 / h1 | $154.960 / $427.340 |
| Trades m5 (compras / ventas) | 1.517 / 1.201 |
| Edad del par | 12,2 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 43; motivos sin regla: young-0.4 · edad 12.2 min · pesos info 59 / estructura 21 / precio 21 · info 17.3 · estructura 12.8 · precio/volumen 12.4 · cobertura 93/100, [info] narrative_wave: ola 'french': 26 lanzamientos más en 1 h → +14.7, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.6, [estructura] bonding_progress: graduado (pumpswap) → +9.9, [estructura] holders_struct: holders 1673 · top-10 36.4 % → +2.5, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1673/7948 = 0.21 → +0.3, [precio/volumen] volume_acceleration: vol 5 min ×4.4 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 56% en 5 min vs 53% en 1 h (s 0.12), [precio/volumen] liquidity_inflow: liquidez +82% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1049→1673 (+104.0/min) · top10 48.2%→36.4% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=23242.66, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 43 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-18T20:44:56+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 64 de 40.132 tokens analizados (0,16%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 18/10/2026 20:44 UTC, hasta 20/10/2026 20:44 UTC · vigente: quedan 47,4 h.
- **Aceleración al detectar:** cambio m5 +20,8% · h1 +92,2% · h24 +92% · volumen m5/h1 0,36 · edad del par 12,2 min.
- **Precio de entrada** (alerta): $0,00008058.
- **Consulta 18/10/2026 21:19 UTC:** $0,00003896 (-51,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump_2026-10-18_204456.json` · blob `d8f002852f2849e889949337a97c777a15d6e691` · commit `2338440` (2026-10-18T21:08:35Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-18_204456`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump · registro · 18/10/2026 20:44 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump · HTTP 200 · 18/10/2026 21:19 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump/report · HTTP 200 · 18/10/2026 21:19 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump · HTTP 200 · 18/10/2026 21:19 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Aj8fhavw2WhvBZrhFppHgXrgnJB5wSWroAAoJ8Ahpcyo/ohlcv/hour?limit=1000 · HTTP 200 · 18/10/2026 21:19 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump · HTTP 404 · 18/10/2026 21:19 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=PIERREUSDT · HTTP 400 · 18/10/2026 21:19 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/PIERRE-USD · HTTP 404 · 18/10/2026 21:19 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $16.166 vs $15.571 → 3,69%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00003896 vs $0,00003499 → 10,19%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump_2026-10-18_204456.json',encoding='utf-8'));d=d.get('GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump',d);p=mock.patch('time.time',return_value=1792356296);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint GwyTG9Mt8N66Rjje9PkTRne8Po8aFRhuTyBYfHdApump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 18/10/2026 21:19 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `3165921484cb5e71…`
