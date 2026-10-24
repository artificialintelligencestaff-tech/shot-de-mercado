# PEPE PILL (PEPILL) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001966 · liquidez $68.784 · mcap $196.669 (al detectar)  
Detectado el 24/10/2026 10:42 UTC por: young-0.4 · edad 12.7 min · pesos info 59 / estructura 21 / precio 21 · info 16.5 · estructura 14.8 · precio/volumen 8.6 · cobertura 84/100, [info] narrative_wave: ola 'pepe': 1 lanzamientos más en 1 h → +1.8, [info] trending_match: 'pepe' en trending #12 Pepe → +5.9 (score 40, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 26/10/2026 10:42 UTC (< 48 h) · vigente: quedan 45,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir PEPILL

Estudio de cómo se adquiere PEPILL, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 24/10/2026 13:08 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 24/10/2026 10:42 UTC | pumpswap `D7BowV4…Ncbk` | $68.784 | 5% | 0,291% | 2,908% | 29,077% | $344 | $1.032 |
| consulta 24/10/2026 13:07 UTC | pumpswap `D7BowV4…Ncbk` | $2.259 | 10% | 8,853% | 88,530% | 885,297% | $11 | $34 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump`
5. Configurar el slippage: 10% (liquidez $2.259, consulta 24/10/2026 13:07 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump) y el par en DexScreener (https://dexscreener.com/solana/D7BowV4pby8J8UmVxkd3gRL9rSoBiZVQWqqpWQUbNcbk); mint authority / freeze authority: revocada / revocada · holders 1.137 · top-10 99,27% (consulta 24/10/2026 13:07 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump
- Par en DexScreener: https://dexscreener.com/solana/D7BowV4pby8J8UmVxkd3gRL9rSoBiZVQWqqpWQUbNcbk
- Página del lanzamiento (pump.fun): https://pump.fun/coin/BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.137 · top-10 99,27% (consulta 24/10/2026 13:07 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | PEPE PILL / PEPILL | registro de la detección (pumpportal_live) |
| Mint / contrato | `BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `D7BowV4pby8J8UmVxkd3gRL9rSoBiZVQWqqpWQUbNcbk` | DexScreener, al detectar (3 par(es) en la consulta 24/10/2026 13:07 UTC) |
| Deployer | `3BSykVa4NaYHfET1Wzqxt4LKj1k7PEr1832MZdL1dpGT` | PumpPortal (evento create), al detectar |
| Par creado | 24/10/2026 10:30 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 12,7 min / 12,7 min / 2,6 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 24/10/2026 13:07 UTC |
| Holders / top-10 | 1.137 / 99,27% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 24/10/2026 13:07 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 24/10/2026 13:07 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 24/10/2026 13:07 UTC |
| Links | DexScreener: https://dexscreener.com/solana/D7BowV4pby8J8UmVxkd3gRL9rSoBiZVQWqqpWQUbNcbk · Solscan: https://solscan.io/token/BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump · pump.fun: https://pump.fun/coin/BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump · web: https://pepepill.fun/ · twitter: https://x.com/pepepillsol | consulta 24/10/2026 13:07 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 24/10/2026 13:07 UTC)
- **Historia:**
  - Par creado el 24/10/2026 10:30 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 24/10/2026 10:42 UTC, con el par a 12,7 min de creado: precio $0,0001966, mcap $196.669, liquidez $68.784.
  - Velas de 1 h de GeckoTerminal (3, desde 24/10/2026 10:00 UTC): apertura $0,00004172 · máximo $0,0003402 (24/10/2026 10:00 UTC) · mínimo $0,000002079 (24/10/2026 11:00 UTC) · último cierre $0,000002094.
  - En la consulta 24/10/2026 13:07 UTC: precio $0,000002093, liquidez $2.259, FDV $2.041.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 24/10/2026 10:42 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001966 |
| Liquidez | $68.784 |
| MCap | $196.669 |
| Volumen 24 h | $575.711 |
| Cambio 24 h | +369% |
| Cambio m5 / h1 | +64,1% / +369,0% |
| Volumen m5 / h1 | $226.695 / $575.711 |
| Trades m5 (compras / ventas) | 750 / 605 |
| Edad del par | 12,7 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 40; motivos sin regla: young-0.4 · edad 12.7 min · pesos info 59 / estructura 21 / precio 21 · info 16.5 · estructura 14.8 · precio/volumen 8.6 · cobertura 84/100, [info] narrative_wave: ola 'pepe': 1 lanzamientos más en 1 h → +1.8, [info] trending_match: 'pepe' en trending #12 Pepe → +5.9, [info] dex_profile: perfil pago en DexScreener → +2.9, [info] mentions: menciones 1 h 2 (1 familias) · 26 h 2 → +5.9, [estructura] bonding_progress: graduado (pumpswap) → +9.9, [estructura] holders_struct: holders 1020 · top-10 30.7 % → +2.5, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.0, [estructura] holder_to_txn_ratio: holders/txns 1020/4493 = 0.23 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×4.7 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +92% en 8 min (s 1.00), [flag, no suma] tradable=True, liquidity_usd=68783.94, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=22257.4, score 40 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-24T10:42:59+00:00, sin estado previo): **50** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez decente, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 75 de 45.691 tokens analizados (0,16%) quedan ≥ 56. Con score 50, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 24/10/2026 10:42 UTC, hasta 26/10/2026 10:42 UTC · vigente: quedan 45,6 h.
- **Aceleración al detectar:** cambio m5 +64,1% · h1 +369,0% · h24 +369% · volumen m5/h1 0,39 · edad del par 12,7 min.
- **Precio de entrada** (alerta): $0,0001966.
- **Consulta 24/10/2026 13:07 UTC:** $0,000002093 (-98,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump_2026-10-24_104259.json` · blob `3398b204d92191f6adaeb6e10a61575279b294d8` · commit `bb3ff33` (2026-10-24T12:57:13Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-24_104259`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump · registro · 24/10/2026 10:42 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump · HTTP 200 · 24/10/2026 13:07 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump/report · HTTP 200 · 24/10/2026 13:08 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump · HTTP 200 · 24/10/2026 13:08 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/D7BowV4pby8J8UmVxkd3gRL9rSoBiZVQWqqpWQUbNcbk/ohlcv/hour?limit=1000 · HTTP 200 · 24/10/2026 13:08 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump · HTTP 404 · 24/10/2026 13:08 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=PEPILLUSDT · HTTP 400 · 24/10/2026 13:08 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/PEPILL-USD · HTTP 404 · 24/10/2026 13:08 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.259 vs $2.263 → 0,16%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002093 vs $0,000002094 → 0,04%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump_2026-10-24_104259.json',encoding='utf-8'));d=d.get('BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump',d);p=mock.patch('time.time',return_value=1792838579);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint BPEtujorjTND3qWFPT4jgz73Acr1SadgGyRYSUmHpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 24/10/2026 13:08 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `46191e770c2a8fd5…`
