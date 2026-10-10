# Benny's Hub (BENNY) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00002775 · liquidez $13.511 · mcap $27.758 (al detectar)  
Detectado el 10/10/2026 05:23 UTC por: young-0.4 · edad 11.0 min · pesos info 59 / estructura 20 / precio 20 · info 19.4 · estructura 13.0 · precio/volumen 8.4 · cobertura 93/100, [info] narrative_wave: ola 'hub': 6 lanzamientos más en 1 h → +11.2, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +5.3 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 12/10/2026 05:23 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir BENNY

Estudio de cómo se adquiere BENNY, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 10/10/2026 05:55 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 10/10/2026 05:23 UTC | pumpswap `DmsAZnf…nYJz` | $13.511 | 10% | 1,480% | 14,803% | 148,025% | $68 | $203 |
| consulta 10/10/2026 05:55 UTC | pumpswap `DmsAZnf…nYJz` | $20.626 | 10% | 0,970% | 9,697% | 96,967% | $103 | $309 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump`
5. Configurar el slippage: 10% (liquidez $20.626, consulta 10/10/2026 05:55 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump) y el par en DexScreener (https://dexscreener.com/solana/DmsAZnfNY4styDK7iKyWMM2rthcew4EVfkM1MW8VnYJz); mint authority / freeze authority: revocada / revocada · holders 1.812 · top-10 36,37% (consulta 10/10/2026 05:55 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump
- Par en DexScreener: https://dexscreener.com/solana/DmsAZnfNY4styDK7iKyWMM2rthcew4EVfkM1MW8VnYJz
- Página del lanzamiento (pump.fun): https://pump.fun/coin/EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.812 · top-10 36,37% (consulta 10/10/2026 05:55 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Benny's Hub / BENNY | registro de la detección (pumpportal_live) |
| Mint / contrato | `EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DmsAZnfNY4styDK7iKyWMM2rthcew4EVfkM1MW8VnYJz` | DexScreener, al detectar (2 par(es) en la consulta 10/10/2026 05:55 UTC) |
| Deployer | `F5XvCe4233m6mHRbkkq2ZsFvqrPAnRrDBExeQy2fwagQ` | PumpPortal (evento create), al detectar |
| Par creado | 10/10/2026 05:12 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,0 min / 11,0 min / 43,3 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 10/10/2026 05:55 UTC |
| Holders / top-10 | 1.812 / 36,37% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 10/10/2026 05:55 UTC |
| Holders efectivos del top-10 | 3,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 10/10/2026 05:55 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 10/10/2026 05:55 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DmsAZnfNY4styDK7iKyWMM2rthcew4EVfkM1MW8VnYJz · Solscan: https://solscan.io/token/EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump · pump.fun: https://pump.fun/coin/EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump · web / Telegram / X: no publicados en DexScreener | consulta 10/10/2026 05:55 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 10/10/2026 05:55 UTC)
- **Historia:**
  - Par creado el 10/10/2026 05:12 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 10/10/2026 05:23 UTC, con el par a 11,0 min de creado: precio $0,00002775, mcap $27.758, liquidez $13.511.
  - Velas de 1 h de GeckoTerminal (1, desde 10/10/2026 05:00 UTC): apertura $0,00004650 · máximo $0,0001293 (10/10/2026 05:00 UTC) · mínimo $0,00001634 (10/10/2026 05:00 UTC) · último cierre $0,00005745.
  - En la consulta 10/10/2026 05:55 UTC: precio $0,00006071, liquidez $20.626, FDV $57.343.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 10/10/2026 05:23 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00002775 |
| Liquidez | $13.511 |
| MCap | $27.758 |
| Volumen 24 h | $62.180 |
| Cambio 24 h | -40% |
| Cambio m5 / h1 | -53,2% / -40,3% |
| Volumen m5 / h1 | $20.692 / $62.180 |
| Trades m5 (compras / ventas) | 266 / 225 |
| Edad del par | 11,0 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 11.0 min · pesos info 59 / estructura 20 / precio 20 · info 19.4 · estructura 13.0 · precio/volumen 8.4 · cobertura 93/100, [info] narrative_wave: ola 'hub': 6 lanzamientos más en 1 h → +11.2, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +5.3, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 952 · top-10 39.6 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 952/1417 = 0.67 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×4.0 la tasa horaria (s 1.00), [precio/volumen] holder_accumulation: holders 600→952 (+58.7/min) · top10 45.1%→39.6% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=13511.19, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-10T05:23:29+00:00, sin estado previo): **5** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen decente, Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 43 de 26.507 tokens analizados (0,16%) quedan ≥ 56. Con score 5, este activo queda en el percentil 87,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 10/10/2026 05:23 UTC, hasta 12/10/2026 05:23 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -53,2% · h1 -40,3% · h24 -40% · volumen m5/h1 0,33 · edad del par 11,0 min.
- **Precio de entrada** (alerta): $0,00002775.
- **Consulta 10/10/2026 05:55 UTC:** $0,00006071 (+118,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump_2026-10-10_052329.json` · blob `2ad2ef24d266ab924322f6e7dc76b1c6da8beb32` · commit `aa3ad44` (2026-10-10T05:49:07Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-10_050708.json` · blob `387ad565efd1b834c20e71b5be1009ac31b8d3a3` · commit `aa3ad44` (2026-10-10T05:49:07Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-10_052329`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump · registro · 10/10/2026 05:23 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump · HTTP 200 · 10/10/2026 05:55 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump/report · HTTP 200 · 10/10/2026 05:55 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump · HTTP 200 · 10/10/2026 05:55 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DmsAZnfNY4styDK7iKyWMM2rthcew4EVfkM1MW8VnYJz/ohlcv/hour?limit=1000 · HTTP 200 · 10/10/2026 05:55 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump · HTTP 404 · 10/10/2026 05:55 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BENNYUSDT · HTTP 400 · 10/10/2026 05:55 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BENNY-USD · HTTP 404 · 10/10/2026 05:55 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $20.626 vs $20.398 → 1,10%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00006071 vs $0,00005745 → 5,36%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump_2026-10-10_052329.json',encoding='utf-8'));d=d.get('EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump',d);p=mock.patch('time.time',return_value=1791609809);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint EKfBSf5etGkBxgEf9ydZCrtRE8KEHvg5sC7tgFS6pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 10/10/2026 05:55 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `75f42c782a488aa0…`
