# Frog and Toad (FAT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00006622 · liquidez $21.827 · mcap $66.222 (al detectar)  
Detectado el 06/10/2026 12:20 UTC por: young-0.4 · edad 10.8 min · pesos info 60 / estructura 20 / precio 20 · info 20.2 · estructura 12.9 · precio/volumen 9.0 · cobertura 93/100, [info] narrative_wave: ola 'frog': 47 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +5.3 (score 42, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 08/10/2026 12:20 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir FAT

Estudio de cómo se adquiere FAT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 12:44 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 12:20 UTC | pumpswap `DXaCpHM…kFfv` | $21.827 | 10% | 0,916% | 9,163% | 91,628% | $109 | $327 |
| consulta 06/10/2026 12:44 UTC | pumpswap `DXaCpHM…kFfv` | $15.562 | 10% | 1,285% | 12,852% | 128,520% | $78 | $233 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p`
5. Configurar el slippage: 10% (liquidez $15.562, consulta 06/10/2026 12:44 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p) y el par en DexScreener (https://dexscreener.com/solana/DXaCpHMcH3sc4bFArvLJxBEhSb1CBPhtVu98dvtEkFfv); mint authority / freeze authority: revocada / revocada · holders 1.507 · top-10 45,80% (consulta 06/10/2026 12:44 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p
- Par en DexScreener: https://dexscreener.com/solana/DXaCpHMcH3sc4bFArvLJxBEhSb1CBPhtVu98dvtEkFfv
- Página del lanzamiento (pump.fun): https://pump.fun/coin/94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.507 · top-10 45,80% (consulta 06/10/2026 12:44 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Frog and Toad / FAT | registro de la detección (pumpportal_live) |
| Mint / contrato | `94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DXaCpHMcH3sc4bFArvLJxBEhSb1CBPhtVu98dvtEkFfv` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 12:44 UTC) |
| Deployer | `CxxcsDAobcZPeYgWUGfuXb4Via5QNm9xhdU96dUTKsfR` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 12:09 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,8 min / 10,8 min / 34,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 12:44 UTC |
| Holders / top-10 | 1.507 / 45,80% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 12:44 UTC |
| Holders efectivos del top-10 | 2,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 12:44 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 12:44 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DXaCpHMcH3sc4bFArvLJxBEhSb1CBPhtVu98dvtEkFfv · Solscan: https://solscan.io/token/94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p · pump.fun: https://pump.fun/coin/94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p · web: https://www.frogandtoad.ai/ · twitter: https://x.com/captain__crunch/status/2107441675761066371 | consulta 06/10/2026 12:44 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 12:44 UTC)
- **Historia:**
  - Par creado el 06/10/2026 12:09 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 12:20 UTC, con el par a 10,8 min de creado: precio $0,00006622, mcap $66.222, liquidez $21.827.
  - Velas de 1 h de GeckoTerminal (1, desde 06/10/2026 12:00 UTC): apertura $0,00004876 · máximo $0,00008442 (06/10/2026 12:00 UTC) · mínimo $0,00001971 (06/10/2026 12:00 UTC) · último cierre $0,00003520.
  - En la consulta 06/10/2026 12:44 UTC: precio $0,00003599, liquidez $15.562, FDV $35.995.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 12:20 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00006622 |
| Liquidez | $21.827 |
| MCap | $66.222 |
| Volumen 24 h | $152.743 |
| Cambio 24 h | +36% |
| Cambio m5 / h1 | +12,9% / +35,9% |
| Volumen m5 / h1 | $54.284 / $152.743 |
| Trades m5 (compras / ventas) | 589 / 462 |
| Edad del par | 10,8 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 42; motivos sin regla: young-0.4 · edad 10.8 min · pesos info 60 / estructura 20 / precio 20 · info 20.2 · estructura 12.9 · precio/volumen 9.0 · cobertura 93/100, [info] narrative_wave: ola 'frog': 47 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1421 · top-10 34.7 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1421/3168 = 0.45 → +0.7, [precio/volumen] volume_acceleration: vol 5 min ×4.3 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +5% en 8 min (s 0.16), [precio/volumen] holder_accumulation: holders 430→1421 (+82.6/min) · top10 44.3%→34.7% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=21827.47, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 42 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T12:20:47+00:00, sin estado previo): **35** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Subida 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 18 de 15.299 tokens analizados (0,12%) quedan ≥ 56. Con score 35, este activo queda en el percentil 98,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 12:20 UTC, hasta 08/10/2026 12:20 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +12,9% · h1 +35,9% · h24 +36% · volumen m5/h1 0,36 · edad del par 10,8 min.
- **Precio de entrada** (alerta): $0,00006622.
- **Consulta 06/10/2026 12:44 UTC:** $0,00003599 (-45,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p_2026-10-06_122047.json` · blob `b5e505664d452f458f980c0f6d68476a46d7eb3f` · commit `39af862` (2026-10-06T12:37:42Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_122047`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p · registro · 06/10/2026 12:20 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p · HTTP 200 · 06/10/2026 12:44 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p/report · HTTP 200 · 06/10/2026 12:44 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p · HTTP 200 · 06/10/2026 12:44 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DXaCpHMcH3sc4bFArvLJxBEhSb1CBPhtVu98dvtEkFfv/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 12:44 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p · HTTP 404 · 06/10/2026 12:44 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=FATUSDT · HTTP 400 · 06/10/2026 12:44 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/FAT-USD · HTTP 404 · 06/10/2026 12:44 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $15.562 vs $15.675 → 0,72%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00003599 vs $0,00003520 → 2,18%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p_2026-10-06_122047.json',encoding='utf-8'));d=d.get('94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p',d);p=mock.patch('time.time',return_value=1791289247);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 94aCbmNsv4BqBkeBwFPtxzQ6J7deatZe86YVrrgLqN2p --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 12:44 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `e828c23814825aee…`
