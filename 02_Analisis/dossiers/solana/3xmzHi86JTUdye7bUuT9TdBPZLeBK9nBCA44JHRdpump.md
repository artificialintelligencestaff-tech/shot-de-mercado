# AUDACITY ROADSTER (Audaster) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000002484 · liquidez $2.811 · mcap $2.474 (al detectar)  
Detectado el 17/10/2026 00:04 UTC por: WS score muy alto, MCap bajo, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 19/10/2026 00:04 UTC (< 48 h) · vigente: quedan 46,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Audaster

Estudio de cómo se adquiere Audaster, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 17/10/2026 01:18 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 17/10/2026 00:04 UTC | pumpswap `3QNg1RK…GR4f` | $2.811 | 10% | 7,115% | 71,150% | 711,503% | $14 | $42 |
| consulta 17/10/2026 01:18 UTC | pumpswap `3QNg1RK…GR4f` | $2.746 | 10% | 7,284% | 72,839% | 728,390% | $14 | $41 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump`
5. Configurar el slippage: 10% (liquidez $2.746, consulta 17/10/2026 01:18 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump) y el par en DexScreener (https://dexscreener.com/solana/3QNg1RKG3xH4d4snKmdC5vF6CCP8SBBEfy3NWpT8GR4f); mint authority / freeze authority: revocada / revocada · holders 396 · top-10 99,58% (consulta 17/10/2026 01:18 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump
- Par en DexScreener: https://dexscreener.com/solana/3QNg1RKG3xH4d4snKmdC5vF6CCP8SBBEfy3NWpT8GR4f
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 396 · top-10 99,58% (consulta 17/10/2026 01:18 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | AUDACITY ROADSTER / Audaster | registro de la detección (trending) |
| Mint / contrato | `3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `3QNg1RKG3xH4d4snKmdC5vF6CCP8SBBEfy3NWpT8GR4f` | DexScreener, al detectar (4 par(es) en la consulta 17/10/2026 01:18 UTC) |
| Deployer | `AsMnEHpsPtV2mymQeWhD2QkZj4a7LV7i77sSmiX5Vh5v` | RugCheck `creator` |
| Par creado | 16/10/2026 13:30 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,6 h / 10,6 h / 11,8 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 17/10/2026 01:18 UTC |
| Holders / top-10 | 396 / 99,58% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 17/10/2026 01:18 UTC |
| Holders efectivos del top-10 | 1,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 17/10/2026 01:18 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 17/10/2026 01:18 UTC |
| Links | DexScreener: https://dexscreener.com/solana/3QNg1RKG3xH4d4snKmdC5vF6CCP8SBBEfy3NWpT8GR4f · Solscan: https://solscan.io/token/3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump · pump.fun: https://pump.fun/coin/3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump · web: https://audaster.fun · twitter: https://x.com/Audaster | consulta 17/10/2026 01:18 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 17/10/2026 01:18 UTC)
- **Historia:**
  - Par creado el 16/10/2026 13:30 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 17/10/2026 00:04 UTC, con el par a 10,6 h de creado: precio $0,000002484, mcap $2.474, liquidez $2.811.
  - Velas de 1 h de GeckoTerminal (10, desde 16/10/2026 13:00 UTC): apertura $0,0003251 · máximo $0,002855 (16/10/2026 14:00 UTC) · mínimo $0,000002415 (17/10/2026 00:00 UTC) · último cierre $0,000002415.
  - En la consulta 17/10/2026 01:18 UTC: precio $0,000002415, liquidez $2.746, FDV $2.405.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 17/10/2026 00:04 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000002484 |
| Liquidez | $2.811 |
| MCap | $2.474 |
| Volumen 24 h | $3.525.546 |
| Cambio 24 h | -96% |
| Cambio m5 / h1 | +1,9% / +1,9% |
| Volumen m5 / h1 | $1 / $1 |
| Trades m5 (compras / ventas) | 1 / 0 |
| Edad del par | 10,6 h |
| Score del feed (WS) | 84 |

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
| Score del feed | score WS × 0,3 | WS 84 × 0,3 | +25,1 |
| MCap | < $50K | $2.474 | +0 |
| Volumen 24 h | ≥ $1M | $3.525.546 | +20 |
| Volumen m5/h1 | > 0,5 (par maduro) | 1,00 | +25 |
| Trades m5/h1 | > 0,5 (par maduro) | 1,00 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 100% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +1,9% · h1 +1,9% | +20 |
| Liquidez | < $20K | $2.811 | +0 |
| Cambio 24 h | ≤ −30% | -96% | -5 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-17T00:04:40+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap bajo, Volumen masivo, Volumen acelerado (5m/1h > 50%), Trades acelerados (5m/1h > 50%), Buy pressure >60%, Momentum corto+medio positivo, Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 62 de 37.848 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 17/10/2026 00:04 UTC, hasta 19/10/2026 00:04 UTC · vigente: quedan 46,8 h.
- **Aceleración al detectar:** cambio m5 +1,9% · h1 +1,9% · h24 -96% · volumen m5/h1 1,00 · edad del par 10,6 h.
- **Precio de entrada** (alerta): $0,000002484.
- **Consulta 17/10/2026 01:18 UTC:** $0,000002415 (-2,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump_2026-10-17_000440.json` · blob `4498a44f1cc51a701c811decba1bbeffecf86b55` · commit `c30aadc` (2026-10-17T01:11:07Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-16_235816.json` · blob `dfdb062b060766e421a26b135c39863812cb83d0` · commit `c30aadc` (2026-10-17T01:11:07Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-17_000440`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump · registro · 17/10/2026 00:04 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump · HTTP 200 · 17/10/2026 01:18 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump/report · HTTP 200 · 17/10/2026 01:18 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump · HTTP 200 · 17/10/2026 01:18 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/3QNg1RKG3xH4d4snKmdC5vF6CCP8SBBEfy3NWpT8GR4f/ohlcv/hour?limit=1000 · HTTP 200 · 17/10/2026 01:18 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump · HTTP 404 · 17/10/2026 01:18 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AUDASTERUSDT · HTTP 400 · 17/10/2026 01:18 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AUDASTER-USD · HTTP 404 · 17/10/2026 01:18 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.746 vs $2.763 → 0,62%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002415 vs $0,000002415 → 0,00%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump_2026-10-17_000440.json',encoding='utf-8'));d=d.get('3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump',d);p=mock.patch('time.time',return_value=1792195480);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3xmzHi86JTUdye7bUuT9TdBPZLeBK9nBCA44JHRdpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 17/10/2026 01:18 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `38cf72b71b826f1a…`
