# tout va bien (Bien) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00006289 · liquidez $20.278 · mcap $62.791 (al detectar)  
Detectado el 20/10/2026 04:03 UTC por: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 20.6 · estructura 12.9 · precio/volumen 12.7 · cobertura 93/100, [info] narrative_wave: ola 'bien': 13 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter'] · descripción 35 caracteres → +2.7 (score 46, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 22/10/2026 04:03 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Bien

Estudio de cómo se adquiere Bien, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 20/10/2026 04:27 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 20/10/2026 04:03 UTC | pumpswap `BoN8nuj…6UDV` | $20.278 | 10% | 0,986% | 9,863% | 98,631% | $101 | $304 |
| consulta 20/10/2026 04:27 UTC | pumpswap `BoN8nuj…6UDV` | $26.244 | 10% | 0,762% | 7,621% | 76,207% | $131 | $394 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump`
5. Configurar el slippage: 10% (liquidez $26.244, consulta 20/10/2026 04:27 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump) y el par en DexScreener (https://dexscreener.com/solana/BoN8nuj2w2eooRbEGnxru7hYR5pCT7xdLDqghmif6UDV); mint authority / freeze authority: revocada / revocada · holders 2.197 · top-10 30,57% (consulta 20/10/2026 04:27 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump
- Par en DexScreener: https://dexscreener.com/solana/BoN8nuj2w2eooRbEGnxru7hYR5pCT7xdLDqghmif6UDV
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.197 · top-10 30,57% (consulta 20/10/2026 04:27 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | tout va bien / Bien | registro de la detección (pumpportal_live) |
| Mint / contrato | `HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BoN8nuj2w2eooRbEGnxru7hYR5pCT7xdLDqghmif6UDV` | DexScreener, al detectar (4 par(es) en la consulta 20/10/2026 04:27 UTC) |
| Deployer | `AufH68UFBGSVVRL9D7u5W6NySCrukL4fWfSRTxDcJC6u` | PumpPortal (evento create), al detectar |
| Par creado | 20/10/2026 03:53 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,3 min / 10,3 min / 34,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 20/10/2026 04:27 UTC |
| Holders / top-10 | 2.197 / 30,57% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 20/10/2026 04:27 UTC |
| Holders efectivos del top-10 | 3,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 20/10/2026 04:27 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 20/10/2026 04:27 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BoN8nuj2w2eooRbEGnxru7hYR5pCT7xdLDqghmif6UDV · Solscan: https://solscan.io/token/HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump · pump.fun: https://pump.fun/coin/HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump · twitter: https://x.com/MarioNawfal/status/2112388391232807287 | consulta 20/10/2026 04:27 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 20/10/2026 04:27 UTC)
- **Historia:**
  - Par creado el 20/10/2026 03:53 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 20/10/2026 04:03 UTC, con el par a 10,3 min de creado: precio $0,00006289, mcap $62.791, liquidez $20.278.
  - Velas de 1 h de GeckoTerminal (2, desde 20/10/2026 03:00 UTC): apertura $0,00004492 · máximo $0,0001360 (20/10/2026 04:00 UTC) · mínimo $0,00002050 (20/10/2026 03:00 UTC) · último cierre $0,00009794.
  - En la consulta 20/10/2026 04:27 UTC: precio $0,0001017, liquidez $26.244, FDV $101.602.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 20/10/2026 04:03 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00006289 |
| Liquidez | $20.278 |
| MCap | $62.791 |
| Volumen 24 h | $80.214 |
| Cambio 24 h | +39% |
| Cambio m5 / h1 | +49,5% / +38,6% |
| Volumen m5 / h1 | $27.941 / $80.214 |
| Trades m5 (compras / ventas) | 417 / 234 |
| Edad del par | 10,3 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 46; motivos sin regla: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 20.6 · estructura 12.9 · precio/volumen 12.7 · cobertura 93/100, [info] narrative_wave: ola 'bien': 13 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter'] · descripción 35 caracteres → +2.7, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1012 · top-10 35.6 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1012/1651 = 0.61 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×4.2 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 64% en 5 min vs 58% en 1 h (s 0.30), [precio/volumen] liquidity_inflow: liquidez +54% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 571→1012 (+36.7/min) · top10 48.9%→35.6% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=20277.68, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 46 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-20T04:03:30+00:00, sin estado previo): **30** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen decente, Liquidez mínima, Subida 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 68 de 41.619 tokens analizados (0,16%) quedan ≥ 56. Con score 30, este activo queda en el percentil 97,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 20/10/2026 04:03 UTC, hasta 22/10/2026 04:03 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +49,5% · h1 +38,6% · h24 +39% · volumen m5/h1 0,35 · edad del par 10,3 min.
- **Precio de entrada** (alerta): $0,00006289.
- **Consulta 20/10/2026 04:27 UTC:** $0,0001017 (+61,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump_2026-10-20_040330.json` · blob `d36da3a67476eb24cc5285d9c086ac6d096a289e` · commit `0f45629` (2026-10-20T04:15:24Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-20_040330`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump · registro · 20/10/2026 04:03 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump · HTTP 200 · 20/10/2026 04:27 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump/report · HTTP 200 · 20/10/2026 04:27 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump · HTTP 200 · 20/10/2026 04:27 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BoN8nuj2w2eooRbEGnxru7hYR5pCT7xdLDqghmif6UDV/ohlcv/hour?limit=1000 · HTTP 200 · 20/10/2026 04:27 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump · HTTP 404 · 20/10/2026 04:27 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BIENUSDT · HTTP 400 · 20/10/2026 04:27 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BIEN-USD · HTTP 404 · 20/10/2026 04:27 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $26.244 vs $25.788 → 1,74%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001017 vs $0,00009794 → 3,69%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump_2026-10-20_040330.json',encoding='utf-8'));d=d.get('HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump',d);p=mock.patch('time.time',return_value=1792469010);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HsM7vtzwCpoWDNE4zRp91j4JxkLMSv3cK46rggE3pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 20/10/2026 04:27 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `176f0a155285521d…`
