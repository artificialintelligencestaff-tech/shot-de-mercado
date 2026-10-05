# Super Intelligence Force (SIF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001172 · liquidez $29.965 · mcap $117.196 (al detectar)  
Detectado el 05/10/2026 00:35 UTC por: young-0.4 · edad 29.8 min · pesos info 50 / estructura 25 / precio 25 · info 13.5 · estructura 21.4 · precio/volumen 5.0 · cobertura 85/100, [info] narrative_wave: ola 'intelligence': 7 lanzamientos más en 1 h → +11.0, [info] dex_profile: perfil pago en DexScreener → +2.5 (score 40, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 07/10/2026 00:35 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SIF

Estudio de cómo se adquiere SIF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 05/10/2026 00:48 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 05/10/2026 00:35 UTC | pumpswap `96yJma4…rAk7` | $29.965 | 10% | 0,667% | 6,675% | 66,745% | $150 | $449 |
| consulta 05/10/2026 00:48 UTC | pumpswap `96yJma4…rAk7` | $27.215 | 10% | 0,735% | 7,349% | 73,489% | $136 | $408 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump`
5. Configurar el slippage: 10% (liquidez $27.215, consulta 05/10/2026 00:48 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump) y el par en DexScreener (https://dexscreener.com/solana/96yJma4gn885iUi61syLMdH5XjMTz1AGoxNHcBM5rAk7); mint authority / freeze authority: revocada / revocada · holders 4.706 · top-10 17,22% (consulta 05/10/2026 00:48 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump
- Par en DexScreener: https://dexscreener.com/solana/96yJma4gn885iUi61syLMdH5XjMTz1AGoxNHcBM5rAk7
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.706 · top-10 17,22% (consulta 05/10/2026 00:48 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Super Intelligence Force / SIF | registro de la detección (pumpportal_live) |
| Mint / contrato | `2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `96yJma4gn885iUi61syLMdH5XjMTz1AGoxNHcBM5rAk7` | DexScreener, al detectar (2 par(es) en la consulta 05/10/2026 00:48 UTC) |
| Deployer | `58VSAZVhz2cWRK4KteTbpnMUUJLUmUswxZf6iG9NAMH4` | PumpPortal (evento create), al detectar |
| Par creado | 05/10/2026 00:05 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 29,8 min / 29,8 min / 42,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 05/10/2026 00:48 UTC |
| Holders / top-10 | 4.706 / 17,22% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 05/10/2026 00:48 UTC |
| Holders efectivos del top-10 | 1,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 05/10/2026 00:48 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 05/10/2026 00:48 UTC |
| Links | DexScreener: https://dexscreener.com/solana/96yJma4gn885iUi61syLMdH5XjMTz1AGoxNHcBM5rAk7 · Solscan: https://solscan.io/token/2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump · pump.fun: https://pump.fun/coin/2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump · web: https://superintforce.lol · twitter: https://x.com/superintforce | consulta 05/10/2026 00:48 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 05/10/2026 00:48 UTC)
- **Historia:**
  - Par creado el 05/10/2026 00:05 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 05/10/2026 00:35 UTC, con el par a 29,8 min de creado: precio $0,0001172, mcap $117.196, liquidez $29.965.
  - Velas de 1 h de GeckoTerminal (1, desde 05/10/2026 00:00 UTC): apertura $0,0001131 · máximo $0,0001816 (05/10/2026 00:00 UTC) · mínimo $0,00007417 (05/10/2026 00:00 UTC) · último cierre $0,0001034.
  - En la consulta 05/10/2026 00:48 UTC: precio $0,00009627, liquidez $27.215, FDV $96.200.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 05/10/2026 00:35 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001172 |
| Liquidez | $29.965 |
| MCap | $117.196 |
| Volumen 24 h | $260.220 |
| Cambio 24 h | +56% |
| Cambio m5 / h1 | -22,9% / +56,3% |
| Volumen m5 / h1 | $38.119 / $260.220 |
| Trades m5 (compras / ventas) | 641 / 157 |
| Edad del par | 29,8 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 40; motivos sin regla: young-0.4 · edad 29.8 min · pesos info 50 / estructura 25 / precio 25 · info 13.5 · estructura 21.4 · precio/volumen 5.0 · cobertura 85/100, [info] narrative_wave: ola 'intelligence': 7 lanzamientos más en 1 h → +11.0, [info] dex_profile: perfil pago en DexScreener → +2.5, [estructura] bonding_progress: graduado (pumpswap) → +12.0, [estructura] holders_struct: holders 3863 · top-10 16.5 % → +6.0, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.5, [estructura] holder_to_txn_ratio: holders/txns 3863/5059 = 0.76 → +1.0, [precio/volumen] volume_acceleration: vol 5 min ×1.8 la tasa horaria (s 0.10), [precio/volumen] liquidity_inflow: liquidez +2% en 8 min (s 0.05), [precio/volumen] holder_accumulation: holders 2292→3863 (+130.9/min) · top10 37.1%→16.5% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=29964.77, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=31441.86, score 40 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-05T00:35:25+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 13 de 11.039 tokens analizados (0,12%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 05/10/2026 00:35 UTC, hasta 07/10/2026 00:35 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -22,9% · h1 +56,3% · h24 +56% · volumen m5/h1 0,15 · edad del par 29,8 min.
- **Precio de entrada** (alerta): $0,0001172.
- **Consulta 05/10/2026 00:48 UTC:** $0,00009627 (-17,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump_2026-10-05_003525.json` · blob `b84a1b577664a2e672461c7c72f9e332f3fc749d` · commit `c0e698a` (2026-10-05T00:40:54Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-05_003525`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump · registro · 05/10/2026 00:35 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump · HTTP 200 · 05/10/2026 00:48 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump/report · HTTP 200 · 05/10/2026 00:48 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump · HTTP 200 · 05/10/2026 00:48 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/96yJma4gn885iUi61syLMdH5XjMTz1AGoxNHcBM5rAk7/ohlcv/hour?limit=1000 · HTTP 200 · 05/10/2026 00:48 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump · HTTP 404 · 05/10/2026 00:48 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SIFUSDT · HTTP 400 · 05/10/2026 00:48 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SIF-USD · HTTP 404 · 05/10/2026 00:48 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $27.215 vs $29.401 → 7,44%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00009627 vs $0,0001034 → 6,85%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump_2026-10-05_003525.json',encoding='utf-8'));d=d.get('2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump',d);p=mock.patch('time.time',return_value=1791160525);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2trQcQbEiSsNCGhjUKZ7cNtcREgjFdGeTHndet2kpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 05/10/2026 00:48 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `296624ea9f210ead…`
