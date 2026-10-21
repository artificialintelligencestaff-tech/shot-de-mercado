# Russian Oil Reserve (ROR) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1582 · liquidez $1.084.297 · mcap $158.239.805 (al detectar)  
Detectado el 21/10/2026 04:20 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 23/10/2026 04:20 UTC (< 48 h) · vigente: quedan 47,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ROR

Estudio de cómo se adquiere ROR, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 21/10/2026 04:54 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 21/10/2026 04:20 UTC | pumpswap `94mwrQY…9K5m` | $1.084.297 | 1% | 0,018% | 0,184% | 1,845% | $5.421 | $16.264 |
| consulta 21/10/2026 04:54 UTC | pumpswap `94mwrQY…9K5m` | $1.091.325 | 1% | 0,018% | 0,183% | 1,833% | $5.457 | $16.370 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump`
5. Configurar el slippage: 1% (liquidez $1.091.325, consulta 21/10/2026 04:54 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump) y el par en DexScreener (https://dexscreener.com/solana/94mwrQYepyroN7vaDMtrczFdhrnmBCQrGPMtEXmv9K5m); mint authority / freeze authority: revocada / revocada · holders 2.839 · top-10 1,24% (consulta 21/10/2026 04:54 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump
- Par en DexScreener: https://dexscreener.com/solana/94mwrQYepyroN7vaDMtrczFdhrnmBCQrGPMtEXmv9K5m
- Página del lanzamiento (pump.fun): https://pump.fun/coin/nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.839 · top-10 1,24% (consulta 21/10/2026 04:54 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Russian Oil Reserve / ROR | registro de la detección (trending) |
| Mint / contrato | `nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `94mwrQYepyroN7vaDMtrczFdhrnmBCQrGPMtEXmv9K5m` | DexScreener, al detectar (2 par(es) en la consulta 21/10/2026 04:54 UTC) |
| Deployer | `47KwGV6qGm9HgDM8y27mWNqw7atoaC8ByFAWeaLcTUCG` | RugCheck `creator` |
| Par creado | 21/10/2026 03:19 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,3 min / 60,3 min / 94,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 21/10/2026 04:54 UTC |
| Holders / top-10 | 2.839 / 1,24% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 21/10/2026 04:54 UTC |
| Holders efectivos del top-10 | 7,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 21/10/2026 04:54 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 21/10/2026 04:54 UTC |
| Links | DexScreener: https://dexscreener.com/solana/94mwrQYepyroN7vaDMtrczFdhrnmBCQrGPMtEXmv9K5m · Solscan: https://solscan.io/token/nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump · pump.fun: https://pump.fun/coin/nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump · web / Telegram / X: no publicados en DexScreener | consulta 21/10/2026 04:54 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 21/10/2026 04:54 UTC)
- **Historia:**
  - Par creado el 21/10/2026 03:19 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 21/10/2026 04:20 UTC, con el par a 60,3 min de creado: precio $0,1582, mcap $158.239.805, liquidez $1.084.297.
  - Velas de 1 h de GeckoTerminal (2, desde 21/10/2026 03:00 UTC): apertura $0,1531 · máximo $0,1603 (21/10/2026 04:00 UTC) · mínimo $0,00004400 (21/10/2026 03:00 UTC) · último cierre $0,1602.
  - En la consulta 21/10/2026 04:54 UTC: precio $0,1603, liquidez $1.091.325, FDV $160.336.319.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 21/10/2026 04:20 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1582 |
| Liquidez | $1.084.297 |
| MCap | $158.239.805 |
| Volumen 24 h | $535.664 |
| Cambio 24 h | +358.936% |
| Cambio m5 / h1 | +0,2% / +3,1% |
| Volumen m5 / h1 | $838 / $9.895 |
| Trades m5 (compras / ventas) | 154 / 5 |
| Edad del par | 60,3 min |
| Score del feed (WS) | 97 |

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
| Score del feed | score WS × 0,3 | WS 97 × 0,3 | +29,2 |
| MCap | ≥ $1M | $158.239.805 | +25 |
| Volumen 24 h | ≥ $100K | $535.664 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 97% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,2% · h1 +3,1% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,3 min | +8 |
| Volumen m5 | > $500 (par maduro) | $838 | +5 |
| Liquidez | ≥ $100K | $1.084.297 | +15 |
| Cambio 24 h | ≥ +50% | +358.936% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +358.936% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-21T04:20:09+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 72 de 42.753 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 21/10/2026 04:20 UTC, hasta 23/10/2026 04:20 UTC · vigente: quedan 47,4 h.
- **Aceleración al detectar:** cambio m5 +0,2% · h1 +3,1% · h24 +358.936% · volumen m5/h1 0,08 · edad del par 60,3 min.
- **Precio de entrada** (alerta): $0,1582.
- **Consulta 21/10/2026 04:54 UTC:** $0,1603 (+1,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump_2026-10-21_042009.json` · blob `6cc87339af63c432d1c538f32881dd4a0295f968` · commit `305f676` (2026-10-21T04:47:05Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-21_032202.json` · blob `bfe4729d26d184834e8d2ebbb28df819ca884e0a` · commit `305f676` (2026-10-21T04:47:05Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-21_042009`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump · registro · 21/10/2026 04:20 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump · HTTP 200 · 21/10/2026 04:54 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump/report · HTTP 200 · 21/10/2026 04:54 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump · HTTP 200 · 21/10/2026 04:54 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/94mwrQYepyroN7vaDMtrczFdhrnmBCQrGPMtEXmv9K5m/ohlcv/hour?limit=1000 · HTTP 200 · 21/10/2026 04:54 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump · HTTP 404 · 21/10/2026 04:54 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=RORUSDT · HTTP 400 · 21/10/2026 04:54 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ROR-USD · HTTP 404 · 21/10/2026 04:54 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.091.325 vs $1.090.998 → 0,03%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1603 vs $0,1602 → 0,04%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump_2026-10-21_042009.json',encoding='utf-8'));d=d.get('nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump',d);p=mock.patch('time.time',return_value=1792556409);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint nYSAJK8PxNi9eDoNiiKpgY8CULFjBWVHNy1Gxjgpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 21/10/2026 04:54 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `9b1ad5da08b0736c…`
