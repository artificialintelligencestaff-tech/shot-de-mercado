# Larpcoin (LARP) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00008926 · liquidez $25.601 · mcap $89.261 (al detectar)  
Detectado el 22/10/2026 23:35 UTC por: young-0.4 · edad 10.1 min · pesos info 60 / estructura 20 / precio 20 · info 15.0 · estructura 14.5 · precio/volumen 11.7 · cobertura 83/100, [info] narrative_wave: ola 'larp': 9 lanzamientos más en 1 h → +15.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 24/10/2026 23:35 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir LARP

Estudio de cómo se adquiere LARP, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 22/10/2026 23:54 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 22/10/2026 23:35 UTC | pumpswap `AM15gVr…zRkQ` | $25.601 | 10% | 0,781% | 7,812% | 78,123% | $128 | $384 |
| consulta 22/10/2026 23:53 UTC | pumpswap `AM15gVr…zRkQ` | $5.376 | 10% | 3,720% | 37,204% | 372,042% | $27 | $81 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump`
5. Configurar el slippage: 10% (liquidez $5.376, consulta 22/10/2026 23:53 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump) y el par en DexScreener (https://dexscreener.com/solana/AM15gVr8euiWaScjmMLNCHtzZmQYgcpGLySEpZH6zRkQ); mint authority / freeze authority: revocada / revocada · holders 2.255 · top-10 78,25% (consulta 22/10/2026 23:53 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump
- Par en DexScreener: https://dexscreener.com/solana/AM15gVr8euiWaScjmMLNCHtzZmQYgcpGLySEpZH6zRkQ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.255 · top-10 78,25% (consulta 22/10/2026 23:53 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Larpcoin / LARP | registro de la detección (pumpportal_live) |
| Mint / contrato | `4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `AM15gVr8euiWaScjmMLNCHtzZmQYgcpGLySEpZH6zRkQ` | DexScreener, al detectar (11 par(es) en la consulta 22/10/2026 23:53 UTC) |
| Deployer | `CLYJnCAVmRE8iEzP88ujM9ymfBT4B7pBfHHxmNrVASa6` | PumpPortal (evento create), al detectar |
| Par creado | 22/10/2026 23:25 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,1 min / 10,1 min / 28,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 22/10/2026 23:53 UTC |
| Holders / top-10 | 2.255 / 78,25% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 22/10/2026 23:53 UTC |
| Holders efectivos del top-10 | 1,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 22/10/2026 23:53 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 22/10/2026 23:53 UTC |
| Links | DexScreener: https://dexscreener.com/solana/AM15gVr8euiWaScjmMLNCHtzZmQYgcpGLySEpZH6zRkQ · Solscan: https://solscan.io/token/4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump · pump.fun: https://pump.fun/coin/4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump · twitter: https://x.com/i/communities/2019581792840306728 | consulta 22/10/2026 23:53 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 22/10/2026 23:53 UTC)
- **Historia:**
  - Par creado el 22/10/2026 23:25 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 22/10/2026 23:35 UTC, con el par a 10,1 min de creado: precio $0,00008926, mcap $89.261, liquidez $25.601.
  - Velas de 1 h de GeckoTerminal (1, desde 22/10/2026 23:00 UTC): apertura $0,00004258 · máximo $0,0001076 (22/10/2026 23:00 UTC) · mínimo $0,000005283 (22/10/2026 23:00 UTC) · último cierre $0,000005283.
  - En la consulta 22/10/2026 23:53 UTC: precio $0,000005680, liquidez $5.376, FDV $5.681.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 22/10/2026 23:35 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00008926 |
| Liquidez | $25.601 |
| MCap | $89.261 |
| Volumen 24 h | $258.229 |
| Cambio 24 h | +112% |
| Cambio m5 / h1 | +40,2% / +112,0% |
| Volumen m5 / h1 | $102.065 / $258.229 |
| Trades m5 (compras / ventas) | 1.295 / 1.060 |
| Edad del par | 10,1 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 10.1 min · pesos info 60 / estructura 20 / precio 20 · info 15.0 · estructura 14.5 · precio/volumen 11.7 · cobertura 83/100, [info] narrative_wave: ola 'larp': 9 lanzamientos más en 1 h → +15.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1973 · top-10 32.0 % → +2.4, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.0, [estructura] holder_to_txn_ratio: holders/txns 1973/6019 = 0.33 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×4.7 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 55% en 5 min vs 55% en 1 h (s 0.02), [precio/volumen] liquidity_inflow: liquidez +167% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1478→1973 (+82.5/min) · top10 35.2%→32.0% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=25600.52, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-22T23:35:31+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 75 de 44.367 tokens analizados (0,17%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 22/10/2026 23:35 UTC, hasta 24/10/2026 23:35 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +40,2% · h1 +112,0% · h24 +112% · volumen m5/h1 0,40 · edad del par 10,1 min.
- **Precio de entrada** (alerta): $0,00008926.
- **Consulta 22/10/2026 23:53 UTC:** $0,000005680 (-93,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump_2026-10-22_233531.json` · blob `995d55ecab8348a22314221fe84f1339301b3701` · commit `210fba4` (2026-10-22T23:45:35Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-22_233531`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump · registro · 22/10/2026 23:35 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump · HTTP 200 · 22/10/2026 23:53 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump/report · HTTP 200 · 22/10/2026 23:53 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump · HTTP 200 · 22/10/2026 23:53 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/AM15gVr8euiWaScjmMLNCHtzZmQYgcpGLySEpZH6zRkQ/ohlcv/hour?limit=1000 · HTTP 200 · 22/10/2026 23:53 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump · HTTP 404 · 22/10/2026 23:53 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=LARPUSDT · HTTP 400 · 22/10/2026 23:53 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/LARP-USD · HTTP 404 · 22/10/2026 23:53 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $5.376 vs $4.733 → 11,95%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000005680 vs $0,000005283 → 7,00%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump_2026-10-22_233531.json',encoding='utf-8'));d=d.get('4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump',d);p=mock.patch('time.time',return_value=1792712131);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 4aVoUcyhHmhxfUSzDaUpEKchuc8V8d1cGphxakvVpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 22/10/2026 23:54 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `4e599c6044a339a9…`
