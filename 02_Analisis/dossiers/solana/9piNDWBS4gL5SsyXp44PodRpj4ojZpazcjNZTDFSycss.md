# THE MAX EXTRACTOR (EXTRACTOR) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00005882 · liquidez $20.500 · mcap $57.806 (al detectar)  
Detectado el 06/10/2026 17:15 UTC por: MCap > $50K, Volumen alto, Buy pressure >55% (score 63, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 08/10/2026 17:15 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir EXTRACTOR

Estudio de cómo se adquiere EXTRACTOR, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 17:36 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 17:15 UTC | pumpswap `2hM2uZz…BqxK` | $20.500 | 10% | 0,976% | 9,756% | 97,561% | $102 | $307 |
| consulta 06/10/2026 17:36 UTC | pumpswap `2hM2uZz…BqxK` | $20.281 | 10% | 0,986% | 9,862% | 98,616% | $101 | $304 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss`
5. Configurar el slippage: 10% (liquidez $20.281, consulta 06/10/2026 17:36 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss) y el par en DexScreener (https://dexscreener.com/solana/2hM2uZzzMfK2hmAFcGa7j6ijf2Btx249Hta4FTuZBqxK); mint authority / freeze authority: revocada / revocada · holders 490 · top-10 92,99% (consulta 06/10/2026 17:36 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss
- Par en DexScreener: https://dexscreener.com/solana/2hM2uZzzMfK2hmAFcGa7j6ijf2Btx249Hta4FTuZBqxK
- Página del lanzamiento (pump.fun): https://pump.fun/coin/9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 490 · top-10 92,99% (consulta 06/10/2026 17:36 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | THE MAX EXTRACTOR / EXTRACTOR | registro de la detección (pumpportal) |
| Mint / contrato | `9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `2hM2uZzzMfK2hmAFcGa7j6ijf2Btx249Hta4FTuZBqxK` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 17:36 UTC) |
| Deployer | `yHCxHBEaJW5tbndqC8JciSThr7U1cqLpdcsvHcx6PRe` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 16:13 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 62,3 min / 62,3 min / 83,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 17:36 UTC |
| Holders / top-10 | 490 / 92,99% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 17:36 UTC |
| Holders efectivos del top-10 | 1,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 17:36 UTC |
| Etiquetas de RugCheck | «Top 10 holders high ownership», «Single holder ownership» | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 17:36 UTC |
| Links | DexScreener: https://dexscreener.com/solana/2hM2uZzzMfK2hmAFcGa7j6ijf2Btx249Hta4FTuZBqxK · Solscan: https://solscan.io/token/9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss · pump.fun: https://pump.fun/coin/9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss · web: https://maxextractor.xyz/ · twitter: https://x.com/MaxExtractorTV | consulta 06/10/2026 17:36 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 17:36 UTC)
- **Historia:**
  - Par creado el 06/10/2026 16:13 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 17:15 UTC, con el par a 62,3 min de creado: precio $0,00005882, mcap $57.806, liquidez $20.500.
  - Velas de 1 h de GeckoTerminal (2, desde 06/10/2026 16:00 UTC): apertura $0,0001762 · máximo $0,0002111 (06/10/2026 16:00 UTC) · mínimo $0,00003694 (06/10/2026 16:00 UTC) · último cierre $0,00005676.
  - En la consulta 06/10/2026 17:36 UTC: precio $0,00005758, liquidez $20.281, FDV $56.590.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 17:15 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00005882 |
| Liquidez | $20.500 |
| MCap | $57.806 |
| Volumen 24 h | $221.101 |
| Cambio 24 h | -2% |
| Cambio m5 / h1 | +21,2% / -50,9% |
| Volumen m5 / h1 | $1.389 / $83.328 |
| Trades m5 (compras / ventas) | 8 / 6 |
| Edad del par | 62,3 min |
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

Desglose reconstruido desde los motivos registrados; suma 63 = score registrado 63 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $50K | $57.806 | +10 |
| Volumen 24 h | ≥ $100K | $221.101 | +15 |
| Buy pressure m5 | > 55% (par maduro) | 57% | +15 |
| Edge temprano | edad < 4 h (par maduro) | edad 62,3 min | +8 |
| Volumen m5 | > $1K (par maduro) | $1.389 | +10 |
| Liquidez | ≥ $20K | $20.500 | +5 |
| **Total** | recortado a 0–100 |  | **63** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T17:15:28+00:00, sin estado previo): **63** · motivos: MCap > $50K, Volumen alto, Buy pressure >55%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez mínima.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 20 de 16.137 tokens analizados (0,12%) quedan ≥ 56. Con score 63, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 17:15 UTC, hasta 08/10/2026 17:15 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +21,2% · h1 -50,9% · h24 -2% · volumen m5/h1 0,02 · edad del par 62,3 min.
- **Precio de entrada** (alerta): $0,00005882.
- **Consulta 06/10/2026 17:36 UTC:** $0,00005758 (-2,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss_2026-10-06_171528.json` · blob `b4101a6d345b6f230447b3c54017138818902447` · commit `81401f7` (2026-10-06T17:29:56Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_171528`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss · registro · 06/10/2026 17:15 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss · HTTP 200 · 06/10/2026 17:36 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss/report · HTTP 200 · 06/10/2026 17:36 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss · HTTP 200 · 06/10/2026 17:36 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/2hM2uZzzMfK2hmAFcGa7j6ijf2Btx249Hta4FTuZBqxK/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 17:36 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss · HTTP 404 · 06/10/2026 17:36 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=EXTRACTORUSDT · HTTP 400 · 06/10/2026 17:36 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/EXTRACTOR-USD · HTTP 404 · 06/10/2026 17:36 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $20.281 vs $20.271 → 0,05%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00005758 vs $0,00005676 → 1,43%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss_2026-10-06_171528.json',encoding='utf-8'));d=d.get('9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss',d);p=mock.patch('time.time',return_value=1791306928);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 9piNDWBS4gL5SsyXp44PodRpj4ojZpazcjNZTDFSycss --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 17:36 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `177522dcc1183fa7…`
