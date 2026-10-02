# BlackHoles (BlackHoles) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0002677 · liquidez $50.160 · mcap $259.570 (al detectar)  
Detectado el 02/10/2026 09:38 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 87, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 04/10/2026 09:38 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir BlackHoles

Estudio de cómo se adquiere BlackHoles, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 09:55 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 09:38 UTC | pumpswap `GEShq9L…m5ie` | $50.160 | 5% | 0,399% | 3,987% | 39,873% | $251 | $752 |
| consulta 02/10/2026 09:55 UTC | pumpswap `GEShq9L…m5ie` | $58.738 | 5% | 0,340% | 3,405% | 34,049% | $294 | $881 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump`
5. Configurar el slippage: 5% (liquidez $58.738, consulta 02/10/2026 09:55 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump) y el par en DexScreener (https://dexscreener.com/solana/GEShq9LZ2yyatWVmZvRD1jQYFMhQSfhVyCFztqA8m5ie); mint authority / freeze authority: revocada / revocada · holders 5.084 · top-10 16,72% (consulta 02/10/2026 09:55 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump
- Par en DexScreener: https://dexscreener.com/solana/GEShq9LZ2yyatWVmZvRD1jQYFMhQSfhVyCFztqA8m5ie
- Página del lanzamiento (pump.fun): https://pump.fun/coin/6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.084 · top-10 16,72% (consulta 02/10/2026 09:55 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | BlackHoles / BlackHoles | registro de la detección (trending) |
| Mint / contrato | `6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `GEShq9LZ2yyatWVmZvRD1jQYFMhQSfhVyCFztqA8m5ie` | DexScreener, al detectar (2 par(es) en la consulta 02/10/2026 09:55 UTC) |
| Deployer | `AEGuBv8qZTuBiqSYvDhktpk5F1DHUgvdKTxnLh81HaWm` | RugCheck `creator` |
| Par creado | 02/10/2026 02:33 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 7,1 h / 7,1 h / 7,4 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 09:55 UTC |
| Holders / top-10 | 5.084 / 16,72% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 09:55 UTC |
| Holders efectivos del top-10 | 3,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 09:55 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 09:55 UTC |
| Links | DexScreener: https://dexscreener.com/solana/GEShq9LZ2yyatWVmZvRD1jQYFMhQSfhVyCFztqA8m5ie · Solscan: https://solscan.io/token/6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump · pump.fun: https://pump.fun/coin/6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump · web: https://blackholes.world/ · twitter: https://x.com/blackholes_sol | consulta 02/10/2026 09:55 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 09:55 UTC)
- **Historia:**
  - Par creado el 02/10/2026 02:33 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 09:38 UTC, con el par a 7,1 h de creado: precio $0,0002677, mcap $259.570, liquidez $50.160.
  - Velas de 1 h de GeckoTerminal (8, desde 02/10/2026 02:00 UTC): apertura $0,00006879 · máximo $0,001982 (02/10/2026 06:00 UTC) · mínimo $0,00005712 (02/10/2026 02:00 UTC) · último cierre $0,0003560.
  - En la consulta 02/10/2026 09:55 UTC: precio $0,0003607, liquidez $58.738, FDV $349.730.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 09:38 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0002677 |
| Liquidez | $50.160 |
| MCap | $259.570 |
| Volumen 24 h | $2.918.060 |
| Cambio 24 h | +369% |
| Cambio m5 / h1 | -19,1% / -48,4% |
| Volumen m5 / h1 | $19.559 / $312.591 |
| Trades m5 (compras / ventas) | 75 / 96 |
| Edad del par | 7,1 h |
| Score del feed (WS) | 75 |

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

Desglose reconstruido desde los motivos registrados; suma 87 = score registrado 87 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 75 × 0,3 | +22,5 |
| MCap | ≥ $100K | $259.570 | +15 |
| Volumen 24 h | ≥ $1M | $2.918.060 | +20 |
| Volumen m5 | > $1K (par maduro) | $19.559 | +10 |
| Liquidez | ≥ $50K | $50.160 | +10 |
| Cambio 24 h | ≥ +50% | +369% | +10 |
| **Total** | recortado a 0–100 |  | **87** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T09:38:59+00:00, sin estado previo): **87** · motivos: WS score alto, MCap > $100K, Volumen masivo, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 8 de 7.153 tokens analizados (0,11%) quedan ≥ 56. Con score 87, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 09:38 UTC, hasta 04/10/2026 09:38 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -19,1% · h1 -48,4% · h24 +369% · volumen m5/h1 0,06 · edad del par 7,1 h.
- **Precio de entrada** (alerta): $0,0002677.
- **Consulta 02/10/2026 09:55 UTC:** $0,0003607 (+34,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump_2026-10-02_093859.json` · blob `01a7d480b132431ddccf1a0c5f123a0876244614` · commit `59d7927` (2026-10-02T09:49:54Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-02_093334.json` · blob `33e0ce39e41f5ffcb5d1790b5e8d5d65e30f8746` · commit `59d7927` (2026-10-02T09:49:54Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_093859`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump · registro · 02/10/2026 09:38 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump · HTTP 200 · 02/10/2026 09:55 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump/report · HTTP 200 · 02/10/2026 09:55 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump · HTTP 200 · 02/10/2026 09:55 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/GEShq9LZ2yyatWVmZvRD1jQYFMhQSfhVyCFztqA8m5ie/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 09:55 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump · HTTP 404 · 02/10/2026 09:55 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BLACKHOLESUSDT · HTTP 400 · 02/10/2026 09:55 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BLACKHOLES-USD · HTTP 404 · 02/10/2026 09:55 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $58.738 vs $58.225 → 0,87%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0003607 vs $0,0003560 → 1,30%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump_2026-10-02_093859.json',encoding='utf-8'));d=d.get('6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump',d);p=mock.patch('time.time',return_value=1790933939);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 6qs8xGPpmyHnW7LpySq9iCs36kT7utFBt8mwM1ATpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 09:55 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `1a67d0040147ebfc…`
