# UNITED DIVIDEND RESERVE (UDR) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,005731 · liquidez $220.844 · mcap $5.731.789 (al detectar)  
Detectado el 02/10/2026 04:58 UTC por: MCap > $1M, Volumen decente, Liquidez alta (score 60, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 04/10/2026 04:58 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir UDR

Estudio de cómo se adquiere UDR, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 05:11 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 04:58 UTC | pumpswap `BsmAQv4…56na` | $220.844 | 5% | 0,091% | 0,906% | 9,056% | $1.104 | $3.313 |
| consulta 02/10/2026 05:11 UTC | pumpswap `BsmAQv4…56na` | $222.602 | 5% | 0,090% | 0,898% | 8,985% | $1.113 | $3.339 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump`
5. Configurar el slippage: 5% (liquidez $222.602, consulta 02/10/2026 05:11 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump) y el par en DexScreener (https://dexscreener.com/solana/BsmAQv4zXcT11a3oTYxneAbV5bD8N2V3DuQCy3kD56na); mint authority / freeze authority: revocada / revocada · holders 2.951 · top-10 2,73% (consulta 02/10/2026 05:11 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump
- Par en DexScreener: https://dexscreener.com/solana/BsmAQv4zXcT11a3oTYxneAbV5bD8N2V3DuQCy3kD56na
- Página del lanzamiento (pump.fun): https://pump.fun/coin/EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.951 · top-10 2,73% (consulta 02/10/2026 05:11 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | UNITED DIVIDEND RESERVE / UDR | registro de la detección (pumpportal_live) |
| Mint / contrato | `EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BsmAQv4zXcT11a3oTYxneAbV5bD8N2V3DuQCy3kD56na` | DexScreener, al detectar (2 par(es) en la consulta 02/10/2026 05:11 UTC) |
| Deployer | `Dan1z3cto8kbuFV1QY2hNWdJFXTWUzNuY6WYNv5KUFDX` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 04:47 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,4 min / 11,4 min / 24,5 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 05:11 UTC |
| Holders / top-10 | 2.951 / 2,73% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 05:11 UTC |
| Holders efectivos del top-10 | 2,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 05:11 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 05:11 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BsmAQv4zXcT11a3oTYxneAbV5bD8N2V3DuQCy3kD56na · Solscan: https://solscan.io/token/EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump · pump.fun: https://pump.fun/coin/EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump · web / Telegram / X: no publicados en DexScreener | consulta 02/10/2026 05:11 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 05:11 UTC)
- **Historia:**
  - Par creado el 02/10/2026 04:47 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 04:58 UTC, con el par a 11,4 min de creado: precio $0,005731, mcap $5.731.789, liquidez $220.844.
  - Velas de 1 h de GeckoTerminal (2, desde 02/10/2026 04:00 UTC): apertura $0,00005087 · máximo $0,005826 (02/10/2026 05:00 UTC) · mínimo $0,00005087 (02/10/2026 04:00 UTC) · último cierre $0,005826.
  - En la consulta 02/10/2026 05:11 UTC: precio $0,005819, liquidez $222.602, FDV $5.819.711.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 04:58 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,005731 |
| Liquidez | $220.844 |
| MCap | $5.731.789 |
| Volumen 24 h | $99.480 |
| Cambio 24 h | +11.178% |
| Cambio m5 / h1 | -0,0% / +11.178,0% |
| Volumen m5 / h1 | $456 / $99.480 |
| Trades m5 (compras / ventas) | 10 / 6 |
| Edad del par | 11,4 min |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 0/1 (0,0%, IC90 0,0%–73,0%) · secundaria 0/0 resueltas (shadow_monitor.json).

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

Desglose reconstruido desde los motivos registrados; suma 60 = score registrado 60 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| Gate de edad v7.2.1 | edad < 60 min o desconocida: sin bonos temporales | edad 11,4 min | +0 |
| MCap | ≥ $1M | $5.731.789 | +25 |
| Volumen 24 h | ≥ $50K | $99.480 | +10 |
| Liquidez | ≥ $100K | $220.844 | +15 |
| Cambio 24 h | ≥ +50% | +11.178% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +11.178% · liq/mcap 3,9% | +0 |
| **Total** | recortado a 0–100 |  | **60** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T04:58:39+00:00, sin estado previo): **60** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen decente, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=3.9% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 6 de 6.940 tokens analizados (0,09%) quedan ≥ 56. Con score 60, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 04:58 UTC, hasta 04/10/2026 04:58 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -0,0% · h1 +11.178,0% · h24 +11.178% · volumen m5/h1 0,00 · edad del par 11,4 min.
- **Precio de entrada** (alerta): $0,005731.
- **Consulta 02/10/2026 05:11 UTC:** $0,005819 (+1,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump_2026-10-02_045839.json` · blob `c8aade409a091239313dc0322166aa85d3974380` · commit `a7c867f` (2026-10-02T05:04:18Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_045839`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump · registro · 02/10/2026 04:58 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump · HTTP 200 · 02/10/2026 05:11 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump/report · HTTP 200 · 02/10/2026 05:11 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump · HTTP 200 · 02/10/2026 05:11 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BsmAQv4zXcT11a3oTYxneAbV5bD8N2V3DuQCy3kD56na/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 05:11 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump · HTTP 404 · 02/10/2026 05:11 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=UDRUSDT · HTTP 400 · 02/10/2026 05:11 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/UDR-USD · HTTP 404 · 02/10/2026 05:11 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $222.602 vs $222.851 → 0,11%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,005819 vs $0,005826 → 0,12%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump_2026-10-02_045839.json',encoding='utf-8'));d=d.get('EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump',d);p=mock.patch('time.time',return_value=1790917119);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint EscbxDPmuRdGGvS1Ad579JewsRtZ7NCq9ED4YfAupump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 05:11 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `32798f06eafe4a50…`
