# Human Intelligence (HI) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00004671 · liquidez $17.334 · mcap $46.718 (al detectar)  
Detectado el 19/10/2026 16:31 UTC por: young-0.4 · edad 10.2 min · pesos info 60 / estructura 20 / precio 20 · info 23.3 · estructura 12.7 · precio/volumen 8.5 · cobertura 93/100, [info] narrative_wave: ola 'human': 8 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 29 caracteres → +5.3 (score 44, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 21/10/2026 16:31 UTC (< 48 h) · vigente: quedan 47,3 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HI

Estudio de cómo se adquiere HI, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 19/10/2026 17:13 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 19/10/2026 16:31 UTC | pumpswap `4B6BHPj…NPN5` | $17.334 | 10% | 1,154% | 11,538% | 115,381% | $87 | $260 |
| consulta 19/10/2026 17:13 UTC | pumpswap `4B6BHPj…NPN5` | $14.881 | 10% | 1,344% | 13,440% | 134,399% | $74 | $223 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump`
5. Configurar el slippage: 10% (liquidez $14.881, consulta 19/10/2026 17:13 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump) y el par en DexScreener (https://dexscreener.com/solana/4B6BHPjuF2CT1JqmwYrwv8976mdN9xfRtJjgU29oNPN5); mint authority / freeze authority: revocada / revocada · holders 1.716 · top-10 43,69% (consulta 19/10/2026 17:13 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump
- Par en DexScreener: https://dexscreener.com/solana/4B6BHPjuF2CT1JqmwYrwv8976mdN9xfRtJjgU29oNPN5
- Página del lanzamiento (pump.fun): https://pump.fun/coin/BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.716 · top-10 43,69% (consulta 19/10/2026 17:13 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Human Intelligence / HI | registro de la detección (pumpportal_live) |
| Mint / contrato | `BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `4B6BHPjuF2CT1JqmwYrwv8976mdN9xfRtJjgU29oNPN5` | DexScreener, al detectar (7 par(es) en la consulta 19/10/2026 17:13 UTC) |
| Deployer | `AAXkBLCmi7sEnr6CD8HTTPdPb36JA5MJajEru2tMjXBM` | PumpPortal (evento create), al detectar |
| Par creado | 19/10/2026 16:21 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,2 min / 10,2 min / 52,5 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 19/10/2026 17:13 UTC |
| Holders / top-10 | 1.716 / 43,69% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 19/10/2026 17:13 UTC |
| Holders efectivos del top-10 | 3,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 19/10/2026 17:13 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 19/10/2026 17:13 UTC |
| Links | DexScreener: https://dexscreener.com/solana/4B6BHPjuF2CT1JqmwYrwv8976mdN9xfRtJjgU29oNPN5 · Solscan: https://solscan.io/token/BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump · pump.fun: https://pump.fun/coin/BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump · web: https://x.com/i/trending/2112071617241075943?timeline=VGltZWxpbmU6CgCaHU%2BV8hXW0OcA · twitter: https://x.com/HumainISol/status/2112216643115925529?s=20 | consulta 19/10/2026 17:13 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 19/10/2026 17:13 UTC)
- **Historia:**
  - Par creado el 19/10/2026 16:21 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 19/10/2026 16:31 UTC, con el par a 10,2 min de creado: precio $0,00004671, mcap $46.718, liquidez $17.334.
  - Velas de 1 h de GeckoTerminal (2, desde 19/10/2026 16:00 UTC): apertura $0,00004653 · máximo $0,00007459 (19/10/2026 16:00 UTC) · mínimo $0,00001072 (19/10/2026 16:00 UTC) · último cierre $0,00004112.
  - En la consulta 19/10/2026 17:13 UTC: precio $0,00003731, liquidez $14.881, FDV $35.734.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 19/10/2026 16:31 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00004671 |
| Liquidez | $17.334 |
| MCap | $46.718 |
| Volumen 24 h | $171.973 |
| Cambio 24 h | -4% |
| Cambio m5 / h1 | +46,5% / -3,7% |
| Volumen m5 / h1 | $38.253 / $171.973 |
| Trades m5 (compras / ventas) | 697 / 479 |
| Edad del par | 10,2 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 44; motivos sin regla: young-0.4 · edad 10.2 min · pesos info 60 / estructura 20 / precio 20 · info 23.3 · estructura 12.7 · precio/volumen 8.5 · cobertura 93/100, [info] narrative_wave: ola 'human': 8 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 29 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1615 · top-10 35.4 % → +2.4, [estructura] dev_wallet: creador compró 9.6 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1615/4838 = 0.33 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×2.7 la tasa horaria (s 0.47), [precio/volumen] buy_pressure_shift: compras 59% en 5 min vs 56% en 1 h (s 0.15), [precio/volumen] liquidity_inflow: liquidez +21% en 8 min (s 0.69), [precio/volumen] holder_accumulation: holders 1281→1615 (+55.7/min) · top10 37.2%→35.4% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=17333.89, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 44 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-19T16:31:33+00:00, sin estado previo): **15** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 67 de 40.989 tokens analizados (0,16%) quedan ≥ 56. Con score 15, este activo queda en el percentil 97,2 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 19/10/2026 16:31 UTC, hasta 21/10/2026 16:31 UTC · vigente: quedan 47,3 h.
- **Aceleración al detectar:** cambio m5 +46,5% · h1 -3,7% · h24 -4% · volumen m5/h1 0,22 · edad del par 10,2 min.
- **Precio de entrada** (alerta): $0,00004671.
- **Consulta 19/10/2026 17:13 UTC:** $0,00003731 (-20,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump_2026-10-19_163133.json` · blob `3d36371a31e6bad509430f3f51df1d52e0488989` · commit `fa11a30` (2026-10-19T17:05:29Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-19_163133`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump · registro · 19/10/2026 16:31 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump · HTTP 200 · 19/10/2026 17:13 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump/report · HTTP 200 · 19/10/2026 17:13 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump · HTTP 200 · 19/10/2026 17:13 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/4B6BHPjuF2CT1JqmwYrwv8976mdN9xfRtJjgU29oNPN5/ohlcv/hour?limit=1000 · HTTP 200 · 19/10/2026 17:13 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump · HTTP 404 · 19/10/2026 17:13 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HIUSDT · HTTP 400 · 19/10/2026 17:13 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HI-USD · HTTP 404 · 19/10/2026 17:13 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $14.881 vs $14.890 → 0,06%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00003731 vs $0,00004112 → 9,26%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump_2026-10-19_163133.json',encoding='utf-8'));d=d.get('BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump',d);p=mock.patch('time.time',return_value=1792427493);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint BU9hz1JXJZCjJwMdBPggxdEF1FEsJzyHiRwAkU8qpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 19/10/2026 17:13 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `6df09740e2074d56…`
