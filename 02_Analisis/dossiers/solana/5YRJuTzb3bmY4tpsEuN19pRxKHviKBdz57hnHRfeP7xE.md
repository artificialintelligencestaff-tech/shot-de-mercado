# IShowSpeed (Speed) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001009 · liquidez $90.198 · mcap $1.009.676 (al detectar)  
Detectado el 02/10/2026 02:42 UTC por: MCap > $1M, Volumen decente, Liquidez decente (score 58, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 04/10/2026 02:42 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Speed

Estudio de cómo se adquiere Speed, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 02:54 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 02:42 UTC | pumpswap `ALfnFvt…p95x` | $90.198 | 5% | 0,222% | 2,217% | 22,174% | $451 | $1.353 |
| consulta 02/10/2026 02:54 UTC | pumpswap `ALfnFvt…p95x` | $2.164 | 10% | 9,240% | 92,402% | 924,018% | $11 | $32 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE`
5. Configurar el slippage: 10% (liquidez $2.164, consulta 02/10/2026 02:54 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE) y el par en DexScreener (https://dexscreener.com/solana/ALfnFvthn741Xk6oSqT28kjzREkpThDERPtEsP7Gp95x); mint authority / freeze authority: revocada / revocada · holders 69 · top-10 100,00% (consulta 02/10/2026 02:54 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE
- Par en DexScreener: https://dexscreener.com/solana/ALfnFvthn741Xk6oSqT28kjzREkpThDERPtEsP7Gp95x
- Página del lanzamiento (pump.fun): https://pump.fun/coin/5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 69 · top-10 100,00% (consulta 02/10/2026 02:54 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | IShowSpeed / Speed | registro de la detección (pumpportal_live) |
| Mint / contrato | `5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `ALfnFvthn741Xk6oSqT28kjzREkpThDERPtEsP7Gp95x` | DexScreener, al detectar (2 par(es) en la consulta 02/10/2026 02:54 UTC) |
| Deployer | `31eb9r8fUka72faWS26tH8pb6pd4nAvsz898pybL7XDL` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 02:18 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 24,1 min / 24,1 min / 36,3 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 02:54 UTC |
| Holders / top-10 | 69 / 100,00% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 02:54 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 02:54 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 02:54 UTC |
| Links | DexScreener: https://dexscreener.com/solana/ALfnFvthn741Xk6oSqT28kjzREkpThDERPtEsP7Gp95x · Solscan: https://solscan.io/token/5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE · pump.fun: https://pump.fun/coin/5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE · web / Telegram / X: no publicados en DexScreener | consulta 02/10/2026 02:54 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 02:54 UTC)
- **Historia:**
  - Par creado el 02/10/2026 02:18 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 02:42 UTC, con el par a 24,1 min de creado: precio $0,001009, mcap $1.009.676, liquidez $90.198.
  - Velas de 1 h de GeckoTerminal (1, desde 02/10/2026 02:00 UTC): apertura $0,0001193 · máximo $0,001141 (02/10/2026 02:00 UTC) · mínimo $0,000002135 (02/10/2026 02:00 UTC) · último cierre $0,000002147.
  - En la consulta 02/10/2026 02:54 UTC: precio $0,000002141, liquidez $2.164, FDV $2.142.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 02:42 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001009 |
| Liquidez | $90.198 |
| MCap | $1.009.676 |
| Volumen 24 h | $64.060 |
| Cambio 24 h | +1.926% |
| Cambio m5 / h1 | +25,8% / +1.926,0% |
| Volumen m5 / h1 | $12.898 / $64.060 |
| Trades m5 (compras / ventas) | 1.923 / 1.412 |
| Edad del par | 24,1 min |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 0/1 (0,0%, IC90 0,0%–73,0%) · secundaria 0/0 resueltas (shadow_monitor.json).

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

Desglose no reproducible desde los motivos registrados (suma 55 vs score 58; motivos sin regla: Anticipación (lib_early_signals early-0.2): +3 — volume_acceleration: vol 5 min ×2.4 la tasa horaria → +1.1; liquidity_inflow: liquidez +30% en 8 min → +1.97): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T02:42:25+00:00, sin estado previo): **55** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen decente, Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=8.9% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 6 de 6.691 tokens analizados (0,09%) quedan ≥ 56. Con score 55, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 02:42 UTC, hasta 04/10/2026 02:42 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +25,8% · h1 +1.926,0% · h24 +1.926% · volumen m5/h1 0,20 · edad del par 24,1 min.
- **Precio de entrada** (alerta): $0,001009.
- **Consulta 02/10/2026 02:54 UTC:** $0,000002141 (-99,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE_2026-10-02_024225.json` · blob `6cfb010917dc686e1329dedaf71e057011044024` · commit `5f9f01e` (2026-10-02T02:47:51Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_024225`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE · registro · 02/10/2026 02:42 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE · HTTP 200 · 02/10/2026 02:54 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE/report · HTTP 200 · 02/10/2026 02:54 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE · HTTP 200 · 02/10/2026 02:54 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/ALfnFvthn741Xk6oSqT28kjzREkpThDERPtEsP7Gp95x/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 02:54 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE · HTTP 404 · 02/10/2026 02:54 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SPEEDUSDT · HTTP 400 · 02/10/2026 02:54 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SPEED-USD · HTTP 404 · 02/10/2026 02:54 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.164 vs $2.170 → 0,26%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002141 vs $0,000002147 → 0,27%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE_2026-10-02_024225.json',encoding='utf-8'));d=d.get('5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE',d);p=mock.patch('time.time',return_value=1790908945);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 5YRJuTzb3bmY4tpsEuN19pRxKHviKBdz57hnHRfeP7xE --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 02:54 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `92beab20bd271211…`
