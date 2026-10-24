# BIBICOIN (BIBI) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001514 · liquidez $33.506 · mcap $151.416 (al detectar)  
Detectado el 24/10/2026 20:23 UTC por: young-0.4 · edad 10.3 min · pesos info 60 / estructura 20 / precio 20 · info 21.4 · estructura 14.0 · precio/volumen 11.7 · cobertura 93/100, [info] narrative_wave: ola 'bibicoin': 7 lanzamientos más en 1 h → +13.1, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 47, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 26/10/2026 20:23 UTC (< 48 h) · vigente: quedan 46,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir BIBI

Estudio de cómo se adquiere BIBI, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 24/10/2026 21:33 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 24/10/2026 20:23 UTC | pumpswap `7SxEbUm…bD5P` | $33.506 | 10% | 0,597% | 5,969% | 59,691% | $168 | $503 |
| consulta 24/10/2026 21:33 UTC | pumpswap `7SxEbUm…bD5P` | $35.545 | 10% | 0,563% | 5,627% | 56,267% | $178 | $533 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump`
5. Configurar el slippage: 10% (liquidez $35.545, consulta 24/10/2026 21:33 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump) y el par en DexScreener (https://dexscreener.com/solana/7SxEbUmVNSi9uABfNk5xcACh1QSHCVhhFynxDF5XbD5P); mint authority / freeze authority: revocada / revocada · holders 5.158 · top-10 26,69% (consulta 24/10/2026 21:33 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump
- Par en DexScreener: https://dexscreener.com/solana/7SxEbUmVNSi9uABfNk5xcACh1QSHCVhhFynxDF5XbD5P
- Página del lanzamiento (pump.fun): https://pump.fun/coin/AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.158 · top-10 26,69% (consulta 24/10/2026 21:33 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | BIBICOIN / BIBI | registro de la detección (pumpportal_live) |
| Mint / contrato | `AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7SxEbUmVNSi9uABfNk5xcACh1QSHCVhhFynxDF5XbD5P` | DexScreener, al detectar (30 par(es) en la consulta 24/10/2026 21:33 UTC) |
| Deployer | `FSHjV2Pq7RVX3KV5aPtmDhQ5FDMZeKKmWaeK3KtWb2Vr` | PumpPortal (evento create), al detectar |
| Par creado | 24/10/2026 20:13 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,3 min / 10,3 min / 80,3 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 24/10/2026 21:33 UTC |
| Holders / top-10 | 5.158 / 26,69% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 24/10/2026 21:33 UTC |
| Holders efectivos del top-10 | 4,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 24/10/2026 21:33 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 24/10/2026 21:33 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7SxEbUmVNSi9uABfNk5xcACh1QSHCVhhFynxDF5XbD5P · Solscan: https://solscan.io/token/AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump · pump.fun: https://pump.fun/coin/AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump · web: https://www.jpost.com/israel-election-2026/article-912715 · twitter: https://x.com/Peptide442396/status/2114086350450507923?s=20 | consulta 24/10/2026 21:33 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 24/10/2026 21:33 UTC)
- **Historia:**
  - Par creado el 24/10/2026 20:13 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 24/10/2026 20:23 UTC, con el par a 10,3 min de creado: precio $0,0001514, mcap $151.416, liquidez $33.506.
  - Velas de 1 h de GeckoTerminal (2, desde 24/10/2026 20:00 UTC): apertura $0,00003660 · máximo $0,0003503 (24/10/2026 20:00 UTC) · mínimo $0,00001638 (24/10/2026 20:00 UTC) · último cierre $0,0001723.
  - En la consulta 24/10/2026 21:33 UTC: precio $0,0001607, liquidez $35.545, FDV $152.831.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 24/10/2026 20:23 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001514 |
| Liquidez | $33.506 |
| MCap | $151.416 |
| Volumen 24 h | $291.387 |
| Cambio 24 h | +280% |
| Cambio m5 / h1 | +235,0% / +280,0% |
| Volumen m5 / h1 | $172.849 / $291.387 |
| Trades m5 (compras / ventas) | 1.676 / 1.703 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 47; motivos sin regla: young-0.4 · edad 10.3 min · pesos info 60 / estructura 20 / precio 20 · info 21.4 · estructura 14.0 · precio/volumen 11.7 · cobertura 93/100, [info] narrative_wave: ola 'bibicoin': 7 lanzamientos más en 1 h → +13.1, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1957 · top-10 31.9 % → +2.4, [estructura] dev_wallet: creador compró 5.1 % del supply → +1.5, [estructura] holder_to_txn_ratio: holders/txns 1957/6772 = 0.29 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×7.1 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +99% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1227→1957 (+121.7/min) · top10 47.5%→31.9% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=33506.04, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 47 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-24T20:23:53+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 75 de 45.821 tokens analizados (0,16%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 24/10/2026 20:23 UTC, hasta 26/10/2026 20:23 UTC · vigente: quedan 46,8 h.
- **Aceleración al detectar:** cambio m5 +235,0% · h1 +280,0% · h24 +280% · volumen m5/h1 0,59 · edad del par 10,3 min.
- **Precio de entrada** (alerta): $0,0001514.
- **Consulta 24/10/2026 21:33 UTC:** $0,0001607 (+6,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump_2026-10-24_202353.json` · blob `a07bcb6994df162dc4555835883b421a47ab02b0` · commit `4979937` (2026-10-24T21:17:34Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-24_202353`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump · registro · 24/10/2026 20:23 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump · HTTP 200 · 24/10/2026 21:33 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump/report · HTTP 200 · 24/10/2026 21:33 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump · HTTP 200 · 24/10/2026 21:33 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7SxEbUmVNSi9uABfNk5xcACh1QSHCVhhFynxDF5XbD5P/ohlcv/hour?limit=1000 · HTTP 200 · 24/10/2026 21:33 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump · HTTP 404 · 24/10/2026 21:33 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BIBIUSDT · HTTP 400 · 24/10/2026 21:33 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BIBI-USD · HTTP 404 · 24/10/2026 21:33 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $35.545 vs $41.211 → 13,75%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001607 vs $0,0001723 → 6,75%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump_2026-10-24_202353.json',encoding='utf-8'));d=d.get('AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump',d);p=mock.patch('time.time',return_value=1792873433);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint AcsdEAts1wWTW3wXCs96L33PPovrDiymT1hf8sY5pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 24/10/2026 21:33 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `364669dced7b248a…`
