# TITS (TITS) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00009375 · liquidez $25.789 · mcap $93.755 (al detectar)  
Detectado el 07/10/2026 18:00 UTC por: young-0.4 · edad 10.3 min · pesos info 60 / estructura 20 / precio 20 · info 17.6 · estructura 16.7 · precio/volumen 11.9 · cobertura 93/100, [info] narrative_wave: ola 'tits': 12 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.7 (score 46, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 09/10/2026 18:00 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir TITS

Estudio de cómo se adquiere TITS, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/10/2026 18:14 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/10/2026 18:00 UTC | pumpswap `D9epQK1…UW8Y` | $25.789 | 10% | 0,776% | 7,755% | 77,553% | $129 | $387 |
| consulta 07/10/2026 18:14 UTC | pumpswap `D9epQK1…UW8Y` | $2.297 | 10% | 8,705% | 87,052% | 870,523% | $11 | $34 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump`
5. Configurar el slippage: 10% (liquidez $2.297, consulta 07/10/2026 18:14 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump) y el par en DexScreener (https://dexscreener.com/solana/D9epQK1ESAaBSwP1suUi7h8uUyjykNv43zY2tuGuUW8Y); mint authority / freeze authority: revocada / revocada · holders 217 · top-10 99,84% (consulta 07/10/2026 18:14 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump
- Par en DexScreener: https://dexscreener.com/solana/D9epQK1ESAaBSwP1suUi7h8uUyjykNv43zY2tuGuUW8Y
- Página del lanzamiento (pump.fun): https://pump.fun/coin/5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 217 · top-10 99,84% (consulta 07/10/2026 18:14 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | TITS / TITS | registro de la detección (pumpportal_live) |
| Mint / contrato | `5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `D9epQK1ESAaBSwP1suUi7h8uUyjykNv43zY2tuGuUW8Y` | DexScreener, al detectar (2 par(es) en la consulta 07/10/2026 18:14 UTC) |
| Deployer | `G5tkyqZ88FEpevwEFnUisE26sKh38Kz2L8kRsjGKbH6X` | PumpPortal (evento create), al detectar |
| Par creado | 07/10/2026 17:50 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,3 min / 10,3 min / 24,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/10/2026 18:14 UTC |
| Holders / top-10 | 217 / 99,84% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/10/2026 18:14 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/10/2026 18:14 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 07/10/2026 18:14 UTC |
| Links | DexScreener: https://dexscreener.com/solana/D9epQK1ESAaBSwP1suUi7h8uUyjykNv43zY2tuGuUW8Y · Solscan: https://solscan.io/token/5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump · pump.fun: https://pump.fun/coin/5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump · web / Telegram / X: no publicados en DexScreener | consulta 07/10/2026 18:14 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/10/2026 18:14 UTC)
- **Historia:**
  - Par creado el 07/10/2026 17:50 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/10/2026 18:00 UTC, con el par a 10,3 min de creado: precio $0,00009375, mcap $93.755, liquidez $25.789.
  - Velas de 1 h de GeckoTerminal (2, desde 07/10/2026 17:00 UTC): apertura $0,00004962 · máximo $0,0001736 (07/10/2026 17:00 UTC) · mínimo $0,000002254 (07/10/2026 18:00 UTC) · último cierre $0,000002254.
  - En la consulta 07/10/2026 18:14 UTC: precio $0,000002254, liquidez $2.297, FDV $2.254.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/10/2026 18:00 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00009375 |
| Liquidez | $25.789 |
| MCap | $93.755 |
| Volumen 24 h | $70.981 |
| Cambio 24 h | +94% |
| Cambio m5 / h1 | +54,9% / +93,7% |
| Volumen m5 / h1 | $40.897 / $70.981 |
| Trades m5 (compras / ventas) | 1.011 / 272 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 46; motivos sin regla: young-0.4 · edad 10.3 min · pesos info 60 / estructura 20 / precio 20 · info 17.6 · estructura 16.7 · precio/volumen 11.9 · cobertura 93/100, [info] narrative_wave: ola 'tits': 12 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.7, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1121 · top-10 26.3 % → +4.8, [estructura] dev_wallet: creador compró 4.2 % del supply → +1.8, [estructura] holder_to_txn_ratio: holders/txns 1121/3444 = 0.33 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×6.9 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 79% en 5 min vs 78% en 1 h (s 0.06), [precio/volumen] liquidity_inflow: liquidez +39% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1058→1121 (+10.5/min) · top10 32.7%→26.3% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=25788.67, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 46 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-07T18:00:55+00:00, sin estado previo): **35** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen decente, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 31 de 19.385 tokens analizados (0,16%) quedan ≥ 56. Con score 35, este activo queda en el percentil 98,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/10/2026 18:00 UTC, hasta 09/10/2026 18:00 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +54,9% · h1 +93,7% · h24 +94% · volumen m5/h1 0,58 · edad del par 10,3 min.
- **Precio de entrada** (alerta): $0,00009375.
- **Consulta 07/10/2026 18:14 UTC:** $0,000002254 (-97,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump_2026-10-07_180055.json` · blob `4d1ea24b2bae6c3eb4ea68c799e005097ca2e1e8` · commit `cada667` (2026-10-07T18:05:54Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-07_180055`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump · registro · 07/10/2026 18:00 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump · HTTP 200 · 07/10/2026 18:14 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump/report · HTTP 200 · 07/10/2026 18:14 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump · HTTP 200 · 07/10/2026 18:14 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/D9epQK1ESAaBSwP1suUi7h8uUyjykNv43zY2tuGuUW8Y/ohlcv/hour?limit=1000 · HTTP 200 · 07/10/2026 18:14 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump · HTTP 404 · 07/10/2026 18:14 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=TITSUSDT · HTTP 400 · 07/10/2026 18:14 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/TITS-USD · HTTP 404 · 07/10/2026 18:14 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.297 vs $2.300 → 0,12%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002254 vs $0,000002254 → 0,00%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump_2026-10-07_180055.json',encoding='utf-8'));d=d.get('5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump',d);p=mock.patch('time.time',return_value=1791396055);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 5TWALdrNGxmAyN7mQoC7m3eGxJXitH25mmgEBBiTpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/10/2026 18:14 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `c12d7e69bb0fefc2…`
