# Habibi Cat (HABICAT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00005783 · liquidez $18.593 · mcap $57.726 (al detectar)  
Detectado el 08/11/2026 02:30 UTC por: young-0.4 · edad 10.7 min · pesos info 60 / estructura 20 / precio 20 · info 14.9 · estructura 17.3 · precio/volumen 8.9 · cobertura 83/100, [info] narrative_wave: ola 'habibi': 9 lanzamientos más en 1 h → +14.9, [estructura] bonding_progress: graduado (pumpswap) → +9.7 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 10/11/2026 02:30 UTC (< 48 h) · vigente: quedan 41,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HABICAT

Estudio de cómo se adquiere HABICAT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/11/2026 09:09 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/11/2026 02:30 UTC | pumpswap `6qfCiUj…vZ1c` | $18.593 | 10% | 1,076% | 10,757% | 107,567% | $93 | $279 |
| consulta 08/11/2026 09:09 UTC | pumpswap `6qfCiUj…vZ1c` | $2.207 | 10% | 9,061% | 90,610% | 906,101% | $11 | $33 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump`
5. Configurar el slippage: 10% (liquidez $2.207, consulta 08/11/2026 09:09 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump) y el par en DexScreener (https://dexscreener.com/solana/6qfCiUjQ5C3MnnF8FwoosENgekNNwGGoTsJExBTwvZ1c); mint authority / freeze authority: revocada / revocada · holders 570 · top-10 99,03% (consulta 08/11/2026 09:09 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump
- Par en DexScreener: https://dexscreener.com/solana/6qfCiUjQ5C3MnnF8FwoosENgekNNwGGoTsJExBTwvZ1c
- Página del lanzamiento (pump.fun): https://pump.fun/coin/CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 570 · top-10 99,03% (consulta 08/11/2026 09:09 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Habibi Cat / HABICAT | registro de la detección (pumpportal_live) |
| Mint / contrato | `CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6qfCiUjQ5C3MnnF8FwoosENgekNNwGGoTsJExBTwvZ1c` | DexScreener, al detectar (3 par(es) en la consulta 08/11/2026 09:09 UTC) |
| Deployer | `De1pad2eUeQJ84FDKaeD7iHYcxGrosfndo4qHUpQtLKB` | PumpPortal (evento create), al detectar |
| Par creado | 08/11/2026 02:19 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,7 min / 10,7 min / 6,8 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/11/2026 09:09 UTC |
| Holders / top-10 | 570 / 99,03% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/11/2026 09:09 UTC |
| Holders efectivos del top-10 | 1,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/11/2026 09:09 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 08/11/2026 09:09 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6qfCiUjQ5C3MnnF8FwoosENgekNNwGGoTsJExBTwvZ1c · Solscan: https://solscan.io/token/CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump · pump.fun: https://pump.fun/coin/CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump · web / Telegram / X: no publicados en DexScreener | consulta 08/11/2026 09:09 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/11/2026 09:09 UTC)
- **Historia:**
  - Par creado el 08/11/2026 02:19 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/11/2026 02:30 UTC, con el par a 10,7 min de creado: precio $0,00005783, mcap $57.726, liquidez $18.593.
  - Velas de 1 h de GeckoTerminal (5, desde 08/11/2026 02:00 UTC): apertura $0,00003757 · máximo $0,0001003 (08/11/2026 02:00 UTC) · mínimo $0,000002097 (08/11/2026 07:00 UTC) · último cierre $0,000002098.
  - En la consulta 08/11/2026 09:09 UTC: precio $0,000002095, liquidez $2.207, FDV $2.032.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/11/2026 02:30 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00005783 |
| Liquidez | $18.593 |
| MCap | $57.726 |
| Volumen 24 h | $295.367 |
| Cambio 24 h | +57% |
| Cambio m5 / h1 | +1,1% / +56,9% |
| Volumen m5 / h1 | $93.161 / $295.367 |
| Trades m5 (compras / ventas) | 831 / 812 |
| Edad del par | 10,7 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 10.7 min · pesos info 60 / estructura 20 / precio 20 · info 14.9 · estructura 17.3 · precio/volumen 8.9 · cobertura 83/100, [info] narrative_wave: ola 'habibi': 9 lanzamientos más en 1 h → +14.9, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 2453 · top-10 24.5 % → +4.8, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.0, [estructura] holder_to_txn_ratio: holders/txns 2453/4698 = 0.52 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×3.8 la tasa horaria (s 0.91), [precio/volumen] liquidity_inflow: liquidez +9% en 8 min (s 0.29), [precio/volumen] holder_accumulation: holders 1565→2453 (+148.0/min) · top10 20.2%→24.5% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=18593.04, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-08T02:30:35+00:00, sin estado previo): **35** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez baja, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 94 de 46.901 tokens analizados (0,20%) quedan ≥ 56. Con score 35, este activo queda en el percentil 98,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/11/2026 02:30 UTC, hasta 10/11/2026 02:30 UTC · vigente: quedan 41,4 h.
- **Aceleración al detectar:** cambio m5 +1,1% · h1 +56,9% · h24 +57% · volumen m5/h1 0,32 · edad del par 10,7 min.
- **Precio de entrada** (alerta): $0,00005783.
- **Consulta 08/11/2026 09:09 UTC:** $0,000002095 (-96,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump_2026-11-08_023035.json` · blob `ea3905038b736b1ce472343b17bedb85c027a4f4` · commit `dbd4a73` (2026-11-08T08:53:52Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-08_023035`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump · registro · 08/11/2026 02:30 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump · HTTP 200 · 08/11/2026 09:09 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump/report · HTTP 200 · 08/11/2026 09:09 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump · HTTP 200 · 08/11/2026 09:09 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6qfCiUjQ5C3MnnF8FwoosENgekNNwGGoTsJExBTwvZ1c/ohlcv/hour?limit=1000 · HTTP 200 · 08/11/2026 09:09 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump · HTTP 404 · 08/11/2026 09:09 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HABICATUSDT · HTTP 400 · 08/11/2026 09:09 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HABICAT-USD · HTTP 404 · 08/11/2026 09:09 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.207 vs $2.215 → 0,35%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002095 vs $0,000002098 → 0,15%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump_2026-11-08_023035.json',encoding='utf-8'));d=d.get('CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump',d);p=mock.patch('time.time',return_value=1794105035);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint CCeygruVRoRvb2sCN2ouo6XMSCVtGFBFumwm3hhYpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/11/2026 09:09 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `f621bb8612433afb…`
