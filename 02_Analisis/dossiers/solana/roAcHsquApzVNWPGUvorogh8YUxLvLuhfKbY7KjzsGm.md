# Yapping Roaches (YAPROACH) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000003164 · liquidez $3.473 · mcap $3.095 (al detectar)  
Detectado el 22/10/2026 22:55 UTC por: WS score alto, MCap bajo, Volumen masivo (score 79, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 24/10/2026 22:55 UTC (< 48 h) · vigente: quedan 47,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir YAPROACH

Estudio de cómo se adquiere YAPROACH, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 22/10/2026 23:54 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 22/10/2026 22:55 UTC | pumpswap `EcniqD2…t27F` | $3.473 | 10% | 5,759% | 57,595% | 575,946% | $17 | $52 |
| consulta 22/10/2026 23:54 UTC | pumpswap `EcniqD2…t27F` | $3.433 | 10% | 5,826% | 58,258% | 582,576% | $17 | $51 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm`
5. Configurar el slippage: 10% (liquidez $3.433, consulta 22/10/2026 23:54 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm) y el par en DexScreener (https://dexscreener.com/solana/EcniqD24ETYitYhWEm3iNPCJFVwgSzYCQsRVN2eit27F); mint authority / freeze authority: revocada / revocada · holders 1.328 · top-10 98,23% (consulta 22/10/2026 23:54 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm
- Par en DexScreener: https://dexscreener.com/solana/EcniqD24ETYitYhWEm3iNPCJFVwgSzYCQsRVN2eit27F
- Página del lanzamiento (pump.fun): https://pump.fun/coin/roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.328 · top-10 98,23% (consulta 22/10/2026 23:54 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Yapping Roaches / YAPROACH | registro de la detección (trending) |
| Mint / contrato | `roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `EcniqD24ETYitYhWEm3iNPCJFVwgSzYCQsRVN2eit27F` | DexScreener, al detectar (4 par(es) en la consulta 22/10/2026 23:54 UTC) |
| Deployer | `YAPPiN94hnsfPNC1LSbjixsTh6FdJ4TCVERV3cjGzmR` | RugCheck `creator` |
| Par creado | 22/10/2026 12:25 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,5 h / 10,5 h / 11,5 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 22/10/2026 23:54 UTC |
| Holders / top-10 | 1.328 / 98,23% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 22/10/2026 23:54 UTC |
| Holders efectivos del top-10 | 1,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 22/10/2026 23:54 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 22/10/2026 23:54 UTC |
| Links | DexScreener: https://dexscreener.com/solana/EcniqD24ETYitYhWEm3iNPCJFVwgSzYCQsRVN2eit27F · Solscan: https://solscan.io/token/roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm · pump.fun: https://pump.fun/coin/roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm · web: https://yaproach.com/ · twitter: https://x.com/yaproach | consulta 22/10/2026 23:54 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 22/10/2026 23:54 UTC)
- **Historia:**
  - Par creado el 22/10/2026 12:25 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 22/10/2026 22:55 UTC, con el par a 10,5 h de creado: precio $0,000003164, mcap $3.095, liquidez $3.473.
  - Velas de 1 h de GeckoTerminal (12, desde 22/10/2026 12:00 UTC): apertura $0,00004888 · máximo $0,0007533 (22/10/2026 13:00 UTC) · mínimo $0,000003028 (22/10/2026 13:00 UTC) · último cierre $0,000003118.
  - En la consulta 22/10/2026 23:54 UTC: precio $0,000003115, liquidez $3.433, FDV $3.047.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 22/10/2026 22:55 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000003164 |
| Liquidez | $3.473 |
| MCap | $3.095 |
| Volumen 24 h | $4.171.742 |
| Cambio 24 h | -93% |
| Cambio m5 / h1 | +0,0% / -2,5% |
| Volumen m5 / h1 | $0 / $26 |
| Trades m5 (compras / ventas) | 0 / 0 |
| Edad del par | 10,5 h |
| Score del feed (WS) | 65 |

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

Desglose no reproducible desde los motivos registrados (suma 4 vs score 79; motivos sin regla: score de detección 79 (script_82, hace 1 min) > re-score 4: vale el de detección (paridad con script_97)): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-22T22:55:38+00:00, sin estado previo): **4** · motivos: WS score alto, MCap bajo, Volumen masivo, Detección tardía (sin datos m5, >4h), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 75 de 44.367 tokens analizados (0,17%) quedan ≥ 56. Con score 4, este activo queda en el percentil 85,5 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 22/10/2026 22:55 UTC, hasta 24/10/2026 22:55 UTC · vigente: quedan 47,0 h.
- **Aceleración al detectar:** cambio m5 +0,0% · h1 -2,5% · h24 -93% · volumen m5/h1 0,00 · edad del par 10,5 h.
- **Precio de entrada** (alerta): $0,000003164.
- **Consulta 22/10/2026 23:54 UTC:** $0,000003115 (-1,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm_2026-10-22_225538.json` · blob `04569c5bdc25bca64273a0d96f8ff608a42450f7` · commit `210fba4` (2026-10-22T23:45:35Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-22_224922.json` · blob `52c4e51450e1fa34f00edf529d5774be2c9afaab` · commit `210fba4` (2026-10-22T23:45:35Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-22_225538`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm · registro · 22/10/2026 22:55 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm · HTTP 200 · 22/10/2026 23:54 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm/report · HTTP 200 · 22/10/2026 23:54 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm · HTTP 200 · 22/10/2026 23:54 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/EcniqD24ETYitYhWEm3iNPCJFVwgSzYCQsRVN2eit27F/ohlcv/hour?limit=1000 · HTTP 200 · 22/10/2026 23:54 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm · HTTP 404 · 22/10/2026 23:54 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=YAPROACHUSDT · HTTP 400 · 22/10/2026 23:54 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/YAPROACH-USD · HTTP 404 · 22/10/2026 23:54 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.433 vs $3.558 → 3,51%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000003115 vs $0,000003118 → 0,08%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm_2026-10-22_225538.json',encoding='utf-8'));d=d.get('roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm',d);p=mock.patch('time.time',return_value=1792709738);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint roAcHsquApzVNWPGUvorogh8YUxLvLuhfKbY7KjzsGm --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 22/10/2026 23:54 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `586da5a7bc5c15ea…`
