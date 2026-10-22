# Capycoin (CAPY) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00008743 · liquidez $24.973 · mcap $87.437 (al detectar)  
Detectado el 22/10/2026 08:21 UTC por: young-0.4 · edad 14.9 min · pesos info 58 / estructura 21 / precio 21 · info 19.8 · estructura 13.3 · precio/volumen 9.6 · cobertura 94/100, [info] narrative_wave: ola 'capycoin': 8 lanzamientos más en 1 h → +14.4, [info] metadata_socials: enlaces ['twitter'] · descripción 29 caracteres → +2.6 (score 43, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 24/10/2026 08:21 UTC (< 48 h) · vigente: quedan 46,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir CAPY

Estudio de cómo se adquiere CAPY, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 22/10/2026 09:31 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 22/10/2026 08:21 UTC | pumpswap `675q1ik…8HyP` | $24.973 | 10% | 0,801% | 8,009% | 80,086% | $125 | $375 |
| consulta 22/10/2026 09:31 UTC | pumpswap `675q1ik…8HyP` | $14.273 | 10% | 1,401% | 14,012% | 140,125% | $71 | $214 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump`
5. Configurar el slippage: 10% (liquidez $14.273, consulta 22/10/2026 09:31 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump) y el par en DexScreener (https://dexscreener.com/solana/675q1ikTQQ4ijHBvSgHVbC2CrEPCjRDuEQ3yDtiU8HyP); mint authority / freeze authority: revocada / revocada · holders 2.153 · top-10 48,58% (consulta 22/10/2026 09:31 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump
- Par en DexScreener: https://dexscreener.com/solana/675q1ikTQQ4ijHBvSgHVbC2CrEPCjRDuEQ3yDtiU8HyP
- Página del lanzamiento (pump.fun): https://pump.fun/coin/G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.153 · top-10 48,58% (consulta 22/10/2026 09:31 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Capycoin / CAPY | registro de la detección (pumpportal_live) |
| Mint / contrato | `G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `675q1ikTQQ4ijHBvSgHVbC2CrEPCjRDuEQ3yDtiU8HyP` | DexScreener, al detectar (6 par(es) en la consulta 22/10/2026 09:31 UTC) |
| Deployer | `8AcZBvDXSwayFvAy8sb5ZD3PwqVHbnwNb2F3Fp2pdQmt` | PumpPortal (evento create), al detectar |
| Par creado | 22/10/2026 08:06 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 14,9 min / 14,9 min / 85,2 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 22/10/2026 09:31 UTC |
| Holders / top-10 | 2.153 / 48,58% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 22/10/2026 09:31 UTC |
| Holders efectivos del top-10 | 3,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 22/10/2026 09:31 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 22/10/2026 09:31 UTC |
| Links | DexScreener: https://dexscreener.com/solana/675q1ikTQQ4ijHBvSgHVbC2CrEPCjRDuEQ3yDtiU8HyP · Solscan: https://solscan.io/token/G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump · pump.fun: https://pump.fun/coin/G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump · twitter: https://x.com/cremieuxrecueil/status/2112720873442664756?s=46 | consulta 22/10/2026 09:31 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 22/10/2026 09:31 UTC)
- **Historia:**
  - Par creado el 22/10/2026 08:06 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 22/10/2026 08:21 UTC, con el par a 14,9 min de creado: precio $0,00008743, mcap $87.437, liquidez $24.973.
  - Velas de 1 h de GeckoTerminal (2, desde 22/10/2026 08:00 UTC): apertura $0,00004333 · máximo $0,0001259 (22/10/2026 08:00 UTC) · mínimo $0,00002637 (22/10/2026 08:00 UTC) · último cierre $0,00003430.
  - En la consulta 22/10/2026 09:31 UTC: precio $0,00003226, liquidez $14.273, FDV $31.016.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 22/10/2026 08:21 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00008743 |
| Liquidez | $24.973 |
| MCap | $87.437 |
| Volumen 24 h | $233.739 |
| Cambio 24 h | +100% |
| Cambio m5 / h1 | +41,7% / +100,0% |
| Volumen m5 / h1 | $65.236 / $233.739 |
| Trades m5 (compras / ventas) | 769 / 578 |
| Edad del par | 14,9 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 43; motivos sin regla: young-0.4 · edad 14.9 min · pesos info 58 / estructura 21 / precio 21 · info 19.8 · estructura 13.3 · precio/volumen 9.6 · cobertura 94/100, [info] narrative_wave: ola 'capycoin': 8 lanzamientos más en 1 h → +14.4, [info] metadata_socials: enlaces ['twitter'] · descripción 29 caracteres → +2.6, [info] dex_profile: perfil pago en DexScreener → +2.9, [estructura] bonding_progress: graduado (pumpswap) → +10.2, [estructura] holders_struct: holders 1350 · top-10 39.9 % → +2.5, [estructura] dev_wallet: creador compró 9.6 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1350/4953 = 0.27 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×3.3 la tasa horaria (s 0.74), [precio/volumen] buy_pressure_shift: compras 57% en 5 min vs 57% en 1 h (s 0.02), [precio/volumen] liquidity_inflow: liquidez +18% en 8 min (s 0.58), [precio/volumen] holder_accumulation: holders 1007→1350 (+57.2/min) · top10 45.3%→39.9% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=24973.0, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 43 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-22T08:21:03+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 74 de 43.800 tokens analizados (0,17%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 22/10/2026 08:21 UTC, hasta 24/10/2026 08:21 UTC · vigente: quedan 46,8 h.
- **Aceleración al detectar:** cambio m5 +41,7% · h1 +100,0% · h24 +100% · volumen m5/h1 0,28 · edad del par 14,9 min.
- **Precio de entrada** (alerta): $0,00008743.
- **Consulta 22/10/2026 09:31 UTC:** $0,00003226 (-63,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump_2026-10-22_082103.json` · blob `5a18251bbccd36c3fdad0e5b5b9d08ecc7f27cae` · commit `12673c8` (2026-10-22T09:22:58Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-22_082103`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump · registro · 22/10/2026 08:21 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump · HTTP 200 · 22/10/2026 09:31 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump/report · HTTP 200 · 22/10/2026 09:31 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump · HTTP 200 · 22/10/2026 09:31 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/675q1ikTQQ4ijHBvSgHVbC2CrEPCjRDuEQ3yDtiU8HyP/ohlcv/hour?limit=1000 · HTTP 200 · 22/10/2026 09:31 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump · HTTP 404 · 22/10/2026 09:31 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=CAPYUSDT · HTTP 400 · 22/10/2026 09:31 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/CAPY-USD · HTTP 404 · 22/10/2026 09:31 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $14.273 vs $14.308 → 0,24%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00003226 vs $0,00003430 → 5,95%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump_2026-10-22_082103.json',encoding='utf-8'));d=d.get('G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump',d);p=mock.patch('time.time',return_value=1792657263);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint G9xrNbBBYBsGFL2XiHdXDy56gWfAMnefD6L8ZKHLpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 22/10/2026 09:31 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `de802eca6bc82323…`
