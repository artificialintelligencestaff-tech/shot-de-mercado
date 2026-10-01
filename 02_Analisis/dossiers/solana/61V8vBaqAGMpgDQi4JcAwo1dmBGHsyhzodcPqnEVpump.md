# AI Rig Complex (arc) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a meteora) · precio $0,07169 · liquidez $10.333.552 · mcap $71.693.009 (al detectar)  
Detectado el 01/10/2026 08:40 UTC por: WS score alto, MCap > $1M, Volumen bajo (score 72, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 03/10/2026 08:40 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir arc

Estudio de cómo se adquiere arc, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **meteora**; un agregador como Jupiter enruta la orden hacia ese pool.

Cotiza en exchanges centralizados (par confirmado por contrato en CoinGecko, consulta 01/10/2026 08:40 UTC): Kraken (https://pro.kraken.com/app/trade/ARC-USD)

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 01/10/2026 08:40 UTC | meteora `DW2QC5y…W6i9` | $10.333.552 | 1% | 0,002% | 0,019% | 0,194% | $51.668 | $155.003 |
| consulta 01/10/2026 08:40 UTC | meteora `DW2QC5y…W6i9` | $10.353.329 | 1% | 0,002% | 0,019% | 0,193% | $51.767 | $155.300 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en meteora
4. Pegar el mint y verificar que coincide carácter por carácter: `61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump`
5. Configurar el slippage: 1% (liquidez $10.353.329, consulta 01/10/2026 08:40 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump) y el par en DexScreener (https://dexscreener.com/solana/DW2QC5ychRKmA3YpY6eWetxt1YdMK8hir3vNjNjRW6i9); mint authority / freeze authority: revocada / revocada · holders 180.716 · top-10 80,92% (consulta 01/10/2026 08:40 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump
- Par en DexScreener: https://dexscreener.com/solana/DW2QC5ychRKmA3YpY6eWetxt1YdMK8hir3vNjNjRW6i9
- Página del lanzamiento (pump.fun): https://pump.fun/coin/61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 180.716 · top-10 80,92% (consulta 01/10/2026 08:40 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | AI Rig Complex / arc | registro de la detección (trending) |
| Mint / contrato | `61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump` | registro de la detección |
| Chain / DEX / par | Solana / meteora / `DW2QC5ychRKmA3YpY6eWetxt1YdMK8hir3vNjNjRW6i9` | DexScreener, al detectar (30 par(es) en la consulta 01/10/2026 08:40 UTC) |
| Deployer | `TSLvdd1pWpHVjahSpsvCXUbgwsL3JAcvokwaKt1eokM` | RugCheck `creator` |
| Par creado | 17/01/2025 16:44 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 621,7 días / 621,7 días / 621,7 días | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 01/10/2026 08:40 UTC |
| Holders / top-10 | 180.716 / 80,92% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 01/10/2026 08:40 UTC |
| Holders efectivos del top-10 | 5,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | meteoraDlmm 0%; raydium 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; orca 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora 21%; orca 0%; meteoraDlmm 0%; orca 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteora 100%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; orca 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 100%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; raydium_cpmm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 72%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; raydium_cpmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; pump_fun_amm 100%; meteoraDlmm 0%; raydium 100%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; orca 0%; pump_fun_amm 0%; raydium_cpmm 100%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; orca 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; orca 0%; meteoraDlmm 0%; orca 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; raydium_cpmm 100%; meteora_damm_v2 0%; meteoraDlmm 0%; raydium_cpmm 100%; meteoraDlmm 0%; meteoraDlmm 0%; pump_fun_amm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteora_damm_v2 0%; pump_fun_amm 0%; pump_fun_amm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; raydium_cpmm 100%; pump_fun_amm 100%; orca 0%; meteoraDlmm 0%; raydium_cpmm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; raydium_cpmm 100%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; orca 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; orca 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; tuna_fusion_amm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; pump_fun_amm 100%; orca 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; orca 0%; meteora_damm_v2 0%; raydium_cpmm 100%; raydium_cpmm 100%; meteoraDlmm 0%; meteora_damm_v2 0%; raydium_cpmm 100%; raydium_cpmm 100%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteora_damm_v2 0%; meteoraDlmm 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; raydium_cpmm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora 100%; pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; pump_fun_amm 100%; orca 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 01/10/2026 08:40 UTC |
| Etiquetas de RugCheck | «Single holder ownership», «High holder concentration» | RugCheck `risks[].name` (texto de la fuente), consulta 01/10/2026 08:40 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DW2QC5ychRKmA3YpY6eWetxt1YdMK8hir3vNjNjRW6i9 · Solscan: https://solscan.io/token/61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump · pump.fun: https://pump.fun/coin/61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump · web: https://www.arc.fun/ · web: https://www.arc.fun/manifesto.html · web: https://github.com/0xPlaygrounds/rig · twitter: https://x.com/arcdotfun · telegram: https://t.me/arcfunportal | consulta 01/10/2026 08:40 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a meteora
- **Categoría / narrativa:** CoinGecko: Artificial Intelligence (AI), Infrastructure, Solana Ecosystem, AI Agents, Pump.fun Ecosystem, AI Agent Launchpad, Binance Alpha Spotlight, AI Framework
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 01/10/2026 08:40 UTC)
- **Historia:**
  - Par creado el 17/01/2025 16:44 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 01/10/2026 08:40 UTC, con el par a 621,7 días de creado: precio $0,07169, mcap $71.693.009, liquidez $10.333.552.
  - Velas de 1 h de GeckoTerminal (1000, desde 19/08/2026 22:00 UTC): apertura $0,07229 · máximo $0,1142 (09/09/2026 17:00 UTC) · mínimo $0,06213 (20/09/2026 02:00 UTC) · último cierre $0,07180.
  - En la consulta 01/10/2026 08:40 UTC: precio $0,07183, liquidez $10.353.329, FDV $71.830.019.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 01/10/2026 08:40 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,07169 |
| Liquidez | $10.333.552 |
| MCap | $71.693.009 |
| Volumen 24 h | $6.955 |
| Cambio 24 h | +1% |
| Cambio m5 / h1 | +0,6% / +0,6% |
| Volumen m5 / h1 | $64 / $207 |
| Trades m5 (compras / ventas) | 5 / 0 |
| Edad del par | 621,7 días |
| Score del feed (WS) | 76 |

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

Desglose reconstruido desde los motivos registrados; suma 72 = score registrado 72 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 76 × 0,3 | +22,8 |
| MCap | ≥ $1M | $71.693.009 | +25 |
| Volumen 24 h | < $50K | $6.955 | +0 |
| Volumen m5/h1 | > 0,25 (par maduro) | 0,31 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 100% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,6% · h1 +0,6% | +20 |
| Par viejo | edad > 24 h | edad 621,7 días | -50 |
| Liquidez | ≥ $100K | $10.333.552 | +15 |
| **Total** | recortado a 0–100 |  | **72** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-01T08:40:22+00:00, sin estado previo): **72** · motivos: WS score alto, MCap > $1M, Volumen bajo, Volumen en aceleración (5m/1h > 25%), Buy pressure >60%, Momentum corto+medio positivo, Par >24h, no nativo pump.fun, Liquidez alta.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 4 de 3.701 tokens analizados (0,11%) quedan ≥ 56. Con score 72, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 01/10/2026 08:40 UTC, hasta 03/10/2026 08:40 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +0,6% · h1 +0,6% · h24 +1% · volumen m5/h1 0,31 · edad del par 621,7 días.
- **Precio de entrada** (alerta): $0,07169.
- **Consulta 01/10/2026 08:40 UTC:** $0,07183 (+0,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump_2026-10-01_084036.json` · blob `d166ce7e0c17fdd373c3a9d76391b6cc2aa28c8e` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-01_083519.json` · blob `392b0270ee97a2f91d975662e8a4862982275359` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-01_084036`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump · registro · 01/10/2026 08:40 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump · HTTP 200 · 01/10/2026 08:40 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump/report · HTTP 200 · 01/10/2026 08:40 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump · HTTP 200 · 01/10/2026 08:40 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DW2QC5ychRKmA3YpY6eWetxt1YdMK8hir3vNjNjRW6i9/ohlcv/hour?limit=1000 · HTTP 200 · 01/10/2026 08:40 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump · HTTP 200 · 01/10/2026 08:40 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ARCUSDT · HTTP 400 · 01/10/2026 08:40 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ARC-USD · HTTP 404 · 01/10/2026 08:40 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $10.353.329 vs $17.832.826 → 41,94%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,07183 vs $0,07180 → 0,04%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump_2026-10-01_084036.json',encoding='utf-8'));d=d.get('61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump',d);p=mock.patch('time.time',return_value=1790844022);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 01/10/2026 08:40 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `492b0c40245f07e5…`
