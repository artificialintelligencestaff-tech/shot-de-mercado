# NASBOT (Taku) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001302 · liquidez $30.879 · mcap $130.207 (al detectar)  
Detectado el 13/10/2026 20:15 UTC por: young-0.4 · edad 11.1 min · pesos info 59 / estructura 20 / precio 20 · info 23.1 · estructura 16.4 · precio/volumen 12.0 · cobertura 93/100, [info] narrative_wave: ola 'nasbot': 36 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 51, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 15/10/2026 20:15 UTC (< 48 h) · vigente: quedan 47,3 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Taku

Estudio de cómo se adquiere Taku, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 13/10/2026 20:56 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 13/10/2026 20:15 UTC | pumpswap `5LG65Rv…DpoR` | $30.879 | 10% | 0,648% | 6,477% | 64,768% | $154 | $463 |
| consulta 13/10/2026 20:56 UTC | pumpswap `5LG65Rv…DpoR` | $19.964 | 10% | 1,002% | 10,018% | 100,178% | $100 | $299 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump`
5. Configurar el slippage: 10% (liquidez $19.964, consulta 13/10/2026 20:56 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump) y el par en DexScreener (https://dexscreener.com/solana/5LG65RvWYQCGfG86KudJacDd919v3aNR1z4VSeMjDpoR); mint authority / freeze authority: revocada / revocada · holders 3.172 · top-10 40,74% (consulta 13/10/2026 20:56 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump
- Par en DexScreener: https://dexscreener.com/solana/5LG65RvWYQCGfG86KudJacDd919v3aNR1z4VSeMjDpoR
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.172 · top-10 40,74% (consulta 13/10/2026 20:56 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | NASBOT / Taku | registro de la detección (pumpportal_live) |
| Mint / contrato | `2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `5LG65RvWYQCGfG86KudJacDd919v3aNR1z4VSeMjDpoR` | DexScreener, al detectar (4 par(es) en la consulta 13/10/2026 20:56 UTC) |
| Deployer | `2UAXcrMfzbRgbsMNgh1N1jPC2fznbq1YAVqSCQHnMBZC` | PumpPortal (evento create), al detectar |
| Par creado | 13/10/2026 20:04 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,1 min / 11,1 min / 52,1 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 13/10/2026 20:56 UTC |
| Holders / top-10 | 3.172 / 40,74% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 13/10/2026 20:56 UTC |
| Holders efectivos del top-10 | 3,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 13/10/2026 20:56 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 13/10/2026 20:56 UTC |
| Links | DexScreener: https://dexscreener.com/solana/5LG65RvWYQCGfG86KudJacDd919v3aNR1z4VSeMjDpoR · Solscan: https://solscan.io/token/2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump · pump.fun: https://pump.fun/coin/2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump · web: https://otcdesks.cash/coin/2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump · twitter: https://x.com/Infinitidigits/status/2110100966271799672?s=20 | consulta 13/10/2026 20:56 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 13/10/2026 20:56 UTC)
- **Historia:**
  - Par creado el 13/10/2026 20:04 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 13/10/2026 20:15 UTC, con el par a 11,1 min de creado: precio $0,0001302, mcap $130.207, liquidez $30.879.
  - Velas de 1 h de GeckoTerminal (1, desde 13/10/2026 20:00 UTC): apertura $0,00004040 · máximo $0,0002263 (13/10/2026 20:00 UTC) · mínimo $0,000006412 (13/10/2026 20:00 UTC) · último cierre $0,00005839.
  - En la consulta 13/10/2026 20:56 UTC: precio $0,00005595, liquidez $19.964, FDV $52.886.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 13/10/2026 20:15 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001302 |
| Liquidez | $30.879 |
| MCap | $130.207 |
| Volumen 24 h | $190.531 |
| Cambio 24 h | +205% |
| Cambio m5 / h1 | -9,7% / +205,0% |
| Volumen m5 / h1 | $107.303 / $190.531 |
| Trades m5 (compras / ventas) | 961 / 706 |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 51; motivos sin regla: young-0.4 · edad 11.1 min · pesos info 59 / estructura 20 / precio 20 · info 23.1 · estructura 16.4 · precio/volumen 12.0 · cobertura 93/100, [info] narrative_wave: ola 'nasbot': 36 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1963 · top-10 26.4 % → +4.9, [estructura] dev_wallet: creador compró 6.7 % del supply → +1.0, [estructura] holder_to_txn_ratio: holders/txns 1963/3089 = 0.64 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×6.8 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 58% en 5 min vs 57% en 1 h (s 0.04), [precio/volumen] liquidity_inflow: liquidez +113% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 551→1963 (+235.3/min) · top10 45.8%→26.4% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=30879.28, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=11518.55, score 51 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-13T20:15:21+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 53 de 34.026 tokens analizados (0,16%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 13/10/2026 20:15 UTC, hasta 15/10/2026 20:15 UTC · vigente: quedan 47,3 h.
- **Aceleración al detectar:** cambio m5 -9,7% · h1 +205,0% · h24 +205% · volumen m5/h1 0,56 · edad del par 11,1 min.
- **Precio de entrada** (alerta): $0,0001302.
- **Consulta 13/10/2026 20:56 UTC:** $0,00005595 (-57,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump_2026-10-13_201521.json` · blob `acd40612e680ce688dbae8949af615afda6db941` · commit `2c0fcf3` (2026-10-13T20:49:12Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-13_200233.json` · blob `3d0df84eba2bf9ac8f18218c51e590b86c68989c` · commit `2c0fcf3` (2026-10-13T20:49:12Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-13_201521`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump · registro · 13/10/2026 20:15 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump · HTTP 200 · 13/10/2026 20:56 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump/report · HTTP 200 · 13/10/2026 20:56 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump · HTTP 200 · 13/10/2026 20:56 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/5LG65RvWYQCGfG86KudJacDd919v3aNR1z4VSeMjDpoR/ohlcv/hour?limit=1000 · HTTP 200 · 13/10/2026 20:56 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump · HTTP 404 · 13/10/2026 20:56 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=TAKUUSDT · HTTP 400 · 13/10/2026 20:56 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/TAKU-USD · HTTP 404 · 13/10/2026 20:56 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $19.964 vs $20.210 → 1,21%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00005595 vs $0,00005839 → 4,19%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump_2026-10-13_201521.json',encoding='utf-8'));d=d.get('2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump',d);p=mock.patch('time.time',return_value=1791922521);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2gruZnSufXhDrVfTLeb8jAJ8tnjv8BWvHYeyGQb3pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 13/10/2026 20:56 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `bed045c12bf2f935…`
