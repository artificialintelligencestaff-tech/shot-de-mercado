# anti inu (ai) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00006482 · liquidez $20.702 · mcap $64.735 (al detectar)  
Detectado el 11/10/2026 15:06 UTC por: young-0.4 · edad 10.2 min · pesos info 60 / estructura 20 / precio 20 · info 18.0 · estructura 14.6 · precio/volumen 10.4 · cobertura 83/100, [info] narrative_wave: ola 'anti': 10 lanzamientos más en 1 h → +15.0, [info] dex_profile: perfil pago en DexScreener → +3.0 (score 43, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 13/10/2026 15:06 UTC (< 48 h) · vigente: quedan 47,2 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ai

Estudio de cómo se adquiere ai, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/10/2026 15:56 UTC; CoinGecko sin ficha para este contrato). Binance tiene un par AIUSDT, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza. Coinbase tiene un par AI-USD, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza.

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 11/10/2026 15:06 UTC | pumpswap `76jfVJv…6DaM` | $20.702 | 10% | 0,966% | 9,661% | 96,607% | $104 | $311 |
| consulta 11/10/2026 15:56 UTC | pumpswap `76jfVJv…6DaM` | $4.827 | 10% | 4,143% | 41,433% | 414,333% | $24 | $72 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump`
5. Configurar el slippage: 10% (liquidez $4.827, consulta 11/10/2026 15:56 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump) y el par en DexScreener (https://dexscreener.com/solana/76jfVJvQWerZmmuyvJegJ2EE27dHGpSqZa3CZuTP6DaM); mint authority / freeze authority: revocada / revocada · holders 2.413 · top-10 79,22% (consulta 11/10/2026 15:56 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump
- Par en DexScreener: https://dexscreener.com/solana/76jfVJvQWerZmmuyvJegJ2EE27dHGpSqZa3CZuTP6DaM
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.413 · top-10 79,22% (consulta 11/10/2026 15:56 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | anti inu / ai | registro de la detección (pumpportal_live) |
| Mint / contrato | `8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `76jfVJvQWerZmmuyvJegJ2EE27dHGpSqZa3CZuTP6DaM` | DexScreener, al detectar (3 par(es) en la consulta 11/10/2026 15:56 UTC) |
| Deployer | `HBWhLRREycDwM44Vw3LvNfV6uquqNEbyihUmV7J65EpZ` | PumpPortal (evento create), al detectar |
| Par creado | 11/10/2026 14:56 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,2 min / 10,2 min / 60,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/10/2026 15:56 UTC |
| Holders / top-10 | 2.413 / 79,22% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/10/2026 15:56 UTC |
| Holders efectivos del top-10 | 1,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/10/2026 15:56 UTC |
| Etiquetas de RugCheck | «Copycat token», «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 11/10/2026 15:56 UTC |
| Links | DexScreener: https://dexscreener.com/solana/76jfVJvQWerZmmuyvJegJ2EE27dHGpSqZa3CZuTP6DaM · Solscan: https://solscan.io/token/8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump · pump.fun: https://pump.fun/coin/8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump · web: https://x.com/i/communities/1943899913760518593 · twitter: https://x.com/nicoscalls/status/2109295897129496728?s=20 | consulta 11/10/2026 15:56 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/10/2026 15:56 UTC)
- **Historia:**
  - Par creado el 11/10/2026 14:56 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 11/10/2026 15:06 UTC, con el par a 10,2 min de creado: precio $0,00006482, mcap $64.735, liquidez $20.702.
  - Velas de 1 h de GeckoTerminal (2, desde 11/10/2026 14:00 UTC): apertura $0,00004340 · máximo $0,0001230 (11/10/2026 15:00 UTC) · mínimo $0,000005416 (11/10/2026 15:00 UTC) · último cierre $0,000005416.
  - En la consulta 11/10/2026 15:56 UTC: precio $0,000005609, liquidez $4.827, FDV $5.240.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 11/10/2026 15:06 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00006482 |
| Liquidez | $20.702 |
| MCap | $64.735 |
| Volumen 24 h | $85.392 |
| Cambio 24 h | +44% |
| Cambio m5 / h1 | +62,3% / +43,6% |
| Volumen m5 / h1 | $22.063 / $85.392 |
| Trades m5 (compras / ventas) | 360 / 251 |
| Edad del par | 10,2 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 43; motivos sin regla: young-0.4 · edad 10.2 min · pesos info 60 / estructura 20 / precio 20 · info 18.0 · estructura 14.6 · precio/volumen 10.4 · cobertura 83/100, [info] narrative_wave: ola 'anti': 10 lanzamientos más en 1 h → +15.0, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1510 · top-10 36.9 % → +2.4, [estructura] dev_wallet: creador compró 4.0 % del supply → +1.8, [estructura] holder_to_txn_ratio: holders/txns 1510/2064 = 0.73 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×3.1 la tasa horaria (s 0.64), [precio/volumen] buy_pressure_shift: compras 59% en 5 min vs 56% en 1 h (s 0.16), [precio/volumen] liquidity_inflow: liquidez +122% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1135→1510 (+62.5/min) · top10 47.3%→36.9% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=20702.4, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 43 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-11T15:06:20+00:00, sin estado previo): **30** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen decente, Liquidez mínima, Subida 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 49 de 29.337 tokens analizados (0,17%) quedan ≥ 56. Con score 30, este activo queda en el percentil 97,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 11/10/2026 15:06 UTC, hasta 13/10/2026 15:06 UTC · vigente: quedan 47,2 h.
- **Aceleración al detectar:** cambio m5 +62,3% · h1 +43,6% · h24 +44% · volumen m5/h1 0,26 · edad del par 10,2 min.
- **Precio de entrada** (alerta): $0,00006482.
- **Consulta 11/10/2026 15:56 UTC:** $0,000005609 (-91,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump_2026-10-11_150620.json` · blob `759e1c503396c77de32e948136f0d78031cb2de2` · commit `e318d8b` (2026-10-11T15:49:16Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-11_145052.json` · blob `ed7dab9ed8af260a61db76c2d83db9a927c82fbd` · commit `e318d8b` (2026-10-11T15:49:16Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-11_150620`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump · registro · 11/10/2026 15:06 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump · HTTP 200 · 11/10/2026 15:56 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump/report · HTTP 200 · 11/10/2026 15:56 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump · HTTP 200 · 11/10/2026 15:56 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/76jfVJvQWerZmmuyvJegJ2EE27dHGpSqZa3CZuTP6DaM/ohlcv/hour?limit=1000 · HTTP 200 · 11/10/2026 15:56 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump · HTTP 404 · 11/10/2026 15:56 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AIUSDT · HTTP 200 · 11/10/2026 15:56 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AI-USD · HTTP 200 · 11/10/2026 15:56 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $4.827 vs $4.947 → 2,43%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000005609 vs $0,000005416 → 3,44%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump_2026-10-11_150620.json',encoding='utf-8'));d=d.get('8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump',d);p=mock.patch('time.time',return_value=1791731180);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8oDatNBDRsQPjeNKELDT3QAnt84Go6RevnUDc2Sepump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/10/2026 15:56 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `1bdf473721b8b4e3…`
