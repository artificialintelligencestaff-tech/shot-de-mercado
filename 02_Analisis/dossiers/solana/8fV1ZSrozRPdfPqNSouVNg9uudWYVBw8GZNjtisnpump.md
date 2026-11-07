# HIGH CAP MEMECOIN (HIGHCAP) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001042 · liquidez $24.475 · mcap $104.147 (al detectar)  
Detectado el 07/11/2026 22:53 UTC por: young-0.4 · edad 10.7 min · pesos info 60 / estructura 20 / precio 20 · info 17.6 · estructura 16.9 · precio/volumen 11.8 · cobertura 93/100, [info] narrative_wave: ola 'high': 10 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter'] · descripción 35 caracteres → +2.7 (score 46, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 09/11/2026 22:53 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HIGHCAP

Estudio de cómo se adquiere HIGHCAP, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/11/2026 23:04 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/11/2026 22:53 UTC | pumpswap `3irEED9…5dyF` | $24.475 | 10% | 0,817% | 8,172% | 81,717% | $122 | $367 |
| consulta 07/11/2026 23:03 UTC | pumpswap `3irEED9…5dyF` | $2.189 | 10% | 9,138% | 91,381% | 913,805% | $11 | $33 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump`
5. Configurar el slippage: 10% (liquidez $2.189, consulta 07/11/2026 23:03 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump) y el par en DexScreener (https://dexscreener.com/solana/3irEED9GsibRomv2f44V24Q6MLWwYUKnWg4bd3ei5dyF); mint authority / freeze authority: revocada / revocada · holders 326 · top-10 95,36% (consulta 07/11/2026 23:03 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump
- Par en DexScreener: https://dexscreener.com/solana/3irEED9GsibRomv2f44V24Q6MLWwYUKnWg4bd3ei5dyF
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 326 · top-10 95,36% (consulta 07/11/2026 23:03 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | HIGH CAP MEMECOIN / HIGHCAP | registro de la detección (pumpportal_live) |
| Mint / contrato | `8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `3irEED9GsibRomv2f44V24Q6MLWwYUKnWg4bd3ei5dyF` | DexScreener, al detectar (2 par(es) en la consulta 07/11/2026 23:03 UTC) |
| Deployer | `4vF9bHMxgUEKq7GSqEEZVeq1rpuV99x7hur5KkKKqEu3` | PumpPortal (evento create), al detectar |
| Par creado | 07/11/2026 22:42 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,7 min / 10,7 min / 21,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/11/2026 23:03 UTC |
| Holders / top-10 | 326 / 95,36% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/11/2026 23:03 UTC |
| Holders efectivos del top-10 | 1,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/11/2026 23:03 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 07/11/2026 23:03 UTC |
| Links | DexScreener: https://dexscreener.com/solana/3irEED9GsibRomv2f44V24Q6MLWwYUKnWg4bd3ei5dyF · Solscan: https://solscan.io/token/8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump · pump.fun: https://pump.fun/coin/8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump · web / Telegram / X: no publicados en DexScreener | consulta 07/11/2026 23:03 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/11/2026 23:03 UTC)
- **Historia:**
  - Par creado el 07/11/2026 22:42 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/11/2026 22:53 UTC, con el par a 10,7 min de creado: precio $0,0001042, mcap $104.147, liquidez $24.475.
  - Velas de 1 h de GeckoTerminal (2, desde 07/11/2026 22:00 UTC): apertura $0,00004577 · máximo $0,0001517 (07/11/2026 22:00 UTC) · mínimo $0,000002138 (07/11/2026 22:00 UTC) · último cierre $0,000002168.
  - En la consulta 07/11/2026 23:03 UTC: precio $0,000002185, liquidez $2.189, FDV $2.183.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/11/2026 22:53 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001042 |
| Liquidez | $24.475 |
| MCap | $104.147 |
| Volumen 24 h | $144.415 |
| Cambio 24 h | +178% |
| Cambio m5 / h1 | +47,5% / +178,0% |
| Volumen m5 / h1 | $86.236 / $144.415 |
| Trades m5 (compras / ventas) | 1.053 / 1.092 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 46; motivos sin regla: young-0.4 · edad 10.7 min · pesos info 60 / estructura 20 / precio 20 · info 17.6 · estructura 16.9 · precio/volumen 11.8 · cobertura 93/100, [info] narrative_wave: ola 'high': 10 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter'] · descripción 35 caracteres → +2.7, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 847 · top-10 28.4 % → +4.8, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.0, [estructura] holder_to_txn_ratio: holders/txns 847/4142 = 0.20 → +0.3, [precio/volumen] volume_acceleration: vol 5 min ×7.2 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +43% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 461→847 (+32.2/min) · top10 36.4%→28.4% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=24474.78, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 46 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-07T22:53:14+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 94 de 46.888 tokens analizados (0,20%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/11/2026 22:53 UTC, hasta 09/11/2026 22:53 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +47,5% · h1 +178,0% · h24 +178% · volumen m5/h1 0,60 · edad del par 10,7 min.
- **Precio de entrada** (alerta): $0,0001042.
- **Consulta 07/11/2026 23:03 UTC:** $0,000002185 (-97,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump_2026-11-07_225314.json` · blob `a3cf85b53e4128d3cd8e3c685de395075a1f40eb` · commit `1c88c15` (2026-11-07T22:55:33Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-07_225314`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump · registro · 07/11/2026 22:53 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump · HTTP 200 · 07/11/2026 23:03 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump/report · HTTP 200 · 07/11/2026 23:03 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump · HTTP 200 · 07/11/2026 23:03 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/3irEED9GsibRomv2f44V24Q6MLWwYUKnWg4bd3ei5dyF/ohlcv/hour?limit=1000 · HTTP 200 · 07/11/2026 23:04 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump · HTTP 404 · 07/11/2026 23:04 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HIGHCAPUSDT · HTTP 400 · 07/11/2026 23:04 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HIGHCAP-USD · HTTP 404 · 07/11/2026 23:04 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.189 vs $2.151 → 1,74%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002185 vs $0,000002168 → 0,76%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump_2026-11-07_225314.json',encoding='utf-8'));d=d.get('8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump',d);p=mock.patch('time.time',return_value=1794091994);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8fV1ZSrozRPdfPqNSouVNg9uudWYVBw8GZNjtisnpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/11/2026 23:04 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `f51f3da5343b50fb…`
