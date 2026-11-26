# Grodia (Grodia) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0004022 · liquidez $46.508 · mcap $402.211 (al detectar)  
Detectado el 26/11/2026 09:41 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 98, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 28/11/2026 09:41 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Grodia

Estudio de cómo se adquiere Grodia, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 26/11/2026 09:41 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 26/11/2026 09:41 UTC | pumpswap `7wNXypS…Rbve` | $46.508 | 10% | 0,430% | 4,300% | 43,003% | $233 | $698 |
| consulta 26/11/2026 09:41 UTC | pumpswap `7wNXypS…Rbve` | $46.106 | 10% | 0,434% | 4,338% | 43,378% | $231 | $692 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump`
5. Configurar el slippage: 10% (liquidez $46.106, consulta 26/11/2026 09:41 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) y el par en DexScreener (https://dexscreener.com/solana/7wNXypS79Whx7vX8NCrkdhQAFiYVbQZbBuqrRdKMRbve); mint authority / freeze authority: revocada / revocada · holders 8.145 · top-10 7,14% (consulta 26/11/2026 09:41 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump
- Par en DexScreener: https://dexscreener.com/solana/7wNXypS79Whx7vX8NCrkdhQAFiYVbQZbBuqrRdKMRbve
- Página del lanzamiento (pump.fun): https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 8.145 · top-10 7,14% (consulta 26/11/2026 09:41 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Grodia / Grodia | registro de la detección (trending) |
| Mint / contrato | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7wNXypS79Whx7vX8NCrkdhQAFiYVbQZbBuqrRdKMRbve` | DexScreener, al detectar (2 par(es) en la consulta 26/11/2026 09:41 UTC) |
| Deployer | `HbSb63ETYrgEmS5LFUNRbeREEpQYf8hNijVzHctUndQZ` | RugCheck `creator` |
| Par creado | 25/11/2026 22:26 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,2 h / 11,2 h / 11,2 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 26/11/2026 09:41 UTC |
| Holders / top-10 | 8.145 / 7,14% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 26/11/2026 09:41 UTC |
| Holders efectivos del top-10 | 1,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 26/11/2026 09:41 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 26/11/2026 09:41 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7wNXypS79Whx7vX8NCrkdhQAFiYVbQZbBuqrRdKMRbve · Solscan: https://solscan.io/token/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump · pump.fun: https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump · web: https://thegrodia.site · twitter: https://x.com/thegrodia | consulta 26/11/2026 09:41 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 26/11/2026 09:41 UTC)
- **Historia:**
  - Par creado el 25/11/2026 22:26 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 26/11/2026 09:41 UTC, con el par a 11,2 h de creado: precio $0,0004022, mcap $402.211, liquidez $46.508.
  - Velas de 1 h de GeckoTerminal (12, desde 25/11/2026 22:00 UTC): apertura $0,00005448 · máximo $0,002637 (26/11/2026 01:00 UTC) · mínimo $0,00003505 (25/11/2026 22:00 UTC) · último cierre $0,0003853.
  - En la consulta 26/11/2026 09:41 UTC: precio $0,0003954, liquidez $46.106, FDV $395.456.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 26/11/2026 09:41 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0004022 |
| Liquidez | $46.508 |
| MCap | $402.211 |
| Volumen 24 h | $2.219.240 |
| Cambio 24 h | +1.040% |
| Cambio m5 / h1 | -14,4% / -36,3% |
| Volumen m5 / h1 | $5.261 / $54.443 |
| Trades m5 (compras / ventas) | 312 / 216 |
| Edad del par | 11,2 h |
| Score del feed (WS) | 79 |

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

Desglose reconstruido desde los motivos registrados; suma 98 = score registrado 98 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 79 × 0,3 | +23,6 |
| MCap | ≥ $100K | $402.211 | +15 |
| Volumen 24 h | ≥ $1M | $2.219.240 | +20 |
| Buy pressure m5 | > 55% (par maduro) | 59% | +15 |
| Volumen m5 | > $1K (par maduro) | $5.261 | +10 |
| Liquidez | ≥ $20K | $46.508 | +5 |
| Cambio 24 h | ≥ +50% | +1.040% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.040% · liq/mcap 11,6% | +0 |
| **Total** | recortado a 0–100 |  | **98** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-26T09:41:10+00:00, sin estado previo): **98** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >55%, Volumen activo m5 (>$1K), Liquidez mínima, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=11.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 111 de 47.688 tokens analizados (0,23%) quedan ≥ 56. Con score 98, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 26/11/2026 09:41 UTC, hasta 28/11/2026 09:41 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -14,4% · h1 -36,3% · h24 +1.040% · volumen m5/h1 0,10 · edad del par 11,2 h.
- **Precio de entrada** (alerta): $0,0004022.
- **Consulta 26/11/2026 09:41 UTC:** $0,0003954 (-1,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump_2026-11-26_094122.json` · blob `fe54f4a71386954e735890e55dee2fcaf71623e4` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-26_093553.json` · blob `afa084b083e2268413a5c3fea04d7ee8a682d097` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-26_094122`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump · registro · 26/11/2026 09:41 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump · HTTP 200 · 26/11/2026 09:41 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump/report · HTTP 200 · 26/11/2026 09:41 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump · HTTP 200 · 26/11/2026 09:41 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7wNXypS79Whx7vX8NCrkdhQAFiYVbQZbBuqrRdKMRbve/ohlcv/hour?limit=1000 · HTTP 200 · 26/11/2026 09:41 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump · HTTP 404 · 26/11/2026 09:41 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=GRODIAUSDT · HTTP 400 · 26/11/2026 09:41 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/GRODIA-USD · HTTP 404 · 26/11/2026 09:41 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $46.106 vs $45.743 → 0,79%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0003954 vs $0,0003853 → 2,56%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump_2026-11-26_094122.json',encoding='utf-8'));d=d.get('6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump',d);p=mock.patch('time.time',return_value=1795686070);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 26/11/2026 09:41 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `35648a24eaecf8e3…`
