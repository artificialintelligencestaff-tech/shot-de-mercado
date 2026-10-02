# Catecoin (CATE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,07079 · liquidez $3.212.335 · mcap $68.258.280 (al detectar)  
Detectado el 02/10/2026 07:56 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 59, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 04/10/2026 07:56 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir CATE

Estudio de cómo se adquiere CATE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 08:13 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 07:56 UTC | pumpswap `HMzvsEE…7ca3` | $3.212.335 | 1% | 0,006% | 0,062% | 0,623% | $16.062 | $48.185 |
| consulta 02/10/2026 08:12 UTC | pumpswap `HMzvsEE…7ca3` | $3.196.353 | 1% | 0,006% | 0,063% | 0,626% | $15.982 | $47.945 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump`
5. Configurar el slippage: 1% (liquidez $3.196.353, consulta 02/10/2026 08:12 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) y el par en DexScreener (https://dexscreener.com/solana/HMzvsEEmtzHhvZNw9uwbaG85HCTmFnkbhzUx16cy7ca3); mint authority / freeze authority: revocada / revocada · holders 358.924 · top-10 16,57% (consulta 02/10/2026 08:12 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump
- Par en DexScreener: https://dexscreener.com/solana/HMzvsEEmtzHhvZNw9uwbaG85HCTmFnkbhzUx16cy7ca3
- Página del lanzamiento (pump.fun): https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 358.924 · top-10 16,57% (consulta 02/10/2026 08:12 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Catecoin / CATE | registro de la detección (trending) |
| Mint / contrato | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HMzvsEEmtzHhvZNw9uwbaG85HCTmFnkbhzUx16cy7ca3` | DexScreener, al detectar (30 par(es) en la consulta 02/10/2026 08:12 UTC) |
| Deployer | `12cQ8tQsQNT4mNkRxjdYbmftbNR2q1ayygjF9wKrx6Jz` | RugCheck `creator` |
| Par creado | 26/07/2026 16:32 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 67,6 días / 67,6 días / 67,7 días | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 08:12 UTC |
| Holders / top-10 | 358.924 / 16,57% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 08:12 UTC |
| Holders efectivos del top-10 | 8,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 100%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; raydium_cpmm 100%; orca 0%; meteora_damm_v2 100%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; pump_fun_amm 0%; pump_fun_amm 0%; meteoraDlmm 0%; pump_fun_amm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteoraDlmm 0%; orca 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; orca 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; orca 0%; meteoraDlmm 0%; orca 0%; raydium_cpmm 100%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; raydium_cpmm 100%; meteora_damm_v2 0%; orca 0%; meteora_damm_v2 0%; tuna_fusion_amm 0%; orca 0%; tuna_fusion_amm 0%; raydium_cpmm 100%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 08:12 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 08:12 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HMzvsEEmtzHhvZNw9uwbaG85HCTmFnkbhzUx16cy7ca3 · Solscan: https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump · pump.fun: https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump · web: https://cate.meme/ · twitter: https://x.com/i/communities/2004330768022004131 · telegram: https://t.me/catecoin_telegram | consulta 02/10/2026 08:12 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 08:12 UTC)
- **Historia:**
  - Par creado el 26/07/2026 16:32 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 07:56 UTC, con el par a 67,6 días de creado: precio $0,07079, mcap $68.258.280, liquidez $3.212.335.
  - Velas de 1 h de GeckoTerminal (1000, desde 21/08/2026 17:00 UTC): apertura $0,04853 · máximo $0,1307 (19/09/2026 20:00 UTC) · mínimo $0,02379 (08/09/2026 07:00 UTC) · último cierre $0,06970.
  - En la consulta 02/10/2026 08:12 UTC: precio $0,06974, liquidez $3.196.353, FDV $67.245.757.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 07:56 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,07079 |
| Liquidez | $3.212.335 |
| MCap | $68.258.280 |
| Volumen 24 h | $5.141.994 |
| Cambio 24 h | +12% |
| Cambio m5 / h1 | +0,0% / -3,6% |
| Volumen m5 / h1 | $54 / $78.027 |
| Trades m5 (compras / ventas) | 4 / 2 |
| Edad del par | 67,6 días |
| Score del feed (WS) | 80 |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 1/1 (100,0%, IC90 27,0%–100,0%) · secundaria 0/0 resueltas (shadow_monitor.json).

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

Desglose reconstruido desde los motivos registrados; suma 59 = score registrado 59 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 80 × 0,3 | +24 |
| MCap | ≥ $1M | $68.258.280 | +25 |
| Volumen 24 h | ≥ $1M | $5.141.994 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 67% | +25 |
| Par viejo | edad > 24 h | edad 67,6 días | -50 |
| Liquidez | ≥ $100K | $3.212.335 | +15 |
| **Total** | recortado a 0–100 |  | **59** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T07:56:51+00:00, sin estado previo): **59** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Par >24h, no nativo pump.fun, Liquidez alta.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 8 de 7.153 tokens analizados (0,11%) quedan ≥ 56. Con score 59, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 07:56 UTC, hasta 04/10/2026 07:56 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +0,0% · h1 -3,6% · h24 +12% · volumen m5/h1 0,00 · edad del par 67,6 días.
- **Precio de entrada** (alerta): $0,07079.
- **Consulta 02/10/2026 08:12 UTC:** $0,06974 (-1,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump_2026-10-02_075651.json` · blob `3c763163b31ac694fa0b7380dd04c0d80fd32e9a` · commit `de11366` (2026-10-02T08:04:40Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-02_075028.json` · blob `b82fd5014c66c0dd4fce8be447c35adcb7742632` · commit `de11366` (2026-10-02T08:04:40Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_075651`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump · registro · 02/10/2026 07:56 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump · HTTP 200 · 02/10/2026 08:12 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump/report · HTTP 200 · 02/10/2026 08:12 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump · HTTP 200 · 02/10/2026 08:12 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HMzvsEEmtzHhvZNw9uwbaG85HCTmFnkbhzUx16cy7ca3/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 08:13 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump · HTTP 404 · 02/10/2026 08:13 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=CATEUSDT · HTTP 400 · 02/10/2026 08:13 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/CATE-USD · HTTP 404 · 02/10/2026 08:13 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.196.353 vs $4.121.150 → 22,44%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,06974 vs $0,06970 → 0,05%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump_2026-10-02_075651.json',encoding='utf-8'));d=d.get('Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump',d);p=mock.patch('time.time',return_value=1790927811);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 08:13 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `98f3e6c3697a95a9…`
