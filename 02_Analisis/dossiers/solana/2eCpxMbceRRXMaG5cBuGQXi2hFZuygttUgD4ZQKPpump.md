# DOTF (D O T ) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1876 · liquidez $1.260.082 · mcap $187.627.436 (al detectar)  
Detectado el 06/10/2026 02:47 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 08/10/2026 02:47 UTC (< 48 h) · vigente: quedan 47,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir D O T 

Estudio de cómo se adquiere D O T , con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 02:55 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 02:47 UTC | pumpswap `HTCPC97…PcZ2` | $1.260.082 | 1% | 0,016% | 0,159% | 1,587% | $6.300 | $18.901 |
| consulta 06/10/2026 02:55 UTC | pumpswap `HTCPC97…PcZ2` | $1.264.879 | 1% | 0,016% | 0,158% | 1,581% | $6.324 | $18.973 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump`
5. Configurar el slippage: 1% (liquidez $1.264.879, consulta 06/10/2026 02:55 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump) y el par en DexScreener (https://dexscreener.com/solana/HTCPC97xiwKY8NqkQsfRGvqJFfx8WAkqBgvRPMagPcZ2); mint authority / freeze authority: revocada / revocada · holders 2.495 · top-10 10,02% (consulta 06/10/2026 02:55 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump
- Par en DexScreener: https://dexscreener.com/solana/HTCPC97xiwKY8NqkQsfRGvqJFfx8WAkqBgvRPMagPcZ2
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.495 · top-10 10,02% (consulta 06/10/2026 02:55 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | DOTF / D O T  | registro de la detección (trending) |
| Mint / contrato | `2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HTCPC97xiwKY8NqkQsfRGvqJFfx8WAkqBgvRPMagPcZ2` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 02:55 UTC) |
| Deployer | `AKAgJXiHUKfj36WF1RSvkuidyjyKhhN7kDPF9t3EukGS` | RugCheck `creator` |
| Par creado | 06/10/2026 01:47 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,1 min / 60,1 min / 68,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 02:55 UTC |
| Holders / top-10 | 2.495 / 10,02% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 02:55 UTC |
| Holders efectivos del top-10 | 10,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 02:55 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 02:55 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HTCPC97xiwKY8NqkQsfRGvqJFfx8WAkqBgvRPMagPcZ2 · Solscan: https://solscan.io/token/2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump · pump.fun: https://pump.fun/coin/2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump · web / Telegram / X: no publicados en DexScreener | consulta 06/10/2026 02:55 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 02:55 UTC)
- **Historia:**
  - Par creado el 06/10/2026 01:47 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 02:47 UTC, con el par a 60,1 min de creado: precio $0,1876, mcap $187.627.436, liquidez $1.260.082.
  - Velas de 1 h de GeckoTerminal (2, desde 06/10/2026 01:00 UTC): apertura $0,002968 · máximo $0,1894 (06/10/2026 02:00 UTC) · mínimo $0,00005008 (06/10/2026 01:00 UTC) · último cierre $0,1893.
  - En la consulta 06/10/2026 02:55 UTC: precio $0,1893, liquidez $1.264.879, FDV $189.334.523.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 02:47 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1876 |
| Liquidez | $1.260.082 |
| MCap | $187.627.436 |
| Volumen 24 h | $645.140 |
| Cambio 24 h | +374.311% |
| Cambio m5 / h1 | +0,5% / +7,7% |
| Volumen m5 / h1 | $3.474 / $47.988 |
| Trades m5 (compras / ventas) | 260 / 4 |
| Edad del par | 60,1 min |
| Score del feed (WS) | 99 |

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
| Score del feed | score WS × 0,3 | WS 99 × 0,3 | +29,8 |
| MCap | ≥ $1M | $187.627.436 | +25 |
| Volumen 24 h | ≥ $100K | $645.140 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 98% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,5% · h1 +7,7% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,1 min | +8 |
| Volumen m5 | > $1K (par maduro) | $3.474 | +10 |
| Liquidez | ≥ $100K | $1.260.082 | +15 |
| Cambio 24 h | ≥ +50% | +374.311% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +374.311% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T02:47:31+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 17 de 13.973 tokens analizados (0,12%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 02:47 UTC, hasta 08/10/2026 02:47 UTC · vigente: quedan 47,9 h.
- **Aceleración al detectar:** cambio m5 +0,5% · h1 +7,7% · h24 +374.311% · volumen m5/h1 0,07 · edad del par 60,1 min.
- **Precio de entrada** (alerta): $0,1876.
- **Consulta 06/10/2026 02:55 UTC:** $0,1893 (+0,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump_2026-10-06_024731.json` · blob `fc7f0ef60411b9c366c9dad601d9c2c6f9246aed` · commit `f80fb7c` (2026-10-06T02:49:43Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-06_014816.json` · blob `58110362259e49c228fa65f7fd25ecffaec89222` · commit `f80fb7c` (2026-10-06T02:49:43Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_024731`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump · registro · 06/10/2026 02:47 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump · HTTP 200 · 06/10/2026 02:55 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump/report · HTTP 200 · 06/10/2026 02:55 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump · HTTP 200 · 06/10/2026 02:55 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HTCPC97xiwKY8NqkQsfRGvqJFfx8WAkqBgvRPMagPcZ2/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 02:55 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump · HTTP 404 · 06/10/2026 02:55 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.264.879 vs $1.264.621 → 0,02%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1893 vs $0,1893 → 0,01%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump_2026-10-06_024731.json',encoding='utf-8'));d=d.get('2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump',d);p=mock.patch('time.time',return_value=1791254851);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2eCpxMbceRRXMaG5cBuGQXi2hFZuygttUgD4ZQKPpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 02:55 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `7d2274153f2653f4…`
