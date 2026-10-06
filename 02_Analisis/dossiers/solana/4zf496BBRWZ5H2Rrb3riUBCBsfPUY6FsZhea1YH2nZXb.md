# Buto (Buto) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001164 · liquidez $30.811 · mcap $116.356 (al detectar)  
Detectado el 06/10/2026 17:57 UTC por: young-0.4 · edad 10.2 min · pesos info 60 / estructura 20 / precio 20 · info 23.3 · estructura 14.9 · precio/volumen 7.8 · cobertura 93/100, [info] narrative_wave: ola 'buto': 32 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 46, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 08/10/2026 17:57 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Buto

Estudio de cómo se adquiere Buto, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 18:12 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 17:57 UTC | pumpswap `AxYiepv…Lc1E` | $30.811 | 10% | 0,649% | 6,491% | 64,913% | $154 | $462 |
| consulta 06/10/2026 18:12 UTC | pumpswap `AxYiepv…Lc1E` | $36.051 | 10% | 0,555% | 5,548% | 55,476% | $180 | $541 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb`
5. Configurar el slippage: 10% (liquidez $36.051, consulta 06/10/2026 18:12 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb) y el par en DexScreener (https://dexscreener.com/solana/AxYiepv73mBDpgEd2amnEaLdPiEYNqcuUpnoiZjTLc1E); mint authority / freeze authority: revocada / revocada · holders 3.689 · top-10 25,75% (consulta 06/10/2026 18:12 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb
- Par en DexScreener: https://dexscreener.com/solana/AxYiepv73mBDpgEd2amnEaLdPiEYNqcuUpnoiZjTLc1E
- Página del lanzamiento (pump.fun): https://pump.fun/coin/4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.689 · top-10 25,75% (consulta 06/10/2026 18:12 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Buto / Buto | registro de la detección (pumpportal_live) |
| Mint / contrato | `4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `AxYiepv73mBDpgEd2amnEaLdPiEYNqcuUpnoiZjTLc1E` | DexScreener, al detectar (4 par(es) en la consulta 06/10/2026 18:12 UTC) |
| Deployer | `2dE3XMa3y4um1XXstv1ZUdNk96NctLW1cP5ewnLBUsRV` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 17:47 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,2 min / 10,2 min / 25,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 18:12 UTC |
| Holders / top-10 | 3.689 / 25,75% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 18:12 UTC |
| Holders efectivos del top-10 | 4,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 18:12 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 18:12 UTC |
| Links | DexScreener: https://dexscreener.com/solana/AxYiepv73mBDpgEd2amnEaLdPiEYNqcuUpnoiZjTLc1E · Solscan: https://solscan.io/token/4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb · pump.fun: https://pump.fun/coin/4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb · web: https://boldmast.com · twitter: https://x.com/search?q=$Buto | consulta 06/10/2026 18:12 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 18:12 UTC)
- **Historia:**
  - Par creado el 06/10/2026 17:47 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 17:57 UTC, con el par a 10,2 min de creado: precio $0,0001164, mcap $116.356, liquidez $30.811.
  - Velas de 1 h de GeckoTerminal (2, desde 06/10/2026 17:00 UTC): apertura $0,00005006 · máximo $0,0002620 (06/10/2026 17:00 UTC) · mínimo $0,00004625 (06/10/2026 17:00 UTC) · último cierre $0,0001510.
  - En la consulta 06/10/2026 18:12 UTC: precio $0,0001489, liquidez $36.051, FDV $148.774.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 17:57 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001164 |
| Liquidez | $30.811 |
| MCap | $116.356 |
| Volumen 24 h | $826.080 |
| Cambio 24 h | +139% |
| Cambio m5 / h1 | -47,0% / +139,0% |
| Volumen m5 / h1 | $231.250 / $826.080 |
| Trades m5 (compras / ventas) | 2.284 / 1.709 |
| Edad del par | 10,2 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 46; motivos sin regla: young-0.4 · edad 10.2 min · pesos info 60 / estructura 20 / precio 20 · info 23.3 · estructura 14.9 · precio/volumen 7.8 · cobertura 93/100, [info] narrative_wave: ola 'buto': 32 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 2983 · top-10 27.7 % → +4.8, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 2983/12771 = 0.23 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×3.4 la tasa horaria (s 0.74), [precio/volumen] buy_pressure_shift: compras 57% en 5 min vs 53% en 1 h (s 0.22), [precio/volumen] holder_accumulation: holders 2002→2983 (+163.5/min) · top10 28.9%→27.7% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=30810.65, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 46 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T17:57:43+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 20 de 16.275 tokens analizados (0,12%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 17:57 UTC, hasta 08/10/2026 17:57 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -47,0% · h1 +139,0% · h24 +139% · volumen m5/h1 0,28 · edad del par 10,2 min.
- **Precio de entrada** (alerta): $0,0001164.
- **Consulta 06/10/2026 18:12 UTC:** $0,0001489 (+27,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb_2026-10-06_175743.json` · blob `037d1d5c1a151756995250256fded22160d664c7` · commit `5baf72c` (2026-10-06T18:04:13Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_175743`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb · registro · 06/10/2026 17:57 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb · HTTP 200 · 06/10/2026 18:12 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb/report · HTTP 200 · 06/10/2026 18:12 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb · HTTP 200 · 06/10/2026 18:12 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/AxYiepv73mBDpgEd2amnEaLdPiEYNqcuUpnoiZjTLc1E/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 18:12 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb · HTTP 404 · 06/10/2026 18:12 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BUTOUSDT · HTTP 400 · 06/10/2026 18:12 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BUTO-USD · HTTP 404 · 06/10/2026 18:12 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $36.051 vs $39.158 → 7,93%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001489 vs $0,0001510 → 1,36%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb_2026-10-06_175743.json',encoding='utf-8'));d=d.get('4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb',d);p=mock.patch('time.time',return_value=1791309463);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 4zf496BBRWZ5H2Rrb3riUBCBsfPUY6FsZhea1YH2nZXb --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 18:12 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `4de0f532e8e1a7aa…`
