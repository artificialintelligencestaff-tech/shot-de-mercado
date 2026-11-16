# BLOB (BLOB) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,01341 · liquidez $303.677 · mcap $13.297.291 (al detectar)  
Detectado el 16/11/2026 10:34 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 70, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 18/11/2026 10:34 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir BLOB

Estudio de cómo se adquiere BLOB, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 16/11/2026 10:34 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 16/11/2026 10:34 UTC | pumpswap `Hr9qopJ…2EwU` | $303.677 | 3% | 0,066% | 0,659% | 6,586% | $1.518 | $4.555 |
| consulta 16/11/2026 10:34 UTC | pumpswap `Hr9qopJ…2EwU` | $303.115 | 3% | 0,066% | 0,660% | 6,598% | $1.516 | $4.547 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump`
5. Configurar el slippage: 3% (liquidez $303.115, consulta 16/11/2026 10:34 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump) y el par en DexScreener (https://dexscreener.com/solana/Hr9qopJXCuak38rxDpZduUFhdAK2BfjtoXbfQZVn2EwU); mint authority / freeze authority: revocada / revocada · holders 36.289 · top-10 2,51% (consulta 16/11/2026 10:34 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump
- Par en DexScreener: https://dexscreener.com/solana/Hr9qopJXCuak38rxDpZduUFhdAK2BfjtoXbfQZVn2EwU
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 36.289 · top-10 2,51% (consulta 16/11/2026 10:34 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | BLOB / BLOB | registro de la detección (trending) |
| Mint / contrato | `8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Hr9qopJXCuak38rxDpZduUFhdAK2BfjtoXbfQZVn2EwU` | DexScreener, al detectar (1 par(es) en la consulta 16/11/2026 10:34 UTC) |
| Deployer | `9iSKstsyUHkDptPb4RujjAdftqowZ14YdtxzQR3VKqP5` | RugCheck `creator` |
| Par creado | 31/10/2026 15:36 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 15,8 días / 15,8 días / 15,8 días | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 16/11/2026 10:34 UTC |
| Holders / top-10 | 36.289 / 2,51% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 16/11/2026 10:34 UTC |
| Holders efectivos del top-10 | 4,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; orca 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 16/11/2026 10:34 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 16/11/2026 10:34 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Hr9qopJXCuak38rxDpZduUFhdAK2BfjtoXbfQZVn2EwU · Solscan: https://solscan.io/token/8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump · pump.fun: https://pump.fun/coin/8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump · web: https://www.blob.community/ · twitter: https://x.com/BL0B0nS0L | consulta 16/11/2026 10:34 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 16/11/2026 10:34 UTC)
- **Historia:**
  - Par creado el 31/10/2026 15:36 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 16/11/2026 10:34 UTC, con el par a 15,8 días de creado: precio $0,01341, mcap $13.297.291, liquidez $303.677.
  - Velas de 1 h de GeckoTerminal (380, desde 31/10/2026 15:00 UTC): apertura $0,0001237 · máximo $0,01495 (16/11/2026 08:00 UTC) · mínimo $0,00009295 (31/10/2026 15:00 UTC) · último cierre $0,01331.
  - En la consulta 16/11/2026 10:34 UTC: precio $0,01336, liquidez $303.115, FDV $13.247.915.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 16/11/2026 10:34 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,01341 |
| Liquidez | $303.677 |
| MCap | $13.297.291 |
| Volumen 24 h | $2.901.768 |
| Cambio 24 h | +283% |
| Cambio m5 / h1 | +0,5% / +0,2% |
| Volumen m5 / h1 | $13.424 / $205.735 |
| Trades m5 (compras / ventas) | 80 / 72 |
| Edad del par | 15,8 días |
| Score del feed (WS) | 70 |

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

Desglose reconstruido desde los motivos registrados; suma 70 = score registrado 70 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 70 × 0,3 | +21,0 |
| MCap | ≥ $1M | $13.297.291 | +25 |
| Volumen 24 h | ≥ $1M | $2.901.768 | +20 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,5% · h1 +0,2% | +20 |
| Volumen m5 | > $1K (par maduro) | $13.424 | +10 |
| Par viejo | edad > 24 h | edad 15,8 días | -50 |
| Liquidez | ≥ $100K | $303.677 | +15 |
| Cambio 24 h | ≥ +50% | +283% | +10 |
| **Total** | recortado a 0–100 |  | **70** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-16T10:34:12+00:00, sin estado previo): **70** · motivos: WS score alto, MCap > $1M, Volumen masivo, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Par >24h, no nativo pump.fun, Liquidez alta, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 103 de 47.309 tokens analizados (0,22%) quedan ≥ 56. Con score 70, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 16/11/2026 10:34 UTC, hasta 18/11/2026 10:34 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +0,5% · h1 +0,2% · h24 +283% · volumen m5/h1 0,07 · edad del par 15,8 días.
- **Precio de entrada** (alerta): $0,01341.
- **Consulta 16/11/2026 10:34 UTC:** $0,01336 (-0,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump_2026-11-16_103438.json` · blob `07c0d6d190256db725733f947ce6f3aaecd15a35` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-16_102908.json` · blob `ddf81fb343ec36f2f7b9202da4d02ad31d8ee266` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-16_103438`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump · registro · 16/11/2026 10:34 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump · HTTP 200 · 16/11/2026 10:34 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump/report · HTTP 200 · 16/11/2026 10:34 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump · HTTP 200 · 16/11/2026 10:34 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Hr9qopJXCuak38rxDpZduUFhdAK2BfjtoXbfQZVn2EwU/ohlcv/hour?limit=1000 · HTTP 200 · 16/11/2026 10:34 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump · HTTP 404 · 16/11/2026 10:34 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BLOBUSDT · HTTP 400 · 16/11/2026 10:34 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BLOB-USD · HTTP 404 · 16/11/2026 10:34 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $303.115 vs $303.455 → 0,11%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,01336 vs $0,01331 → 0,35%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump_2026-11-16_103438.json',encoding='utf-8'));d=d.get('8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump',d);p=mock.patch('time.time',return_value=1794825252);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 16/11/2026 10:34 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `e69f661f7f290d55…`
