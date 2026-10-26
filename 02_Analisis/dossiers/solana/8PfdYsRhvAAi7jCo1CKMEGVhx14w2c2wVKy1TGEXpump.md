# Onchain Intelligence (ORYN) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00006478 · liquidez $19.856 · mcap $64.782 (al detectar)  
Detectado el 26/10/2026 14:14 UTC por: young-0.4 · edad 10.0 min · pesos info 60 / estructura 20 / precio 20 · info 16.0 · estructura 17.0 · precio/volumen 7.8 · cobertura 93/100, [info] narrative_wave: ola 'intelligence': 3 lanzamientos más en 1 h → +5.6, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 160 caracteres → +7.3 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 28/10/2026 14:14 UTC (< 48 h) · vigente: quedan 46,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ORYN

Estudio de cómo se adquiere ORYN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 26/10/2026 15:20 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 26/10/2026 14:14 UTC | pumpswap `HHw7sq6…X6qN` | $19.856 | 10% | 1,007% | 10,072% | 100,724% | $99 | $298 |
| consulta 26/10/2026 15:20 UTC | pumpswap `HHw7sq6…X6qN` | $2.420 | 10% | 8,266% | 82,657% | 826,573% | $12 | $36 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump`
5. Configurar el slippage: 10% (liquidez $2.420, consulta 26/10/2026 15:20 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump) y el par en DexScreener (https://dexscreener.com/solana/HHw7sq6ZvDp9fwU2o3SEVmqKgrMh7wzDqSVHbfdQX6qN); mint authority / freeze authority: revocada / revocada · holders 700 · top-10 97,43% (consulta 26/10/2026 15:20 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump
- Par en DexScreener: https://dexscreener.com/solana/HHw7sq6ZvDp9fwU2o3SEVmqKgrMh7wzDqSVHbfdQX6qN
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 700 · top-10 97,43% (consulta 26/10/2026 15:20 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Onchain Intelligence / ORYN | registro de la detección (pumpportal_live) |
| Mint / contrato | `8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HHw7sq6ZvDp9fwU2o3SEVmqKgrMh7wzDqSVHbfdQX6qN` | DexScreener, al detectar (2 par(es) en la consulta 26/10/2026 15:20 UTC) |
| Deployer | `CExU5tHqCka69UCSLG1bsgP1v1FhgguYBSz3SMgMvrha` | PumpPortal (evento create), al detectar |
| Par creado | 26/10/2026 14:04 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,0 min / 10,0 min / 76,3 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 26/10/2026 15:20 UTC |
| Holders / top-10 | 700 / 97,43% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 26/10/2026 15:20 UTC |
| Holders efectivos del top-10 | 1,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 26/10/2026 15:20 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 26/10/2026 15:20 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HHw7sq6ZvDp9fwU2o3SEVmqKgrMh7wzDqSVHbfdQX6qN · Solscan: https://solscan.io/token/8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump · pump.fun: https://pump.fun/coin/8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump · web: https://orynagent.fun/ · twitter: https://x.com/orynagent | consulta 26/10/2026 15:20 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 26/10/2026 15:20 UTC)
- **Historia:**
  - Par creado el 26/10/2026 14:04 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 26/10/2026 14:14 UTC, con el par a 10,0 min de creado: precio $0,00006478, mcap $64.782, liquidez $19.856.
  - Velas de 1 h de GeckoTerminal (2, desde 26/10/2026 14:00 UTC): apertura $0,00004302 · máximo $0,0001020 (26/10/2026 14:00 UTC) · mínimo $0,000002220 (26/10/2026 14:00 UTC) · último cierre $0,000002366.
  - En la consulta 26/10/2026 15:20 UTC: precio $0,000002365, liquidez $2.420, FDV $2.256.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 26/10/2026 14:14 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00006478 |
| Liquidez | $19.856 |
| MCap | $64.782 |
| Volumen 24 h | $105.517 |
| Cambio 24 h | +55% |
| Cambio m5 / h1 | +55,3% / +54,7% |
| Volumen m5 / h1 | $43.627 / $105.517 |
| Trades m5 (compras / ventas) | 1.454 / 642 |
| Edad del par | 10,0 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 10.0 min · pesos info 60 / estructura 20 / precio 20 · info 16.0 · estructura 17.0 · precio/volumen 7.8 · cobertura 93/100, [info] narrative_wave: ola 'intelligence': 3 lanzamientos más en 1 h → +5.6, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 160 caracteres → +7.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 470 · top-10 28.9 % → +4.8, [estructura] dev_wallet: creador compró 1.8 % del supply → +2.4, [estructura] holder_to_txn_ratio: holders/txns 470/5117 = 0.09 → +0.1, [precio/volumen] volume_acceleration: vol 5 min ×5.0 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 69% en 5 min vs 69% en 1 h (s 0.02), [precio/volumen] liquidity_inflow: liquidez +24% en 8 min (s 0.81), [flag, no suma] tradable=True, liquidity_usd=19856.19, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-26T14:14:30+00:00, sin estado previo): **35** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez baja, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 78 de 46.003 tokens analizados (0,17%) quedan ≥ 56. Con score 35, este activo queda en el percentil 98,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 26/10/2026 14:14 UTC, hasta 28/10/2026 14:14 UTC · vigente: quedan 46,9 h.
- **Aceleración al detectar:** cambio m5 +55,3% · h1 +54,7% · h24 +55% · volumen m5/h1 0,41 · edad del par 10,0 min.
- **Precio de entrada** (alerta): $0,00006478.
- **Consulta 26/10/2026 15:20 UTC:** $0,000002365 (-96,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump_2026-10-26_141430.json` · blob `2a6a3c769efaf1cd269b4086e8399b9081789007` · commit `50b47d3` (2026-10-26T15:08:24Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-26_141430`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump · registro · 26/10/2026 14:14 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump · HTTP 200 · 26/10/2026 15:20 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump/report · HTTP 200 · 26/10/2026 15:20 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump · HTTP 200 · 26/10/2026 15:20 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HHw7sq6ZvDp9fwU2o3SEVmqKgrMh7wzDqSVHbfdQX6qN/ohlcv/hour?limit=1000 · HTTP 200 · 26/10/2026 15:20 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump · HTTP 404 · 26/10/2026 15:20 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ORYNUSDT · HTTP 400 · 26/10/2026 15:20 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ORYN-USD · HTTP 404 · 26/10/2026 15:20 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.420 vs $2.422 → 0,11%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002365 vs $0,000002366 → 0,02%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump_2026-10-26_141430.json',encoding='utf-8'));d=d.get('8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump',d);p=mock.patch('time.time',return_value=1793024070);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8PfdYsRhvAAi7jCo1CKMEGVhx14w2c2wVKy1TGEXpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 26/10/2026 15:20 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `6f9bdd58b8df97f3…`
