# Ansem is Back (AIB) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0003617 · liquidez $47.922 · mcap $359.919 (al detectar)  
Detectado el 12/11/2026 11:27 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 83, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 14/11/2026 11:27 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir AIB

Estudio de cómo se adquiere AIB, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 12/11/2026 11:28 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 12/11/2026 11:27 UTC | pumpswap `5jN7YxK…aGK3` | $47.922 | 10% | 0,417% | 4,173% | 41,735% | $240 | $719 |
| consulta 12/11/2026 11:27 UTC | pumpswap `5jN7YxK…aGK3` | $47.365 | 10% | 0,422% | 4,223% | 42,225% | $237 | $710 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump`
5. Configurar el slippage: 10% (liquidez $47.365, consulta 12/11/2026 11:27 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump) y el par en DexScreener (https://dexscreener.com/solana/5jN7YxKhncGwi3njP5Z8M6YYBKkuhL7p2axLLG2DaGK3); mint authority / freeze authority: revocada / revocada · holders 4.851 · top-10 20,14% (consulta 12/11/2026 11:27 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump
- Par en DexScreener: https://dexscreener.com/solana/5jN7YxKhncGwi3njP5Z8M6YYBKkuhL7p2axLLG2DaGK3
- Página del lanzamiento (pump.fun): https://pump.fun/coin/AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.851 · top-10 20,14% (consulta 12/11/2026 11:27 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Ansem is Back / AIB | registro de la detección (trending) |
| Mint / contrato | `AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `5jN7YxKhncGwi3njP5Z8M6YYBKkuhL7p2axLLG2DaGK3` | DexScreener, al detectar (3 par(es) en la consulta 12/11/2026 11:27 UTC) |
| Deployer | `FkLwrNJYkmG3d6ZxFUSX7wgu77xoYbFBewYniRRHTMTD` | RugCheck `creator` |
| Par creado | 12/11/2026 01:19 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,1 h / 10,1 h / 10,1 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 12/11/2026 11:27 UTC |
| Holders / top-10 | 4.851 / 20,14% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 12/11/2026 11:27 UTC |
| Holders efectivos del top-10 | 4,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 12/11/2026 11:27 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 12/11/2026 11:27 UTC |
| Links | DexScreener: https://dexscreener.com/solana/5jN7YxKhncGwi3njP5Z8M6YYBKkuhL7p2axLLG2DaGK3 · Solscan: https://solscan.io/token/AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump · pump.fun: https://pump.fun/coin/AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump · web: https://aibcoin.fun · twitter: https://x.com/AIBMemeCoin | consulta 12/11/2026 11:27 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 12/11/2026 11:27 UTC)
- **Historia:**
  - Par creado el 12/11/2026 01:19 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 12/11/2026 11:27 UTC, con el par a 10,1 h de creado: precio $0,0003617, mcap $359.919, liquidez $47.922.
  - Velas de 1 h de GeckoTerminal (11, desde 12/11/2026 01:00 UTC): apertura $0,0001232 · máximo $0,0009529 (12/11/2026 02:00 UTC) · mínimo $0,00005503 (12/11/2026 01:00 UTC) · último cierre $0,0003460.
  - En la consulta 12/11/2026 11:27 UTC: precio $0,0003536, liquidez $47.365, FDV $351.851.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 12/11/2026 11:27 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0003617 |
| Liquidez | $47.922 |
| MCap | $359.919 |
| Volumen 24 h | $1.812.777 |
| Cambio 24 h | +553% |
| Cambio m5 / h1 | -0,6% / -35,8% |
| Volumen m5 / h1 | $2.110 / $76.121 |
| Trades m5 (compras / ventas) | 205 / 186 |
| Edad del par | 10,1 h |
| Score del feed (WS) | 77 |

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

Desglose reconstruido desde los motivos registrados; suma 83 = score registrado 83 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 77 × 0,3 | +23,2 |
| MCap | ≥ $100K | $359.919 | +15 |
| Volumen 24 h | ≥ $1M | $1.812.777 | +20 |
| Volumen m5 | > $1K (par maduro) | $2.110 | +10 |
| Liquidez | ≥ $20K | $47.922 | +5 |
| Cambio 24 h | ≥ +50% | +553% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +553% · liq/mcap 13,3% | +0 |
| **Total** | recortado a 0–100 |  | **83** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-12T11:27:28+00:00, sin estado previo): **83** · motivos: WS score alto, MCap > $100K, Volumen masivo, Volumen activo m5 (>$1K), Liquidez mínima, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=13.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 97 de 47.096 tokens analizados (0,21%) quedan ≥ 56. Con score 83, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 12/11/2026 11:27 UTC, hasta 14/11/2026 11:27 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -0,6% · h1 -35,8% · h24 +553% · volumen m5/h1 0,03 · edad del par 10,1 h.
- **Precio de entrada** (alerta): $0,0003617.
- **Consulta 12/11/2026 11:27 UTC:** $0,0003536 (-2,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump_2026-11-12_112737.json` · blob `869c88515e675fa1d6f4ae1a077290a7e8796496` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-12_112225.json` · blob `db040ef230160f3cba6a987c28a0f815393bbeb4` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-12_112737`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump · registro · 12/11/2026 11:27 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump · HTTP 200 · 12/11/2026 11:27 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump/report · HTTP 200 · 12/11/2026 11:27 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump · HTTP 200 · 12/11/2026 11:27 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/5jN7YxKhncGwi3njP5Z8M6YYBKkuhL7p2axLLG2DaGK3/ohlcv/hour?limit=1000 · HTTP 200 · 12/11/2026 11:27 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump · HTTP 404 · 12/11/2026 11:27 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AIBUSDT · HTTP 400 · 12/11/2026 11:27 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AIB-USD · HTTP 404 · 12/11/2026 11:27 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $47.365 vs $46.969 → 0,84%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0003536 vs $0,0003460 → 2,15%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump_2026-11-12_112737.json',encoding='utf-8'));d=d.get('AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump',d);p=mock.patch('time.time',return_value=1794482848);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 12/11/2026 11:28 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `da49ee280eba7c1b…`
