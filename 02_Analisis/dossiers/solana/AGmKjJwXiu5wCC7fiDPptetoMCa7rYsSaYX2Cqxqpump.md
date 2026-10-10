# lil uzi cat (uzicat) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00009838 · liquidez $26.450 · mcap $98.380 (al detectar)  
Detectado el 10/10/2026 21:53 UTC por: young-0.4 · edad 14.3 min · pesos info 58 / estructura 21 / precio 21 · info 17.4 · estructura 16.1 · precio/volumen 11.9 · cobertura 84/100, [info] narrative_wave: ola 'cat': 8 lanzamientos más en 1 h → +14.5, [info] dex_profile: perfil pago en DexScreener → +2.9 (score 45, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 12/10/2026 21:53 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir uzicat

Estudio de cómo se adquiere uzicat, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 10/10/2026 22:11 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 10/10/2026 21:53 UTC | pumpswap `B3TmYR7…kXoJ` | $26.450 | 10% | 0,756% | 7,562% | 75,615% | $132 | $397 |
| consulta 10/10/2026 22:11 UTC | pumpswap `B3TmYR7…kXoJ` | $31.395 | 10% | 0,637% | 6,370% | 63,704% | $157 | $471 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump`
5. Configurar el slippage: 10% (liquidez $31.395, consulta 10/10/2026 22:11 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump) y el par en DexScreener (https://dexscreener.com/solana/B3TmYR7S7TbfWybN6Bxkn7WWHoAP8YKBud3VNdkokXoJ); mint authority / freeze authority: revocada / revocada · holders 3.658 · top-10 27,90% (consulta 10/10/2026 22:11 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump
- Par en DexScreener: https://dexscreener.com/solana/B3TmYR7S7TbfWybN6Bxkn7WWHoAP8YKBud3VNdkokXoJ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.658 · top-10 27,90% (consulta 10/10/2026 22:11 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | lil uzi cat / uzicat | registro de la detección (pumpportal_live) |
| Mint / contrato | `AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `B3TmYR7S7TbfWybN6Bxkn7WWHoAP8YKBud3VNdkokXoJ` | DexScreener, al detectar (6 par(es) en la consulta 10/10/2026 22:11 UTC) |
| Deployer | `G1yeL2A71oRo14U8UvPLDiDkoHAHY8quq8uKBz2AGoKT` | PumpPortal (evento create), al detectar |
| Par creado | 10/10/2026 21:38 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 14,3 min / 14,3 min / 32,5 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 10/10/2026 22:11 UTC |
| Holders / top-10 | 3.658 / 27,90% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 10/10/2026 22:11 UTC |
| Holders efectivos del top-10 | 3,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 10/10/2026 22:11 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 10/10/2026 22:11 UTC |
| Links | DexScreener: https://dexscreener.com/solana/B3TmYR7S7TbfWybN6Bxkn7WWHoAP8YKBud3VNdkokXoJ · Solscan: https://solscan.io/token/AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump · pump.fun: https://pump.fun/coin/AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump · twitter: https://x.com/_numanuk/status/2109033918683111935?s=46 | consulta 10/10/2026 22:11 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 10/10/2026 22:11 UTC)
- **Historia:**
  - Par creado el 10/10/2026 21:38 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 10/10/2026 21:53 UTC, con el par a 14,3 min de creado: precio $0,00009838, mcap $98.380, liquidez $26.450.
  - Velas de 1 h de GeckoTerminal (2, desde 10/10/2026 21:00 UTC): apertura $0,00005104 · máximo $0,0001905 (10/10/2026 22:00 UTC) · mínimo $0,00004047 (10/10/2026 21:00 UTC) · último cierre $0,0001266.
  - En la consulta 10/10/2026 22:11 UTC: precio $0,0001263, liquidez $31.395, FDV $126.386.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 10/10/2026 21:53 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00009838 |
| Liquidez | $26.450 |
| MCap | $98.380 |
| Volumen 24 h | $120.647 |
| Cambio 24 h | +107% |
| Cambio m5 / h1 | +53,4% / +107,0% |
| Volumen m5 / h1 | $38.192 / $120.647 |
| Trades m5 (compras / ventas) | 627 / 481 |
| Edad del par | 14,3 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 45; motivos sin regla: young-0.4 · edad 14.3 min · pesos info 58 / estructura 21 / precio 21 · info 17.4 · estructura 16.1 · precio/volumen 11.9 · cobertura 84/100, [info] narrative_wave: ola 'cat': 8 lanzamientos más en 1 h → +14.5, [info] dex_profile: perfil pago en DexScreener → +2.9, [estructura] bonding_progress: graduado (pumpswap) → +10.1, [estructura] holders_struct: holders 2466 · top-10 29.3 % → +5.1, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 2466/3235 = 0.76 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×3.8 la tasa horaria (s 0.92), [precio/volumen] liquidity_inflow: liquidez +39% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1864→2466 (+100.3/min) · top10 32.1%→29.3% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=26449.62, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 45 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-10T21:53:03+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 45 de 27.997 tokens analizados (0,16%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 10/10/2026 21:53 UTC, hasta 12/10/2026 21:53 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +53,4% · h1 +107,0% · h24 +107% · volumen m5/h1 0,32 · edad del par 14,3 min.
- **Precio de entrada** (alerta): $0,00009838.
- **Consulta 10/10/2026 22:11 UTC:** $0,0001263 (+28,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump_2026-10-10_215303.json` · blob `1618542951d27812111636fed43d2ca186aafabf` · commit `1778442` (2026-10-10T22:04:34Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-10_215303`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump · registro · 10/10/2026 21:53 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump · HTTP 200 · 10/10/2026 22:11 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump/report · HTTP 200 · 10/10/2026 22:11 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump · HTTP 200 · 10/10/2026 22:11 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/B3TmYR7S7TbfWybN6Bxkn7WWHoAP8YKBud3VNdkokXoJ/ohlcv/hour?limit=1000 · HTTP 200 · 10/10/2026 22:11 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump · HTTP 404 · 10/10/2026 22:11 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=UZICATUSDT · HTTP 400 · 10/10/2026 22:11 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/UZICAT-USD · HTTP 404 · 10/10/2026 22:11 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $31.395 vs $30.379 → 3,24%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001263 vs $0,0001266 → 0,24%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump_2026-10-10_215303.json',encoding='utf-8'));d=d.get('AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump',d);p=mock.patch('time.time',return_value=1791669183);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint AGmKjJwXiu5wCC7fiDPptetoMCa7rYsSaYX2Cqxqpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 10/10/2026 22:11 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `7d0ef23d1346d824…`
