# Grokia (GROKIA) — dossier

🎴 n/d en Solana · precio $0,0003852 · liquidez $171.933 · mcap $385.284 (al detectar)  
Detectado el 17/11/2026 12:03 UTC por: WS score alto, MCap > $100K, Volumen bajo (score 77, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 19/11/2026 12:03 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir GROKIA

Estudio de cómo se adquiere GROKIA, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **meteora**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 17/11/2026 12:04 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 17/11/2026 12:03 UTC | meteora `6HG9W5y…WX5u` | $171.933 | 5% | 0,116% | 1,163% | 11,632% | $860 | $2.579 |
| consulta 17/11/2026 12:03 UTC | meteora `6HG9W5y…WX5u` | $171.933 | 5% | 0,116% | 1,163% | 11,632% | $860 | $2.579 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en meteora
4. Pegar el mint y verificar que coincide carácter por carácter: `A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm`
5. Configurar el slippage: 5% (liquidez $171.933, consulta 17/11/2026 12:03 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm) y el par en DexScreener (https://dexscreener.com/solana/6HG9W5yNMQBpeEv3iCXiPUPYJY1wy7V7ELzkiSCLWX5u); mint authority / freeze authority: revocada / revocada · holders 1.758 · top-10 15,33% (consulta 17/11/2026 12:03 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm
- Par en DexScreener: https://dexscreener.com/solana/6HG9W5yNMQBpeEv3iCXiPUPYJY1wy7V7ELzkiSCLWX5u
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.758 · top-10 15,33% (consulta 17/11/2026 12:03 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Grokia / GROKIA | registro de la detección (trending) |
| Mint / contrato | `A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm` | registro de la detección |
| Chain / DEX / par | Solana / meteora / `6HG9W5yNMQBpeEv3iCXiPUPYJY1wy7V7ELzkiSCLWX5u` | DexScreener, al detectar (4 par(es) en la consulta 17/11/2026 12:03 UTC) |
| Deployer | n/d | n/d (fuente: RugCheck `creator`) |
| Par creado | 17/11/2026 10:57 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 65,6 min / 65,9 min / 66,2 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 17/11/2026 12:03 UTC |
| Holders / top-10 | 1.758 / 15,33% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 17/11/2026 12:03 UTC |
| Holders efectivos del top-10 | 5,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | meteoraDlmm 0%; raydium_cpmm 100%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 17/11/2026 12:03 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 17/11/2026 12:03 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6HG9W5yNMQBpeEv3iCXiPUPYJY1wy7V7ELzkiSCLWX5u · Solscan: https://solscan.io/token/A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm · twitter: https://x.com/TheGrokia · telegram: https://t.me/TheGrokia | consulta 17/11/2026 12:03 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** n/d
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 17/11/2026 12:03 UTC)
- **Historia:**
  - Par creado el 17/11/2026 10:57 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 17/11/2026 12:03 UTC, con el par a 65,6 min de creado: precio $0,0003852, mcap $385.284, liquidez $171.933.
  - Velas de 1 h de GeckoTerminal (3, desde 17/11/2026 10:00 UTC): apertura $0,0001616 · máximo $0,0005267 (17/11/2026 11:00 UTC) · mínimo $0,0001421 (17/11/2026 11:00 UTC) · último cierre $0,0003855.
  - En la consulta 17/11/2026 12:03 UTC: precio $0,0003852, liquidez $171.933, FDV $385.284.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 17/11/2026 12:03 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0003852 |
| Liquidez | $171.933 |
| MCap | $385.284 |
| Volumen 24 h | $16.776 |
| Cambio 24 h | +139% |
| Cambio m5 / h1 | +1,6% / +84,1% |
| Volumen m5 / h1 | $2.372 / $16.688 |
| Trades m5 (compras / ventas) | 2 / 15 |
| Edad del par | 65,6 min |
| Score del feed (WS) | 66 |

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

Desglose reconstruido desde los motivos registrados; suma 77 = score registrado 77 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 66 × 0,3 | +19,8 |
| MCap | ≥ $100K | $385.284 | +15 |
| Volumen 24 h | < $50K | $16.776 | +0 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +1,6% · h1 +84,1% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 65,6 min | +8 |
| Volumen m5 | > $1K (par maduro) | $2.372 | +10 |
| Venta dominante | buy pressure < 40% con volumen m5 | 12% | -20 |
| Liquidez | ≥ $100K | $171.933 | +15 |
| Cambio 24 h | ≥ +50% | +139% | +10 |
| **Total** | recortado a 0–100 |  | **77** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-17T12:03:35+00:00, sin estado previo): **77** · motivos: WS score alto, MCap > $100K, Volumen bajo, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Venta dominante (buy_pressure <40%), Liquidez alta, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 105 de 47.373 tokens analizados (0,22%) quedan ≥ 56. Con score 77, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 17/11/2026 12:03 UTC, hasta 19/11/2026 12:03 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +1,6% · h1 +84,1% · h24 +139% · volumen m5/h1 0,14 · edad del par 65,6 min.
- **Precio de entrada** (alerta): $0,0003852.
- **Consulta 17/11/2026 12:03 UTC:** $0,0003852 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm_2026-11-17_120354.json` · blob `29631861cf9b48a6afa5556f413475b92941668c` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-17_115830.json` · blob `cdbd0548075ec7e52e2c3cd3ee7b92db414a5a10` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-17_120354`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm · registro · 17/11/2026 12:03 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm · HTTP 200 · 17/11/2026 12:03 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm/report · HTTP 200 · 17/11/2026 12:03 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm · HTTP 200 · 17/11/2026 12:03 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6HG9W5yNMQBpeEv3iCXiPUPYJY1wy7V7ELzkiSCLWX5u/ohlcv/hour?limit=1000 · HTTP 200 · 17/11/2026 12:04 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm · HTTP 404 · 17/11/2026 12:04 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=GROKIAUSDT · HTTP 400 · 17/11/2026 12:04 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/GROKIA-USD · HTTP 404 · 17/11/2026 12:04 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $171.933 vs $239.315 → 28,16%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0003852 vs $0,0003855 → 0,09%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm_2026-11-17_120354.json',encoding='utf-8'));d=d.get('A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm',d);p=mock.patch('time.time',return_value=1794917015);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 17/11/2026 12:04 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `30d5f71c3a184652…`
