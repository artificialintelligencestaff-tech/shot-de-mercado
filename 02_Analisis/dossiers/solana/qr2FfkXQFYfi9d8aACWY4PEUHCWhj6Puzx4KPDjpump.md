# Dregg (DREGG) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003366 · liquidez $167.587 · mcap $3.366.886 (al detectar)  
Detectado el 02/10/2026 14:47 UTC por: MCap > $1M, Volumen decente, Liquidez alta (score 62, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 04/10/2026 14:47 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir DREGG

Estudio de cómo se adquiere DREGG, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 14:58 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 14:47 UTC | pumpswap `Ebis85w…jGmB` | $167.587 | 5% | 0,119% | 1,193% | 11,934% | $838 | $2.514 |
| consulta 02/10/2026 14:58 UTC | pumpswap `Ebis85w…jGmB` | $166.522 | 5% | 0,120% | 1,201% | 12,010% | $833 | $2.498 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump`
5. Configurar el slippage: 5% (liquidez $166.522, consulta 02/10/2026 14:58 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump) y el par en DexScreener (https://dexscreener.com/solana/Ebis85wyZiKxmi6yUWZmQYFCjCazcp6wXgyCxc2mjGmB); mint authority / freeze authority: revocada / revocada · holders 3.977 · top-10 11,28% (consulta 02/10/2026 14:58 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump
- Par en DexScreener: https://dexscreener.com/solana/Ebis85wyZiKxmi6yUWZmQYFCjCazcp6wXgyCxc2mjGmB
- Página del lanzamiento (pump.fun): https://pump.fun/coin/qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.977 · top-10 11,28% (consulta 02/10/2026 14:58 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Dregg / DREGG | registro de la detección (pumpportal_live) |
| Mint / contrato | `qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Ebis85wyZiKxmi6yUWZmQYFCjCazcp6wXgyCxc2mjGmB` | DexScreener, al detectar (2 par(es) en la consulta 02/10/2026 14:58 UTC) |
| Deployer | `ECrMoS6UJDSkiQN7uGQwF4XVUNwiTwiQV7hYcUReBn6B` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 14:37 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,0 min / 10,0 min / 21,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 14:58 UTC |
| Holders / top-10 | 3.977 / 11,28% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 14:58 UTC |
| Holders efectivos del top-10 | 8,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 14:58 UTC |
| Etiquetas de RugCheck | «High holder correlation», «Copycat token» | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 14:58 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Ebis85wyZiKxmi6yUWZmQYFCjCazcp6wXgyCxc2mjGmB · Solscan: https://solscan.io/token/qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump · pump.fun: https://pump.fun/coin/qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump · web / Telegram / X: no publicados en DexScreener | consulta 02/10/2026 14:58 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 14:58 UTC)
- **Historia:**
  - Par creado el 02/10/2026 14:37 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 14:47 UTC, con el par a 10,0 min de creado: precio $0,003366, mcap $3.366.886, liquidez $167.587.
  - Velas de 1 h de GeckoTerminal (1, desde 02/10/2026 14:00 UTC): apertura $0,003178 · máximo $0,003382 (02/10/2026 14:00 UTC) · mínimo $0,00005036 (02/10/2026 14:00 UTC) · último cierre $0,003346.
  - En la consulta 02/10/2026 14:58 UTC: precio $0,003347, liquidez $166.522, FDV $3.347.189.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 14:47 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003366 |
| Liquidez | $167.587 |
| MCap | $3.366.886 |
| Volumen 24 h | $72.837 |
| Cambio 24 h | +6.569% |
| Cambio m5 / h1 | +2,5% / +6.569,0% |
| Volumen m5 / h1 | $521 / $72.837 |
| Trades m5 (compras / ventas) | 10 / 8 |
| Edad del par | 10,0 min |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 1/2 (50,0%, IC90 12,1%–87,9%) · secundaria 0/1 resueltas (shadow_monitor.json).

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

Desglose no reproducible desde los motivos registrados (suma 60 vs score 62; motivos sin regla: Anticipación (lib_early_signals early-0.2): +2 — liquidity_inflow: liquidez +3% en 8 min → +0.17; holder_accumulation: holders 3880→3977 (+16.2/min) · top10 100.0%→11.3% → +2): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T14:47:14+00:00, sin estado previo): **60** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen decente, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=5.0% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 11 de 7.819 tokens analizados (0,14%) quedan ≥ 56. Con score 60, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 14:47 UTC, hasta 04/10/2026 14:47 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +2,5% · h1 +6.569,0% · h24 +6.569% · volumen m5/h1 0,01 · edad del par 10,0 min.
- **Precio de entrada** (alerta): $0,003366.
- **Consulta 02/10/2026 14:58 UTC:** $0,003347 (-0,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump_2026-10-02_144714.json` · blob `762b235cd768d8782d4d0605a821c9bf127b4f36` · commit `416efc5` (2026-10-02T14:52:02Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-02_143451.json` · blob `2c7d9d0cb0486556247b0f184fca02583d2d5ad2` · commit `416efc5` (2026-10-02T14:52:02Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_144714`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump · registro · 02/10/2026 14:47 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump · HTTP 200 · 02/10/2026 14:58 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump/report · HTTP 200 · 02/10/2026 14:58 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump · HTTP 200 · 02/10/2026 14:58 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Ebis85wyZiKxmi6yUWZmQYFCjCazcp6wXgyCxc2mjGmB/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 14:58 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump · HTTP 404 · 02/10/2026 14:58 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=DREGGUSDT · HTTP 400 · 02/10/2026 14:58 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/DREGG-USD · HTTP 404 · 02/10/2026 14:58 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $166.522 vs $166.576 → 0,03%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003347 vs $0,003346 → 0,02%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump_2026-10-02_144714.json',encoding='utf-8'));d=d.get('qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump',d);p=mock.patch('time.time',return_value=1790952434);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint qr2FfkXQFYfi9d8aACWY4PEUHCWhj6Puzx4KPDjpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 14:58 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `41488395b680f252…`
