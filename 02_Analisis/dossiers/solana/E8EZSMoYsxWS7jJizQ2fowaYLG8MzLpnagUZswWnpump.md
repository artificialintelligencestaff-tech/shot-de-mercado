# ai doomer (AI) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00009316 · liquidez $26.128 · mcap $93.166 (al detectar)  
Detectado el 06/10/2026 20:47 UTC por: young-0.4 · edad 11.2 min · pesos info 59 / estructura 20 / precio 20 · info 15.6 · estructura 17.4 · precio/volumen 10.5 · cobertura 93/100, [info] narrative_wave: ola 'doomer': 7 lanzamientos más en 1 h → +13.0, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.6 (score 44, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 08/10/2026 20:47 UTC (< 48 h) · vigente: quedan 47,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir AI

Estudio de cómo se adquiere AI, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 20:55 UTC; CoinGecko sin ficha para este contrato). Binance tiene un par AIUSDT, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza. Coinbase tiene un par AI-USD, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza.

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 20:47 UTC | pumpswap `Aw6L7t1…uoSv` | $26.128 | 10% | 0,765% | 7,655% | 76,547% | $131 | $392 |
| consulta 06/10/2026 20:55 UTC | pumpswap `Aw6L7t1…uoSv` | $2.284 | 10% | 8,757% | 87,571% | 875,707% | $11 | $34 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump`
5. Configurar el slippage: 10% (liquidez $2.284, consulta 06/10/2026 20:55 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump) y el par en DexScreener (https://dexscreener.com/solana/Aw6L7t14j4YC6Ewu3Rz5vnrKpApeztnudgNzMLKFuoSv); mint authority / freeze authority: revocada / revocada · holders 101 · top-10 99,99% (consulta 06/10/2026 20:55 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump
- Par en DexScreener: https://dexscreener.com/solana/Aw6L7t14j4YC6Ewu3Rz5vnrKpApeztnudgNzMLKFuoSv
- Página del lanzamiento (pump.fun): https://pump.fun/coin/E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 101 · top-10 99,99% (consulta 06/10/2026 20:55 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | ai doomer / AI | registro de la detección (pumpportal_live) |
| Mint / contrato | `E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Aw6L7t14j4YC6Ewu3Rz5vnrKpApeztnudgNzMLKFuoSv` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 20:55 UTC) |
| Deployer | `2jpxDSj2dC6zAdbmdci1hAehT6kmboAsGAcsno4tbm2d` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 20:36 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,2 min / 11,2 min / 19,5 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 20:55 UTC |
| Holders / top-10 | 101 / 99,99% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 20:55 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 20:55 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 20:55 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Aw6L7t14j4YC6Ewu3Rz5vnrKpApeztnudgNzMLKFuoSv · Solscan: https://solscan.io/token/E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump · pump.fun: https://pump.fun/coin/E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump · web / Telegram / X: no publicados en DexScreener | consulta 06/10/2026 20:55 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 20:55 UTC)
- **Historia:**
  - Par creado el 06/10/2026 20:36 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 20:47 UTC, con el par a 11,2 min de creado: precio $0,00009316, mcap $93.166, liquidez $26.128.
  - Velas de 1 h de GeckoTerminal (1, desde 06/10/2026 20:00 UTC): apertura $0,00005103 · máximo $0,0001177 (06/10/2026 20:00 UTC) · mínimo $0,000002264 (06/10/2026 20:00 UTC) · último cierre $0,000002264.
  - En la consulta 06/10/2026 20:55 UTC: precio $0,000002263, liquidez $2.284, FDV $2.263.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 20:47 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00009316 |
| Liquidez | $26.128 |
| MCap | $93.166 |
| Volumen 24 h | $46.560 |
| Cambio 24 h | +82% |
| Cambio m5 / h1 | +4,6% / +82,3% |
| Volumen m5 / h1 | $12.527 / $46.560 |
| Trades m5 (compras / ventas) | 532 / 242 |
| Edad del par | 11,2 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 44; motivos sin regla: young-0.4 · edad 11.2 min · pesos info 59 / estructura 20 / precio 20 · info 15.6 · estructura 17.4 · precio/volumen 10.5 · cobertura 93/100, [info] narrative_wave: ola 'doomer': 7 lanzamientos más en 1 h → +13.0, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.6, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1907 · top-10 28.8 % → +4.9, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.0, [estructura] holder_to_txn_ratio: holders/txns 1907/2610 = 0.73 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×3.2 la tasa horaria (s 0.69), [precio/volumen] quiet_accumulation: precio quieto (m5 +4.6%) con vol ×3.2 y compras 69% (s 0.53), [precio/volumen] liquidity_inflow: liquidez +8% en 8 min (s 0.27), [precio/volumen] holder_accumulation: holders 1166→1907 (+123.5/min) · top10 32.9%→28.8% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=26127.74, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 44 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T20:47:37+00:00, sin estado previo): **25** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen bajo, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 19 de 16.749 tokens analizados (0,11%) quedan ≥ 56. Con score 25, este activo queda en el percentil 97,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 20:47 UTC, hasta 08/10/2026 20:47 UTC · vigente: quedan 47,9 h.
- **Aceleración al detectar:** cambio m5 +4,6% · h1 +82,3% · h24 +82% · volumen m5/h1 0,27 · edad del par 11,2 min.
- **Precio de entrada** (alerta): $0,00009316.
- **Consulta 06/10/2026 20:55 UTC:** $0,000002263 (-97,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump_2026-10-06_204737.json` · blob `a363dca610d1803cf3ff73939d1397b6aa9b217d` · commit `3c57620` (2026-10-06T20:49:37Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_204737`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump · registro · 06/10/2026 20:47 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump · HTTP 200 · 06/10/2026 20:55 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump/report · HTTP 200 · 06/10/2026 20:55 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump · HTTP 200 · 06/10/2026 20:55 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Aw6L7t14j4YC6Ewu3Rz5vnrKpApeztnudgNzMLKFuoSv/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 20:55 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump · HTTP 404 · 06/10/2026 20:55 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AIUSDT · HTTP 200 · 06/10/2026 20:55 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AI-USD · HTTP 200 · 06/10/2026 20:55 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.284 vs $2.286 → 0,09%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002263 vs $0,000002264 → 0,03%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump_2026-10-06_204737.json',encoding='utf-8'));d=d.get('E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump',d);p=mock.patch('time.time',return_value=1791319657);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint E8EZSMoYsxWS7jJizQ2fowaYLG8MzLpnagUZswWnpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 20:55 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `c7acbdb11caf4e5f…`
