# Lil Caesar (CAESAR) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00007933 · liquidez $24.264 · mcap $79.335 (al detectar)  
Detectado el 06/10/2026 05:01 UTC por: young-0.4 · edad 10.6 min · pesos info 60 / estructura 20 / precio 20 · info 23.2 · estructura 12.6 · precio/volumen 11.1 · cobertura 93/100, [info] narrative_wave: ola 'lil': 9 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +5.3 (score 47, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 08/10/2026 05:01 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir CAESAR

Estudio de cómo se adquiere CAESAR, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 05:12 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 05:01 UTC | pumpswap `9ebYNt7…syGT` | $24.264 | 10% | 0,824% | 8,243% | 82,428% | $121 | $364 |
| consulta 06/10/2026 05:12 UTC | pumpswap `9ebYNt7…syGT` | $31.183 | 10% | 0,641% | 6,414% | 64,138% | $156 | $468 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ`
5. Configurar el slippage: 10% (liquidez $31.183, consulta 06/10/2026 05:12 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ) y el par en DexScreener (https://dexscreener.com/solana/9ebYNt7c7aZtaKQS8UPbCT6gdzyXWAje3x8Ca28ysyGT); mint authority / freeze authority: revocada / revocada · holders 2.501 · top-10 29,26% (consulta 06/10/2026 05:12 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ
- Par en DexScreener: https://dexscreener.com/solana/9ebYNt7c7aZtaKQS8UPbCT6gdzyXWAje3x8Ca28ysyGT
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.501 · top-10 29,26% (consulta 06/10/2026 05:12 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Lil Caesar / CAESAR | registro de la detección (pumpportal_live) |
| Mint / contrato | `8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `9ebYNt7c7aZtaKQS8UPbCT6gdzyXWAje3x8Ca28ysyGT` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 05:12 UTC) |
| Deployer | `29yFzeBZgxf5zqrAkKXwgZtQehRf4pL8WbV2nRJikbw8` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 04:51 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,6 min / 10,6 min / 21,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 05:12 UTC |
| Holders / top-10 | 2.501 / 29,26% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 05:12 UTC |
| Holders efectivos del top-10 | 3,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 05:12 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 05:12 UTC |
| Links | DexScreener: https://dexscreener.com/solana/9ebYNt7c7aZtaKQS8UPbCT6gdzyXWAje3x8Ca28ysyGT · Solscan: https://solscan.io/token/8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ · pump.fun: https://pump.fun/coin/8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ · twitter: https://x.com/ddddddd8a/status/2107331999367123380 · instagram: https://www.instagram.com/reels/DZRbzzCTXNN/ | consulta 06/10/2026 05:12 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 05:12 UTC)
- **Historia:**
  - Par creado el 06/10/2026 04:51 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 05:01 UTC, con el par a 10,6 min de creado: precio $0,00007933, mcap $79.335, liquidez $24.264.
  - Velas de 1 h de GeckoTerminal (2, desde 06/10/2026 04:00 UTC): apertura $0,00004943 · máximo $0,0002056 (06/10/2026 05:00 UTC) · mínimo $0,00003276 (06/10/2026 04:00 UTC) · último cierre $0,0001217.
  - En la consulta 06/10/2026 05:12 UTC: precio $0,0001233, liquidez $31.183, FDV $123.329.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 05:01 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00007933 |
| Liquidez | $24.264 |
| MCap | $79.335 |
| Volumen 24 h | $248.574 |
| Cambio 24 h | +60% |
| Cambio m5 / h1 | +6,2% / +60,4% |
| Volumen m5 / h1 | $93.741 / $248.574 |
| Trades m5 (compras / ventas) | 1.353 / 920 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 47; motivos sin regla: young-0.4 · edad 10.6 min · pesos info 60 / estructura 20 / precio 20 · info 23.2 · estructura 12.6 · precio/volumen 11.1 · cobertura 93/100, [info] narrative_wave: ola 'lil': 9 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1654 · top-10 33.5 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1654/5744 = 0.29 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×4.5 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 60% en 5 min vs 57% en 1 h (s 0.13), [precio/volumen] liquidity_inflow: liquidez +20% en 8 min (s 0.66), [precio/volumen] holder_accumulation: holders 842→1654 (+135.3/min) · top10 40.7%→33.5% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=24263.54, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 47 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T05:01:40+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 17 de 14.235 tokens analizados (0,12%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 05:01 UTC, hasta 08/10/2026 05:01 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +6,2% · h1 +60,4% · h24 +60% · volumen m5/h1 0,38 · edad del par 10,6 min.
- **Precio de entrada** (alerta): $0,00007933.
- **Consulta 06/10/2026 05:12 UTC:** $0,0001233 (+55,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ_2026-10-06_050140.json` · blob `08c23bb58c2623a00d0d525768bc271667c3faf3` · commit `128251a` (2026-10-06T05:06:46Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_050140`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ · registro · 06/10/2026 05:01 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ · HTTP 200 · 06/10/2026 05:12 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ/report · HTTP 200 · 06/10/2026 05:12 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ · HTTP 200 · 06/10/2026 05:12 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/9ebYNt7c7aZtaKQS8UPbCT6gdzyXWAje3x8Ca28ysyGT/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 05:12 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ · HTTP 404 · 06/10/2026 05:12 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=CAESARUSDT · HTTP 400 · 06/10/2026 05:12 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/CAESAR-USD · HTTP 404 · 06/10/2026 05:12 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $31.183 vs $32.601 → 4,35%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001233 vs $0,0001217 → 1,28%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ_2026-10-06_050140.json',encoding='utf-8'));d=d.get('8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ',d);p=mock.patch('time.time',return_value=1791262900);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8cp1WhUDxTbfX8nDe1kAB1ogPUyQvUSKgzFz365LbQyZ --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 05:12 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `3cf01070a7decc4a…`
