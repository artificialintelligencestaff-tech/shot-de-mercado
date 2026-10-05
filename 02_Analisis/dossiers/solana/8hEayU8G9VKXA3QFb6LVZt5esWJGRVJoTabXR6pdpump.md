# PUMP IS LIFE (PUMPLIFE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001519 · liquidez $33.800 · mcap $151.747 (al detectar)  
Detectado el 05/10/2026 17:50 UTC por: young-0.4 · edad 10.3 min · pesos info 60 / estructura 20 / precio 20 · info 17.6 · estructura 14.4 · precio/volumen 12.7 · cobertura 93/100, [info] narrative_wave: ola 'life': 11 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.7 (score 45, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 07/10/2026 17:50 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir PUMPLIFE

Estudio de cómo se adquiere PUMPLIFE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 05/10/2026 18:15 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 05/10/2026 17:50 UTC | pumpswap `Hjr4kA2…qC8d` | $33.800 | 10% | 0,592% | 5,917% | 59,171% | $169 | $507 |
| consulta 05/10/2026 18:14 UTC | pumpswap `Hjr4kA2…qC8d` | $2.324 | 10% | 8,607% | 86,066% | 860,663% | $12 | $35 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump`
5. Configurar el slippage: 10% (liquidez $2.324, consulta 05/10/2026 18:14 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump) y el par en DexScreener (https://dexscreener.com/solana/Hjr4kA2txKhPcMnTqAeKvJS5ExbtHmpV95biv6dPqC8d); mint authority / freeze authority: revocada / revocada · holders 65 · top-10 100,00% (consulta 05/10/2026 18:14 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump
- Par en DexScreener: https://dexscreener.com/solana/Hjr4kA2txKhPcMnTqAeKvJS5ExbtHmpV95biv6dPqC8d
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 65 · top-10 100,00% (consulta 05/10/2026 18:14 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | PUMP IS LIFE / PUMPLIFE | registro de la detección (pumpportal_live) |
| Mint / contrato | `8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Hjr4kA2txKhPcMnTqAeKvJS5ExbtHmpV95biv6dPqC8d` | DexScreener, al detectar (2 par(es) en la consulta 05/10/2026 18:14 UTC) |
| Deployer | `8Cr88QzHHGkP2byd1R3uSRGjYi5DokYeQPHNcg8xVSdc` | PumpPortal (evento create), al detectar |
| Par creado | 05/10/2026 17:40 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,3 min / 10,3 min / 34,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 05/10/2026 18:14 UTC |
| Holders / top-10 | 65 / 100,00% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 05/10/2026 18:14 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 05/10/2026 18:14 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 05/10/2026 18:14 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Hjr4kA2txKhPcMnTqAeKvJS5ExbtHmpV95biv6dPqC8d · Solscan: https://solscan.io/token/8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump · pump.fun: https://pump.fun/coin/8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump · web / Telegram / X: no publicados en DexScreener | consulta 05/10/2026 18:14 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 05/10/2026 18:14 UTC)
- **Historia:**
  - Par creado el 05/10/2026 17:40 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 05/10/2026 17:50 UTC, con el par a 10,3 min de creado: precio $0,0001519, mcap $151.747, liquidez $33.800.
  - Velas de 1 h de GeckoTerminal (2, desde 05/10/2026 17:00 UTC): apertura $0,00005061 · máximo $0,0001613 (05/10/2026 17:00 UTC) · mínimo $0,000002298 (05/10/2026 18:00 UTC) · último cierre $0,000002298.
  - En la consulta 05/10/2026 18:14 UTC: precio $0,000002299, liquidez $2.324, FDV $2.297.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 05/10/2026 17:50 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001519 |
| Liquidez | $33.800 |
| MCap | $151.747 |
| Volumen 24 h | $54.566 |
| Cambio 24 h | +204% |
| Cambio m5 / h1 | +87,6% / +204,0% |
| Volumen m5 / h1 | $26.385 / $54.566 |
| Trades m5 (compras / ventas) | 1.085 / 211 |
| Edad del par | 10,3 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 45; motivos sin regla: young-0.4 · edad 10.3 min · pesos info 60 / estructura 20 / precio 20 · info 17.6 · estructura 14.4 · precio/volumen 12.7 · cobertura 93/100, [info] narrative_wave: ola 'life': 11 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.7, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1572 · top-10 38.4 % → +2.4, [estructura] dev_wallet: creador compró 4.9 % del supply → +1.5, [estructura] holder_to_txn_ratio: holders/txns 1572/2445 = 0.64 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×5.8 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 84% en 5 min vs 78% en 1 h (s 0.30), [precio/volumen] liquidity_inflow: liquidez +76% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 518→1572 (+175.7/min) · top10 49.6%→38.4% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=33800.19, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=18270.86, score 45 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-05T17:50:33+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen decente, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 16 de 13.149 tokens analizados (0,12%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 05/10/2026 17:50 UTC, hasta 07/10/2026 17:50 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +87,6% · h1 +204,0% · h24 +204% · volumen m5/h1 0,48 · edad del par 10,3 min.
- **Precio de entrada** (alerta): $0,0001519.
- **Consulta 05/10/2026 18:14 UTC:** $0,000002299 (-98,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump_2026-10-05_175033.json` · blob `bc61de79b696cdc300ac3f29af6469adef598892` · commit `49d00f4` (2026-10-05T18:07:20Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-05_175033`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump · registro · 05/10/2026 17:50 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump · HTTP 200 · 05/10/2026 18:14 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump/report · HTTP 200 · 05/10/2026 18:14 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump · HTTP 200 · 05/10/2026 18:14 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Hjr4kA2txKhPcMnTqAeKvJS5ExbtHmpV95biv6dPqC8d/ohlcv/hour?limit=1000 · HTTP 200 · 05/10/2026 18:14 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump · HTTP 404 · 05/10/2026 18:14 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=PUMPLIFEUSDT · HTTP 400 · 05/10/2026 18:14 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/PUMPLIFE-USD · HTTP 404 · 05/10/2026 18:14 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.324 vs $2.324 → 0,01%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002299 vs $0,000002298 → 0,03%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump_2026-10-05_175033.json',encoding='utf-8'));d=d.get('8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump',d);p=mock.patch('time.time',return_value=1791222633);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8hEayU8G9VKXA3QFb6LVZt5esWJGRVJoTabXR6pdpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 05/10/2026 18:15 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `915b42a0cb15fcc3…`
