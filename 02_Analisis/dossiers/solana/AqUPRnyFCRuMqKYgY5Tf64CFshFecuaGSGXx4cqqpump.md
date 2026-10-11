# Artificial Internet Cat (9LIVES) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00008990 · liquidez $24.841 · mcap $89.904 (al detectar)  
Detectado el 11/10/2026 19:58 UTC por: young-0.4 · edad 11.3 min · pesos info 59 / estructura 20 / precio 20 · info 21.1 · estructura 17.0 · precio/volumen 11.5 · cobertura 84/100, [info] narrative_wave: ola 'cat': 5 lanzamientos más en 1 h → +9.3, [info] trending_match: 'cat' en trending #4 cat wif hood → +5.9 (score 50, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 13/10/2026 19:58 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir 9LIVES

Estudio de cómo se adquiere 9LIVES, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/10/2026 20:11 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 11/10/2026 19:58 UTC | pumpswap `ENtnEE6…eQJP` | $24.841 | 10% | 0,805% | 8,051% | 80,511% | $124 | $373 |
| consulta 11/10/2026 20:11 UTC | pumpswap `ENtnEE6…eQJP` | $27.348 | 10% | 0,731% | 7,313% | 73,132% | $137 | $410 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump`
5. Configurar el slippage: 10% (liquidez $27.348, consulta 11/10/2026 20:11 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump) y el par en DexScreener (https://dexscreener.com/solana/ENtnEE6cmK1nfqKd6keZe1eGL6HmRBqYVyXRsWcBeQJP); mint authority / freeze authority: revocada / revocada · holders 1.516 · top-10 22,67% (consulta 11/10/2026 20:11 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump
- Par en DexScreener: https://dexscreener.com/solana/ENtnEE6cmK1nfqKd6keZe1eGL6HmRBqYVyXRsWcBeQJP
- Página del lanzamiento (pump.fun): https://pump.fun/coin/AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.516 · top-10 22,67% (consulta 11/10/2026 20:11 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Artificial Internet Cat / 9LIVES | registro de la detección (pumpportal_live) |
| Mint / contrato | `AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `ENtnEE6cmK1nfqKd6keZe1eGL6HmRBqYVyXRsWcBeQJP` | DexScreener, al detectar (2 par(es) en la consulta 11/10/2026 20:11 UTC) |
| Deployer | `HttnA8EqThxT4n7G95Dweki84RXccTNEeAhdc1MbNQVd` | PumpPortal (evento create), al detectar |
| Par creado | 11/10/2026 19:47 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,3 min / 11,3 min / 24,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/10/2026 20:11 UTC |
| Holders / top-10 | 1.516 / 22,67% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/10/2026 20:11 UTC |
| Holders efectivos del top-10 | 2,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/10/2026 20:11 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 11/10/2026 20:11 UTC |
| Links | DexScreener: https://dexscreener.com/solana/ENtnEE6cmK1nfqKd6keZe1eGL6HmRBqYVyXRsWcBeQJP · Solscan: https://solscan.io/token/AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump · pump.fun: https://pump.fun/coin/AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump · web: https://artificialinternetcat.fun/ · twitter: https://x.com/9livesagent | consulta 11/10/2026 20:11 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/10/2026 20:11 UTC)
- **Historia:**
  - Par creado el 11/10/2026 19:47 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 11/10/2026 19:58 UTC, con el par a 11,3 min de creado: precio $0,00008990, mcap $89.904, liquidez $24.841.
  - Velas de 1 h de GeckoTerminal (2, desde 11/10/2026 19:00 UTC): apertura $0,00004676 · máximo $0,0001272 (11/10/2026 20:00 UTC) · mínimo $0,00003321 (11/10/2026 19:00 UTC) · último cierre $0,0001043.
  - En la consulta 11/10/2026 20:11 UTC: precio $0,0001042, liquidez $27.348, FDV $104.221.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 11/10/2026 19:58 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00008990 |
| Liquidez | $24.841 |
| MCap | $89.904 |
| Volumen 24 h | $103.963 |
| Cambio 24 h | +94% |
| Cambio m5 / h1 | +27,0% / +94,3% |
| Volumen m5 / h1 | $49.963 / $103.963 |
| Trades m5 (compras / ventas) | 1.517 / 707 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 50; motivos sin regla: young-0.4 · edad 11.3 min · pesos info 59 / estructura 20 / precio 20 · info 21.1 · estructura 17.0 · precio/volumen 11.5 · cobertura 84/100, [info] narrative_wave: ola 'cat': 5 lanzamientos más en 1 h → +9.3, [info] trending_match: 'cat' en trending #4 cat wif hood → +5.9, [info] dex_profile: perfil pago en DexScreener → +3.0, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 1105 · top-10 24.8 % → +4.9, [estructura] dev_wallet: creador compró 3.6 % del supply → +1.9, [estructura] holder_to_txn_ratio: holders/txns 1105/4007 = 0.28 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×5.8 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 68% en 5 min vs 67% en 1 h (s 0.07), [precio/volumen] liquidity_inflow: liquidez +24% en 8 min (s 0.81), [precio/volumen] holder_accumulation: holders 529→1105 (+96.0/min) · top10 30.5%→24.8% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=24841.2, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 50 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-11T19:58:40+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 50 de 29.929 tokens analizados (0,17%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 11/10/2026 19:58 UTC, hasta 13/10/2026 19:58 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +27,0% · h1 +94,3% · h24 +94% · volumen m5/h1 0,48 · edad del par 11,3 min.
- **Precio de entrada** (alerta): $0,00008990.
- **Consulta 11/10/2026 20:11 UTC:** $0,0001042 (+15,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump_2026-10-11_195840.json` · blob `46dba5880c8026979f8852339c0cfb386c930ffc` · commit `d8cdc15` (2026-10-11T20:03:58Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-11_195840`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump · registro · 11/10/2026 19:58 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump · HTTP 200 · 11/10/2026 20:11 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump/report · HTTP 200 · 11/10/2026 20:11 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump · HTTP 200 · 11/10/2026 20:11 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/ENtnEE6cmK1nfqKd6keZe1eGL6HmRBqYVyXRsWcBeQJP/ohlcv/hour?limit=1000 · HTTP 200 · 11/10/2026 20:11 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump · HTTP 404 · 11/10/2026 20:11 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=9LIVESUSDT · HTTP 400 · 11/10/2026 20:11 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/9LIVES-USD · HTTP 404 · 11/10/2026 20:11 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $27.348 vs $27.743 → 1,42%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001042 vs $0,0001043 → 0,08%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump_2026-10-11_195840.json',encoding='utf-8'));d=d.get('AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump',d);p=mock.patch('time.time',return_value=1791748720);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint AqUPRnyFCRuMqKYgY5Tf64CFshFecuaGSGXx4cqqpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/10/2026 20:11 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `39e9534429f0603c…`
