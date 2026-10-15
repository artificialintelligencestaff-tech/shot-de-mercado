# patience (PATIENCE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00006283 · liquidez $19.871 · mcap $62.835 (al detectar)  
Detectado el 15/10/2026 16:44 UTC por: young-0.4 · edad 11.8 min · pesos info 59 / estructura 20 / precio 20 · info 22.3 · estructura 14.9 · precio/volumen 11.7 · cobertura 93/100, [info] narrative_wave: ola 'patience': 8 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter'] · descripción 43 caracteres → +4.6 (score 49, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 17/10/2026 16:44 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir PATIENCE

Estudio de cómo se adquiere PATIENCE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 15/10/2026 17:03 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 15/10/2026 16:44 UTC | pumpswap `GnjDzLH…hU4c` | $19.871 | 10% | 1,006% | 10,065% | 100,650% | $99 | $298 |
| consulta 15/10/2026 17:02 UTC | pumpswap `GnjDzLH…hU4c` | $2.051 | 10% | 9,753% | 97,531% | 975,315% | $10 | $31 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump`
5. Configurar el slippage: 10% (liquidez $2.051, consulta 15/10/2026 17:02 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump) y el par en DexScreener (https://dexscreener.com/solana/GnjDzLHAjT3t4MjPnKrm13gaFwEAnbw3rVWLmAp1hU4c); mint authority / freeze authority: revocada / revocada · holders 1.094 · top-10 123,89% (consulta 15/10/2026 17:02 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump
- Par en DexScreener: https://dexscreener.com/solana/GnjDzLHAjT3t4MjPnKrm13gaFwEAnbw3rVWLmAp1hU4c
- Página del lanzamiento (pump.fun): https://pump.fun/coin/Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.094 · top-10 123,89% (consulta 15/10/2026 17:02 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | patience / PATIENCE | registro de la detección (pumpportal_live) |
| Mint / contrato | `Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `GnjDzLHAjT3t4MjPnKrm13gaFwEAnbw3rVWLmAp1hU4c` | DexScreener, al detectar (2 par(es) en la consulta 15/10/2026 17:02 UTC) |
| Deployer | `BsfZVLBSSoZDbFg91SFKaPE1GinDuWaMKYQaxNjnDnqf` | PumpPortal (evento create), al detectar |
| Par creado | 15/10/2026 16:32 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,8 min / 11,8 min / 30,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 15/10/2026 17:02 UTC |
| Holders / top-10 | 1.094 / 123,89% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 15/10/2026 17:02 UTC |
| Holders efectivos del top-10 | 1,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 15/10/2026 17:02 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 15/10/2026 17:02 UTC |
| Links | DexScreener: https://dexscreener.com/solana/GnjDzLHAjT3t4MjPnKrm13gaFwEAnbw3rVWLmAp1hU4c · Solscan: https://solscan.io/token/Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump · pump.fun: https://pump.fun/coin/Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump · web / Telegram / X: no publicados en DexScreener | consulta 15/10/2026 17:02 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 15/10/2026 17:02 UTC)
- **Historia:**
  - Par creado el 15/10/2026 16:32 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 15/10/2026 16:44 UTC, con el par a 11,8 min de creado: precio $0,00006283, mcap $62.835, liquidez $19.871.
  - Velas de 1 h de GeckoTerminal (1, desde 15/10/2026 16:00 UTC): apertura $0,00004533 · máximo $0,00008350 (15/10/2026 16:00 UTC) · mínimo $0,000002028 (15/10/2026 16:00 UTC) · último cierre $0,000002028.
  - En la consulta 15/10/2026 17:02 UTC: precio $0,000002029, liquidez $2.051, FDV $2.030.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 15/10/2026 16:44 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00006283 |
| Liquidez | $19.871 |
| MCap | $62.835 |
| Volumen 24 h | $86.889 |
| Cambio 24 h | +43% |
| Cambio m5 / h1 | +30,6% / +43,1% |
| Volumen m5 / h1 | $37.699 / $86.889 |
| Trades m5 (compras / ventas) | 1.147 / 396 |
| Edad del par | 11,8 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 49; motivos sin regla: young-0.4 · edad 11.8 min · pesos info 59 / estructura 20 / precio 20 · info 22.3 · estructura 14.9 · precio/volumen 11.7 · cobertura 93/100, [info] narrative_wave: ola 'patience': 8 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter'] · descripción 43 caracteres → +4.6, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 508 · top-10 45.8 % → +2.5, [estructura] dev_wallet: creador compró 2.0 % del supply → +2.4, [estructura] holder_to_txn_ratio: holders/txns 508/4559 = 0.11 → +0.2, [precio/volumen] volume_acceleration: vol 5 min ×5.2 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 74% en 5 min vs 68% en 1 h (s 0.32), [precio/volumen] liquidity_inflow: liquidez +21% en 8 min (s 0.70), [precio/volumen] holder_accumulation: holders 453→508 (+4.6/min) · top10 45.0%→45.8% (s 0.92), [flag, no suma] tradable=True, liquidity_usd=19870.88, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 49 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-15T16:44:09+00:00, sin estado previo): **25** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen decente, Liquidez baja, Subida 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 59 de 36.181 tokens analizados (0,16%) quedan ≥ 56. Con score 25, este activo queda en el percentil 97,5 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 15/10/2026 16:44 UTC, hasta 17/10/2026 16:44 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +30,6% · h1 +43,1% · h24 +43% · volumen m5/h1 0,43 · edad del par 11,8 min.
- **Precio de entrada** (alerta): $0,00006283.
- **Consulta 15/10/2026 17:02 UTC:** $0,000002029 (-96,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump_2026-10-15_164409.json` · blob `491ac031f6924c2ff181b5a09d6f7ea5461fd9c9` · commit `975a2cb` (2026-10-15T16:56:34Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-15_164409`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump · registro · 15/10/2026 16:44 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump · HTTP 200 · 15/10/2026 17:02 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump/report · HTTP 200 · 15/10/2026 17:03 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump · HTTP 200 · 15/10/2026 17:03 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/GnjDzLHAjT3t4MjPnKrm13gaFwEAnbw3rVWLmAp1hU4c/ohlcv/hour?limit=1000 · HTTP 200 · 15/10/2026 17:03 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump · HTTP 404 · 15/10/2026 17:03 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=PATIENCEUSDT · HTTP 400 · 15/10/2026 17:03 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/PATIENCE-USD · HTTP 404 · 15/10/2026 17:03 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.051 vs $2.056 → 0,26%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002029 vs $0,000002028 → 0,03%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump_2026-10-15_164409.json',encoding='utf-8'));d=d.get('Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump',d);p=mock.patch('time.time',return_value=1792082649);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint Bav8Z8q7g95Uyqqxr4BHFiSXedbT8Xyxb96oTiTwpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 15/10/2026 17:03 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `dbf0593a67256b03…`
