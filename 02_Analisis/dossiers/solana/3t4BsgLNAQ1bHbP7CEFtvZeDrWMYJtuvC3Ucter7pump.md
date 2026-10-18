# Artificial Coin (AFC) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00008356 · liquidez $26.257 · mcap $83.408 (al detectar)  
Detectado el 18/10/2026 02:53 UTC por: young-0.4 · edad 11.3 min · pesos info 59 / estructura 20 / precio 20 · info 20.8 · estructura 15.0 · precio/volumen 12.2 · cobertura 84/100, [info] narrative_wave: ola 'afc': 14 lanzamientos más en 1 h → +14.8, [info] trending_match: 'artificial' en trending #13 Artificial Superintelligence Alliance → +5.9 (score 48, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 20/10/2026 02:53 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir AFC

Estudio de cómo se adquiere AFC, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 18/10/2026 03:23 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 18/10/2026 02:53 UTC | pumpswap `89JPenU…xMXx` | $26.257 | 10% | 0,762% | 7,617% | 76,169% | $131 | $394 |
| consulta 18/10/2026 03:23 UTC | pumpswap `89JPenU…xMXx` | $52.806 | 5% | 0,379% | 3,787% | 37,875% | $264 | $792 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump`
5. Configurar el slippage: 5% (liquidez $52.806, consulta 18/10/2026 03:23 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump) y el par en DexScreener (https://dexscreener.com/solana/89JPenUnoDKjoGzJ8NzVxDdariGiPGyMsmjF2mUoxMXx); mint authority / freeze authority: revocada / revocada · holders 4.267 · top-10 23,68% (consulta 18/10/2026 03:23 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump
- Par en DexScreener: https://dexscreener.com/solana/89JPenUnoDKjoGzJ8NzVxDdariGiPGyMsmjF2mUoxMXx
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.267 · top-10 23,68% (consulta 18/10/2026 03:23 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Artificial Coin / AFC | registro de la detección (pumpportal_live) |
| Mint / contrato | `3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `89JPenUnoDKjoGzJ8NzVxDdariGiPGyMsmjF2mUoxMXx` | DexScreener, al detectar (7 par(es) en la consulta 18/10/2026 03:23 UTC) |
| Deployer | `4pKsEyvDxWqp8Rz82z4ZtZ7RqKoQDa24QjmQHV3cJL6k` | PumpPortal (evento create), al detectar |
| Par creado | 18/10/2026 02:42 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,3 min / 11,3 min / 40,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 18/10/2026 03:23 UTC |
| Holders / top-10 | 4.267 / 23,68% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 18/10/2026 03:23 UTC |
| Holders efectivos del top-10 | 5,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 18/10/2026 03:23 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 18/10/2026 03:23 UTC |
| Links | DexScreener: https://dexscreener.com/solana/89JPenUnoDKjoGzJ8NzVxDdariGiPGyMsmjF2mUoxMXx · Solscan: https://solscan.io/token/3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump · pump.fun: https://pump.fun/coin/3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump · web: https://otcdesks.cash/coin/3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump · twitter: https://x.com/DexRynn/status/2111648830026362948 | consulta 18/10/2026 03:23 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 18/10/2026 03:23 UTC)
- **Historia:**
  - Par creado el 18/10/2026 02:42 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 18/10/2026 02:53 UTC, con el par a 11,3 min de creado: precio $0,00008356, mcap $83.408, liquidez $26.257.
  - Velas de 1 h de GeckoTerminal (2, desde 18/10/2026 02:00 UTC): apertura $0,00004115 · máximo $0,0005044 (18/10/2026 03:00 UTC) · mínimo $0,00001076 (18/10/2026 02:00 UTC) · último cierre $0,0003216.
  - En la consulta 18/10/2026 03:23 UTC: precio $0,0003364, liquidez $52.806, FDV $321.343.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 18/10/2026 02:53 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00008356 |
| Liquidez | $26.257 |
| MCap | $83.408 |
| Volumen 24 h | $464.854 |
| Cambio 24 h | +99% |
| Cambio m5 / h1 | -8,4% / +98,6% |
| Volumen m5 / h1 | $169.952 / $464.854 |
| Trades m5 (compras / ventas) | 2.152 / 1.742 |
| Edad del par | 11,3 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 48; motivos sin regla: young-0.4 · edad 11.3 min · pesos info 59 / estructura 20 / precio 20 · info 20.8 · estructura 15.0 · precio/volumen 12.2 · cobertura 84/100, [info] narrative_wave: ola 'afc': 14 lanzamientos más en 1 h → +14.8, [info] trending_match: 'artificial' en trending #13 Artificial Superintelligence Alliance → +5.9, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 2311 · top-10 27.3 % → +4.9, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 2311/11846 = 0.20 → +0.3, [precio/volumen] volume_acceleration: vol 5 min ×4.4 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 55% en 5 min vs 46% en 1 h (s 0.26), [precio/volumen] liquidity_inflow: liquidez +26% en 8 min (s 0.85), [precio/volumen] holder_accumulation: holders 931→2311 (+230.0/min) · top10 33.2%→27.3% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=26257.46, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=8659.81, score 48 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-18T02:53:56+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 65 de 39.151 tokens analizados (0,17%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 18/10/2026 02:53 UTC, hasta 20/10/2026 02:53 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -8,4% · h1 +98,6% · h24 +99% · volumen m5/h1 0,37 · edad del par 11,3 min.
- **Precio de entrada** (alerta): $0,00008356.
- **Consulta 18/10/2026 03:23 UTC:** $0,0003364 (+302,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump_2026-10-18_025356.json` · blob `dc29fef11996a88ad021509e43317dda912e3387` · commit `55cb222` (2026-10-18T03:16:42Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-18_025356`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump · registro · 18/10/2026 02:53 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump · HTTP 200 · 18/10/2026 03:23 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump/report · HTTP 200 · 18/10/2026 03:23 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump · HTTP 200 · 18/10/2026 03:23 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/89JPenUnoDKjoGzJ8NzVxDdariGiPGyMsmjF2mUoxMXx/ohlcv/hour?limit=1000 · HTTP 200 · 18/10/2026 03:23 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump · HTTP 404 · 18/10/2026 03:23 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AFCUSDT · HTTP 400 · 18/10/2026 03:23 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AFC-USD · HTTP 404 · 18/10/2026 03:23 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $52.806 vs $63.115 → 16,33%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0003364 vs $0,0003216 → 4,40%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump_2026-10-18_025356.json',encoding='utf-8'));d=d.get('3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump',d);p=mock.patch('time.time',return_value=1792292036);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3t4BsgLNAQ1bHbP7CEFtvZeDrWMYJtuvC3Ucter7pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 18/10/2026 03:23 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `b64a1468a5dc77b2…`
