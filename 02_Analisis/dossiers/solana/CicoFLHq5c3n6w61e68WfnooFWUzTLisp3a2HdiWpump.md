# Energy Coin (ENERGY) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00004973 · liquidez $17.934 · mcap $49.735 (al detectar)  
Detectado el 20/10/2026 19:45 UTC por: young-0.4 · edad 11.8 min · pesos info 59 / estructura 20 / precio 20 · info 23.0 · estructura 12.8 · precio/volumen 5.9 · cobertura 93/100, [info] narrative_wave: ola 'energy': 30 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 42, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 22/10/2026 19:45 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ENERGY

Estudio de cómo se adquiere ENERGY, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 20/10/2026 20:11 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 20/10/2026 19:45 UTC | pumpswap `EvdxxQA…ADxp` | $17.934 | 10% | 1,115% | 11,152% | 111,522% | $90 | $269 |
| consulta 20/10/2026 20:11 UTC | pumpswap `EvdxxQA…ADxp` | $27.120 | 10% | 0,737% | 7,375% | 73,746% | $136 | $407 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump`
5. Configurar el slippage: 10% (liquidez $27.120, consulta 20/10/2026 20:11 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump) y el par en DexScreener (https://dexscreener.com/solana/EvdxxQA1TPuANNW2EMMHsJ36G9QumjHHCL8nui9SADxp); mint authority / freeze authority: revocada / revocada · holders 1.795 · top-10 39,23% (consulta 20/10/2026 20:11 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump
- Par en DexScreener: https://dexscreener.com/solana/EvdxxQA1TPuANNW2EMMHsJ36G9QumjHHCL8nui9SADxp
- Página del lanzamiento (pump.fun): https://pump.fun/coin/CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.795 · top-10 39,23% (consulta 20/10/2026 20:11 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Energy Coin / ENERGY | registro de la detección (pumpportal_live) |
| Mint / contrato | `CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `EvdxxQA1TPuANNW2EMMHsJ36G9QumjHHCL8nui9SADxp` | DexScreener, al detectar (5 par(es) en la consulta 20/10/2026 20:11 UTC) |
| Deployer | `5RQ1UWATaMjjXC34BW6UusEUdEoCuNRECBW8nnHPiCGH` | PumpPortal (evento create), al detectar |
| Par creado | 20/10/2026 19:33 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,8 min / 11,8 min / 38,1 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 20/10/2026 20:11 UTC |
| Holders / top-10 | 1.795 / 39,23% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 20/10/2026 20:11 UTC |
| Holders efectivos del top-10 | 5,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 20/10/2026 20:11 UTC |
| Etiquetas de RugCheck | «Copycat token» | RugCheck `risks[].name` (texto de la fuente), consulta 20/10/2026 20:11 UTC |
| Links | DexScreener: https://dexscreener.com/solana/EvdxxQA1TPuANNW2EMMHsJ36G9QumjHHCL8nui9SADxp · Solscan: https://solscan.io/token/CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump · pump.fun: https://pump.fun/coin/CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump · web: https://otcdesks.cash/coin/CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump · twitter: https://x.com/HimothyJamesJr_/status/2112628830427099247?s=20 | consulta 20/10/2026 20:11 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 20/10/2026 20:11 UTC)
- **Historia:**
  - Par creado el 20/10/2026 19:33 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 20/10/2026 19:45 UTC, con el par a 11,8 min de creado: precio $0,00004973, mcap $49.735, liquidez $17.934.
  - Velas de 1 h de GeckoTerminal (2, desde 20/10/2026 19:00 UTC): apertura $0,00004041 · máximo $0,0001284 (20/10/2026 20:00 UTC) · mínimo $0,00001688 (20/10/2026 20:00 UTC) · último cierre $0,0001010.
  - En la consulta 20/10/2026 20:11 UTC: precio $0,0001065, liquidez $27.120, FDV $102.817.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 20/10/2026 19:45 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00004973 |
| Liquidez | $17.934 |
| MCap | $49.735 |
| Volumen 24 h | $174.632 |
| Cambio 24 h | +14% |
| Cambio m5 / h1 | -9,0% / +14,1% |
| Volumen m5 / h1 | $35.325 / $174.632 |
| Trades m5 (compras / ventas) | 546 / 414 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 42; motivos sin regla: young-0.4 · edad 11.8 min · pesos info 59 / estructura 20 / precio 20 · info 23.0 · estructura 12.8 · precio/volumen 5.9 · cobertura 93/100, [info] narrative_wave: ola 'energy': 30 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 1330 · top-10 43.7 % → +2.5, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1330/4560 = 0.29 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×2.4 la tasa horaria (s 0.37), [precio/volumen] buy_pressure_shift: compras 57% en 5 min vs 53% en 1 h (s 0.18), [precio/volumen] holder_accumulation: holders 414→1330 (+76.3/min) · top10 48.5%→43.7% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=17933.7, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 42 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-20T19:45:00+00:00, sin estado previo): **15** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 68 de 42.401 tokens analizados (0,16%) quedan ≥ 56. Con score 15, este activo queda en el percentil 97,3 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 20/10/2026 19:45 UTC, hasta 22/10/2026 19:45 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 -9,0% · h1 +14,1% · h24 +14% · volumen m5/h1 0,20 · edad del par 11,8 min.
- **Precio de entrada** (alerta): $0,00004973.
- **Consulta 20/10/2026 20:11 UTC:** $0,0001065 (+114,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump_2026-10-20_194500.json` · blob `f6c4ce0ac433dd8ed896265247188670964aaa24` · commit `1e24df0` (2026-10-20T20:00:47Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-20_192535.json` · blob `57b9d113d291561cfffefaf4feab1c01e6111b8d` · commit `1e24df0` (2026-10-20T20:00:47Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-20_194500`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump · registro · 20/10/2026 19:45 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump · HTTP 200 · 20/10/2026 20:11 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump/report · HTTP 200 · 20/10/2026 20:11 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump · HTTP 200 · 20/10/2026 20:11 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/EvdxxQA1TPuANNW2EMMHsJ36G9QumjHHCL8nui9SADxp/ohlcv/hour?limit=1000 · HTTP 200 · 20/10/2026 20:11 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump · HTTP 404 · 20/10/2026 20:11 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ENERGYUSDT · HTTP 400 · 20/10/2026 20:11 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ENERGY-USD · HTTP 404 · 20/10/2026 20:11 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $27.120 vs $27.396 → 1,01%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001065 vs $0,0001010 → 5,16%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump_2026-10-20_194500.json',encoding='utf-8'));d=d.get('CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump',d);p=mock.patch('time.time',return_value=1792525500);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint CicoFLHq5c3n6w61e68WfnooFWUzTLisp3a2HdiWpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 20/10/2026 20:11 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `c80a9fbe3b7bb222…`
