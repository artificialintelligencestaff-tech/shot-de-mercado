# Snowball (Snowball) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0005662 · liquidez $59.569 · mcap $566.220 (al detectar)  
Detectado el 27/11/2026 02:20 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 70, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 29/11/2026 02:20 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Snowball

Estudio de cómo se adquiere Snowball, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 27/11/2026 02:21 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 27/11/2026 02:20 UTC | pumpswap `AirCDeU…zKt2` | $59.569 | 5% | 0,336% | 3,357% | 33,574% | $298 | $894 |
| consulta 27/11/2026 02:20 UTC | pumpswap `AirCDeU…zKt2` | $59.569 | 5% | 0,336% | 3,357% | 33,574% | $298 | $894 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump`
5. Configurar el slippage: 5% (liquidez $59.569, consulta 27/11/2026 02:20 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) y el par en DexScreener (https://dexscreener.com/solana/AirCDeU4yL6hjuina65mtWAKzmex7STKZSiNMYZhzKt2); mint authority / freeze authority: revocada / revocada · holders 97.364 · top-10 23,18% (consulta 27/11/2026 02:20 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump
- Par en DexScreener: https://dexscreener.com/solana/AirCDeU4yL6hjuina65mtWAKzmex7STKZSiNMYZhzKt2
- Página del lanzamiento (pump.fun): https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 97.364 · top-10 23,18% (consulta 27/11/2026 02:20 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Snowball / Snowball | registro de la detección (trending) |
| Mint / contrato | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `AirCDeU4yL6hjuina65mtWAKzmex7STKZSiNMYZhzKt2` | DexScreener, al detectar (30 par(es) en la consulta 27/11/2026 02:20 UTC) |
| Deployer | `D4kuhipR2T9xsf6hwHynwWWS9SUbPacjmU3Lq75NwX8L` | RugCheck `creator` |
| Par creado | 25/11/2026 18:22 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 32,0 h / 32,0 h / 32,0 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 27/11/2026 02:20 UTC |
| Holders / top-10 | 97.364 / 23,18% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 27/11/2026 02:20 UTC |
| Holders efectivos del top-10 | 7,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 27/11/2026 02:20 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 27/11/2026 02:20 UTC |
| Links | DexScreener: https://dexscreener.com/solana/AirCDeU4yL6hjuina65mtWAKzmex7STKZSiNMYZhzKt2 · Solscan: https://solscan.io/token/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump · pump.fun: https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump · web: https://holdersnowball.fun/ · twitter: https://x.com/holdersnowball | consulta 27/11/2026 02:20 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 27/11/2026 02:20 UTC)
- **Historia:**
  - Par creado el 25/11/2026 18:22 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 27/11/2026 02:20 UTC, con el par a 32,0 h de creado: precio $0,0005662, mcap $566.220, liquidez $59.569.
  - Velas de 1 h de GeckoTerminal (33, desde 25/11/2026 18:00 UTC): apertura $0,00002980 · máximo $0,0008241 (26/11/2026 22:00 UTC) · mínimo $0,000006737 (25/11/2026 18:00 UTC) · último cierre $0,0005639.
  - En la consulta 27/11/2026 02:20 UTC: precio $0,0005662, liquidez $59.569, FDV $566.220.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 27/11/2026 02:20 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0005662 |
| Liquidez | $59.569 |
| MCap | $566.220 |
| Volumen 24 h | $1.697.101 |
| Cambio 24 h | +3.166% |
| Cambio m5 / h1 | +0,7% / -4,3% |
| Volumen m5 / h1 | $3.119 / $51.239 |
| Trades m5 (compras / ventas) | 57 / 36 |
| Edad del par | 32,0 h |
| Score del feed (WS) | 67 |

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

Desglose reconstruido desde los motivos registrados; suma 70 = score registrado 70 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 67 × 0,3 | +20,2 |
| MCap | ≥ $100K | $566.220 | +15 |
| Volumen 24 h | ≥ $1M | $1.697.101 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 61% | +25 |
| Momentum | m5 > 0 y h1 > −5% (par maduro) | m5 +0,7% · h1 -4,3% | +10 |
| Volumen m5 | > $1K (par maduro) | $3.119 | +10 |
| Par viejo | edad > 24 h | edad 32,0 h | -50 |
| Liquidez | ≥ $50K | $59.569 | +10 |
| Cambio 24 h | ≥ +50% | +3.166% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +3.166% · liq/mcap 10,5% | +0 |
| **Total** | recortado a 0–100 |  | **70** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-27T02:20:43+00:00, sin estado previo): **70** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Momentum corto positivo, Volumen activo m5 (>$1K), Par >24h, no nativo pump.fun, Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=10.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 112 de 47.717 tokens analizados (0,23%) quedan ≥ 56. Con score 70, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 27/11/2026 02:20 UTC, hasta 29/11/2026 02:20 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +0,7% · h1 -4,3% · h24 +3.166% · volumen m5/h1 0,06 · edad del par 32,0 h.
- **Precio de entrada** (alerta): $0,0005662.
- **Consulta 27/11/2026 02:20 UTC:** $0,0005662 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump_2026-11-27_022051.json` · blob `ffd10cd400b1070415127a1809a8b28dd3e97be8` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-27_021527.json` · blob `78601045617deba4e5585cb7c4156b66f30e603a` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-27_022051`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump · registro · 27/11/2026 02:20 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump · HTTP 200 · 27/11/2026 02:20 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump/report · HTTP 200 · 27/11/2026 02:20 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump · HTTP 200 · 27/11/2026 02:20 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/AirCDeU4yL6hjuina65mtWAKzmex7STKZSiNMYZhzKt2/ohlcv/hour?limit=1000 · HTTP 200 · 27/11/2026 02:20 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump · HTTP 404 · 27/11/2026 02:20 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SNOWBALLUSDT · HTTP 400 · 27/11/2026 02:20 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SNOWBALL-USD · HTTP 404 · 27/11/2026 02:21 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $59.569 vs $90.484 → 34,17%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0005662 vs $0,0005639 → 0,40%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump_2026-11-27_022051.json',encoding='utf-8'));d=d.get('9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump',d);p=mock.patch('time.time',return_value=1795746043);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 27/11/2026 02:21 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `119cbbf831ea19dc…`
