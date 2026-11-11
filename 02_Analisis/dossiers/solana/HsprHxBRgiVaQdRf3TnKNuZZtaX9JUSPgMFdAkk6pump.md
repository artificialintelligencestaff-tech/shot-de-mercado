# GTA6CAT (GATO) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,008908 · liquidez $313.325 · mcap $8.792.239 (al detectar)  
Detectado el 10/11/2026 21:28 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 69, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 12/11/2026 21:28 UTC (< 48 h) · vigente: quedan 44,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir GATO

Estudio de cómo se adquiere GATO, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/11/2026 00:48 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 10/11/2026 21:28 UTC | pumpswap `5E3dXLX…gt2m` | $313.325 | 3% | 0,064% | 0,638% | 6,383% | $1.567 | $4.700 |
| consulta 11/11/2026 00:48 UTC | pumpswap `5E3dXLX…gt2m` | $296.071 | 3% | 0,068% | 0,676% | 6,755% | $1.480 | $4.441 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump`
5. Configurar el slippage: 3% (liquidez $296.071, consulta 11/11/2026 00:48 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) y el par en DexScreener (https://dexscreener.com/solana/5E3dXLXGwmTDCokA51WYYaKttjFZBwqCoyUHBUi5gt2m); mint authority / freeze authority: revocada / revocada · holders 25.285 · top-10 16,26% (consulta 11/11/2026 00:48 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump
- Par en DexScreener: https://dexscreener.com/solana/5E3dXLXGwmTDCokA51WYYaKttjFZBwqCoyUHBUi5gt2m
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 25.285 · top-10 16,26% (consulta 11/11/2026 00:48 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | GTA6CAT / GATO | registro de la detección (trending) |
| Mint / contrato | `HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `5E3dXLXGwmTDCokA51WYYaKttjFZBwqCoyUHBUi5gt2m` | DexScreener, al detectar (10 par(es) en la consulta 11/11/2026 00:48 UTC) |
| Deployer | `5MVneCfDge5vtf4C7QZmczCJbBB8vfvDbMqvopvkBLJm` | RugCheck `creator` |
| Par creado | 25/08/2026 12:27 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 77,4 días / 77,4 días / 77,5 días | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/11/2026 00:48 UTC |
| Holders / top-10 | 25.285 / 16,26% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/11/2026 00:48 UTC |
| Holders efectivos del top-10 | 8,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; orca 0%; orca 0%; meteoraDlmm 0%; orca 0%; orca 0%; orca 0%; orca 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/11/2026 00:48 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 11/11/2026 00:48 UTC |
| Links | DexScreener: https://dexscreener.com/solana/5E3dXLXGwmTDCokA51WYYaKttjFZBwqCoyUHBUi5gt2m · Solscan: https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump · pump.fun: https://pump.fun/coin/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump · web: https://thegta6cat.com/ · twitter: https://x.com/TheGTA6cat | consulta 11/11/2026 00:48 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/11/2026 00:48 UTC)
- **Historia:**
  - Par creado el 25/08/2026 12:27 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 10/11/2026 21:28 UTC, con el par a 77,4 días de creado: precio $0,008908, mcap $8.792.239, liquidez $313.325.
  - Velas de 1 h de GeckoTerminal (1000, desde 30/09/2026 09:00 UTC): apertura $0,001562 · máximo $0,01512 (07/11/2026 17:00 UTC) · mínimo $0,001335 (02/10/2026 18:00 UTC) · último cierre $0,007854.
  - En la consulta 11/11/2026 00:48 UTC: precio $0,007931, liquidez $296.071, FDV $7.827.877.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 10/11/2026 21:28 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,008908 |
| Liquidez | $313.325 |
| MCap | $8.792.239 |
| Volumen 24 h | $2.170.413 |
| Cambio 24 h | -23% |
| Cambio m5 / h1 | -3,1% / -12,8% |
| Volumen m5 / h1 | $10.158 / $44.808 |
| Trades m5 (compras / ventas) | 34 / 13 |
| Edad del par | 77,4 días |
| Score del feed (WS) | 69 |

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

Desglose no reproducible desde los motivos registrados (suma 65 vs score 69; motivos sin regla: Anticipación (lib_early_signals early-0.2): +4 — volume_acceleration: vol 5 min ×2.7 la tasa horaria → +1.46; buy_pressure_shift: compras 72% en 5 min vs 54% en 1 h → +1.8; quiet_accumulation: precio quieto (m5 -3.1%) con vol ×2.7 y compras 72% → +1.47): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-10T21:28:40+00:00, sin estado previo): **65** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Par >24h, no nativo pump.fun, Liquidez alta.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 96 de 47.025 tokens analizados (0,20%) quedan ≥ 56. Con score 65, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 10/11/2026 21:28 UTC, hasta 12/11/2026 21:28 UTC · vigente: quedan 44,7 h.
- **Aceleración al detectar:** cambio m5 -3,1% · h1 -12,8% · h24 -23% · volumen m5/h1 0,23 · edad del par 77,4 días.
- **Precio de entrada** (alerta): $0,008908.
- **Consulta 11/11/2026 00:48 UTC:** $0,007931 (-11,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump_2026-11-10_212840.json` · blob `d4b88adff07797ee5b13446d94b6022190819ffa` · commit `eb15973` (2026-11-11T00:38:38Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-10_212840`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump · registro · 10/11/2026 21:28 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump · HTTP 200 · 11/11/2026 00:48 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump/report · HTTP 200 · 11/11/2026 00:48 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump · HTTP 200 · 11/11/2026 00:48 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/5E3dXLXGwmTDCokA51WYYaKttjFZBwqCoyUHBUi5gt2m/ohlcv/hour?limit=1000 · HTTP 200 · 11/11/2026 00:48 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump · HTTP 404 · 11/11/2026 00:48 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=GATOUSDT · HTTP 400 · 11/11/2026 00:48 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/GATO-USD · HTTP 404 · 11/11/2026 00:48 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $296.071 vs $447.557 → 33,85%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,007931 vs $0,007854 → 0,97%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump_2026-11-10_212840.json',encoding='utf-8'));d=d.get('HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump',d);p=mock.patch('time.time',return_value=1794346120);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/11/2026 00:48 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `c4b2cc18cc6bd500…`
