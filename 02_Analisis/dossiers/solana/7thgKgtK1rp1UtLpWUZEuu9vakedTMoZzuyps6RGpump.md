# Kimchi Coin (KIMCHI) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,01480 · liquidez $357.329 · mcap $14.753.135 (al detectar)  
Detectado el 21/10/2026 01:56 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 23/10/2026 01:56 UTC (< 48 h) · vigente: quedan 46,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir KIMCHI

Estudio de cómo se adquiere KIMCHI, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 21/10/2026 03:00 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 21/10/2026 01:56 UTC | pumpswap `AYq1Hkk…vPzD` | $357.329 | 3% | 0,056% | 0,560% | 5,597% | $1.787 | $5.360 |
| consulta 21/10/2026 02:59 UTC | pumpswap `AYq1Hkk…vPzD` | $306.881 | 3% | 0,065% | 0,652% | 6,517% | $1.534 | $4.603 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump`
5. Configurar el slippage: 3% (liquidez $306.881, consulta 21/10/2026 02:59 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump) y el par en DexScreener (https://dexscreener.com/solana/AYq1Hkkkq6oitjCNbDEYUo9AHHo6FLaXjuybmLBvvPzD); mint authority / freeze authority: revocada / revocada · holders 8.180 · top-10 15,24% (consulta 21/10/2026 02:59 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump
- Par en DexScreener: https://dexscreener.com/solana/AYq1Hkkkq6oitjCNbDEYUo9AHHo6FLaXjuybmLBvvPzD
- Página del lanzamiento (pump.fun): https://pump.fun/coin/7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 8.180 · top-10 15,24% (consulta 21/10/2026 02:59 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Kimchi Coin / KIMCHI | registro de la detección (trending) |
| Mint / contrato | `7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `AYq1Hkkkq6oitjCNbDEYUo9AHHo6FLaXjuybmLBvvPzD` | DexScreener, al detectar (7 par(es) en la consulta 21/10/2026 02:59 UTC) |
| Deployer | `4Y1M1FNNaggYnje1fCzG4PmBVm7qMqa6RBiZFbLCjmDz` | RugCheck `creator` |
| Par creado | 20/10/2026 23:50 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 2,1 h / 2,1 h / 3,2 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 21/10/2026 02:59 UTC |
| Holders / top-10 | 8.180 / 15,24% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 21/10/2026 02:59 UTC |
| Holders efectivos del top-10 | 10,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 21/10/2026 02:59 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 21/10/2026 02:59 UTC |
| Links | DexScreener: https://dexscreener.com/solana/AYq1Hkkkq6oitjCNbDEYUo9AHHo6FLaXjuybmLBvvPzD · Solscan: https://solscan.io/token/7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump · pump.fun: https://pump.fun/coin/7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump · web: https://kimchicoin.life · twitter: https://x.com/KimChcoinX | consulta 21/10/2026 02:59 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 21/10/2026 02:59 UTC)
- **Historia:**
  - Par creado el 20/10/2026 23:50 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 21/10/2026 01:56 UTC, con el par a 2,1 h de creado: precio $0,01480, mcap $14.753.135, liquidez $357.329.
  - Velas de 1 h de GeckoTerminal (4, desde 20/10/2026 23:00 UTC): apertura $0,0003694 · máximo $0,01515 (21/10/2026 01:00 UTC) · mínimo $0,00005810 (20/10/2026 23:00 UTC) · último cierre $0,01099.
  - En la consulta 21/10/2026 02:59 UTC: precio $0,01092, liquidez $306.881, FDV $10.894.299.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 21/10/2026 01:56 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,01480 |
| Liquidez | $357.329 |
| MCap | $14.753.135 |
| Volumen 24 h | $7.229.328 |
| Cambio 24 h | +25.168% |
| Cambio m5 / h1 | +16,8% / +32,2% |
| Volumen m5 / h1 | $287.260 / $2.030.561 |
| Trades m5 (compras / ventas) | 1.250 / 538 |
| Edad del par | 2,1 h |
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
| MCap | ≥ $1M | $14.753.135 | +25 |
| Volumen 24 h | ≥ $1M | $7.229.328 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 70% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +16,8% · h1 +32,2% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 2,1 h | +8 |
| Volumen m5 | > $1K (par maduro) | $287.260 | +10 |
| Liquidez | ≥ $100K | $357.329 | +15 |
| Cambio 24 h | ≥ +50% | +25.168% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap < 3% | +25.168% · liq/mcap 2,4% | -15 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-21T01:56:23+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=2.4% <3%.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 71 de 42.672 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 21/10/2026 01:56 UTC, hasta 23/10/2026 01:56 UTC · vigente: quedan 46,9 h.
- **Aceleración al detectar:** cambio m5 +16,8% · h1 +32,2% · h24 +25.168% · volumen m5/h1 0,14 · edad del par 2,1 h.
- **Precio de entrada** (alerta): $0,01480.
- **Consulta 21/10/2026 02:59 UTC:** $0,01092 (-26,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump_2026-10-21_015623.json` · blob `786b850fd626042c7c38afa0ccb78735763f05fc` · commit `49726ad` (2026-10-21T02:52:08Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-21_014933.json` · blob `b6c7726ca19ed036cf688fba25a1b9262124efef` · commit `49726ad` (2026-10-21T02:52:08Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-21_015623`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump · registro · 21/10/2026 01:56 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump · HTTP 200 · 21/10/2026 02:59 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump/report · HTTP 200 · 21/10/2026 02:59 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump · HTTP 200 · 21/10/2026 02:59 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/AYq1Hkkkq6oitjCNbDEYUo9AHHo6FLaXjuybmLBvvPzD/ohlcv/hour?limit=1000 · HTTP 200 · 21/10/2026 03:00 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump · HTTP 404 · 21/10/2026 03:00 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=KIMCHIUSDT · HTTP 400 · 21/10/2026 03:00 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/KIMCHI-USD · HTTP 404 · 21/10/2026 03:00 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $306.881 vs $307.241 → 0,12%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,01092 vs $0,01099 → 0,64%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump_2026-10-21_015623.json',encoding='utf-8'));d=d.get('7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump',d);p=mock.patch('time.time',return_value=1792547783);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 7thgKgtK1rp1UtLpWUZEuu9vakedTMoZzuyps6RGpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 21/10/2026 03:00 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `4478a475d06980a7…`
