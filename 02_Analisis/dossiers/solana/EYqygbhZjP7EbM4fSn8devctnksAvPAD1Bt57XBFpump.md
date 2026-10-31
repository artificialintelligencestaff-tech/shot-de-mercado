# Broke Nigga Baddie (BNB) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0005764 · liquidez $66.682 · mcap $573.623 (al detectar)  
Detectado el 31/10/2026 06:37 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 02/11/2026 06:38 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir BNB

Estudio de cómo se adquiere BNB, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 31/10/2026 06:38 UTC; CoinGecko sin ficha para este contrato). Binance tiene un par BNBUSDT, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza. Coinbase tiene un par BNB-USD, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza.

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 31/10/2026 06:37 UTC | pumpswap `81jgrpT…HWDB` | $66.682 | 5% | 0,300% | 2,999% | 29,993% | $333 | $1.000 |
| consulta 31/10/2026 06:38 UTC | pumpswap `81jgrpT…HWDB` | $66.691 | 5% | 0,300% | 2,999% | 29,989% | $333 | $1.000 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump`
5. Configurar el slippage: 5% (liquidez $66.691, consulta 31/10/2026 06:38 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump) y el par en DexScreener (https://dexscreener.com/solana/81jgrpTMsQWc1rGWXutyYWW27ruiAtehUZwLydcHHWDB); mint authority / freeze authority: revocada / revocada · holders n/d · top-10 n/d (consulta 31/10/2026 06:38 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump
- Par en DexScreener: https://dexscreener.com/solana/81jgrpTMsQWc1rGWXutyYWW27ruiAtehUZwLydcHHWDB
- Página del lanzamiento (pump.fun): https://pump.fun/coin/EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders n/d · top-10 n/d (consulta 31/10/2026 06:38 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Broke Nigga Baddie / BNB | registro de la detección (trending) |
| Mint / contrato | `EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `81jgrpTMsQWc1rGWXutyYWW27ruiAtehUZwLydcHHWDB` | DexScreener, al detectar (5 par(es) en la consulta 31/10/2026 06:38 UTC) |
| Deployer | n/d | n/d (fuente: RugCheck `creator`) |
| Par creado | 30/10/2026 20:50 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 9,8 h / 9,8 h / 9,8 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | GoPlus, consulta 31/10/2026 06:38 UTC |
| Holders / top-10 | n/d / n/d | RugCheck [P: sin consulta] |
| Holders efectivos del top-10 | n/d | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | n/d | RugCheck [P] |
| Etiquetas de RugCheck | n/d | RugCheck [P] |
| Links | DexScreener: https://dexscreener.com/solana/81jgrpTMsQWc1rGWXutyYWW27ruiAtehUZwLydcHHWDB · Solscan: https://solscan.io/token/EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump · pump.fun: https://pump.fun/coin/EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump · web: https://brokeniggabaddie.vip/ · twitter: https://x.com/BrokeNiggaBadd | consulta 31/10/2026 06:38 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (metadata sin consultar [P])
- **Historia:**
  - Par creado el 30/10/2026 20:50 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 31/10/2026 06:37 UTC, con el par a 9,8 h de creado: precio $0,0005764, mcap $573.623, liquidez $66.682.
  - Velas de 1 h de GeckoTerminal (11, desde 30/10/2026 20:00 UTC): apertura $0,0002815 · máximo $0,002029 (31/10/2026 02:00 UTC) · mínimo $0,00005366 (30/10/2026 20:00 UTC) · último cierre $0,0005875.
  - En la consulta 31/10/2026 06:38 UTC: precio $0,0005765, liquidez $66.691, FDV $573.682.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 31/10/2026 06:37 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0005764 |
| Liquidez | $66.682 |
| MCap | $573.623 |
| Volumen 24 h | $3.317.862 |
| Cambio 24 h | +966% |
| Cambio m5 / h1 | +16,7% / -16,7% |
| Volumen m5 / h1 | $23.843 / $281.057 |
| Trades m5 (compras / ventas) | 367 / 173 |
| Edad del par | 9,8 h |
| Score del feed (WS) | 74 |

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
| Score del feed | score WS × 0,3 | WS 74 × 0,3 | +22,1 |
| MCap | ≥ $100K | $573.623 | +15 |
| Volumen 24 h | ≥ $1M | $3.317.862 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 68% | +25 |
| Volumen m5 | > $1K (par maduro) | $23.843 | +10 |
| Liquidez | ≥ $50K | $66.682 | +10 |
| Cambio 24 h | ≥ +50% | +966% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +966% · liq/mcap 11,6% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-31T06:37:57+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=11.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 84 de 46.348 tokens analizados (0,18%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 31/10/2026 06:38 UTC, hasta 02/11/2026 06:38 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +16,7% · h1 -16,7% · h24 +966% · volumen m5/h1 0,08 · edad del par 9,8 h.
- **Precio de entrada** (alerta): $0,0005764.
- **Consulta 31/10/2026 06:38 UTC:** $0,0005765 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump_2026-10-31_063808.json` · blob `fe4be22e1fd85690d584664c83e544dce6e19df7` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-31_063251.json` · blob `3fbf22556406888d7f6c2f6a904bb6d4ed5cc873` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-31_063808`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump · registro · 31/10/2026 06:37 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump · HTTP 200 · 31/10/2026 06:38 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump/report · HTTP 400 · 31/10/2026 06:38 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump · HTTP 200 · 31/10/2026 06:38 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/81jgrpTMsQWc1rGWXutyYWW27ruiAtehUZwLydcHHWDB/ohlcv/hour?limit=1000 · HTTP 200 · 31/10/2026 06:38 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump · HTTP 404 · 31/10/2026 06:38 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BNBUSDT · HTTP 200 · 31/10/2026 06:38 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BNB-USD · HTTP 200 · 31/10/2026 06:38 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0005765 vs $0,0005875 → 1,87%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump_2026-10-31_063808.json',encoding='utf-8'));d=d.get('EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump',d);p=mock.patch('time.time',return_value=1793428677);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint EYqygbhZjP7EbM4fSn8devctnksAvPAD1Bt57XBFpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 31/10/2026 06:38 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `a00ad2a772b55dcb…`
