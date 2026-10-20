# xingxing (Xingxing) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00007318 · liquidez $22.207 · mcap $73.189 (al detectar)  
Detectado el 20/10/2026 20:24 UTC por: young-0.4 · edad 20.3 min · pesos info 55 / estructura 23 / precio 23 · info 22.4 · estructura 14.0 · precio/volumen 4.1 · cobertura 94/100, [info] narrative_wave: ola 'xingxing': 7 lanzamientos más en 1 h → +12.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +4.9 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 22/10/2026 20:24 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Xingxing

Estudio de cómo se adquiere Xingxing, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 20/10/2026 20:55 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 20/10/2026 20:24 UTC | pumpswap `DQJymzE…UxxR` | $22.207 | 10% | 0,901% | 9,006% | 90,063% | $111 | $333 |
| consulta 20/10/2026 20:55 UTC | pumpswap `DQJymzE…UxxR` | $17.184 | 10% | 1,164% | 11,639% | 116,389% | $86 | $258 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump`
5. Configurar el slippage: 10% (liquidez $17.184, consulta 20/10/2026 20:55 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump) y el par en DexScreener (https://dexscreener.com/solana/DQJymzEaB41ffVY9pr6symzWUVaBK1wxE7TKWzHnUxxR); mint authority / freeze authority: revocada / revocada · holders 1.952 · top-10 42,88% (consulta 20/10/2026 20:55 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump
- Par en DexScreener: https://dexscreener.com/solana/DQJymzEaB41ffVY9pr6symzWUVaBK1wxE7TKWzHnUxxR
- Página del lanzamiento (pump.fun): https://pump.fun/coin/Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.952 · top-10 42,88% (consulta 20/10/2026 20:55 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | xingxing / Xingxing | registro de la detección (pumpportal_live) |
| Mint / contrato | `Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DQJymzEaB41ffVY9pr6symzWUVaBK1wxE7TKWzHnUxxR` | DexScreener, al detectar (8 par(es) en la consulta 20/10/2026 20:55 UTC) |
| Deployer | `5RQ1UWATaMjjXC34BW6UusEUdEoCuNRECBW8nnHPiCGH` | PumpPortal (evento create), al detectar |
| Par creado | 20/10/2026 20:04 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 20,3 min / 20,3 min / 51,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 20/10/2026 20:55 UTC |
| Holders / top-10 | 1.952 / 42,88% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 20/10/2026 20:55 UTC |
| Holders efectivos del top-10 | 3,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 20/10/2026 20:55 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 20/10/2026 20:55 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DQJymzEaB41ffVY9pr6symzWUVaBK1wxE7TKWzHnUxxR · Solscan: https://solscan.io/token/Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump · pump.fun: https://pump.fun/coin/Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump · twitter: https://x.com/TheBlueprint99/status/2112633868260127008?s=20 · instagram: https://www.instagram.com/fengchunxingxing/reels/ | consulta 20/10/2026 20:55 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 20/10/2026 20:55 UTC)
- **Historia:**
  - Par creado el 20/10/2026 20:04 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 20/10/2026 20:24 UTC, con el par a 20,3 min de creado: precio $0,00007318, mcap $73.189, liquidez $22.207.
  - Velas de 1 h de GeckoTerminal (1, desde 20/10/2026 20:00 UTC): apertura $0,00004033 · máximo $0,0001558 (20/10/2026 20:00 UTC) · mínimo $0,00003291 (20/10/2026 20:00 UTC) · último cierre $0,00004408.
  - En la consulta 20/10/2026 20:55 UTC: precio $0,00004521, liquidez $17.184, FDV $44.203.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 20/10/2026 20:24 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00007318 |
| Liquidez | $22.207 |
| MCap | $73.189 |
| Volumen 24 h | $405.784 |
| Cambio 24 h | +66% |
| Cambio m5 / h1 | -3,4% / +65,6% |
| Volumen m5 / h1 | $55.854 / $405.784 |
| Trades m5 (compras / ventas) | 507 / 435 |
| Edad del par | 20,3 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 20.3 min · pesos info 55 / estructura 23 / precio 23 · info 22.4 · estructura 14.0 · precio/volumen 4.1 · cobertura 94/100, [info] narrative_wave: ola 'xingxing': 7 lanzamientos más en 1 h → +12.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +4.9, [info] dex_profile: perfil pago en DexScreener → +2.7, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +2.7, [estructura] bonding_progress: graduado (pumpswap) → +10.8, [estructura] holders_struct: holders 1875 · top-10 38.8 % → +2.7, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1875/8083 = 0.23 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×1.7 la tasa horaria (s 0.06), [precio/volumen] holder_accumulation: holders 1230→1875 (+53.7/min) · top10 35.9%→38.8% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=22206.8, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-20T20:24:28+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 69 de 42.444 tokens analizados (0,16%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 20/10/2026 20:24 UTC, hasta 22/10/2026 20:24 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -3,4% · h1 +65,6% · h24 +66% · volumen m5/h1 0,14 · edad del par 20,3 min.
- **Precio de entrada** (alerta): $0,00007318.
- **Consulta 20/10/2026 20:55 UTC:** $0,00004521 (-38,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump_2026-10-20_202428.json` · blob `c8ffab22984ca1a6454cd8a9455fe591aeadc9a7` · commit `97f65da` (2026-10-20T20:48:57Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-20_202428`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump · registro · 20/10/2026 20:24 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump · HTTP 200 · 20/10/2026 20:55 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump/report · HTTP 200 · 20/10/2026 20:55 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump · HTTP 200 · 20/10/2026 20:55 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DQJymzEaB41ffVY9pr6symzWUVaBK1wxE7TKWzHnUxxR/ohlcv/hour?limit=1000 · HTTP 200 · 20/10/2026 20:55 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump · HTTP 404 · 20/10/2026 20:55 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=XINGXINGUSDT · HTTP 400 · 20/10/2026 20:55 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/XINGXING-USD · HTTP 404 · 20/10/2026 20:55 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $17.184 vs $16.992 → 1,11%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00004521 vs $0,00004408 → 2,51%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump_2026-10-20_202428.json',encoding='utf-8'));d=d.get('Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump',d);p=mock.patch('time.time',return_value=1792527868);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint Bivugv4GNFUiqUabDhvFcepDskTcgPk7EtExV4mvpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 20/10/2026 20:55 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `01c51a73609ae6c6…`
