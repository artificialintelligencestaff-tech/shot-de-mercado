# Umbra Cash (UCASH) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0008410 · liquidez $69.927 · mcap $837.907 (al detectar)  
Detectado el 23/11/2026 06:29 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 25/11/2026 06:29 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir UCASH

Estudio de cómo se adquiere UCASH, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 23/11/2026 06:30 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 23/11/2026 06:29 UTC | pumpswap `4h7R5Jz…1Rxt` | $69.927 | 5% | 0,286% | 2,860% | 28,601% | $350 | $1.049 |
| consulta 23/11/2026 06:30 UTC | pumpswap `4h7R5Jz…1Rxt` | $69.300 | 5% | 0,289% | 2,886% | 28,860% | $347 | $1.040 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump`
5. Configurar el slippage: 5% (liquidez $69.300, consulta 23/11/2026 06:30 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump) y el par en DexScreener (https://dexscreener.com/solana/4h7R5JzaQ6PgNjFuD12AeUQJRQYgwz2YhPSrA6sh1Rxt); mint authority / freeze authority: revocada / revocada · holders 5.820 · top-10 11,14% (consulta 23/11/2026 06:30 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump
- Par en DexScreener: https://dexscreener.com/solana/4h7R5JzaQ6PgNjFuD12AeUQJRQYgwz2YhPSrA6sh1Rxt
- Página del lanzamiento (pump.fun): https://pump.fun/coin/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.820 · top-10 11,14% (consulta 23/11/2026 06:30 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Umbra Cash / UCASH | registro de la detección (trending) |
| Mint / contrato | `7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `4h7R5JzaQ6PgNjFuD12AeUQJRQYgwz2YhPSrA6sh1Rxt` | DexScreener, al detectar (3 par(es) en la consulta 23/11/2026 06:30 UTC) |
| Deployer | `2soHxDiRD541G2TqhUL4mzzpm48v5GawtGDCR22BF9LR` | RugCheck `creator` |
| Par creado | 22/11/2026 11:15 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 19,2 h / 19,2 h / 19,3 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 23/11/2026 06:30 UTC |
| Holders / top-10 | 5.820 / 11,14% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 23/11/2026 06:30 UTC |
| Holders efectivos del top-10 | 5,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 23/11/2026 06:30 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 23/11/2026 06:30 UTC |
| Links | DexScreener: https://dexscreener.com/solana/4h7R5JzaQ6PgNjFuD12AeUQJRQYgwz2YhPSrA6sh1Rxt · Solscan: https://solscan.io/token/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump · pump.fun: https://pump.fun/coin/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump · web: https://www.umbracash.vip/ · twitter: https://x.com/UmbraCashApp | consulta 23/11/2026 06:30 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 23/11/2026 06:30 UTC)
- **Historia:**
  - Par creado el 22/11/2026 11:15 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 23/11/2026 06:29 UTC, con el par a 19,2 h de creado: precio $0,0008410, mcap $837.907, liquidez $69.927.
  - Velas de 1 h de GeckoTerminal (20, desde 22/11/2026 11:00 UTC): apertura $0,00007899 · máximo $0,002242 (23/11/2026 05:00 UTC) · mínimo $0,00004749 (22/11/2026 11:00 UTC) · último cierre $0,0008671.
  - En la consulta 23/11/2026 06:30 UTC: precio $0,0008262, liquidez $69.300, FDV $823.172.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 23/11/2026 06:29 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0008410 |
| Liquidez | $69.927 |
| MCap | $837.907 |
| Volumen 24 h | $2.953.772 |
| Cambio 24 h | +1.661% |
| Cambio m5 / h1 | -12,0% / -46,4% |
| Volumen m5 / h1 | $15.092 / $194.171 |
| Trades m5 (compras / ventas) | 413 / 122 |
| Edad del par | 19,2 h |
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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 76 × 0,3 | +22,8 |
| MCap | ≥ $100K | $837.907 | +15 |
| Volumen 24 h | ≥ $1M | $2.953.772 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 77% | +25 |
| Volumen m5 | > $1K (par maduro) | $15.092 | +10 |
| Liquidez | ≥ $50K | $69.927 | +10 |
| Cambio 24 h | ≥ +50% | +1.661% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.661% · liq/mcap 8,3% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-23T06:29:45+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=8.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 110 de 47.584 tokens analizados (0,23%) quedan ≥ 56. Con score 100, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 23/11/2026 06:29 UTC, hasta 25/11/2026 06:29 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -12,0% · h1 -46,4% · h24 +1.661% · volumen m5/h1 0,08 · edad del par 19,2 h.
- **Precio de entrada** (alerta): $0,0008410.
- **Consulta 23/11/2026 06:30 UTC:** $0,0008262 (-1,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump_2026-11-23_062956.json` · blob `47a0f41c353bd9b737d17e71cbb4e0cb7e991da7` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-23_062440.json` · blob `9fb06d99bf2826baf5368d82b2a1b7af3326dcbe` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-23_062956`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump · registro · 23/11/2026 06:29 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump · HTTP 200 · 23/11/2026 06:30 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump/report · HTTP 200 · 23/11/2026 06:30 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump · HTTP 200 · 23/11/2026 06:30 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/4h7R5JzaQ6PgNjFuD12AeUQJRQYgwz2YhPSrA6sh1Rxt/ohlcv/hour?limit=1000 · HTTP 200 · 23/11/2026 06:30 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump · HTTP 404 · 23/11/2026 06:30 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=UCASHUSDT · HTTP 400 · 23/11/2026 06:30 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/UCASH-USD · HTTP 404 · 23/11/2026 06:30 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $69.300 vs $71.640 → 3,27%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0008262 vs $0,0008671 → 4,72%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump_2026-11-23_062956.json',encoding='utf-8'));d=d.get('7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump',d);p=mock.patch('time.time',return_value=1795415385);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 23/11/2026 06:30 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `b6ccbfc14cd1cd39…`
