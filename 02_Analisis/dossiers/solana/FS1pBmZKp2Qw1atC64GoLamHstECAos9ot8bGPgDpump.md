# Socks Neobank (Socks) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001645 · liquidez $31.634 · mcap $158.863 (al detectar)  
Detectado el 16/11/2026 00:00 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 18/11/2026 00:00 UTC (< 48 h) · vigente: quedan 45,1 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Socks

Estudio de cómo se adquiere Socks, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 16/11/2026 02:53 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 16/11/2026 00:00 UTC | pumpswap `AgqoLMP…aJK3` | $31.634 | 10% | 0,632% | 6,322% | 63,224% | $158 | $475 |
| consulta 16/11/2026 02:53 UTC | pumpswap `AgqoLMP…aJK3` | $28.094 | 10% | 0,712% | 7,119% | 71,188% | $140 | $421 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump`
5. Configurar el slippage: 10% (liquidez $28.094, consulta 16/11/2026 02:53 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump) y el par en DexScreener (https://dexscreener.com/solana/AgqoLMPxk7ETjY74TnyePqKSQQYTTsCrmMVgyQRkaJK3); mint authority / freeze authority: revocada / revocada · holders 5.362 · top-10 26,26% (consulta 16/11/2026 02:53 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump
- Par en DexScreener: https://dexscreener.com/solana/AgqoLMPxk7ETjY74TnyePqKSQQYTTsCrmMVgyQRkaJK3
- Página del lanzamiento (pump.fun): https://pump.fun/coin/FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.362 · top-10 26,26% (consulta 16/11/2026 02:53 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Socks Neobank / Socks | registro de la detección (trending) |
| Mint / contrato | `FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `AgqoLMPxk7ETjY74TnyePqKSQQYTTsCrmMVgyQRkaJK3` | DexScreener, al detectar (30 par(es) en la consulta 16/11/2026 02:53 UTC) |
| Deployer | `CrSbohT2Tm9RL4NsfriLt9wZ3xo8FVk5HoSKxGoepdVw` | RugCheck `creator` |
| Par creado | 15/11/2026 09:45 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 14,2 h / 14,2 h / 17,1 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 16/11/2026 02:53 UTC |
| Holders / top-10 | 5.362 / 26,26% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 16/11/2026 02:53 UTC |
| Holders efectivos del top-10 | 4,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; orca 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 16/11/2026 02:53 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 16/11/2026 02:53 UTC |
| Links | DexScreener: https://dexscreener.com/solana/AgqoLMPxk7ETjY74TnyePqKSQQYTTsCrmMVgyQRkaJK3 · Solscan: https://solscan.io/token/FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump · pump.fun: https://pump.fun/coin/FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump · web: https://www.thesocks.fun/ · twitter: https://x.com/SocksDotFun · telegram: https://t.me/sockneobank | consulta 16/11/2026 02:53 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 16/11/2026 02:53 UTC)
- **Historia:**
  - Par creado el 15/11/2026 09:45 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 16/11/2026 00:00 UTC, con el par a 14,2 h de creado: precio $0,0001645, mcap $158.863, liquidez $31.634.
  - Velas de 1 h de GeckoTerminal (18, desde 15/11/2026 09:00 UTC): apertura $0,00003018 · máximo $0,0005117 (15/11/2026 11:00 UTC) · mínimo $0,00002386 (15/11/2026 09:00 UTC) · último cierre $0,0001322.
  - En la consulta 16/11/2026 02:53 UTC: precio $0,0001309, liquidez $28.094, FDV $126.468.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 16/11/2026 00:00 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001645 |
| Liquidez | $31.634 |
| MCap | $158.863 |
| Volumen 24 h | $2.117.059 |
| Cambio 24 h | +445% |
| Cambio m5 / h1 | +8,2% / +12,4% |
| Volumen m5 / h1 | $1.204 / $14.433 |
| Trades m5 (compras / ventas) | 17 / 14 |
| Edad del par | 14,2 h |
| Score del feed (WS) | 70 |

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
| Score del feed | score WS × 0,3 | WS 70 × 0,3 | +21,0 |
| MCap | ≥ $100K | $158.863 | +15 |
| Volumen 24 h | ≥ $1M | $2.117.059 | +20 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +8,2% · h1 +12,4% | +20 |
| Volumen m5 | > $1K (par maduro) | $1.204 | +10 |
| Liquidez | ≥ $20K | $31.634 | +5 |
| Cambio 24 h | ≥ +50% | +445% | +10 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-16T00:00:42+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 102 de 47.283 tokens analizados (0,22%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 16/11/2026 00:00 UTC, hasta 18/11/2026 00:00 UTC · vigente: quedan 45,1 h.
- **Aceleración al detectar:** cambio m5 +8,2% · h1 +12,4% · h24 +445% · volumen m5/h1 0,08 · edad del par 14,2 h.
- **Precio de entrada** (alerta): $0,0001645.
- **Consulta 16/11/2026 02:53 UTC:** $0,0001309 (-20,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump_2026-11-16_000042.json` · blob `2d2dd24f51b83a4aabb631eb169a5bb012850376` · commit `899fca3` (2026-11-16T02:30:59Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-15_231000.json` · blob `cf65db130649059393033473352b0082c0772b93` · commit `899fca3` (2026-11-16T02:30:59Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-16_000042`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump · registro · 16/11/2026 00:00 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump · HTTP 200 · 16/11/2026 02:53 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump/report · HTTP 200 · 16/11/2026 02:53 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump · HTTP 200 · 16/11/2026 02:53 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/AgqoLMPxk7ETjY74TnyePqKSQQYTTsCrmMVgyQRkaJK3/ohlcv/hour?limit=1000 · HTTP 200 · 16/11/2026 02:53 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump · HTTP 404 · 16/11/2026 02:53 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SOCKSUSDT · HTTP 400 · 16/11/2026 02:53 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SOCKS-USD · HTTP 404 · 16/11/2026 02:53 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $28.094 vs $28.621 → 1,84%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001309 vs $0,0001322 → 0,97%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump_2026-11-16_000042.json',encoding='utf-8'));d=d.get('FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump',d);p=mock.patch('time.time',return_value=1794787242);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 16/11/2026 02:53 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `f0715f3322ea4c96…`
