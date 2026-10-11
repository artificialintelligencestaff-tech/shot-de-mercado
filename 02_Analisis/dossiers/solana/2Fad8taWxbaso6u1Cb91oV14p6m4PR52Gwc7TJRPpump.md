# Strk.trade (STRKT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0002317 · liquidez $42.566 · mcap $231.770 (al detectar)  
Detectado el 11/10/2026 03:03 UTC por: young-0.4 · edad 16.2 min · pesos info 57 / estructura 22 / precio 22 · info 8.5 · estructura 18.4 · precio/volumen 12.6 · cobertura 84/100, [info] trending_match: 'strk' en trending #2 Starknet → +5.7, [info] dex_profile: perfil pago en DexScreener → +2.8 (score 40, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 13/10/2026 03:03 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir STRKT

Estudio de cómo se adquiere STRKT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/10/2026 03:13 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 11/10/2026 03:03 UTC | pumpswap `ChRE2kR…PhkX` | $42.566 | 10% | 0,470% | 4,699% | 46,986% | $213 | $638 |
| consulta 11/10/2026 03:12 UTC | pumpswap `ChRE2kR…PhkX` | $32.939 | 10% | 0,607% | 6,072% | 60,718% | $165 | $494 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump`
5. Configurar el slippage: 10% (liquidez $32.939, consulta 11/10/2026 03:12 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump) y el par en DexScreener (https://dexscreener.com/solana/ChRE2kRDxyMpBMLVwxCMMG3tofXPxyfqheQ8BsKoPhkX); mint authority / freeze authority: revocada / revocada · holders 3.155 · top-10 27,84% (consulta 11/10/2026 03:12 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump
- Par en DexScreener: https://dexscreener.com/solana/ChRE2kRDxyMpBMLVwxCMMG3tofXPxyfqheQ8BsKoPhkX
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.155 · top-10 27,84% (consulta 11/10/2026 03:12 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Strk.trade / STRKT | registro de la detección (pumpportal_live) |
| Mint / contrato | `2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `ChRE2kRDxyMpBMLVwxCMMG3tofXPxyfqheQ8BsKoPhkX` | DexScreener, al detectar (9 par(es) en la consulta 11/10/2026 03:12 UTC) |
| Deployer | `FmzJDszFourvjZ49UVK38VZGbmVJ5aDKyZxUzEJvTxo2` | PumpPortal (evento create), al detectar |
| Par creado | 11/10/2026 02:47 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 16,2 min / 16,2 min / 25,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/10/2026 03:12 UTC |
| Holders / top-10 | 3.155 / 27,84% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/10/2026 03:12 UTC |
| Holders efectivos del top-10 | 4,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/10/2026 03:12 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 11/10/2026 03:12 UTC |
| Links | DexScreener: https://dexscreener.com/solana/ChRE2kRDxyMpBMLVwxCMMG3tofXPxyfqheQ8BsKoPhkX · Solscan: https://solscan.io/token/2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump · pump.fun: https://pump.fun/coin/2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump · web: https://strk.trade · twitter: https://x.com/strktrade | consulta 11/10/2026 03:12 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/10/2026 03:12 UTC)
- **Historia:**
  - Par creado el 11/10/2026 02:47 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 11/10/2026 03:03 UTC, con el par a 16,2 min de creado: precio $0,0002317, mcap $231.770, liquidez $42.566.
  - Velas de 1 h de GeckoTerminal (2, desde 11/10/2026 02:00 UTC): apertura $0,00003542 · máximo $0,0002488 (11/10/2026 03:00 UTC) · mínimo $0,00003530 (11/10/2026 02:00 UTC) · último cierre $0,0001323.
  - En la consulta 11/10/2026 03:12 UTC: precio $0,0001424, liquidez $32.939, FDV $142.422.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 11/10/2026 03:03 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0002317 |
| Liquidez | $42.566 |
| MCap | $231.770 |
| Volumen 24 h | $272.155 |
| Cambio 24 h | +411% |
| Cambio m5 / h1 | +73,8% / +411,0% |
| Volumen m5 / h1 | $107.205 / $272.155 |
| Trades m5 (compras / ventas) | 710 / 625 |
| Edad del par | 16,2 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 40; motivos sin regla: young-0.4 · edad 16.2 min · pesos info 57 / estructura 22 / precio 22 · info 8.5 · estructura 18.4 · precio/volumen 12.6 · cobertura 84/100, [info] trending_match: 'strk' en trending #2 Starknet → +5.7, [info] dex_profile: perfil pago en DexScreener → +2.8, [estructura] bonding_progress: graduado (pumpswap) → +10.3, [estructura] holders_struct: holders 1871 · top-10 29.9 % → +5.2, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.1, [estructura] holder_to_txn_ratio: holders/txns 1871/4268 = 0.44 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×4.7 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 53% en 5 min vs 53% en 1 h (s 0.02), [precio/volumen] liquidity_inflow: liquidez +97% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1297→1871 (+95.7/min) · top10 37.0%→29.9% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=42566.22, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 40 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-11T03:03:26+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 45 de 28.401 tokens analizados (0,16%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 11/10/2026 03:03 UTC, hasta 13/10/2026 03:03 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +73,8% · h1 +411,0% · h24 +411% · volumen m5/h1 0,39 · edad del par 16,2 min.
- **Precio de entrada** (alerta): $0,0002317.
- **Consulta 11/10/2026 03:12 UTC:** $0,0001424 (-38,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump_2026-10-11_030326.json` · blob `12b9f6182fcef47ab9c330565e69d2a9dc9cce1e` · commit `117b627` (2026-10-11T03:06:01Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-11_023252.json` · blob `72166aeed161fa0b040c5f34a0e5c19546bbe4c5` · commit `117b627` (2026-10-11T03:06:01Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-11_030326`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump · registro · 11/10/2026 03:03 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump · HTTP 200 · 11/10/2026 03:12 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump/report · HTTP 200 · 11/10/2026 03:12 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump · HTTP 200 · 11/10/2026 03:13 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/ChRE2kRDxyMpBMLVwxCMMG3tofXPxyfqheQ8BsKoPhkX/ohlcv/hour?limit=1000 · HTTP 200 · 11/10/2026 03:13 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump · HTTP 404 · 11/10/2026 03:13 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=STRKTUSDT · HTTP 400 · 11/10/2026 03:13 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/STRKT-USD · HTTP 404 · 11/10/2026 03:13 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $32.939 vs $32.320 → 1,88%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001424 vs $0,0001323 → 7,08%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump_2026-10-11_030326.json',encoding='utf-8'));d=d.get('2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump',d);p=mock.patch('time.time',return_value=1791687806);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2Fad8taWxbaso6u1Cb91oV14p6m4PR52Gwc7TJRPpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/10/2026 03:13 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `82404aeaf26f0298…`
