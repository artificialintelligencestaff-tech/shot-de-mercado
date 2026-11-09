# Money Laundering Coin (MLC) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00009455 · liquidez $22.914 · mcap $94.453 (al detectar)  
Detectado el 09/11/2026 17:33 UTC por: young-0.4 · edad 15.0 min · pesos info 58 / estructura 21 / precio 21 · info 14.4 · estructura 15.2 · precio/volumen 11.5 · cobertura 84/100, [info] narrative_wave: ola 'money': 13 lanzamientos más en 1 h → +14.4, [estructura] bonding_progress: graduado (pumpswap) → +10.2 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 11/11/2026 17:33 UTC (< 48 h) · vigente: quedan 42,2 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir MLC

Estudio de cómo se adquiere MLC, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 09/11/2026 23:23 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 09/11/2026 17:33 UTC | pumpswap `92X7khc…GvDU` | $22.914 | 10% | 0,873% | 8,728% | 87,282% | $115 | $344 |
| consulta 09/11/2026 23:23 UTC | pumpswap `92X7khc…GvDU` | $1.799 | 10% | 11,117% | 111,172% | 1.111,723% | $9 | $27 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump`
5. Configurar el slippage: 10% (liquidez $1.799, consulta 09/11/2026 23:23 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump) y el par en DexScreener (https://dexscreener.com/solana/92X7khc9tUroXzyBTCU31rPq3aQxY4Z1R25Pd76ZGvDU); mint authority / freeze authority: revocada / revocada · holders 242 · top-10 99,51% (consulta 09/11/2026 23:23 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump
- Par en DexScreener: https://dexscreener.com/solana/92X7khc9tUroXzyBTCU31rPq3aQxY4Z1R25Pd76ZGvDU
- Página del lanzamiento (pump.fun): https://pump.fun/coin/34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 242 · top-10 99,51% (consulta 09/11/2026 23:23 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Money Laundering Coin / MLC | registro de la detección (pumpportal_live) |
| Mint / contrato | `34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `92X7khc9tUroXzyBTCU31rPq3aQxY4Z1R25Pd76ZGvDU` | DexScreener, al detectar (2 par(es) en la consulta 09/11/2026 23:23 UTC) |
| Deployer | `FniLij7J1auQjMuexNF9SqeNbLwKDGTBjeeSnndzi2Nc` | PumpPortal (evento create), al detectar |
| Par creado | 09/11/2026 17:18 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 15,0 min / 15,0 min / 6,1 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 09/11/2026 23:23 UTC |
| Holders / top-10 | 242 / 99,51% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 09/11/2026 23:23 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 09/11/2026 23:23 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 09/11/2026 23:23 UTC |
| Links | DexScreener: https://dexscreener.com/solana/92X7khc9tUroXzyBTCU31rPq3aQxY4Z1R25Pd76ZGvDU · Solscan: https://solscan.io/token/34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump · pump.fun: https://pump.fun/coin/34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump · web / Telegram / X: no publicados en DexScreener | consulta 09/11/2026 23:23 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 09/11/2026 23:23 UTC)
- **Historia:**
  - Par creado el 09/11/2026 17:18 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 09/11/2026 17:33 UTC, con el par a 15,0 min de creado: precio $0,00009455, mcap $94.453, liquidez $22.914.
  - Velas de 1 h de GeckoTerminal (4, desde 09/11/2026 17:00 UTC): apertura $0,00004012 · máximo $0,0001209 (09/11/2026 17:00 UTC) · mínimo $0,000001722 (09/11/2026 19:00 UTC) · último cierre $0,000001728.
  - En la consulta 09/11/2026 23:23 UTC: precio $0,000001725, liquidez $1.799, FDV $1.672.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 09/11/2026 17:33 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00009455 |
| Liquidez | $22.914 |
| MCap | $94.453 |
| Volumen 24 h | $171.292 |
| Cambio 24 h | +161% |
| Cambio m5 / h1 | +60,7% / +161,0% |
| Volumen m5 / h1 | $50.584 / $171.292 |
| Trades m5 (compras / ventas) | 1.053 / 899 |
| Edad del par | 15,0 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 15.0 min · pesos info 58 / estructura 21 / precio 21 · info 14.4 · estructura 15.2 · precio/volumen 11.5 · cobertura 84/100, [info] narrative_wave: ola 'money': 13 lanzamientos más en 1 h → +14.4, [estructura] bonding_progress: graduado (pumpswap) → +10.2, [estructura] holders_struct: holders 1442 · top-10 30.6 % → +2.5, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.1, [estructura] holder_to_txn_ratio: holders/txns 1442/6200 = 0.23 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×3.5 la tasa horaria (s 0.82), [precio/volumen] buy_pressure_shift: compras 54% en 5 min vs 47% en 1 h (s 0.20), [precio/volumen] liquidity_inflow: liquidez +25% en 8 min (s 0.83), [precio/volumen] holder_accumulation: holders 673→1442 (+64.1/min) · top10 36.1%→30.6% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=22914.25, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-09T17:33:32+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 95 de 46.968 tokens analizados (0,20%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 09/11/2026 17:33 UTC, hasta 11/11/2026 17:33 UTC · vigente: quedan 42,2 h.
- **Aceleración al detectar:** cambio m5 +60,7% · h1 +161,0% · h24 +161% · volumen m5/h1 0,30 · edad del par 15,0 min.
- **Precio de entrada** (alerta): $0,00009455.
- **Consulta 09/11/2026 23:23 UTC:** $0,000001725 (-98,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump_2026-11-09_173332.json` · blob `1e5cd326a8032b59f83a672ef41f97bacecdd92e` · commit `dba489d` (2026-11-09T22:42:44Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-09_173332`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump · registro · 09/11/2026 17:33 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump · HTTP 200 · 09/11/2026 23:23 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump/report · HTTP 200 · 09/11/2026 23:23 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump · HTTP 200 · 09/11/2026 23:23 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/92X7khc9tUroXzyBTCU31rPq3aQxY4Z1R25Pd76ZGvDU/ohlcv/hour?limit=1000 · HTTP 200 · 09/11/2026 23:23 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump · HTTP 404 · 09/11/2026 23:23 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MLCUSDT · HTTP 400 · 09/11/2026 23:23 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MLC-USD · HTTP 404 · 09/11/2026 23:23 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.799 vs $1.801 → 0,10%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000001725 vs $0,000001728 → 0,19%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump_2026-11-09_173332.json',encoding='utf-8'));d=d.get('34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump',d);p=mock.patch('time.time',return_value=1794245612);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 34SR1CCxRRM8pG582cpFMnx3nuzCKHPhN2E8iejFpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 09/11/2026 23:23 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `cdc129cf342d3d36…`
