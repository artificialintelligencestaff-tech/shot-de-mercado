# Phantom Cat (PCAT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001262 · liquidez $31.041 · mcap $126.232 (al detectar)  
Detectado el 03/10/2026 08:52 UTC por: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 20.6 · estructura 13.1 · precio/volumen 10.3 · cobertura 93/100, [info] narrative_wave: ola 'phantom': 9 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.7 (score 44, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 05/10/2026 08:52 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir PCAT

Estudio de cómo se adquiere PCAT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 03/10/2026 09:13 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 03/10/2026 08:52 UTC | pumpswap `DuJRqJT…ZJyq` | $31.041 | 10% | 0,644% | 6,443% | 64,430% | $155 | $466 |
| consulta 03/10/2026 09:13 UTC | pumpswap `DuJRqJT…ZJyq` | $42.275 | 10% | 0,473% | 4,731% | 47,309% | $211 | $634 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV`
5. Configurar el slippage: 10% (liquidez $42.275, consulta 03/10/2026 09:13 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV) y el par en DexScreener (https://dexscreener.com/solana/DuJRqJTcyHNB56xomwF6eqaQdQYp3RJmryEf5vr1ZJyq); mint authority / freeze authority: revocada / revocada · holders 2.995 · top-10 30,23% (consulta 03/10/2026 09:13 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV
- Par en DexScreener: https://dexscreener.com/solana/DuJRqJTcyHNB56xomwF6eqaQdQYp3RJmryEf5vr1ZJyq
- Página del lanzamiento (pump.fun): https://pump.fun/coin/5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.995 · top-10 30,23% (consulta 03/10/2026 09:13 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Phantom Cat / PCAT | registro de la detección (pumpportal_live) |
| Mint / contrato | `5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DuJRqJTcyHNB56xomwF6eqaQdQYp3RJmryEf5vr1ZJyq` | DexScreener, al detectar (6 par(es) en la consulta 03/10/2026 09:13 UTC) |
| Deployer | `GHKNXvdtd8Gj6au4XGqimvRS96v8m5HBBjdSiKcYZua4` | PumpPortal (evento create), al detectar |
| Par creado | 03/10/2026 08:42 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,4 min / 10,4 min / 31,2 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 03/10/2026 09:13 UTC |
| Holders / top-10 | 2.995 / 30,23% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 03/10/2026 09:13 UTC |
| Holders efectivos del top-10 | 5,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 03/10/2026 09:13 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 03/10/2026 09:13 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DuJRqJTcyHNB56xomwF6eqaQdQYp3RJmryEf5vr1ZJyq · Solscan: https://solscan.io/token/5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV · pump.fun: https://pump.fun/coin/5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV · twitter: https://x.com/NubziDev/status/2106300955171991720?s=20 | consulta 03/10/2026 09:13 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 03/10/2026 09:13 UTC)
- **Historia:**
  - Par creado el 03/10/2026 08:42 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 03/10/2026 08:52 UTC, con el par a 10,4 min de creado: precio $0,0001262, mcap $126.232, liquidez $31.041.
  - Velas de 1 h de GeckoTerminal (2, desde 03/10/2026 08:00 UTC): apertura $0,00004820 · máximo $0,0002371 (03/10/2026 09:00 UTC) · mínimo $0,00004564 (03/10/2026 08:00 UTC) · último cierre $0,0001989.
  - En la consulta 03/10/2026 09:13 UTC: precio $0,0002181, liquidez $42.275, FDV $218.167.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 03/10/2026 08:52 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001262 |
| Liquidez | $31.041 |
| MCap | $126.232 |
| Volumen 24 h | $243.959 |
| Cambio 24 h | +162% |
| Cambio m5 / h1 | +34,8% / +162,0% |
| Volumen m5 / h1 | $71.824 / $243.959 |
| Trades m5 (compras / ventas) | 910 / 735 |
| Edad del par | 10,4 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 44; motivos sin regla: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 20.6 · estructura 13.1 · precio/volumen 10.3 · cobertura 93/100, [info] narrative_wave: ola 'phantom': 9 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.7, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1819 · top-10 35.5 % → +2.4, [estructura] dev_wallet: creador compró 8.3 % del supply → +0.5, [estructura] holder_to_txn_ratio: holders/txns 1819/5556 = 0.33 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×3.5 la tasa horaria (s 0.81), [precio/volumen] liquidity_inflow: liquidez +25% en 8 min (s 0.85), [precio/volumen] holder_accumulation: holders 1422→1819 (+66.2/min) · top10 35.6%→35.5% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=31041.37, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 44 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-03T08:52:55+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 9 de 10.140 tokens analizados (0,09%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 03/10/2026 08:52 UTC, hasta 05/10/2026 08:52 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +34,8% · h1 +162,0% · h24 +162% · volumen m5/h1 0,29 · edad del par 10,4 min.
- **Precio de entrada** (alerta): $0,0001262.
- **Consulta 03/10/2026 09:13 UTC:** $0,0002181 (+72,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV_2026-10-03_085255.json` · blob `011a616144df1b13a80ada1253e77fabbe6459d0` · commit `fce2ca1` (2026-10-03T09:07:20Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-03_085255`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV · registro · 03/10/2026 08:52 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV · HTTP 200 · 03/10/2026 09:13 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV/report · HTTP 200 · 03/10/2026 09:13 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV · HTTP 200 · 03/10/2026 09:13 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DuJRqJTcyHNB56xomwF6eqaQdQYp3RJmryEf5vr1ZJyq/ohlcv/hour?limit=1000 · HTTP 200 · 03/10/2026 09:13 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV · HTTP 404 · 03/10/2026 09:13 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=PCATUSDT · HTTP 400 · 03/10/2026 09:13 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/PCAT-USD · HTTP 404 · 03/10/2026 09:13 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $42.275 vs $48.358 → 12,58%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0002181 vs $0,0001989 → 8,80%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV_2026-10-03_085255.json',encoding='utf-8'));d=d.get('5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV',d);p=mock.patch('time.time',return_value=1791017575);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 5dyyu2XWGhWHua52JjfhoNSbDLni654DD5yR6DcYe3zV --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 03/10/2026 09:13 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `daec6834fdab3524…`
