# My Super Intelligent Cat (Ollie) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001895 · liquidez $39.371 · mcap $189.572 (al detectar)  
Detectado el 11/10/2026 01:25 UTC por: young-0.4 · edad 13.3 min · pesos info 58 / estructura 21 / precio 21 · info 15.7 · estructura 17.4 · precio/volumen 7.3 · cobertura 84/100, [info] narrative_wave: ola 'super': 7 lanzamientos más en 1 h → +12.8, [info] dex_profile: perfil pago en DexScreener → +2.9 (score 40, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 13/10/2026 01:25 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Ollie

Estudio de cómo se adquiere Ollie, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/10/2026 01:37 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 11/10/2026 01:25 UTC | pumpswap `Bos7G49…tv1f` | $39.371 | 10% | 0,508% | 5,080% | 50,799% | $197 | $591 |
| consulta 11/10/2026 01:37 UTC | pumpswap `Bos7G49…tv1f` | $31.828 | 10% | 0,628% | 6,284% | 62,838% | $159 | $477 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump`
5. Configurar el slippage: 10% (liquidez $31.828, consulta 11/10/2026 01:37 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump) y el par en DexScreener (https://dexscreener.com/solana/Bos7G49PSy2SaYnPNWsZjDL25Sc4qgUwmncmGAZitv1f); mint authority / freeze authority: revocada / revocada · holders 3.690 · top-10 30,11% (consulta 11/10/2026 01:37 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump
- Par en DexScreener: https://dexscreener.com/solana/Bos7G49PSy2SaYnPNWsZjDL25Sc4qgUwmncmGAZitv1f
- Página del lanzamiento (pump.fun): https://pump.fun/coin/564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.690 · top-10 30,11% (consulta 11/10/2026 01:37 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | My Super Intelligent Cat / Ollie | registro de la detección (pumpportal_live) |
| Mint / contrato | `564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Bos7G49PSy2SaYnPNWsZjDL25Sc4qgUwmncmGAZitv1f` | DexScreener, al detectar (6 par(es) en la consulta 11/10/2026 01:37 UTC) |
| Deployer | `AGja5tTMvTzsgdKgMLboRGSsioQV2cJuLFiud9fgnSgr` | PumpPortal (evento create), al detectar |
| Par creado | 11/10/2026 01:11 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 13,3 min / 13,3 min / 25,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/10/2026 01:37 UTC |
| Holders / top-10 | 3.690 / 30,11% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/10/2026 01:37 UTC |
| Holders efectivos del top-10 | 4,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/10/2026 01:37 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 11/10/2026 01:37 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Bos7G49PSy2SaYnPNWsZjDL25Sc4qgUwmncmGAZitv1f · Solscan: https://solscan.io/token/564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump · pump.fun: https://pump.fun/coin/564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump · twitter: https://x.com/TAsimovF | consulta 11/10/2026 01:37 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/10/2026 01:37 UTC)
- **Historia:**
  - Par creado el 11/10/2026 01:11 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 11/10/2026 01:25 UTC, con el par a 13,3 min de creado: precio $0,0001895, mcap $189.572, liquidez $39.371.
  - Velas de 1 h de GeckoTerminal (1, desde 11/10/2026 01:00 UTC): apertura $0,00004353 · máximo $0,0003753 (11/10/2026 01:00 UTC) · mínimo $0,00004105 (11/10/2026 01:00 UTC) · último cierre $0,0001312.
  - En la consulta 11/10/2026 01:37 UTC: precio $0,0001270, liquidez $31.828, FDV $127.066.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 11/10/2026 01:25 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001895 |
| Liquidez | $39.371 |
| MCap | $189.572 |
| Volumen 24 h | $388.254 |
| Cambio 24 h | +317% |
| Cambio m5 / h1 | -15,8% / +317,0% |
| Volumen m5 / h1 | $81.179 / $388.254 |
| Trades m5 (compras / ventas) | 692 / 647 |
| Edad del par | 13,3 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 40; motivos sin regla: young-0.4 · edad 13.3 min · pesos info 58 / estructura 21 / precio 21 · info 15.7 · estructura 17.4 · precio/volumen 7.3 · cobertura 84/100, [info] narrative_wave: ola 'super': 7 lanzamientos más en 1 h → +12.8, [info] dex_profile: perfil pago en DexScreener → +2.9, [estructura] bonding_progress: graduado (pumpswap) → +10.0, [estructura] holders_struct: holders 2977 · top-10 28.4 % → +5.0, [estructura] dev_wallet: creador compró 5.0 % del supply → +1.6, [estructura] holder_to_txn_ratio: holders/txns 2977/5580 = 0.53 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×2.5 la tasa horaria (s 0.40), [precio/volumen] liquidity_inflow: liquidez +15% en 8 min (s 0.49), [precio/volumen] holder_accumulation: holders 2188→2977 (+131.5/min) · top10 28.1%→28.4% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=39371.09, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=24836.63, score 40 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-11T01:25:11+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 45 de 28.204 tokens analizados (0,16%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 11/10/2026 01:25 UTC, hasta 13/10/2026 01:25 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -15,8% · h1 +317,0% · h24 +317% · volumen m5/h1 0,21 · edad del par 13,3 min.
- **Precio de entrada** (alerta): $0,0001895.
- **Consulta 11/10/2026 01:37 UTC:** $0,0001270 (-33,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump_2026-10-11_012511.json` · blob `95f3791645886d1ec50530ba8aeecaa3e3dc7be4` · commit `a0e6e28` (2026-10-11T01:31:14Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-11_010937.json` · blob `0c13f1c1196fe35d56d955a6afc7eec2cf720a07` · commit `a0e6e28` (2026-10-11T01:31:14Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-11_012511`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump · registro · 11/10/2026 01:25 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump · HTTP 200 · 11/10/2026 01:37 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump/report · HTTP 200 · 11/10/2026 01:37 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump · HTTP 200 · 11/10/2026 01:37 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Bos7G49PSy2SaYnPNWsZjDL25Sc4qgUwmncmGAZitv1f/ohlcv/hour?limit=1000 · HTTP 200 · 11/10/2026 01:37 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump · HTTP 404 · 11/10/2026 01:37 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=OLLIEUSDT · HTTP 400 · 11/10/2026 01:37 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/OLLIE-USD · HTTP 404 · 11/10/2026 01:37 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $31.828 vs $32.092 → 0,82%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001270 vs $0,0001312 → 3,20%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump_2026-10-11_012511.json',encoding='utf-8'));d=d.get('564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump',d);p=mock.patch('time.time',return_value=1791681911);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 564TGXSRPH2a7vJvdp1uSaZ4M1qDmeKgoMZyfBvYpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/10/2026 01:37 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `8b1cb641d5bfc324…`
