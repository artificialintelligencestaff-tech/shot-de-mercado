# EVERNORTHXRP (XRPN) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1811 · liquidez $1.240.616 · mcap $181.186.412 (al detectar)  
Detectado el 06/10/2026 16:10 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 08/10/2026 16:10 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir XRPN

Estudio de cómo se adquiere XRPN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 16:41 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 16:10 UTC | pumpswap `GdVeeP6…dqh6` | $1.240.616 | 1% | 0,016% | 0,161% | 1,612% | $6.203 | $18.609 |
| consulta 06/10/2026 16:41 UTC | pumpswap `GdVeeP6…dqh6` | $1.242.444 | 1% | 0,016% | 0,161% | 1,610% | $6.212 | $18.637 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump`
5. Configurar el slippage: 1% (liquidez $1.242.444, consulta 06/10/2026 16:41 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump) y el par en DexScreener (https://dexscreener.com/solana/GdVeeP6jJWK1rCLUZbpd9AQyjgf9EHJENoPaccL6dqh6); mint authority / freeze authority: revocada / revocada · holders 2.155 · top-10 1,17% (consulta 06/10/2026 16:41 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump
- Par en DexScreener: https://dexscreener.com/solana/GdVeeP6jJWK1rCLUZbpd9AQyjgf9EHJENoPaccL6dqh6
- Página del lanzamiento (pump.fun): https://pump.fun/coin/mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.155 · top-10 1,17% (consulta 06/10/2026 16:41 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | EVERNORTHXRP / XRPN | registro de la detección (trending) |
| Mint / contrato | `mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `GdVeeP6jJWK1rCLUZbpd9AQyjgf9EHJENoPaccL6dqh6` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 16:41 UTC) |
| Deployer | `KFASPgCyzs2dGtFP2rzu2AY8XWHmCAix1bKX89E1EbV` | RugCheck `creator` |
| Par creado | 06/10/2026 15:09 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 61,1 min / 61,1 min / 91,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 16:41 UTC |
| Holders / top-10 | 2.155 / 1,17% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 16:41 UTC |
| Holders efectivos del top-10 | 4,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 16:41 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 16:41 UTC |
| Links | DexScreener: https://dexscreener.com/solana/GdVeeP6jJWK1rCLUZbpd9AQyjgf9EHJENoPaccL6dqh6 · Solscan: https://solscan.io/token/mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump · pump.fun: https://pump.fun/coin/mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump · web / Telegram / X: no publicados en DexScreener | consulta 06/10/2026 16:41 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 16:41 UTC)
- **Historia:**
  - Par creado el 06/10/2026 15:09 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 16:10 UTC, con el par a 61,1 min de creado: precio $0,1811, mcap $181.186.412, liquidez $1.240.616.
  - Velas de 1 h de GeckoTerminal (2, desde 06/10/2026 15:00 UTC): apertura $0,1758 · máximo $0,1824 (06/10/2026 16:00 UTC) · mínimo $0,00005052 (06/10/2026 15:00 UTC) · último cierre $0,1824.
  - En la consulta 06/10/2026 16:41 UTC: precio $0,1825, liquidez $1.242.444, FDV $182.528.893.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 16:10 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1811 |
| Liquidez | $1.240.616 |
| MCap | $181.186.412 |
| Volumen 24 h | $615.658 |
| Cambio 24 h | +358.042% |
| Cambio m5 / h1 | +0,3% / +2,7% |
| Volumen m5 / h1 | $886 / $11.863 |
| Trades m5 (compras / ventas) | 139 / 4 |
| Edad del par | 61,1 min |
| Score del feed (WS) | 100 |

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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 100 × 0,3 | +30 |
| MCap | ≥ $1M | $181.186.412 | +25 |
| Volumen 24 h | ≥ $100K | $615.658 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 97% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,3% · h1 +2,7% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 61,1 min | +8 |
| Volumen m5 | > $500 (par maduro) | $886 | +5 |
| Liquidez | ≥ $100K | $1.240.616 | +15 |
| Cambio 24 h | ≥ +50% | +358.042% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +358.042% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T16:10:37+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 21 de 15.947 tokens analizados (0,13%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 16:10 UTC, hasta 08/10/2026 16:10 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +0,3% · h1 +2,7% · h24 +358.042% · volumen m5/h1 0,07 · edad del par 61,1 min.
- **Precio de entrada** (alerta): $0,1811.
- **Consulta 06/10/2026 16:41 UTC:** $0,1825 (+0,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump_2026-10-06_161037.json` · blob `295f6a77fbc57a745ac135b4d2a676236ef6c894` · commit `9a0135d` (2026-10-06T16:34:08Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_161037`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump · registro · 06/10/2026 16:10 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump · HTTP 200 · 06/10/2026 16:41 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump/report · HTTP 200 · 06/10/2026 16:41 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump · HTTP 200 · 06/10/2026 16:41 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/GdVeeP6jJWK1rCLUZbpd9AQyjgf9EHJENoPaccL6dqh6/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 16:41 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump · HTTP 404 · 06/10/2026 16:41 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=XRPNUSDT · HTTP 400 · 06/10/2026 16:41 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/XRPN-USD · HTTP 404 · 06/10/2026 16:41 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.242.444 vs $1.242.586 → 0,01%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1825 vs $0,1824 → 0,05%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump_2026-10-06_161037.json',encoding='utf-8'));d=d.get('mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump',d);p=mock.patch('time.time',return_value=1791303037);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint mHinvysGkV4YPfj1PYxHGgyc4S7LCDwVki4r1Phpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 16:41 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `061ac5d85fd130c7…`
