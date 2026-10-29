# Cat Bot (CATBOT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000003364 · liquidez $3.867 · mcap $3.342 (al detectar)  
Detectado el 29/10/2026 20:09 UTC por: WS score alto, MCap bajo, Volumen masivo (score 61, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 31/10/2026 20:09 UTC (< 48 h) · vigente: quedan 44,2 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir CATBOT

Estudio de cómo se adquiere CATBOT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 29/10/2026 23:58 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 29/10/2026 20:09 UTC | pumpswap `9CnCbMd…swvW` | $3.867 | 10% | 5,172% | 51,720% | 517,197% | $19 | $58 |
| consulta 29/10/2026 23:58 UTC | pumpswap `9CnCbMd…swvW` | $3.506 | 10% | 5,704% | 57,042% | 570,418% | $18 | $53 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
5. Configurar el slippage: 10% (liquidez $3.506, consulta 29/10/2026 23:58 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump) y el par en DexScreener (https://dexscreener.com/solana/9CnCbMdSHu7P4VvPzoELHbB6rmBy3quiAby36KqcswvW); mint authority / freeze authority: revocada / revocada · holders 910 · top-10 97,30% (consulta 29/10/2026 23:58 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump
- Par en DexScreener: https://dexscreener.com/solana/9CnCbMdSHu7P4VvPzoELHbB6rmBy3quiAby36KqcswvW
- Página del lanzamiento (pump.fun): https://pump.fun/coin/dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 910 · top-10 97,30% (consulta 29/10/2026 23:58 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Cat Bot / CATBOT | registro de la detección (trending) |
| Mint / contrato | `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `9CnCbMdSHu7P4VvPzoELHbB6rmBy3quiAby36KqcswvW` | DexScreener, al detectar (2 par(es) en la consulta 29/10/2026 23:58 UTC) |
| Deployer | `EmT1MRYkDvN24ww6gzcXcdkXzipDdbsQKzMFV1XRKUig` | RugCheck `creator` |
| Par creado | 28/10/2026 20:47 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 23,4 h / 23,4 h / 27,2 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 29/10/2026 23:58 UTC |
| Holders / top-10 | 910 / 97,30% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 29/10/2026 23:58 UTC |
| Holders efectivos del top-10 | 1,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; orca 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 29/10/2026 23:58 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 29/10/2026 23:58 UTC |
| Links | DexScreener: https://dexscreener.com/solana/9CnCbMdSHu7P4VvPzoELHbB6rmBy3quiAby36KqcswvW · Solscan: https://solscan.io/token/dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump · pump.fun: https://pump.fun/coin/dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump · web: https://trycatbot.fun · twitter: https://x.com/trycatbot · telegram: https://t.me/catbottry | consulta 29/10/2026 23:58 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 29/10/2026 23:58 UTC)
- **Historia:**
  - Par creado el 28/10/2026 20:47 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 29/10/2026 20:09 UTC, con el par a 23,4 h de creado: precio $0,000003364, mcap $3.342, liquidez $3.867.
  - Velas de 1 h de GeckoTerminal (28, desde 28/10/2026 20:00 UTC): apertura $0,0002511 · máximo $0,006430 (29/10/2026 15:00 UTC) · mínimo $0,000002585 (29/10/2026 19:00 UTC) · último cierre $0,000002958.
  - En la consulta 29/10/2026 23:58 UTC: precio $0,000002969, liquidez $3.506, FDV $2.950.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 29/10/2026 20:09 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000003364 |
| Liquidez | $3.867 |
| MCap | $3.342 |
| Volumen 24 h | $7.455.241 |
| Cambio 24 h | -93% |
| Cambio m5 / h1 | -2,0% / -97,0% |
| Volumen m5 / h1 | $40 / $39.848 |
| Trades m5 (compras / ventas) | 1 / 3 |
| Edad del par | 23,4 h |
| Score del feed (WS) | 70 |

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

Desglose no reproducible desde los motivos registrados (suma 16 vs score 61; motivos sin regla: score de detección 61 (script_82, hace 3 min) > re-score 16: vale el de detección (paridad con script_97)): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-29T20:09:15+00:00, sin estado previo): **16** · motivos: WS score alto, MCap bajo, Volumen masivo, Venta dominante (buy_pressure <40%), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 81 de 46.271 tokens analizados (0,18%) quedan ≥ 56. Con score 16, este activo queda en el percentil 97,3 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 29/10/2026 20:09 UTC, hasta 31/10/2026 20:09 UTC · vigente: quedan 44,2 h.
- **Aceleración al detectar:** cambio m5 -2,0% · h1 -97,0% · h24 -93% · volumen m5/h1 0,00 · edad del par 23,4 h.
- **Precio de entrada** (alerta): $0,000003364.
- **Consulta 29/10/2026 23:58 UTC:** $0,000002969 (-11,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump_2026-10-29_200915.json` · blob `5af278027a41c71824d46d420968e008ff989c03` · commit `fed3aeb` (2026-10-29T23:34:59Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-29_200120.json` · blob `37556ae5d41e54a99999d30bac5dec664e22973c` · commit `fed3aeb` (2026-10-29T23:34:59Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-29_200915`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump · registro · 29/10/2026 20:09 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump · HTTP 200 · 29/10/2026 23:58 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump/report · HTTP 200 · 29/10/2026 23:58 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump · HTTP 200 · 29/10/2026 23:58 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/9CnCbMdSHu7P4VvPzoELHbB6rmBy3quiAby36KqcswvW/ohlcv/hour?limit=1000 · HTTP 200 · 29/10/2026 23:58 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump · HTTP 404 · 29/10/2026 23:58 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=CATBOTUSDT · HTTP 400 · 29/10/2026 23:58 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/CATBOT-USD · HTTP 404 · 29/10/2026 23:58 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.506 vs $3.506 → 0,00%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002969 vs $0,000002958 → 0,36%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump_2026-10-29_200915.json',encoding='utf-8'));d=d.get('dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump',d);p=mock.patch('time.time',return_value=1793304555);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 29/10/2026 23:58 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `4e755802984df576…`
