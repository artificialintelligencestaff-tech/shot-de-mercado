# Google Gemini (Gemini) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001255 · liquidez $101.699 · mcap $1.255.353 (al detectar)  
Detectado el 02/10/2026 14:13 UTC por: MCap > $1M, Volumen decente, Liquidez alta (score 62, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 04/10/2026 14:13 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Gemini

Estudio de cómo se adquiere Gemini, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 14:40 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 14:13 UTC | pumpswap `4kuq9em…saMx` | $101.699 | 5% | 0,197% | 1,967% | 19,666% | $508 | $1.525 |
| consulta 02/10/2026 14:40 UTC | pumpswap `4kuq9em…saMx` | $155.459 | 5% | 0,129% | 1,287% | 12,865% | $777 | $2.332 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump`
5. Configurar el slippage: 5% (liquidez $155.459, consulta 02/10/2026 14:40 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump) y el par en DexScreener (https://dexscreener.com/solana/4kuq9em9nAvgJQ52mvmFGsJtVdbwx1rC9nhandhZsaMx); mint authority / freeze authority: revocada / revocada · holders 2.295 · top-10 16,24% (consulta 02/10/2026 14:40 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump
- Par en DexScreener: https://dexscreener.com/solana/4kuq9em9nAvgJQ52mvmFGsJtVdbwx1rC9nhandhZsaMx
- Página del lanzamiento (pump.fun): https://pump.fun/coin/Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.295 · top-10 16,24% (consulta 02/10/2026 14:40 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Google Gemini / Gemini | registro de la detección (pumpportal_live) |
| Mint / contrato | `Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `4kuq9em9nAvgJQ52mvmFGsJtVdbwx1rC9nhandhZsaMx` | DexScreener, al detectar (2 par(es) en la consulta 02/10/2026 14:40 UTC) |
| Deployer | `24EfL3o6HKKnfSH6Ky1bcCW2a6C1u4aQMP4wXVcqi34v` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 13:50 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 22,7 min / 22,7 min / 50,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 14:40 UTC |
| Holders / top-10 | 2.295 / 16,24% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 14:40 UTC |
| Holders efectivos del top-10 | 1,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 14:40 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 14:40 UTC |
| Links | DexScreener: https://dexscreener.com/solana/4kuq9em9nAvgJQ52mvmFGsJtVdbwx1rC9nhandhZsaMx · Solscan: https://solscan.io/token/Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump · pump.fun: https://pump.fun/coin/Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump · web / Telegram / X: no publicados en DexScreener | consulta 02/10/2026 14:40 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 14:40 UTC)
- **Historia:**
  - Par creado el 02/10/2026 13:50 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 14:13 UTC, con el par a 22,7 min de creado: precio $0,001255, mcap $1.255.353, liquidez $101.699.
  - Velas de 1 h de GeckoTerminal (2, desde 02/10/2026 13:00 UTC): apertura $0,00005098 · máximo $0,002877 (02/10/2026 14:00 UTC) · mínimo $0,00005098 (02/10/2026 13:00 UTC) · último cierre $0,002877.
  - En la consulta 02/10/2026 14:40 UTC: precio $0,002897, liquidez $155.459, FDV $2.883.007.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 14:13 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001255 |
| Liquidez | $101.699 |
| MCap | $1.255.353 |
| Volumen 24 h | $50.896 |
| Cambio 24 h | +2.356% |
| Cambio m5 / h1 | +32,7% / +2.356,0% |
| Volumen m5 / h1 | $9.708 / $50.896 |
| Trades m5 (compras / ventas) | 1.517 / 1.413 |
| Edad del par | 22,7 min |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 1/2 (50,0%, IC90 12,1%–87,9%) · secundaria 0/1 resueltas (shadow_monitor.json).

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

Desglose no reproducible desde los motivos registrados (suma 60 vs score 62; motivos sin regla: Anticipación (lib_early_signals early-0.2): +2 — volume_acceleration: vol 5 min ×2.3 la tasa horaria → +0.95; buy_pressure_shift: compras 52% en 5 min vs 52% en 1 h → +0.01; liquidity_inflow: liquidez +30% en 8 min → +2): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T14:13:03+00:00, sin estado previo): **60** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen decente, Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=8.1% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 11 de 7.754 tokens analizados (0,14%) quedan ≥ 56. Con score 60, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 14:13 UTC, hasta 04/10/2026 14:13 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +32,7% · h1 +2.356,0% · h24 +2.356% · volumen m5/h1 0,19 · edad del par 22,7 min.
- **Precio de entrada** (alerta): $0,001255.
- **Consulta 02/10/2026 14:40 UTC:** $0,002897 (+130,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump_2026-10-02_141303.json` · blob `f372b63fba97d9e18c8af2d5c2d92faaadc9a998` · commit `39390b1` (2026-10-02T14:33:51Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_141303`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump · registro · 02/10/2026 14:13 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump · HTTP 200 · 02/10/2026 14:40 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump/report · HTTP 200 · 02/10/2026 14:40 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump · HTTP 200 · 02/10/2026 14:40 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/4kuq9em9nAvgJQ52mvmFGsJtVdbwx1rC9nhandhZsaMx/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 14:40 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump · HTTP 404 · 02/10/2026 14:40 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=GEMINIUSDT · HTTP 400 · 02/10/2026 14:40 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/GEMINI-USD · HTTP 404 · 02/10/2026 14:40 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $155.459 vs $156.237 → 0,50%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002897 vs $0,002877 → 0,71%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump_2026-10-02_141303.json',encoding='utf-8'));d=d.get('Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump',d);p=mock.patch('time.time',return_value=1790950383);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint Cs7nqUSYyJhU3qHw9XsBWk9hir95rHUbKy4rXbiQpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 14:40 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `eb4eb5a81bf41c6f…`
