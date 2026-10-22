# fartless (fartless) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00005477 · liquidez $19.194 · mcap $54.703 (al detectar)  
Detectado el 22/10/2026 05:07 UTC por: young-0.4 · edad 11.3 min · pesos info 59 / estructura 20 / precio 20 · info 17.5 · estructura 12.8 · precio/volumen 9.9 · cobertura 93/100, [info] narrative_wave: ola 'fartless': 8 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.6 (score 40, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 24/10/2026 05:07 UTC (< 48 h) · vigente: quedan 46,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir fartless

Estudio de cómo se adquiere fartless, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 22/10/2026 06:30 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 22/10/2026 05:07 UTC | pumpswap `EPb75PN…QV6v` | $19.194 | 10% | 1,042% | 10,420% | 104,197% | $96 | $288 |
| consulta 22/10/2026 06:30 UTC | pumpswap `EPb75PN…QV6v` | $2.403 | 10% | 8,322% | 83,223% | 832,234% | $12 | $36 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump`
5. Configurar el slippage: 10% (liquidez $2.403, consulta 22/10/2026 06:30 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump) y el par en DexScreener (https://dexscreener.com/solana/EPb75PNZ8coCHFRKtmCV5Rq6RiKQLL8UAdtuLRydQV6v); mint authority / freeze authority: revocada / revocada · holders 1.070 · top-10 97,51% (consulta 22/10/2026 06:30 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump
- Par en DexScreener: https://dexscreener.com/solana/EPb75PNZ8coCHFRKtmCV5Rq6RiKQLL8UAdtuLRydQV6v
- Página del lanzamiento (pump.fun): https://pump.fun/coin/9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.070 · top-10 97,51% (consulta 22/10/2026 06:30 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | fartless / fartless | registro de la detección (pumpportal_live) |
| Mint / contrato | `9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `EPb75PNZ8coCHFRKtmCV5Rq6RiKQLL8UAdtuLRydQV6v` | DexScreener, al detectar (6 par(es) en la consulta 22/10/2026 06:30 UTC) |
| Deployer | `F5XvCe4233m6mHRbkkq2ZsFvqrPAnRrDBExeQy2fwagQ` | PumpPortal (evento create), al detectar |
| Par creado | 22/10/2026 04:55 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,3 min / 11,3 min / 94,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 22/10/2026 06:30 UTC |
| Holders / top-10 | 1.070 / 97,51% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 22/10/2026 06:30 UTC |
| Holders efectivos del top-10 | 1,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 22/10/2026 06:30 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 22/10/2026 06:30 UTC |
| Links | DexScreener: https://dexscreener.com/solana/EPb75PNZ8coCHFRKtmCV5Rq6RiKQLL8UAdtuLRydQV6v · Solscan: https://solscan.io/token/9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump · pump.fun: https://pump.fun/coin/9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump · web / Telegram / X: no publicados en DexScreener | consulta 22/10/2026 06:30 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 22/10/2026 06:30 UTC)
- **Historia:**
  - Par creado el 22/10/2026 04:55 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 22/10/2026 05:07 UTC, con el par a 11,3 min de creado: precio $0,00005477, mcap $54.703, liquidez $19.194.
  - Velas de 1 h de GeckoTerminal (3, desde 22/10/2026 04:00 UTC): apertura $0,00004279 · máximo $0,0001099 (22/10/2026 05:00 UTC) · mínimo $0,000002388 (22/10/2026 06:00 UTC) · último cierre $0,000002535.
  - En la consulta 22/10/2026 06:30 UTC: precio $0,000002391, liquidez $2.403, FDV $2.301.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 22/10/2026 05:07 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00005477 |
| Liquidez | $19.194 |
| MCap | $54.703 |
| Volumen 24 h | $143.536 |
| Cambio 24 h | +21% |
| Cambio m5 / h1 | -33,6% / +21,4% |
| Volumen m5 / h1 | $60.882 / $143.536 |
| Trades m5 (compras / ventas) | 915 / 710 |
| Edad del par | 11,3 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 40; motivos sin regla: young-0.4 · edad 11.3 min · pesos info 59 / estructura 20 / precio 20 · info 17.5 · estructura 12.8 · precio/volumen 9.9 · cobertura 93/100, [info] narrative_wave: ola 'fartless': 8 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter'] · descripción 0 caracteres → +2.6, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 1274 · top-10 37.9 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1274/3836 = 0.33 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×5.1 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 56% en 5 min vs 56% en 1 h (s 0.01), [precio/volumen] liquidity_inflow: liquidez +13% en 8 min (s 0.43), [precio/volumen] holder_accumulation: holders 962→1274 (+52.0/min) · top10 33.1%→37.9% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=19194.4, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 40 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-22T05:07:10+00:00, sin estado previo): **30** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez baja, Subida 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 74 de 43.766 tokens analizados (0,17%) quedan ≥ 56. Con score 30, este activo queda en el percentil 97,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 22/10/2026 05:07 UTC, hasta 24/10/2026 05:07 UTC · vigente: quedan 46,6 h.
- **Aceleración al detectar:** cambio m5 -33,6% · h1 +21,4% · h24 +21% · volumen m5/h1 0,42 · edad del par 11,3 min.
- **Precio de entrada** (alerta): $0,00005477.
- **Consulta 22/10/2026 06:30 UTC:** $0,000002391 (-95,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump_2026-10-22_050710.json` · blob `5fe575a0e620f4c2bb20fad3fdb94630e023d1b7` · commit `26b9c0c` (2026-10-22T06:22:56Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-22_050710`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump · registro · 22/10/2026 05:07 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump · HTTP 200 · 22/10/2026 06:30 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump/report · HTTP 200 · 22/10/2026 06:30 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump · HTTP 200 · 22/10/2026 06:30 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/EPb75PNZ8coCHFRKtmCV5Rq6RiKQLL8UAdtuLRydQV6v/ohlcv/hour?limit=1000 · HTTP 200 · 22/10/2026 06:30 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump · HTTP 404 · 22/10/2026 06:30 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=FARTLESSUSDT · HTTP 400 · 22/10/2026 06:30 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/FARTLESS-USD · HTTP 404 · 22/10/2026 06:30 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.403 vs $2.399 → 0,16%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002391 vs $0,000002535 → 5,68%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump_2026-10-22_050710.json',encoding='utf-8'));d=d.get('9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump',d);p=mock.patch('time.time',return_value=1792645630);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 9WFCdTCE7JBbPTQP2hnUdAGeARZWNHmPoo9CoEj1pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 22/10/2026 06:30 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `7bff922c8cea6104…`
