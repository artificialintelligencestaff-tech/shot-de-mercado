# La Tortue Sagace (Tortue) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00004669 · liquidez $17.647 · mcap $46.697 (al detectar)  
Detectado el 18/10/2026 11:16 UTC por: young-0.4 · edad 10.8 min · pesos info 60 / estructura 20 / precio 20 · info 19.4 · estructura 14.5 · precio/volumen 7.6 · cobertura 93/100, [info] narrative_wave: ola 'tortue': 6 lanzamientos más en 1 h → +11.2, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 42, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 20/10/2026 11:16 UTC (< 48 h) · vigente: quedan 46,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Tortue

Estudio de cómo se adquiere Tortue, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 18/10/2026 12:19 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 18/10/2026 11:16 UTC | pumpswap `8mJM5Ze…MSkQ` | $17.647 | 10% | 1,133% | 11,333% | 113,333% | $88 | $265 |
| consulta 18/10/2026 12:19 UTC | pumpswap `8mJM5Ze…MSkQ` | $37.053 | 10% | 0,540% | 5,398% | 53,976% | $185 | $556 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump`
5. Configurar el slippage: 10% (liquidez $37.053, consulta 18/10/2026 12:19 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump) y el par en DexScreener (https://dexscreener.com/solana/8mJM5ZetfmjWVwM6kZSJrEozrV5NreV89oyELc6jMSkQ); mint authority / freeze authority: revocada / revocada · holders 3.254 · top-10 30,13% (consulta 18/10/2026 12:19 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump
- Par en DexScreener: https://dexscreener.com/solana/8mJM5ZetfmjWVwM6kZSJrEozrV5NreV89oyELc6jMSkQ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.254 · top-10 30,13% (consulta 18/10/2026 12:19 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | La Tortue Sagace / Tortue | registro de la detección (pumpportal_live) |
| Mint / contrato | `7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `8mJM5ZetfmjWVwM6kZSJrEozrV5NreV89oyELc6jMSkQ` | DexScreener, al detectar (5 par(es) en la consulta 18/10/2026 12:19 UTC) |
| Deployer | `FwUB3rBAUcG9gx8dYXsqwHTsAYzqB6TzBfR4htp67DgT` | PumpPortal (evento create), al detectar |
| Par creado | 18/10/2026 11:05 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,8 min / 10,8 min / 74,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 18/10/2026 12:19 UTC |
| Holders / top-10 | 3.254 / 30,13% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 18/10/2026 12:19 UTC |
| Holders efectivos del top-10 | 5,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 18/10/2026 12:19 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 18/10/2026 12:19 UTC |
| Links | DexScreener: https://dexscreener.com/solana/8mJM5ZetfmjWVwM6kZSJrEozrV5NreV89oyELc6jMSkQ · Solscan: https://solscan.io/token/7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump · pump.fun: https://pump.fun/coin/7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump · web: https://www.20minutes.fr/politique/4221744-20260504-presidentielle-2027-remontada-unite-pourquoi-jean-luc-melenchon-animal-totem-tortue · twitter: https://x.com/th3onlyoneleft/status/2111786952500363280 | consulta 18/10/2026 12:19 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 18/10/2026 12:19 UTC)
- **Historia:**
  - Par creado el 18/10/2026 11:05 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 18/10/2026 11:16 UTC, con el par a 10,8 min de creado: precio $0,00004669, mcap $46.697, liquidez $17.647.
  - Velas de 1 h de GeckoTerminal (2, desde 18/10/2026 11:00 UTC): apertura $0,00004149 · máximo $0,0002377 (18/10/2026 11:00 UTC) · mínimo $0,00002956 (18/10/2026 11:00 UTC) · último cierre $0,0001766.
  - En la consulta 18/10/2026 12:19 UTC: precio $0,0001839, liquidez $37.053, FDV $178.875.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 18/10/2026 11:16 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00004669 |
| Liquidez | $17.647 |
| MCap | $46.697 |
| Volumen 24 h | $189.279 |
| Cambio 24 h | +10% |
| Cambio m5 / h1 | -30,5% / +10,5% |
| Volumen m5 / h1 | $53.698 / $189.279 |
| Trades m5 (compras / ventas) | 787 / 602 |
| Edad del par | 10,8 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 42; motivos sin regla: young-0.4 · edad 10.8 min · pesos info 60 / estructura 20 / precio 20 · info 19.4 · estructura 14.5 · precio/volumen 7.6 · cobertura 93/100, [info] narrative_wave: ola 'tortue': 6 lanzamientos más en 1 h → +11.2, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1262 · top-10 38.9 % → +2.4, [estructura] dev_wallet: creador compró 3.5 % del supply → +2.0, [estructura] holder_to_txn_ratio: holders/txns 1262/4852 = 0.26 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×3.4 la tasa horaria (s 0.76), [precio/volumen] buy_pressure_shift: compras 57% en 5 min vs 54% en 1 h (s 0.12), [precio/volumen] holder_accumulation: holders 743→1262 (+86.5/min) · top10 38.3%→38.9% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=17647.16, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 42 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-18T11:16:11+00:00, sin estado previo): **15** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 65 de 39.523 tokens analizados (0,16%) quedan ≥ 56. Con score 15, este activo queda en el percentil 97,2 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 18/10/2026 11:16 UTC, hasta 20/10/2026 11:16 UTC · vigente: quedan 46,9 h.
- **Aceleración al detectar:** cambio m5 -30,5% · h1 +10,5% · h24 +10% · volumen m5/h1 0,28 · edad del par 10,8 min.
- **Precio de entrada** (alerta): $0,00004669.
- **Consulta 18/10/2026 12:19 UTC:** $0,0001839 (+293,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump_2026-10-18_111611.json` · blob `0e2f5f24b7bc841d1e2e8220e0cf0e3c65690462` · commit `e2ace01` (2026-10-18T12:08:57Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-18_111611`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump · registro · 18/10/2026 11:16 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump · HTTP 200 · 18/10/2026 12:19 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump/report · HTTP 200 · 18/10/2026 12:19 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump · HTTP 200 · 18/10/2026 12:19 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/8mJM5ZetfmjWVwM6kZSJrEozrV5NreV89oyELc6jMSkQ/ohlcv/hour?limit=1000 · HTTP 200 · 18/10/2026 12:19 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump · HTTP 404 · 18/10/2026 12:19 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=TORTUEUSDT · HTTP 400 · 18/10/2026 12:19 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/TORTUE-USD · HTTP 404 · 18/10/2026 12:19 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $37.053 vs $40.297 → 8,05%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001839 vs $0,0001766 → 3,95%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump_2026-10-18_111611.json',encoding='utf-8'));d=d.get('7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump',d);p=mock.patch('time.time',return_value=1792322171);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 7kASdbzxWLdioHhzYvXwtM3tRztAbFmeLKF4bDW8pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 18/10/2026 12:19 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `f80ed21364804c88…`
