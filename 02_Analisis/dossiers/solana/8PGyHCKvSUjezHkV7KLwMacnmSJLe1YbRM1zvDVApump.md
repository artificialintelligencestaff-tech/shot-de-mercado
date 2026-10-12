# Sean Dynasty Prosper (SEAN) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,002011 · liquidez $130.094 · mcap $1.991.469 (al detectar)  
Detectado el 12/10/2026 01:44 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 14/10/2026 01:44 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SEAN

Estudio de cómo se adquiere SEAN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 12/10/2026 02:00 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 12/10/2026 01:44 UTC | pumpswap `CnVst3s…1nvJ` | $130.094 | 5% | 0,154% | 1,537% | 15,373% | $650 | $1.951 |
| consulta 12/10/2026 02:00 UTC | pumpswap `CnVst3s…1nvJ` | $116.739 | 5% | 0,171% | 1,713% | 17,132% | $584 | $1.751 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump`
5. Configurar el slippage: 5% (liquidez $116.739, consulta 12/10/2026 02:00 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump) y el par en DexScreener (https://dexscreener.com/solana/CnVst3sUYmo1GFYgnaNgygpQhwTNZzmb59wyyzQF1nvJ); mint authority / freeze authority: revocada / revocada · holders 5.996 · top-10 6,85% (consulta 12/10/2026 02:00 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump
- Par en DexScreener: https://dexscreener.com/solana/CnVst3sUYmo1GFYgnaNgygpQhwTNZzmb59wyyzQF1nvJ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.996 · top-10 6,85% (consulta 12/10/2026 02:00 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Sean Dynasty Prosper / SEAN | registro de la detección (trending) |
| Mint / contrato | `8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `CnVst3sUYmo1GFYgnaNgygpQhwTNZzmb59wyyzQF1nvJ` | DexScreener, al detectar (2 par(es) en la consulta 12/10/2026 02:00 UTC) |
| Deployer | `GftdVYUDaZzLD4KynoHm4BbUKvxofn2fu2YyrZ8eLeMS` | RugCheck `creator` |
| Par creado | 12/10/2026 00:37 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 67,0 min / 67,0 min / 83,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 12/10/2026 02:00 UTC |
| Holders / top-10 | 5.996 / 6,85% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 12/10/2026 02:00 UTC |
| Holders efectivos del top-10 | 3,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 12/10/2026 02:00 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 12/10/2026 02:00 UTC |
| Links | DexScreener: https://dexscreener.com/solana/CnVst3sUYmo1GFYgnaNgygpQhwTNZzmb59wyyzQF1nvJ · Solscan: https://solscan.io/token/8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump · pump.fun: https://pump.fun/coin/8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump · web: https://seandynasty.me · twitter: https://x.com/SeanDynastyX | consulta 12/10/2026 02:00 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 12/10/2026 02:00 UTC)
- **Historia:**
  - Par creado el 12/10/2026 00:37 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 12/10/2026 01:44 UTC, con el par a 67,0 min de creado: precio $0,002011, mcap $1.991.469, liquidez $130.094.
  - Velas de 1 h de GeckoTerminal (3, desde 12/10/2026 00:00 UTC): apertura $0,0001284 · máximo $0,002711 (12/10/2026 01:00 UTC) · mínimo $0,00005543 (12/10/2026 00:00 UTC) · último cierre $0,001629.
  - En la consulta 12/10/2026 02:00 UTC: precio $0,001624, liquidez $116.739, FDV $1.608.026.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 12/10/2026 01:44 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,002011 |
| Liquidez | $130.094 |
| MCap | $1.991.469 |
| Volumen 24 h | $1.976.217 |
| Cambio 24 h | +1.468% |
| Cambio m5 / h1 | -7,9% / +601,0% |
| Volumen m5 / h1 | $19.857 / $1.733.914 |
| Trades m5 (compras / ventas) | 421 / 284 |
| Edad del par | 67,0 min |
| Score del feed (WS) | 82 |

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
| Score del feed | score WS × 0,3 | WS 82 × 0,3 | +24,5 |
| MCap | ≥ $1M | $1.991.469 | +25 |
| Volumen 24 h | ≥ $1M | $1.976.217 | +20 |
| Buy pressure m5 | > 55% (par maduro) | 60% | +15 |
| Edge temprano | edad < 4 h (par maduro) | edad 67,0 min | +8 |
| Volumen m5 | > $1K (par maduro) | $19.857 | +10 |
| Liquidez | ≥ $100K | $130.094 | +15 |
| Cambio 24 h | ≥ +50% | +1.468% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.468% · liq/mcap 6,5% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-12T01:44:04+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >55%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=6.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 50 de 30.342 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 12/10/2026 01:44 UTC, hasta 14/10/2026 01:44 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -7,9% · h1 +601,0% · h24 +1.468% · volumen m5/h1 0,01 · edad del par 67,0 min.
- **Precio de entrada** (alerta): $0,002011.
- **Consulta 12/10/2026 02:00 UTC:** $0,001624 (-19,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump_2026-10-12_014404.json` · blob `720325931c20e3e8300dabacedf1515365f33adf` · commit `f8ec1f4` (2026-10-12T01:54:10Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-12_013638.json` · blob `29a5f62a5776cd586c72f1ab96af651069e56be5` · commit `f8ec1f4` (2026-10-12T01:54:10Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-12_014404`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump · registro · 12/10/2026 01:44 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump · HTTP 200 · 12/10/2026 02:00 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump/report · HTTP 200 · 12/10/2026 02:00 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump · HTTP 200 · 12/10/2026 02:00 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/CnVst3sUYmo1GFYgnaNgygpQhwTNZzmb59wyyzQF1nvJ/ohlcv/hour?limit=1000 · HTTP 200 · 12/10/2026 02:00 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump · HTTP 404 · 12/10/2026 02:00 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SEANUSDT · HTTP 400 · 12/10/2026 02:00 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SEAN-USD · HTTP 404 · 12/10/2026 02:00 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $116.739 vs $120.320 → 2,98%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001624 vs $0,001629 → 0,29%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump_2026-10-12_014404.json',encoding='utf-8'));d=d.get('8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump',d);p=mock.patch('time.time',return_value=1791769444);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8PGyHCKvSUjezHkV7KLwMacnmSJLe1YbRM1zvDVApump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 12/10/2026 02:00 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `00550558375f6a5a…`
