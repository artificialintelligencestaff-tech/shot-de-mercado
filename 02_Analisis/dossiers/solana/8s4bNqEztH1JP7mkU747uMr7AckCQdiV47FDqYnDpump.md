# Anakin Coin (ANAKIN) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003381 · liquidez $161.348 · mcap $3.366.925 (al detectar)  
Detectado el 02/11/2026 07:07 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 04/11/2026 07:08 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ANAKIN

Estudio de cómo se adquiere ANAKIN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/11/2026 07:08 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/11/2026 07:07 UTC | pumpswap `HcGPz2e…GwbK` | $161.348 | 5% | 0,124% | 1,240% | 12,396% | $807 | $2.420 |
| consulta 02/11/2026 07:08 UTC | pumpswap `HcGPz2e…GwbK` | $161.348 | 5% | 0,124% | 1,240% | 12,396% | $807 | $2.420 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump`
5. Configurar el slippage: 5% (liquidez $161.348, consulta 02/11/2026 07:08 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump) y el par en DexScreener (https://dexscreener.com/solana/HcGPz2eXV8SFcMVQ9fJPBd71bRLJVzUtd2avvv86GwbK); mint authority / freeze authority: revocada / revocada · holders 8.244 · top-10 3,14% (consulta 02/11/2026 07:08 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump
- Par en DexScreener: https://dexscreener.com/solana/HcGPz2eXV8SFcMVQ9fJPBd71bRLJVzUtd2avvv86GwbK
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 8.244 · top-10 3,14% (consulta 02/11/2026 07:08 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Anakin Coin / ANAKIN | registro de la detección (trending) |
| Mint / contrato | `8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HcGPz2eXV8SFcMVQ9fJPBd71bRLJVzUtd2avvv86GwbK` | DexScreener, al detectar (8 par(es) en la consulta 02/11/2026 07:08 UTC) |
| Deployer | `AoEEgeHgLMbANGd2zyRH8wTy2ekvxFNduSTFTxuVydeF` | RugCheck `creator` |
| Par creado | 01/11/2026 22:28 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 8,7 h / 8,7 h / 8,7 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/11/2026 07:08 UTC |
| Holders / top-10 | 8.244 / 3,14% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/11/2026 07:08 UTC |
| Holders efectivos del top-10 | 1,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/11/2026 07:08 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 02/11/2026 07:08 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HcGPz2eXV8SFcMVQ9fJPBd71bRLJVzUtd2avvv86GwbK · Solscan: https://solscan.io/token/8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump · pump.fun: https://pump.fun/coin/8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump · web: https://anakin.meme · twitter: https://x.com/AnakinMemeCoin | consulta 02/11/2026 07:08 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/11/2026 07:08 UTC)
- **Historia:**
  - Par creado el 01/11/2026 22:28 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/11/2026 07:07 UTC, con el par a 8,7 h de creado: precio $0,003381, mcap $3.366.925, liquidez $161.348.
  - Velas de 1 h de GeckoTerminal (10, desde 01/11/2026 22:00 UTC): apertura $0,0003724 · máximo $0,005168 (02/11/2026 01:00 UTC) · mínimo $0,00005097 (01/11/2026 22:00 UTC) · último cierre $0,003427.
  - En la consulta 02/11/2026 07:08 UTC: precio $0,003381, liquidez $161.348, FDV $3.366.925.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/11/2026 07:07 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003381 |
| Liquidez | $161.348 |
| MCap | $3.366.925 |
| Volumen 24 h | $4.809.609 |
| Cambio 24 h | +6.490% |
| Cambio m5 / h1 | +2,0% / -0,7% |
| Volumen m5 / h1 | $6.275 / $120.160 |
| Trades m5 (compras / ventas) | 360 / 221 |
| Edad del par | 8,7 h |
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
| Score del feed | score WS × 0,3 | WS 71 × 0,3 | +21,4 |
| MCap | ≥ $1M | $3.366.925 | +25 |
| Volumen 24 h | ≥ $1M | $4.809.609 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 62% | +25 |
| Momentum | m5 > 0 y h1 > −5% (par maduro) | m5 +2,0% · h1 -0,7% | +10 |
| Volumen m5 | > $1K (par maduro) | $6.275 | +10 |
| Liquidez | ≥ $100K | $161.348 | +15 |
| Cambio 24 h | ≥ +50% | +6.490% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +6.490% · liq/mcap 4,8% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-02T07:07:50+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Momentum corto positivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.8% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 86 de 46.474 tokens analizados (0,19%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/11/2026 07:08 UTC, hasta 04/11/2026 07:08 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +2,0% · h1 -0,7% · h24 +6.490% · volumen m5/h1 0,05 · edad del par 8,7 h.
- **Precio de entrada** (alerta): $0,003381.
- **Consulta 02/11/2026 07:08 UTC:** $0,003381 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump_2026-11-02_070802.json` · blob `a3ae24a57d30e8f5eda8a908a21f330901a48156` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-02_070247.json` · blob `35acd113bdc939cd65b70d69eb2e17da3578237c` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-02_070802`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump · registro · 02/11/2026 07:07 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump · HTTP 200 · 02/11/2026 07:08 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump/report · HTTP 200 · 02/11/2026 07:08 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump · HTTP 200 · 02/11/2026 07:08 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HcGPz2eXV8SFcMVQ9fJPBd71bRLJVzUtd2avvv86GwbK/ohlcv/hour?limit=1000 · HTTP 200 · 02/11/2026 07:08 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump · HTTP 404 · 02/11/2026 07:08 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ANAKINUSDT · HTTP 400 · 02/11/2026 07:08 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ANAKIN-USD · HTTP 404 · 02/11/2026 07:08 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $161.348 vs $161.630 → 0,17%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003381 vs $0,003427 → 1,33%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump_2026-11-02_070802.json',encoding='utf-8'));d=d.get('8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump',d);p=mock.patch('time.time',return_value=1793603270);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/11/2026 07:08 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `ade075006f6bb9d9…`
