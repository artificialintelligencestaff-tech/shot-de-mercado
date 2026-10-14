# Hydra (Hydra) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00008685 · liquidez $25.622 · mcap $83.825 (al detectar)  
Detectado el 14/10/2026 10:28 UTC por: WS score alto, MCap > $50K, Volumen masivo (score 57, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 16/10/2026 10:28 UTC (< 48 h) · vigente: quedan 47,3 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Hydra

Estudio de cómo se adquiere Hydra, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 14/10/2026 11:11 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 14/10/2026 10:28 UTC | pumpswap `DYV6aZg…X2Td` | $25.622 | 10% | 0,781% | 7,806% | 78,058% | $128 | $384 |
| consulta 14/10/2026 11:11 UTC | pumpswap `DYV6aZg…X2Td` | $3.093 | 10% | 6,467% | 64,668% | 646,684% | $15 | $46 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump`
5. Configurar el slippage: 10% (liquidez $3.093, consulta 14/10/2026 11:11 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump) y el par en DexScreener (https://dexscreener.com/solana/DYV6aZgJT9QzqkMo3SShdViC7kMeLYBmCQ1V2dLLX2Td); mint authority / freeze authority: revocada / revocada · holders 3.821 · top-10 96,91% (consulta 14/10/2026 11:11 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump
- Par en DexScreener: https://dexscreener.com/solana/DYV6aZgJT9QzqkMo3SShdViC7kMeLYBmCQ1V2dLLX2Td
- Página del lanzamiento (pump.fun): https://pump.fun/coin/GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.821 · top-10 96,91% (consulta 14/10/2026 11:11 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Hydra / Hydra | registro de la detección (trending) |
| Mint / contrato | `GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DYV6aZgJT9QzqkMo3SShdViC7kMeLYBmCQ1V2dLLX2Td` | DexScreener, al detectar (3 par(es) en la consulta 14/10/2026 11:11 UTC) |
| Deployer | `HLdvShtrehwta2az1my3Z9KAX3c7tLooWaoRwhrNQCB5` | RugCheck `creator` |
| Par creado | 14/10/2026 01:34 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 8,9 h / 8,9 h / 9,6 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 14/10/2026 11:11 UTC |
| Holders / top-10 | 3.821 / 96,91% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 14/10/2026 11:11 UTC |
| Holders efectivos del top-10 | 1,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 14/10/2026 11:11 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 14/10/2026 11:11 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DYV6aZgJT9QzqkMo3SShdViC7kMeLYBmCQ1V2dLLX2Td · Solscan: https://solscan.io/token/GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump · pump.fun: https://pump.fun/coin/GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump · web: https://hydraai.world/ · twitter: https://x.com/hydraai_world | consulta 14/10/2026 11:11 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 14/10/2026 11:11 UTC)
- **Historia:**
  - Par creado el 14/10/2026 01:34 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 14/10/2026 10:28 UTC, con el par a 8,9 h de creado: precio $0,00008685, mcap $83.825, liquidez $25.622.
  - Velas de 1 h de GeckoTerminal (11, desde 14/10/2026 01:00 UTC): apertura $0,00004421 · máximo $0,0005612 (14/10/2026 05:00 UTC) · mínimo $0,000002668 (14/10/2026 11:00 UTC) · último cierre $0,000002732.
  - En la consulta 14/10/2026 11:11 UTC: precio $0,000002786, liquidez $3.093, FDV $2.690.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 14/10/2026 10:28 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00008685 |
| Liquidez | $25.622 |
| MCap | $83.825 |
| Volumen 24 h | $1.438.351 |
| Cambio 24 h | +96% |
| Cambio m5 / h1 | -2,3% / -49,5% |
| Volumen m5 / h1 | $10.516 / $193.093 |
| Trades m5 (compras / ventas) | 65 / 284 |
| Edad del par | 8,9 h |
| Score del feed (WS) | 75 |

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

Desglose reconstruido desde los motivos registrados; suma 57 = score registrado 57 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 75 × 0,3 | +22,5 |
| MCap | ≥ $50K | $83.825 | +10 |
| Volumen 24 h | ≥ $1M | $1.438.351 | +20 |
| Volumen m5 | > $1K (par maduro) | $10.516 | +10 |
| Venta dominante | buy pressure < 40% con volumen m5 | 19% | -20 |
| Liquidez | ≥ $20K | $25.622 | +5 |
| Cambio 24 h | ≥ +50% | +96% | +10 |
| **Total** | recortado a 0–100 |  | **57** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-14T10:28:57+00:00, sin estado previo): **57** · motivos: WS score alto, MCap > $50K, Volumen masivo, Volumen activo m5 (>$1K), Venta dominante (buy_pressure <40%), Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 55 de 34.655 tokens analizados (0,16%) quedan ≥ 56. Con score 57, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 14/10/2026 10:28 UTC, hasta 16/10/2026 10:28 UTC · vigente: quedan 47,3 h.
- **Aceleración al detectar:** cambio m5 -2,3% · h1 -49,5% · h24 +96% · volumen m5/h1 0,05 · edad del par 8,9 h.
- **Precio de entrada** (alerta): $0,00008685.
- **Consulta 14/10/2026 11:11 UTC:** $0,000002786 (-96,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump_2026-10-14_102857.json` · blob `9a6adb8b8c6d87913c82332eef195c86b2eb8697` · commit `5f8df52` (2026-10-14T11:04:18Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-14_102140.json` · blob `b7b1377c92402b0422c8784b5007e7dfa8133c75` · commit `5f8df52` (2026-10-14T11:04:18Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-14_102857`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump · registro · 14/10/2026 10:28 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump · HTTP 200 · 14/10/2026 11:11 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump/report · HTTP 200 · 14/10/2026 11:11 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump · HTTP 200 · 14/10/2026 11:11 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DYV6aZgJT9QzqkMo3SShdViC7kMeLYBmCQ1V2dLLX2Td/ohlcv/hour?limit=1000 · HTTP 200 · 14/10/2026 11:11 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump · HTTP 404 · 14/10/2026 11:11 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HYDRAUSDT · HTTP 400 · 14/10/2026 11:11 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HYDRA-USD · HTTP 404 · 14/10/2026 11:11 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.093 vs $3.268 → 5,36%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002786 vs $0,000002732 → 1,95%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump_2026-10-14_102857.json',encoding='utf-8'));d=d.get('GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump',d);p=mock.patch('time.time',return_value=1791973737);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint GZBTotcV7TPvquqQgjKKStyd4yk7nQ7gGttqLjwtpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 14/10/2026 11:11 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `9d7fb74b49393301…`
