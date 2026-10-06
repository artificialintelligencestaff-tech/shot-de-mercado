# Generational Bottom (Bottom) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0004222 · liquidez $60.125 · mcap $422.202 (al detectar)  
Detectado el 06/10/2026 02:42 UTC por: young-0.4 · edad 14.2 min · pesos info 58 / estructura 21 / precio 21 · info 13.0 · estructura 17.9 · precio/volumen 12.2 · cobertura 84/100, [info] narrative_wave: ola 'generational': 4 lanzamientos más en 1 h → +7.2, [info] dex_profile: perfil pago en DexScreener → +2.9 (score 43, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 08/10/2026 02:42 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Bottom

Estudio de cómo se adquiere Bottom, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 02:55 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 02:42 UTC | pumpswap `B5ZN14A…a7P6` | $60.125 | 5% | 0,333% | 3,326% | 33,264% | $301 | $902 |
| consulta 06/10/2026 02:55 UTC | pumpswap `B5ZN14A…a7P6` | $3.056 | 10% | 6,544% | 65,438% | 654,382% | $15 | $46 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump`
5. Configurar el slippage: 10% (liquidez $3.056, consulta 06/10/2026 02:55 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump) y el par en DexScreener (https://dexscreener.com/solana/B5ZN14AFtP2eFt6R4gK9wNVGfcKNXWcEukSBfH3ha7P6); mint authority / freeze authority: revocada / revocada · holders 1.280 · top-10 98,02% (consulta 06/10/2026 02:55 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump
- Par en DexScreener: https://dexscreener.com/solana/B5ZN14AFtP2eFt6R4gK9wNVGfcKNXWcEukSBfH3ha7P6
- Página del lanzamiento (pump.fun): https://pump.fun/coin/9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.280 · top-10 98,02% (consulta 06/10/2026 02:55 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Generational Bottom / Bottom | registro de la detección (pumpportal_live) |
| Mint / contrato | `9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `B5ZN14AFtP2eFt6R4gK9wNVGfcKNXWcEukSBfH3ha7P6` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 02:55 UTC) |
| Deployer | `GfM7awjAogSUJC3app4jLJaAZX2GyHJ8nrViY5wYS1op` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 02:28 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 14,2 min / 14,2 min / 27,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 02:55 UTC |
| Holders / top-10 | 1.280 / 98,02% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 02:55 UTC |
| Holders efectivos del top-10 | 1,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 02:55 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 02:55 UTC |
| Links | DexScreener: https://dexscreener.com/solana/B5ZN14AFtP2eFt6R4gK9wNVGfcKNXWcEukSBfH3ha7P6 · Solscan: https://solscan.io/token/9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump · pump.fun: https://pump.fun/coin/9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump · web: https://rirally.com · twitter: https://x.com/search?q=$Bottom | consulta 06/10/2026 02:55 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 02:55 UTC)
- **Historia:**
  - Par creado el 06/10/2026 02:28 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 02:42 UTC, con el par a 14,2 min de creado: precio $0,0004222, mcap $422.202, liquidez $60.125.
  - Velas de 1 h de GeckoTerminal (1, desde 06/10/2026 02:00 UTC): apertura $0,00005013 · máximo $0,0005646 (06/10/2026 02:00 UTC) · mínimo $0,000002796 (06/10/2026 02:00 UTC) · último cierre $0,000002851.
  - En la consulta 06/10/2026 02:55 UTC: precio $0,000002853, liquidez $3.056, FDV $2.854.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 02:42 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0004222 |
| Liquidez | $60.125 |
| MCap | $422.202 |
| Volumen 24 h | $856.838 |
| Cambio 24 h | +742% |
| Cambio m5 / h1 | -16,1% / +742,0% |
| Volumen m5 / h1 | $272.095 / $856.838 |
| Trades m5 (compras / ventas) | 1.329 / 879 |
| Edad del par | 14,2 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 43; motivos sin regla: young-0.4 · edad 14.2 min · pesos info 58 / estructura 21 / precio 21 · info 13.0 · estructura 17.9 · precio/volumen 12.2 · cobertura 84/100, [info] narrative_wave: ola 'generational': 4 lanzamientos más en 1 h → +7.2, [info] dex_profile: perfil pago en DexScreener → +2.9, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +2.9, [estructura] bonding_progress: graduado (pumpswap) → +10.1, [estructura] holders_struct: holders 3162 · top-10 8.8 % → +5.1, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.1, [estructura] holder_to_txn_ratio: holders/txns 3162/7631 = 0.41 → +0.7, [precio/volumen] volume_acceleration: vol 5 min ×3.8 la tasa horaria (s 0.92), [precio/volumen] buy_pressure_shift: compras 60% en 5 min vs 58% en 1 h (s 0.10), [precio/volumen] liquidity_inflow: liquidez +83% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 2002→3162 (+193.3/min) · top10 9.3%→8.8% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=60124.62, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 43 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T02:42:26+00:00, sin estado previo): **50** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=14.2% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 17 de 13.973 tokens analizados (0,12%) quedan ≥ 56. Con score 50, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 02:42 UTC, hasta 08/10/2026 02:42 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -16,1% · h1 +742,0% · h24 +742% · volumen m5/h1 0,32 · edad del par 14,2 min.
- **Precio de entrada** (alerta): $0,0004222.
- **Consulta 06/10/2026 02:55 UTC:** $0,000002853 (-99,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump_2026-10-06_024226.json` · blob `43231da764194c6602ff64287f3fc196e7c32bf3` · commit `f80fb7c` (2026-10-06T02:49:43Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_024226`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump · registro · 06/10/2026 02:42 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump · HTTP 200 · 06/10/2026 02:55 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump/report · HTTP 200 · 06/10/2026 02:55 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump · HTTP 200 · 06/10/2026 02:55 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/B5ZN14AFtP2eFt6R4gK9wNVGfcKNXWcEukSBfH3ha7P6/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 02:55 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump · HTTP 404 · 06/10/2026 02:55 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BOTTOMUSDT · HTTP 400 · 06/10/2026 02:55 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BOTTOM-USD · HTTP 404 · 06/10/2026 02:55 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.056 vs $3.057 → 0,01%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002853 vs $0,000002851 → 0,07%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump_2026-10-06_024226.json',encoding='utf-8'));d=d.get('9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump',d);p=mock.patch('time.time',return_value=1791254546);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 9NEGAPZd4NzWbC24im1jY5BtDYFUq9ZVLpDvims2pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 02:55 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `9b3af8e3abb9291b…`
