# Official Elon Coin (ELON) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000009168 · liquidez $6.938 · mcap $9.168 (al detectar)  
Detectado el 17/10/2026 04:51 UTC por: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 23.3 · estructura 12.7 · precio/volumen 8.4 · cobertura 93/100, [info] narrative_wave: ola 'elon': 22 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 44, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 19/10/2026 04:51 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ELON

Estudio de cómo se adquiere ELON, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 17/10/2026 05:22 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 17/10/2026 04:51 UTC | pumpswap `E8SYVXE…gP6a` | $6.938 | 10% | 2,883% | 28,827% | 288,273% | $35 | $104 |
| consulta 17/10/2026 05:22 UTC | pumpswap `E8SYVXE…gP6a` | $2.942 | 10% | 6,798% | 67,976% | 679,757% | $15 | $44 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump`
5. Configurar el slippage: 10% (liquidez $2.942, consulta 17/10/2026 05:22 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump) y el par en DexScreener (https://dexscreener.com/solana/E8SYVXEVoYK2M141Dj5moRDVqEcFzTVbgFmmNb7CgP6a); mint authority / freeze authority: revocada / revocada · holders 1.214 · top-10 94,28% (consulta 17/10/2026 05:22 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump
- Par en DexScreener: https://dexscreener.com/solana/E8SYVXEVoYK2M141Dj5moRDVqEcFzTVbgFmmNb7CgP6a
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.214 · top-10 94,28% (consulta 17/10/2026 05:22 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Official Elon Coin / ELON | registro de la detección (pumpportal_live) |
| Mint / contrato | `HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `E8SYVXEVoYK2M141Dj5moRDVqEcFzTVbgFmmNb7CgP6a` | DexScreener, al detectar (2 par(es) en la consulta 17/10/2026 05:22 UTC) |
| Deployer | `AufH68UFBGSVVRL9D7u5W6NySCrukL4fWfSRTxDcJC6u` | PumpPortal (evento create), al detectar |
| Par creado | 17/10/2026 04:40 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,4 min / 10,4 min / 41,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 17/10/2026 05:22 UTC |
| Holders / top-10 | 1.214 / 94,28% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 17/10/2026 05:22 UTC |
| Holders efectivos del top-10 | 1,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 17/10/2026 05:22 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 17/10/2026 05:22 UTC |
| Links | DexScreener: https://dexscreener.com/solana/E8SYVXEVoYK2M141Dj5moRDVqEcFzTVbgFmmNb7CgP6a · Solscan: https://solscan.io/token/HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump · pump.fun: https://pump.fun/coin/HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump · web: https://otcdesks.cash/coin/HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump · twitter: https://x.com/lilbruhfish/status/2111314590462083151 | consulta 17/10/2026 05:22 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 17/10/2026 05:22 UTC)
- **Historia:**
  - Par creado el 17/10/2026 04:40 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 17/10/2026 04:51 UTC, con el par a 10,4 min de creado: precio $0,000009168, mcap $9.168, liquidez $6.938.
  - Velas de 1 h de GeckoTerminal (2, desde 17/10/2026 04:00 UTC): apertura $0,00004028 · máximo $0,00006346 (17/10/2026 04:00 UTC) · mínimo $0,000002761 (17/10/2026 05:00 UTC) · último cierre $0,000003064.
  - En la consulta 17/10/2026 05:22 UTC: precio $0,000003068, liquidez $2.942, FDV $2.920.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 17/10/2026 04:51 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000009168 |
| Liquidez | $6.938 |
| MCap | $9.168 |
| Volumen 24 h | $114.000 |
| Cambio 24 h | -79% |
| Cambio m5 / h1 | -83,3% / -79,4% |
| Volumen m5 / h1 | $59.325 / $114.000 |
| Trades m5 (compras / ventas) | 1.059 / 879 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 44; motivos sin regla: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 23.3 · estructura 12.7 · precio/volumen 8.4 · cobertura 93/100, [info] narrative_wave: ola 'elon': 22 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1305 · top-10 41.1 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1305/3773 = 0.35 → +0.6, [precio/volumen] volume_acceleration: vol 5 min ×6.2 la tasa horaria (s 1.00), [precio/volumen] holder_accumulation: holders 386→1305 (+76.6/min) · top10 50.0%→41.1% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=6937.87, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 44 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-17T04:51:17+00:00, sin estado previo): **10** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 61 de 38.058 tokens analizados (0,16%) quedan ≥ 56. Con score 10, este activo queda en el percentil 93,6 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 17/10/2026 04:51 UTC, hasta 19/10/2026 04:51 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -83,3% · h1 -79,4% · h24 -79% · volumen m5/h1 0,52 · edad del par 10,4 min.
- **Precio de entrada** (alerta): $0,000009168.
- **Consulta 17/10/2026 05:22 UTC:** $0,000003068 (-66,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump_2026-10-17_045117.json` · blob `fae5b7ab8f02d5549790a1b14a07c45de27f6aff` · commit `cef320b` (2026-10-17T05:15:54Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-17_045117`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump · registro · 17/10/2026 04:51 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump · HTTP 200 · 17/10/2026 05:22 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump/report · HTTP 200 · 17/10/2026 05:22 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump · HTTP 200 · 17/10/2026 05:22 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/E8SYVXEVoYK2M141Dj5moRDVqEcFzTVbgFmmNb7CgP6a/ohlcv/hour?limit=1000 · HTTP 200 · 17/10/2026 05:22 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump · HTTP 404 · 17/10/2026 05:22 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ELONUSDT · HTTP 400 · 17/10/2026 05:22 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ELON-USD · HTTP 404 · 17/10/2026 05:22 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.942 vs $2.972 → 0,99%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000003068 vs $0,000003064 → 0,13%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump_2026-10-17_045117.json',encoding='utf-8'));d=d.get('HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump',d);p=mock.patch('time.time',return_value=1792212677);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HwwKrDPq9pkcJcBPar7qmc5UGcPXj2QYixjkvztppump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 17/10/2026 05:22 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `924070dca3835564…`
