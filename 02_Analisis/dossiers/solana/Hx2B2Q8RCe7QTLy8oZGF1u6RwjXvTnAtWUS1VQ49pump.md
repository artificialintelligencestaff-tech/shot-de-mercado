# Anime Cat (ACAT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000007651 · liquidez $6.246 · mcap $7.514 (al detectar)  
Detectado el 12/10/2026 18:12 UTC por: MCap bajo, Volumen alto, Buy pressure >60% (score 65, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 14/10/2026 18:12 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ACAT

Estudio de cómo se adquiere ACAT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 12/10/2026 18:45 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 12/10/2026 18:12 UTC | pumpswap `812WJtn…gQUh` | $6.246 | 10% | 3,202% | 32,020% | 320,200% | $31 | $94 |
| consulta 12/10/2026 18:45 UTC | pumpswap `812WJtn…gQUh` | $6.194 | 10% | 3,229% | 32,291% | 322,911% | $31 | $93 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump`
5. Configurar el slippage: 10% (liquidez $6.194, consulta 12/10/2026 18:45 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump) y el par en DexScreener (https://dexscreener.com/solana/812WJtnNW9r8LhgFNA98wvWGwVBMpCfjUjYabWkEgQUh); mint authority / freeze authority: revocada / revocada · holders 2.957 · top-10 98,94% (consulta 12/10/2026 18:45 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump
- Par en DexScreener: https://dexscreener.com/solana/812WJtnNW9r8LhgFNA98wvWGwVBMpCfjUjYabWkEgQUh
- Página del lanzamiento (pump.fun): https://pump.fun/coin/Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.957 · top-10 98,94% (consulta 12/10/2026 18:45 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Anime Cat / ACAT | registro de la detección (pumpportal) |
| Mint / contrato | `Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `812WJtnNW9r8LhgFNA98wvWGwVBMpCfjUjYabWkEgQUh` | DexScreener, al detectar (4 par(es) en la consulta 12/10/2026 18:45 UTC) |
| Deployer | `7kGAXsa7n1qN2FuNoJAGmzebmN9KqqLAHcwj7gvoekKk` | PumpPortal (evento create), al detectar |
| Par creado | 12/10/2026 15:39 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 2,6 h / 2,6 h / 3,1 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 12/10/2026 18:45 UTC |
| Holders / top-10 | 2.957 / 98,94% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 12/10/2026 18:45 UTC |
| Holders efectivos del top-10 | 2,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 12/10/2026 18:45 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 12/10/2026 18:45 UTC |
| Links | DexScreener: https://dexscreener.com/solana/812WJtnNW9r8LhgFNA98wvWGwVBMpCfjUjYabWkEgQUh · Solscan: https://solscan.io/token/Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump · pump.fun: https://pump.fun/coin/Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump · web: https://otcdesks.cash/coin/Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump · twitter: https://x.com/chillfindooor/status/2109670252611096962 | consulta 12/10/2026 18:45 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 12/10/2026 18:45 UTC)
- **Historia:**
  - Par creado el 12/10/2026 15:39 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 12/10/2026 18:12 UTC, con el par a 2,6 h de creado: precio $0,000007651, mcap $7.514, liquidez $6.246.
  - Velas de 1 h de GeckoTerminal (4, desde 12/10/2026 15:00 UTC): apertura $0,00004506 · máximo $0,0001473 (12/10/2026 15:00 UTC) · mínimo $0,000004496 (12/10/2026 17:00 UTC) · último cierre $0,000007637.
  - En la consulta 12/10/2026 18:45 UTC: precio $0,000007557, liquidez $6.194, FDV $7.423.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 12/10/2026 18:12 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000007651 |
| Liquidez | $6.246 |
| MCap | $7.514 |
| Volumen 24 h | $422.812 |
| Cambio 24 h | -83% |
| Cambio m5 / h1 | +2,2% / +27,3% |
| Volumen m5 / h1 | $21 / $1.336 |
| Trades m5 (compras / ventas) | 1 / 0 |
| Edad del par | 2,6 h |
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

Desglose no reproducible desde los motivos registrados (suma 63 vs score 65; motivos sin regla: Anticipación (lib_early_signals early-0.2): +2 — liquidity_inflow: liquidez +1% en 9 min → +0.08; holder_accumulation: holders 395→3184 (+33.0/min) · top10 60.8%→102.1% → +2): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-12T18:12:57+00:00, sin estado previo): **63** · motivos: MCap bajo, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 50 de 31.716 tokens analizados (0,16%) quedan ≥ 56. Con score 63, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 12/10/2026 18:12 UTC, hasta 14/10/2026 18:12 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +2,2% · h1 +27,3% · h24 -83% · volumen m5/h1 0,02 · edad del par 2,6 h.
- **Precio de entrada** (alerta): $0,000007651.
- **Consulta 12/10/2026 18:45 UTC:** $0,000007557 (-1,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump_2026-10-12_181257.json` · blob `e3df5b5299fb6f5d0ce53abe8769ea552d38f0aa` · commit `5da21a4` (2026-10-12T18:38:27Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-12_181257`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump · registro · 12/10/2026 18:12 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump · HTTP 200 · 12/10/2026 18:45 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump/report · HTTP 200 · 12/10/2026 18:45 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump · HTTP 200 · 12/10/2026 18:45 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/812WJtnNW9r8LhgFNA98wvWGwVBMpCfjUjYabWkEgQUh/ohlcv/hour?limit=1000 · HTTP 200 · 12/10/2026 18:45 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump · HTTP 404 · 12/10/2026 18:45 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ACATUSDT · HTTP 400 · 12/10/2026 18:45 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ACAT-USD · HTTP 404 · 12/10/2026 18:45 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $6.194 vs $6.201 → 0,12%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000007557 vs $0,000007637 → 1,05%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump_2026-10-12_181257.json',encoding='utf-8'));d=d.get('Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump',d);p=mock.patch('time.time',return_value=1791828777);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint Hx2B2Q8RCe7QTLy8oZGF1u6RwjXvTnAtWUS1VQ49pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 12/10/2026 18:45 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `c445f3011933e258…`
