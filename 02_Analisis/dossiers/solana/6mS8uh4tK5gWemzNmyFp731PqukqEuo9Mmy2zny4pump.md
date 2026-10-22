# Shamonda virus (SHAV) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001252 · liquidez $29.979 · mcap $125.234 (al detectar)  
Detectado el 22/10/2026 10:21 UTC por: young-0.4 · edad 15.3 min · pesos info 57 / estructura 21 / precio 21 · info 13.6 · estructura 18.1 · precio/volumen 9.1 · cobertura 84/100, [info] narrative_wave: ola 'virus': 6 lanzamientos más en 1 h → +10.8, [info] dex_profile: perfil pago en DexScreener → +2.9 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 24/10/2026 10:21 UTC (< 48 h) · vigente: quedan 47,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SHAV

Estudio de cómo se adquiere SHAV, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 22/10/2026 10:54 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 22/10/2026 10:21 UTC | pumpswap `64FvRkt…vSoM` | $29.979 | 10% | 0,667% | 6,671% | 66,713% | $150 | $450 |
| consulta 22/10/2026 10:54 UTC | pumpswap `64FvRkt…vSoM` | $34.277 | 10% | 0,583% | 5,835% | 58,349% | $171 | $514 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump`
5. Configurar el slippage: 10% (liquidez $34.277, consulta 22/10/2026 10:54 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump) y el par en DexScreener (https://dexscreener.com/solana/64FvRkt9dMgGgREKQRfowCJHqkqYLG17afDtU5mJvSoM); mint authority / freeze authority: revocada / revocada · holders 1.648 · top-10 26,51% (consulta 22/10/2026 10:54 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump
- Par en DexScreener: https://dexscreener.com/solana/64FvRkt9dMgGgREKQRfowCJHqkqYLG17afDtU5mJvSoM
- Página del lanzamiento (pump.fun): https://pump.fun/coin/6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.648 · top-10 26,51% (consulta 22/10/2026 10:54 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Shamonda virus / SHAV | registro de la detección (pumpportal_live) |
| Mint / contrato | `6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `64FvRkt9dMgGgREKQRfowCJHqkqYLG17afDtU5mJvSoM` | DexScreener, al detectar (3 par(es) en la consulta 22/10/2026 10:54 UTC) |
| Deployer | `BUWmKsrTLDHnJL9hD15cxuQe7infJdzA6osMDbanGpW5` | PumpPortal (evento create), al detectar |
| Par creado | 22/10/2026 10:06 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 15,3 min / 15,3 min / 48,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 22/10/2026 10:54 UTC |
| Holders / top-10 | 1.648 / 26,51% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 22/10/2026 10:54 UTC |
| Holders efectivos del top-10 | 4,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 22/10/2026 10:54 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 22/10/2026 10:54 UTC |
| Links | DexScreener: https://dexscreener.com/solana/64FvRkt9dMgGgREKQRfowCJHqkqYLG17afDtU5mJvSoM · Solscan: https://solscan.io/token/6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump · pump.fun: https://pump.fun/coin/6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump · web: https://www.euronews.com/2026/10/22/france-confirms-first-human-case-of-shamonda-virus-previously-found-only-in-animals · twitter: https://x.com/i/status/2113197745288700045 | consulta 22/10/2026 10:54 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 22/10/2026 10:54 UTC)
- **Historia:**
  - Par creado el 22/10/2026 10:06 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 22/10/2026 10:21 UTC, con el par a 15,3 min de creado: precio $0,0001252, mcap $125.234, liquidez $29.979.
  - Velas de 1 h de GeckoTerminal (1, desde 22/10/2026 10:00 UTC): apertura $0,00004674 · máximo $0,0002646 (22/10/2026 10:00 UTC) · mínimo $0,00004674 (22/10/2026 10:00 UTC) · último cierre $0,0001721.
  - En la consulta 22/10/2026 10:54 UTC: precio $0,0001683, liquidez $34.277, FDV $163.086.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 22/10/2026 10:21 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001252 |
| Liquidez | $29.979 |
| MCap | $125.234 |
| Volumen 24 h | $123.717 |
| Cambio 24 h | +166% |
| Cambio m5 / h1 | +15,3% / +166,0% |
| Volumen m5 / h1 | $25.086 / $123.717 |
| Trades m5 (compras / ventas) | 267 / 153 |
| Edad del par | 15,3 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 15.3 min · pesos info 57 / estructura 21 / precio 21 · info 13.6 · estructura 18.1 · precio/volumen 9.1 · cobertura 84/100, [info] narrative_wave: ola 'virus': 6 lanzamientos más en 1 h → +10.8, [info] dex_profile: perfil pago en DexScreener → +2.9, [estructura] bonding_progress: graduado (pumpswap) → +10.2, [estructura] holders_struct: holders 450 · top-10 21.2 % → +5.1, [estructura] dev_wallet: creador compró 2.9 % del supply → +2.3, [estructura] holder_to_txn_ratio: holders/txns 450/1682 = 0.27 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×2.4 la tasa horaria (s 0.37), [precio/volumen] liquidity_inflow: liquidez +31% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 296→450 (+25.7/min) · top10 41.9%→21.2% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=29979.12, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=17412.34, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-22T10:21:26+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 74 de 43.832 tokens analizados (0,17%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 22/10/2026 10:21 UTC, hasta 24/10/2026 10:21 UTC · vigente: quedan 47,4 h.
- **Aceleración al detectar:** cambio m5 +15,3% · h1 +166,0% · h24 +166% · volumen m5/h1 0,20 · edad del par 15,3 min.
- **Precio de entrada** (alerta): $0,0001252.
- **Consulta 22/10/2026 10:54 UTC:** $0,0001683 (+34,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump_2026-10-22_102126.json` · blob `db0b03deac1c767381142054eb4cde18ee104809` · commit `f2344dd` (2026-10-22T10:47:28Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-22_102126`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump · registro · 22/10/2026 10:21 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump · HTTP 200 · 22/10/2026 10:54 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump/report · HTTP 200 · 22/10/2026 10:54 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump · HTTP 200 · 22/10/2026 10:54 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/64FvRkt9dMgGgREKQRfowCJHqkqYLG17afDtU5mJvSoM/ohlcv/hour?limit=1000 · HTTP 200 · 22/10/2026 10:54 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump · HTTP 404 · 22/10/2026 10:54 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SHAVUSDT · HTTP 400 · 22/10/2026 10:54 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SHAV-USD · HTTP 404 · 22/10/2026 10:54 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $34.277 vs $32.952 → 3,87%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001683 vs $0,0001721 → 2,22%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump_2026-10-22_102126.json',encoding='utf-8'));d=d.get('6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump',d);p=mock.patch('time.time',return_value=1792664486);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 6mS8uh4tK5gWemzNmyFp731PqukqEuo9Mmy2zny4pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 22/10/2026 10:54 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `6424be74431263e0…`
