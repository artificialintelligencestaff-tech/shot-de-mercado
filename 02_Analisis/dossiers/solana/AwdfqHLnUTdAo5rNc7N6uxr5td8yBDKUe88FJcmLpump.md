# JEZ (JEZ) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001188 · liquidez $28.726 · mcap $118.770 (al detectar)  
Detectado el 08/10/2026 13:47 UTC por: young-0.4 · edad 10.3 min · pesos info 60 / estructura 20 / precio 20 · info 18.8 · estructura 17.2 · precio/volumen 11.9 · cobertura 93/100, [info] narrative_wave: ola 'jez': 7 lanzamientos más en 1 h → +13.1, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.7 (score 48, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 10/10/2026 13:47 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir JEZ

Estudio de cómo se adquiere JEZ, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/10/2026 13:59 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/10/2026 13:47 UTC | pumpswap `73cbwUU…X6MW` | $28.726 | 10% | 0,696% | 6,962% | 69,622% | $144 | $431 |
| consulta 08/10/2026 13:59 UTC | pumpswap `73cbwUU…X6MW` | $2.147 | 10% | 9,316% | 93,165% | 931,650% | $11 | $32 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump`
5. Configurar el slippage: 10% (liquidez $2.147, consulta 08/10/2026 13:59 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump) y el par en DexScreener (https://dexscreener.com/solana/73cbwUULj7pRpkk2q4tSbNx6yU8R52mJehCLWCrFX6MW); mint authority / freeze authority: revocada / revocada · holders 181 · top-10 99,77% (consulta 08/10/2026 13:59 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump
- Par en DexScreener: https://dexscreener.com/solana/73cbwUULj7pRpkk2q4tSbNx6yU8R52mJehCLWCrFX6MW
- Página del lanzamiento (pump.fun): https://pump.fun/coin/AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 181 · top-10 99,77% (consulta 08/10/2026 13:59 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | JEZ / JEZ | registro de la detección (pumpportal_live) |
| Mint / contrato | `AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `73cbwUULj7pRpkk2q4tSbNx6yU8R52mJehCLWCrFX6MW` | DexScreener, al detectar (2 par(es) en la consulta 08/10/2026 13:59 UTC) |
| Deployer | `8S8Z8kEmABsYG3z8V12kMpyVGXpPjsCPiqAtgPAdNpt` | PumpPortal (evento create), al detectar |
| Par creado | 08/10/2026 13:37 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,2 min / 10,2 min / 22,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/10/2026 13:59 UTC |
| Holders / top-10 | 181 / 99,77% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/10/2026 13:59 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/10/2026 13:59 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 08/10/2026 13:59 UTC |
| Links | DexScreener: https://dexscreener.com/solana/73cbwUULj7pRpkk2q4tSbNx6yU8R52mJehCLWCrFX6MW · Solscan: https://solscan.io/token/AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump · pump.fun: https://pump.fun/coin/AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump · web / Telegram / X: no publicados en DexScreener | consulta 08/10/2026 13:59 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/10/2026 13:59 UTC)
- **Historia:**
  - Par creado el 08/10/2026 13:37 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/10/2026 13:47 UTC, con el par a 10,2 min de creado: precio $0,0001188, mcap $118.770, liquidez $28.726.
  - Velas de 1 h de GeckoTerminal (1, desde 08/10/2026 13:00 UTC): apertura $0,00006116 · máximo $0,0001643 (08/10/2026 13:00 UTC) · mínimo $0,000002114 (08/10/2026 13:00 UTC) · último cierre $0,000002120.
  - En la consulta 08/10/2026 13:59 UTC: precio $0,000002120, liquidez $2.147, FDV $2.118.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/10/2026 13:47 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001188 |
| Liquidez | $28.726 |
| MCap | $118.770 |
| Volumen 24 h | $58.174 |
| Cambio 24 h | +104% |
| Cambio m5 / h1 | +23,5% / +104,0% |
| Volumen m5 / h1 | $27.579 / $58.174 |
| Trades m5 (compras / ventas) | 1.386 / 426 |
| Edad del par | 10,2 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 48; motivos sin regla: young-0.4 · edad 10.3 min · pesos info 60 / estructura 20 / precio 20 · info 18.8 · estructura 17.2 · precio/volumen 11.9 · cobertura 93/100, [info] narrative_wave: ola 'jez': 7 lanzamientos más en 1 h → +13.1, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.7, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1912 · top-10 25.2 % → +4.8, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.0, [estructura] holder_to_txn_ratio: holders/txns 1912/3852 = 0.50 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×5.7 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 76% en 5 min vs 76% en 1 h (s 0.04), [precio/volumen] liquidity_inflow: liquidez +43% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 811→1912 (+91.7/min) · top10 42.0%→25.2% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=28726.46, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 48 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-08T13:47:49+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen decente, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 38 de 21.804 tokens analizados (0,17%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/10/2026 13:47 UTC, hasta 10/10/2026 13:47 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +23,5% · h1 +104,0% · h24 +104% · volumen m5/h1 0,47 · edad del par 10,2 min.
- **Precio de entrada** (alerta): $0,0001188.
- **Consulta 08/10/2026 13:59 UTC:** $0,000002120 (-98,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump_2026-10-08_134749.json` · blob `4a53d1dcc5c8438c3daf510d2f494dc037dd1f6f` · commit `0c76b0a` (2026-10-08T13:53:05Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-08_134749`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump · registro · 08/10/2026 13:47 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump · HTTP 200 · 08/10/2026 13:59 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump/report · HTTP 200 · 08/10/2026 13:59 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump · HTTP 200 · 08/10/2026 13:59 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/73cbwUULj7pRpkk2q4tSbNx6yU8R52mJehCLWCrFX6MW/ohlcv/hour?limit=1000 · HTTP 200 · 08/10/2026 13:59 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump · HTTP 404 · 08/10/2026 13:59 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=JEZUSDT · HTTP 400 · 08/10/2026 13:59 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/JEZ-USD · HTTP 404 · 08/10/2026 13:59 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.147 vs $2.141 → 0,26%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002120 vs $0,000002120 → 0,01%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump_2026-10-08_134749.json',encoding='utf-8'));d=d.get('AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump',d);p=mock.patch('time.time',return_value=1791467269);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint AwdfqHLnUTdAo5rNc7N6uxr5td8yBDKUe88FJcmLpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/10/2026 13:59 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `9445c1e230c873f1…`
