# Ollie (Ollie) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00001439 · liquidez $8.712 · mcap $14.394 (al detectar)  
Detectado el 20/10/2026 06:18 UTC por: young-0.4 · edad 10.7 min · pesos info 60 / estructura 20 / precio 20 · info 22.8 · estructura 14.9 · precio/volumen 8.3 · cobertura 93/100, [info] narrative_wave: ola 'ollie': 6 lanzamientos más en 1 h → +11.2, [info] metadata_socials: enlaces ['twitter'] · descripción 29 caracteres → +2.7 (score 46, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 22/10/2026 06:18 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Ollie

Estudio de cómo se adquiere Ollie, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 20/10/2026 06:27 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 20/10/2026 06:18 UTC | pumpswap `5abbToS…RtRi` | $8.712 | 10% | 2,296% | 22,956% | 229,557% | $44 | $131 |
| consulta 20/10/2026 06:27 UTC | pumpswap `5abbToS…RtRi` | $7.183 | 10% | 2,784% | 27,843% | 278,427% | $36 | $108 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump`
5. Configurar el slippage: 10% (liquidez $7.183, consulta 20/10/2026 06:27 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump) y el par en DexScreener (https://dexscreener.com/solana/5abbToSTeofz8JdmqeWbs7rAAJ6iJruouBxZm33xRtRi); mint authority / freeze authority: revocada / revocada · holders 1.097 · top-10 64,33% (consulta 20/10/2026 06:27 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump
- Par en DexScreener: https://dexscreener.com/solana/5abbToSTeofz8JdmqeWbs7rAAJ6iJruouBxZm33xRtRi
- Página del lanzamiento (pump.fun): https://pump.fun/coin/7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.097 · top-10 64,33% (consulta 20/10/2026 06:27 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Ollie / Ollie | registro de la detección (pumpportal_live) |
| Mint / contrato | `7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `5abbToSTeofz8JdmqeWbs7rAAJ6iJruouBxZm33xRtRi` | DexScreener, al detectar (3 par(es) en la consulta 20/10/2026 06:27 UTC) |
| Deployer | `FaUsobigSFqqivRm3PM6nidQD26QMwk3goi69x3Pi2ce` | PumpPortal (evento create), al detectar |
| Par creado | 20/10/2026 06:07 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,7 min / 10,7 min / 20,0 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 20/10/2026 06:27 UTC |
| Holders / top-10 | 1.097 / 64,33% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 20/10/2026 06:27 UTC |
| Holders efectivos del top-10 | 2,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 20/10/2026 06:27 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 20/10/2026 06:27 UTC |
| Links | DexScreener: https://dexscreener.com/solana/5abbToSTeofz8JdmqeWbs7rAAJ6iJruouBxZm33xRtRi · Solscan: https://solscan.io/token/7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump · pump.fun: https://pump.fun/coin/7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump · twitter: https://x.com/ddddddd8a/status/2112424397432631489 · facebook: https://www.facebook.com/100064614645841/posts/ollie-the-prickle-less-hedgehog-update-well-he-seems-to-have-gone-viral-everyone/1526408942856246/ | consulta 20/10/2026 06:27 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 20/10/2026 06:27 UTC)
- **Historia:**
  - Par creado el 20/10/2026 06:07 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 20/10/2026 06:18 UTC, con el par a 10,7 min de creado: precio $0,00001439, mcap $14.394, liquidez $8.712.
  - Velas de 1 h de GeckoTerminal (1, desde 20/10/2026 06:00 UTC): apertura $0,00004294 · máximo $0,00004447 (20/10/2026 06:00 UTC) · mínimo $0,000008965 (20/10/2026 06:00 UTC) · último cierre $0,00001292.
  - En la consulta 20/10/2026 06:27 UTC: precio $0,00001101, liquidez $7.183, FDV $11.013.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 20/10/2026 06:18 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00001439 |
| Liquidez | $8.712 |
| MCap | $14.394 |
| Volumen 24 h | $59.732 |
| Cambio 24 h | -67% |
| Cambio m5 / h1 | -55,7% / -66,8% |
| Volumen m5 / h1 | $19.623 / $59.732 |
| Trades m5 (compras / ventas) | 303 / 306 |
| Edad del par | 10,7 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 46; motivos sin regla: young-0.4 · edad 10.7 min · pesos info 60 / estructura 20 / precio 20 · info 22.8 · estructura 14.9 · precio/volumen 8.3 · cobertura 93/100, [info] narrative_wave: ola 'ollie': 6 lanzamientos más en 1 h → +11.2, [info] metadata_socials: enlaces ['twitter'] · descripción 29 caracteres → +2.7, [info] dex_profile: perfil pago en DexScreener → +3.0, [info] mentions: menciones 1 h 2 (1 familias) · 26 h 2 → +6.0, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1012 · top-10 49.3 % → +2.4, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.0, [estructura] holder_to_txn_ratio: holders/txns 1012/1967 = 0.51 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×3.9 la tasa horaria (s 0.98), [precio/volumen] holder_accumulation: holders 743→1012 (+44.8/min) · top10 45.5%→49.3% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=8712.43, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 46 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-20T06:18:17+00:00, sin estado previo): **5** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen decente, Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 68 de 41.673 tokens analizados (0,16%) quedan ≥ 56. Con score 5, este activo queda en el percentil 87,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 20/10/2026 06:18 UTC, hasta 22/10/2026 06:18 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -55,7% · h1 -66,8% · h24 -67% · volumen m5/h1 0,33 · edad del par 10,7 min.
- **Precio de entrada** (alerta): $0,00001439.
- **Consulta 20/10/2026 06:27 UTC:** $0,00001101 (-23,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump_2026-10-20_061817.json` · blob `a2e1eccc12cdab4e4e1c88de99191c4a8c846c53` · commit `f9d1eb3` (2026-10-20T06:19:44Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-20_061817`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump · registro · 20/10/2026 06:18 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump · HTTP 200 · 20/10/2026 06:27 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump/report · HTTP 200 · 20/10/2026 06:27 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump · HTTP 200 · 20/10/2026 06:27 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/5abbToSTeofz8JdmqeWbs7rAAJ6iJruouBxZm33xRtRi/ohlcv/hour?limit=1000 · HTTP 200 · 20/10/2026 06:27 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump · HTTP 404 · 20/10/2026 06:27 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=OLLIEUSDT · HTTP 400 · 20/10/2026 06:27 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/OLLIE-USD · HTTP 404 · 20/10/2026 06:27 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $7.183 vs $7.953 → 9,68%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00001101 vs $0,00001292 → 14,79%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump_2026-10-20_061817.json',encoding='utf-8'));d=d.get('7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump',d);p=mock.patch('time.time',return_value=1792477097);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 7p4v45eyQWQGpvNRGNQDrUoyyC3VhFWjKaALFexapump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 20/10/2026 06:27 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `0f2517298c9e5fce…`
