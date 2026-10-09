# Quantum Safe Bitcoin (QSB) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00006122 · liquidez $21.430 · mcap $61.224 (al detectar)  
Detectado el 09/10/2026 14:57 UTC por: young-0.4 · edad 11.8 min · pesos info 59 / estructura 20 / precio 20 · info 23.0 · estructura 12.9 · precio/volumen 10.2 · cobertura 93/100, [info] narrative_wave: ola 'quantum': 25 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 46, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 11/10/2026 14:57 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir QSB

Estudio de cómo se adquiere QSB, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 09/10/2026 15:16 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 09/10/2026 14:57 UTC | pumpswap `58rYv8o…RQSx` | $21.430 | 10% | 0,933% | 9,333% | 93,326% | $107 | $321 |
| consulta 09/10/2026 15:15 UTC | pumpswap `58rYv8o…RQSx` | $8.362 | 10% | 2,392% | 23,918% | 239,176% | $42 | $125 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5`
5. Configurar el slippage: 10% (liquidez $8.362, consulta 09/10/2026 15:15 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5) y el par en DexScreener (https://dexscreener.com/solana/58rYv8ojei9fUdDzzZLh3GpmfCHz87e3uFRaY9NnRQSx); mint authority / freeze authority: revocada / revocada · holders 2.508 · top-10 124,40% (consulta 09/10/2026 15:15 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5
- Par en DexScreener: https://dexscreener.com/solana/58rYv8ojei9fUdDzzZLh3GpmfCHz87e3uFRaY9NnRQSx
- Página del lanzamiento (pump.fun): https://pump.fun/coin/DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.508 · top-10 124,40% (consulta 09/10/2026 15:15 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Quantum Safe Bitcoin / QSB | registro de la detección (pumpportal_live) |
| Mint / contrato | `DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `58rYv8ojei9fUdDzzZLh3GpmfCHz87e3uFRaY9NnRQSx` | DexScreener, al detectar (2 par(es) en la consulta 09/10/2026 15:15 UTC) |
| Deployer | `29yFzeBZgxf5zqrAkKXwgZtQehRf4pL8WbV2nRJikbw8` | PumpPortal (evento create), al detectar |
| Par creado | 09/10/2026 14:45 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,8 min / 11,8 min / 30,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 09/10/2026 15:15 UTC |
| Holders / top-10 | 2.508 / 124,40% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 09/10/2026 15:15 UTC |
| Holders efectivos del top-10 | 2,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 09/10/2026 15:15 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 09/10/2026 15:15 UTC |
| Links | DexScreener: https://dexscreener.com/solana/58rYv8ojei9fUdDzzZLh3GpmfCHz87e3uFRaY9NnRQSx · Solscan: https://solscan.io/token/DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5 · pump.fun: https://pump.fun/coin/DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5 · web: https://github.com/avihu28 · twitter: https://x.com/ddddddd8a/status/2108567707624812964 | consulta 09/10/2026 15:15 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 09/10/2026 15:15 UTC)
- **Historia:**
  - Par creado el 09/10/2026 14:45 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 09/10/2026 14:57 UTC, con el par a 11,8 min de creado: precio $0,00006122, mcap $61.224, liquidez $21.430.
  - Velas de 1 h de GeckoTerminal (2, desde 09/10/2026 14:00 UTC): apertura $0,00003890 · máximo $0,00009811 (09/10/2026 14:00 UTC) · mínimo $0,00001062 (09/10/2026 15:00 UTC) · último cierre $0,00001248.
  - En la consulta 09/10/2026 15:15 UTC: precio $0,00001287, liquidez $8.362, FDV $12.879.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 09/10/2026 14:57 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00006122 |
| Liquidez | $21.430 |
| MCap | $61.224 |
| Volumen 24 h | $251.335 |
| Cambio 24 h | +42% |
| Cambio m5 / h1 | -10,5% / +42,1% |
| Volumen m5 / h1 | $71.920 / $251.335 |
| Trades m5 (compras / ventas) | 1.045 / 781 |
| Edad del par | 11,8 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 46; motivos sin regla: young-0.4 · edad 11.8 min · pesos info 59 / estructura 20 / precio 20 · info 23.0 · estructura 12.9 · precio/volumen 10.2 · cobertura 93/100, [info] narrative_wave: ola 'quantum': 25 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 2064 · top-10 35.9 % → +2.5, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 2064/5759 = 0.36 → +0.6, [precio/volumen] volume_acceleration: vol 5 min ×3.4 la tasa horaria (s 0.77), [precio/volumen] buy_pressure_shift: compras 57% en 5 min vs 57% en 1 h (s 0.03), [precio/volumen] liquidity_inflow: liquidez +24% en 8 min (s 0.81), [precio/volumen] holder_accumulation: holders 719→2064 (+224.2/min) · top10 38.5%→35.9% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=21430.3, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 46 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-09T14:57:34+00:00, sin estado previo): **35** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Subida 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 41 de 24.984 tokens analizados (0,16%) quedan ≥ 56. Con score 35, este activo queda en el percentil 98,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 09/10/2026 14:57 UTC, hasta 11/10/2026 14:57 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -10,5% · h1 +42,1% · h24 +42% · volumen m5/h1 0,29 · edad del par 11,8 min.
- **Precio de entrada** (alerta): $0,00006122.
- **Consulta 09/10/2026 15:15 UTC:** $0,00001287 (-79,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5_2026-10-09_145734.json` · blob `b9fe8c74eb874bd811bb7b1da084e90e70dbcb9a` · commit `511fa5c` (2026-10-09T15:09:27Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-09_145734`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5 · registro · 09/10/2026 14:57 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5 · HTTP 200 · 09/10/2026 15:15 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5/report · HTTP 200 · 09/10/2026 15:15 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5 · HTTP 200 · 09/10/2026 15:15 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/58rYv8ojei9fUdDzzZLh3GpmfCHz87e3uFRaY9NnRQSx/ohlcv/hour?limit=1000 · HTTP 200 · 09/10/2026 15:16 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5 · HTTP 404 · 09/10/2026 15:16 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=QSBUSDT · HTTP 400 · 09/10/2026 15:16 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/QSB-USD · HTTP 404 · 09/10/2026 15:16 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $8.362 vs $8.150 → 2,54%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00001287 vs $0,00001248 → 3,06%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5_2026-10-09_145734.json',encoding='utf-8'));d=d.get('DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5',d);p=mock.patch('time.time',return_value=1791557854);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint DiHNMd2GCsjc73jMphP7V5RPUBcW3sYJbCvoGhiD5Pm5 --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 09/10/2026 15:16 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `53a2ad2f9f208065…`
