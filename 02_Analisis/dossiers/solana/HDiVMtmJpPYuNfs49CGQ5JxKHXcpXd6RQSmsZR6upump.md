# Sundown Gulch ($GULCH) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00005307 · liquidez $18.471 · mcap $52.963 (al detectar)  
Detectado el 09/10/2026 16:29 UTC por: young-0.4 · edad 11.8 min · pesos info 59 / estructura 20 / precio 20 · info 14.8 · estructura 14.0 · precio/volumen 11.0 · cobertura 84/100, [info] narrative_wave: ola 'sundown': 8 lanzamientos más en 1 h → +14.8, [estructura] bonding_progress: graduado (pumpswap) → +9.8 (score 40, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 11/10/2026 16:29 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir $GULCH

Estudio de cómo se adquiere $GULCH, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 09/10/2026 16:40 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 09/10/2026 16:29 UTC | pumpswap `6eqs6T7…H87M` | $18.471 | 10% | 1,083% | 10,828% | 108,279% | $92 | $277 |
| consulta 09/10/2026 16:40 UTC | pumpswap `6eqs6T7…H87M` | $24.394 | 10% | 0,820% | 8,199% | 81,987% | $122 | $366 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump`
5. Configurar el slippage: 10% (liquidez $24.394, consulta 09/10/2026 16:40 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump) y el par en DexScreener (https://dexscreener.com/solana/6eqs6T7bPdRS2K8aku96KejCz7TwxYPvwubYRaxeH87M); mint authority / freeze authority: revocada / revocada · holders 995 · top-10 42,69% (consulta 09/10/2026 16:40 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump
- Par en DexScreener: https://dexscreener.com/solana/6eqs6T7bPdRS2K8aku96KejCz7TwxYPvwubYRaxeH87M
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 995 · top-10 42,69% (consulta 09/10/2026 16:40 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Sundown Gulch / $GULCH | registro de la detección (pumpportal_live) |
| Mint / contrato | `HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6eqs6T7bPdRS2K8aku96KejCz7TwxYPvwubYRaxeH87M` | DexScreener, al detectar (2 par(es) en la consulta 09/10/2026 16:40 UTC) |
| Deployer | `GHXQLmuDn9MEPL5i1G2shaFS5hZ3Ncsuq2RRK9FdJivM` | PumpPortal (evento create), al detectar |
| Par creado | 09/10/2026 16:17 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,8 min / 11,8 min / 22,5 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 09/10/2026 16:40 UTC |
| Holders / top-10 | 995 / 42,69% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 09/10/2026 16:40 UTC |
| Holders efectivos del top-10 | 6,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 09/10/2026 16:40 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 09/10/2026 16:40 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6eqs6T7bPdRS2K8aku96KejCz7TwxYPvwubYRaxeH87M · Solscan: https://solscan.io/token/HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump · pump.fun: https://pump.fun/coin/HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump · web / Telegram / X: no publicados en DexScreener | consulta 09/10/2026 16:40 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 09/10/2026 16:40 UTC)
- **Historia:**
  - Par creado el 09/10/2026 16:17 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 09/10/2026 16:29 UTC, con el par a 11,8 min de creado: precio $0,00005307, mcap $52.963, liquidez $18.471.
  - Velas de 1 h de GeckoTerminal (1, desde 09/10/2026 16:00 UTC): apertura $0,00003898 · máximo $0,0001441 (09/10/2026 16:00 UTC) · mínimo $0,00002112 (09/10/2026 16:00 UTC) · último cierre $0,0001018.
  - En la consulta 09/10/2026 16:40 UTC: precio $0,00008682, liquidez $24.394, FDV $86.650.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 09/10/2026 16:29 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00005307 |
| Liquidez | $18.471 |
| MCap | $52.963 |
| Volumen 24 h | $79.387 |
| Cambio 24 h | +23% |
| Cambio m5 / h1 | +2,6% / +22,5% |
| Volumen m5 / h1 | $23.014 / $79.387 |
| Trades m5 (compras / ventas) | 231 / 113 |
| Edad del par | 11,8 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 40; motivos sin regla: young-0.4 · edad 11.8 min · pesos info 59 / estructura 20 / precio 20 · info 14.8 · estructura 14.0 · precio/volumen 11.0 · cobertura 84/100, [info] narrative_wave: ola 'sundown': 8 lanzamientos más en 1 h → +14.8, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 675 · top-10 46.9 % → +2.5, [estructura] dev_wallet: creador compró 6.9 % del supply → +0.9, [estructura] holder_to_txn_ratio: holders/txns 675/1218 = 0.55 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×3.5 la tasa horaria (s 0.79), [precio/volumen] buy_pressure_shift: compras 67% en 5 min vs 63% en 1 h (s 0.20), [precio/volumen] quiet_accumulation: precio quieto (m5 +2.6%) con vol ×3.5 y compras 67% (s 0.55), [precio/volumen] holder_accumulation: holders 512→675 (+27.2/min) · top10 48.8%→46.9% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=18470.79, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 40 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-09T16:29:28+00:00, sin estado previo): **25** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen decente, Liquidez baja, Subida 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 40 de 25.090 tokens analizados (0,16%) quedan ≥ 56. Con score 25, este activo queda en el percentil 97,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 09/10/2026 16:29 UTC, hasta 11/10/2026 16:29 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +2,6% · h1 +22,5% · h24 +23% · volumen m5/h1 0,29 · edad del par 11,8 min.
- **Precio de entrada** (alerta): $0,00005307.
- **Consulta 09/10/2026 16:40 UTC:** $0,00008682 (+63,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump_2026-10-09_162928.json` · blob `44daf269a901449e02edcd6620b7d10d4aa401a5` · commit `47acafb` (2026-10-09T16:33:47Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-09_162928`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump · registro · 09/10/2026 16:29 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump · HTTP 200 · 09/10/2026 16:40 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump/report · HTTP 200 · 09/10/2026 16:40 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump · HTTP 200 · 09/10/2026 16:40 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6eqs6T7bPdRS2K8aku96KejCz7TwxYPvwubYRaxeH87M/ohlcv/hour?limit=1000 · HTTP 200 · 09/10/2026 16:40 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump · HTTP 404 · 09/10/2026 16:40 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $24.394 vs $24.173 → 0,91%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00008682 vs $0,0001018 → 14,71%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump_2026-10-09_162928.json',encoding='utf-8'));d=d.get('HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump',d);p=mock.patch('time.time',return_value=1791563368);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HDiVMtmJpPYuNfs49CGQ5JxKHXcpXd6RQSmsZR6upump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 09/10/2026 16:40 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `d91334d27b874b83…`
