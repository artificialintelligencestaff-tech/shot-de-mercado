# qOMPUTE (qOMPUTE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,004531 · liquidez $193.653 · mcap $4.503.275 (al detectar)  
Detectado el 10/10/2026 00:17 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 12/10/2026 00:17 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir qOMPUTE

Estudio de cómo se adquiere qOMPUTE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 10/10/2026 00:50 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 10/10/2026 00:17 UTC | pumpswap `7F7Q1oK…azPb` | $193.653 | 5% | 0,103% | 1,033% | 10,328% | $968 | $2.905 |
| consulta 10/10/2026 00:50 UTC | pumpswap `7F7Q1oK…azPb` | $170.374 | 5% | 0,117% | 1,174% | 11,739% | $852 | $2.556 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump`
5. Configurar el slippage: 5% (liquidez $170.374, consulta 10/10/2026 00:50 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump) y el par en DexScreener (https://dexscreener.com/solana/7F7Q1oKtpuyg7oYyHXzAUszcnmKHRi18BxBVx7DHazPb); mint authority / freeze authority: revocada / revocada · holders 6.203 · top-10 4,27% (consulta 10/10/2026 00:50 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump
- Par en DexScreener: https://dexscreener.com/solana/7F7Q1oKtpuyg7oYyHXzAUszcnmKHRi18BxBVx7DHazPb
- Página del lanzamiento (pump.fun): https://pump.fun/coin/BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 6.203 · top-10 4,27% (consulta 10/10/2026 00:50 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | qOMPUTE / qOMPUTE | registro de la detección (trending) |
| Mint / contrato | `BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7F7Q1oKtpuyg7oYyHXzAUszcnmKHRi18BxBVx7DHazPb` | DexScreener, al detectar (2 par(es) en la consulta 10/10/2026 00:50 UTC) |
| Deployer | `E7JzWSx2XVaWFaQRbd9K5Yani9Q3aZfC3AwExU1T4m5G` | RugCheck `creator` |
| Par creado | 09/10/2026 23:13 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 63,6 min / 63,6 min / 96,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 10/10/2026 00:50 UTC |
| Holders / top-10 | 6.203 / 4,27% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 10/10/2026 00:50 UTC |
| Holders efectivos del top-10 | 2,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 10/10/2026 00:50 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 10/10/2026 00:50 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7F7Q1oKtpuyg7oYyHXzAUszcnmKHRi18BxBVx7DHazPb · Solscan: https://solscan.io/token/BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump · pump.fun: https://pump.fun/coin/BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump · web: https://qompute.online · twitter: https://x.com/qOMPUTEx | consulta 10/10/2026 00:50 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 10/10/2026 00:50 UTC)
- **Historia:**
  - Par creado el 09/10/2026 23:13 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 10/10/2026 00:17 UTC, con el par a 63,6 min de creado: precio $0,004531, mcap $4.503.275, liquidez $193.653.
  - Velas de 1 h de GeckoTerminal (2, desde 09/10/2026 23:00 UTC): apertura $0,0001076 · máximo $0,004923 (10/10/2026 00:00 UTC) · mínimo $0,00005428 (09/10/2026 23:00 UTC) · último cierre $0,003579.
  - En la consulta 10/10/2026 00:50 UTC: precio $0,003486, liquidez $170.374, FDV $3.464.388.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 10/10/2026 00:17 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,004531 |
| Liquidez | $193.653 |
| MCap | $4.503.275 |
| Volumen 24 h | $2.142.013 |
| Cambio 24 h | +1.762% |
| Cambio m5 / h1 | +18,7% / +1.343,0% |
| Volumen m5 / h1 | $247.469 / $2.001.095 |
| Trades m5 (compras / ventas) | 1.420 / 749 |
| Edad del par | 63,6 min |
| Score del feed (WS) | 83 |

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
| Score del feed | score WS × 0,3 | WS 83 × 0,3 | +25,0 |
| MCap | ≥ $1M | $4.503.275 | +25 |
| Volumen 24 h | ≥ $1M | $2.142.013 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 65% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +18,7% · h1 +1.343,0% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 63,6 min | +8 |
| Volumen m5 | > $1K (par maduro) | $247.469 | +10 |
| Liquidez | ≥ $100K | $193.653 | +15 |
| Cambio 24 h | ≥ +50% | +1.762% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.762% · liq/mcap 4,3% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-10T00:17:20+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=4.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 42 de 26.066 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 10/10/2026 00:17 UTC, hasta 12/10/2026 00:17 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +18,7% · h1 +1.343,0% · h24 +1.762% · volumen m5/h1 0,12 · edad del par 63,6 min.
- **Precio de entrada** (alerta): $0,004531.
- **Consulta 10/10/2026 00:50 UTC:** $0,003486 (-23,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump_2026-10-10_001720.json` · blob `0f26236024bc102f5f0b5ee7c34d9a89c1610107` · commit `988701f` (2026-10-10T00:43:17Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-10_000950.json` · blob `f991d2f5a1021217574a1e818ddd36b7a07f2ab0` · commit `988701f` (2026-10-10T00:43:17Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-10_001720`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump · registro · 10/10/2026 00:17 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump · HTTP 200 · 10/10/2026 00:50 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump/report · HTTP 200 · 10/10/2026 00:50 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump · HTTP 200 · 10/10/2026 00:50 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7F7Q1oKtpuyg7oYyHXzAUszcnmKHRi18BxBVx7DHazPb/ohlcv/hour?limit=1000 · HTTP 200 · 10/10/2026 00:50 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump · HTTP 404 · 10/10/2026 00:50 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=QOMPUTEUSDT · HTTP 400 · 10/10/2026 00:50 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/QOMPUTE-USD · HTTP 404 · 10/10/2026 00:50 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $170.374 vs $170.071 → 0,18%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003486 vs $0,003579 → 2,59%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump_2026-10-10_001720.json',encoding='utf-8'));d=d.get('BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump',d);p=mock.patch('time.time',return_value=1791591440);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint BQAeeSowpwEx8Km8GcporcbuLKq4a7EQceH3F2qZpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 10/10/2026 00:50 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `5153b44f09f2f766…`
