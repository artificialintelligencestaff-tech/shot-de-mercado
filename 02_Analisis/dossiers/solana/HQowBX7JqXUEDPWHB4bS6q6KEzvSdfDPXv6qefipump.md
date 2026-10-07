# United States Dividend Fund (USDF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,8114 · liquidez $2.597.814 · mcap $811.445.281 (al detectar)  
Detectado el 07/10/2026 09:41 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 09/10/2026 09:41 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir USDF

Estudio de cómo se adquiere USDF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/10/2026 09:58 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/10/2026 09:41 UTC | pumpswap `FL5gakw…31c6` | $2.597.814 | 1% | 0,008% | 0,077% | 0,770% | $12.989 | $38.967 |
| consulta 07/10/2026 09:58 UTC | pumpswap `FL5gakw…31c6` | $2.610.023 | 1% | 0,008% | 0,077% | 0,766% | $13.050 | $39.150 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump`
5. Configurar el slippage: 1% (liquidez $2.610.023, consulta 07/10/2026 09:58 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump) y el par en DexScreener (https://dexscreener.com/solana/FL5gakwfZqwgQMoW3qWa8U3y4Z8GQPQuvLjEdphF31c6); mint authority / freeze authority: revocada / revocada · holders 3.104 · top-10 0,90% (consulta 07/10/2026 09:58 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump
- Par en DexScreener: https://dexscreener.com/solana/FL5gakwfZqwgQMoW3qWa8U3y4Z8GQPQuvLjEdphF31c6
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.104 · top-10 0,90% (consulta 07/10/2026 09:58 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | United States Dividend Fund / USDF | registro de la detección (trending) |
| Mint / contrato | `HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `FL5gakwfZqwgQMoW3qWa8U3y4Z8GQPQuvLjEdphF31c6` | DexScreener, al detectar (2 par(es) en la consulta 07/10/2026 09:58 UTC) |
| Deployer | `Fh3rFz75XJq9jZ8s8HnwxNEmohCh4cro4RQQgq9iPFnF` | RugCheck `creator` |
| Par creado | 07/10/2026 08:22 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 78,6 min / 78,6 min / 95,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/10/2026 09:58 UTC |
| Holders / top-10 | 3.104 / 0,90% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/10/2026 09:58 UTC |
| Holders efectivos del top-10 | 5,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/10/2026 09:58 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 07/10/2026 09:58 UTC |
| Links | DexScreener: https://dexscreener.com/solana/FL5gakwfZqwgQMoW3qWa8U3y4Z8GQPQuvLjEdphF31c6 · Solscan: https://solscan.io/token/HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump · pump.fun: https://pump.fun/coin/HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump · web / Telegram / X: no publicados en DexScreener | consulta 07/10/2026 09:58 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/10/2026 09:58 UTC)
- **Historia:**
  - Par creado el 07/10/2026 08:22 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/10/2026 09:41 UTC, con el par a 78,6 min de creado: precio $0,8114, mcap $811.445.281, liquidez $2.597.814.
  - Velas de 1 h de GeckoTerminal (2, desde 07/10/2026 08:00 UTC): apertura $0,00004928 · máximo $0,8254 (07/10/2026 09:00 UTC) · mínimo $0,00004928 (07/10/2026 08:00 UTC) · último cierre $0,8204.
  - En la consulta 07/10/2026 09:58 UTC: precio $0,8205, liquidez $2.610.023, FDV $820.584.689.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/10/2026 09:41 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,8114 |
| Liquidez | $2.597.814 |
| MCap | $811.445.281 |
| Volumen 24 h | $2.741.730 |
| Cambio 24 h | +1.648.803% |
| Cambio m5 / h1 | -0,1% / +17,1% |
| Volumen m5 / h1 | $119.560 / $1.342.405 |
| Trades m5 (compras / ventas) | 444 / 152 |
| Edad del par | 78,6 min |
| Score del feed (WS) | 85 |

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

Desglose no reproducible desde los motivos registrados (suma 88 vs score 100; motivos sin regla: score de detección 100 (script_82, hace 2 min) > re-score 88: vale el de detección (paridad con script_97)): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-07T09:41:19+00:00, sin estado previo): **88** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 27 de 18.298 tokens analizados (0,15%) quedan ≥ 56. Con score 88, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/10/2026 09:41 UTC, hasta 09/10/2026 09:41 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -0,1% · h1 +17,1% · h24 +1.648.803% · volumen m5/h1 0,09 · edad del par 78,6 min.
- **Precio de entrada** (alerta): $0,8114.
- **Consulta 07/10/2026 09:58 UTC:** $0,8205 (+1,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump_2026-10-07_094119.json` · blob `504666293fee10ac6f20fdb02ee646fa1873cd25` · commit `9d2fa31` (2026-10-07T09:52:17Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-07_093431.json` · blob `0ca5f44d2cb005906f513551b0e8c66842cd1b07` · commit `9d2fa31` (2026-10-07T09:52:17Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-07_094119`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump · registro · 07/10/2026 09:41 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump · HTTP 200 · 07/10/2026 09:58 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump/report · HTTP 200 · 07/10/2026 09:58 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump · HTTP 200 · 07/10/2026 09:58 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/FL5gakwfZqwgQMoW3qWa8U3y4Z8GQPQuvLjEdphF31c6/ohlcv/hour?limit=1000 · HTTP 200 · 07/10/2026 09:58 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump · HTTP 404 · 07/10/2026 09:58 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=USDFUSDT · HTTP 400 · 07/10/2026 09:58 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/USDF-USD · HTTP 404 · 07/10/2026 09:58 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.610.023 vs $2.610.417 → 0,02%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,8205 vs $0,8204 → 0,01%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump_2026-10-07_094119.json',encoding='utf-8'));d=d.get('HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump',d);p=mock.patch('time.time',return_value=1791366079);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HQowBX7JqXUEDPWHB4bS6q6KEzvSdfDPXv6qefipump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/10/2026 09:58 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `038b19811ff32c6d…`
