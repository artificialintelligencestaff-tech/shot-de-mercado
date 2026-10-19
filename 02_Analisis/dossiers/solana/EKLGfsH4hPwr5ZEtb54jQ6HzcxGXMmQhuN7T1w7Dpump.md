# make me rich make no mistakes (RICH) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00006805 · liquidez $21.771 · mcap $68.054 (al detectar)  
Detectado el 19/10/2026 12:21 UTC por: young-0.4 · edad 10.1 min · pesos info 60 / estructura 20 / precio 20 · info 20.3 · estructura 12.7 · precio/volumen 10.8 · cobertura 93/100, [info] narrative_wave: ola 'make': 22 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 44, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 21/10/2026 12:21 UTC (< 48 h) · vigente: quedan 47,2 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir RICH

Estudio de cómo se adquiere RICH, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 19/10/2026 13:06 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 19/10/2026 12:21 UTC | pumpswap `CoJPUW4…vMQS` | $21.771 | 10% | 0,919% | 9,186% | 91,864% | $109 | $327 |
| consulta 19/10/2026 13:06 UTC | pumpswap `CoJPUW4…vMQS` | $3.808 | 10% | 5,252% | 52,521% | 525,209% | $19 | $57 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump`
5. Configurar el slippage: 10% (liquidez $3.808, consulta 19/10/2026 13:06 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump) y el par en DexScreener (https://dexscreener.com/solana/CoJPUW4HnBk9oSJYSbM5YgUbzdcokK8vWVXJMgwKvMQS); mint authority / freeze authority: revocada / revocada · holders 1.959 · top-10 88,01% (consulta 19/10/2026 13:06 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump
- Par en DexScreener: https://dexscreener.com/solana/CoJPUW4HnBk9oSJYSbM5YgUbzdcokK8vWVXJMgwKvMQS
- Página del lanzamiento (pump.fun): https://pump.fun/coin/EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.959 · top-10 88,01% (consulta 19/10/2026 13:06 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | make me rich make no mistakes / RICH | registro de la detección (pumpportal_live) |
| Mint / contrato | `EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `CoJPUW4HnBk9oSJYSbM5YgUbzdcokK8vWVXJMgwKvMQS` | DexScreener, al detectar (8 par(es) en la consulta 19/10/2026 13:06 UTC) |
| Deployer | `4Swe7mXkRyUkWDopexdSuwpMerB9QDozR6393XcyxfVt` | PumpPortal (evento create), al detectar |
| Par creado | 19/10/2026 12:11 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,1 min / 10,1 min / 55,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 19/10/2026 13:06 UTC |
| Holders / top-10 | 1.959 / 88,01% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 19/10/2026 13:06 UTC |
| Holders efectivos del top-10 | 1,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 19/10/2026 13:06 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 19/10/2026 13:06 UTC |
| Links | DexScreener: https://dexscreener.com/solana/CoJPUW4HnBk9oSJYSbM5YgUbzdcokK8vWVXJMgwKvMQS · Solscan: https://solscan.io/token/EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump · pump.fun: https://pump.fun/coin/EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump · web / Telegram / X: no publicados en DexScreener | consulta 19/10/2026 13:06 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 19/10/2026 13:06 UTC)
- **Historia:**
  - Par creado el 19/10/2026 12:11 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 19/10/2026 12:21 UTC, con el par a 10,1 min de creado: precio $0,00006805, mcap $68.054, liquidez $21.771.
  - Velas de 1 h de GeckoTerminal (2, desde 19/10/2026 12:00 UTC): apertura $0,00004292 · máximo $0,00008897 (19/10/2026 12:00 UTC) · mínimo $0,000003962 (19/10/2026 12:00 UTC) · último cierre $0,000004211.
  - En la consulta 19/10/2026 13:06 UTC: precio $0,000004165, liquidez $3.808, FDV $4.030.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 19/10/2026 12:21 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00006805 |
| Liquidez | $21.771 |
| MCap | $68.054 |
| Volumen 24 h | $176.762 |
| Cambio 24 h | +58% |
| Cambio m5 / h1 | +4,8% / +58,5% |
| Volumen m5 / h1 | $62.029 / $176.762 |
| Trades m5 (compras / ventas) | 1.179 / 794 |
| Edad del par | 10,1 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 44; motivos sin regla: young-0.4 · edad 10.1 min · pesos info 60 / estructura 20 / precio 20 · info 20.3 · estructura 12.7 · precio/volumen 10.8 · cobertura 93/100, [info] narrative_wave: ola 'make': 22 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 2036 · top-10 41.0 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 2036/5106 = 0.40 → +0.6, [precio/volumen] volume_acceleration: vol 5 min ×4.2 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 60% en 5 min vs 58% en 1 h (s 0.09), [precio/volumen] liquidity_inflow: liquidez +20% en 8 min (s 0.66), [precio/volumen] holder_accumulation: holders 610→2036 (+118.8/min) · top10 47.3%→41.0% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=21771.36, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 44 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-19T12:21:06+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 67 de 40.782 tokens analizados (0,16%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 19/10/2026 12:21 UTC, hasta 21/10/2026 12:21 UTC · vigente: quedan 47,2 h.
- **Aceleración al detectar:** cambio m5 +4,8% · h1 +58,5% · h24 +58% · volumen m5/h1 0,35 · edad del par 10,1 min.
- **Precio de entrada** (alerta): $0,00006805.
- **Consulta 19/10/2026 13:06 UTC:** $0,000004165 (-93,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump_2026-10-19_122106.json` · blob `0a2779c7256c9918a3b8da4bfd66f17244df1369` · commit `ed2d6c9` (2026-10-19T12:56:54Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-19_122106`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump · registro · 19/10/2026 12:21 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump · HTTP 200 · 19/10/2026 13:06 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump/report · HTTP 200 · 19/10/2026 13:06 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump · HTTP 200 · 19/10/2026 13:06 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/CoJPUW4HnBk9oSJYSbM5YgUbzdcokK8vWVXJMgwKvMQS/ohlcv/hour?limit=1000 · HTTP 200 · 19/10/2026 13:06 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump · HTTP 404 · 19/10/2026 13:06 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=RICHUSDT · HTTP 400 · 19/10/2026 13:06 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/RICH-USD · HTTP 404 · 19/10/2026 13:06 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.808 vs $3.895 → 2,24%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000004165 vs $0,000004211 → 1,08%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump_2026-10-19_122106.json',encoding='utf-8'));d=d.get('EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump',d);p=mock.patch('time.time',return_value=1792412466);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint EKLGfsH4hPwr5ZEtb54jQ6HzcxGXMmQhuN7T1w7Dpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 19/10/2026 13:06 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `f021b3b58ab8bb93…`
