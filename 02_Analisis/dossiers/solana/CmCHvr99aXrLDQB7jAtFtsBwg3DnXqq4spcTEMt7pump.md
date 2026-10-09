# Owl Nighter (OWLNIGHT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0005260 · liquidez $70.945 · mcap $522.081 (al detectar)  
Detectado el 09/10/2026 08:41 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 11/10/2026 08:41 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir OWLNIGHT

Estudio de cómo se adquiere OWLNIGHT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 09/10/2026 08:59 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 09/10/2026 08:41 UTC | pumpswap `BGT9hRw…pdcy` | $70.945 | 5% | 0,282% | 2,819% | 28,191% | $355 | $1.064 |
| consulta 09/10/2026 08:59 UTC | pumpswap `BGT9hRw…pdcy` | $69.962 | 5% | 0,286% | 2,859% | 28,587% | $350 | $1.049 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump`
5. Configurar el slippage: 5% (liquidez $69.962, consulta 09/10/2026 08:59 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump) y el par en DexScreener (https://dexscreener.com/solana/BGT9hRweDn8TjWHrw14zYsHXRG5SxHJMHRvSrTW1pdcy); mint authority / freeze authority: revocada / revocada · holders 16.228 · top-10 9,23% (consulta 09/10/2026 08:59 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump
- Par en DexScreener: https://dexscreener.com/solana/BGT9hRweDn8TjWHrw14zYsHXRG5SxHJMHRvSrTW1pdcy
- Página del lanzamiento (pump.fun): https://pump.fun/coin/CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 16.228 · top-10 9,23% (consulta 09/10/2026 08:59 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Owl Nighter / OWLNIGHT | registro de la detección (trending) |
| Mint / contrato | `CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BGT9hRweDn8TjWHrw14zYsHXRG5SxHJMHRvSrTW1pdcy` | DexScreener, al detectar (3 par(es) en la consulta 09/10/2026 08:59 UTC) |
| Deployer | `3GrJNLixQ11WYmpFtWoTDUSJLyYZbzg9R31XiBJTgXZr` | RugCheck `creator` |
| Par creado | 08/10/2026 16:58 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 15,7 h / 15,7 h / 16,0 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 09/10/2026 08:59 UTC |
| Holders / top-10 | 16.228 / 9,23% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 09/10/2026 08:59 UTC |
| Holders efectivos del top-10 | 1,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 09/10/2026 08:59 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 09/10/2026 08:59 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BGT9hRweDn8TjWHrw14zYsHXRG5SxHJMHRvSrTW1pdcy · Solscan: https://solscan.io/token/CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump · pump.fun: https://pump.fun/coin/CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump · web: https://www.owlnight.top · twitter: https://x.com/owlnight_meme | consulta 09/10/2026 08:59 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 09/10/2026 08:59 UTC)
- **Historia:**
  - Par creado el 08/10/2026 16:58 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 09/10/2026 08:41 UTC, con el par a 15,7 h de creado: precio $0,0005260, mcap $522.081, liquidez $70.945.
  - Velas de 1 h de GeckoTerminal (17, desde 08/10/2026 16:00 UTC): apertura $0,00006477 · máximo $0,001249 (09/10/2026 05:00 UTC) · mínimo $0,00006477 (08/10/2026 16:00 UTC) · último cierre $0,0005203.
  - En la consulta 09/10/2026 08:59 UTC: precio $0,0005096, liquidez $69.962, FDV $505.750.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 09/10/2026 08:41 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0005260 |
| Liquidez | $70.945 |
| MCap | $522.081 |
| Volumen 24 h | $4.776.762 |
| Cambio 24 h | +707% |
| Cambio m5 / h1 | -1,5% / -34,5% |
| Volumen m5 / h1 | $11.947 / $289.892 |
| Trades m5 (compras / ventas) | 458 / 96 |
| Edad del par | 15,7 h |
| Score del feed (WS) | 77 |

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
| Score del feed | score WS × 0,3 | WS 77 × 0,3 | +23,0 |
| MCap | ≥ $100K | $522.081 | +15 |
| Volumen 24 h | ≥ $1M | $4.776.762 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 83% | +25 |
| Volumen m5 | > $1K (par maduro) | $11.947 | +10 |
| Liquidez | ≥ $50K | $70.945 | +10 |
| Cambio 24 h | ≥ +50% | +707% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +707% · liq/mcap 13,6% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-09T08:41:40+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=13.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 42 de 24.312 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 09/10/2026 08:41 UTC, hasta 11/10/2026 08:41 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -1,5% · h1 -34,5% · h24 +707% · volumen m5/h1 0,04 · edad del par 15,7 h.
- **Precio de entrada** (alerta): $0,0005260.
- **Consulta 09/10/2026 08:59 UTC:** $0,0005096 (-3,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump_2026-10-09_084140.json` · blob `ba528932ccc1b8d83bb5e47186aa7ab65df4dbdc` · commit `43748d0` (2026-10-09T08:53:29Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-09_083555.json` · blob `2768220adc3c45a406644885ef4ed82448e6dce0` · commit `43748d0` (2026-10-09T08:53:29Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-09_084140`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump · registro · 09/10/2026 08:41 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump · HTTP 200 · 09/10/2026 08:59 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump/report · HTTP 200 · 09/10/2026 08:59 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump · HTTP 200 · 09/10/2026 08:59 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BGT9hRweDn8TjWHrw14zYsHXRG5SxHJMHRvSrTW1pdcy/ohlcv/hour?limit=1000 · HTTP 200 · 09/10/2026 08:59 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump · HTTP 404 · 09/10/2026 08:59 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=OWLNIGHTUSDT · HTTP 400 · 09/10/2026 08:59 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/OWLNIGHT-USD · HTTP 404 · 09/10/2026 08:59 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $69.962 vs $70.275 → 0,45%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0005096 vs $0,0005203 → 2,05%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump_2026-10-09_084140.json',encoding='utf-8'));d=d.get('CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump',d);p=mock.patch('time.time',return_value=1791535300);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint CmCHvr99aXrLDQB7jAtFtsBwg3DnXqq4spcTEMt7pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 09/10/2026 08:59 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `222a5952521e0203…`
