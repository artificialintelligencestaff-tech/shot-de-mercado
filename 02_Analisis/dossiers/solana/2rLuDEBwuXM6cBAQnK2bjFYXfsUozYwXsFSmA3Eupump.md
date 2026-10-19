# Rip Kim Jong-Un (김정은) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00007170 · liquidez $21.997 · mcap $71.703 (al detectar)  
Detectado el 19/10/2026 11:39 UTC por: young-0.4 · edad 11.4 min · pesos info 59 / estructura 20 / precio 20 · info 17.5 · estructura 15.6 · precio/volumen 10.2 · cobertura 93/100, [info] narrative_wave: ola 'kim': 43 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.6 (score 43, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 21/10/2026 11:39 UTC (< 48 h) · vigente: quedan 47,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir 김정은

Estudio de cómo se adquiere 김정은, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 19/10/2026 12:15 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 19/10/2026 11:39 UTC | pumpswap `HRZmPU1…pXaB` | $21.997 | 10% | 0,909% | 9,092% | 90,923% | $110 | $330 |
| consulta 19/10/2026 12:15 UTC | pumpswap `HRZmPU1…pXaB` | $12.021 | 10% | 1,664% | 16,637% | 166,370% | $60 | $180 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump`
5. Configurar el slippage: 10% (liquidez $12.021, consulta 19/10/2026 12:15 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump) y el par en DexScreener (https://dexscreener.com/solana/HRZmPU1pQP5fuMTjt6Ji44eXspqWRcKhitY2bnSTpXaB); mint authority / freeze authority: revocada / revocada · holders 3.272 · top-10 49,84% (consulta 19/10/2026 12:15 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump
- Par en DexScreener: https://dexscreener.com/solana/HRZmPU1pQP5fuMTjt6Ji44eXspqWRcKhitY2bnSTpXaB
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.272 · top-10 49,84% (consulta 19/10/2026 12:15 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Rip Kim Jong-Un / 김정은 | registro de la detección (pumpportal_live) |
| Mint / contrato | `2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HRZmPU1pQP5fuMTjt6Ji44eXspqWRcKhitY2bnSTpXaB` | DexScreener, al detectar (6 par(es) en la consulta 19/10/2026 12:15 UTC) |
| Deployer | `Aqje5DsN4u2PHmQxGF9PKfpsDGwQRCBhWeLKHCFhSMXk` | PumpPortal (evento create), al detectar |
| Par creado | 19/10/2026 11:28 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,4 min / 11,4 min / 47,5 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 19/10/2026 12:15 UTC |
| Holders / top-10 | 3.272 / 49,84% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 19/10/2026 12:15 UTC |
| Holders efectivos del top-10 | 2,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 19/10/2026 12:15 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 19/10/2026 12:15 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HRZmPU1pQP5fuMTjt6Ji44eXspqWRcKhitY2bnSTpXaB · Solscan: https://solscan.io/token/2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump · pump.fun: https://pump.fun/coin/2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump · twitter: https://twitter.com/dailystar/status/2112140024502235446 | consulta 19/10/2026 12:15 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 19/10/2026 12:15 UTC)
- **Historia:**
  - Par creado el 19/10/2026 11:28 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 19/10/2026 11:39 UTC, con el par a 11,4 min de creado: precio $0,00007170, mcap $71.703, liquidez $21.997.
  - Velas de 1 h de GeckoTerminal (2, desde 19/10/2026 11:00 UTC): apertura $0,00004129 · máximo $0,0001939 (19/10/2026 11:00 UTC) · mínimo $0,00002116 (19/10/2026 12:00 UTC) · último cierre $0,00002424.
  - En la consulta 19/10/2026 12:15 UTC: precio $0,00002362, liquidez $12.021, FDV $22.914.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 19/10/2026 11:39 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00007170 |
| Liquidez | $21.997 |
| MCap | $71.703 |
| Volumen 24 h | $433.403 |
| Cambio 24 h | +74% |
| Cambio m5 / h1 | -55,9% / +73,7% |
| Volumen m5 / h1 | $204.394 / $433.403 |
| Trades m5 (compras / ventas) | 2.327 / 2.094 |
| Edad del par | 11,4 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 43; motivos sin regla: young-0.4 · edad 11.4 min · pesos info 59 / estructura 20 / precio 20 · info 17.5 · estructura 15.6 · precio/volumen 10.2 · cobertura 93/100, [info] narrative_wave: ola 'kim': 43 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.6, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 2162 · top-10 27.9 % → +4.9, [estructura] dev_wallet: creador compró 8.3 % del supply → +0.5, [estructura] holder_to_txn_ratio: holders/txns 2162/9645 = 0.22 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×5.7 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 53% en 5 min vs 52% en 1 h (s 0.01), [precio/volumen] liquidity_inflow: liquidez +14% en 8 min (s 0.48), [precio/volumen] holder_accumulation: holders 1127→2162 (+172.5/min) · top10 41.2%→27.9% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=21996.56, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 43 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-19T11:39:43+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 67 de 40.740 tokens analizados (0,16%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 19/10/2026 11:39 UTC, hasta 21/10/2026 11:39 UTC · vigente: quedan 47,4 h.
- **Aceleración al detectar:** cambio m5 -55,9% · h1 +73,7% · h24 +74% · volumen m5/h1 0,47 · edad del par 11,4 min.
- **Precio de entrada** (alerta): $0,00007170.
- **Consulta 19/10/2026 12:15 UTC:** $0,00002362 (-67,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump_2026-10-19_113943.json` · blob `1ef287ffdec7f548603f1e6d5315956090928827` · commit `15a0e16` (2026-10-19T12:08:14Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-19_113943`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump · registro · 19/10/2026 11:39 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump · HTTP 200 · 19/10/2026 12:15 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump/report · HTTP 200 · 19/10/2026 12:15 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump · HTTP 200 · 19/10/2026 12:15 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HRZmPU1pQP5fuMTjt6Ji44eXspqWRcKhitY2bnSTpXaB/ohlcv/hour?limit=1000 · HTTP 200 · 19/10/2026 12:15 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump · HTTP 404 · 19/10/2026 12:15 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $12.021 vs $12.056 → 0,28%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00002362 vs $0,00002424 → 2,57%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump_2026-10-19_113943.json',encoding='utf-8'));d=d.get('2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump',d);p=mock.patch('time.time',return_value=1792409983);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2rLuDEBwuXM6cBAQnK2bjFYXfsUozYwXsFSmA3Eupump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 19/10/2026 12:15 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `eca70f53b5295383…`
