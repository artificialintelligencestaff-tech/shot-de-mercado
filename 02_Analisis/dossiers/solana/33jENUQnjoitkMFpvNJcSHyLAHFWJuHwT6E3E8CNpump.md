# Doge Pepe (DOPE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0004528 · liquidez $61.518 · mcap $452.885 (al detectar)  
Detectado el 11/10/2026 13:44 UTC por: young-0.4 · edad 11.1 min · pesos info 59 / estructura 20 / precio 20 · info 26.1 · estructura 15.3 · precio/volumen 11.0 · cobertura 93/100, [info] narrative_wave: ola 'doge': 16 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 52, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 13/10/2026 13:44 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir DOPE

Estudio de cómo se adquiere DOPE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/10/2026 14:12 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 11/10/2026 13:44 UTC | pumpswap `6iep3Eg…8AGQ` | $61.518 | 5% | 0,325% | 3,251% | 32,511% | $308 | $923 |
| consulta 11/10/2026 14:12 UTC | pumpswap `6iep3Eg…8AGQ` | $86.176 | 5% | 0,232% | 2,321% | 23,208% | $431 | $1.293 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump`
5. Configurar el slippage: 5% (liquidez $86.176, consulta 11/10/2026 14:12 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump) y el par en DexScreener (https://dexscreener.com/solana/6iep3EgqksbZwgzMBCyAJtiVtVYkCgL9BnPBEwLR8AGQ); mint authority / freeze authority: revocada / revocada · holders 7.739 · top-10 18,48% (consulta 11/10/2026 14:12 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump
- Par en DexScreener: https://dexscreener.com/solana/6iep3EgqksbZwgzMBCyAJtiVtVYkCgL9BnPBEwLR8AGQ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 7.739 · top-10 18,48% (consulta 11/10/2026 14:12 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Doge Pepe / DOPE | registro de la detección (pumpportal_live) |
| Mint / contrato | `33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6iep3EgqksbZwgzMBCyAJtiVtVYkCgL9BnPBEwLR8AGQ` | DexScreener, al detectar (14 par(es) en la consulta 11/10/2026 14:12 UTC) |
| Deployer | `CZutgB7w4WbkeCEwFv1qxhkeGyjVGn9XXPYxjwQo3NaM` | PumpPortal (evento create), al detectar |
| Par creado | 11/10/2026 13:33 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,1 min / 11,1 min / 39,0 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/10/2026 14:12 UTC |
| Holders / top-10 | 7.739 / 18,48% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/10/2026 14:12 UTC |
| Holders efectivos del top-10 | 7,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/10/2026 14:12 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 11/10/2026 14:12 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6iep3EgqksbZwgzMBCyAJtiVtVYkCgL9BnPBEwLR8AGQ · Solscan: https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump · pump.fun: https://pump.fun/coin/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump · web: https://otcdesks.cash/coin/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump · twitter: https://x.com/essencepnl/status/2109274831673807308 | consulta 11/10/2026 14:12 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/10/2026 14:12 UTC)
- **Historia:**
  - Par creado el 11/10/2026 13:33 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 11/10/2026 13:44 UTC, con el par a 11,1 min de creado: precio $0,0004528, mcap $452.885, liquidez $61.518.
  - Velas de 1 h de GeckoTerminal (2, desde 11/10/2026 13:00 UTC): apertura $0,00004564 · máximo $0,0009086 (11/10/2026 14:00 UTC) · mínimo $0,00004201 (11/10/2026 13:00 UTC) · último cierre $0,0008042.
  - En la consulta 11/10/2026 14:12 UTC: precio $0,0008053, liquidez $86.176, FDV $795.084.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 11/10/2026 13:44 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0004528 |
| Liquidez | $61.518 |
| MCap | $452.885 |
| Volumen 24 h | $667.183 |
| Cambio 24 h | +933% |
| Cambio m5 / h1 | +13,0% / +933,0% |
| Volumen m5 / h1 | $191.883 / $667.183 |
| Trades m5 (compras / ventas) | 1.393 / 1.132 |
| Edad del par | 11,1 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 52; motivos sin regla: young-0.4 · edad 11.1 min · pesos info 59 / estructura 20 / precio 20 · info 26.1 · estructura 15.3 · precio/volumen 11.0 · cobertura 93/100, [info] narrative_wave: ola 'doge': 16 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 3378 · top-10 22.3 % → +4.9, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 3378/8321 = 0.41 → +0.7, [precio/volumen] volume_acceleration: vol 5 min ×3.5 la tasa horaria (s 0.78), [precio/volumen] buy_pressure_shift: compras 55% en 5 min vs 53% en 1 h (s 0.10), [precio/volumen] liquidity_inflow: liquidez +56% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 882→3378 (+416.0/min) · top10 28.6%→22.3% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=61518.09, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 52 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-11T13:44:11+00:00, sin estado previo): **50** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=13.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 49 de 29.187 tokens analizados (0,17%) quedan ≥ 56. Con score 50, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 11/10/2026 13:44 UTC, hasta 13/10/2026 13:44 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +13,0% · h1 +933,0% · h24 +933% · volumen m5/h1 0,29 · edad del par 11,1 min.
- **Precio de entrada** (alerta): $0,0004528.
- **Consulta 11/10/2026 14:12 UTC:** $0,0008053 (+77,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump_2026-10-11_134411.json` · blob `db64a4b876da590eb72f01d8f20215d27292106c` · commit `71c2157` (2026-10-11T14:04:40Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-11_134411`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump · registro · 11/10/2026 13:44 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump · HTTP 200 · 11/10/2026 14:12 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump/report · HTTP 200 · 11/10/2026 14:12 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump · HTTP 200 · 11/10/2026 14:12 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6iep3EgqksbZwgzMBCyAJtiVtVYkCgL9BnPBEwLR8AGQ/ohlcv/hour?limit=1000 · HTTP 200 · 11/10/2026 14:12 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump · HTTP 404 · 11/10/2026 14:12 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=DOPEUSDT · HTTP 400 · 11/10/2026 14:12 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/DOPE-USD · HTTP 404 · 11/10/2026 14:12 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $86.176 vs $189.233 → 54,46%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0008053 vs $0,0008042 → 0,13%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump_2026-10-11_134411.json',encoding='utf-8'));d=d.get('33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump',d);p=mock.patch('time.time',return_value=1791726251);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/10/2026 14:12 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `26f532ea30aadf1e…`
