# Believe in Something (Something) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001459 · liquidez $110.000 · mcap $1.453.962 (al detectar)  
Detectado el 28/10/2026 05:54 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 30/10/2026 05:54 UTC (< 48 h) · vigente: quedan 41,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Something

Estudio de cómo se adquiere Something, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 28/10/2026 12:02 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 28/10/2026 05:54 UTC | pumpswap `FAHXgxD…f9kk` | $110.000 | 5% | 0,182% | 1,818% | 18,182% | $550 | $1.650 |
| consulta 28/10/2026 12:02 UTC | pumpswap `FAHXgxD…f9kk` | $103.011 | 5% | 0,194% | 1,942% | 19,415% | $515 | $1.545 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump`
5. Configurar el slippage: 5% (liquidez $103.011, consulta 28/10/2026 12:02 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump) y el par en DexScreener (https://dexscreener.com/solana/FAHXgxDGMw5sfFW77SCHBcT9qiQ2ArrPzo98xJxMf9kk); mint authority / freeze authority: revocada / revocada · holders 3.608 · top-10 11,78% (consulta 28/10/2026 12:02 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump
- Par en DexScreener: https://dexscreener.com/solana/FAHXgxDGMw5sfFW77SCHBcT9qiQ2ArrPzo98xJxMf9kk
- Página del lanzamiento (pump.fun): https://pump.fun/coin/AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.608 · top-10 11,78% (consulta 28/10/2026 12:02 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Believe in Something / Something | registro de la detección (trending) |
| Mint / contrato | `AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `FAHXgxDGMw5sfFW77SCHBcT9qiQ2ArrPzo98xJxMf9kk` | DexScreener, al detectar (2 par(es) en la consulta 28/10/2026 12:02 UTC) |
| Deployer | `6vJjnQkrp7HF1Ns8EpAEMVLdtsX4ZeeHop7Uhn2cJu23` | RugCheck `creator` |
| Par creado | 27/10/2026 21:23 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 8,5 h / 8,5 h / 14,6 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 28/10/2026 12:02 UTC |
| Holders / top-10 | 3.608 / 11,78% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 28/10/2026 12:02 UTC |
| Holders efectivos del top-10 | 5,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 28/10/2026 12:02 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 28/10/2026 12:02 UTC |
| Links | DexScreener: https://dexscreener.com/solana/FAHXgxDGMw5sfFW77SCHBcT9qiQ2ArrPzo98xJxMf9kk · Solscan: https://solscan.io/token/AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump · pump.fun: https://pump.fun/coin/AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump · web: https://believeinsomethingpump.lol/ · twitter: https://x.com/SomethingToPump | consulta 28/10/2026 12:02 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 28/10/2026 12:02 UTC)
- **Historia:**
  - Par creado el 27/10/2026 21:23 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 28/10/2026 05:54 UTC, con el par a 8,5 h de creado: precio $0,001459, mcap $1.453.962, liquidez $110.000.
  - Velas de 1 h de GeckoTerminal (16, desde 27/10/2026 21:00 UTC): apertura $0,0001128 · máximo $0,002310 (28/10/2026 10:00 UTC) · mínimo $0,00005115 (27/10/2026 21:00 UTC) · último cierre $0,001211.
  - En la consulta 28/10/2026 12:02 UTC: precio $0,001193, liquidez $103.011, FDV $1.188.897.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 28/10/2026 05:54 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001459 |
| Liquidez | $110.000 |
| MCap | $1.453.962 |
| Volumen 24 h | $3.844.892 |
| Cambio 24 h | +2.730% |
| Cambio m5 / h1 | -0,9% / +22,2% |
| Volumen m5 / h1 | $11.506 / $220.555 |
| Trades m5 (compras / ventas) | 418 / 73 |
| Edad del par | 8,5 h |
| Score del feed (WS) | 86 |

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
| Score del feed | score WS × 0,3 | WS 86 × 0,3 | +25,7 |
| MCap | ≥ $1M | $1.453.962 | +25 |
| Volumen 24 h | ≥ $1M | $3.844.892 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 85% | +25 |
| Volumen m5 | > $1K (par maduro) | $11.506 | +10 |
| Liquidez | ≥ $100K | $110.000 | +15 |
| Cambio 24 h | ≥ +50% | +2.730% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +2.730% · liq/mcap 7,6% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-28T05:54:48+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=7.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 79 de 46.148 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 28/10/2026 05:54 UTC, hasta 30/10/2026 05:54 UTC · vigente: quedan 41,9 h.
- **Aceleración al detectar:** cambio m5 -0,9% · h1 +22,2% · h24 +2.730% · volumen m5/h1 0,05 · edad del par 8,5 h.
- **Precio de entrada** (alerta): $0,001459.
- **Consulta 28/10/2026 12:02 UTC:** $0,001193 (-18,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump_2026-10-28_055448.json` · blob `bba3a74afa7e07c1a7c3dcea30b4b8ddcd45c32e` · commit `0c1b7f8` (2026-10-28T11:54:19Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-28_054803.json` · blob `12e3ac175274276bf188ee0ddca2edf6d41df6fc` · commit `0c1b7f8` (2026-10-28T11:54:19Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-28_055448`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump · registro · 28/10/2026 05:54 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump · HTTP 200 · 28/10/2026 12:02 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump/report · HTTP 200 · 28/10/2026 12:02 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump · HTTP 200 · 28/10/2026 12:02 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/FAHXgxDGMw5sfFW77SCHBcT9qiQ2ArrPzo98xJxMf9kk/ohlcv/hour?limit=1000 · HTTP 200 · 28/10/2026 12:02 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump · HTTP 404 · 28/10/2026 12:02 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SOMETHINGUSDT · HTTP 400 · 28/10/2026 12:02 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SOMETHING-USD · HTTP 404 · 28/10/2026 12:02 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $103.011 vs $104.765 → 1,67%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001193 vs $0,001211 → 1,50%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump_2026-10-28_055448.json',encoding='utf-8'));d=d.get('AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump',d);p=mock.patch('time.time',return_value=1793166888);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 28/10/2026 12:02 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `22dde086491f31de…`
