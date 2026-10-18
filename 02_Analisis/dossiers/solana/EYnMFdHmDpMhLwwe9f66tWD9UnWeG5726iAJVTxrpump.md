# French Goku Hero (EZECK) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001759 · liquidez $39.009 · mcap $175.983 (al detectar)  
Detectado el 18/10/2026 20:49 UTC por: young-0.4 · edad 10.0 min · pesos info 60 / estructura 20 / precio 20 · info 17.7 · estructura 14.8 · precio/volumen 12.2 · cobertura 93/100, [info] narrative_wave: ola 'french': 23 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.7 (score 45, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 20/10/2026 20:49 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir EZECK

Estudio de cómo se adquiere EZECK, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 18/10/2026 21:19 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 18/10/2026 20:49 UTC | pumpswap `BSfr5us…AtFR` | $39.009 | 10% | 0,513% | 5,127% | 51,271% | $195 | $585 |
| consulta 18/10/2026 21:19 UTC | pumpswap `BSfr5us…AtFR` | $6.439 | 10% | 3,106% | 31,058% | 310,584% | $32 | $97 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump`
5. Configurar el slippage: 10% (liquidez $6.439, consulta 18/10/2026 21:19 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump) y el par en DexScreener (https://dexscreener.com/solana/BSfr5usSZwT662TA1PYpqsTVN8oYYDXmkLKRxn8eAtFR); mint authority / freeze authority: revocada / revocada · holders 2.372 · top-10 70,47% (consulta 18/10/2026 21:19 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump
- Par en DexScreener: https://dexscreener.com/solana/BSfr5usSZwT662TA1PYpqsTVN8oYYDXmkLKRxn8eAtFR
- Página del lanzamiento (pump.fun): https://pump.fun/coin/EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.372 · top-10 70,47% (consulta 18/10/2026 21:19 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | French Goku Hero / EZECK | registro de la detección (pumpportal_live) |
| Mint / contrato | `EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BSfr5usSZwT662TA1PYpqsTVN8oYYDXmkLKRxn8eAtFR` | DexScreener, al detectar (4 par(es) en la consulta 18/10/2026 21:19 UTC) |
| Deployer | `9xjfctksMVknvzdwo3iMR1WR76jwzUNokBnhaWUQr3CC` | PumpPortal (evento create), al detectar |
| Par creado | 18/10/2026 20:39 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,0 min / 10,0 min / 39,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 18/10/2026 21:19 UTC |
| Holders / top-10 | 2.372 / 70,47% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 18/10/2026 21:19 UTC |
| Holders efectivos del top-10 | 2,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 18/10/2026 21:19 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 18/10/2026 21:19 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BSfr5usSZwT662TA1PYpqsTVN8oYYDXmkLKRxn8eAtFR · Solscan: https://solscan.io/token/EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump · pump.fun: https://pump.fun/coin/EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump · twitter: https://x.com/thedevelopooor/status/2111919780181532689?s=20 · instagram: https://www.instagram.com/stonebrushstudio/ | consulta 18/10/2026 21:19 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 18/10/2026 21:19 UTC)
- **Historia:**
  - Par creado el 18/10/2026 20:39 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 18/10/2026 20:49 UTC, con el par a 10,0 min de creado: precio $0,0001759, mcap $175.983, liquidez $39.009.
  - Velas de 1 h de GeckoTerminal (2, desde 18/10/2026 20:00 UTC): apertura $0,00004253 · máximo $0,0002324 (18/10/2026 20:00 UTC) · mínimo $0,000007769 (18/10/2026 21:00 UTC) · último cierre $0,000008308.
  - En la consulta 18/10/2026 21:19 UTC: precio $0,000008320, liquidez $6.439, FDV $8.180.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 18/10/2026 20:49 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001759 |
| Liquidez | $39.009 |
| MCap | $175.983 |
| Volumen 24 h | $590.053 |
| Cambio 24 h | +314% |
| Cambio m5 / h1 | -2,2% / +314,0% |
| Volumen m5 / h1 | $236.450 / $590.053 |
| Trades m5 (compras / ventas) | 1.966 / 1.619 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 45; motivos sin regla: young-0.4 · edad 10.0 min · pesos info 60 / estructura 20 / precio 20 · info 17.7 · estructura 14.8 · precio/volumen 12.2 · cobertura 93/100, [info] narrative_wave: ola 'french': 23 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.7, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1847 · top-10 29.5 % → +4.8, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1847/9209 = 0.20 → +0.3, [precio/volumen] volume_acceleration: vol 5 min ×4.8 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 55% en 5 min vs 52% en 1 h (s 0.16), [precio/volumen] liquidity_inflow: liquidez +73% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1120→1847 (+121.2/min) · top10 26.4%→29.5% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=39008.55, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 45 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-18T20:49:40+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 64 de 40.132 tokens analizados (0,16%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 18/10/2026 20:49 UTC, hasta 20/10/2026 20:49 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -2,2% · h1 +314,0% · h24 +314% · volumen m5/h1 0,40 · edad del par 10,0 min.
- **Precio de entrada** (alerta): $0,0001759.
- **Consulta 18/10/2026 21:19 UTC:** $0,000008320 (-95,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump_2026-10-18_204940.json` · blob `966d935e09c1a25271c686b93f56901623579ae8` · commit `2338440` (2026-10-18T21:08:35Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-18_204940`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump · registro · 18/10/2026 20:49 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump · HTTP 200 · 18/10/2026 21:19 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump/report · HTTP 200 · 18/10/2026 21:19 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump · HTTP 200 · 18/10/2026 21:19 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BSfr5usSZwT662TA1PYpqsTVN8oYYDXmkLKRxn8eAtFR/ohlcv/hour?limit=1000 · HTTP 200 · 18/10/2026 21:19 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump · HTTP 404 · 18/10/2026 21:19 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=EZECKUSDT · HTTP 400 · 18/10/2026 21:19 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/EZECK-USD · HTTP 404 · 18/10/2026 21:19 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $6.439 vs $6.438 → 0,02%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000008320 vs $0,000008308 → 0,14%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump_2026-10-18_204940.json',encoding='utf-8'));d=d.get('EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump',d);p=mock.patch('time.time',return_value=1792356580);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint EYnMFdHmDpMhLwwe9f66tWD9UnWeG5726iAJVTxrpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 18/10/2026 21:19 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `8bb21550df029240…`
