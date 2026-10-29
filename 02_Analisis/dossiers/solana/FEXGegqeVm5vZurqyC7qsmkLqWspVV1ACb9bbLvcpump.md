# Dubble (DUBBLE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,002176 · liquidez $137.473 · mcap $2.143.810 (al detectar)  
Detectado el 28/10/2026 22:11 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 30/10/2026 22:11 UTC (< 48 h) · vigente: quedan 44,3 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir DUBBLE

Estudio de cómo se adquiere DUBBLE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 29/10/2026 01:56 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 28/10/2026 22:11 UTC | pumpswap `EWiqwm9…4P24` | $137.473 | 5% | 0,145% | 1,455% | 14,548% | $687 | $2.062 |
| consulta 29/10/2026 01:55 UTC | pumpswap `EWiqwm9…4P24` | $150.503 | 5% | 0,133% | 1,329% | 13,289% | $753 | $2.258 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump`
5. Configurar el slippage: 5% (liquidez $150.503, consulta 29/10/2026 01:55 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump) y el par en DexScreener (https://dexscreener.com/solana/EWiqwm9wXVoj5yyb8VV2FkS9rc5HWJ3PmtwCKuv94P24); mint authority / freeze authority: revocada / revocada · holders 7.814 · top-10 3,77% (consulta 29/10/2026 01:55 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump
- Par en DexScreener: https://dexscreener.com/solana/EWiqwm9wXVoj5yyb8VV2FkS9rc5HWJ3PmtwCKuv94P24
- Página del lanzamiento (pump.fun): https://pump.fun/coin/FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 7.814 · top-10 3,77% (consulta 29/10/2026 01:55 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Dubble / DUBBLE | registro de la detección (trending) |
| Mint / contrato | `FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `EWiqwm9wXVoj5yyb8VV2FkS9rc5HWJ3PmtwCKuv94P24` | DexScreener, al detectar (3 par(es) en la consulta 29/10/2026 01:55 UTC) |
| Deployer | `Gg3XQwbH25TniQppLvk3cVcnY2ygPiT2f3QhX6Z9MSqH` | RugCheck `creator` |
| Par creado | 28/10/2026 15:02 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 7,2 h / 7,2 h / 10,9 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 29/10/2026 01:55 UTC |
| Holders / top-10 | 7.814 / 3,77% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 29/10/2026 01:55 UTC |
| Holders efectivos del top-10 | 1,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; orca 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 29/10/2026 01:55 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 29/10/2026 01:55 UTC |
| Links | DexScreener: https://dexscreener.com/solana/EWiqwm9wXVoj5yyb8VV2FkS9rc5HWJ3PmtwCKuv94P24 · Solscan: https://solscan.io/token/FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump · pump.fun: https://pump.fun/coin/FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump · web: https://dubblepad.fun · twitter: https://x.com/DubblePadX | consulta 29/10/2026 01:55 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 29/10/2026 01:55 UTC)
- **Historia:**
  - Par creado el 28/10/2026 15:02 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 28/10/2026 22:11 UTC, con el par a 7,2 h de creado: precio $0,002176, mcap $2.143.810, liquidez $137.473.
  - Velas de 1 h de GeckoTerminal (11, desde 28/10/2026 15:00 UTC): apertura $0,0001379 · máximo $0,005097 (28/10/2026 23:00 UTC) · mínimo $0,00004114 (28/10/2026 15:00 UTC) · último cierre $0,002584.
  - En la consulta 29/10/2026 01:55 UTC: precio $0,002592, liquidez $150.503, FDV $2.553.447.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 28/10/2026 22:11 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,002176 |
| Liquidez | $137.473 |
| MCap | $2.143.810 |
| Volumen 24 h | $5.143.726 |
| Cambio 24 h | +4.850% |
| Cambio m5 / h1 | +12,7% / +0,5% |
| Volumen m5 / h1 | $7.452 / $201.785 |
| Trades m5 (compras / ventas) | 375 / 183 |
| Edad del par | 7,2 h |
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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 69 × 0,3 | +20,6 |
| MCap | ≥ $1M | $2.143.810 | +25 |
| Volumen 24 h | ≥ $1M | $5.143.726 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 67% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +12,7% · h1 +0,5% | +20 |
| Volumen m5 | > $1K (par maduro) | $7.452 | +10 |
| Liquidez | ≥ $100K | $137.473 | +15 |
| Cambio 24 h | ≥ +50% | +4.850% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +4.850% · liq/mcap 6,4% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-28T22:11:16+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=6.4% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 80 de 46.197 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 28/10/2026 22:11 UTC, hasta 30/10/2026 22:11 UTC · vigente: quedan 44,3 h.
- **Aceleración al detectar:** cambio m5 +12,7% · h1 +0,5% · h24 +4.850% · volumen m5/h1 0,04 · edad del par 7,2 h.
- **Precio de entrada** (alerta): $0,002176.
- **Consulta 29/10/2026 01:55 UTC:** $0,002592 (+19,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump_2026-10-28_221116.json` · blob `4ec223ba5d77f63c213d024e27d21ce0ae59a7e7` · commit `a72e593` (2026-10-29T01:40:52Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-28_220520.json` · blob `578ddbb078cd4cfe1b7bcf3b760f95dbeea1a66d` · commit `a72e593` (2026-10-29T01:40:52Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-28_221116`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump · registro · 28/10/2026 22:11 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump · HTTP 200 · 29/10/2026 01:55 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump/report · HTTP 200 · 29/10/2026 01:56 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump · HTTP 200 · 29/10/2026 01:56 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/EWiqwm9wXVoj5yyb8VV2FkS9rc5HWJ3PmtwCKuv94P24/ohlcv/hour?limit=1000 · HTTP 200 · 29/10/2026 01:56 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump · HTTP 404 · 29/10/2026 01:56 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=DUBBLEUSDT · HTTP 400 · 29/10/2026 01:56 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/DUBBLE-USD · HTTP 404 · 29/10/2026 01:56 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $150.503 vs $149.641 → 0,57%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002592 vs $0,002584 → 0,32%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump_2026-10-28_221116.json',encoding='utf-8'));d=d.get('FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump',d);p=mock.patch('time.time',return_value=1793225476);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 29/10/2026 01:56 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `13de73e7bc10a05e…`
