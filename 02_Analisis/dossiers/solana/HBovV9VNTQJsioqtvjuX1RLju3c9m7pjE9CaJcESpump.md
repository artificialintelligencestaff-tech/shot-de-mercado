# I Fart In Your General Direction (FART) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00005687 · liquidez $19.817 · mcap $56.803 (al detectar)  
Detectado el 18/10/2026 17:22 UTC por: young-0.4 · edad 10.2 min · pesos info 60 / estructura 20 / precio 20 · info 23.3 · estructura 12.6 · precio/volumen 10.1 · cobertura 93/100, [info] narrative_wave: ola 'fart': 33 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 46, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 20/10/2026 17:22 UTC (< 48 h) · vigente: quedan 47,1 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir FART

Estudio de cómo se adquiere FART, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 18/10/2026 18:17 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 18/10/2026 17:22 UTC | pumpswap `H14tTw8…SQ7H` | $19.817 | 10% | 1,009% | 10,092% | 100,921% | $99 | $297 |
| consulta 18/10/2026 18:17 UTC | pumpswap `H14tTw8…SQ7H` | $4.134 | 10% | 4,838% | 48,377% | 483,766% | $21 | $62 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump`
5. Configurar el slippage: 10% (liquidez $4.134, consulta 18/10/2026 18:17 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump) y el par en DexScreener (https://dexscreener.com/solana/H14tTw8GPbM12TSxm4MYiooD6upHoz9xWaKj435iSQ7H); mint authority / freeze authority: revocada / revocada · holders 1.763 · top-10 84,84% (consulta 18/10/2026 18:17 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump
- Par en DexScreener: https://dexscreener.com/solana/H14tTw8GPbM12TSxm4MYiooD6upHoz9xWaKj435iSQ7H
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.763 · top-10 84,84% (consulta 18/10/2026 18:17 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | I Fart In Your General Direction / FART | registro de la detección (pumpportal_live) |
| Mint / contrato | `HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `H14tTw8GPbM12TSxm4MYiooD6upHoz9xWaKj435iSQ7H` | DexScreener, al detectar (2 par(es) en la consulta 18/10/2026 18:17 UTC) |
| Deployer | `29yFzeBZgxf5zqrAkKXwgZtQehRf4pL8WbV2nRJikbw8` | PumpPortal (evento create), al detectar |
| Par creado | 18/10/2026 17:12 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,2 min / 10,2 min / 65,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 18/10/2026 18:17 UTC |
| Holders / top-10 | 1.763 / 84,84% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 18/10/2026 18:17 UTC |
| Holders efectivos del top-10 | 1,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 18/10/2026 18:17 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 18/10/2026 18:17 UTC |
| Links | DexScreener: https://dexscreener.com/solana/H14tTw8GPbM12TSxm4MYiooD6upHoz9xWaKj435iSQ7H · Solscan: https://solscan.io/token/HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump · pump.fun: https://pump.fun/coin/HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump · twitter: https://x.com/elonmusk/status/2111865900680778194?s=20 | consulta 18/10/2026 18:17 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 18/10/2026 18:17 UTC)
- **Historia:**
  - Par creado el 18/10/2026 17:12 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 18/10/2026 17:22 UTC, con el par a 10,2 min de creado: precio $0,00005687, mcap $56.803, liquidez $19.817.
  - Velas de 1 h de GeckoTerminal (2, desde 18/10/2026 17:00 UTC): apertura $0,00004158 · máximo $0,00008732 (18/10/2026 17:00 UTC) · mínimo $0,000004552 (18/10/2026 18:00 UTC) · último cierre $0,000004552.
  - En la consulta 18/10/2026 18:17 UTC: precio $0,000004722, liquidez $4.134, FDV $4.529.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 18/10/2026 17:22 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00005687 |
| Liquidez | $19.817 |
| MCap | $56.803 |
| Volumen 24 h | $201.139 |
| Cambio 24 h | +37% |
| Cambio m5 / h1 | -18,6% / +36,9% |
| Volumen m5 / h1 | $49.756 / $201.139 |
| Trades m5 (compras / ventas) | 796 / 560 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 46; motivos sin regla: young-0.4 · edad 10.2 min · pesos info 60 / estructura 20 / precio 20 · info 23.3 · estructura 12.6 · precio/volumen 10.1 · cobertura 93/100, [info] narrative_wave: ola 'fart': 33 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1446 · top-10 37.9 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1446/5004 = 0.29 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×3.0 la tasa horaria (s 0.59), [precio/volumen] buy_pressure_shift: compras 59% en 5 min vs 56% en 1 h (s 0.16), [precio/volumen] liquidity_inflow: liquidez +45% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 661→1446 (+130.8/min) · top10 40.7%→37.9% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=19817.4, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 46 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-18T17:22:13+00:00, sin estado previo): **30** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez baja, Subida 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 64 de 39.863 tokens analizados (0,16%) quedan ≥ 56. Con score 30, este activo queda en el percentil 97,7 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 18/10/2026 17:22 UTC, hasta 20/10/2026 17:22 UTC · vigente: quedan 47,1 h.
- **Aceleración al detectar:** cambio m5 -18,6% · h1 +36,9% · h24 +37% · volumen m5/h1 0,25 · edad del par 10,2 min.
- **Precio de entrada** (alerta): $0,00005687.
- **Consulta 18/10/2026 18:17 UTC:** $0,000004722 (-91,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump_2026-10-18_172213.json` · blob `3367e0ee0bd206dc8879bc43f689112909bbbf07` · commit `2d91259` (2026-10-18T18:07:38Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-18_172213`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump · registro · 18/10/2026 17:22 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump · HTTP 200 · 18/10/2026 18:17 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump/report · HTTP 200 · 18/10/2026 18:17 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump · HTTP 200 · 18/10/2026 18:17 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/H14tTw8GPbM12TSxm4MYiooD6upHoz9xWaKj435iSQ7H/ohlcv/hour?limit=1000 · HTTP 200 · 18/10/2026 18:17 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump · HTTP 404 · 18/10/2026 18:17 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=FARTUSDT · HTTP 400 · 18/10/2026 18:17 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/FART-USD · HTTP 404 · 18/10/2026 18:17 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $4.134 vs $4.167 → 0,78%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000004722 vs $0,000004552 → 3,60%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump_2026-10-18_172213.json',encoding='utf-8'));d=d.get('HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump',d);p=mock.patch('time.time',return_value=1792344133);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HBovV9VNTQJsioqtvjuX1RLju3c9m7pjE9CaJcESpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 18/10/2026 18:17 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `82c7a22375688221…`
