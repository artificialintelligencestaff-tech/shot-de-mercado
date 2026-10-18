# Massive.gg (MASSIVE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0002550 · liquidez $46.829 · mcap $254.816 (al detectar)  
Detectado el 18/10/2026 05:38 UTC por: young-0.4 · edad 10.5 min · pesos info 60 / estructura 20 / precio 20 · info 14.9 · estructura 17.3 · precio/volumen 7.8 · cobertura 83/100, [info] narrative_wave: ola 'massive': 8 lanzamientos más en 1 h → +14.9, [estructura] bonding_progress: graduado (pumpswap) → +9.7 (score 40, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 20/10/2026 05:38 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir MASSIVE

Estudio de cómo se adquiere MASSIVE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 18/10/2026 05:51 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 18/10/2026 05:38 UTC | pumpswap `2EuQkDn…GaxQ` | $46.829 | 10% | 0,427% | 4,271% | 42,709% | $234 | $702 |
| consulta 18/10/2026 05:51 UTC | pumpswap `2EuQkDn…GaxQ` | $35.517 | 10% | 0,563% | 5,631% | 56,311% | $178 | $533 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump`
5. Configurar el slippage: 10% (liquidez $35.517, consulta 18/10/2026 05:51 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump) y el par en DexScreener (https://dexscreener.com/solana/2EuQkDnsiPTDqdYm63UWiTReqGw2v8R2e2KJTEttGaxQ); mint authority / freeze authority: revocada / revocada · holders 3.510 · top-10 21,61% (consulta 18/10/2026 05:51 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump
- Par en DexScreener: https://dexscreener.com/solana/2EuQkDnsiPTDqdYm63UWiTReqGw2v8R2e2KJTEttGaxQ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.510 · top-10 21,61% (consulta 18/10/2026 05:51 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Massive.gg / MASSIVE | registro de la detección (pumpportal_live) |
| Mint / contrato | `7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `2EuQkDnsiPTDqdYm63UWiTReqGw2v8R2e2KJTEttGaxQ` | DexScreener, al detectar (12 par(es) en la consulta 18/10/2026 05:51 UTC) |
| Deployer | `HwHzPpNsQYEdFs2xmE6jwqSTSQKSYkkmykb8574TjLfJ` | PumpPortal (evento create), al detectar |
| Par creado | 18/10/2026 05:28 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,5 min / 10,5 min / 23,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 18/10/2026 05:51 UTC |
| Holders / top-10 | 3.510 / 21,61% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 18/10/2026 05:51 UTC |
| Holders efectivos del top-10 | 3,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 18/10/2026 05:51 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 18/10/2026 05:51 UTC |
| Links | DexScreener: https://dexscreener.com/solana/2EuQkDnsiPTDqdYm63UWiTReqGw2v8R2e2KJTEttGaxQ · Solscan: https://solscan.io/token/7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump · pump.fun: https://pump.fun/coin/7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump · web / Telegram / X: no publicados en DexScreener | consulta 18/10/2026 05:51 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 18/10/2026 05:51 UTC)
- **Historia:**
  - Par creado el 18/10/2026 05:28 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 18/10/2026 05:38 UTC, con el par a 10,5 min de creado: precio $0,0002550, mcap $254.816, liquidez $46.829.
  - Velas de 1 h de GeckoTerminal (1, desde 18/10/2026 05:00 UTC): apertura $0,00003966 · máximo $0,0003147 (18/10/2026 05:00 UTC) · mínimo $0,00003091 (18/10/2026 05:00 UTC) · último cierre $0,0001659.
  - En la consulta 18/10/2026 05:51 UTC: precio $0,0001683, liquidez $35.517, FDV $168.178.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 18/10/2026 05:38 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0002550 |
| Liquidez | $46.829 |
| MCap | $254.816 |
| Volumen 24 h | $713.013 |
| Cambio 24 h | +520% |
| Cambio m5 / h1 | +30,4% / +520,0% |
| Volumen m5 / h1 | $166.675 / $713.013 |
| Trades m5 (compras / ventas) | 1.510 / 1.042 |
| Edad del par | 10,5 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 40; motivos sin regla: young-0.4 · edad 10.5 min · pesos info 60 / estructura 20 / precio 20 · info 14.9 · estructura 17.3 · precio/volumen 7.8 · cobertura 83/100, [info] narrative_wave: ola 'massive': 8 lanzamientos más en 1 h → +14.9, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 2868 · top-10 20.2 % → +4.8, [estructura] dev_wallet: creador compró 2.0 % del supply → +2.4, [estructura] holder_to_txn_ratio: holders/txns 2868/12059 = 0.24 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×2.8 la tasa horaria (s 0.52), [precio/volumen] buy_pressure_shift: compras 59% en 5 min vs 50% en 1 h (s 0.46), [precio/volumen] liquidity_inflow: liquidez +2% en 8 min (s 0.08), [precio/volumen] holder_accumulation: holders 2019→2868 (+141.5/min) · top10 22.2%→20.2% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=46828.71, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=23315.44, score 40 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-18T05:38:30+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=18.4% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 65 de 39.246 tokens analizados (0,17%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 18/10/2026 05:38 UTC, hasta 20/10/2026 05:38 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +30,4% · h1 +520,0% · h24 +520% · volumen m5/h1 0,23 · edad del par 10,5 min.
- **Precio de entrada** (alerta): $0,0002550.
- **Consulta 18/10/2026 05:51 UTC:** $0,0001683 (-34,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump_2026-10-18_053830.json` · blob `1c244f53d1e21c239fc765b4948ba4c985ae0c22` · commit `9ad13ee` (2026-10-18T05:44:43Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-18_053830`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump · registro · 18/10/2026 05:38 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump · HTTP 200 · 18/10/2026 05:51 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump/report · HTTP 200 · 18/10/2026 05:51 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump · HTTP 200 · 18/10/2026 05:51 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/2EuQkDnsiPTDqdYm63UWiTReqGw2v8R2e2KJTEttGaxQ/ohlcv/hour?limit=1000 · HTTP 200 · 18/10/2026 05:51 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump · HTTP 404 · 18/10/2026 05:51 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MASSIVEUSDT · HTTP 418 · 18/10/2026 05:51 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MASSIVE-USD · HTTP 404 · 18/10/2026 05:51 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $35.517 vs $41.661 → 14,75%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001683 vs $0,0001659 → 1,45%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump_2026-10-18_053830.json',encoding='utf-8'));d=d.get('7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump',d);p=mock.patch('time.time',return_value=1792301910);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 7UAWdJjrBykopzco6bCBmMLdggaiec6bd4bTKmQqpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 18/10/2026 05:51 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `1d5b8c1eded52605…`
