# DOGCOIN (DOGCOIN) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00008169 · liquidez $25.611 · mcap $81.700 (al detectar)  
Detectado el 12/10/2026 05:27 UTC por: young-0.4 · edad 18.6 min · pesos info 56 / estructura 22 / precio 22 · info 14.0 · estructura 17.8 · precio/volumen 8.3 · cobertura 94/100, [info] narrative_wave: ola 'dogcoin': 5 lanzamientos más en 1 h → +8.7, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.5 (score 40, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 14/10/2026 05:27 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir DOGCOIN

Estudio de cómo se adquiere DOGCOIN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 12/10/2026 05:41 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 12/10/2026 05:27 UTC | pumpswap `8c8S1zo…rFj2` | $25.611 | 10% | 0,781% | 7,809% | 78,093% | $128 | $384 |
| consulta 12/10/2026 05:41 UTC | pumpswap `8c8S1zo…rFj2` | $35.700 | 10% | 0,560% | 5,602% | 56,022% | $179 | $536 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump`
5. Configurar el slippage: 10% (liquidez $35.700, consulta 12/10/2026 05:41 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump) y el par en DexScreener (https://dexscreener.com/solana/8c8S1zosjxYLLNFa6Fz9QHeusfEMRSWWix7GjTucrFj2); mint authority / freeze authority: revocada / revocada · holders 3.000 · top-10 26,66% (consulta 12/10/2026 05:41 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump
- Par en DexScreener: https://dexscreener.com/solana/8c8S1zosjxYLLNFa6Fz9QHeusfEMRSWWix7GjTucrFj2
- Página del lanzamiento (pump.fun): https://pump.fun/coin/GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.000 · top-10 26,66% (consulta 12/10/2026 05:41 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | DOGCOIN / DOGCOIN | registro de la detección (pumpportal_live) |
| Mint / contrato | `GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `8c8S1zosjxYLLNFa6Fz9QHeusfEMRSWWix7GjTucrFj2` | DexScreener, al detectar (6 par(es) en la consulta 12/10/2026 05:41 UTC) |
| Deployer | `4CACkyfE7TDHFLRevxc4uTyE6xbmZYxCWAvBcSFQCwfG` | PumpPortal (evento create), al detectar |
| Par creado | 12/10/2026 05:08 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 18,6 min / 18,6 min / 32,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 12/10/2026 05:41 UTC |
| Holders / top-10 | 3.000 / 26,66% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 12/10/2026 05:41 UTC |
| Holders efectivos del top-10 | 4,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 12/10/2026 05:41 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 12/10/2026 05:41 UTC |
| Links | DexScreener: https://dexscreener.com/solana/8c8S1zosjxYLLNFa6Fz9QHeusfEMRSWWix7GjTucrFj2 · Solscan: https://solscan.io/token/GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump · pump.fun: https://pump.fun/coin/GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump · twitter: https://x.com/0xVamonos/status/2109511261859803285 | consulta 12/10/2026 05:41 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 12/10/2026 05:41 UTC)
- **Historia:**
  - Par creado el 12/10/2026 05:08 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 12/10/2026 05:27 UTC, con el par a 18,6 min de creado: precio $0,00008169, mcap $81.700, liquidez $25.611.
  - Velas de 1 h de GeckoTerminal (1, desde 12/10/2026 05:00 UTC): apertura $0,00004360 · máximo $0,0002039 (12/10/2026 05:00 UTC) · mínimo $0,00001919 (12/10/2026 05:00 UTC) · último cierre $0,0001771.
  - En la consulta 12/10/2026 05:41 UTC: precio $0,0001560, liquidez $35.700, FDV $156.080.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 12/10/2026 05:27 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00008169 |
| Liquidez | $25.611 |
| MCap | $81.700 |
| Volumen 24 h | $248.697 |
| Cambio 24 h | +79% |
| Cambio m5 / h1 | -17,4% / +78,9% |
| Volumen m5 / h1 | $60.142 / $248.697 |
| Trades m5 (compras / ventas) | 593 / 423 |
| Edad del par | 18,6 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 40; motivos sin regla: young-0.4 · edad 18.6 min · pesos info 56 / estructura 22 / precio 22 · info 14.0 · estructura 17.8 · precio/volumen 8.3 · cobertura 94/100, [info] narrative_wave: ola 'dogcoin': 5 lanzamientos más en 1 h → +8.7, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.5, [info] dex_profile: perfil pago en DexScreener → +2.8, [estructura] bonding_progress: graduado (pumpswap) → +10.6, [estructura] holders_struct: holders 2179 · top-10 28.1 % → +5.3, [estructura] dev_wallet: creador compró 6.7 % del supply → +1.1, [estructura] holder_to_txn_ratio: holders/txns 2179/5120 = 0.43 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×2.9 la tasa horaria (s 0.56), [precio/volumen] buy_pressure_shift: compras 58% en 5 min vs 57% en 1 h (s 0.06), [precio/volumen] liquidity_inflow: liquidez +10% en 8 min (s 0.34), [precio/volumen] holder_accumulation: holders 1759→2179 (+70.0/min) · top10 30.9%→28.1% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=25610.65, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=13163.39, score 40 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-12T05:27:13+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 50 de 30.644 tokens analizados (0,16%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 12/10/2026 05:27 UTC, hasta 14/10/2026 05:27 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -17,4% · h1 +78,9% · h24 +79% · volumen m5/h1 0,24 · edad del par 18,6 min.
- **Precio de entrada** (alerta): $0,00008169.
- **Consulta 12/10/2026 05:41 UTC:** $0,0001560 (+91,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump_2026-10-12_052713.json` · blob `f4a923dfaac07ee66c160beea5eefd76f109675f` · commit `d983a20` (2026-10-12T05:35:11Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-12_052713`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump · registro · 12/10/2026 05:27 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump · HTTP 200 · 12/10/2026 05:41 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump/report · HTTP 200 · 12/10/2026 05:41 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump · HTTP 200 · 12/10/2026 05:41 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/8c8S1zosjxYLLNFa6Fz9QHeusfEMRSWWix7GjTucrFj2/ohlcv/hour?limit=1000 · HTTP 200 · 12/10/2026 05:41 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump · HTTP 404 · 12/10/2026 05:41 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=DOGCOINUSDT · HTTP 400 · 12/10/2026 05:41 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/DOGCOIN-USD · HTTP 404 · 12/10/2026 05:41 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $35.700 vs $40.373 → 11,57%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001560 vs $0,0001771 → 11,92%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump_2026-10-12_052713.json',encoding='utf-8'));d=d.get('GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump',d);p=mock.patch('time.time',return_value=1791782833);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint GmDjFweCHd1FaDUV6TiUreVZa24KMeQMCBA18d5opump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 12/10/2026 05:41 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `129cad712c3bf04a…`
