# Bordrless (BORDR) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,06304 · liquidez $701.260 · mcap $63.038.162 (al detectar)  
Detectado el 12/10/2026 02:13 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 14/10/2026 02:13 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir BORDR

Estudio de cómo se adquiere BORDR, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 12/10/2026 02:41 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 12/10/2026 02:13 UTC | pumpswap `8dpLsjn…PyP5` | $701.260 | 3% | 0,029% | 0,285% | 2,852% | $3.506 | $10.519 |
| consulta 12/10/2026 02:41 UTC | pumpswap `8dpLsjn…PyP5` | $712.247 | 3% | 0,028% | 0,281% | 2,808% | $3.561 | $10.684 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump`
5. Configurar el slippage: 3% (liquidez $712.247, consulta 12/10/2026 02:41 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump) y el par en DexScreener (https://dexscreener.com/solana/8dpLsjnhXX65eLoYavjDQU2nYKZstFhqGR8LjgfKPyP5); mint authority / freeze authority: revocada / revocada · holders 2.966 · top-10 1,32% (consulta 12/10/2026 02:41 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump
- Par en DexScreener: https://dexscreener.com/solana/8dpLsjnhXX65eLoYavjDQU2nYKZstFhqGR8LjgfKPyP5
- Página del lanzamiento (pump.fun): https://pump.fun/coin/fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.966 · top-10 1,32% (consulta 12/10/2026 02:41 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Bordrless / BORDR | registro de la detección (trending) |
| Mint / contrato | `fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `8dpLsjnhXX65eLoYavjDQU2nYKZstFhqGR8LjgfKPyP5` | DexScreener, al detectar (2 par(es) en la consulta 12/10/2026 02:41 UTC) |
| Deployer | `CmF58op57R8DQiVhhaw8j5bRPE6MFktwsFenLKosoWKv` | RugCheck `creator` |
| Par creado | 12/10/2026 01:12 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,4 min / 60,4 min / 88,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 12/10/2026 02:41 UTC |
| Holders / top-10 | 2.966 / 1,32% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 12/10/2026 02:41 UTC |
| Holders efectivos del top-10 | 4,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 12/10/2026 02:41 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 12/10/2026 02:41 UTC |
| Links | DexScreener: https://dexscreener.com/solana/8dpLsjnhXX65eLoYavjDQU2nYKZstFhqGR8LjgfKPyP5 · Solscan: https://solscan.io/token/fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump · pump.fun: https://pump.fun/coin/fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump · web / Telegram / X: no publicados en DexScreener | consulta 12/10/2026 02:41 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 12/10/2026 02:41 UTC)
- **Historia:**
  - Par creado el 12/10/2026 01:12 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 12/10/2026 02:13 UTC, con el par a 60,4 min de creado: precio $0,06304, mcap $63.038.162, liquidez $701.260.
  - Velas de 1 h de GeckoTerminal (2, desde 12/10/2026 01:00 UTC): apertura $0,00004633 · máximo $0,06470 (12/10/2026 02:00 UTC) · mínimo $0,00004633 (12/10/2026 01:00 UTC) · último cierre $0,06469.
  - En la consulta 12/10/2026 02:41 UTC: precio $0,06463, liquidez $712.247, FDV $64.634.623.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 12/10/2026 02:13 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,06304 |
| Liquidez | $701.260 |
| MCap | $63.038.162 |
| Volumen 24 h | $342.973 |
| Cambio 24 h | +136.148% |
| Cambio m5 / h1 | +0,0% / +5,8% |
| Volumen m5 / h1 | $952 / $12.330 |
| Trades m5 (compras / ventas) | 296 / 6 |
| Edad del par | 60,4 min |
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
| MCap | ≥ $1M | $63.038.162 | +25 |
| Volumen 24 h | ≥ $100K | $342.973 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 98% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,0% · h1 +5,8% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,4 min | +8 |
| Volumen m5 | > $500 (par maduro) | $952 | +5 |
| Liquidez | ≥ $100K | $701.260 | +15 |
| Cambio 24 h | ≥ +50% | +136.148% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +136.148% · liq/mcap 1,1% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-12T02:13:12+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 50 de 30.419 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 12/10/2026 02:13 UTC, hasta 14/10/2026 02:13 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +0,0% · h1 +5,8% · h24 +136.148% · volumen m5/h1 0,08 · edad del par 60,4 min.
- **Precio de entrada** (alerta): $0,06304.
- **Consulta 12/10/2026 02:41 UTC:** $0,06463 (+2,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump_2026-10-12_021312.json` · blob `1c29c2b60d429f270a6cef4f1526f4e02f7d3c3f` · commit `1752ff5` (2026-10-12T02:34:55Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-12_011345.json` · blob `0f2fca197b461cfa4fdbc011b04e55abf6769b2a` · commit `1752ff5` (2026-10-12T02:34:55Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-12_021312`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump · registro · 12/10/2026 02:13 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump · HTTP 200 · 12/10/2026 02:41 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump/report · HTTP 200 · 12/10/2026 02:41 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump · HTTP 200 · 12/10/2026 02:41 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/8dpLsjnhXX65eLoYavjDQU2nYKZstFhqGR8LjgfKPyP5/ohlcv/hour?limit=1000 · HTTP 200 · 12/10/2026 02:41 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump · HTTP 404 · 12/10/2026 02:41 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BORDRUSDT · HTTP 400 · 12/10/2026 02:41 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BORDR-USD · HTTP 404 · 12/10/2026 02:41 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $712.247 vs $712.169 → 0,01%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,06463 vs $0,06469 → 0,09%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump_2026-10-12_021312.json',encoding='utf-8'));d=d.get('fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump',d);p=mock.patch('time.time',return_value=1791771192);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint fV1UQVdy7TntqeYwPFnKo9cM5pmCdn3zK33bKnZpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 12/10/2026 02:41 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `5fb0a2caef3a6b64…`
