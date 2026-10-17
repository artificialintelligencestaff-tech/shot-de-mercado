# The French Avengers (Avengers) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00003117 · liquidez $13.878 · mcap $31.105 (al detectar)  
Detectado el 17/10/2026 15:57 UTC por: young-0.4 · edad 10.5 min · pesos info 60 / estructura 20 / precio 20 · info 20.2 · estructura 12.6 · precio/volumen 8.4 · cobertura 93/100, [info] narrative_wave: ola 'french': 22 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 19/10/2026 15:57 UTC (< 48 h) · vigente: quedan 47,1 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Avengers

Estudio de cómo se adquiere Avengers, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 17/10/2026 16:50 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 17/10/2026 15:57 UTC | pumpswap `x7m4HZj…6WAE` | $13.878 | 10% | 1,441% | 14,411% | 144,110% | $69 | $208 |
| consulta 17/10/2026 16:50 UTC | pumpswap `x7m4HZj…6WAE` | $3.889 | 10% | 5,142% | 51,422% | 514,218% | $19 | $58 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump`
5. Configurar el slippage: 10% (liquidez $3.889, consulta 17/10/2026 16:50 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump) y el par en DexScreener (https://dexscreener.com/solana/x7m4HZj2mWHF3mRbug54AQ4Zn8SH8G9w3VYfuqG6WAE); mint authority / freeze authority: revocada / revocada · holders 1.645 · top-10 85,12% (consulta 17/10/2026 16:50 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump
- Par en DexScreener: https://dexscreener.com/solana/x7m4HZj2mWHF3mRbug54AQ4Zn8SH8G9w3VYfuqG6WAE
- Página del lanzamiento (pump.fun): https://pump.fun/coin/ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.645 · top-10 85,12% (consulta 17/10/2026 16:50 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | The French Avengers / Avengers | registro de la detección (pumpportal_live) |
| Mint / contrato | `ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `x7m4HZj2mWHF3mRbug54AQ4Zn8SH8G9w3VYfuqG6WAE` | DexScreener, al detectar (2 par(es) en la consulta 17/10/2026 16:50 UTC) |
| Deployer | `5MTjkAZMe1ur64ADTgnaYFN1ByTapu2RqcKYUdQNaE2E` | PumpPortal (evento create), al detectar |
| Par creado | 17/10/2026 15:46 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,5 min / 10,5 min / 64,1 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 17/10/2026 16:50 UTC |
| Holders / top-10 | 1.645 / 85,12% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 17/10/2026 16:50 UTC |
| Holders efectivos del top-10 | 1,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 17/10/2026 16:50 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 17/10/2026 16:50 UTC |
| Links | DexScreener: https://dexscreener.com/solana/x7m4HZj2mWHF3mRbug54AQ4Zn8SH8G9w3VYfuqG6WAE · Solscan: https://solscan.io/token/ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump · pump.fun: https://pump.fun/coin/ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump · web / Telegram / X: no publicados en DexScreener | consulta 17/10/2026 16:50 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 17/10/2026 16:50 UTC)
- **Historia:**
  - Par creado el 17/10/2026 15:46 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 17/10/2026 15:57 UTC, con el par a 10,5 min de creado: precio $0,00003117, mcap $31.105, liquidez $13.878.
  - Velas de 1 h de GeckoTerminal (2, desde 17/10/2026 15:00 UTC): apertura $0,00004337 · máximo $0,00009631 (17/10/2026 15:00 UTC) · mínimo $0,000003885 (17/10/2026 16:00 UTC) · último cierre $0,000004227.
  - En la consulta 17/10/2026 16:50 UTC: precio $0,000004304, liquidez $3.889, FDV $4.145.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 17/10/2026 15:57 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00003117 |
| Liquidez | $13.878 |
| MCap | $31.105 |
| Volumen 24 h | $250.979 |
| Cambio 24 h | -28% |
| Cambio m5 / h1 | -53,5% / -28,2% |
| Volumen m5 / h1 | $109.498 / $250.979 |
| Trades m5 (compras / ventas) | 1.420 / 1.329 |
| Edad del par | 10,5 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 10.5 min · pesos info 60 / estructura 20 / precio 20 · info 20.2 · estructura 12.6 · precio/volumen 8.4 · cobertura 93/100, [info] narrative_wave: ola 'french': 22 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1570 · top-10 35.7 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1570/6366 = 0.25 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×5.2 la tasa horaria (s 1.00), [precio/volumen] holder_accumulation: holders 675→1570 (+149.2/min) · top10 40.4%→35.7% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=13878.3, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-17T15:57:04+00:00, sin estado previo): **15** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 64 de 38.586 tokens analizados (0,17%) quedan ≥ 56. Con score 15, este activo queda en el percentil 97,2 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 17/10/2026 15:57 UTC, hasta 19/10/2026 15:57 UTC · vigente: quedan 47,1 h.
- **Aceleración al detectar:** cambio m5 -53,5% · h1 -28,2% · h24 -28% · volumen m5/h1 0,44 · edad del par 10,5 min.
- **Precio de entrada** (alerta): $0,00003117.
- **Consulta 17/10/2026 16:50 UTC:** $0,000004304 (-86,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump_2026-10-17_155704.json` · blob `9f8a846058c02111cfdf7bec420d97f607c2a848` · commit `34c9424` (2026-10-17T16:43:35Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-17_154247.json` · blob `492975649012ff2ab4f7ec1f66dcdf9c50822f72` · commit `34c9424` (2026-10-17T16:43:35Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-17_155704`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump · registro · 17/10/2026 15:57 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump · HTTP 200 · 17/10/2026 16:50 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump/report · HTTP 200 · 17/10/2026 16:50 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump · HTTP 200 · 17/10/2026 16:50 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/x7m4HZj2mWHF3mRbug54AQ4Zn8SH8G9w3VYfuqG6WAE/ohlcv/hour?limit=1000 · HTTP 200 · 17/10/2026 16:50 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump · HTTP 404 · 17/10/2026 16:50 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AVENGERSUSDT · HTTP 400 · 17/10/2026 16:50 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AVENGERS-USD · HTTP 404 · 17/10/2026 16:50 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.889 vs $3.889 → 0,00%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000004304 vs $0,000004227 → 1,78%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump_2026-10-17_155704.json',encoding='utf-8'));d=d.get('ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump',d);p=mock.patch('time.time',return_value=1792252624);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint ByCsUXz2aGsbiJDfW53X7YoRNJAsGhxKUX4jiL7Bpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 17/10/2026 16:50 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `1e3f8eb1f695f7df…`
