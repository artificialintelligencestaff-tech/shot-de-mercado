# XRPN (EVERNORTHXRP) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1622 · liquidez $1.108.403 · mcap $162.272.021 (al detectar)  
Detectado el 13/10/2026 16:20 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 92, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 15/10/2026 16:20 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir EVERNORTHXRP

Estudio de cómo se adquiere EVERNORTHXRP, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 13/10/2026 16:43 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 13/10/2026 16:20 UTC | pumpswap `GDNA4YT…cq13` | $1.108.403 | 1% | 0,018% | 0,180% | 1,804% | $5.542 | $16.626 |
| consulta 13/10/2026 16:43 UTC | pumpswap `GDNA4YT…cq13` | $1.112.121 | 1% | 0,018% | 0,180% | 1,798% | $5.561 | $16.682 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump`
5. Configurar el slippage: 1% (liquidez $1.112.121, consulta 13/10/2026 16:43 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump) y el par en DexScreener (https://dexscreener.com/solana/GDNA4YTgEzt559PRCm1tKMdkMtErJ6ows9nqLJ3Rcq13); mint authority / freeze authority: revocada / revocada · holders 3.077 · top-10 2,48% (consulta 13/10/2026 16:43 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump
- Par en DexScreener: https://dexscreener.com/solana/GDNA4YTgEzt559PRCm1tKMdkMtErJ6ows9nqLJ3Rcq13
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.077 · top-10 2,48% (consulta 13/10/2026 16:43 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | XRPN / EVERNORTHXRP | registro de la detección (trending) |
| Mint / contrato | `2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `GDNA4YTgEzt559PRCm1tKMdkMtErJ6ows9nqLJ3Rcq13` | DexScreener, al detectar (2 par(es) en la consulta 13/10/2026 16:43 UTC) |
| Deployer | `CC9bbbb1Nw2TWoACVpKukT8taAGLBiFKQbQC4BknFSHo` | RugCheck `creator` |
| Par creado | 13/10/2026 02:21 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 14,0 h / 14,0 h / 14,4 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 13/10/2026 16:43 UTC |
| Holders / top-10 | 3.077 / 2,48% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 13/10/2026 16:43 UTC |
| Holders efectivos del top-10 | 9,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 13/10/2026 16:43 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 13/10/2026 16:43 UTC |
| Links | DexScreener: https://dexscreener.com/solana/GDNA4YTgEzt559PRCm1tKMdkMtErJ6ows9nqLJ3Rcq13 · Solscan: https://solscan.io/token/2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump · pump.fun: https://pump.fun/coin/2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump · web / Telegram / X: no publicados en DexScreener | consulta 13/10/2026 16:43 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 13/10/2026 16:43 UTC)
- **Historia:**
  - Par creado el 13/10/2026 02:21 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 13/10/2026 16:20 UTC, con el par a 14,0 h de creado: precio $0,1622, mcap $162.272.021, liquidez $1.108.403.
  - Velas de 1 h de GeckoTerminal (15, desde 13/10/2026 02:00 UTC): apertura $0,00004403 · máximo $0,1640 (13/10/2026 16:00 UTC) · mínimo $0,00004403 (13/10/2026 02:00 UTC) · último cierre $0,1640.
  - En la consulta 13/10/2026 16:43 UTC: precio $0,1637, liquidez $1.112.121, FDV $163.783.074.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 13/10/2026 16:20 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1622 |
| Liquidez | $1.108.403 |
| MCap | $162.272.021 |
| Volumen 24 h | $536.005 |
| Cambio 24 h | +368.887% |
| Cambio m5 / h1 | +0,2% / +3,0% |
| Volumen m5 / h1 | $557 / $7.658 |
| Trades m5 (compras / ventas) | 3 / 0 |
| Edad del par | 14,0 h |
| Score del feed (WS) | 90 |

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

Desglose reconstruido desde los motivos registrados; suma 92 = score registrado 92 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 90 × 0,3 | +27,1 |
| MCap | ≥ $1M | $162.272.021 | +25 |
| Volumen 24 h | ≥ $100K | $536.005 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 100% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,2% · h1 +3,0% | +20 |
| Volumen m5 | > $500 (par maduro) | $557 | +5 |
| Liquidez | ≥ $100K | $1.108.403 | +15 |
| Cambio 24 h | ≥ +50% | +368.887% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +368.887% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **92** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-13T16:20:56+00:00, sin estado previo): **92** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 53 de 33.623 tokens analizados (0,16%) quedan ≥ 56. Con score 92, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 13/10/2026 16:20 UTC, hasta 15/10/2026 16:20 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +0,2% · h1 +3,0% · h24 +368.887% · volumen m5/h1 0,07 · edad del par 14,0 h.
- **Precio de entrada** (alerta): $0,1622.
- **Consulta 13/10/2026 16:43 UTC:** $0,1637 (+0,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump_2026-10-13_162056.json` · blob `4711022f45d92c0ac77acb67248dd3f08e4191cf` · commit `36932f1` (2026-10-13T16:35:56Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-13_161354.json` · blob `72dd3c0ece0714c59220f35ee9cfc1355ab53827` · commit `36932f1` (2026-10-13T16:35:56Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-13_162056`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump · registro · 13/10/2026 16:20 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump · HTTP 200 · 13/10/2026 16:43 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump/report · HTTP 200 · 13/10/2026 16:43 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump · HTTP 200 · 13/10/2026 16:43 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/GDNA4YTgEzt559PRCm1tKMdkMtErJ6ows9nqLJ3Rcq13/ohlcv/hour?limit=1000 · HTTP 200 · 13/10/2026 16:43 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump · HTTP 404 · 13/10/2026 16:43 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=EVERNORTHXRPUSDT · HTTP 400 · 13/10/2026 16:43 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/EVERNORTHXRP-USD · HTTP 404 · 13/10/2026 16:43 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.112.121 vs $1.113.308 → 0,11%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1637 vs $0,1640 → 0,16%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump_2026-10-13_162056.json',encoding='utf-8'));d=d.get('2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump',d);p=mock.patch('time.time',return_value=1791908456);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2m3hiFbtduQe3Dz1Y2kQqztLmJJntrXgnaRPzrLnpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 13/10/2026 16:43 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `b5b989dac1fca89b…`
