# A Meme Dacity (AMD) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,002806 · liquidez $142.526 · mcap $2.769.644 (al detectar)  
Detectado el 06/11/2026 17:37 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 08/11/2026 17:38 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir AMD

Estudio de cómo se adquiere AMD, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/11/2026 17:38 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/11/2026 17:37 UTC | pumpswap `6ZV8dyR…J3rr` | $142.526 | 5% | 0,140% | 1,403% | 14,033% | $713 | $2.138 |
| consulta 06/11/2026 17:38 UTC | pumpswap `6ZV8dyR…J3rr` | $143.195 | 5% | 0,140% | 1,397% | 13,967% | $716 | $2.148 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump`
5. Configurar el slippage: 5% (liquidez $143.195, consulta 06/11/2026 17:38 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump) y el par en DexScreener (https://dexscreener.com/solana/6ZV8dyRdxH56Au2EbhpZZBMKpRP5ixBKPRJ7hB2pJ3rr); mint authority / freeze authority: revocada / revocada · holders 12.893 · top-10 3,55% (consulta 06/11/2026 17:38 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump
- Par en DexScreener: https://dexscreener.com/solana/6ZV8dyRdxH56Au2EbhpZZBMKpRP5ixBKPRJ7hB2pJ3rr
- Página del lanzamiento (pump.fun): https://pump.fun/coin/oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 12.893 · top-10 3,55% (consulta 06/11/2026 17:38 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | A Meme Dacity / AMD | registro de la detección (trending) |
| Mint / contrato | `oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6ZV8dyRdxH56Au2EbhpZZBMKpRP5ixBKPRJ7hB2pJ3rr` | DexScreener, al detectar (2 par(es) en la consulta 06/11/2026 17:38 UTC) |
| Deployer | `F8fd7TUcwiHz5w9PdeoLoc2SeMHzpyjKxNHmchJwM3go` | RugCheck `creator` |
| Par creado | 06/11/2026 02:31 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 15,1 h / 15,1 h / 15,1 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/11/2026 17:38 UTC |
| Holders / top-10 | 12.893 / 3,55% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/11/2026 17:38 UTC |
| Holders efectivos del top-10 | 1,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/11/2026 17:38 UTC |
| Etiquetas de RugCheck | «Copycat token» | RugCheck `risks[].name` (texto de la fuente), consulta 06/11/2026 17:38 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6ZV8dyRdxH56Au2EbhpZZBMKpRP5ixBKPRJ7hB2pJ3rr · Solscan: https://solscan.io/token/oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump · pump.fun: https://pump.fun/coin/oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump · web: http://amemedacity.lol/ · twitter: https://x.com/amemedacityonx · telegram: https://t.me/amemedacity_tg | consulta 06/11/2026 17:38 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/11/2026 17:38 UTC)
- **Historia:**
  - Par creado el 06/11/2026 02:31 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/11/2026 17:37 UTC, con el par a 15,1 h de creado: precio $0,002806, mcap $2.769.644, liquidez $142.526.
  - Velas de 1 h de GeckoTerminal (16, desde 06/11/2026 02:00 UTC): apertura $0,00009053 · máximo $0,003603 (06/11/2026 16:00 UTC) · mínimo $0,00003942 (06/11/2026 02:00 UTC) · último cierre $0,002826.
  - En la consulta 06/11/2026 17:38 UTC: precio $0,002832, liquidez $143.195, FDV $2.795.450.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/11/2026 17:37 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,002806 |
| Liquidez | $142.526 |
| MCap | $2.769.644 |
| Volumen 24 h | $3.288.279 |
| Cambio 24 h | +6.983% |
| Cambio m5 / h1 | +0,7% / -4,1% |
| Volumen m5 / h1 | $6.675 / $125.181 |
| Trades m5 (compras / ventas) | 711 / 369 |
| Edad del par | 15,1 h |
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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 79 × 0,3 | +23,6 |
| MCap | ≥ $1M | $2.769.644 | +25 |
| Volumen 24 h | ≥ $1M | $3.288.279 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 66% | +25 |
| Momentum | m5 > 0 y h1 > −5% (par maduro) | m5 +0,7% · h1 -4,1% | +10 |
| Volumen m5 | > $1K (par maduro) | $6.675 | +10 |
| Liquidez | ≥ $100K | $142.526 | +15 |
| Cambio 24 h | ≥ +50% | +6.983% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +6.983% · liq/mcap 5,1% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-06T17:37:43+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Momentum corto positivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=5.1% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 94 de 46.790 tokens analizados (0,20%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/11/2026 17:38 UTC, hasta 08/11/2026 17:38 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +0,7% · h1 -4,1% · h24 +6.983% · volumen m5/h1 0,05 · edad del par 15,1 h.
- **Precio de entrada** (alerta): $0,002806.
- **Consulta 06/11/2026 17:38 UTC:** $0,002832 (+0,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump_2026-11-06_173808.json` · blob `e44c4667e3062f2cb5d1c938f6f99dcbd0f820d2` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-06_173239.json` · blob `2af286a35d24307d3f1961177fb798e16aa5f10a` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-06_173808`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump · registro · 06/11/2026 17:37 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump · HTTP 200 · 06/11/2026 17:38 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump/report · HTTP 200 · 06/11/2026 17:38 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump · HTTP 200 · 06/11/2026 17:38 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6ZV8dyRdxH56Au2EbhpZZBMKpRP5ixBKPRJ7hB2pJ3rr/ohlcv/hour?limit=1000 · HTTP 200 · 06/11/2026 17:38 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump · HTTP 404 · 06/11/2026 17:38 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AMDUSDT · HTTP 400 · 06/11/2026 17:38 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AMD-USD · HTTP 404 · 06/11/2026 17:38 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $143.195 vs $142.037 → 0,81%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002832 vs $0,002826 → 0,23%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump_2026-11-06_173808.json',encoding='utf-8'));d=d.get('oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump',d);p=mock.patch('time.time',return_value=1793986663);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/11/2026 17:38 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `e1b8aebd29b07175…`
