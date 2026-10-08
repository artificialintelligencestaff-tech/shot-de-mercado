# The Stoic Penguin (Penguin) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00003411 · liquidez $14.736 · mcap $34.111 (al detectar)  
Detectado el 08/10/2026 07:54 UTC por: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 23.3 · estructura 13.0 · precio/volumen 7.2 · cobertura 93/100, [info] narrative_wave: ola 'penguin': 9 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 29 caracteres → +5.3 (score 43, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 10/10/2026 07:54 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Penguin

Estudio de cómo se adquiere Penguin, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/10/2026 08:14 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/10/2026 07:54 UTC | pumpswap `H4Jn1yG…XuX2` | $14.736 | 10% | 1,357% | 13,572% | 135,721% | $74 | $221 |
| consulta 08/10/2026 08:14 UTC | pumpswap `H4Jn1yG…XuX2` | $5.387 | 10% | 3,712% | 37,124% | 371,239% | $27 | $81 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump`
5. Configurar el slippage: 10% (liquidez $5.387, consulta 08/10/2026 08:14 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump) y el par en DexScreener (https://dexscreener.com/solana/H4Jn1yGe39YgCySJoUigduLb314ujzfEMN29BTMJXuX2); mint authority / freeze authority: revocada / revocada · holders 1.643 · top-10 77,45% (consulta 08/10/2026 08:14 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump
- Par en DexScreener: https://dexscreener.com/solana/H4Jn1yGe39YgCySJoUigduLb314ujzfEMN29BTMJXuX2
- Página del lanzamiento (pump.fun): https://pump.fun/coin/6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.643 · top-10 77,45% (consulta 08/10/2026 08:14 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | The Stoic Penguin / Penguin | registro de la detección (pumpportal_live) |
| Mint / contrato | `6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `H4Jn1yGe39YgCySJoUigduLb314ujzfEMN29BTMJXuX2` | DexScreener, al detectar (2 par(es) en la consulta 08/10/2026 08:14 UTC) |
| Deployer | `5htGpHK2oV9g2BcDqLdRBqjCLdy8mc3fsESfR5DU73eM` | PumpPortal (evento create), al detectar |
| Par creado | 08/10/2026 07:44 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,4 min / 10,4 min / 30,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/10/2026 08:14 UTC |
| Holders / top-10 | 1.643 / 77,45% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/10/2026 08:14 UTC |
| Holders efectivos del top-10 | 1,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/10/2026 08:14 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 08/10/2026 08:14 UTC |
| Links | DexScreener: https://dexscreener.com/solana/H4Jn1yGe39YgCySJoUigduLb314ujzfEMN29BTMJXuX2 · Solscan: https://solscan.io/token/6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump · pump.fun: https://pump.fun/coin/6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump · twitter: https://x.com/Zeeko__Dev/status/2108098567483138475 · reddit: https://www.reddit.com/r/funny/comments/1x08ejx/a_curious_african_penguin_hopped_aboard_a/ | consulta 08/10/2026 08:14 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/10/2026 08:14 UTC)
- **Historia:**
  - Par creado el 08/10/2026 07:44 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/10/2026 07:54 UTC, con el par a 10,4 min de creado: precio $0,00003411, mcap $34.111, liquidez $14.736.
  - Velas de 1 h de GeckoTerminal (2, desde 08/10/2026 07:00 UTC): apertura $0,00004708 · máximo $0,00007007 (08/10/2026 08:00 UTC) · mínimo $0,000005461 (08/10/2026 08:00 UTC) · último cierre $0,000006174.
  - En la consulta 08/10/2026 08:14 UTC: precio $0,000006703, liquidez $5.387, FDV $6.704.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/10/2026 07:54 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00003411 |
| Liquidez | $14.736 |
| MCap | $34.111 |
| Volumen 24 h | $100.421 |
| Cambio 24 h | -28% |
| Cambio m5 / h1 | -11,6% / -28,2% |
| Volumen m5 / h1 | $28.630 / $100.421 |
| Trades m5 (compras / ventas) | 407 / 440 |
| Edad del par | 10,4 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 43; motivos sin regla: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 23.3 · estructura 13.0 · precio/volumen 7.2 · cobertura 93/100, [info] narrative_wave: ola 'penguin': 9 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 29 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1485 · top-10 47.6 % → +2.4, [estructura] dev_wallet: creador compró 9.6 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1485/2959 = 0.50 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×3.4 la tasa horaria (s 0.77), [precio/volumen] holder_accumulation: holders 826→1485 (+54.9/min) · top10 41.1%→47.6% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=14736.08, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 43 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-08T07:54:35+00:00, sin estado previo): **15** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 35 de 21.169 tokens analizados (0,17%) quedan ≥ 56. Con score 15, este activo queda en el percentil 97,3 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/10/2026 07:54 UTC, hasta 10/10/2026 07:54 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -11,6% · h1 -28,2% · h24 -28% · volumen m5/h1 0,29 · edad del par 10,4 min.
- **Precio de entrada** (alerta): $0,00003411.
- **Consulta 08/10/2026 08:14 UTC:** $0,000006703 (-80,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump_2026-10-08_075435.json` · blob `2f06b4da17f130bcda983308b051f0e4aa96c8c5` · commit `f3b0741` (2026-10-08T08:08:21Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-08_075435`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump · registro · 08/10/2026 07:54 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump · HTTP 200 · 08/10/2026 08:14 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump/report · HTTP 200 · 08/10/2026 08:14 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump · HTTP 200 · 08/10/2026 08:14 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/H4Jn1yGe39YgCySJoUigduLb314ujzfEMN29BTMJXuX2/ohlcv/hour?limit=1000 · HTTP 200 · 08/10/2026 08:14 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump · HTTP 404 · 08/10/2026 08:14 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=PENGUINUSDT · HTTP 400 · 08/10/2026 08:14 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/PENGUIN-USD · HTTP 404 · 08/10/2026 08:14 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $5.387 vs $5.382 → 0,10%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000006703 vs $0,000006174 → 7,89%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump_2026-10-08_075435.json',encoding='utf-8'));d=d.get('6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump',d);p=mock.patch('time.time',return_value=1791446075);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 6Aug5n6KjCfu8JmMk1xxCxoqtyprD3uNcmHF4Phdpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/10/2026 08:14 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `3cf217daa7f5a35f…`
