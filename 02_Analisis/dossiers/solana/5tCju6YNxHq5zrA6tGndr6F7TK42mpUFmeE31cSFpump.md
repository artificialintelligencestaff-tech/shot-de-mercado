# cat wif sword (swordcat) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003595 · liquidez $246.634 · mcap $3.451.711 (al detectar)  
Detectado el 08/10/2026 14:04 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 67, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 10/10/2026 14:04 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir swordcat

Estudio de cómo se adquiere swordcat, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **meteora**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/10/2026 14:15 UTC; CoinGecko sin pares de este contrato en esos exchanges).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/10/2026 14:04 UTC | pumpswap `8ewuF2o…w83d` | $246.634 | 5% | 0,081% | 0,811% | 8,109% | $1.233 | $3.700 |
| consulta 08/10/2026 14:15 UTC | meteora `2YaGc2i…PGn1` | $299.271 | 3% | 0,067% | 0,668% | 6,683% | $1.496 | $4.489 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en meteora
4. Pegar el mint y verificar que coincide carácter por carácter: `5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump`
5. Configurar el slippage: 3% (liquidez $299.271, consulta 08/10/2026 14:15 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump) y el par en DexScreener (https://dexscreener.com/solana/2YaGc2iYZt44B5zn5Tvk59APbAn51xGekzNQAPF2PGn1); mint authority / freeze authority: revocada / revocada · holders 30.712 · top-10 22,58% (consulta 08/10/2026 14:15 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump
- Par en DexScreener: https://dexscreener.com/solana/2YaGc2iYZt44B5zn5Tvk59APbAn51xGekzNQAPF2PGn1
- Página del lanzamiento (pump.fun): https://pump.fun/coin/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 30.712 · top-10 22,58% (consulta 08/10/2026 14:15 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | cat wif sword / swordcat | registro de la detección (trending) |
| Mint / contrato | `5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `8ewuF2o8ACro7fqWepZ3tKhkbBjndZU4Ldk9scRPw83d` | DexScreener, al detectar (27 par(es) en la consulta 08/10/2026 14:15 UTC) |
| Deployer | `7naFFwuEJWeWwWYQUkgAWHsxYKg3KctEuUj42JdAMidP` | RugCheck `creator` |
| Par creado | 28/09/2026 09:13 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,2 días / 10,2 días / 10,2 días | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/10/2026 14:15 UTC |
| Holders / top-10 | 30.712 / 22,58% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/10/2026 14:15 UTC |
| Holders efectivos del top-10 | 9,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | meteoraDlmm 0%; pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; manifest 0%; raydium_clmm 0%; manifest 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; raydium_clmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; raydium_cpmm 100%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0%; raydium_launchlab 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/10/2026 14:15 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 08/10/2026 14:15 UTC |
| Links | DexScreener: https://dexscreener.com/solana/2YaGc2iYZt44B5zn5Tvk59APbAn51xGekzNQAPF2PGn1 · Solscan: https://solscan.io/token/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump · pump.fun: https://pump.fun/coin/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump · web: https://x.com/SoyLaMejori/status/2103894236466761867 · twitter: https://x.com/catwifswordsoll | consulta 08/10/2026 14:15 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** CoinGecko: Solana Ecosystem, Meme, Solana Meme, Cat-Themed, Pump.fun Ecosystem · scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/10/2026 14:15 UTC)
- **Historia:**
  - Par creado el 28/09/2026 09:13 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/10/2026 14:04 UTC, con el par a 10,2 días de creado: precio $0,003595, mcap $3.451.711, liquidez $246.634.
  - Velas de 1 h de GeckoTerminal (244, desde 28/09/2026 11:00 UTC): apertura $0,0003546 · máximo $0,005075 (05/10/2026 21:00 UTC) · mínimo $0,0001798 (29/09/2026 23:00 UTC) · último cierre $0,003896.
  - En la consulta 08/10/2026 14:15 UTC: precio $0,003921, liquidez $299.271, FDV $3.765.941.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/10/2026 14:04 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003595 |
| Liquidez | $246.634 |
| MCap | $3.451.711 |
| Volumen 24 h | $1.649.187 |
| Cambio 24 h | +62% |
| Cambio m5 / h1 | -5,7% / +27,5% |
| Volumen m5 / h1 | $5.104 / $412.635 |
| Trades m5 (compras / ventas) | 40 / 31 |
| Edad del par | 10,2 días |
| Score del feed (WS) | 75 |

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

Desglose reconstruido desde los motivos registrados; suma 67 = score registrado 67 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 75 × 0,3 | +22,4 |
| MCap | ≥ $1M | $3.451.711 | +25 |
| Volumen 24 h | ≥ $1M | $1.649.187 | +20 |
| Buy pressure m5 | > 55% (par maduro) | 56% | +15 |
| Volumen m5 | > $1K (par maduro) | $5.104 | +10 |
| Par viejo | edad > 24 h | edad 10,2 días | -50 |
| Liquidez | ≥ $100K | $246.634 | +15 |
| Cambio 24 h | ≥ +50% | +62% | +10 |
| **Total** | recortado a 0–100 |  | **67** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-08T14:04:17+00:00, sin estado previo): **67** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >55%, Volumen activo m5 (>$1K), Par >24h, no nativo pump.fun, Liquidez alta, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 38 de 21.860 tokens analizados (0,17%) quedan ≥ 56. Con score 67, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/10/2026 14:04 UTC, hasta 10/10/2026 14:04 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -5,7% · h1 +27,5% · h24 +62% · volumen m5/h1 0,01 · edad del par 10,2 días.
- **Precio de entrada** (alerta): $0,003595.
- **Consulta 08/10/2026 14:15 UTC:** $0,003921 (+9,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump_2026-10-08_140417.json` · blob `b827fdf20988034f05775383155cdc25320619ec` · commit `da8d2ba` (2026-10-08T14:09:16Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-08_135413.json` · blob `cb775d2777d8cc572fe5e81da581c40e38fb9c7c` · commit `da8d2ba` (2026-10-08T14:09:16Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-08_140417`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump · registro · 08/10/2026 14:04 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump · HTTP 200 · 08/10/2026 14:15 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump/report · HTTP 200 · 08/10/2026 14:15 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump · HTTP 200 · 08/10/2026 14:15 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/2YaGc2iYZt44B5zn5Tvk59APbAn51xGekzNQAPF2PGn1/ohlcv/hour?limit=1000 · HTTP 200 · 08/10/2026 14:15 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump · HTTP 200 · 08/10/2026 14:15 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SWORDCATUSDT · HTTP 400 · 08/10/2026 14:15 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SWORDCAT-USD · HTTP 404 · 08/10/2026 14:15 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $299.271 vs $563.671 → 46,91%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003921 vs $0,003896 → 0,63%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump_2026-10-08_140417.json',encoding='utf-8'));d=d.get('5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump',d);p=mock.patch('time.time',return_value=1791468257);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/10/2026 14:15 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `fc58f800818b1894…`
