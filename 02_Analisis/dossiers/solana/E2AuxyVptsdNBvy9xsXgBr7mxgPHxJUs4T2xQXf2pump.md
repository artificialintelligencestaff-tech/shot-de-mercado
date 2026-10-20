# Justice for Noppy (Noppy) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00004195 · liquidez $17.114 · mcap $41.954 (al detectar)  
Detectado el 20/10/2026 22:52 UTC por: young-0.4 · edad 11.3 min · pesos info 59 / estructura 20 / precio 20 · info 24.2 · estructura 12.7 · precio/volumen 9.2 · cobertura 93/100, [info] narrative_wave: ola 'justice': 7 lanzamientos más en 1 h → +13.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 46, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 22/10/2026 22:52 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Noppy

Estudio de cómo se adquiere Noppy, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 20/10/2026 23:23 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 20/10/2026 22:52 UTC | pumpswap `5QHcTT5…YGeL` | $17.114 | 10% | 1,169% | 11,686% | 116,864% | $86 | $257 |
| consulta 20/10/2026 23:23 UTC | pumpswap `5QHcTT5…YGeL` | $3.858 | 10% | 5,184% | 51,838% | 518,385% | $19 | $58 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump`
5. Configurar el slippage: 10% (liquidez $3.858, consulta 20/10/2026 23:23 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump) y el par en DexScreener (https://dexscreener.com/solana/5QHcTT5t9BzcNNYhFP69Lrh1TekTL8EQb6ecCLzTYGeL); mint authority / freeze authority: revocada / revocada · holders 1.616 · top-10 84,94% (consulta 20/10/2026 23:23 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump
- Par en DexScreener: https://dexscreener.com/solana/5QHcTT5t9BzcNNYhFP69Lrh1TekTL8EQb6ecCLzTYGeL
- Página del lanzamiento (pump.fun): https://pump.fun/coin/E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.616 · top-10 84,94% (consulta 20/10/2026 23:23 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Justice for Noppy / Noppy | registro de la detección (pumpportal_live) |
| Mint / contrato | `E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `5QHcTT5t9BzcNNYhFP69Lrh1TekTL8EQb6ecCLzTYGeL` | DexScreener, al detectar (3 par(es) en la consulta 20/10/2026 23:23 UTC) |
| Deployer | `75GMVrr2xfgAeybuNg1VMHqFE3GTFJLzEHo6xC4MwUzF` | PumpPortal (evento create), al detectar |
| Par creado | 20/10/2026 22:41 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,3 min / 11,3 min / 42,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 20/10/2026 23:23 UTC |
| Holders / top-10 | 1.616 / 84,94% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 20/10/2026 23:23 UTC |
| Holders efectivos del top-10 | 1,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 20/10/2026 23:23 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 20/10/2026 23:23 UTC |
| Links | DexScreener: https://dexscreener.com/solana/5QHcTT5t9BzcNNYhFP69Lrh1TekTL8EQb6ecCLzTYGeL · Solscan: https://solscan.io/token/E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump · pump.fun: https://pump.fun/coin/E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump · twitter: https://x.com/Na1_N1ako/status/2112674135356641581 · facebook: https://www.facebook.com/ProtectTheWild.UK/posts/pfbid02CLeJo8MBreWWyWkYL57W2Dd196whourmELaEJuUovja9pWSqQseU8qVq9WvcjXvAl?comment_id=1782219663039009&__cft__[0]=AZjK2pI_LXyKs7iSMS6ibTIvP5bIZYt3CXc-M9jBuWzpd_JrvrrHGweNREXe7apENDTjDmTLWtcBZVImJAtAi0Cn8p0EIx2egfKcxXMlEaSzQYcySER2AV4vE2ibf0EubLgz8D3VHM_1SxH9nbmXiIDNQ1xBzr9A&__tn__=R]-R | consulta 20/10/2026 23:23 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 20/10/2026 23:23 UTC)
- **Historia:**
  - Par creado el 20/10/2026 22:41 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 20/10/2026 22:52 UTC, con el par a 11,3 min de creado: precio $0,00004195, mcap $41.954, liquidez $17.114.
  - Velas de 1 h de GeckoTerminal (2, desde 20/10/2026 22:00 UTC): apertura $0,00004865 · máximo $0,00008176 (20/10/2026 22:00 UTC) · mínimo $0,000004239 (20/10/2026 23:00 UTC) · último cierre $0,000004294.
  - En la consulta 20/10/2026 23:23 UTC: precio $0,000004240, liquidez $3.858, FDV $4.054.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 20/10/2026 22:52 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00004195 |
| Liquidez | $17.114 |
| MCap | $41.954 |
| Volumen 24 h | $209.204 |
| Cambio 24 h | -5% |
| Cambio m5 / h1 | -31,2% / -4,7% |
| Volumen m5 / h1 | $49.977 / $209.204 |
| Trades m5 (compras / ventas) | 773 / 603 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 46; motivos sin regla: young-0.4 · edad 11.3 min · pesos info 59 / estructura 20 / precio 20 · info 24.2 · estructura 12.7 · precio/volumen 9.2 · cobertura 93/100, [info] narrative_wave: ola 'justice': 7 lanzamientos más en 1 h → +13.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 1419 · top-10 41.8 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1419/5105 = 0.28 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×2.9 la tasa horaria (s 0.55), [precio/volumen] buy_pressure_shift: compras 56% en 5 min vs 55% en 1 h (s 0.07), [precio/volumen] liquidity_inflow: liquidez +25% en 8 min (s 0.83), [precio/volumen] holder_accumulation: holders 878→1419 (+90.2/min) · top10 40.9%→41.8% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=17113.93, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 46 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-20T22:52:25+00:00, sin estado previo): **15** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 69 de 42.527 tokens analizados (0,16%) quedan ≥ 56. Con score 15, este activo queda en el percentil 97,3 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 20/10/2026 22:52 UTC, hasta 22/10/2026 22:52 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -31,2% · h1 -4,7% · h24 -5% · volumen m5/h1 0,24 · edad del par 11,3 min.
- **Precio de entrada** (alerta): $0,00004195.
- **Consulta 20/10/2026 23:23 UTC:** $0,000004240 (-89,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump_2026-10-20_225225.json` · blob `b3d0b3f1bbe71edb58b3564eb3fa2489fa7bf79a` · commit `0466a20` (2026-10-20T23:16:37Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-20_225225`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump · registro · 20/10/2026 22:52 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump · HTTP 200 · 20/10/2026 23:23 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump/report · HTTP 200 · 20/10/2026 23:23 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump · HTTP 200 · 20/10/2026 23:23 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/5QHcTT5t9BzcNNYhFP69Lrh1TekTL8EQb6ecCLzTYGeL/ohlcv/hour?limit=1000 · HTTP 200 · 20/10/2026 23:23 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump · HTTP 404 · 20/10/2026 23:23 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=NOPPYUSDT · HTTP 400 · 20/10/2026 23:23 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/NOPPY-USD · HTTP 404 · 20/10/2026 23:23 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.858 vs $3.949 → 2,30%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000004240 vs $0,000004294 → 1,25%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump_2026-10-20_225225.json',encoding='utf-8'));d=d.get('E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump',d);p=mock.patch('time.time',return_value=1792536745);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint E2AuxyVptsdNBvy9xsXgBr7mxgPHxJUs4T2xQXf2pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 20/10/2026 23:23 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `6417074f834db6c7…`
