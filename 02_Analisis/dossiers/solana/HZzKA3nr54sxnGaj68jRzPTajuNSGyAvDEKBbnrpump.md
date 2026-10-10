# DOTF (DOTF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1643 · liquidez $1.125.200 · mcap $164.355.513 (al detectar)  
Detectado el 10/10/2026 02:58 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 12/10/2026 02:58 UTC (< 48 h) · vigente: quedan 47,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir DOTF

Estudio de cómo se adquiere DOTF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 10/10/2026 03:57 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 10/10/2026 02:58 UTC | pumpswap `6s4QZ5f…EPYQ` | $1.125.200 | 1% | 0,018% | 0,178% | 1,777% | $5.626 | $16.878 |
| consulta 10/10/2026 03:57 UTC | pumpswap `6s4QZ5f…EPYQ` | $1.970 | 10% | 10,153% | 101,529% | 1.015,285% | $10 | $30 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump`
5. Configurar el slippage: 10% (liquidez $1.970, consulta 10/10/2026 03:57 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump) y el par en DexScreener (https://dexscreener.com/solana/6s4QZ5fj4uhXuyvgkKNWBoTvbAoUtG3VTRBbqrakEPYQ); mint authority / freeze authority: revocada / revocada · holders 47 · top-10 100,00% (consulta 10/10/2026 03:57 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump
- Par en DexScreener: https://dexscreener.com/solana/6s4QZ5fj4uhXuyvgkKNWBoTvbAoUtG3VTRBbqrakEPYQ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 47 · top-10 100,00% (consulta 10/10/2026 03:57 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | DOTF / DOTF | registro de la detección (trending) |
| Mint / contrato | `HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6s4QZ5fj4uhXuyvgkKNWBoTvbAoUtG3VTRBbqrakEPYQ` | DexScreener, al detectar (2 par(es) en la consulta 10/10/2026 03:57 UTC) |
| Deployer | `7bN9MEuHgNM2HSGnJCRg6drsxGCUA59CVAmXcveYKYKx` | RugCheck `creator` |
| Par creado | 10/10/2026 01:44 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 73,8 min / 73,8 min / 2,2 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 10/10/2026 03:57 UTC |
| Holders / top-10 | 47 / 100,00% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 10/10/2026 03:57 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 10/10/2026 03:57 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 10/10/2026 03:57 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6s4QZ5fj4uhXuyvgkKNWBoTvbAoUtG3VTRBbqrakEPYQ · Solscan: https://solscan.io/token/HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump · pump.fun: https://pump.fun/coin/HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump · web / Telegram / X: no publicados en DexScreener | consulta 10/10/2026 03:57 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 10/10/2026 03:57 UTC)
- **Historia:**
  - Par creado el 10/10/2026 01:44 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 10/10/2026 02:58 UTC, con el par a 73,8 min de creado: precio $0,1643, mcap $164.355.513, liquidez $1.125.200.
  - Velas de 1 h de GeckoTerminal (3, desde 10/10/2026 01:00 UTC): apertura $0,1509 · máximo $0,1684 (10/10/2026 03:00 UTC) · mínimo $0,000001924 (10/10/2026 03:00 UTC) · último cierre $0,000001948.
  - En la consulta 10/10/2026 03:57 UTC: precio $0,000001948, liquidez $1.970, FDV $1.948.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 10/10/2026 02:58 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1643 |
| Liquidez | $1.125.200 |
| MCap | $164.355.513 |
| Volumen 24 h | $571.083 |
| Cambio 24 h | +360.732% |
| Cambio m5 / h1 | +0,2% / +5,2% |
| Volumen m5 / h1 | $2.150 / $29.956 |
| Trades m5 (compras / ventas) | 8 / 4 |
| Edad del par | 73,8 min |
| Score del feed (WS) | 83 |

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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 83 × 0,3 | +24,8 |
| MCap | ≥ $1M | $164.355.513 | +25 |
| Volumen 24 h | ≥ $100K | $571.083 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 67% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,2% · h1 +5,2% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 73,8 min | +8 |
| Volumen m5 | > $1K (par maduro) | $2.150 | +10 |
| Liquidez | ≥ $100K | $1.125.200 | +15 |
| Cambio 24 h | ≥ +50% | +360.732% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +360.732% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-10T02:58:41+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 43 de 26.399 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 10/10/2026 02:58 UTC, hasta 12/10/2026 02:58 UTC · vigente: quedan 47,0 h.
- **Aceleración al detectar:** cambio m5 +0,2% · h1 +5,2% · h24 +360.732% · volumen m5/h1 0,07 · edad del par 73,8 min.
- **Precio de entrada** (alerta): $0,1643.
- **Consulta 10/10/2026 03:57 UTC:** $0,000001948 (-100,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump_2026-10-10_025841.json` · blob `07ff6dc57d0d490eadf8cdffd9c56364df4aa8b2` · commit `0c7c6ef` (2026-10-10T03:50:15Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-10_025145.json` · blob `6dbf8627f9385ecdc21d64a43b68e47756fcca69` · commit `0c7c6ef` (2026-10-10T03:50:15Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-10_025841`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump · registro · 10/10/2026 02:58 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump · HTTP 200 · 10/10/2026 03:57 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump/report · HTTP 200 · 10/10/2026 03:57 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump · HTTP 200 · 10/10/2026 03:57 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6s4QZ5fj4uhXuyvgkKNWBoTvbAoUtG3VTRBbqrakEPYQ/ohlcv/hour?limit=1000 · HTTP 200 · 10/10/2026 03:57 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump · HTTP 404 · 10/10/2026 03:57 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=DOTFUSDT · HTTP 400 · 10/10/2026 03:57 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/DOTF-USD · HTTP 404 · 10/10/2026 03:57 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.970 vs $1.971 → 0,04%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000001948 vs $0,000001948 → 0,01%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump_2026-10-10_025841.json',encoding='utf-8'));d=d.get('HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump',d);p=mock.patch('time.time',return_value=1791601121);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HZzKA3nr54sxnGaj68jRzPTajuNSGyAvDEKBbnrpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 10/10/2026 03:57 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `7c630170d340b39d…`
