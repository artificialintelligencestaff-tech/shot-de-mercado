# Pet Rock (ROCK) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00006546 · liquidez $21.661 · mcap $65.369 (al detectar)  
Detectado el 06/10/2026 13:42 UTC por: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 17.6 · estructura 17.2 · precio/volumen 10.0 · cobertura 93/100, [info] narrative_wave: ola 'rock': 25 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.7 (score 45, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 08/10/2026 13:42 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ROCK

Estudio de cómo se adquiere ROCK, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 13:57 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 13:42 UTC | pumpswap `7dN3vWd…pfFu` | $21.661 | 10% | 0,923% | 9,233% | 92,332% | $108 | $325 |
| consulta 06/10/2026 13:57 UTC | pumpswap `7dN3vWd…pfFu` | $2.573 | 10% | 7,774% | 77,743% | 777,430% | $13 | $39 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump`
5. Configurar el slippage: 10% (liquidez $2.573, consulta 06/10/2026 13:57 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump) y el par en DexScreener (https://dexscreener.com/solana/7dN3vWdZs9dsMmVE83pVKLCva6a3MZgFfMEaBmKapfFu); mint authority / freeze authority: revocada / revocada · holders 222 · top-10 99,83% (consulta 06/10/2026 13:57 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump
- Par en DexScreener: https://dexscreener.com/solana/7dN3vWdZs9dsMmVE83pVKLCva6a3MZgFfMEaBmKapfFu
- Página del lanzamiento (pump.fun): https://pump.fun/coin/9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 222 · top-10 99,83% (consulta 06/10/2026 13:57 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Pet Rock / ROCK | registro de la detección (pumpportal_live) |
| Mint / contrato | `9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7dN3vWdZs9dsMmVE83pVKLCva6a3MZgFfMEaBmKapfFu` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 13:57 UTC) |
| Deployer | `5NP8E7NhDdg41RxmFcD4Nq7GhPifRRhoVwUi8XjpSm6b` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 13:32 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,4 min / 10,4 min / 25,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 13:57 UTC |
| Holders / top-10 | 222 / 99,83% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 13:57 UTC |
| Holders efectivos del top-10 | 1,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 13:57 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 13:57 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7dN3vWdZs9dsMmVE83pVKLCva6a3MZgFfMEaBmKapfFu · Solscan: https://solscan.io/token/9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump · pump.fun: https://pump.fun/coin/9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump · web / Telegram / X: no publicados en DexScreener | consulta 06/10/2026 13:57 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 13:57 UTC)
- **Historia:**
  - Par creado el 06/10/2026 13:32 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 13:42 UTC, con el par a 10,4 min de creado: precio $0,00006546, mcap $65.369, liquidez $21.661.
  - Velas de 1 h de GeckoTerminal (1, desde 06/10/2026 13:00 UTC): apertura $0,00005035 · máximo $0,0001067 (06/10/2026 13:00 UTC) · mínimo $0,000002401 (06/10/2026 13:00 UTC) · último cierre $0,000002542.
  - En la consulta 06/10/2026 13:57 UTC: precio $0,000002541, liquidez $2.573, FDV $2.538.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 13:42 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00006546 |
| Liquidez | $21.661 |
| MCap | $65.369 |
| Volumen 24 h | $125.253 |
| Cambio 24 h | +30% |
| Cambio m5 / h1 | +13,6% / +30,2% |
| Volumen m5 / h1 | $91.867 / $125.253 |
| Trades m5 (compras / ventas) | 1.989 / 504 |
| Edad del par | 10,4 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 45; motivos sin regla: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 17.6 · estructura 17.2 · precio/volumen 10.0 · cobertura 93/100, [info] narrative_wave: ola 'rock': 25 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.7, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 2121 · top-10 21.1 % → +4.8, [estructura] dev_wallet: creador compró 3.4 % del supply → +2.0, [estructura] holder_to_txn_ratio: holders/txns 2121/4743 = 0.45 → +0.7, [precio/volumen] volume_acceleration: vol 5 min ×8.8 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 80% en 5 min vs 77% en 1 h (s 0.15), [precio/volumen] liquidity_inflow: liquidez +10% en 8 min (s 0.34), [precio/volumen] holder_accumulation: holders 939→2121 (+98.5/min) · top10 39.7%→21.1% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=21661.05, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 45 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T13:42:38+00:00, sin estado previo): **35** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Subida 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 19 de 15.560 tokens analizados (0,12%) quedan ≥ 56. Con score 35, este activo queda en el percentil 98,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 13:42 UTC, hasta 08/10/2026 13:42 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +13,6% · h1 +30,2% · h24 +30% · volumen m5/h1 0,73 · edad del par 10,4 min.
- **Precio de entrada** (alerta): $0,00006546.
- **Consulta 06/10/2026 13:57 UTC:** $0,000002541 (-96,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump_2026-10-06_134238.json` · blob `d8788f90cd7926830dbf1950f9716b95635a3f91` · commit `736da8f` (2026-10-06T13:51:38Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_134238`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump · registro · 06/10/2026 13:42 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump · HTTP 200 · 06/10/2026 13:57 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump/report · HTTP 200 · 06/10/2026 13:57 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump · HTTP 200 · 06/10/2026 13:57 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7dN3vWdZs9dsMmVE83pVKLCva6a3MZgFfMEaBmKapfFu/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 13:57 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump · HTTP 404 · 06/10/2026 13:57 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ROCKUSDT · HTTP 400 · 06/10/2026 13:57 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ROCK-USD · HTTP 404 · 06/10/2026 13:57 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.573 vs $2.575 → 0,08%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002541 vs $0,000002542 → 0,04%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump_2026-10-06_134238.json',encoding='utf-8'));d=d.get('9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump',d);p=mock.patch('time.time',return_value=1791294158);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 9jhvNe7AdozaRTdVDy1AsyMWqitbkoKNeZhBistZpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 13:57 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `e9fa964d49d29650…`
