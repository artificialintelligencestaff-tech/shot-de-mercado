# thrustcoin (thrust) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00009031 · liquidez $24.807 · mcap $90.313 (al detectar)  
Detectado el 18/10/2026 15:01 UTC por: young-0.4 · edad 10.3 min · pesos info 60 / estructura 20 / precio 20 · info 20.3 · estructura 13.5 · precio/volumen 11.7 · cobertura 93/100, [info] narrative_wave: ola 'thrustcoin': 14 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 45, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 20/10/2026 15:01 UTC (< 48 h) · vigente: quedan 47,2 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir thrust

Estudio de cómo se adquiere thrust, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 18/10/2026 15:51 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 18/10/2026 15:01 UTC | pumpswap `2QRcK27…s1Lt` | $24.807 | 10% | 0,806% | 8,062% | 80,622% | $124 | $372 |
| consulta 18/10/2026 15:51 UTC | pumpswap `2QRcK27…s1Lt` | $5.005 | 10% | 3,996% | 39,960% | 399,596% | $25 | $75 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump`
5. Configurar el slippage: 10% (liquidez $5.005, consulta 18/10/2026 15:51 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump) y el par en DexScreener (https://dexscreener.com/solana/2QRcK27Cv6Rtyzuq1VLcN3MYhia5gSeuZmkpvB1Ws1Lt); mint authority / freeze authority: revocada / revocada · holders 2.325 · top-10 80,41% (consulta 18/10/2026 15:51 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump
- Par en DexScreener: https://dexscreener.com/solana/2QRcK27Cv6Rtyzuq1VLcN3MYhia5gSeuZmkpvB1Ws1Lt
- Página del lanzamiento (pump.fun): https://pump.fun/coin/6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.325 · top-10 80,41% (consulta 18/10/2026 15:51 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | thrustcoin / thrust | registro de la detección (pumpportal_live) |
| Mint / contrato | `6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `2QRcK27Cv6Rtyzuq1VLcN3MYhia5gSeuZmkpvB1Ws1Lt` | DexScreener, al detectar (3 par(es) en la consulta 18/10/2026 15:51 UTC) |
| Deployer | `CMipoWEjjm9he34xrS1nvJmTjfdKSxZKD2CHP1rfa8bo` | PumpPortal (evento create), al detectar |
| Par creado | 18/10/2026 14:51 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,3 min / 10,3 min / 60,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 18/10/2026 15:51 UTC |
| Holders / top-10 | 2.325 / 80,41% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 18/10/2026 15:51 UTC |
| Holders efectivos del top-10 | 1,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 18/10/2026 15:51 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 18/10/2026 15:51 UTC |
| Links | DexScreener: https://dexscreener.com/solana/2QRcK27Cv6Rtyzuq1VLcN3MYhia5gSeuZmkpvB1Ws1Lt · Solscan: https://solscan.io/token/6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump · pump.fun: https://pump.fun/coin/6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump · web / Telegram / X: no publicados en DexScreener | consulta 18/10/2026 15:51 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 18/10/2026 15:51 UTC)
- **Historia:**
  - Par creado el 18/10/2026 14:51 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 18/10/2026 15:01 UTC, con el par a 10,3 min de creado: precio $0,00009031, mcap $90.313, liquidez $24.807.
  - Velas de 1 h de GeckoTerminal (2, desde 18/10/2026 14:00 UTC): apertura $0,00004195 · máximo $0,0001030 (18/10/2026 15:00 UTC) · mínimo $0,000004196 (18/10/2026 15:00 UTC) · último cierre $0,000006102.
  - En la consulta 18/10/2026 15:51 UTC: precio $0,000006187, liquidez $5.005, FDV $5.934.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 18/10/2026 15:01 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00009031 |
| Liquidez | $24.807 |
| MCap | $90.313 |
| Volumen 24 h | $191.073 |
| Cambio 24 h | +115% |
| Cambio m5 / h1 | +58,8% / +115,0% |
| Volumen m5 / h1 | $80.857 / $191.073 |
| Trades m5 (compras / ventas) | 1.273 / 1.053 |
| Edad del par | 10,3 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 45; motivos sin regla: young-0.4 · edad 10.3 min · pesos info 60 / estructura 20 / precio 20 · info 20.3 · estructura 13.5 · precio/volumen 11.7 · cobertura 93/100, [info] narrative_wave: ola 'thrustcoin': 14 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1451 · top-10 36.1 % → +2.4, [estructura] dev_wallet: creador compró 6.7 % del supply → +1.0, [estructura] holder_to_txn_ratio: holders/txns 1451/5583 = 0.26 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×5.1 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +53% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 615→1451 (+139.3/min) · top10 45.2%→36.1% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=24807.19, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 45 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-18T15:01:47+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 65 de 39.721 tokens analizados (0,16%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 18/10/2026 15:01 UTC, hasta 20/10/2026 15:01 UTC · vigente: quedan 47,2 h.
- **Aceleración al detectar:** cambio m5 +58,8% · h1 +115,0% · h24 +115% · volumen m5/h1 0,42 · edad del par 10,3 min.
- **Precio de entrada** (alerta): $0,00009031.
- **Consulta 18/10/2026 15:51 UTC:** $0,000006187 (-93,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump_2026-10-18_150147.json` · blob `0c67a1dd1751e912a8263e5f2c7a13de472d80a0` · commit `c44f8a7` (2026-10-18T15:42:24Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-18_150147`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump · registro · 18/10/2026 15:01 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump · HTTP 200 · 18/10/2026 15:51 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump/report · HTTP 200 · 18/10/2026 15:51 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump · HTTP 200 · 18/10/2026 15:51 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/2QRcK27Cv6Rtyzuq1VLcN3MYhia5gSeuZmkpvB1Ws1Lt/ohlcv/hour?limit=1000 · HTTP 200 · 18/10/2026 15:51 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump · HTTP 404 · 18/10/2026 15:51 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=THRUSTUSDT · HTTP 400 · 18/10/2026 15:51 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/THRUST-USD · HTTP 404 · 18/10/2026 15:51 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $5.005 vs $4.951 → 1,07%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000006187 vs $0,000006102 → 1,38%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump_2026-10-18_150147.json',encoding='utf-8'));d=d.get('6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump',d);p=mock.patch('time.time',return_value=1792335707);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 6hgCbySsJFVxHCZEy4H9E7WnSY7HVnZkBrUHCa9rpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 18/10/2026 15:51 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `8daadc210b17fbed…`
