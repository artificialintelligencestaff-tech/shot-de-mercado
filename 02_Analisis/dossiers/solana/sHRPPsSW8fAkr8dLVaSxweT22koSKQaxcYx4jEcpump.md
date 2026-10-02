# World AI Fund (WAIF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,008077 · liquidez $257.628 · mcap $8.077.873 (al detectar)  
Detectado el 02/10/2026 00:11 UTC por: MCap > $1M, Volumen alto, Liquidez alta (score 65, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 04/10/2026 00:11 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir WAIF

Estudio de cómo se adquiere WAIF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 00:44 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 00:11 UTC | pumpswap `94qC4pC…SjVg` | $257.628 | 3% | 0,078% | 0,776% | 7,763% | $1.288 | $3.864 |
| consulta 02/10/2026 00:44 UTC | pumpswap `94qC4pC…SjVg` | $260.442 | 3% | 0,077% | 0,768% | 7,679% | $1.302 | $3.907 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump`
5. Configurar el slippage: 3% (liquidez $260.442, consulta 02/10/2026 00:44 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump) y el par en DexScreener (https://dexscreener.com/solana/94qC4pCs8NKQLvmmANC22EEJ9455N3kCrwxxQFn4SjVg); mint authority / freeze authority: revocada / revocada · holders 2.018 · top-10 4,34% (consulta 02/10/2026 00:44 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump
- Par en DexScreener: https://dexscreener.com/solana/94qC4pCs8NKQLvmmANC22EEJ9455N3kCrwxxQFn4SjVg
- Página del lanzamiento (pump.fun): https://pump.fun/coin/sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.018 · top-10 4,34% (consulta 02/10/2026 00:44 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | World AI Fund / WAIF | registro de la detección (pumpportal_live) |
| Mint / contrato | `sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `94qC4pCs8NKQLvmmANC22EEJ9455N3kCrwxxQFn4SjVg` | DexScreener, al detectar (2 par(es) en la consulta 02/10/2026 00:44 UTC) |
| Deployer | `EiJZq6HQXx3A9zpfhzykoX42BvurRe7R84tmZhYZtSqs` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 00:01 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,2 min / 10,2 min / 43,1 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 00:44 UTC |
| Holders / top-10 | 2.018 / 4,34% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 00:44 UTC |
| Holders efectivos del top-10 | 4,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 00:44 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 00:44 UTC |
| Links | DexScreener: https://dexscreener.com/solana/94qC4pCs8NKQLvmmANC22EEJ9455N3kCrwxxQFn4SjVg · Solscan: https://solscan.io/token/sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump · pump.fun: https://pump.fun/coin/sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump · web / Telegram / X: no publicados en DexScreener | consulta 02/10/2026 00:44 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 00:44 UTC)
- **Historia:**
  - Par creado el 02/10/2026 00:01 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 00:11 UTC, con el par a 10,2 min de creado: precio $0,008077, mcap $8.077.873, liquidez $257.628.
  - Velas de 1 h de GeckoTerminal (1, desde 02/10/2026 00:00 UTC): apertura $0,00004915 · máximo $0,008246 (02/10/2026 00:00 UTC) · mínimo $0,00004915 (02/10/2026 00:00 UTC) · último cierre $0,008241.
  - En la consulta 02/10/2026 00:44 UTC: precio $0,008242, liquidez $260.442, FDV $8.242.400.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 00:11 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,008077 |
| Liquidez | $257.628 |
| MCap | $8.077.873 |
| Volumen 24 h | $119.059 |
| Cambio 24 h | +16.320% |
| Cambio m5 / h1 | +0,5% / +16.320,0% |
| Volumen m5 / h1 | $791 / $119.059 |
| Trades m5 (compras / ventas) | 468 / 14 |
| Edad del par | 10,2 min |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 1/1 (100,0%, IC90 27,0%–100,0%) · secundaria 0/0 resueltas (shadow_monitor.json).

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

Desglose reconstruido desde los motivos registrados; suma 65 = score registrado 65 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| Gate de edad v7.2.1 | edad < 60 min o desconocida: sin bonos temporales | edad 10,2 min | +0 |
| MCap | ≥ $1M | $8.077.873 | +25 |
| Volumen 24 h | ≥ $100K | $119.059 | +15 |
| Liquidez | ≥ $100K | $257.628 | +15 |
| Cambio 24 h | ≥ +50% | +16.320% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +16.320% · liq/mcap 3,2% | +0 |
| **Total** | recortado a 0–100 |  | **65** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T00:11:48+00:00, sin estado previo): **65** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen alto, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=3.2% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 6 de 6.334 tokens analizados (0,09%) quedan ≥ 56. Con score 65, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 00:11 UTC, hasta 04/10/2026 00:11 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +0,5% · h1 +16.320,0% · h24 +16.320% · volumen m5/h1 0,01 · edad del par 10,2 min.
- **Precio de entrada** (alerta): $0,008077.
- **Consulta 02/10/2026 00:44 UTC:** $0,008242 (+2,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump_2026-10-02_001148.json` · blob `0038ea049ccaa13da5332bb9dd2087c43e3e86d3` · commit `ef4e54a` (2026-10-02T00:38:02Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_001148`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump · registro · 02/10/2026 00:11 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump · HTTP 200 · 02/10/2026 00:44 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump/report · HTTP 200 · 02/10/2026 00:44 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump · HTTP 200 · 02/10/2026 00:44 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/94qC4pCs8NKQLvmmANC22EEJ9455N3kCrwxxQFn4SjVg/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 00:44 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump · HTTP 404 · 02/10/2026 00:44 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=WAIFUSDT · HTTP 400 · 02/10/2026 00:44 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/WAIF-USD · HTTP 404 · 02/10/2026 00:44 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $260.442 vs $260.698 → 0,10%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,008242 vs $0,008241 → 0,01%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump_2026-10-02_001148.json',encoding='utf-8'));d=d.get('sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump',d);p=mock.patch('time.time',return_value=1790899908);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint sHRPPsSW8fAkr8dLVaSxweT22koSKQaxcYx4jEcpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 00:44 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `83066404855acb77…`
