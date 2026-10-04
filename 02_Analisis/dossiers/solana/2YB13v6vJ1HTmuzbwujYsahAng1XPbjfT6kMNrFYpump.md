# Higgs Agents (HIGGS) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001169 · liquidez $30.013 · mcap $116.837 (al detectar)  
Detectado el 04/10/2026 21:58 UTC por: young-0.4 · edad 23.7 min · pesos info 53 / estructura 23 / precio 23 · info 9.3 · estructura 20.1 · precio/volumen 10.5 · cobertura 85/100, [info] narrative_wave: ola 'agents': 4 lanzamientos más en 1 h → +6.6, [info] dex_profile: perfil pago en DexScreener → +2.7 (score 40, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 06/10/2026 21:58 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HIGGS

Estudio de cómo se adquiere HIGGS, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 04/10/2026 22:12 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 04/10/2026 21:58 UTC | pumpswap `4gSpTkf…9D1s` | $30.013 | 10% | 0,666% | 6,664% | 66,638% | $150 | $450 |
| consulta 04/10/2026 22:12 UTC | pumpswap `4gSpTkf…9D1s` | $25.386 | 10% | 0,788% | 7,878% | 78,783% | $127 | $381 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump`
5. Configurar el slippage: 10% (liquidez $25.386, consulta 04/10/2026 22:12 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump) y el par en DexScreener (https://dexscreener.com/solana/4gSpTkfUp3Xgg6oQ3QrmDdyRTBm8xvNm1NAUTVxx9D1s); mint authority / freeze authority: revocada / revocada · holders 5.180 · top-10 18,35% (consulta 04/10/2026 22:12 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump
- Par en DexScreener: https://dexscreener.com/solana/4gSpTkfUp3Xgg6oQ3QrmDdyRTBm8xvNm1NAUTVxx9D1s
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.180 · top-10 18,35% (consulta 04/10/2026 22:12 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Higgs Agents / HIGGS | registro de la detección (pumpportal_live) |
| Mint / contrato | `2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `4gSpTkfUp3Xgg6oQ3QrmDdyRTBm8xvNm1NAUTVxx9D1s` | DexScreener, al detectar (2 par(es) en la consulta 04/10/2026 22:12 UTC) |
| Deployer | `5gD1m1D9iqDx7AJtBvotbEFogjndADC4Mn3nv7nGAEjA` | PumpPortal (evento create), al detectar |
| Par creado | 04/10/2026 21:34 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 23,7 min / 23,7 min / 37,5 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 04/10/2026 22:12 UTC |
| Holders / top-10 | 5.180 / 18,35% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 04/10/2026 22:12 UTC |
| Holders efectivos del top-10 | 1,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 04/10/2026 22:12 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 04/10/2026 22:12 UTC |
| Links | DexScreener: https://dexscreener.com/solana/4gSpTkfUp3Xgg6oQ3QrmDdyRTBm8xvNm1NAUTVxx9D1s · Solscan: https://solscan.io/token/2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump · pump.fun: https://pump.fun/coin/2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump · web: https://higgsagents.lol · twitter: https://x.com/higgs_agents | consulta 04/10/2026 22:12 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 04/10/2026 22:12 UTC)
- **Historia:**
  - Par creado el 04/10/2026 21:34 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 04/10/2026 21:58 UTC, con el par a 23,7 min de creado: precio $0,0001169, mcap $116.837, liquidez $30.013.
  - Velas de 1 h de GeckoTerminal (2, desde 04/10/2026 21:00 UTC): apertura $0,0001044 · máximo $0,0001413 (04/10/2026 21:00 UTC) · mínimo $0,00003176 (04/10/2026 21:00 UTC) · último cierre $0,00009378.
  - En la consulta 04/10/2026 22:12 UTC: precio $0,00008288, liquidez $25.386, FDV $82.840.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 04/10/2026 21:58 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001169 |
| Liquidez | $30.013 |
| MCap | $116.837 |
| Volumen 24 h | $256.084 |
| Cambio 24 h | +62% |
| Cambio m5 / h1 | +30,2% / +62,1% |
| Volumen m5 / h1 | $56.453 / $256.084 |
| Trades m5 (compras / ventas) | 823 / 135 |
| Edad del par | 23,7 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 40; motivos sin regla: young-0.4 · edad 23.7 min · pesos info 53 / estructura 23 / precio 23 · info 9.3 · estructura 20.1 · precio/volumen 10.5 · cobertura 85/100, [info] narrative_wave: ola 'agents': 4 lanzamientos más en 1 h → +6.6, [info] dex_profile: perfil pago en DexScreener → +2.7, [estructura] bonding_progress: graduado (pumpswap) → +11.2, [estructura] holders_struct: holders 3104 · top-10 19.9 % → +5.6, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.3, [estructura] holder_to_txn_ratio: holders/txns 3104/4661 = 0.67 → +0.9, [precio/volumen] volume_acceleration: vol 5 min ×2.6 la tasa horaria (s 0.46), [precio/volumen] liquidity_inflow: liquidez +35% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 2178→3104 (+154.3/min) · top10 22.6%→19.9% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=30012.74, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=29528.15, score 40 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-04T21:58:38+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 12 de 10.759 tokens analizados (0,11%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 04/10/2026 21:58 UTC, hasta 06/10/2026 21:58 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +30,2% · h1 +62,1% · h24 +62% · volumen m5/h1 0,22 · edad del par 23,7 min.
- **Precio de entrada** (alerta): $0,0001169.
- **Consulta 04/10/2026 22:12 UTC:** $0,00008288 (-29,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump_2026-10-04_215838.json` · blob `189beab9bddcf3a524db6e7acb51414cd49c726d` · commit `92fe807` (2026-10-04T22:03:57Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-04_215838`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump · registro · 04/10/2026 21:58 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump · HTTP 200 · 04/10/2026 22:12 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump/report · HTTP 200 · 04/10/2026 22:12 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump · HTTP 200 · 04/10/2026 22:12 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/4gSpTkfUp3Xgg6oQ3QrmDdyRTBm8xvNm1NAUTVxx9D1s/ohlcv/hour?limit=1000 · HTTP 200 · 04/10/2026 22:12 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump · HTTP 404 · 04/10/2026 22:12 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HIGGSUSDT · HTTP 400 · 04/10/2026 22:12 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HIGGS-USD · HTTP 404 · 04/10/2026 22:12 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $25.386 vs $27.615 → 8,07%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00008288 vs $0,00009378 → 11,62%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump_2026-10-04_215838.json',encoding='utf-8'));d=d.get('2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump',d);p=mock.patch('time.time',return_value=1791151118);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2YB13v6vJ1HTmuzbwujYsahAng1XPbjfT6kMNrFYpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 04/10/2026 22:12 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `0f49bb274f794a85…`
