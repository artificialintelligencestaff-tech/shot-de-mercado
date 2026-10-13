# wizardcat (wizardcat) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00004079 · liquidez $15.867 · mcap $40.793 (al detectar)  
Detectado el 13/10/2026 17:32 UTC por: young-0.4 · edad 10.0 min · pesos info 60 / estructura 20 / precio 20 · info 20.3 · estructura 12.9 · precio/volumen 9.7 · cobertura 93/100, [info] narrative_wave: ola 'wizardcat': 8 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 43, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 15/10/2026 17:32 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir wizardcat

Estudio de cómo se adquiere wizardcat, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 13/10/2026 17:41 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 13/10/2026 17:32 UTC | pumpswap `53QHU8H…hwPD` | $15.867 | 10% | 1,260% | 12,605% | 126,047% | $79 | $238 |
| consulta 13/10/2026 17:41 UTC | pumpswap `53QHU8H…hwPD` | $22.237 | 10% | 0,899% | 8,994% | 89,940% | $111 | $334 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump`
5. Configurar el slippage: 10% (liquidez $22.237, consulta 13/10/2026 17:41 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump) y el par en DexScreener (https://dexscreener.com/solana/53QHU8H5g4EvZPJYGNi4PPKo2U6h6JTZENtRS1n7hwPD); mint authority / freeze authority: revocada / revocada · holders 1.821 · top-10 33,23% (consulta 13/10/2026 17:41 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump
- Par en DexScreener: https://dexscreener.com/solana/53QHU8H5g4EvZPJYGNi4PPKo2U6h6JTZENtRS1n7hwPD
- Página del lanzamiento (pump.fun): https://pump.fun/coin/DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.821 · top-10 33,23% (consulta 13/10/2026 17:41 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | wizardcat / wizardcat | registro de la detección (pumpportal_live) |
| Mint / contrato | `DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `53QHU8H5g4EvZPJYGNi4PPKo2U6h6JTZENtRS1n7hwPD` | DexScreener, al detectar (3 par(es) en la consulta 13/10/2026 17:41 UTC) |
| Deployer | `DWHEZ8JnfGtud25Gjhn3MndpTMshNEd12WMu2ciCa7ri` | PumpPortal (evento create), al detectar |
| Par creado | 13/10/2026 17:22 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,0 min / 10,0 min / 19,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 13/10/2026 17:41 UTC |
| Holders / top-10 | 1.821 / 33,23% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 13/10/2026 17:41 UTC |
| Holders efectivos del top-10 | 3,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 13/10/2026 17:41 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 13/10/2026 17:41 UTC |
| Links | DexScreener: https://dexscreener.com/solana/53QHU8H5g4EvZPJYGNi4PPKo2U6h6JTZENtRS1n7hwPD · Solscan: https://solscan.io/token/DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump · pump.fun: https://pump.fun/coin/DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump · web / Telegram / X: no publicados en DexScreener | consulta 13/10/2026 17:41 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 13/10/2026 17:41 UTC)
- **Historia:**
  - Par creado el 13/10/2026 17:22 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 13/10/2026 17:32 UTC, con el par a 10,0 min de creado: precio $0,00004079, mcap $40.793, liquidez $15.867.
  - Velas de 1 h de GeckoTerminal (1, desde 13/10/2026 17:00 UTC): apertura $0,00004181 · máximo $0,00008602 (13/10/2026 17:00 UTC) · mínimo $0,00001728 (13/10/2026 17:00 UTC) · último cierre $0,00008421.
  - En la consulta 13/10/2026 17:41 UTC: precio $0,00007254, liquidez $22.237, FDV $72.542.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 13/10/2026 17:32 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00004079 |
| Liquidez | $15.867 |
| MCap | $40.793 |
| Volumen 24 h | $44.559 |
| Cambio 24 h | -6% |
| Cambio m5 / h1 | -26,2% / -6,3% |
| Volumen m5 / h1 | $17.536 / $44.559 |
| Trades m5 (compras / ventas) | 400 / 275 |
| Edad del par | 10,0 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 43; motivos sin regla: young-0.4 · edad 10.0 min · pesos info 60 / estructura 20 / precio 20 · info 20.3 · estructura 12.9 · precio/volumen 9.7 · cobertura 93/100, [info] narrative_wave: ola 'wizardcat': 8 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1433 · top-10 40.2 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1433/1593 = 0.90 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×4.7 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +12% en 8 min (s 0.39), [precio/volumen] holder_accumulation: holders 1035→1433 (+66.3/min) · top10 40.0%→40.2% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=15867.14, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 43 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-13T17:32:04+00:00, sin estado previo): **0** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen bajo, Liquidez baja.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 53 de 33.786 tokens analizados (0,16%) quedan ≥ 56. Con score 0, este activo queda en el percentil 42,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 13/10/2026 17:32 UTC, hasta 15/10/2026 17:32 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -26,2% · h1 -6,3% · h24 -6% · volumen m5/h1 0,39 · edad del par 10,0 min.
- **Precio de entrada** (alerta): $0,00004079.
- **Consulta 13/10/2026 17:41 UTC:** $0,00007254 (+77,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump_2026-10-13_173204.json` · blob `19bd787b740addfb3f46848cca6a17d8d5be1251` · commit `fbddad2` (2026-10-13T17:33:35Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-13_173204`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump · registro · 13/10/2026 17:32 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump · HTTP 200 · 13/10/2026 17:41 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump/report · HTTP 200 · 13/10/2026 17:41 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump · HTTP 200 · 13/10/2026 17:41 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/53QHU8H5g4EvZPJYGNi4PPKo2U6h6JTZENtRS1n7hwPD/ohlcv/hour?limit=1000 · HTTP 200 · 13/10/2026 17:41 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump · HTTP 404 · 13/10/2026 17:41 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=WIZARDCATUSDT · HTTP 400 · 13/10/2026 17:41 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/WIZARDCAT-USD · HTTP 404 · 13/10/2026 17:41 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $22.237 vs $22.175 → 0,28%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00007254 vs $0,00008421 → 13,85%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump_2026-10-13_173204.json',encoding='utf-8'));d=d.get('DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump',d);p=mock.patch('time.time',return_value=1791912724);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint DRPDTRjTg2RrmfVM8g6DXMtXBGRWb37i7VTm2Ymgpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 13/10/2026 17:41 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `b5b95eabdb9099b5…`
