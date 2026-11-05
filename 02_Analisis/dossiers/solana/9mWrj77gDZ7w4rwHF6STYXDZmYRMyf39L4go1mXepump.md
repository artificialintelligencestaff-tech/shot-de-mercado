# Gavel Drop (GAVELDROP) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0002072 · liquidez $40.095 · mcap $206.250 (al detectar)  
Detectado el 05/11/2026 22:34 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 07/11/2026 22:34 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir GAVELDROP

Estudio de cómo se adquiere GAVELDROP, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 05/11/2026 22:34 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 05/11/2026 22:34 UTC | pumpswap `GgGoctY…akTo` | $40.095 | 10% | 0,499% | 4,988% | 49,881% | $200 | $601 |
| consulta 05/11/2026 22:34 UTC | pumpswap `GgGoctY…akTo` | $40.526 | 10% | 0,494% | 4,935% | 49,351% | $203 | $608 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump`
5. Configurar el slippage: 10% (liquidez $40.526, consulta 05/11/2026 22:34 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump) y el par en DexScreener (https://dexscreener.com/solana/GgGoctYNusmGdFpqmrC9pv8JX6JPG4mkm4RkeNzkakTo); mint authority / freeze authority: revocada / revocada · holders 12.585 · top-10 12,03% (consulta 05/11/2026 22:34 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump
- Par en DexScreener: https://dexscreener.com/solana/GgGoctYNusmGdFpqmrC9pv8JX6JPG4mkm4RkeNzkakTo
- Página del lanzamiento (pump.fun): https://pump.fun/coin/9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 12.585 · top-10 12,03% (consulta 05/11/2026 22:34 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Gavel Drop / GAVELDROP | registro de la detección (trending) |
| Mint / contrato | `9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `GgGoctYNusmGdFpqmrC9pv8JX6JPG4mkm4RkeNzkakTo` | DexScreener, al detectar (3 par(es) en la consulta 05/11/2026 22:34 UTC) |
| Deployer | `3jedanvgSEd4ReVUDnY2uL7SmiGBjwohp41KneKt2g82` | RugCheck `creator` |
| Par creado | 04/11/2026 22:44 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 23,8 h / 23,8 h / 23,8 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 05/11/2026 22:34 UTC |
| Holders / top-10 | 12.585 / 12,03% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 05/11/2026 22:34 UTC |
| Holders efectivos del top-10 | 1,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; orca 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 05/11/2026 22:34 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 05/11/2026 22:34 UTC |
| Links | DexScreener: https://dexscreener.com/solana/GgGoctYNusmGdFpqmrC9pv8JX6JPG4mkm4RkeNzkakTo · Solscan: https://solscan.io/token/9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump · pump.fun: https://pump.fun/coin/9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump · web: https://gaveldrop.mom · twitter: https://x.com/gaveldrop · telegram: https://t.me/GAVELDROPSOL | consulta 05/11/2026 22:34 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 05/11/2026 22:34 UTC)
- **Historia:**
  - Par creado el 04/11/2026 22:44 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 05/11/2026 22:34 UTC, con el par a 23,8 h de creado: precio $0,0002072, mcap $206.250, liquidez $40.095.
  - Velas de 1 h de GeckoTerminal (25, desde 04/11/2026 22:00 UTC): apertura $0,0003233 · máximo $0,001553 (05/11/2026 15:00 UTC) · mínimo $0,00006232 (04/11/2026 22:00 UTC) · último cierre $0,0002091.
  - En la consulta 05/11/2026 22:34 UTC: precio $0,0002115, liquidez $40.526, FDV $210.539.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 05/11/2026 22:34 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0002072 |
| Liquidez | $40.095 |
| MCap | $206.250 |
| Volumen 24 h | $4.904.008 |
| Cambio 24 h | +233% |
| Cambio m5 / h1 | +2,1% / -41,0% |
| Volumen m5 / h1 | $5.664 / $130.726 |
| Trades m5 (compras / ventas) | 980 / 210 |
| Edad del par | 23,8 h |
| Score del feed (WS) | 76 |

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
| Score del feed | score WS × 0,3 | WS 76 × 0,3 | +22,7 |
| MCap | ≥ $100K | $206.250 | +15 |
| Volumen 24 h | ≥ $1M | $4.904.008 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 82% | +25 |
| Volumen m5 | > $1K (par maduro) | $5.664 | +10 |
| Liquidez | ≥ $20K | $40.095 | +5 |
| Cambio 24 h | ≥ +50% | +233% | +10 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-05T22:34:22+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 92 de 46.731 tokens analizados (0,20%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 05/11/2026 22:34 UTC, hasta 07/11/2026 22:34 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +2,1% · h1 -41,0% · h24 +233% · volumen m5/h1 0,04 · edad del par 23,8 h.
- **Precio de entrada** (alerta): $0,0002072.
- **Consulta 05/11/2026 22:34 UTC:** $0,0002115 (+2,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump_2026-11-05_223431.json` · blob `ed82a2c681e09e17d993e99eac81416dbf569811` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-05_222917.json` · blob `a0f85b2c02f18863b1cf3fba7d8a55d83bc53982` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-05_223431`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump · registro · 05/11/2026 22:34 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump · HTTP 200 · 05/11/2026 22:34 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump/report · HTTP 200 · 05/11/2026 22:34 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump · HTTP 200 · 05/11/2026 22:34 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/GgGoctYNusmGdFpqmrC9pv8JX6JPG4mkm4RkeNzkakTo/ohlcv/hour?limit=1000 · HTTP 200 · 05/11/2026 22:34 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump · HTTP 404 · 05/11/2026 22:34 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=GAVELDROPUSDT · HTTP 400 · 05/11/2026 22:34 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/GAVELDROP-USD · HTTP 404 · 05/11/2026 22:34 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $40.526 vs $40.189 → 0,83%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0002115 vs $0,0002091 → 1,15%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump_2026-11-05_223431.json',encoding='utf-8'));d=d.get('9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump',d);p=mock.patch('time.time',return_value=1793918062);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 05/11/2026 22:34 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `2d83d593911b87ec…`
