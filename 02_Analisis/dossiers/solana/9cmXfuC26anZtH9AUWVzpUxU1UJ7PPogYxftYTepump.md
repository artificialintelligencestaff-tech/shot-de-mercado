# Wishmas  (WISHMAS) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001270 · liquidez $25.911 · mcap $126.906 (al detectar)  
Detectado el 13/11/2026 21:58 UTC por: young-0.4 · edad 14.7 min · pesos info 58 / estructura 21 / precio 21 · info 13.4 · estructura 15.7 · precio/volumen 12.3 · cobertura 94/100, [info] narrative_wave: ola 'wishmas': 3 lanzamientos más en 1 h → +5.4, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.1 (score 42, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 15/11/2026 21:58 UTC (< 48 h) · vigente: quedan 44,1 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir WISHMAS

Estudio de cómo se adquiere WISHMAS, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 14/11/2026 01:49 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 13/11/2026 21:58 UTC | pumpswap `FcsUyth…qx3p` | $25.911 | 10% | 0,772% | 7,719% | 77,188% | $130 | $389 |
| consulta 14/11/2026 01:49 UTC | pumpswap `FcsUyth…qx3p` | $27.699 | 10% | 0,722% | 7,220% | 72,205% | $138 | $415 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump`
5. Configurar el slippage: 10% (liquidez $27.699, consulta 14/11/2026 01:49 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump) y el par en DexScreener (https://dexscreener.com/solana/FcsUythNUWbfT7RP2yuFp1kiWjft15du9WtgLUrrqx3p); mint authority / freeze authority: revocada / revocada · holders 4.085 · top-10 30,50% (consulta 14/11/2026 01:49 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump
- Par en DexScreener: https://dexscreener.com/solana/FcsUythNUWbfT7RP2yuFp1kiWjft15du9WtgLUrrqx3p
- Página del lanzamiento (pump.fun): https://pump.fun/coin/9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.085 · top-10 30,50% (consulta 14/11/2026 01:49 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Wishmas  / WISHMAS | registro de la detección (pumpportal_live) |
| Mint / contrato | `9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `FcsUythNUWbfT7RP2yuFp1kiWjft15du9WtgLUrrqx3p` | DexScreener, al detectar (19 par(es) en la consulta 14/11/2026 01:49 UTC) |
| Deployer | `3jBqTnG6Q7YbAu44sxXuZvwM1ThqZHq2kEgiU7PYySkw` | PumpPortal (evento create), al detectar |
| Par creado | 13/11/2026 21:43 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 14,7 min / 14,7 min / 4,1 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 14/11/2026 01:49 UTC |
| Holders / top-10 | 4.085 / 30,50% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 14/11/2026 01:49 UTC |
| Holders efectivos del top-10 | 5,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 14/11/2026 01:49 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 14/11/2026 01:49 UTC |
| Links | DexScreener: https://dexscreener.com/solana/FcsUythNUWbfT7RP2yuFp1kiWjft15du9WtgLUrrqx3p · Solscan: https://solscan.io/token/9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump · pump.fun: https://pump.fun/coin/9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump · twitter: https://x.com/WishmasOnPump | consulta 14/11/2026 01:49 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 14/11/2026 01:49 UTC)
- **Historia:**
  - Par creado el 13/11/2026 21:43 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 13/11/2026 21:58 UTC, con el par a 14,7 min de creado: precio $0,0001270, mcap $126.906, liquidez $25.911.
  - Velas de 1 h de GeckoTerminal (5, desde 13/11/2026 21:00 UTC): apertura $0,00003248 · máximo $0,0002862 (14/11/2026 00:00 UTC) · mínimo $0,00001402 (13/11/2026 21:00 UTC) · último cierre $0,0001241.
  - En la consulta 14/11/2026 01:49 UTC: precio $0,0001269, liquidez $27.699, FDV $121.201.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 13/11/2026 21:58 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001270 |
| Liquidez | $25.911 |
| MCap | $126.906 |
| Volumen 24 h | $279.428 |
| Cambio 24 h | +294% |
| Cambio m5 / h1 | +123,0% / +294,0% |
| Volumen m5 / h1 | $107.940 / $279.428 |
| Trades m5 (compras / ventas) | 1.516 / 1.157 |
| Edad del par | 14,7 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 42; motivos sin regla: young-0.4 · edad 14.7 min · pesos info 58 / estructura 21 / precio 21 · info 13.4 · estructura 15.7 · precio/volumen 12.3 · cobertura 94/100, [info] narrative_wave: ola 'wishmas': 3 lanzamientos más en 1 h → +5.4, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.1, [info] dex_profile: perfil pago en DexScreener → +2.9, [estructura] bonding_progress: graduado (pumpswap) → +10.2, [estructura] holders_struct: holders 1768 · top-10 27.0 % → +5.1, [estructura] dev_wallet: creador compró 9.6 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1768/7612 = 0.23 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×4.6 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +49% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1130→1768 (+106.3/min) · top10 37.7%→27.0% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=25910.6, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 42 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-13T21:58:07+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 100 de 47.186 tokens analizados (0,21%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 13/11/2026 21:58 UTC, hasta 15/11/2026 21:58 UTC · vigente: quedan 44,1 h.
- **Aceleración al detectar:** cambio m5 +123,0% · h1 +294,0% · h24 +294% · volumen m5/h1 0,39 · edad del par 14,7 min.
- **Precio de entrada** (alerta): $0,0001270.
- **Consulta 14/11/2026 01:49 UTC:** $0,0001269 (-0,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump_2026-11-13_215807.json` · blob `96f3be53ce9d44193d53c9cc3493705f744c1bc4` · commit `f0d7cab` (2026-11-14T00:29:43Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-13_215807`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump · registro · 13/11/2026 21:58 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump · HTTP 200 · 14/11/2026 01:49 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump/report · HTTP 200 · 14/11/2026 01:49 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump · HTTP 200 · 14/11/2026 01:49 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/FcsUythNUWbfT7RP2yuFp1kiWjft15du9WtgLUrrqx3p/ohlcv/hour?limit=1000 · HTTP 200 · 14/11/2026 01:49 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump · HTTP 404 · 14/11/2026 01:49 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=WISHMASUSDT · HTTP 400 · 14/11/2026 01:49 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/WISHMAS-USD · HTTP 404 · 14/11/2026 01:49 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $27.699 vs $27.855 → 0,56%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001269 vs $0,0001241 → 2,20%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump_2026-11-13_215807.json',encoding='utf-8'));d=d.get('9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump',d);p=mock.patch('time.time',return_value=1794607087);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 14/11/2026 01:49 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `2046f850e8dae231…`
