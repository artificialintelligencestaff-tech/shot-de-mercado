# ATFS (ATFS) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1720 · liquidez $1.185.346 · mcap $172.034.438 (al detectar)  
Detectado el 08/10/2026 03:06 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 10/10/2026 03:06 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ATFS

Estudio de cómo se adquiere ATFS, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/10/2026 03:08 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/10/2026 03:06 UTC | pumpswap `8dbqnfQ…eE84` | $1.185.346 | 1% | 0,017% | 0,169% | 1,687% | $5.927 | $17.780 |
| consulta 08/10/2026 03:08 UTC | pumpswap `8dbqnfQ…eE84` | $1.185.479 | 1% | 0,017% | 0,169% | 1,687% | $5.927 | $17.782 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump`
5. Configurar el slippage: 1% (liquidez $1.185.479, consulta 08/10/2026 03:08 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump) y el par en DexScreener (https://dexscreener.com/solana/8dbqnfQTHgiFyTt4Y4rZQfGvoUjaYnXtfYhaEyeVeE84); mint authority / freeze authority: revocada / revocada · holders 2.883 · top-10 0,86% (consulta 08/10/2026 03:08 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump
- Par en DexScreener: https://dexscreener.com/solana/8dbqnfQTHgiFyTt4Y4rZQfGvoUjaYnXtfYhaEyeVeE84
- Página del lanzamiento (pump.fun): https://pump.fun/coin/oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.883 · top-10 0,86% (consulta 08/10/2026 03:08 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | ATFS / ATFS | registro de la detección (trending) |
| Mint / contrato | `oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `8dbqnfQTHgiFyTt4Y4rZQfGvoUjaYnXtfYhaEyeVeE84` | DexScreener, al detectar (2 par(es) en la consulta 08/10/2026 03:08 UTC) |
| Deployer | `DqG7UMLckPAXbThmjxpQuVNm8pZrrvDV1jvqwLeLRU6K` | RugCheck `creator` |
| Par creado | 08/10/2026 02:06 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,1 min / 60,1 min / 61,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/10/2026 03:08 UTC |
| Holders / top-10 | 2.883 / 0,86% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/10/2026 03:08 UTC |
| Holders efectivos del top-10 | 5,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/10/2026 03:08 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 08/10/2026 03:08 UTC |
| Links | DexScreener: https://dexscreener.com/solana/8dbqnfQTHgiFyTt4Y4rZQfGvoUjaYnXtfYhaEyeVeE84 · Solscan: https://solscan.io/token/oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump · pump.fun: https://pump.fun/coin/oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump · web / Telegram / X: no publicados en DexScreener | consulta 08/10/2026 03:08 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/10/2026 03:08 UTC)
- **Historia:**
  - Par creado el 08/10/2026 02:06 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/10/2026 03:06 UTC, con el par a 60,1 min de creado: precio $0,1720, mcap $172.034.438, liquidez $1.185.346.
  - Velas de 1 h de GeckoTerminal (2, desde 08/10/2026 02:00 UTC): apertura $0,002845 · máximo $0,1720 (08/10/2026 03:00 UTC) · mínimo $0,00004822 (08/10/2026 02:00 UTC) · último cierre $0,1715.
  - En la consulta 08/10/2026 03:08 UTC: precio $0,1720, liquidez $1.185.479, FDV $172.072.882.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/10/2026 03:06 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1720 |
| Liquidez | $1.185.346 |
| MCap | $172.034.438 |
| Volumen 24 h | $584.342 |
| Cambio 24 h | +356.106% |
| Cambio m5 / h1 | +0,1% / +4,0% |
| Volumen m5 / h1 | $962 / $11.268 |
| Trades m5 (compras / ventas) | 231 / 5 |
| Edad del par | 60,1 min |
| Score del feed (WS) | 98 |

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
| Score del feed | score WS × 0,3 | WS 98 × 0,3 | +29,3 |
| MCap | ≥ $1M | $172.034.438 | +25 |
| Volumen 24 h | ≥ $100K | $584.342 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 98% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,1% · h1 +4,0% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,1 min | +8 |
| Volumen m5 | > $500 (par maduro) | $962 | +5 |
| Liquidez | ≥ $100K | $1.185.346 | +15 |
| Cambio 24 h | ≥ +50% | +356.106% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +356.106% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-08T03:06:52+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 32 de 20.635 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/10/2026 03:06 UTC, hasta 10/10/2026 03:06 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +0,1% · h1 +4,0% · h24 +356.106% · volumen m5/h1 0,09 · edad del par 60,1 min.
- **Precio de entrada** (alerta): $0,1720.
- **Consulta 08/10/2026 03:08 UTC:** $0,1720 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump_2026-10-08_030652.json` · blob `d9892b259fb1b01904e6b598c448169464525e1c` · commit `579d875` (2026-10-08T03:07:06Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-08_020708.json` · blob `4013030b5943af8dfa51153b66be5e9df9b21853` · commit `579d875` (2026-10-08T03:07:06Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-08_030652`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump · registro · 08/10/2026 03:06 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump · HTTP 200 · 08/10/2026 03:08 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump/report · HTTP 200 · 08/10/2026 03:08 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump · HTTP 200 · 08/10/2026 03:08 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/8dbqnfQTHgiFyTt4Y4rZQfGvoUjaYnXtfYhaEyeVeE84/ohlcv/hour?limit=1000 · HTTP 200 · 08/10/2026 03:08 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump · HTTP 404 · 08/10/2026 03:08 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ATFSUSDT · HTTP 400 · 08/10/2026 03:08 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ATFS-USD · HTTP 404 · 08/10/2026 03:08 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.185.479 vs $1.182.322 → 0,27%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1720 vs $0,1715 → 0,28%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump_2026-10-08_030652.json',encoding='utf-8'));d=d.get('oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump',d);p=mock.patch('time.time',return_value=1791428812);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint oGYh6buqSxVAR7VLnNwnBj9Dfjj2bQUmGifhtv2pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/10/2026 03:08 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `9d303323df05d1a2…`
