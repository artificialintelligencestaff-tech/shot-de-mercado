# The SI Bubble (BUBBLE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00003666 · liquidez $15.460 · mcap $36.668 (al detectar)  
Detectado el 07/10/2026 06:34 UTC por: young-0.4 · edad 11.4 min · pesos info 59 / estructura 20 / precio 20 · info 23.1 · estructura 12.7 · precio/volumen 4.7 · cobertura 93/100, [info] narrative_wave: ola 'bubble': 17 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 09/10/2026 06:34 UTC (< 48 h) · vigente: quedan 47,2 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir BUBBLE

Estudio de cómo se adquiere BUBBLE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/10/2026 07:20 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/10/2026 06:34 UTC | pumpswap `71o75kx…yo3A` | $15.460 | 10% | 1,294% | 12,937% | 129,368% | $77 | $232 |
| consulta 07/10/2026 07:20 UTC | pumpswap `71o75kx…yo3A` | $3.831 | 10% | 5,220% | 52,203% | 522,031% | $19 | $57 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM`
5. Configurar el slippage: 10% (liquidez $3.831, consulta 07/10/2026 07:20 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM) y el par en DexScreener (https://dexscreener.com/solana/71o75kxUJGskgnCKG8abppHRvfXbcVzhfWeyGySKyo3A); mint authority / freeze authority: revocada / revocada · holders 865 · top-10 94,00% (consulta 07/10/2026 07:20 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM
- Par en DexScreener: https://dexscreener.com/solana/71o75kxUJGskgnCKG8abppHRvfXbcVzhfWeyGySKyo3A
- Página del lanzamiento (pump.fun): https://pump.fun/coin/6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 865 · top-10 94,00% (consulta 07/10/2026 07:20 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | The SI Bubble / BUBBLE | registro de la detección (pumpportal_live) |
| Mint / contrato | `6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `71o75kxUJGskgnCKG8abppHRvfXbcVzhfWeyGySKyo3A` | DexScreener, al detectar (2 par(es) en la consulta 07/10/2026 07:20 UTC) |
| Deployer | `GZ4yE28kFtDjqcogGPqWGeLtefKfWJy1Mgmj2HtkLiix` | PumpPortal (evento create), al detectar |
| Par creado | 07/10/2026 06:23 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,4 min / 11,4 min / 57,2 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/10/2026 07:20 UTC |
| Holders / top-10 | 865 / 94,00% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/10/2026 07:20 UTC |
| Holders efectivos del top-10 | 1,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/10/2026 07:20 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 07/10/2026 07:20 UTC |
| Links | DexScreener: https://dexscreener.com/solana/71o75kxUJGskgnCKG8abppHRvfXbcVzhfWeyGySKyo3A · Solscan: https://solscan.io/token/6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM · pump.fun: https://pump.fun/coin/6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM · web: https://otcdesks.cash/coin/6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM · twitter: https://x.com/BoltricksDev/status/2107717626025660711 | consulta 07/10/2026 07:20 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/10/2026 07:20 UTC)
- **Historia:**
  - Par creado el 07/10/2026 06:23 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/10/2026 06:34 UTC, con el par a 11,4 min de creado: precio $0,00003666, mcap $36.668, liquidez $15.460.
  - Velas de 1 h de GeckoTerminal (2, desde 07/10/2026 06:00 UTC): apertura $0,00005018 · máximo $0,00005396 (07/10/2026 06:00 UTC) · mínimo $0,000003953 (07/10/2026 07:00 UTC) · último cierre $0,000004162.
  - En la consulta 07/10/2026 07:20 UTC: precio $0,000004170, liquidez $3.831, FDV $3.855.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/10/2026 06:34 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00003666 |
| Liquidez | $15.460 |
| MCap | $36.668 |
| Volumen 24 h | $149.218 |
| Cambio 24 h | -26% |
| Cambio m5 / h1 | +83,8% / -25,8% |
| Volumen m5 / h1 | $26.970 / $149.218 |
| Trades m5 (compras / ventas) | 351 / 289 |
| Edad del par | 11,4 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 11.4 min · pesos info 59 / estructura 20 / precio 20 · info 23.1 · estructura 12.7 · precio/volumen 4.7 · cobertura 93/100, [info] narrative_wave: ola 'bubble': 17 lanzamientos más en 1 h → +14.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 866 · top-10 48.1 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 866/3305 = 0.26 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×2.2 la tasa horaria (s 0.27), [precio/volumen] holder_accumulation: holders 713→866 (+25.5/min) · top10 42.7%→48.1% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=15459.82, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-07T06:34:32+00:00, sin estado previo): **15** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 25 de 18.012 tokens analizados (0,14%) quedan ≥ 56. Con score 15, este activo queda en el percentil 97,3 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/10/2026 06:34 UTC, hasta 09/10/2026 06:34 UTC · vigente: quedan 47,2 h.
- **Aceleración al detectar:** cambio m5 +83,8% · h1 -25,8% · h24 -26% · volumen m5/h1 0,18 · edad del par 11,4 min.
- **Precio de entrada** (alerta): $0,00003666.
- **Consulta 07/10/2026 07:20 UTC:** $0,000004170 (-88,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM_2026-10-07_063432.json` · blob `40e29da12908a003b57ee96603019c1262b48b0a` · commit `cdcd775` (2026-10-07T07:13:47Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-07_063432`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM · registro · 07/10/2026 06:34 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM · HTTP 200 · 07/10/2026 07:20 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM/report · HTTP 200 · 07/10/2026 07:20 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM · HTTP 200 · 07/10/2026 07:20 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/71o75kxUJGskgnCKG8abppHRvfXbcVzhfWeyGySKyo3A/ohlcv/hour?limit=1000 · HTTP 200 · 07/10/2026 07:20 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM · HTTP 404 · 07/10/2026 07:20 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BUBBLEUSDT · HTTP 400 · 07/10/2026 07:20 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BUBBLE-USD · HTTP 404 · 07/10/2026 07:20 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.831 vs $3.825 → 0,15%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000004170 vs $0,000004162 → 0,19%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM_2026-10-07_063432.json',encoding='utf-8'));d=d.get('6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM',d);p=mock.patch('time.time',return_value=1791354872);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 6C6JTYtxzpgexek3fzkmsfTeRJaZgTGFHPLu69VDZoUM --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/10/2026 07:20 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `726f131d3fff0f48…`
