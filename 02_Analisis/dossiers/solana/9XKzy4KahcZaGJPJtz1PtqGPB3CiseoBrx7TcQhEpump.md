# Gomo App (GOMO) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001106 · liquidez $101.691 · mcap $918.516 (al detectar)  
Detectado el 08/10/2026 08:00 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 72, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 10/10/2026 08:00 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir GOMO

Estudio de cómo se adquiere GOMO, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/10/2026 08:14 UTC; CoinGecko sin pares de este contrato en esos exchanges).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/10/2026 08:00 UTC | pumpswap `5a7QurJ…sCZy` | $101.691 | 5% | 0,197% | 1,967% | 19,667% | $508 | $1.525 |
| consulta 08/10/2026 08:14 UTC | pumpswap `5a7QurJ…sCZy` | $102.262 | 5% | 0,196% | 1,956% | 19,558% | $511 | $1.534 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump`
5. Configurar el slippage: 5% (liquidez $102.262, consulta 08/10/2026 08:14 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump) y el par en DexScreener (https://dexscreener.com/solana/5a7QurJLARt146JajJYPe5nh6vLyFpN2QrHUSLqbsCZy); mint authority / freeze authority: revocada / revocada · holders 10.842 · top-10 28,94% (consulta 08/10/2026 08:14 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump
- Par en DexScreener: https://dexscreener.com/solana/5a7QurJLARt146JajJYPe5nh6vLyFpN2QrHUSLqbsCZy
- Página del lanzamiento (pump.fun): https://pump.fun/coin/9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 10.842 · top-10 28,94% (consulta 08/10/2026 08:14 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Gomo App / GOMO | registro de la detección (trending) |
| Mint / contrato | `9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `5a7QurJLARt146JajJYPe5nh6vLyFpN2QrHUSLqbsCZy` | DexScreener, al detectar (5 par(es) en la consulta 08/10/2026 08:14 UTC) |
| Deployer | `6nm7Vsepvzv9jsYiJS8HfrQRGSCCiZ9L5DgwhdDgsi8z` | RugCheck `creator` |
| Par creado | 04/10/2026 21:49 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 3,4 días / 3,4 días / 3,4 días | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/10/2026 08:14 UTC |
| Holders / top-10 | 10.842 / 28,94% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/10/2026 08:14 UTC |
| Holders efectivos del top-10 | 8,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0%; manifest 0%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/10/2026 08:14 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 08/10/2026 08:14 UTC |
| Links | DexScreener: https://dexscreener.com/solana/5a7QurJLARt146JajJYPe5nh6vLyFpN2QrHUSLqbsCZy · Solscan: https://solscan.io/token/9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump · pump.fun: https://pump.fun/coin/9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump · web: https://gomofamily.life/ · twitter: https://x.com/gomo_family | consulta 08/10/2026 08:14 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** CoinGecko: SocialFi, Solana Ecosystem, Pump.fun Ecosystem · scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/10/2026 08:14 UTC)
- **Historia:**
  - Par creado el 04/10/2026 21:49 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/10/2026 08:00 UTC, con el par a 3,4 días de creado: precio $0,001106, mcap $918.516, liquidez $101.691.
  - Velas de 1 h de GeckoTerminal (84, desde 04/10/2026 21:00 UTC): apertura $0,00004616 · máximo $0,003649 (07/10/2026 12:00 UTC) · mínimo $0,00001725 (04/10/2026 22:00 UTC) · último cierre $0,001153.
  - En la consulta 08/10/2026 08:14 UTC: precio $0,001119, liquidez $102.262, FDV $929.477.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/10/2026 08:00 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001106 |
| Liquidez | $101.691 |
| MCap | $918.516 |
| Volumen 24 h | $1.265.825 |
| Cambio 24 h | -47% |
| Cambio m5 / h1 | -0,5% / +49,3% |
| Volumen m5 / h1 | $1.280 / $58.543 |
| Trades m5 (compras / ventas) | 5 / 6 |
| Edad del par | 3,4 días |
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

Desglose no reproducible desde los motivos registrados (suma 27 vs score 72; motivos sin regla: score de detección 72 (script_82, hace 2 min) > re-score 27: vale el de detección (paridad con script_97)): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-08T08:00:04+00:00, sin estado previo): **27** · motivos: WS score alto, MCap > $100K, Volumen masivo, Volumen activo m5 (>$1K), Par >24h, no nativo pump.fun, Liquidez alta, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 35 de 21.169 tokens analizados (0,17%) quedan ≥ 56. Con score 27, este activo queda en el percentil 97,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/10/2026 08:00 UTC, hasta 10/10/2026 08:00 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -0,5% · h1 +49,3% · h24 -47% · volumen m5/h1 0,02 · edad del par 3,4 días.
- **Precio de entrada** (alerta): $0,001106.
- **Consulta 08/10/2026 08:14 UTC:** $0,001119 (+1,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump_2026-10-08_080004.json` · blob `c8a6ac37ceb88791413b6d6384efd43a5f724f67` · commit `f3b0741` (2026-10-08T08:08:21Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-08_075321.json` · blob `eb095166559c1171aebe651e58f9b6b932e51e86` · commit `f3b0741` (2026-10-08T08:08:21Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-08_080004`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump · registro · 08/10/2026 08:00 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump · HTTP 200 · 08/10/2026 08:14 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump/report · HTTP 200 · 08/10/2026 08:14 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump · HTTP 200 · 08/10/2026 08:14 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/5a7QurJLARt146JajJYPe5nh6vLyFpN2QrHUSLqbsCZy/ohlcv/hour?limit=1000 · HTTP 200 · 08/10/2026 08:14 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump · HTTP 200 · 08/10/2026 08:14 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=GOMOUSDT · HTTP 400 · 08/10/2026 08:14 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/GOMO-USD · HTTP 404 · 08/10/2026 08:14 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $102.262 vs $156.065 → 34,47%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001119 vs $0,001153 → 2,98%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump_2026-10-08_080004.json',encoding='utf-8'));d=d.get('9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump',d);p=mock.patch('time.time',return_value=1791446404);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/10/2026 08:14 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `0e960d2b40d20c82…`
