# Condo (CONDO) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001342 · liquidez $31.806 · mcap $134.294 (al detectar)  
Detectado el 06/10/2026 23:16 UTC por: young-0.4 · edad 10.7 min · pesos info 60 / estructura 20 / precio 20 · info 20.2 · estructura 17.7 · precio/volumen 12.6 · cobertura 93/100, [info] narrative_wave: ola 'condo': 13 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 33 caracteres → +5.3 (score 51, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 08/10/2026 23:16 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir CONDO

Estudio de cómo se adquiere CONDO, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 23:36 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 23:16 UTC | pumpswap `BbcGFVN…gNRe` | $31.806 | 10% | 0,629% | 6,288% | 62,882% | $159 | $477 |
| consulta 06/10/2026 23:36 UTC | pumpswap `BbcGFVN…gNRe` | $2.347 | 10% | 8,523% | 85,226% | 852,261% | $12 | $35 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump`
5. Configurar el slippage: 10% (liquidez $2.347, consulta 06/10/2026 23:36 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump) y el par en DexScreener (https://dexscreener.com/solana/BbcGFVN7cuZhjnSgZXZ45UPkxkW98zPZC66Z9xAmgNRe); mint authority / freeze authority: revocada / revocada · holders 79 · top-10 100,00% (consulta 06/10/2026 23:36 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump
- Par en DexScreener: https://dexscreener.com/solana/BbcGFVN7cuZhjnSgZXZ45UPkxkW98zPZC66Z9xAmgNRe
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 79 · top-10 100,00% (consulta 06/10/2026 23:36 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Condo / CONDO | registro de la detección (pumpportal_live) |
| Mint / contrato | `2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BbcGFVN7cuZhjnSgZXZ45UPkxkW98zPZC66Z9xAmgNRe` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 23:36 UTC) |
| Deployer | `CSnH16ESkFBrQH2K8cv4LDWokHjZjHMRD83ANTxcar3M` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 23:05 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,7 min / 10,7 min / 30,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 23:36 UTC |
| Holders / top-10 | 79 / 100,00% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 23:36 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 23:36 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 23:36 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BbcGFVN7cuZhjnSgZXZ45UPkxkW98zPZC66Z9xAmgNRe · Solscan: https://solscan.io/token/2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump · pump.fun: https://pump.fun/coin/2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump · web / Telegram / X: no publicados en DexScreener | consulta 06/10/2026 23:36 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 23:36 UTC)
- **Historia:**
  - Par creado el 06/10/2026 23:05 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 23:16 UTC, con el par a 10,7 min de creado: precio $0,0001342, mcap $134.294, liquidez $31.806.
  - Velas de 1 h de GeckoTerminal (1, desde 06/10/2026 23:00 UTC): apertura $0,00006493 · máximo $0,0001692 (06/10/2026 23:00 UTC) · mínimo $0,000002293 (06/10/2026 23:00 UTC) · último cierre $0,000002322.
  - En la consulta 06/10/2026 23:36 UTC: precio $0,000002322, liquidez $2.347, FDV $2.322.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 23:16 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001342 |
| Liquidez | $31.806 |
| MCap | $134.294 |
| Volumen 24 h | $58.115 |
| Cambio 24 h | +166% |
| Cambio m5 / h1 | +62,6% / +166,0% |
| Volumen m5 / h1 | $19.417 / $58.115 |
| Trades m5 (compras / ventas) | 755 / 280 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 51; motivos sin regla: young-0.4 · edad 10.7 min · pesos info 60 / estructura 20 / precio 20 · info 20.2 · estructura 17.7 · precio/volumen 12.6 · cobertura 93/100, [info] narrative_wave: ola 'condo': 13 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 33 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1865 · top-10 27.4 % → +4.8, [estructura] dev_wallet: creador compró 2.1 % del supply → +2.4, [estructura] holder_to_txn_ratio: holders/txns 1865/3279 = 0.57 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×4.0 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 73% en 5 min vs 68% en 1 h (s 0.25), [precio/volumen] liquidity_inflow: liquidez +77% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 595→1865 (+105.8/min) · top10 41.2%→27.4% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=31805.59, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 51 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T23:16:14+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen decente, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 21 de 17.226 tokens analizados (0,12%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 23:16 UTC, hasta 08/10/2026 23:16 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +62,6% · h1 +166,0% · h24 +166% · volumen m5/h1 0,33 · edad del par 10,7 min.
- **Precio de entrada** (alerta): $0,0001342.
- **Consulta 06/10/2026 23:36 UTC:** $0,000002322 (-98,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump_2026-10-06_231614.json` · blob `3fe218162a33872964d4c450f2e798cbca340674` · commit `e3df118` (2026-10-06T23:29:41Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_231614`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump · registro · 06/10/2026 23:16 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump · HTTP 200 · 06/10/2026 23:36 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump/report · HTTP 200 · 06/10/2026 23:36 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump · HTTP 200 · 06/10/2026 23:36 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BbcGFVN7cuZhjnSgZXZ45UPkxkW98zPZC66Z9xAmgNRe/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 23:36 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump · HTTP 404 · 06/10/2026 23:36 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=CONDOUSDT · HTTP 400 · 06/10/2026 23:36 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/CONDO-USD · HTTP 404 · 06/10/2026 23:36 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.347 vs $2.347 → 0,00%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002322 vs $0,000002322 → 0,00%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump_2026-10-06_231614.json',encoding='utf-8'));d=d.get('2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump',d);p=mock.patch('time.time',return_value=1791328574);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2zCjX1tfoHEAiEHQ76EGUoM1aghEgnb27LLMiNX3pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 23:36 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `b83ec3169cd340ee…`
