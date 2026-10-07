# Sidiora Markets (SID) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003116 · liquidez $159.244 · mcap $3.114.542 (al detectar)  
Detectado el 07/10/2026 08:17 UTC por: MCap > $1M, Volumen decente, Buy pressure >55% (score 88, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 09/10/2026 08:17 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SID

Estudio de cómo se adquiere SID, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/10/2026 08:41 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/10/2026 08:17 UTC | pumpswap `DvxQudp…VJKP` | $159.244 | 5% | 0,126% | 1,256% | 12,559% | $796 | $2.389 |
| consulta 07/10/2026 08:41 UTC | pumpswap `DvxQudp…VJKP` | $160.293 | 5% | 0,125% | 1,248% | 12,477% | $801 | $2.404 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump`
5. Configurar el slippage: 5% (liquidez $160.293, consulta 07/10/2026 08:41 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump) y el par en DexScreener (https://dexscreener.com/solana/DvxQudpAmigLByHZWsLTxAn3oUtUszsBgMa4C4hoVJKP); mint authority / freeze authority: revocada / revocada · holders 2.174 · top-10 11,34% (consulta 07/10/2026 08:41 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump
- Par en DexScreener: https://dexscreener.com/solana/DvxQudpAmigLByHZWsLTxAn3oUtUszsBgMa4C4hoVJKP
- Página del lanzamiento (pump.fun): https://pump.fun/coin/Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.174 · top-10 11,34% (consulta 07/10/2026 08:41 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Sidiora Markets / SID | registro de la detección (pumpportal) |
| Mint / contrato | `Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DvxQudpAmigLByHZWsLTxAn3oUtUszsBgMa4C4hoVJKP` | DexScreener, al detectar (2 par(es) en la consulta 07/10/2026 08:41 UTC) |
| Deployer | `L4qzPrKA8o8tZwQMbo9f8G9GQcA4gnLDcUtrxr7ZwcK` | PumpPortal (evento create), al detectar |
| Par creado | 07/10/2026 07:16 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,7 min / 60,7 min / 84,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/10/2026 08:41 UTC |
| Holders / top-10 | 2.174 / 11,34% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/10/2026 08:41 UTC |
| Holders efectivos del top-10 | 8,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/10/2026 08:41 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 07/10/2026 08:41 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DvxQudpAmigLByHZWsLTxAn3oUtUszsBgMa4C4hoVJKP · Solscan: https://solscan.io/token/Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump · pump.fun: https://pump.fun/coin/Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump · web / Telegram / X: no publicados en DexScreener | consulta 07/10/2026 08:41 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/10/2026 08:41 UTC)
- **Historia:**
  - Par creado el 07/10/2026 07:16 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/10/2026 08:17 UTC, con el par a 60,7 min de creado: precio $0,003116, mcap $3.114.542, liquidez $159.244.
  - Velas de 1 h de GeckoTerminal (2, desde 07/10/2026 07:00 UTC): apertura $0,00004938 · máximo $0,003171 (07/10/2026 08:00 UTC) · mínimo $0,00004938 (07/10/2026 07:00 UTC) · último cierre $0,003123.
  - En la consulta 07/10/2026 08:41 UTC: precio $0,003158, liquidez $160.293, FDV $3.156.491.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/10/2026 08:17 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003116 |
| Liquidez | $159.244 |
| MCap | $3.114.542 |
| Volumen 24 h | $76.716 |
| Cambio 24 h | +6.202% |
| Cambio m5 / h1 | -0,9% / +4,3% |
| Volumen m5 / h1 | $678 / $8.181 |
| Trades m5 (compras / ventas) | 13 / 9 |
| Edad del par | 60,7 min |
| Score del feed (WS) | n/d (feed sin score) |

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

Desglose reconstruido desde los motivos registrados; suma 88 = score registrado 88 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $1M | $3.114.542 | +25 |
| Volumen 24 h | ≥ $50K | $76.716 | +10 |
| Buy pressure m5 | > 55% (par maduro) | 59% | +15 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,7 min | +8 |
| Volumen m5 | > $500 (par maduro) | $678 | +5 |
| Liquidez | ≥ $100K | $159.244 | +15 |
| Cambio 24 h | ≥ +50% | +6.202% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +6.202% · liq/mcap 5,1% | +0 |
| **Total** | recortado a 0–100 |  | **88** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-07T08:17:33+00:00, sin estado previo): **88** · motivos: MCap > $1M, Volumen decente, Buy pressure >55%, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=5.1% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 25 de 18.145 tokens analizados (0,14%) quedan ≥ 56. Con score 88, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/10/2026 08:17 UTC, hasta 09/10/2026 08:17 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 -0,9% · h1 +4,3% · h24 +6.202% · volumen m5/h1 0,08 · edad del par 60,7 min.
- **Precio de entrada** (alerta): $0,003116.
- **Consulta 07/10/2026 08:41 UTC:** $0,003158 (+1,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump_2026-10-07_081733.json` · blob `e213ee67d00edf226cdfe7caeb65c029279653d2` · commit `bfce7ca` (2026-10-07T08:34:45Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-07_081733`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump · registro · 07/10/2026 08:17 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump · HTTP 200 · 07/10/2026 08:41 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump/report · HTTP 200 · 07/10/2026 08:41 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump · HTTP 200 · 07/10/2026 08:41 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DvxQudpAmigLByHZWsLTxAn3oUtUszsBgMa4C4hoVJKP/ohlcv/hour?limit=1000 · HTTP 200 · 07/10/2026 08:41 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump · HTTP 404 · 07/10/2026 08:41 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SIDUSDT · HTTP 400 · 07/10/2026 08:41 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SID-USD · HTTP 404 · 07/10/2026 08:41 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $160.293 vs $159.399 → 0,56%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003158 vs $0,003123 → 1,12%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump_2026-10-07_081733.json',encoding='utf-8'));d=d.get('Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump',d);p=mock.patch('time.time',return_value=1791361053);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint Y732CNtrDMqmRTxfLBCw5s272y5U6JjN23VB2fepump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/10/2026 08:41 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `ade98e4689895542…`
