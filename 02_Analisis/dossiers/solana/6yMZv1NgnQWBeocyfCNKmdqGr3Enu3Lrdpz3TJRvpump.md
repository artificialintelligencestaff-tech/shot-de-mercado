# catonthinice (CATONICE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001288 · liquidez $102.925 · mcap $1.278.304 (al detectar)  
Detectado el 19/10/2026 00:03 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 21/10/2026 00:03 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir CATONICE

Estudio de cómo se adquiere CATONICE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 19/10/2026 00:25 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 19/10/2026 00:03 UTC | pumpswap `2aegSTa…QD6v` | $102.925 | 5% | 0,194% | 1,943% | 19,432% | $515 | $1.544 |
| consulta 19/10/2026 00:25 UTC | pumpswap `2aegSTa…QD6v` | $104.415 | 5% | 0,192% | 1,915% | 19,154% | $522 | $1.566 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump`
5. Configurar el slippage: 5% (liquidez $104.415, consulta 19/10/2026 00:25 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump) y el par en DexScreener (https://dexscreener.com/solana/2aegSTad7cZTrd536XtXkjkY88hvthvwsDA5TuCtQD6v); mint authority / freeze authority: revocada / revocada · holders n/d · top-10 n/d (consulta 19/10/2026 00:25 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump
- Par en DexScreener: https://dexscreener.com/solana/2aegSTad7cZTrd536XtXkjkY88hvthvwsDA5TuCtQD6v
- Página del lanzamiento (pump.fun): https://pump.fun/coin/6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders n/d · top-10 n/d (consulta 19/10/2026 00:25 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | catonthinice / CATONICE | registro de la detección (trending) |
| Mint / contrato | `6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `2aegSTad7cZTrd536XtXkjkY88hvthvwsDA5TuCtQD6v` | DexScreener, al detectar (4 par(es) en la consulta 19/10/2026 00:25 UTC) |
| Deployer | n/d | n/d (fuente: RugCheck `creator`) |
| Par creado | 18/10/2026 15:35 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 8,5 h / 8,5 h / 8,8 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | GoPlus, consulta 19/10/2026 00:25 UTC |
| Holders / top-10 | n/d / n/d | RugCheck [P: sin consulta] |
| Holders efectivos del top-10 | n/d | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | n/d | RugCheck [P] |
| Etiquetas de RugCheck | n/d | RugCheck [P] |
| Links | DexScreener: https://dexscreener.com/solana/2aegSTad7cZTrd536XtXkjkY88hvthvwsDA5TuCtQD6v · Solscan: https://solscan.io/token/6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump · pump.fun: https://pump.fun/coin/6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump · web: https://catonthinice.fun · twitter: https://x.com/catonice_meme | consulta 19/10/2026 00:25 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (metadata sin consultar [P])
- **Historia:**
  - Par creado el 18/10/2026 15:35 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 19/10/2026 00:03 UTC, con el par a 8,5 h de creado: precio $0,001288, mcap $1.278.304, liquidez $102.925.
  - Velas de 1 h de GeckoTerminal (10, desde 18/10/2026 15:00 UTC): apertura $0,0001564 · máximo $0,002133 (18/10/2026 19:00 UTC) · mínimo $0,0001564 (18/10/2026 15:00 UTC) · último cierre $0,001287.
  - En la consulta 19/10/2026 00:25 UTC: precio $0,001325, liquidez $104.415, FDV $1.314.867.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 19/10/2026 00:03 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001288 |
| Liquidez | $102.925 |
| MCap | $1.278.304 |
| Volumen 24 h | $2.914.663 |
| Cambio 24 h | +1.950% |
| Cambio m5 / h1 | -4,0% / +27,4% |
| Volumen m5 / h1 | $10.562 / $232.845 |
| Trades m5 (compras / ventas) | 773 / 187 |
| Edad del par | 8,5 h |
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
| MCap | ≥ $1M | $1.278.304 | +25 |
| Volumen 24 h | ≥ $1M | $2.914.663 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 81% | +25 |
| Volumen m5 | > $1K (par maduro) | $10.562 | +10 |
| Liquidez | ≥ $100K | $102.925 | +15 |
| Cambio 24 h | ≥ +50% | +1.950% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.950% · liq/mcap 8,1% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-19T00:03:40+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=8.1% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 67 de 40.270 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 19/10/2026 00:03 UTC, hasta 21/10/2026 00:03 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 -4,0% · h1 +27,4% · h24 +1.950% · volumen m5/h1 0,05 · edad del par 8,5 h.
- **Precio de entrada** (alerta): $0,001288.
- **Consulta 19/10/2026 00:25 UTC:** $0,001325 (+2,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump_2026-10-19_000340.json` · blob `09f0b60834633f0b804b843926b0b1bd062a04d6` · commit `cd905bc` (2026-10-19T00:18:33Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-18_235704.json` · blob `a9f18f60d278090f4928e7e9193a061f67a0230c` · commit `cd905bc` (2026-10-19T00:18:33Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-19_000340`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump · registro · 19/10/2026 00:03 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump · HTTP 200 · 19/10/2026 00:25 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump/report · error ConnectionError · 19/10/2026 00:25 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump · HTTP 200 · 19/10/2026 00:25 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/2aegSTad7cZTrd536XtXkjkY88hvthvwsDA5TuCtQD6v/ohlcv/hour?limit=1000 · HTTP 200 · 19/10/2026 00:25 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump · HTTP 404 · 19/10/2026 00:25 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=CATONICEUSDT · HTTP 400 · 19/10/2026 00:25 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/CATONICE-USD · HTTP 404 · 19/10/2026 00:25 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001325 vs $0,001287 → 2,87%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump_2026-10-19_000340.json',encoding='utf-8'));d=d.get('6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump',d);p=mock.patch('time.time',return_value=1792368220);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 6yMZv1NgnQWBeocyfCNKmdqGr3Enu3Lrdpz3TJRvpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 19/10/2026 00:25 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `51a9eba42d3d7879…`
