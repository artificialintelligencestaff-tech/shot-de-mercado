# Ah Shit, Here We Go Again (HEREWEGO) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001423 · liquidez $103.577 · mcap $1.416.668 (al detectar)  
Detectado el 08/11/2026 20:26 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 10/11/2026 20:26 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HEREWEGO

Estudio de cómo se adquiere HEREWEGO, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/11/2026 20:26 UTC; CoinGecko sin pares de este contrato en esos exchanges).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/11/2026 20:26 UTC | pumpswap `67BwjNj…SziR` | $103.577 | 5% | 0,193% | 1,931% | 19,309% | $518 | $1.554 |
| consulta 08/11/2026 20:26 UTC | pumpswap `67BwjNj…SziR` | $107.804 | 5% | 0,186% | 1,855% | 18,552% | $539 | $1.617 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump`
5. Configurar el slippage: 5% (liquidez $107.804, consulta 08/11/2026 20:26 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump) y el par en DexScreener (https://dexscreener.com/solana/67BwjNjSjbdPP3KPi6GDeevK25QGrprwFTTmQE4wSziR); mint authority / freeze authority: revocada / revocada · holders 9.004 · top-10 12,42% (consulta 08/11/2026 20:26 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump
- Par en DexScreener: https://dexscreener.com/solana/67BwjNjSjbdPP3KPi6GDeevK25QGrprwFTTmQE4wSziR
- Página del lanzamiento (pump.fun): https://pump.fun/coin/483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 9.004 · top-10 12,42% (consulta 08/11/2026 20:26 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Ah Shit, Here We Go Again / HEREWEGO | registro de la detección (trending) |
| Mint / contrato | `483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `67BwjNjSjbdPP3KPi6GDeevK25QGrprwFTTmQE4wSziR` | DexScreener, al detectar (3 par(es) en la consulta 08/11/2026 20:26 UTC) |
| Deployer | `9TJyvArGejxe6swNWfhXx6n5FEBDcNxMTCG83KeJfJPG` | RugCheck `creator` |
| Par creado | 08/11/2026 01:43 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 18,7 h / 18,7 h / 18,7 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/11/2026 20:26 UTC |
| Holders / top-10 | 9.004 / 12,42% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/11/2026 20:26 UTC |
| Holders efectivos del top-10 | 7,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; orca 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/11/2026 20:26 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 08/11/2026 20:26 UTC |
| Links | DexScreener: https://dexscreener.com/solana/67BwjNjSjbdPP3KPi6GDeevK25QGrprwFTTmQE4wSziR · Solscan: https://solscan.io/token/483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump · pump.fun: https://pump.fun/coin/483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump · web: https://ahshitagainsol.vip/ · twitter: https://x.com/AhShitAgainSol | consulta 08/11/2026 20:26 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** CoinGecko: Solana Ecosystem, Meme, Solana Meme, Pump.fun Ecosystem · scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/11/2026 20:26 UTC)
- **Historia:**
  - Par creado el 08/11/2026 01:43 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/11/2026 20:26 UTC, con el par a 18,7 h de creado: precio $0,001423, mcap $1.416.668, liquidez $103.577.
  - Velas de 1 h de GeckoTerminal (20, desde 08/11/2026 01:00 UTC): apertura $0,00006638 · máximo $0,002838 (08/11/2026 17:00 UTC) · mínimo $0,00004496 (08/11/2026 01:00 UTC) · último cierre $0,001430.
  - En la consulta 08/11/2026 20:26 UTC: precio $0,001539, liquidez $107.804, FDV $1.532.424.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/11/2026 20:26 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001423 |
| Liquidez | $103.577 |
| MCap | $1.416.668 |
| Volumen 24 h | $4.699.548 |
| Cambio 24 h | +3.040% |
| Cambio m5 / h1 | +48,3% / +47,6% |
| Volumen m5 / h1 | $25.165 / $187.405 |
| Trades m5 (compras / ventas) | 460 / 98 |
| Edad del par | 18,7 h |
| Score del feed (WS) | 84 |

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
| Score del feed | score WS × 0,3 | WS 84 × 0,3 | +25,3 |
| MCap | ≥ $1M | $1.416.668 | +25 |
| Volumen 24 h | ≥ $1M | $4.699.548 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 82% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +48,3% · h1 +47,6% | +20 |
| Volumen m5 | > $1K (par maduro) | $25.165 | +10 |
| Liquidez | ≥ $100K | $103.577 | +15 |
| Cambio 24 h | ≥ +50% | +3.040% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +3.040% · liq/mcap 7,3% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-08T20:26:17+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=7.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 95 de 46.922 tokens analizados (0,20%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/11/2026 20:26 UTC, hasta 10/11/2026 20:26 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +48,3% · h1 +47,6% · h24 +3.040% · volumen m5/h1 0,13 · edad del par 18,7 h.
- **Precio de entrada** (alerta): $0,001423.
- **Consulta 08/11/2026 20:26 UTC:** $0,001539 (+8,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump_2026-11-08_202627.json` · blob `1aacd86d2a792b7e5270c69c36379b253812bd75` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-08_202112.json` · blob `1cc4de9c270f60fafcaa6549ff32eb51831262ea` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-08_202627`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump · registro · 08/11/2026 20:26 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump · HTTP 200 · 08/11/2026 20:26 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump/report · HTTP 200 · 08/11/2026 20:26 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump · HTTP 200 · 08/11/2026 20:26 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/67BwjNjSjbdPP3KPi6GDeevK25QGrprwFTTmQE4wSziR/ohlcv/hour?limit=1000 · HTTP 200 · 08/11/2026 20:26 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump · HTTP 200 · 08/11/2026 20:26 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HEREWEGOUSDT · HTTP 400 · 08/11/2026 20:26 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HEREWEGO-USD · HTTP 404 · 08/11/2026 20:26 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $107.804 vs $108.457 → 0,60%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001539 vs $0,001430 → 7,06%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump_2026-11-08_202627.json',encoding='utf-8'));d=d.get('483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump',d);p=mock.patch('time.time',return_value=1794169577);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 483nprwoMSoGQgrojSHWiePMbKPre7ZRDy4f8YNSpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/11/2026 20:26 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `6a7d5086d44e41c1…`
