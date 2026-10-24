# This is Private Property (PRIVATE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00001836 · liquidez $10.033 · mcap $18.362 (al detectar)  
Detectado el 24/10/2026 02:58 UTC por: young-0.4 · edad 11.2 min · pesos info 59 / estructura 20 / precio 20 · info 20.1 · estructura 13.6 · precio/volumen 6.9 · cobertura 93/100, [info] narrative_wave: ola 'private': 20 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 26/10/2026 02:58 UTC (< 48 h) · vigente: quedan 47,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir PRIVATE

Estudio de cómo se adquiere PRIVATE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 24/10/2026 04:00 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 24/10/2026 02:58 UTC | pumpswap `MpGZ38d…Apnk` | $10.033 | 10% | 1,993% | 19,933% | 199,334% | $50 | $151 |
| consulta 24/10/2026 04:00 UTC | pumpswap `MpGZ38d…Apnk` | $5.438 | 10% | 3,678% | 36,778% | 367,782% | $27 | $82 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump`
5. Configurar el slippage: 10% (liquidez $5.438, consulta 24/10/2026 04:00 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump) y el par en DexScreener (https://dexscreener.com/solana/MpGZ38dRhgQ5kJKehdFhZfjDWWr9cWpX8MQ9LuwApnk); mint authority / freeze authority: revocada / revocada · holders 1.229 · top-10 75,49% (consulta 24/10/2026 04:00 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump
- Par en DexScreener: https://dexscreener.com/solana/MpGZ38dRhgQ5kJKehdFhZfjDWWr9cWpX8MQ9LuwApnk
- Página del lanzamiento (pump.fun): https://pump.fun/coin/C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.229 · top-10 75,49% (consulta 24/10/2026 04:00 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | This is Private Property / PRIVATE | registro de la detección (pumpportal_live) |
| Mint / contrato | `C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `MpGZ38dRhgQ5kJKehdFhZfjDWWr9cWpX8MQ9LuwApnk` | DexScreener, al detectar (4 par(es) en la consulta 24/10/2026 04:00 UTC) |
| Deployer | `DMT3DnnW4apdgYBZN9mfPhRL7nzFwHfC3bnmZMDK1JxQ` | PumpPortal (evento create), al detectar |
| Par creado | 24/10/2026 02:47 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,2 min / 11,2 min / 73,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 24/10/2026 04:00 UTC |
| Holders / top-10 | 1.229 / 75,49% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 24/10/2026 04:00 UTC |
| Holders efectivos del top-10 | 2,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 24/10/2026 04:00 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 24/10/2026 04:00 UTC |
| Links | DexScreener: https://dexscreener.com/solana/MpGZ38dRhgQ5kJKehdFhZfjDWWr9cWpX8MQ9LuwApnk · Solscan: https://solscan.io/token/C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump · pump.fun: https://pump.fun/coin/C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump · web / Telegram / X: no publicados en DexScreener | consulta 24/10/2026 04:00 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 24/10/2026 04:00 UTC)
- **Historia:**
  - Par creado el 24/10/2026 02:47 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 24/10/2026 02:58 UTC, con el par a 11,2 min de creado: precio $0,00001836, mcap $18.362, liquidez $10.033.
  - Velas de 1 h de GeckoTerminal (2, desde 24/10/2026 02:00 UTC): apertura $0,00004078 · máximo $0,00006175 (24/10/2026 02:00 UTC) · mínimo $0,000006552 (24/10/2026 03:00 UTC) · último cierre $0,000007122.
  - En la consulta 24/10/2026 04:00 UTC: precio $0,000007166, liquidez $5.438, FDV $6.846.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 24/10/2026 02:58 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00001836 |
| Liquidez | $10.033 |
| MCap | $18.362 |
| Volumen 24 h | $150.488 |
| Cambio 24 h | -57% |
| Cambio m5 / h1 | -63,0% / -56,8% |
| Volumen m5 / h1 | $40.582 / $150.488 |
| Trades m5 (compras / ventas) | 592 / 648 |
| Edad del par | 11,2 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 11.2 min · pesos info 59 / estructura 20 / precio 20 · info 20.1 · estructura 13.6 · precio/volumen 6.9 · cobertura 93/100, [info] narrative_wave: ola 'private': 20 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1273 · top-10 47.8 % → +2.4, [estructura] dev_wallet: creador compró 6.7 % del supply → +1.0, [estructura] holder_to_txn_ratio: holders/txns 1273/4716 = 0.27 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×3.2 la tasa horaria (s 0.69), [precio/volumen] holder_accumulation: holders 952→1273 (+53.5/min) · top10 37.4%→47.8% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=10033.43, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=13302.14, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-24T02:58:21+00:00, sin estado previo): **10** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 75 de 45.522 tokens analizados (0,16%) quedan ≥ 56. Con score 10, este activo queda en el percentil 93,5 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 24/10/2026 02:58 UTC, hasta 26/10/2026 02:58 UTC · vigente: quedan 47,0 h.
- **Aceleración al detectar:** cambio m5 -63,0% · h1 -56,8% · h24 -57% · volumen m5/h1 0,27 · edad del par 11,2 min.
- **Precio de entrada** (alerta): $0,00001836.
- **Consulta 24/10/2026 04:00 UTC:** $0,000007166 (-61,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump_2026-10-24_025821.json` · blob `0a14529674e423a8b758ad6d3cc7642d74c8304d` · commit `738c694` (2026-10-24T03:53:28Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-24_025821`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump · registro · 24/10/2026 02:58 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump · HTTP 200 · 24/10/2026 04:00 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump/report · HTTP 200 · 24/10/2026 04:00 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump · HTTP 200 · 24/10/2026 04:00 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/MpGZ38dRhgQ5kJKehdFhZfjDWWr9cWpX8MQ9LuwApnk/ohlcv/hour?limit=1000 · HTTP 200 · 24/10/2026 04:00 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump · HTTP 404 · 24/10/2026 04:00 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=PRIVATEUSDT · HTTP 400 · 24/10/2026 04:00 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/PRIVATE-USD · HTTP 404 · 24/10/2026 04:00 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $5.438 vs $5.368 → 1,30%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000007166 vs $0,000007122 → 0,61%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump_2026-10-24_025821.json',encoding='utf-8'));d=d.get('C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump',d);p=mock.patch('time.time',return_value=1792810701);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint C8JvX1WRffLwMrKoEKrumFhBMhbN24siQtBFJdXBpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 24/10/2026 04:00 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `6ae757c0de887156…`
