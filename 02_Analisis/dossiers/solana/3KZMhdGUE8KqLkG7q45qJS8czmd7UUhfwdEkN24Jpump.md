# XTO (XTO) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1873 · liquidez $1.186.491 · mcap $187.377.948 (al detectar)  
Detectado el 21/10/2026 09:57 UTC por: WS score muy alto, MCap > $1M, Volumen bajo (score 63, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 23/10/2026 09:57 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir XTO

Estudio de cómo se adquiere XTO, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 21/10/2026 10:29 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 21/10/2026 09:57 UTC | pumpswap `3NaQSAo…rcQz` | $1.186.491 | 1% | 0,017% | 0,169% | 1,686% | $5.932 | $17.797 |
| consulta 21/10/2026 10:29 UTC | pumpswap `3NaQSAo…rcQz` | $1.182.701 | 1% | 0,017% | 0,169% | 1,691% | $5.914 | $17.741 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump`
5. Configurar el slippage: 1% (liquidez $1.182.701, consulta 21/10/2026 10:29 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump) y el par en DexScreener (https://dexscreener.com/solana/3NaQSAok3eebqzzgmJZf5guuGzMgTYy2QQXXedqorcQz); mint authority / freeze authority: revocada / revocada · holders 3.234 · top-10 2,45% (consulta 21/10/2026 10:29 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump
- Par en DexScreener: https://dexscreener.com/solana/3NaQSAok3eebqzzgmJZf5guuGzMgTYy2QQXXedqorcQz
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.234 · top-10 2,45% (consulta 21/10/2026 10:29 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | XTO / XTO | registro de la detección (trending) |
| Mint / contrato | `3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `3NaQSAok3eebqzzgmJZf5guuGzMgTYy2QQXXedqorcQz` | DexScreener, al detectar (1 par(es) en la consulta 21/10/2026 10:29 UTC) |
| Deployer | `CC9bbbb1Nw2TWoACVpKukT8taAGLBiFKQbQC4BknFSHo` | RugCheck `creator` |
| Par creado | 14/10/2026 02:56 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 7,3 días / 7,3 días / 7,3 días | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 21/10/2026 10:29 UTC |
| Holders / top-10 | 3.234 / 2,45% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 21/10/2026 10:29 UTC |
| Holders efectivos del top-10 | 9,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 21/10/2026 10:29 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 21/10/2026 10:29 UTC |
| Links | DexScreener: https://dexscreener.com/solana/3NaQSAok3eebqzzgmJZf5guuGzMgTYy2QQXXedqorcQz · Solscan: https://solscan.io/token/3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump · pump.fun: https://pump.fun/coin/3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump · web / Telegram / X: no publicados en DexScreener | consulta 21/10/2026 10:29 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 21/10/2026 10:29 UTC)
- **Historia:**
  - Par creado el 14/10/2026 02:56 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 21/10/2026 09:57 UTC, con el par a 7,3 días de creado: precio $0,1873, mcap $187.377.948, liquidez $1.186.491.
  - Velas de 1 h de GeckoTerminal (177, desde 14/10/2026 02:00 UTC): apertura $0,02615 · máximo $0,1876 (21/10/2026 09:00 UTC) · mínimo $0,00004480 (14/10/2026 02:00 UTC) · último cierre $0,1868.
  - En la consulta 21/10/2026 10:29 UTC: precio $0,1870, liquidez $1.182.701, FDV $186.988.366.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 21/10/2026 09:57 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1873 |
| Liquidez | $1.186.491 |
| MCap | $187.377.948 |
| Volumen 24 h | $40.745 |
| Cambio 24 h | +18% |
| Cambio m5 / h1 | +0,1% / +0,6% |
| Volumen m5 / h1 | $89 / $1.548 |
| Trades m5 (compras / ventas) | 3 / 0 |
| Edad del par | 7,3 días |
| Score del feed (WS) | 94 |

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
| Score del feed | score WS × 0,3 | WS 94 × 0,3 | +28,1 |
| MCap | ≥ $1M | $187.377.948 | +25 |
| Volumen 24 h | < $50K | $40.745 | +0 |
| Buy pressure m5 | > 60% (par maduro) | 100% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,1% · h1 +0,6% | +20 |
| Par viejo | edad > 24 h | edad 7,3 días | -50 |
| Liquidez | ≥ $100K | $1.186.491 | +15 |
| **Total** | recortado a 0–100 |  | **63** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-21T09:57:16+00:00, sin estado previo): **63** · motivos: WS score muy alto, MCap > $1M, Volumen bajo, Buy pressure >60%, Momentum corto+medio positivo, Par >24h, no nativo pump.fun, Liquidez alta.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 73 de 42.880 tokens analizados (0,17%) quedan ≥ 56. Con score 63, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 21/10/2026 09:57 UTC, hasta 23/10/2026 09:57 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +0,1% · h1 +0,6% · h24 +18% · volumen m5/h1 0,06 · edad del par 7,3 días.
- **Precio de entrada** (alerta): $0,1873.
- **Consulta 21/10/2026 10:29 UTC:** $0,1870 (-0,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump_2026-10-21_095716.json` · blob `840c409aac918f3ea21e48aefbfdeffa8d4118b8` · commit `d17c77b` (2026-10-21T10:21:29Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-21_095018.json` · blob `e0eee2179381ef37a14453b8287563970cf0082e` · commit `d17c77b` (2026-10-21T10:21:29Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-21_095716`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump · registro · 21/10/2026 09:57 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump · HTTP 200 · 21/10/2026 10:29 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump/report · HTTP 200 · 21/10/2026 10:29 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump · HTTP 200 · 21/10/2026 10:29 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/3NaQSAok3eebqzzgmJZf5guuGzMgTYy2QQXXedqorcQz/ohlcv/hour?limit=1000 · HTTP 200 · 21/10/2026 10:29 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump · HTTP 404 · 21/10/2026 10:29 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=XTOUSDT · HTTP 400 · 21/10/2026 10:29 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/XTO-USD · HTTP 404 · 21/10/2026 10:29 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.182.701 vs $1.182.317 → 0,03%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1870 vs $0,1868 → 0,11%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump_2026-10-21_095716.json',encoding='utf-8'));d=d.get('3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump',d);p=mock.patch('time.time',return_value=1792576636);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3KZMhdGUE8KqLkG7q45qJS8czmd7UUhfwdEkN24Jpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 21/10/2026 10:29 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `c34bb227eb727259…`
