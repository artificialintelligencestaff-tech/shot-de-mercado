# Jensen Huang (JENSEN) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001780 · liquidez $95.210 · mcap $1.774.126 (al detectar)  
Detectado el 21/11/2026 03:48 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 23/11/2026 03:48 UTC (< 48 h) · vigente: quedan 39,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir JENSEN

Estudio de cómo se adquiere JENSEN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 21/11/2026 12:03 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 21/11/2026 03:48 UTC | pumpswap `7fy71w6…4kXT` | $95.210 | 5% | 0,210% | 2,101% | 21,006% | $476 | $1.428 |
| consulta 21/11/2026 12:03 UTC | pumpswap `7fy71w6…4kXT` | $64.127 | 5% | 0,312% | 3,119% | 31,188% | $321 | $962 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump`
5. Configurar el slippage: 5% (liquidez $64.127, consulta 21/11/2026 12:03 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump) y el par en DexScreener (https://dexscreener.com/solana/7fy71w6jdYias1W66SQscXvuUtYH2N29BKcGGALn4kXT); mint authority / freeze authority: revocada / revocada · holders 2.795 · top-10 25,11% (consulta 21/11/2026 12:03 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump
- Par en DexScreener: https://dexscreener.com/solana/7fy71w6jdYias1W66SQscXvuUtYH2N29BKcGGALn4kXT
- Página del lanzamiento (pump.fun): https://pump.fun/coin/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.795 · top-10 25,11% (consulta 21/11/2026 12:03 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Jensen Huang / JENSEN | registro de la detección (trending) |
| Mint / contrato | `DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7fy71w6jdYias1W66SQscXvuUtYH2N29BKcGGALn4kXT` | DexScreener, al detectar (4 par(es) en la consulta 21/11/2026 12:03 UTC) |
| Deployer | `ZXezTa6K1KEtbZwodqu6ScPWraVVdu1Y1AjotR5se5p` | RugCheck `creator` |
| Par creado | 21/11/2026 00:01 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 3,8 h / 3,8 h / 12,0 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 21/11/2026 12:03 UTC |
| Holders / top-10 | 2.795 / 25,11% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 21/11/2026 12:03 UTC |
| Holders efectivos del top-10 | 9,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 21/11/2026 12:03 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 21/11/2026 12:03 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7fy71w6jdYias1W66SQscXvuUtYH2N29BKcGGALn4kXT · Solscan: https://solscan.io/token/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump · pump.fun: https://pump.fun/coin/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump · web: https://jensenmeme.online · twitter: https://x.com/JensenMemeSOL | consulta 21/11/2026 12:03 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 21/11/2026 12:03 UTC)
- **Historia:**
  - Par creado el 21/11/2026 00:01 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 21/11/2026 03:48 UTC, con el par a 3,8 h de creado: precio $0,001780, mcap $1.774.126, liquidez $95.210.
  - Velas de 1 h de GeckoTerminal (13, desde 21/11/2026 00:00 UTC): apertura $0,00009460 · máximo $0,003285 (21/11/2026 00:00 UTC) · mínimo $0,00009460 (21/11/2026 00:00 UTC) · último cierre $0,0008041.
  - En la consulta 21/11/2026 12:03 UTC: precio $0,0007713, liquidez $64.127, FDV $768.626.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 21/11/2026 03:48 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001780 |
| Liquidez | $95.210 |
| MCap | $1.774.126 |
| Volumen 24 h | $1.677.880 |
| Cambio 24 h | +1.771% |
| Cambio m5 / h1 | +2,1% / -5,3% |
| Volumen m5 / h1 | $5.462 / $66.010 |
| Trades m5 (compras / ventas) | 437 / 240 |
| Edad del par | 3,8 h |
| Score del feed (WS) | 72 |

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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 72 × 0,3 | +21,6 |
| MCap | ≥ $1M | $1.774.126 | +25 |
| Volumen 24 h | ≥ $1M | $1.677.880 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 65% | +25 |
| Edge temprano | edad < 4 h (par maduro) | edad 3,8 h | +8 |
| Volumen m5 | > $1K (par maduro) | $5.462 | +10 |
| Liquidez | ≥ $50K | $95.210 | +10 |
| Cambio 24 h | ≥ +50% | +1.771% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.771% · liq/mcap 5,4% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-21T03:48:43+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=5.4% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 109 de 47.514 tokens analizados (0,23%) quedan ≥ 56. Con score 100, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 21/11/2026 03:48 UTC, hasta 23/11/2026 03:48 UTC · vigente: quedan 39,8 h.
- **Aceleración al detectar:** cambio m5 +2,1% · h1 -5,3% · h24 +1.771% · volumen m5/h1 0,08 · edad del par 3,8 h.
- **Precio de entrada** (alerta): $0,001780.
- **Consulta 21/11/2026 12:03 UTC:** $0,0007713 (-56,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump_2026-11-21_034843.json` · blob `508f061779b378573565b19060dc986ef614277e` · commit `caa53e7` (2026-11-21T11:50:49Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-21_034218.json` · blob `89809b987826b45f6c0652376fcb9c38d19d0a33` · commit `caa53e7` (2026-11-21T11:50:49Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-21_034843`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump · registro · 21/11/2026 03:48 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump · HTTP 200 · 21/11/2026 12:03 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump/report · HTTP 200 · 21/11/2026 12:03 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump · HTTP 200 · 21/11/2026 12:03 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7fy71w6jdYias1W66SQscXvuUtYH2N29BKcGGALn4kXT/ohlcv/hour?limit=1000 · HTTP 200 · 21/11/2026 12:03 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump · HTTP 404 · 21/11/2026 12:03 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=JENSENUSDT · HTTP 400 · 21/11/2026 12:03 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/JENSEN-USD · HTTP 404 · 21/11/2026 12:03 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $64.127 vs $65.428 → 1,99%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0007713 vs $0,0008041 → 4,08%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump_2026-11-21_034843.json',encoding='utf-8'));d=d.get('DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump',d);p=mock.patch('time.time',return_value=1795232923);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 21/11/2026 12:03 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `e405d2400368021f…`
