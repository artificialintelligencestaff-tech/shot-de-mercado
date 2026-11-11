# nihao cat (NIHAO) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003266 · liquidez $143.878 · mcap $3.249.187 (al detectar)  
Detectado el 11/11/2026 00:48 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 94, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 13/11/2026 00:48 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir NIHAO

Estudio de cómo se adquiere NIHAO, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/11/2026 00:48 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 11/11/2026 00:48 UTC | pumpswap `4rsLuj8…JbgN` | $143.878 | 5% | 0,139% | 1,390% | 13,901% | $719 | $2.158 |
| consulta 11/11/2026 00:48 UTC | pumpswap `4rsLuj8…JbgN` | $143.878 | 5% | 0,139% | 1,390% | 13,901% | $719 | $2.158 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump`
5. Configurar el slippage: 5% (liquidez $143.878, consulta 11/11/2026 00:48 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump) y el par en DexScreener (https://dexscreener.com/solana/4rsLuj8sBFFMwM4AK6p4R5RbZ7y2m9CGrefxVb29JbgN); mint authority / freeze authority: revocada / revocada · holders 2.523 · top-10 8,04% (consulta 11/11/2026 00:48 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump
- Par en DexScreener: https://dexscreener.com/solana/4rsLuj8sBFFMwM4AK6p4R5RbZ7y2m9CGrefxVb29JbgN
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.523 · top-10 8,04% (consulta 11/11/2026 00:48 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | nihao cat / NIHAO | registro de la detección (trending) |
| Mint / contrato | `8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `4rsLuj8sBFFMwM4AK6p4R5RbZ7y2m9CGrefxVb29JbgN` | DexScreener, al detectar (3 par(es) en la consulta 11/11/2026 00:48 UTC) |
| Deployer | `FU4TY2ngXtNxgJswspp893H2DAAL7JUvaytoWqtWsyCA` | RugCheck `creator` |
| Par creado | 10/11/2026 23:59 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 48,8 min / 48,9 min / 49,3 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/11/2026 00:48 UTC |
| Holders / top-10 | 2.523 / 8,04% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/11/2026 00:48 UTC |
| Holders efectivos del top-10 | 7,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/11/2026 00:48 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 11/11/2026 00:48 UTC |
| Links | DexScreener: https://dexscreener.com/solana/4rsLuj8sBFFMwM4AK6p4R5RbZ7y2m9CGrefxVb29JbgN · Solscan: https://solscan.io/token/8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump · pump.fun: https://pump.fun/coin/8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump · twitter: https://x.com/nihaocatx | consulta 11/11/2026 00:48 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/11/2026 00:48 UTC)
- **Historia:**
  - Par creado el 10/11/2026 23:59 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 11/11/2026 00:48 UTC, con el par a 48,8 min de creado: precio $0,003266, mcap $3.249.187, liquidez $143.878.
  - Velas de 1 h de GeckoTerminal (2, desde 10/11/2026 23:00 UTC): apertura $0,00007625 · máximo $0,003851 (11/11/2026 00:00 UTC) · mínimo $0,00004556 (10/11/2026 23:00 UTC) · último cierre $0,003237.
  - En la consulta 11/11/2026 00:48 UTC: precio $0,003266, liquidez $143.878, FDV $3.249.187.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 11/11/2026 00:48 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003266 |
| Liquidez | $143.878 |
| MCap | $3.249.187 |
| Volumen 24 h | $2.050.728 |
| Cambio 24 h | +7.024% |
| Cambio m5 / h1 | +3,5% / +7.024,0% |
| Volumen m5 / h1 | $19.323 / $2.050.728 |
| Trades m5 (compras / ventas) | 710 / 604 |
| Edad del par | 48,8 min |
| Score del feed (WS) | 81 |

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

Desglose reconstruido desde los motivos registrados; suma 94 = score registrado 94 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 81 × 0,3 | +24,3 |
| Gate de edad v7.2.1 | edad < 60 min o desconocida: sin bonos temporales | edad 48,8 min | +0 |
| MCap | ≥ $1M | $3.249.187 | +25 |
| Volumen 24 h | ≥ $1M | $2.050.728 | +20 |
| Liquidez | ≥ $100K | $143.878 | +15 |
| Cambio 24 h | ≥ +50% | +7.024% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +7.024% · liq/mcap 4,4% | +0 |
| **Total** | recortado a 0–100 |  | **94** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-11T00:48:01+00:00, sin estado previo): **94** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), WS score muy alto, MCap > $1M, Volumen masivo, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.4% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 96 de 47.025 tokens analizados (0,20%) quedan ≥ 56. Con score 94, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 11/11/2026 00:48 UTC, hasta 13/11/2026 00:48 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +3,5% · h1 +7.024,0% · h24 +7.024% · volumen m5/h1 0,01 · edad del par 48,8 min.
- **Precio de entrada** (alerta): $0,003266.
- **Consulta 11/11/2026 00:48 UTC:** $0,003266 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump_2026-11-11_004810.json` · blob `2c2f3cfa82192bedf9a2e904a37a4008d696eef8` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-11_004255.json` · blob `60c56a126673eb54945dc8b4abb8310706ea5f5b` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-11_004810`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump · registro · 11/11/2026 00:48 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump · HTTP 200 · 11/11/2026 00:48 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump/report · HTTP 200 · 11/11/2026 00:48 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump · HTTP 200 · 11/11/2026 00:48 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/4rsLuj8sBFFMwM4AK6p4R5RbZ7y2m9CGrefxVb29JbgN/ohlcv/hour?limit=1000 · HTTP 200 · 11/11/2026 00:48 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump · HTTP 404 · 11/11/2026 00:48 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=NIHAOUSDT · HTTP 400 · 11/11/2026 00:48 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/NIHAO-USD · HTTP 404 · 11/11/2026 00:48 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $143.878 vs $138.762 → 3,56%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003266 vs $0,003237 → 0,89%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump_2026-11-11_004810.json',encoding='utf-8'));d=d.get('8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump',d);p=mock.patch('time.time',return_value=1794358081);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/11/2026 00:48 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `116803bf64b47663…`
