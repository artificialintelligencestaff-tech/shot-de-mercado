# Hexncoin (HEXN) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0005473 · liquidez $67.057 · mcap $543.505 (al detectar)  
Detectado el 30/10/2026 03:57 UTC por: WS score muy alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 01/11/2026 03:57 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HEXN

Estudio de cómo se adquiere HEXN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 30/10/2026 03:57 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 30/10/2026 03:57 UTC | pumpswap `BQJzers…DKW4` | $67.057 | 5% | 0,298% | 2,983% | 29,826% | $335 | $1.006 |
| consulta 30/10/2026 03:57 UTC | pumpswap `BQJzers…DKW4` | $67.489 | 5% | 0,296% | 2,963% | 29,634% | $337 | $1.012 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump`
5. Configurar el slippage: 5% (liquidez $67.489, consulta 30/10/2026 03:57 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump) y el par en DexScreener (https://dexscreener.com/solana/BQJzersGUgNhav8C1m3VC4WA6MgQBAE8T2W7EpTSDKW4); mint authority / freeze authority: revocada / revocada · holders 7.539 · top-10 7,56% (consulta 30/10/2026 03:57 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump
- Par en DexScreener: https://dexscreener.com/solana/BQJzersGUgNhav8C1m3VC4WA6MgQBAE8T2W7EpTSDKW4
- Página del lanzamiento (pump.fun): https://pump.fun/coin/ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 7.539 · top-10 7,56% (consulta 30/10/2026 03:57 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Hexncoin / HEXN | registro de la detección (trending) |
| Mint / contrato | `ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BQJzersGUgNhav8C1m3VC4WA6MgQBAE8T2W7EpTSDKW4` | DexScreener, al detectar (2 par(es) en la consulta 30/10/2026 03:57 UTC) |
| Deployer | `C2gVV4j6wbi9Yn9HVK31CRHkn4Mt6QeQ6utcgwvTqNMR` | RugCheck `creator` |
| Par creado | 29/10/2026 16:56 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,0 h / 11,0 h / 11,0 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 30/10/2026 03:57 UTC |
| Holders / top-10 | 7.539 / 7,56% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 30/10/2026 03:57 UTC |
| Holders efectivos del top-10 | 1,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 30/10/2026 03:57 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 30/10/2026 03:57 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BQJzersGUgNhav8C1m3VC4WA6MgQBAE8T2W7EpTSDKW4 · Solscan: https://solscan.io/token/ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump · pump.fun: https://pump.fun/coin/ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump · web: https://hexncoin.org/ · twitter: https://x.com/HexncoinSol | consulta 30/10/2026 03:57 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 30/10/2026 03:57 UTC)
- **Historia:**
  - Par creado el 29/10/2026 16:56 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 30/10/2026 03:57 UTC, con el par a 11,0 h de creado: precio $0,0005473, mcap $543.505, liquidez $67.057.
  - Velas de 1 h de GeckoTerminal (12, desde 29/10/2026 16:00 UTC): apertura $0,0001384 · máximo $0,001820 (29/10/2026 19:00 UTC) · mínimo $0,00005162 (29/10/2026 16:00 UTC) · último cierre $0,0005678.
  - En la consulta 30/10/2026 03:57 UTC: precio $0,0005542, liquidez $67.489, FDV $550.316.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 30/10/2026 03:57 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0005473 |
| Liquidez | $67.057 |
| MCap | $543.505 |
| Volumen 24 h | $3.898.649 |
| Cambio 24 h | +952% |
| Cambio m5 / h1 | -3,0% / +29,7% |
| Volumen m5 / h1 | $14.189 / $170.464 |
| Trades m5 (compras / ventas) | 427 / 77 |
| Edad del par | 11,0 h |
| Score del feed (WS) | 91 |

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
| Score del feed | score WS × 0,3 | WS 91 × 0,3 | +27,2 |
| MCap | ≥ $100K | $543.505 | +15 |
| Volumen 24 h | ≥ $1M | $3.898.649 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 85% | +25 |
| Volumen m5 | > $1K (par maduro) | $14.189 | +10 |
| Liquidez | ≥ $50K | $67.057 | +10 |
| Cambio 24 h | ≥ +50% | +952% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +952% · liq/mcap 12,3% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-30T03:57:19+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=12.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 82 de 46.289 tokens analizados (0,18%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 30/10/2026 03:57 UTC, hasta 01/11/2026 03:57 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -3,0% · h1 +29,7% · h24 +952% · volumen m5/h1 0,08 · edad del par 11,0 h.
- **Precio de entrada** (alerta): $0,0005473.
- **Consulta 30/10/2026 03:57 UTC:** $0,0005542 (+1,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump_2026-10-30_035735.json` · blob `8f559de2b03732840cfe16e9d9690582d6fa27f1` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-30_035212.json` · blob `edf49718e4ca503d6d428712c7e22e7c02f5db6c` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-30_035735`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump · registro · 30/10/2026 03:57 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump · HTTP 200 · 30/10/2026 03:57 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump/report · HTTP 200 · 30/10/2026 03:57 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump · HTTP 200 · 30/10/2026 03:57 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BQJzersGUgNhav8C1m3VC4WA6MgQBAE8T2W7EpTSDKW4/ohlcv/hour?limit=1000 · HTTP 200 · 30/10/2026 03:57 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump · HTTP 404 · 30/10/2026 03:57 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HEXNUSDT · HTTP 400 · 30/10/2026 03:57 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HEXN-USD · HTTP 404 · 30/10/2026 03:57 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $67.489 vs $66.973 → 0,76%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0005542 vs $0,0005678 → 2,39%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump_2026-10-30_035735.json',encoding='utf-8'));d=d.get('ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump',d);p=mock.patch('time.time',return_value=1793332639);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint ANVLA6eKiAq4nstD2Sg3SZhfVkSEwfnGccn12UQWpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 30/10/2026 03:57 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `a2df9e2780935f7c…`
