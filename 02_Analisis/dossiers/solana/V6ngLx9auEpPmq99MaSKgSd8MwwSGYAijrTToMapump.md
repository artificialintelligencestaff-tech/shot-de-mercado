# World Oil Trust Fund🔥 (WOTF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1725 · liquidez $1.205.694 · mcap $172.499.314 (al detectar)  
Detectado el 02/10/2026 03:25 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 04/10/2026 03:25 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir WOTF

Estudio de cómo se adquiere WOTF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 03:38 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 03:25 UTC | pumpswap `BKABzEM…kE8L` | $1.205.694 | 1% | 0,017% | 0,166% | 1,659% | $6.028 | $18.085 |
| consulta 02/10/2026 03:37 UTC | pumpswap `BKABzEM…kE8L` | $1.206.546 | 1% | 0,017% | 0,166% | 1,658% | $6.033 | $18.098 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump`
5. Configurar el slippage: 1% (liquidez $1.206.546, consulta 02/10/2026 03:37 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump) y el par en DexScreener (https://dexscreener.com/solana/BKABzEMpo6apeqrZaJGy8r2TYbdGQ9kob8RLj8uhkE8L); mint authority / freeze authority: revocada / revocada · holders 3.841 · top-10 9,96% (consulta 02/10/2026 03:37 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump
- Par en DexScreener: https://dexscreener.com/solana/BKABzEMpo6apeqrZaJGy8r2TYbdGQ9kob8RLj8uhkE8L
- Página del lanzamiento (pump.fun): https://pump.fun/coin/V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.841 · top-10 9,96% (consulta 02/10/2026 03:37 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | World Oil Trust Fund🔥 / WOTF | registro de la detección (trending) |
| Mint / contrato | `V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BKABzEMpo6apeqrZaJGy8r2TYbdGQ9kob8RLj8uhkE8L` | DexScreener, al detectar (2 par(es) en la consulta 02/10/2026 03:37 UTC) |
| Deployer | `66WKxNysraekwCZjNjhTvDpDkzoMzpH68RGr35MsWVuz` | RugCheck `creator` |
| Par creado | 02/10/2026 02:25 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,0 min / 60,0 min / 72,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 03:37 UTC |
| Holders / top-10 | 3.841 / 9,96% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 03:37 UTC |
| Holders efectivos del top-10 | 10,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 03:37 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 03:37 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BKABzEMpo6apeqrZaJGy8r2TYbdGQ9kob8RLj8uhkE8L · Solscan: https://solscan.io/token/V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump · pump.fun: https://pump.fun/coin/V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump · web / Telegram / X: no publicados en DexScreener | consulta 02/10/2026 03:37 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 03:37 UTC)
- **Historia:**
  - Par creado el 02/10/2026 02:25 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 03:25 UTC, con el par a 60,0 min de creado: precio $0,1725, mcap $172.499.314, liquidez $1.205.694.
  - Velas de 1 h de GeckoTerminal (2, desde 02/10/2026 02:00 UTC): apertura $0,002912 · máximo $0,1731 (02/10/2026 03:00 UTC) · mínimo $0,00004965 (02/10/2026 02:00 UTC) · último cierre $0,1728.
  - En la consulta 02/10/2026 03:37 UTC: precio $0,1723, liquidez $1.206.546, FDV $172.383.726.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 03:25 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1725 |
| Liquidez | $1.205.694 |
| MCap | $172.499.314 |
| Volumen 24 h | $594.358 |
| Cambio 24 h | +346.480% |
| Cambio m5 / h1 | +0,1% / +346.480,0% |
| Volumen m5 / h1 | $593 / $594.358 |
| Trades m5 (compras / ventas) | 15 / 5 |
| Edad del par | 60,0 min |
| Score del feed (WS) | 96 |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 0/1 (0,0%, IC90 0,0%–73,0%) · secundaria 0/0 resueltas (shadow_monitor.json).

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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 96 × 0,3 | +28,7 |
| MCap | ≥ $1M | $172.499.314 | +25 |
| Volumen 24 h | ≥ $100K | $594.358 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 75% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,1% · h1 +346.480,0% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,0 min | +8 |
| Volumen m5 | > $500 (par maduro) | $593 | +5 |
| Liquidez | ≥ $100K | $1.205.694 | +15 |
| Cambio 24 h | ≥ +50% | +346.480% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +346.480% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T03:25:10+00:00, sin estado previo): **43** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), WS score muy alto, MCap > $1M, Volumen alto, Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 6 de 6.779 tokens analizados (0,09%) quedan ≥ 56. Con score 43, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 03:25 UTC, hasta 04/10/2026 03:25 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +0,1% · h1 +346.480,0% · h24 +346.480% · volumen m5/h1 0,00 · edad del par 60,0 min.
- **Precio de entrada** (alerta): $0,1725.
- **Consulta 02/10/2026 03:37 UTC:** $0,1723 (-0,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump_2026-10-02_032510.json` · blob `c397f77eefccfddc0fab9b4f6185cc5c0be03bac` · commit `d2e6995` (2026-10-02T03:30:55Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-02_023004.json` · blob `f5ae3b49d74e5594354e10fccdb04acbf0c3e0d1` · commit `d2e6995` (2026-10-02T03:30:55Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_032510`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump · registro · 02/10/2026 03:25 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump · HTTP 200 · 02/10/2026 03:37 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump/report · HTTP 200 · 02/10/2026 03:37 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump · HTTP 200 · 02/10/2026 03:37 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BKABzEMpo6apeqrZaJGy8r2TYbdGQ9kob8RLj8uhkE8L/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 03:37 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump · HTTP 404 · 02/10/2026 03:38 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=WOTFUSDT · HTTP 400 · 02/10/2026 03:38 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/WOTF-USD · HTTP 404 · 02/10/2026 03:38 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.206.546 vs $1.207.504 → 0,08%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1723 vs $0,1728 → 0,29%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump_2026-10-02_032510.json',encoding='utf-8'));d=d.get('V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump',d);p=mock.patch('time.time',return_value=1790911510);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint V6ngLx9auEpPmq99MaSKgSd8MwwSGYAijrTToMapump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 03:38 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `5b69703556d86463…`
