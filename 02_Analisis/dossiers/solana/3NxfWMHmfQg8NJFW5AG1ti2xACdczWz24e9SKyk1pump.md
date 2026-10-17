# Minter (MINTER) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,005453 · liquidez $209.454 · mcap $5.428.127 (al detectar)  
Detectado el 17/10/2026 22:26 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 19/10/2026 22:26 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir MINTER

Estudio de cómo se adquiere MINTER, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 17/10/2026 22:47 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 17/10/2026 22:26 UTC | pumpswap `3p3yajJ…kNRJ` | $209.454 | 5% | 0,095% | 0,955% | 9,549% | $1.047 | $3.142 |
| consulta 17/10/2026 22:46 UTC | pumpswap `3p3yajJ…kNRJ` | $208.449 | 5% | 0,096% | 0,959% | 9,595% | $1.042 | $3.127 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump`
5. Configurar el slippage: 5% (liquidez $208.449, consulta 17/10/2026 22:46 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump) y el par en DexScreener (https://dexscreener.com/solana/3p3yajJRqwrvgNs3M1UDVDXVUriZjZ8vE8bdpnpvkNRJ); mint authority / freeze authority: revocada / revocada · holders 6.043 · top-10 4,39% (consulta 17/10/2026 22:46 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump
- Par en DexScreener: https://dexscreener.com/solana/3p3yajJRqwrvgNs3M1UDVDXVUriZjZ8vE8bdpnpvkNRJ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 6.043 · top-10 4,39% (consulta 17/10/2026 22:46 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Minter / MINTER | registro de la detección (trending) |
| Mint / contrato | `3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `3p3yajJRqwrvgNs3M1UDVDXVUriZjZ8vE8bdpnpvkNRJ` | DexScreener, al detectar (2 par(es) en la consulta 17/10/2026 22:46 UTC) |
| Deployer | `7xvctBv6LK5i9uGgkQUo7yQfCimnVW2PpXr3V4uXaABw` | RugCheck `creator` |
| Par creado | 17/10/2026 21:24 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 61,2 min / 61,2 min / 82,3 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 17/10/2026 22:46 UTC |
| Holders / top-10 | 6.043 / 4,39% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 17/10/2026 22:46 UTC |
| Holders efectivos del top-10 | 4,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 17/10/2026 22:46 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 17/10/2026 22:46 UTC |
| Links | DexScreener: https://dexscreener.com/solana/3p3yajJRqwrvgNs3M1UDVDXVUriZjZ8vE8bdpnpvkNRJ · Solscan: https://solscan.io/token/3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump · pump.fun: https://pump.fun/coin/3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump · web: https://minter.live · twitter: https://x.com/MinterXSOL | consulta 17/10/2026 22:46 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 17/10/2026 22:46 UTC)
- **Historia:**
  - Par creado el 17/10/2026 21:24 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 17/10/2026 22:26 UTC, con el par a 61,2 min de creado: precio $0,005453, mcap $5.428.127, liquidez $209.454.
  - Velas de 1 h de GeckoTerminal (2, desde 17/10/2026 21:00 UTC): apertura $0,00005647 · máximo $0,008336 (17/10/2026 22:00 UTC) · mínimo $0,00005647 (17/10/2026 21:00 UTC) · último cierre $0,005224.
  - En la consulta 17/10/2026 22:46 UTC: precio $0,005379, liquidez $208.449, FDV $5.353.681.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 17/10/2026 22:26 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,005453 |
| Liquidez | $209.454 |
| MCap | $5.428.127 |
| Volumen 24 h | $3.714.334 |
| Cambio 24 h | +9.469% |
| Cambio m5 / h1 | -20,4% / +1.291,0% |
| Volumen m5 / h1 | $235.510 / $3.642.017 |
| Trades m5 (compras / ventas) | 1.729 / 579 |
| Edad del par | 61,2 min |
| Score del feed (WS) | 85 |

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
| Score del feed | score WS × 0,3 | WS 85 × 0,3 | +25,5 |
| MCap | ≥ $1M | $5.428.127 | +25 |
| Volumen 24 h | ≥ $1M | $3.714.334 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 75% | +25 |
| Edge temprano | edad < 4 h (par maduro) | edad 61,2 min | +8 |
| Volumen m5 | > $1K (par maduro) | $235.510 | +10 |
| Liquidez | ≥ $100K | $209.454 | +15 |
| Cambio 24 h | ≥ +50% | +9.469% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +9.469% · liq/mcap 3,9% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-17T22:26:06+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=3.9% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 65 de 38.922 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 17/10/2026 22:26 UTC, hasta 19/10/2026 22:26 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 -20,4% · h1 +1.291,0% · h24 +9.469% · volumen m5/h1 0,06 · edad del par 61,2 min.
- **Precio de entrada** (alerta): $0,005453.
- **Consulta 17/10/2026 22:46 UTC:** $0,005379 (-1,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump_2026-10-17_222606.json` · blob `f3b9037af052e2161a1011c30ac7be09307554a2` · commit `05f9c32` (2026-10-17T22:37:13Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-17_221209.json` · blob `e9b5ee7dc21e34142760e52848018319ee2229f6` · commit `05f9c32` (2026-10-17T22:37:13Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-17_222606`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump · registro · 17/10/2026 22:26 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump · HTTP 200 · 17/10/2026 22:46 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump/report · HTTP 200 · 17/10/2026 22:47 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump · HTTP 200 · 17/10/2026 22:47 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/3p3yajJRqwrvgNs3M1UDVDXVUriZjZ8vE8bdpnpvkNRJ/ohlcv/hour?limit=1000 · HTTP 200 · 17/10/2026 22:47 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump · HTTP 404 · 17/10/2026 22:47 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MINTERUSDT · HTTP 400 · 17/10/2026 22:47 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MINTER-USD · HTTP 404 · 17/10/2026 22:47 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $208.449 vs $205.481 → 1,42%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,005379 vs $0,005224 → 2,88%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump_2026-10-17_222606.json',encoding='utf-8'));d=d.get('3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump',d);p=mock.patch('time.time',return_value=1792275966);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3NxfWMHmfQg8NJFW5AG1ti2xACdczWz24e9SKyk1pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 17/10/2026 22:47 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `dffed61198bc35d6…`
