# Ollie (Ollie) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0006160 · liquidez $73.049 · mcap $616.056 (al detectar)  
Detectado el 11/10/2026 00:27 UTC por: young-0.4 · edad 14.2 min · pesos info 58 / estructura 21 / precio 21 · info 12.7 · estructura 18.1 · precio/volumen 12.3 · cobertura 84/100, [info] narrative_wave: ola 'ollie': 7 lanzamientos más en 1 h → +12.7, [estructura] bonding_progress: graduado (pumpswap) → +10.1 (score 43, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 13/10/2026 00:27 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Ollie

Estudio de cómo se adquiere Ollie, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/10/2026 00:48 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 11/10/2026 00:27 UTC | pumpswap `Cj2rYAJ…qJAB` | $73.049 | 5% | 0,274% | 2,738% | 27,379% | $365 | $1.096 |
| consulta 11/10/2026 00:48 UTC | pumpswap `Cj2rYAJ…qJAB` | $54.657 | 5% | 0,366% | 3,659% | 36,592% | $273 | $820 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump`
5. Configurar el slippage: 5% (liquidez $54.657, consulta 11/10/2026 00:48 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump) y el par en DexScreener (https://dexscreener.com/solana/Cj2rYAJiRF7ZikaxzetJ1aeaJyy44UD1BadZjBuEqJAB); mint authority / freeze authority: revocada / revocada · holders 7.195 · top-10 17,90% (consulta 11/10/2026 00:48 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump
- Par en DexScreener: https://dexscreener.com/solana/Cj2rYAJiRF7ZikaxzetJ1aeaJyy44UD1BadZjBuEqJAB
- Página del lanzamiento (pump.fun): https://pump.fun/coin/7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 7.195 · top-10 17,90% (consulta 11/10/2026 00:48 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Ollie / Ollie | registro de la detección (pumpportal_live) |
| Mint / contrato | `7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Cj2rYAJiRF7ZikaxzetJ1aeaJyy44UD1BadZjBuEqJAB` | DexScreener, al detectar (10 par(es) en la consulta 11/10/2026 00:48 UTC) |
| Deployer | `2tbTtVXgYGSaMn36pmBPMhT7LUz5k9pqaKB6QniczQm5` | PumpPortal (evento create), al detectar |
| Par creado | 11/10/2026 00:13 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 14,2 min / 14,2 min / 35,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/10/2026 00:48 UTC |
| Holders / top-10 | 7.195 / 17,90% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/10/2026 00:48 UTC |
| Holders efectivos del top-10 | 3,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; orca 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/10/2026 00:48 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 11/10/2026 00:48 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Cj2rYAJiRF7ZikaxzetJ1aeaJyy44UD1BadZjBuEqJAB · Solscan: https://solscan.io/token/7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump · pump.fun: https://pump.fun/coin/7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump · web / Telegram / X: no publicados en DexScreener | consulta 11/10/2026 00:48 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/10/2026 00:48 UTC)
- **Historia:**
  - Par creado el 11/10/2026 00:13 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 11/10/2026 00:27 UTC, con el par a 14,2 min de creado: precio $0,0006160, mcap $616.056, liquidez $73.049.
  - Velas de 1 h de GeckoTerminal (1, desde 11/10/2026 00:00 UTC): apertura $0,00004472 · máximo $0,0007423 (11/10/2026 00:00 UTC) · mínimo $0,00002127 (11/10/2026 00:00 UTC) · último cierre $0,0003543.
  - En la consulta 11/10/2026 00:48 UTC: precio $0,0003218, liquidez $54.657, FDV $321.818.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 11/10/2026 00:27 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0006160 |
| Liquidez | $73.049 |
| MCap | $616.056 |
| Volumen 24 h | $899.577 |
| Cambio 24 h | +1.287% |
| Cambio m5 / h1 | +50,1% / +1.287,0% |
| Volumen m5 / h1 | $307.980 / $899.577 |
| Trades m5 (compras / ventas) | 1.806 / 1.725 |
| Edad del par | 14,2 min |
| Score del feed (WS) | n/d (feed sin score) |

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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 43; motivos sin regla: young-0.4 · edad 14.2 min · pesos info 58 / estructura 21 / precio 21 · info 12.7 · estructura 18.1 · precio/volumen 12.3 · cobertura 84/100, [info] narrative_wave: ola 'ollie': 7 lanzamientos más en 1 h → +12.7, [estructura] bonding_progress: graduado (pumpswap) → +10.1, [estructura] holders_struct: holders 4790 · top-10 16.5 % → +5.1, [estructura] dev_wallet: creador compró 3.0 % del supply → +2.2, [estructura] holder_to_txn_ratio: holders/txns 4790/10737 = 0.45 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×4.1 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +78% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 2941→4790 (+308.2/min) · top10 21.4%→16.5% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=73048.57, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=29786.27, score 43 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-11T00:27:26+00:00, sin estado previo): **50** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=11.9% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 44 de 28.142 tokens analizados (0,16%) quedan ≥ 56. Con score 50, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 11/10/2026 00:27 UTC, hasta 13/10/2026 00:27 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +50,1% · h1 +1.287,0% · h24 +1.287% · volumen m5/h1 0,34 · edad del par 14,2 min.
- **Precio de entrada** (alerta): $0,0006160.
- **Consulta 11/10/2026 00:48 UTC:** $0,0003218 (-47,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump_2026-10-11_002726.json` · blob `55ae66ad27d8807337ce1e191e1a9548f9403032` · commit `d358e9e` (2026-10-11T00:42:22Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-11_000929.json` · blob `093a5e2c38f92fcb1a91dca5439c6501ec24f903` · commit `d358e9e` (2026-10-11T00:42:22Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-11_002726`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump · registro · 11/10/2026 00:27 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump · HTTP 200 · 11/10/2026 00:48 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump/report · HTTP 200 · 11/10/2026 00:48 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump · HTTP 200 · 11/10/2026 00:48 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Cj2rYAJiRF7ZikaxzetJ1aeaJyy44UD1BadZjBuEqJAB/ohlcv/hour?limit=1000 · HTTP 200 · 11/10/2026 00:48 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump · HTTP 404 · 11/10/2026 00:48 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=OLLIEUSDT · HTTP 400 · 11/10/2026 00:48 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/OLLIE-USD · HTTP 404 · 11/10/2026 00:48 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $54.657 vs $72.349 → 24,45%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0003218 vs $0,0003543 → 9,18%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump_2026-10-11_002726.json',encoding='utf-8'));d=d.get('7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump',d);p=mock.patch('time.time',return_value=1791678446);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 7vm6ReUqmy6uZVb6Tg9QuRykEau8v52RyYR2EUGmpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/10/2026 00:48 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `feb6686cddd1a4d5…`
