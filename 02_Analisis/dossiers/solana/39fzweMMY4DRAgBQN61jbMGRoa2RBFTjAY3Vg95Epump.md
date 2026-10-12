# พลอย (Ploy) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00006778 · liquidez $22.531 · mcap $67.783 (al detectar)  
Detectado el 12/10/2026 08:38 UTC por: young-0.4 · edad 11.5 min · pesos info 59 / estructura 20 / precio 20 · info 23.0 · estructura 13.1 · precio/volumen 11.6 · cobertura 93/100, [info] narrative_wave: ola 'ploy': 20 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 48, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 14/10/2026 08:38 UTC (< 48 h) · vigente: quedan 47,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Ploy

Estudio de cómo se adquiere Ploy, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 12/10/2026 08:46 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 12/10/2026 08:38 UTC | pumpswap `7X1nomA…BHJY` | $22.531 | 10% | 0,888% | 8,877% | 88,766% | $113 | $338 |
| consulta 12/10/2026 08:46 UTC | pumpswap `7X1nomA…BHJY` | $25.028 | 10% | 0,799% | 7,991% | 79,911% | $125 | $375 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump`
5. Configurar el slippage: 10% (liquidez $25.028, consulta 12/10/2026 08:46 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump) y el par en DexScreener (https://dexscreener.com/solana/7X1nomASzsx8f9uYArTyiKyhsxb1VJob7EjX7UbwBHJY); mint authority / freeze authority: revocada / revocada · holders 1.363 · top-10 32,33% (consulta 12/10/2026 08:46 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump
- Par en DexScreener: https://dexscreener.com/solana/7X1nomASzsx8f9uYArTyiKyhsxb1VJob7EjX7UbwBHJY
- Página del lanzamiento (pump.fun): https://pump.fun/coin/39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.363 · top-10 32,33% (consulta 12/10/2026 08:46 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | พลอย / Ploy | registro de la detección (pumpportal_live) |
| Mint / contrato | `39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7X1nomASzsx8f9uYArTyiKyhsxb1VJob7EjX7UbwBHJY` | DexScreener, al detectar (2 par(es) en la consulta 12/10/2026 08:46 UTC) |
| Deployer | `FFPmqVLMj9TNbQXcrXyevcM3pxGaK4ApaAT4oLq2b3S7` | PumpPortal (evento create), al detectar |
| Par creado | 12/10/2026 08:27 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,5 min / 11,5 min / 19,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 12/10/2026 08:46 UTC |
| Holders / top-10 | 1.363 / 32,33% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 12/10/2026 08:46 UTC |
| Holders efectivos del top-10 | 4,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 12/10/2026 08:46 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 12/10/2026 08:46 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7X1nomASzsx8f9uYArTyiKyhsxb1VJob7EjX7UbwBHJY · Solscan: https://solscan.io/token/39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump · pump.fun: https://pump.fun/coin/39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump · twitter: https://x.com/Esk100x/status/2109563530961903694?s=20 · instagram: https://www.instagram.com/reel/DeW4xypTuSQ/ | consulta 12/10/2026 08:46 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 12/10/2026 08:46 UTC)
- **Historia:**
  - Par creado el 12/10/2026 08:27 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 12/10/2026 08:38 UTC, con el par a 11,5 min de creado: precio $0,00006778, mcap $67.783, liquidez $22.531.
  - Velas de 1 h de GeckoTerminal (1, desde 12/10/2026 08:00 UTC): apertura $0,00004613 · máximo $0,0001498 (12/10/2026 08:00 UTC) · mínimo $0,00002716 (12/10/2026 08:00 UTC) · último cierre $0,0001383.
  - En la consulta 12/10/2026 08:46 UTC: precio $0,00008826, liquidez $25.028, FDV $88.263.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 12/10/2026 08:38 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00006778 |
| Liquidez | $22.531 |
| MCap | $67.783 |
| Volumen 24 h | $104.666 |
| Cambio 24 h | +51% |
| Cambio m5 / h1 | +7,5% / +50,7% |
| Volumen m5 / h1 | $32.547 / $104.666 |
| Trades m5 (compras / ventas) | 388 / 291 |
| Edad del par | 11,5 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 48; motivos sin regla: young-0.4 · edad 11.5 min · pesos info 59 / estructura 20 / precio 20 · info 23.0 · estructura 13.1 · precio/volumen 11.6 · cobertura 93/100, [info] narrative_wave: ola 'ploy': 20 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 1035 · top-10 43.5 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1035/2013 = 0.51 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×3.7 la tasa horaria (s 0.89), [precio/volumen] buy_pressure_shift: compras 57% en 5 min vs 56% en 1 h (s 0.06), [precio/volumen] liquidity_inflow: liquidez +31% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 683→1035 (+58.7/min) · top10 39.4%→43.5% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=22531.2, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 48 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-12T08:38:34+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 49 de 30.776 tokens analizados (0,16%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 12/10/2026 08:38 UTC, hasta 14/10/2026 08:38 UTC · vigente: quedan 47,9 h.
- **Aceleración al detectar:** cambio m5 +7,5% · h1 +50,7% · h24 +51% · volumen m5/h1 0,31 · edad del par 11,5 min.
- **Precio de entrada** (alerta): $0,00006778.
- **Consulta 12/10/2026 08:46 UTC:** $0,00008826 (+30,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump_2026-10-12_083834.json` · blob `c52f21b8edc239832ba1561b35bfea9addc49620` · commit `9f9e847` (2026-10-12T08:39:49Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-12_083834`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump · registro · 12/10/2026 08:38 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump · HTTP 200 · 12/10/2026 08:46 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump/report · HTTP 200 · 12/10/2026 08:46 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump · HTTP 200 · 12/10/2026 08:46 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7X1nomASzsx8f9uYArTyiKyhsxb1VJob7EjX7UbwBHJY/ohlcv/hour?limit=1000 · HTTP 200 · 12/10/2026 08:46 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump · HTTP 404 · 12/10/2026 08:46 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=PLOYUSDT · HTTP 400 · 12/10/2026 08:46 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/PLOY-USD · HTTP 404 · 12/10/2026 08:46 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $25.028 vs $22.632 → 9,57%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00008826 vs $0,0001383 → 36,16%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump_2026-10-12_083834.json',encoding='utf-8'));d=d.get('39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump',d);p=mock.patch('time.time',return_value=1791794314);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 39fzweMMY4DRAgBQN61jbMGRoa2RBFTjAY3Vg95Epump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 12/10/2026 08:46 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `a13f4c32a0b249fd…`
