# DOTF (D O T ) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000003281 · liquidez $4.524 · mcap $3.282 (al detectar)  
Detectado el 07/10/2026 08:42 UTC por: WS score muy alto, MCap bajo, Volumen masivo (score 70, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 09/10/2026 08:42 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir D O T 

Estudio de cómo se adquiere D O T , con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/10/2026 08:58 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/10/2026 08:42 UTC | pumpswap `EXxxrKV…ujkX` | $4.524 | 10% | 4,421% | 44,210% | 442,097% | $23 | $68 |
| consulta 07/10/2026 08:58 UTC | pumpswap `EXxxrKV…ujkX` | $4.524 | 10% | 4,421% | 44,210% | 442,097% | $23 | $68 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump`
5. Configurar el slippage: 10% (liquidez $4.524, consulta 07/10/2026 08:58 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump) y el par en DexScreener (https://dexscreener.com/solana/EXxxrKVB5qTvE7tPnEwYLpvSZUhJMg2NaYTxbSNhujkX); mint authority / freeze authority: revocada / revocada · holders 42 · top-10 100,00% (consulta 07/10/2026 08:58 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump
- Par en DexScreener: https://dexscreener.com/solana/EXxxrKVB5qTvE7tPnEwYLpvSZUhJMg2NaYTxbSNhujkX
- Página del lanzamiento (pump.fun): https://pump.fun/coin/D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 42 · top-10 100,00% (consulta 07/10/2026 08:58 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | DOTF / D O T  | registro de la detección (trending) |
| Mint / contrato | `D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `EXxxrKVB5qTvE7tPnEwYLpvSZUhJMg2NaYTxbSNhujkX` | DexScreener, al detectar (2 par(es) en la consulta 07/10/2026 08:58 UTC) |
| Deployer | `ERuU27Zhxd3cNYDFasErZJWwyznRf8ndQVEMjQkucB8N` | RugCheck `creator` |
| Par creado | 07/10/2026 05:26 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 3,3 h / 3,3 h / 3,5 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/10/2026 08:58 UTC |
| Holders / top-10 | 42 / 100,00% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/10/2026 08:58 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/10/2026 08:58 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 07/10/2026 08:58 UTC |
| Links | DexScreener: https://dexscreener.com/solana/EXxxrKVB5qTvE7tPnEwYLpvSZUhJMg2NaYTxbSNhujkX · Solscan: https://solscan.io/token/D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump · pump.fun: https://pump.fun/coin/D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump · web / Telegram / X: no publicados en DexScreener | consulta 07/10/2026 08:58 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/10/2026 08:58 UTC)
- **Historia:**
  - Par creado el 07/10/2026 05:26 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/10/2026 08:42 UTC, con el par a 3,3 h de creado: precio $0,000003281, mcap $3.282, liquidez $4.524.
  - Velas de 1 h de GeckoTerminal (3, desde 07/10/2026 05:00 UTC): apertura $0,002920 · máximo $0,1860 (07/10/2026 07:00 UTC) · mínimo $0,00004929 (07/10/2026 05:00 UTC) · último cierre $0,1848.
  - En la consulta 07/10/2026 08:58 UTC: precio $0,000003281, liquidez $4.524, FDV $3.282.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/10/2026 08:42 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000003281 |
| Liquidez | $4.524 |
| MCap | $3.282 |
| Volumen 24 h | $1.272.368 |
| Cambio 24 h | -93% |
| Cambio m5 / h1 | -0,3% / -0,3% |
| Volumen m5 / h1 | $0 / $0 |
| Trades m5 (compras / ventas) | 0 / 1 |
| Edad del par | 3,3 h |
| Score del feed (WS) | 92 |

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

Desglose reconstruido desde los motivos registrados; suma 70 = score registrado 70 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 92 × 0,3 | +27,7 |
| MCap | < $50K | $3.282 | +0 |
| Volumen 24 h | ≥ $1M | $1.272.368 | +20 |
| Trades m5/h1 | > 0,5 (par maduro) | 1,00 | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 3,3 h | +8 |
| Liquidez | < $20K | $4.524 | +0 |
| Cambio 24 h | ≤ −30% | -93% | -5 |
| **Total** | recortado a 0–100 |  | **70** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-07T08:42:26+00:00, sin estado previo): **70** · motivos: WS score muy alto, MCap bajo, Volumen masivo, Trades acelerados (5m/1h > 50%), Edge temprano (<4h), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 25 de 18.180 tokens analizados (0,14%) quedan ≥ 56. Con score 70, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/10/2026 08:42 UTC, hasta 09/10/2026 08:42 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -0,3% · h1 -0,3% · h24 -93% · volumen m5/h1 n/d · edad del par 3,3 h.
- **Precio de entrada** (alerta): $0,000003281.
- **Consulta 07/10/2026 08:58 UTC:** $0,000003281 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump_2026-10-07_084226.json` · blob `a4d21a9d114b2f157019042f839b5f70e4a159ab` · commit `27f76dd` (2026-10-07T08:52:25Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-07_083605.json` · blob `e6cfc160c31a7f534fdd89ed96910c13e3f26a69` · commit `27f76dd` (2026-10-07T08:52:25Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-07_084226`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump · registro · 07/10/2026 08:42 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump · HTTP 200 · 07/10/2026 08:58 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump/report · HTTP 200 · 07/10/2026 08:58 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump · HTTP 200 · 07/10/2026 08:58 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/EXxxrKVB5qTvE7tPnEwYLpvSZUhJMg2NaYTxbSNhujkX/ohlcv/hour?limit=1000 · HTTP 200 · 07/10/2026 08:58 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump · HTTP 404 · 07/10/2026 08:58 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $4.524 vs $185.139.234 → 100,00%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000003281 vs $0,1848 → 100,00%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump_2026-10-07_084226.json',encoding='utf-8'));d=d.get('D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump',d);p=mock.patch('time.time',return_value=1791362546);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint D44ndVYQ67avq1jqBvSgeRCxcnCrzjy3F7G8RxAPpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/10/2026 08:58 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `25d0ce8861bdeee5…`
