# Skyridge Gengar Holo (GENGAR) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00002151 · liquidez $10.809 · mcap $21.518 (al detectar)  
Detectado el 20/10/2026 05:24 UTC por: young-0.4 · edad 13.5 min · pesos info 58 / estructura 21 / precio 21 · info 19.7 · estructura 13.4 · precio/volumen 8.7 · cobertura 93/100, [info] narrative_wave: ola 'holo': 10 lanzamientos más en 1 h → +14.6, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.2 (score 42, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 22/10/2026 05:24 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir GENGAR

Estudio de cómo se adquiere GENGAR, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 20/10/2026 05:52 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 20/10/2026 05:24 UTC | pumpswap `EASqxvD…ukFA` | $10.809 | 10% | 1,850% | 18,503% | 185,027% | $54 | $162 |
| consulta 20/10/2026 05:52 UTC | pumpswap `EASqxvD…ukFA` | $2.659 | 10% | 7,522% | 75,222% | 752,222% | $13 | $40 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump`
5. Configurar el slippage: 10% (liquidez $2.659, consulta 20/10/2026 05:52 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump) y el par en DexScreener (https://dexscreener.com/solana/EASqxvDsvgpD6f2L4gxW4JWBQjgy8DY4gLk5jeo3ukFA); mint authority / freeze authority: revocada / revocada · holders 636 · top-10 98,64% (consulta 20/10/2026 05:52 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump
- Par en DexScreener: https://dexscreener.com/solana/EASqxvDsvgpD6f2L4gxW4JWBQjgy8DY4gLk5jeo3ukFA
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 636 · top-10 98,64% (consulta 20/10/2026 05:52 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Skyridge Gengar Holo / GENGAR | registro de la detección (pumpportal_live) |
| Mint / contrato | `8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `EASqxvDsvgpD6f2L4gxW4JWBQjgy8DY4gLk5jeo3ukFA` | DexScreener, al detectar (2 par(es) en la consulta 20/10/2026 05:52 UTC) |
| Deployer | `HynmnmoVhCfT8b7BK1U22Fxzxn1xnNzudbFhRnMvdAVj` | PumpPortal (evento create), al detectar |
| Par creado | 20/10/2026 05:10 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 13,5 min / 13,5 min / 42,1 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 20/10/2026 05:52 UTC |
| Holders / top-10 | 636 / 98,64% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 20/10/2026 05:52 UTC |
| Holders efectivos del top-10 | 1,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 20/10/2026 05:52 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 20/10/2026 05:52 UTC |
| Links | DexScreener: https://dexscreener.com/solana/EASqxvDsvgpD6f2L4gxW4JWBQjgy8DY4gLk5jeo3ukFA · Solscan: https://solscan.io/token/8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump · pump.fun: https://pump.fun/coin/8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump · web / Telegram / X: no publicados en DexScreener | consulta 20/10/2026 05:52 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 20/10/2026 05:52 UTC)
- **Historia:**
  - Par creado el 20/10/2026 05:10 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 20/10/2026 05:24 UTC, con el par a 13,5 min de creado: precio $0,00002151, mcap $21.518, liquidez $10.809.
  - Velas de 1 h de GeckoTerminal (1, desde 20/10/2026 05:00 UTC): apertura $0,00003983 · máximo $0,00006155 (20/10/2026 05:00 UTC) · mínimo $0,000002708 (20/10/2026 05:00 UTC) · último cierre $0,000002732.
  - En la consulta 20/10/2026 05:52 UTC: precio $0,000002730, liquidez $2.659, FDV $2.730.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 20/10/2026 05:24 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00002151 |
| Liquidez | $10.809 |
| MCap | $21.518 |
| Volumen 24 h | $52.850 |
| Cambio 24 h | -51% |
| Cambio m5 / h1 | -64,3% / -51,4% |
| Volumen m5 / h1 | $21.743 / $52.850 |
| Trades m5 (compras / ventas) | 176 / 194 |
| Edad del par | 13,5 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 42; motivos sin regla: young-0.4 · edad 13.5 min · pesos info 58 / estructura 21 / precio 21 · info 19.7 · estructura 13.4 · precio/volumen 8.7 · cobertura 93/100, [info] narrative_wave: ola 'holo': 10 lanzamientos más en 1 h → +14.6, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.2, [estructura] bonding_progress: graduado (pumpswap) → +10.0, [estructura] holders_struct: holders 724 · top-10 49.2 % → +2.5, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 724/1083 = 0.67 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×4.9 la tasa horaria (s 1.00), [precio/volumen] holder_accumulation: holders 636→724 (+14.7/min) · top10 41.6%→49.2% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=10809.22, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 42 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-20T05:24:09+00:00, sin estado previo): **5** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen decente, Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 68 de 41.654 tokens analizados (0,16%) quedan ≥ 56. Con score 5, este activo queda en el percentil 87,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 20/10/2026 05:24 UTC, hasta 22/10/2026 05:24 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -64,3% · h1 -51,4% · h24 -51% · volumen m5/h1 0,41 · edad del par 13,5 min.
- **Precio de entrada** (alerta): $0,00002151.
- **Consulta 20/10/2026 05:52 UTC:** $0,000002730 (-87,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump_2026-10-20_052409.json` · blob `d2815ab7b2d144febe097b6ae54c4e2c8581f4ac` · commit `2c3a879` (2026-10-20T05:45:22Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-20_052409`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump · registro · 20/10/2026 05:24 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump · HTTP 200 · 20/10/2026 05:52 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump/report · HTTP 200 · 20/10/2026 05:52 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump · HTTP 200 · 20/10/2026 05:52 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/EASqxvDsvgpD6f2L4gxW4JWBQjgy8DY4gLk5jeo3ukFA/ohlcv/hour?limit=1000 · HTTP 200 · 20/10/2026 05:52 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump · HTTP 404 · 20/10/2026 05:52 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=GENGARUSDT · HTTP 400 · 20/10/2026 05:52 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/GENGAR-USD · HTTP 404 · 20/10/2026 05:52 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.659 vs $2.744 → 3,09%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002730 vs $0,000002732 → 0,06%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump_2026-10-20_052409.json',encoding='utf-8'));d=d.get('8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump',d);p=mock.patch('time.time',return_value=1792473849);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8dtXKdPmEcTHZwzdHqgyBRA9KeVHtKmnvn4Gzof7pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 20/10/2026 05:52 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `ece6b455eaeaff89…`
