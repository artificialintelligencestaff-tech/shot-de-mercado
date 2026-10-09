# QUANTUMDESK (QDESK) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001589 · liquidez $34.027 · mcap $158.944 (al detectar)  
Detectado el 09/10/2026 23:01 UTC por: young-0.4 · edad 10.9 min · pesos info 60 / estructura 20 / precio 20 · info 14.0 · estructura 14.3 · precio/volumen 11.8 · cobertura 93/100, [info] narrative_wave: ola 'quantumdesk': 2 lanzamientos más en 1 h → +3.7, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 45 caracteres → +7.3 (score 40, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 11/10/2026 23:01 UTC (< 48 h) · vigente: quedan 47,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir QDESK

Estudio de cómo se adquiere QDESK, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 09/10/2026 23:36 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 09/10/2026 23:01 UTC | pumpswap `HtZJhSG…N7qH` | $34.027 | 10% | 0,588% | 5,878% | 58,777% | $170 | $510 |
| consulta 09/10/2026 23:36 UTC | pumpswap `HtZJhSG…N7qH` | $4.510 | 10% | 4,435% | 44,347% | 443,474% | $23 | $68 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK`
5. Configurar el slippage: 10% (liquidez $4.510, consulta 09/10/2026 23:36 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK) y el par en DexScreener (https://dexscreener.com/solana/HtZJhSGQJGF1LWk9AxTwQAZVAKd84BJB56ohP3RgN7qH); mint authority / freeze authority: revocada / revocada · holders 2.304 · top-10 77,29% (consulta 09/10/2026 23:36 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK
- Par en DexScreener: https://dexscreener.com/solana/HtZJhSGQJGF1LWk9AxTwQAZVAKd84BJB56ohP3RgN7qH
- Página del lanzamiento (pump.fun): https://pump.fun/coin/CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.304 · top-10 77,29% (consulta 09/10/2026 23:36 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | QUANTUMDESK / QDESK | registro de la detección (pumpportal_live) |
| Mint / contrato | `CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HtZJhSGQJGF1LWk9AxTwQAZVAKd84BJB56ohP3RgN7qH` | DexScreener, al detectar (5 par(es) en la consulta 09/10/2026 23:36 UTC) |
| Deployer | `C6kZcrFXigCmempgRqqF4q72bwSoQkQgTWygNWQvWtaM` | PumpPortal (evento create), al detectar |
| Par creado | 09/10/2026 22:50 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,9 min / 10,9 min / 46,5 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 09/10/2026 23:36 UTC |
| Holders / top-10 | 2.304 / 77,29% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 09/10/2026 23:36 UTC |
| Holders efectivos del top-10 | 1,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 09/10/2026 23:36 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 09/10/2026 23:36 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HtZJhSGQJGF1LWk9AxTwQAZVAKd84BJB56ohP3RgN7qH · Solscan: https://solscan.io/token/CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK · pump.fun: https://pump.fun/coin/CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK · web: https://quantumdesk.fun/ · twitter: https://x.com/QNTMDESK | consulta 09/10/2026 23:36 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 09/10/2026 23:36 UTC)
- **Historia:**
  - Par creado el 09/10/2026 22:50 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 09/10/2026 23:01 UTC, con el par a 10,9 min de creado: precio $0,0001589, mcap $158.944, liquidez $34.027.
  - Velas de 1 h de GeckoTerminal (2, desde 09/10/2026 22:00 UTC): apertura $0,00004178 · máximo $0,0002023 (09/10/2026 23:00 UTC) · mínimo $0,000004837 (09/10/2026 23:00 UTC) · último cierre $0,000005127.
  - En la consulta 09/10/2026 23:36 UTC: precio $0,000004990, liquidez $4.510, FDV $4.843.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 09/10/2026 23:01 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001589 |
| Liquidez | $34.027 |
| MCap | $158.944 |
| Volumen 24 h | $243.770 |
| Cambio 24 h | +268% |
| Cambio m5 / h1 | +11,1% / +268,0% |
| Volumen m5 / h1 | $127.531 / $243.770 |
| Trades m5 (compras / ventas) | 1.163 / 968 |
| Edad del par | 10,9 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 40; motivos sin regla: young-0.4 · edad 10.9 min · pesos info 60 / estructura 20 / precio 20 · info 14.0 · estructura 14.3 · precio/volumen 11.8 · cobertura 93/100, [info] narrative_wave: ola 'quantumdesk': 2 lanzamientos más en 1 h → +3.7, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 45 caracteres → +7.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 2011 · top-10 31.4 % → +2.4, [estructura] dev_wallet: creador compró 5.1 % del supply → +1.5, [estructura] holder_to_txn_ratio: holders/txns 2011/4489 = 0.45 → +0.7, [precio/volumen] volume_acceleration: vol 5 min ×6.3 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +74% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1192→2011 (+136.5/min) · top10 32.5%→31.4% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=34027.09, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 40 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-09T23:01:07+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 41 de 25.933 tokens analizados (0,16%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 09/10/2026 23:01 UTC, hasta 11/10/2026 23:01 UTC · vigente: quedan 47,4 h.
- **Aceleración al detectar:** cambio m5 +11,1% · h1 +268,0% · h24 +268% · volumen m5/h1 0,52 · edad del par 10,9 min.
- **Precio de entrada** (alerta): $0,0001589.
- **Consulta 09/10/2026 23:36 UTC:** $0,000004990 (-96,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK_2026-10-09_230107.json` · blob `ad6fed48ae26288ea88145f148b690640338ee35` · commit `f55f86a` (2026-10-09T23:30:11Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-09_230107`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK · registro · 09/10/2026 23:01 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK · HTTP 200 · 09/10/2026 23:36 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK/report · HTTP 200 · 09/10/2026 23:36 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK · HTTP 200 · 09/10/2026 23:36 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HtZJhSGQJGF1LWk9AxTwQAZVAKd84BJB56ohP3RgN7qH/ohlcv/hour?limit=1000 · HTTP 200 · 09/10/2026 23:36 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK · HTTP 404 · 09/10/2026 23:36 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=QDESKUSDT · HTTP 400 · 09/10/2026 23:36 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/QDESK-USD · HTTP 404 · 09/10/2026 23:36 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $4.510 vs $4.629 → 2,56%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000004990 vs $0,000005127 → 2,66%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK_2026-10-09_230107.json',encoding='utf-8'));d=d.get('CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK',d);p=mock.patch('time.time',return_value=1791586867);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint CH96B7rRQrcGduNZAHoBoaN2heKPwPnVuJMJ5oUkDESK --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 09/10/2026 23:36 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `a7bd61362cc49b2e…`
