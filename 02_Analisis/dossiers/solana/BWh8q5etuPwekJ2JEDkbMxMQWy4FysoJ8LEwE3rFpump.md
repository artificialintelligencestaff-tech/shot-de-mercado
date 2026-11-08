# Gigahug (GIGAHUG) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001160 · liquidez $88.703 · mcap $1.153.879 (al detectar)  
Detectado el 08/11/2026 09:11 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 10/11/2026 09:11 UTC (< 48 h) · vigente: quedan 41,1 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir GIGAHUG

Estudio de cómo se adquiere GIGAHUG, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/11/2026 16:06 UTC; CoinGecko sin pares de este contrato en esos exchanges).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/11/2026 09:11 UTC | pumpswap `BrkcwRY…R8yt` | $88.703 | 5% | 0,225% | 2,255% | 22,547% | $444 | $1.331 |
| consulta 08/11/2026 16:06 UTC | pumpswap `BrkcwRY…R8yt` | $67.307 | 5% | 0,297% | 2,971% | 29,715% | $337 | $1.010 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump`
5. Configurar el slippage: 5% (liquidez $67.307, consulta 08/11/2026 16:06 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump) y el par en DexScreener (https://dexscreener.com/solana/BrkcwRYAJ22Fgqh6GgeLbRmUEdXx7yLhNcAAsAJoR8yt); mint authority / freeze authority: revocada / revocada · holders 11.293 · top-10 6,62% (consulta 08/11/2026 16:06 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump
- Par en DexScreener: https://dexscreener.com/solana/BrkcwRYAJ22Fgqh6GgeLbRmUEdXx7yLhNcAAsAJoR8yt
- Página del lanzamiento (pump.fun): https://pump.fun/coin/BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 11.293 · top-10 6,62% (consulta 08/11/2026 16:06 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Gigahug / GIGAHUG | registro de la detección (trending) |
| Mint / contrato | `BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BrkcwRYAJ22Fgqh6GgeLbRmUEdXx7yLhNcAAsAJoR8yt` | DexScreener, al detectar (3 par(es) en la consulta 08/11/2026 16:06 UTC) |
| Deployer | `F4LaPF2AgWjmamgVdkzFYw8NZQhGvHSPKmucG192DmXb` | RugCheck `creator` |
| Par creado | 07/11/2026 20:34 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 12,6 h / 12,6 h / 19,5 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/11/2026 16:06 UTC |
| Holders / top-10 | 11.293 / 6,62% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/11/2026 16:06 UTC |
| Holders efectivos del top-10 | 1,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; orca 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/11/2026 16:06 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 08/11/2026 16:06 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BrkcwRYAJ22Fgqh6GgeLbRmUEdXx7yLhNcAAsAJoR8yt · Solscan: https://solscan.io/token/BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump · pump.fun: https://pump.fun/coin/BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump · web: https://gigahug.top/ · twitter: https://x.com/gigahug_sol · telegram: https://t.me/gigahug_meme | consulta 08/11/2026 16:06 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** CoinGecko: Solana Ecosystem, Meme, Pump.fun Ecosystem · scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/11/2026 16:06 UTC)
- **Historia:**
  - Par creado el 07/11/2026 20:34 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/11/2026 09:11 UTC, con el par a 12,6 h de creado: precio $0,001160, mcap $1.153.879, liquidez $88.703.
  - Velas de 1 h de GeckoTerminal (21, desde 07/11/2026 20:00 UTC): apertura $0,0002773 · máximo $0,001629 (08/11/2026 09:00 UTC) · mínimo $0,00005807 (07/11/2026 20:00 UTC) · último cierre $0,0006443.
  - En la consulta 08/11/2026 16:06 UTC: precio $0,0006507, liquidez $67.307, FDV $647.155.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/11/2026 09:11 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001160 |
| Liquidez | $88.703 |
| MCap | $1.153.879 |
| Volumen 24 h | $1.902.253 |
| Cambio 24 h | +1.898% |
| Cambio m5 / h1 | -2,2% / +7,4% |
| Volumen m5 / h1 | $6.437 / $101.843 |
| Trades m5 (compras / ventas) | 588 / 362 |
| Edad del par | 12,6 h |
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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 70 × 0,3 | +21,0 |
| MCap | ≥ $1M | $1.153.879 | +25 |
| Volumen 24 h | ≥ $1M | $1.902.253 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 62% | +25 |
| Volumen m5 | > $1K (par maduro) | $6.437 | +10 |
| Liquidez | ≥ $50K | $88.703 | +10 |
| Cambio 24 h | ≥ +50% | +1.898% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.898% · liq/mcap 7,7% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-08T09:11:01+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=7.7% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 94 de 46.912 tokens analizados (0,20%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/11/2026 09:11 UTC, hasta 10/11/2026 09:11 UTC · vigente: quedan 41,1 h.
- **Aceleración al detectar:** cambio m5 -2,2% · h1 +7,4% · h24 +1.898% · volumen m5/h1 0,06 · edad del par 12,6 h.
- **Precio de entrada** (alerta): $0,001160.
- **Consulta 08/11/2026 16:06 UTC:** $0,0006507 (-43,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump_2026-11-08_091101.json` · blob `8ee97e17bb71cedde436a788cbc7e7a25cb378a3` · commit `9896775` (2026-11-08T15:56:04Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-08_090407.json` · blob `d06f8cc564f7fa8d312011cfd623efab85710e65` · commit `9896775` (2026-11-08T15:56:04Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-08_091101`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump · registro · 08/11/2026 09:11 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump · HTTP 200 · 08/11/2026 16:06 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump/report · HTTP 200 · 08/11/2026 16:06 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump · HTTP 200 · 08/11/2026 16:06 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BrkcwRYAJ22Fgqh6GgeLbRmUEdXx7yLhNcAAsAJoR8yt/ohlcv/hour?limit=1000 · HTTP 200 · 08/11/2026 16:06 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump · HTTP 200 · 08/11/2026 16:06 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=GIGAHUGUSDT · HTTP 400 · 08/11/2026 16:06 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/GIGAHUG-USD · HTTP 404 · 08/11/2026 16:06 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $67.307 vs $67.221 → 0,13%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0006507 vs $0,0006443 → 0,98%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump_2026-11-08_091101.json',encoding='utf-8'));d=d.get('BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump',d);p=mock.patch('time.time',return_value=1794129061);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint BWh8q5etuPwekJ2JEDkbMxMQWy4FysoJ8LEwE3rFpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/11/2026 16:06 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `229825406401707a…`
