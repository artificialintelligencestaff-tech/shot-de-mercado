# Bambi (Bambi) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00004623 · liquidez $17.893 · mcap $46.235 (al detectar)  
Detectado el 06/10/2026 12:56 UTC por: young-0.4 · edad 13.2 min · pesos info 58 / estructura 21 / precio 21 · info 19.1 · estructura 13.1 · precio/volumen 7.4 · cobertura 93/100, [info] narrative_wave: ola 'bambi': 6 lanzamientos más en 1 h → +10.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +5.2 (score 40, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 08/10/2026 12:56 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Bambi

Estudio de cómo se adquiere Bambi, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 13:17 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 12:56 UTC | pumpswap `6gNDWBo…SYPE` | $17.893 | 10% | 1,118% | 11,178% | 111,777% | $89 | $268 |
| consulta 06/10/2026 13:16 UTC | pumpswap `6gNDWBo…SYPE` | $12.469 | 10% | 1,604% | 16,040% | 160,402% | $62 | $187 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr`
5. Configurar el slippage: 10% (liquidez $12.469, consulta 06/10/2026 13:16 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr) y el par en DexScreener (https://dexscreener.com/solana/6gNDWBoNYGDnehP7UCd2ACerbk2gci6samZjaktjSYPE); mint authority / freeze authority: revocada / revocada · holders 1.472 · top-10 53,29% (consulta 06/10/2026 13:16 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr
- Par en DexScreener: https://dexscreener.com/solana/6gNDWBoNYGDnehP7UCd2ACerbk2gci6samZjaktjSYPE
- Página del lanzamiento (pump.fun): https://pump.fun/coin/B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.472 · top-10 53,29% (consulta 06/10/2026 13:16 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Bambi / Bambi | registro de la detección (pumpportal_live) |
| Mint / contrato | `B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6gNDWBoNYGDnehP7UCd2ACerbk2gci6samZjaktjSYPE` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 13:16 UTC) |
| Deployer | `DR87kHASwvyZXmRgRsZ33aaVzGpMQGsU5AKohx6kh5j1` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 12:42 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 13,2 min / 13,2 min / 34,2 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 13:16 UTC |
| Holders / top-10 | 1.472 / 53,29% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 13:16 UTC |
| Holders efectivos del top-10 | 2,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 13:16 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 13:16 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6gNDWBoNYGDnehP7UCd2ACerbk2gci6samZjaktjSYPE · Solscan: https://solscan.io/token/B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr · pump.fun: https://pump.fun/coin/B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr · web: https://x.com/dreeamberry/status/2106721246314635457 · twitter: https://x.com/Infinitidigits/status/2107454135989588293?s=20 | consulta 06/10/2026 13:16 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 13:16 UTC)
- **Historia:**
  - Par creado el 06/10/2026 12:42 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 12:56 UTC, con el par a 13,2 min de creado: precio $0,00004623, mcap $46.235, liquidez $17.893.
  - Velas de 1 h de GeckoTerminal (2, desde 06/10/2026 12:00 UTC): apertura $0,00004939 · máximo $0,00009566 (06/10/2026 12:00 UTC) · mínimo $0,00001272 (06/10/2026 13:00 UTC) · último cierre $0,00002474.
  - En la consulta 06/10/2026 13:16 UTC: precio $0,00002448, liquidez $12.469, FDV $24.484.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 12:56 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00004623 |
| Liquidez | $17.893 |
| MCap | $46.235 |
| Volumen 24 h | $188.936 |
| Cambio 24 h | -5% |
| Cambio m5 / h1 | -37,8% / -4,6% |
| Volumen m5 / h1 | $51.520 / $188.936 |
| Trades m5 (compras / ventas) | 629 / 534 |
| Edad del par | 13,2 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 40; motivos sin regla: young-0.4 · edad 13.2 min · pesos info 58 / estructura 21 / precio 21 · info 19.1 · estructura 13.1 · precio/volumen 7.4 · cobertura 93/100, [info] narrative_wave: ola 'bambi': 6 lanzamientos más en 1 h → +10.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +5.2, [info] dex_profile: perfil pago en DexScreener → +2.9, [estructura] bonding_progress: graduado (pumpswap) → +10.0, [estructura] holders_struct: holders 1323 · top-10 39.8 % → +2.5, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1323/3878 = 0.34 → +0.6, [precio/volumen] volume_acceleration: vol 5 min ×3.3 la tasa horaria (s 0.71), [precio/volumen] liquidity_inflow: liquidez +2% en 8 min (s 0.08), [precio/volumen] holder_accumulation: holders 1011→1323 (+52.0/min) · top10 35.8%→39.8% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=17892.73, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 40 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T12:56:06+00:00, sin estado previo): **15** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 18 de 15.441 tokens analizados (0,12%) quedan ≥ 56. Con score 15, este activo queda en el percentil 97,3 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 12:56 UTC, hasta 08/10/2026 12:56 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -37,8% · h1 -4,6% · h24 -5% · volumen m5/h1 0,27 · edad del par 13,2 min.
- **Precio de entrada** (alerta): $0,00004623.
- **Consulta 06/10/2026 13:16 UTC:** $0,00002448 (-47,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr_2026-10-06_125606.json` · blob `312844fab116915a8447eb10c7f278c09d17424d` · commit `3688ec6` (2026-10-06T13:10:09Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_125606`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr · registro · 06/10/2026 12:56 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr · HTTP 200 · 06/10/2026 13:16 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr/report · HTTP 200 · 06/10/2026 13:16 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr · HTTP 200 · 06/10/2026 13:16 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6gNDWBoNYGDnehP7UCd2ACerbk2gci6samZjaktjSYPE/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 13:16 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr · HTTP 404 · 06/10/2026 13:16 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BAMBIUSDT · HTTP 400 · 06/10/2026 13:16 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BAMBI-USD · HTTP 404 · 06/10/2026 13:16 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $12.469 vs $12.443 → 0,20%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00002448 vs $0,00002474 → 1,06%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr_2026-10-06_125606.json',encoding='utf-8'));d=d.get('B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr',d);p=mock.patch('time.time',return_value=1791291366);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint B6hNoE798PE1y2XTZMC2XX333HRcZiD9RZ3xzCRbeoQr --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 13:17 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `33b7584431535f99…`
