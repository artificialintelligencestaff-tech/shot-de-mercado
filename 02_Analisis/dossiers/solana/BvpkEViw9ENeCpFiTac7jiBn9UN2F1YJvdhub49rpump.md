# SpaceXTesla (X) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00003268 · liquidez $14.550 · mcap $32.620 (al detectar)  
Detectado el 20/10/2026 21:47 UTC por: young-0.4 · edad 10.0 min · pesos info 60 / estructura 20 / precio 20 · info 32.4 · estructura 12.6 · precio/volumen 4.7 · cobertura 93/100, [info] narrative_wave: ola 'spacextesla': 8 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 50, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 22/10/2026 21:47 UTC (< 48 h) · vigente: quedan 46,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir X

Estudio de cómo se adquiere X, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 20/10/2026 23:23 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 20/10/2026 21:47 UTC | pumpswap `GSXL4YV…jQHp` | $14.550 | 10% | 1,375% | 13,746% | 137,460% | $73 | $218 |
| consulta 20/10/2026 23:23 UTC | pumpswap `GSXL4YV…jQHp` | $7.000 | 10% | 2,857% | 28,573% | 285,734% | $35 | $105 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump`
5. Configurar el slippage: 10% (liquidez $7.000, consulta 20/10/2026 23:23 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump) y el par en DexScreener (https://dexscreener.com/solana/GSXL4YVdhSQY8Mbkuhqmu2UZZ6hu2znwo6ErHnJKjQHp); mint authority / freeze authority: revocada / revocada · holders 1.265 · top-10 66,56% (consulta 20/10/2026 23:23 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump
- Par en DexScreener: https://dexscreener.com/solana/GSXL4YVdhSQY8Mbkuhqmu2UZZ6hu2znwo6ErHnJKjQHp
- Página del lanzamiento (pump.fun): https://pump.fun/coin/BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.265 · top-10 66,56% (consulta 20/10/2026 23:23 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | SpaceXTesla / X | registro de la detección (pumpportal_live) |
| Mint / contrato | `BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `GSXL4YVdhSQY8Mbkuhqmu2UZZ6hu2znwo6ErHnJKjQHp` | DexScreener, al detectar (4 par(es) en la consulta 20/10/2026 23:23 UTC) |
| Deployer | `29yFzeBZgxf5zqrAkKXwgZtQehRf4pL8WbV2nRJikbw8` | PumpPortal (evento create), al detectar |
| Par creado | 20/10/2026 21:37 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 9,9 min / 9,9 min / 105,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 20/10/2026 23:23 UTC |
| Holders / top-10 | 1.265 / 66,56% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 20/10/2026 23:23 UTC |
| Holders efectivos del top-10 | 2,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 20/10/2026 23:23 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 20/10/2026 23:23 UTC |
| Links | DexScreener: https://dexscreener.com/solana/GSXL4YVdhSQY8Mbkuhqmu2UZZ6hu2znwo6ErHnJKjQHp · Solscan: https://solscan.io/token/BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump · pump.fun: https://pump.fun/coin/BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump · web: https://otcdesks.cash/coin/BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump · twitter: https://twitter.com/wholemars/status/2112657492035727463 | consulta 20/10/2026 23:23 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 20/10/2026 23:23 UTC)
- **Historia:**
  - Par creado el 20/10/2026 21:37 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 20/10/2026 21:47 UTC, con el par a 9,9 min de creado: precio $0,00003268, mcap $32.620, liquidez $14.550.
  - Velas de 1 h de GeckoTerminal (3, desde 20/10/2026 21:00 UTC): apertura $0,00004383 · máximo $0,00008374 (20/10/2026 21:00 UTC) · mínimo $0,000008266 (20/10/2026 21:00 UTC) · último cierre $0,00001020.
  - En la consulta 20/10/2026 23:23 UTC: precio $0,00001021, liquidez $7.000, FDV $9.873.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 20/10/2026 21:47 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00003268 |
| Liquidez | $14.550 |
| MCap | $32.620 |
| Volumen 24 h | $177.212 |
| Cambio 24 h | -25% |
| Cambio m5 / h1 | -33,1% / -24,8% |
| Volumen m5 / h1 | $31.934 / $177.212 |
| Trades m5 (compras / ventas) | 476 / 476 |
| Edad del par | 9,9 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 50; motivos sin regla: young-0.4 · edad 10.0 min · pesos info 60 / estructura 20 / precio 20 · info 32.4 · estructura 12.6 · precio/volumen 4.7 · cobertura 93/100, [info] narrative_wave: ola 'spacextesla': 8 lanzamientos más en 1 h → +15.0, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [info] mentions: menciones 1 h 3 (1 familias) · 26 h 3 → +9.0, [estructura] bonding_progress: graduado (pumpswap) → +9.6, [estructura] holders_struct: holders 1282 · top-10 47.5 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1282/3739 = 0.34 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×2.2 la tasa horaria (s 0.27), [precio/volumen] holder_accumulation: holders 781→1282 (+83.5/min) · top10 36.0%→47.5% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=14549.74, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 50 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-20T21:47:32+00:00, sin estado previo): **15** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 69 de 42.527 tokens analizados (0,16%) quedan ≥ 56. Con score 15, este activo queda en el percentil 97,3 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 20/10/2026 21:47 UTC, hasta 22/10/2026 21:47 UTC · vigente: quedan 46,4 h.
- **Aceleración al detectar:** cambio m5 -33,1% · h1 -24,8% · h24 -25% · volumen m5/h1 0,18 · edad del par 9,9 min.
- **Precio de entrada** (alerta): $0,00003268.
- **Consulta 20/10/2026 23:23 UTC:** $0,00001021 (-68,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump_2026-10-20_214732.json` · blob `2bd7d8731dd6f2c09935fb2f2454585f7ab65dd5` · commit `0466a20` (2026-10-20T23:16:37Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-20_214732`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump · registro · 20/10/2026 21:47 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump · HTTP 200 · 20/10/2026 23:23 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump/report · HTTP 200 · 20/10/2026 23:23 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump · HTTP 200 · 20/10/2026 23:23 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/GSXL4YVdhSQY8Mbkuhqmu2UZZ6hu2znwo6ErHnJKjQHp/ohlcv/hour?limit=1000 · HTTP 200 · 20/10/2026 23:23 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump · HTTP 404 · 20/10/2026 23:23 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=XUSDT · HTTP 400 · 20/10/2026 23:23 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/X-USD · HTTP 404 · 20/10/2026 23:23 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $7.000 vs $6.656 → 4,91%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00001021 vs $0,00001020 → 0,09%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump_2026-10-20_214732.json',encoding='utf-8'));d=d.get('BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump',d);p=mock.patch('time.time',return_value=1792532852);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint BvpkEViw9ENeCpFiTac7jiBn9UN2F1YJvdhub49rpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 20/10/2026 23:23 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `eb1ffeabc140d391…`
