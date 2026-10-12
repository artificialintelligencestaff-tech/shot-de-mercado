# blackbox (BLACKBOX) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00007799 · liquidez $23.295 · mcap $77.989 (al detectar)  
Detectado el 12/10/2026 10:31 UTC por: young-0.4 · edad 11.4 min · pesos info 59 / estructura 20 / precio 20 · info 27.0 · estructura 13.1 · precio/volumen 10.2 · cobertura 98/100, [info] narrative_wave: ola 'blackbox': 14 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 40 caracteres → +7.3 (score 50, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 14/10/2026 10:31 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir BLACKBOX

Estudio de cómo se adquiere BLACKBOX, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 12/10/2026 10:45 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 12/10/2026 10:31 UTC | pumpswap `FzW4uxT…URhY` | $23.295 | 10% | 0,859% | 8,586% | 85,856% | $116 | $349 |
| consulta 12/10/2026 10:45 UTC | pumpswap `FzW4uxT…URhY` | $13.631 | 10% | 1,467% | 14,672% | 146,723% | $68 | $204 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc`
5. Configurar el slippage: 10% (liquidez $13.631, consulta 12/10/2026 10:45 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc) y el par en DexScreener (https://dexscreener.com/solana/FzW4uxTqRqzvegRi4sCKrxiTouTTtJSJorUu2pJDURhY); mint authority / freeze authority: revocada / revocada · holders 1.719 · top-10 44,56% (consulta 12/10/2026 10:45 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc
- Par en DexScreener: https://dexscreener.com/solana/FzW4uxTqRqzvegRi4sCKrxiTouTTtJSJorUu2pJDURhY
- Página del lanzamiento (pump.fun): https://pump.fun/coin/DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.719 · top-10 44,56% (consulta 12/10/2026 10:45 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | blackbox / BLACKBOX | registro de la detección (pumpportal_live) |
| Mint / contrato | `DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `FzW4uxTqRqzvegRi4sCKrxiTouTTtJSJorUu2pJDURhY` | DexScreener, al detectar (2 par(es) en la consulta 12/10/2026 10:45 UTC) |
| Deployer | `Dfv8M6RUAeDVefkRDEi6nY4pTpBTXTW22yUX9QQeAUJG` | PumpPortal (evento create), al detectar |
| Par creado | 12/10/2026 10:20 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,3 min / 11,3 min / 25,1 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 12/10/2026 10:45 UTC |
| Holders / top-10 | 1.719 / 44,56% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 12/10/2026 10:45 UTC |
| Holders efectivos del top-10 | 3,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 12/10/2026 10:45 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 12/10/2026 10:45 UTC |
| Links | DexScreener: https://dexscreener.com/solana/FzW4uxTqRqzvegRi4sCKrxiTouTTtJSJorUu2pJDURhY · Solscan: https://solscan.io/token/DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc · pump.fun: https://pump.fun/coin/DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc · web / Telegram / X: no publicados en DexScreener | consulta 12/10/2026 10:45 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 12/10/2026 10:45 UTC)
- **Historia:**
  - Par creado el 12/10/2026 10:20 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 12/10/2026 10:31 UTC, con el par a 11,3 min de creado: precio $0,00007799, mcap $77.989, liquidez $23.295.
  - Velas de 1 h de GeckoTerminal (1, desde 12/10/2026 10:00 UTC): apertura $0,00004672 · máximo $0,00009006 (12/10/2026 10:00 UTC) · mínimo $0,00001219 (12/10/2026 10:00 UTC) · último cierre $0,00003051.
  - En la consulta 12/10/2026 10:45 UTC: precio $0,00003002, liquidez $13.631, FDV $30.028.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 12/10/2026 10:31 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00007799 |
| Liquidez | $23.295 |
| MCap | $77.989 |
| Volumen 24 h | $117.307 |
| Cambio 24 h | +67% |
| Cambio m5 / h1 | +12,1% / +67,2% |
| Volumen m5 / h1 | $30.983 / $117.307 |
| Trades m5 (compras / ventas) | 488 / 397 |
| Edad del par | 11,3 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 50; motivos sin regla: young-0.4 · edad 11.4 min · pesos info 59 / estructura 20 / precio 20 · info 27.0 · estructura 13.1 · precio/volumen 10.2 · cobertura 98/100, [info] narrative_wave: ola 'blackbox': 14 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 40 caracteres → +7.3, [info] github_repo: repo half144/overdrive-releases · 408 estrellas → +4.9, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 1332 · top-10 39.5 % → +2.4, [estructura] dev_wallet: creador compró 9.6 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1332/2817 = 0.47 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×3.2 la tasa horaria (s 0.67), [precio/volumen] liquidity_inflow: liquidez +75% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 684→1332 (+108.0/min) · top10 41.0%→39.5% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=23294.81, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 50 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-12T10:31:29+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 49 de 30.898 tokens analizados (0,16%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 12/10/2026 10:31 UTC, hasta 14/10/2026 10:31 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +12,1% · h1 +67,2% · h24 +67% · volumen m5/h1 0,26 · edad del par 11,3 min.
- **Precio de entrada** (alerta): $0,00007799.
- **Consulta 12/10/2026 10:45 UTC:** $0,00003002 (-61,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc_2026-10-12_103129.json` · blob `24c136c3e6b89e2001ed56593a61cd4d79b8b1d8` · commit `50d950a` (2026-10-12T10:37:08Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-12_101734.json` · blob `9cb4bf3c6f9e5c6be0631a65fe9fe0514071f346` · commit `50d950a` (2026-10-12T10:37:08Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-12_103129`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc · registro · 12/10/2026 10:31 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc · HTTP 200 · 12/10/2026 10:45 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc/report · HTTP 200 · 12/10/2026 10:45 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc · HTTP 200 · 12/10/2026 10:45 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/FzW4uxTqRqzvegRi4sCKrxiTouTTtJSJorUu2pJDURhY/ohlcv/hour?limit=1000 · HTTP 200 · 12/10/2026 10:45 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc · HTTP 404 · 12/10/2026 10:45 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BLACKBOXUSDT · HTTP 400 · 12/10/2026 10:45 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BLACKBOX-USD · HTTP 404 · 12/10/2026 10:45 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $13.631 vs $14.066 → 3,09%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00003002 vs $0,00003051 → 1,61%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc_2026-10-12_103129.json',encoding='utf-8'));d=d.get('DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc',d);p=mock.patch('time.time',return_value=1791801089);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint DRonV3rJEeDwYvs2AShLFNWfiV4QkdEYEJz7QWJb7xFc --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 12/10/2026 10:45 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `8af76e5decdb7ed5…`
