# Make America Great Again (MAGA) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000002436 · liquidez $2.636 · mcap $2.427 (al detectar)  
Detectado el 18/10/2026 00:28 UTC por: MCap bajo, Volumen masivo, Buy pressure >60% (score 68, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 20/10/2026 00:28 UTC (< 48 h) · vigente: quedan 47,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir MAGA

Estudio de cómo se adquiere MAGA, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 18/10/2026 01:04 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 18/10/2026 00:28 UTC | pumpswap `9RGx1S8…94YN` | $2.636 | 10% | 7,588% | 75,876% | 758,757% | $13 | $40 |
| consulta 18/10/2026 01:03 UTC | pumpswap `9RGx1S8…94YN` | $2.636 | 10% | 7,588% | 75,876% | 758,757% | $13 | $40 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump`
5. Configurar el slippage: 10% (liquidez $2.636, consulta 18/10/2026 01:03 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump) y el par en DexScreener (https://dexscreener.com/solana/9RGx1S8Gb9onRgLeX4a179FYsELLXuNseFKsmXSz94YN); mint authority / freeze authority: revocada / revocada · holders 2.160 · top-10 96,56% (consulta 18/10/2026 01:03 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump
- Par en DexScreener: https://dexscreener.com/solana/9RGx1S8Gb9onRgLeX4a179FYsELLXuNseFKsmXSz94YN
- Página del lanzamiento (pump.fun): https://pump.fun/coin/GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.160 · top-10 96,56% (consulta 18/10/2026 01:03 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Make America Great Again / MAGA | registro de la detección (pumpportal) |
| Mint / contrato | `GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `9RGx1S8Gb9onRgLeX4a179FYsELLXuNseFKsmXSz94YN` | DexScreener, al detectar (3 par(es) en la consulta 18/10/2026 01:03 UTC) |
| Deployer | `2DwkzcKDEQ59xn2K6QVCT7kbW7mSEKT911kQtrG1w77f` | PumpPortal (evento create), al detectar |
| Par creado | 17/10/2026 21:48 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 2,7 h / 2,7 h / 3,3 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 18/10/2026 01:03 UTC |
| Holders / top-10 | 2.160 / 96,56% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 18/10/2026 01:03 UTC |
| Holders efectivos del top-10 | 1,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 18/10/2026 01:03 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 18/10/2026 01:03 UTC |
| Links | DexScreener: https://dexscreener.com/solana/9RGx1S8Gb9onRgLeX4a179FYsELLXuNseFKsmXSz94YN · Solscan: https://solscan.io/token/GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump · pump.fun: https://pump.fun/coin/GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump · web / Telegram / X: no publicados en DexScreener | consulta 18/10/2026 01:03 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 18/10/2026 01:03 UTC)
- **Historia:**
  - Par creado el 17/10/2026 21:48 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 18/10/2026 00:28 UTC, con el par a 2,7 h de creado: precio $0,000002436, mcap $2.427, liquidez $2.636.
  - Velas de 1 h de GeckoTerminal (4, desde 17/10/2026 21:00 UTC): apertura $0,0004189 · máximo $0,0009368 (17/10/2026 22:00 UTC) · mínimo $0,000002351 (17/10/2026 23:00 UTC) · último cierre $0,000002421.
  - En la consulta 18/10/2026 01:03 UTC: precio $0,000002436, liquidez $2.636, FDV $2.427.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 18/10/2026 00:28 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000002436 |
| Liquidez | $2.636 |
| MCap | $2.427 |
| Volumen 24 h | $1.775.355 |
| Cambio 24 h | -96% |
| Cambio m5 / h1 | +2,1% / +2,5% |
| Volumen m5 / h1 | $0 / $25 |
| Trades m5 (compras / ventas) | 1 / 0 |
| Edad del par | 2,7 h |
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

Desglose reconstruido desde los motivos registrados; suma 68 = score registrado 68 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | < $50K | $2.427 | +0 |
| Volumen 24 h | ≥ $1M | $1.775.355 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 100% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +2,1% · h1 +2,5% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 2,7 h | +8 |
| Liquidez | < $20K | $2.636 | +0 |
| Cambio 24 h | ≤ −30% | -96% | -5 |
| **Total** | recortado a 0–100 |  | **68** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-18T00:28:38+00:00, sin estado previo): **68** · motivos: MCap bajo, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 66 de 39.063 tokens analizados (0,17%) quedan ≥ 56. Con score 68, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 18/10/2026 00:28 UTC, hasta 20/10/2026 00:28 UTC · vigente: quedan 47,4 h.
- **Aceleración al detectar:** cambio m5 +2,1% · h1 +2,5% · h24 -96% · volumen m5/h1 0,00 · edad del par 2,7 h.
- **Precio de entrada** (alerta): $0,000002436.
- **Consulta 18/10/2026 01:03 UTC:** $0,000002436 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump_2026-10-18_002838.json` · blob `0ab2ff0986b6b97d81016887635bb06e36f41ca5` · commit `ec00894` (2026-10-18T00:57:38Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-18_002838`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump · registro · 18/10/2026 00:28 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump · HTTP 200 · 18/10/2026 01:03 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump/report · HTTP 200 · 18/10/2026 01:04 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump · HTTP 200 · 18/10/2026 01:04 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/9RGx1S8Gb9onRgLeX4a179FYsELLXuNseFKsmXSz94YN/ohlcv/hour?limit=1000 · HTTP 200 · 18/10/2026 01:04 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump · HTTP 404 · 18/10/2026 01:04 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MAGAUSDT · HTTP 400 · 18/10/2026 01:04 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MAGA-USD · HTTP 404 · 18/10/2026 01:04 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.636 vs $2.876 → 8,35%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002436 vs $0,000002421 → 0,63%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump_2026-10-18_002838.json',encoding='utf-8'));d=d.get('GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump',d);p=mock.patch('time.time',return_value=1792283318);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint GhpFdKYMVitKPd6kwe27Gvc8B2MnSQmURi9qqWkqpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 18/10/2026 01:04 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `fb6d2627ec30ae53…`
