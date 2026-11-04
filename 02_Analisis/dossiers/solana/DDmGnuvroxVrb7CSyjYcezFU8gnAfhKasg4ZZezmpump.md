# A Meme Dog (AMD) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001276 · liquidez $119.400 · mcap $1.227.375 (al detectar)  
Detectado el 04/11/2026 06:46 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 06/11/2026 06:46 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir AMD

Estudio de cómo se adquiere AMD, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 04/11/2026 06:47 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 04/11/2026 06:46 UTC | pumpswap `7RD5YAL…KeCv` | $119.400 | 5% | 0,168% | 1,675% | 16,750% | $597 | $1.791 |
| consulta 04/11/2026 06:47 UTC | pumpswap `7RD5YAL…KeCv` | $119.608 | 5% | 0,167% | 1,672% | 16,721% | $598 | $1.794 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump`
5. Configurar el slippage: 5% (liquidez $119.608, consulta 04/11/2026 06:47 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump) y el par en DexScreener (https://dexscreener.com/solana/7RD5YALHcMLUFKJ8FRePGd6ei11F15uXZF1rc7mPKeCv); mint authority / freeze authority: revocada / revocada · holders 17.255 · top-10 19,10% (consulta 04/11/2026 06:47 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump
- Par en DexScreener: https://dexscreener.com/solana/7RD5YALHcMLUFKJ8FRePGd6ei11F15uXZF1rc7mPKeCv
- Página del lanzamiento (pump.fun): https://pump.fun/coin/DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 17.255 · top-10 19,10% (consulta 04/11/2026 06:47 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | A Meme Dog / AMD | registro de la detección (trending) |
| Mint / contrato | `DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7RD5YALHcMLUFKJ8FRePGd6ei11F15uXZF1rc7mPKeCv` | DexScreener, al detectar (30 par(es) en la consulta 04/11/2026 06:47 UTC) |
| Deployer | `Cx3tv9NrdDWQ8v6QwgngXH36Sm26qT7sR79NHod9UEgc` | RugCheck `creator` |
| Par creado | 03/11/2026 21:30 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 9,3 h / 9,3 h / 9,3 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 04/11/2026 06:47 UTC |
| Holders / top-10 | 17.255 / 19,10% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 04/11/2026 06:47 UTC |
| Holders efectivos del top-10 | 7,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; manifest 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; raydium_clmm 0%; manifest 0%; orca 0%; meteora_damm_v2 0%; orca 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 04/11/2026 06:47 UTC |
| Etiquetas de RugCheck | «Copycat token» | RugCheck `risks[].name` (texto de la fuente), consulta 04/11/2026 06:47 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7RD5YALHcMLUFKJ8FRePGd6ei11F15uXZF1rc7mPKeCv · Solscan: https://solscan.io/token/DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump · pump.fun: https://pump.fun/coin/DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump · twitter: https://x.com/SKupeal1973/status/2117728954882678804 | consulta 04/11/2026 06:47 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 04/11/2026 06:47 UTC)
- **Historia:**
  - Par creado el 03/11/2026 21:30 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 04/11/2026 06:46 UTC, con el par a 9,3 h de creado: precio $0,001276, mcap $1.227.375, liquidez $119.400.
  - Velas de 1 h de GeckoTerminal (10, desde 03/11/2026 21:00 UTC): apertura $0,00004857 · máximo $0,003668 (03/11/2026 23:00 UTC) · mínimo $0,00001778 (03/11/2026 21:00 UTC) · último cierre $0,001281.
  - En la consulta 04/11/2026 06:47 UTC: precio $0,001280, liquidez $119.608, FDV $1.231.388.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 04/11/2026 06:46 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001276 |
| Liquidez | $119.400 |
| MCap | $1.227.375 |
| Volumen 24 h | $9.422.901 |
| Cambio 24 h | +2.537% |
| Cambio m5 / h1 | +5,0% / -1,6% |
| Volumen m5 / h1 | $5.352 / $115.510 |
| Trades m5 (compras / ventas) | 26 / 34 |
| Edad del par | 9,3 h |
| Score del feed (WS) | 71 |

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
| Score del feed | score WS × 0,3 | WS 71 × 0,3 | +21,2 |
| MCap | ≥ $1M | $1.227.375 | +25 |
| Volumen 24 h | ≥ $1M | $9.422.901 | +20 |
| Momentum | m5 > 0 y h1 > −5% (par maduro) | m5 +5,0% · h1 -1,6% | +10 |
| Volumen m5 | > $1K (par maduro) | $5.352 | +10 |
| Liquidez | ≥ $100K | $119.400 | +15 |
| Cambio 24 h | ≥ +50% | +2.537% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +2.537% · liq/mcap 9,7% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-04T06:46:39+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Momentum corto positivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=9.7% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 90 de 46.634 tokens analizados (0,19%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 04/11/2026 06:46 UTC, hasta 06/11/2026 06:46 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +5,0% · h1 -1,6% · h24 +2.537% · volumen m5/h1 0,05 · edad del par 9,3 h.
- **Precio de entrada** (alerta): $0,001276.
- **Consulta 04/11/2026 06:47 UTC:** $0,001280 (+0,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump_2026-11-04_064654.json` · blob `ff73b5a32a639e91a12a9052bbf047cf78cd557c` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-04_064136.json` · blob `e4594b75800a29d9eac9810088a7ad17a542b4ef` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-04_064654`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump · registro · 04/11/2026 06:46 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump · HTTP 200 · 04/11/2026 06:47 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump/report · HTTP 200 · 04/11/2026 06:47 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump · HTTP 200 · 04/11/2026 06:47 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7RD5YALHcMLUFKJ8FRePGd6ei11F15uXZF1rc7mPKeCv/ohlcv/hour?limit=1000 · HTTP 200 · 04/11/2026 06:47 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump · HTTP 404 · 04/11/2026 06:47 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AMDUSDT · HTTP 400 · 04/11/2026 06:47 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AMD-USD · HTTP 404 · 04/11/2026 06:47 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $119.608 vs $241.814 → 50,54%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001280 vs $0,001281 → 0,09%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump_2026-11-04_064654.json',encoding='utf-8'));d=d.get('DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump',d);p=mock.patch('time.time',return_value=1793774799);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 04/11/2026 06:47 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `d41f1d16f2524466…`
