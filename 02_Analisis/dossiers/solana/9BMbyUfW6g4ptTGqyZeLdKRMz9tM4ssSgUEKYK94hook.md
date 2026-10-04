# Hooker (HOOKER) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001344 · liquidez $32.306 · mcap $134.475 (al detectar)  
Detectado el 04/10/2026 23:00 UTC por: young-0.4 · edad 11.5 min · pesos info 59 / estructura 20 / precio 20 · info 17.5 · estructura 14.7 · precio/volumen 11.9 · cobertura 93/100, [info] narrative_wave: ola 'hooker': 5 lanzamientos más en 1 h → +9.3, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 44, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 06/10/2026 23:00 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HOOKER

Estudio de cómo se adquiere HOOKER, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 04/10/2026 23:10 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 04/10/2026 23:00 UTC | pumpswap `CpEJX4h…8Bao` | $32.306 | 10% | 0,619% | 6,191% | 61,908% | $162 | $485 |
| consulta 04/10/2026 23:10 UTC | pumpswap `CpEJX4h…8Bao` | $37.975 | 10% | 0,527% | 5,267% | 52,666% | $190 | $570 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook`
5. Configurar el slippage: 10% (liquidez $37.975, consulta 04/10/2026 23:10 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook) y el par en DexScreener (https://dexscreener.com/solana/CpEJX4hDGhce57vfyzbZV3UougyS9GGw5rnNGRxW8Bao); mint authority / freeze authority: revocada / revocada · holders 2.459 · top-10 32,69% (consulta 04/10/2026 23:10 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook
- Par en DexScreener: https://dexscreener.com/solana/CpEJX4hDGhce57vfyzbZV3UougyS9GGw5rnNGRxW8Bao
- Página del lanzamiento (pump.fun): https://pump.fun/coin/9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.459 · top-10 32,69% (consulta 04/10/2026 23:10 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Hooker / HOOKER | registro de la detección (pumpportal_live) |
| Mint / contrato | `9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `CpEJX4hDGhce57vfyzbZV3UougyS9GGw5rnNGRxW8Bao` | DexScreener, al detectar (2 par(es) en la consulta 04/10/2026 23:10 UTC) |
| Deployer | `fomosZ2wByGHXygzSzDg1J7uFVCiAj9KbZVjr342hnX` | PumpPortal (evento create), al detectar |
| Par creado | 04/10/2026 22:48 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,5 min / 11,5 min / 22,1 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 04/10/2026 23:10 UTC |
| Holders / top-10 | 2.459 / 32,69% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 04/10/2026 23:10 UTC |
| Holders efectivos del top-10 | 5,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 04/10/2026 23:10 UTC |
| Etiquetas de RugCheck | «Creator history of rugged tokens» | RugCheck `risks[].name` (texto de la fuente), consulta 04/10/2026 23:10 UTC |
| Links | DexScreener: https://dexscreener.com/solana/CpEJX4hDGhce57vfyzbZV3UougyS9GGw5rnNGRxW8Bao · Solscan: https://solscan.io/token/9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook · pump.fun: https://pump.fun/coin/9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook · web: https://hooker.fun · web: https://github.com/hookerdotfun/Hooker · twitter: https://x.com/hookerdotfun | consulta 04/10/2026 23:10 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 04/10/2026 23:10 UTC)
- **Historia:**
  - Par creado el 04/10/2026 22:48 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 04/10/2026 23:00 UTC, con el par a 11,5 min de creado: precio $0,0001344, mcap $134.475, liquidez $32.306.
  - Velas de 1 h de GeckoTerminal (2, desde 04/10/2026 22:00 UTC): apertura $0,00004046 · máximo $0,0002575 (04/10/2026 23:00 UTC) · mínimo $0,00001632 (04/10/2026 22:00 UTC) · último cierre $0,0001745.
  - En la consulta 04/10/2026 23:10 UTC: precio $0,0001767, liquidez $37.975, FDV $176.773.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 04/10/2026 23:00 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001344 |
| Liquidez | $32.306 |
| MCap | $134.475 |
| Volumen 24 h | $307.008 |
| Cambio 24 h | +182% |
| Cambio m5 / h1 | +36,7% / +182,0% |
| Volumen m5 / h1 | $197.300 / $307.008 |
| Trades m5 (compras / ventas) | 1.875 / 1.471 |
| Edad del par | 11,5 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 44; motivos sin regla: young-0.4 · edad 11.5 min · pesos info 59 / estructura 20 / precio 20 · info 17.5 · estructura 14.7 · precio/volumen 11.9 · cobertura 93/100, [info] narrative_wave: ola 'hooker': 5 lanzamientos más en 1 h → +9.3, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 1730 · top-10 33.1 % → +2.4, [estructura] dev_wallet: creador compró 3.5 % del supply → +2.0, [estructura] holder_to_txn_ratio: holders/txns 1730/5594 = 0.31 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×7.7 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 56% en 5 min vs 56% en 1 h (s 0.01), [precio/volumen] liquidity_inflow: liquidez +130% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 734→1730 (+166.0/min) · top10 44.8%→33.1% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=32305.9, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=15097.97, score 44 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-04T23:00:06+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 13 de 10.912 tokens analizados (0,12%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 04/10/2026 23:00 UTC, hasta 06/10/2026 23:00 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +36,7% · h1 +182,0% · h24 +182% · volumen m5/h1 0,64 · edad del par 11,5 min.
- **Precio de entrada** (alerta): $0,0001344.
- **Consulta 04/10/2026 23:10 UTC:** $0,0001767 (+31,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook_2026-10-04_230006.json` · blob `906379e654212c200590dd3eee58fa05a9661fec` · commit `6e3fd9b` (2026-10-04T23:04:22Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-04_230006`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook · registro · 04/10/2026 23:00 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook · HTTP 200 · 04/10/2026 23:10 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook/report · HTTP 200 · 04/10/2026 23:10 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook · HTTP 200 · 04/10/2026 23:10 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/CpEJX4hDGhce57vfyzbZV3UougyS9GGw5rnNGRxW8Bao/ohlcv/hour?limit=1000 · HTTP 200 · 04/10/2026 23:10 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook · HTTP 404 · 04/10/2026 23:10 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HOOKERUSDT · HTTP 400 · 04/10/2026 23:10 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HOOKER-USD · HTTP 404 · 04/10/2026 23:10 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $37.975 vs $40.400 → 6,00%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001767 vs $0,0001745 → 1,23%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook_2026-10-04_230006.json',encoding='utf-8'));d=d.get('9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook',d);p=mock.patch('time.time',return_value=1791154806);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 9BMbyUfW6g4ptTGqyZeLdKRMz9tM4ssSgUEKYK94hook --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 04/10/2026 23:10 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `944df3a901dffcb3…`
