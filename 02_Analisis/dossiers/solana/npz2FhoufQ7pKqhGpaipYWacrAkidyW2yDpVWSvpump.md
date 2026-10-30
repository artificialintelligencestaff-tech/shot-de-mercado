# Dessa (DESSA) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,007801 · liquidez $244.801 · mcap $7.638.323 (al detectar)  
Detectado el 30/10/2026 00:03 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 84, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 01/11/2026 00:03 UTC (< 48 h) · vigente: quedan 44,1 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir DESSA

Estudio de cómo se adquiere DESSA, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 30/10/2026 03:57 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 30/10/2026 00:03 UTC | pumpswap `DEXTCER…ZwvH` | $244.801 | 5% | 0,082% | 0,817% | 8,170% | $1.224 | $3.672 |
| consulta 30/10/2026 03:57 UTC | pumpswap `DEXTCER…ZwvH` | $254.684 | 3% | 0,079% | 0,785% | 7,853% | $1.273 | $3.820 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump`
5. Configurar el slippage: 3% (liquidez $254.684, consulta 30/10/2026 03:57 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump) y el par en DexScreener (https://dexscreener.com/solana/DEXTCER4k9dwbxTMU8zNVVwGevVmvHMB183pF2xxZwvH); mint authority / freeze authority: revocada / revocada · holders 13.391 · top-10 3,33% (consulta 30/10/2026 03:57 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump
- Par en DexScreener: https://dexscreener.com/solana/DEXTCER4k9dwbxTMU8zNVVwGevVmvHMB183pF2xxZwvH
- Página del lanzamiento (pump.fun): https://pump.fun/coin/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 13.391 · top-10 3,33% (consulta 30/10/2026 03:57 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Dessa / DESSA | registro de la detección (trending) |
| Mint / contrato | `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DEXTCER4k9dwbxTMU8zNVVwGevVmvHMB183pF2xxZwvH` | DexScreener, al detectar (1 par(es) en la consulta 30/10/2026 03:57 UTC) |
| Deployer | `CWpPwPQqCW1rkpBV1pgQqFR7FzfuwfMf9XNLtmTwLSH5` | RugCheck `creator` |
| Par creado | 26/10/2026 13:05 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 3,5 días / 3,5 días / 3,6 días | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 30/10/2026 03:57 UTC |
| Holders / top-10 | 13.391 / 3,33% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 30/10/2026 03:57 UTC |
| Holders efectivos del top-10 | 3,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; orca 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 30/10/2026 03:57 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 30/10/2026 03:57 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DEXTCER4k9dwbxTMU8zNVVwGevVmvHMB183pF2xxZwvH · Solscan: https://solscan.io/token/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump · pump.fun: https://pump.fun/coin/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump · web: https://www.dessatalks.space/ · twitter: https://x.com/jack/status/2113697902916751661 | consulta 30/10/2026 03:57 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 30/10/2026 03:57 UTC)
- **Historia:**
  - Par creado el 26/10/2026 13:05 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 30/10/2026 00:03 UTC, con el par a 3,5 días de creado: precio $0,007801, mcap $7.638.323, liquidez $244.801.
  - Velas de 1 h de GeckoTerminal (87, desde 26/10/2026 13:00 UTC): apertura $0,00005368 · máximo $0,01231 (29/10/2026 18:00 UTC) · mínimo $0,00004780 (26/10/2026 13:00 UTC) · último cierre $0,008366.
  - En la consulta 30/10/2026 03:57 UTC: precio $0,008279, liquidez $254.684, FDV $8.106.934.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 30/10/2026 00:03 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,007801 |
| Liquidez | $244.801 |
| MCap | $7.638.323 |
| Volumen 24 h | $4.333.639 |
| Cambio 24 h | +1.006% |
| Cambio m5 / h1 | +2,2% / +8,0% |
| Volumen m5 / h1 | $3.109 / $60.855 |
| Trades m5 (compras / ventas) | 17 / 12 |
| Edad del par | 3,5 días |
| Score del feed (WS) | 66 |

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

Desglose reconstruido desde los motivos registrados; suma 84 = score registrado 84 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 66 × 0,3 | +19,9 |
| MCap | ≥ $1M | $7.638.323 | +25 |
| Volumen 24 h | ≥ $1M | $4.333.639 | +20 |
| Buy pressure m5 | > 55% (par maduro) | 59% | +15 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +2,2% · h1 +8,0% | +20 |
| Volumen m5 | > $1K (par maduro) | $3.109 | +10 |
| Par viejo | edad > 24 h | edad 3,5 días | -50 |
| Liquidez | ≥ $100K | $244.801 | +15 |
| Cambio 24 h | ≥ +50% | +1.006% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.006% · liq/mcap 3,2% | +0 |
| **Total** | recortado a 0–100 |  | **84** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-30T00:03:34+00:00, sin estado previo): **84** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >55%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Par >24h, no nativo pump.fun, Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=3.2% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 82 de 46.289 tokens analizados (0,18%) quedan ≥ 56. Con score 84, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 30/10/2026 00:03 UTC, hasta 01/11/2026 00:03 UTC · vigente: quedan 44,1 h.
- **Aceleración al detectar:** cambio m5 +2,2% · h1 +8,0% · h24 +1.006% · volumen m5/h1 0,05 · edad del par 3,5 días.
- **Precio de entrada** (alerta): $0,007801.
- **Consulta 30/10/2026 03:57 UTC:** $0,008279 (+6,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump_2026-10-30_000334.json` · blob `51f16f3a4819195b338721754606df22e845b21a` · commit `7844806` (2026-10-30T03:02:52Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-29_235307.json` · blob `30cb36f48879e37a50ea588b6d7c6052414a109b` · commit `7844806` (2026-10-30T03:02:52Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-30_000334`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump · registro · 30/10/2026 00:03 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump · HTTP 200 · 30/10/2026 03:57 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump/report · HTTP 200 · 30/10/2026 03:57 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump · HTTP 200 · 30/10/2026 03:57 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DEXTCER4k9dwbxTMU8zNVVwGevVmvHMB183pF2xxZwvH/ohlcv/hour?limit=1000 · HTTP 200 · 30/10/2026 03:57 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump · HTTP 404 · 30/10/2026 03:57 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=DESSAUSDT · HTTP 400 · 30/10/2026 03:57 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/DESSA-USD · HTTP 404 · 30/10/2026 03:57 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $254.684 vs $254.791 → 0,04%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,008279 vs $0,008366 → 1,04%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump_2026-10-30_000334.json',encoding='utf-8'));d=d.get('npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump',d);p=mock.patch('time.time',return_value=1793318614);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 30/10/2026 03:57 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `3729b5aa1a61b115…`
