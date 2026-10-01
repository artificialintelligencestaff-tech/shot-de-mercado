# Super Acceleration (SACC) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0005801 · liquidez $70.327 · mcap $575.060 (al detectar)  
Detectado el 01/10/2026 21:55 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 03/10/2026 21:55 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SACC

Estudio de cómo se adquiere SACC, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 01/10/2026 21:55 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 01/10/2026 21:55 UTC | pumpswap `7eQjxhG…s6Ed` | $70.327 | 5% | 0,284% | 2,844% | 28,439% | $352 | $1.055 |
| consulta 01/10/2026 21:55 UTC | pumpswap `7eQjxhG…s6Ed` | $72.154 | 5% | 0,277% | 2,772% | 27,718% | $361 | $1.082 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump`
5. Configurar el slippage: 5% (liquidez $72.154, consulta 01/10/2026 21:55 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump) y el par en DexScreener (https://dexscreener.com/solana/7eQjxhGFZcjioSBX2GS72poE4XrqYYsyUBDryb36s6Ed); mint authority / freeze authority: revocada / revocada · holders 8.746 · top-10 9,25% (consulta 01/10/2026 21:55 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump
- Par en DexScreener: https://dexscreener.com/solana/7eQjxhGFZcjioSBX2GS72poE4XrqYYsyUBDryb36s6Ed
- Página del lanzamiento (pump.fun): https://pump.fun/coin/4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 8.746 · top-10 9,25% (consulta 01/10/2026 21:55 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Super Acceleration / SACC | registro de la detección (trending) |
| Mint / contrato | `4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7eQjxhGFZcjioSBX2GS72poE4XrqYYsyUBDryb36s6Ed` | DexScreener, al detectar (2 par(es) en la consulta 01/10/2026 21:55 UTC) |
| Deployer | `qTnJWUoNQgqjF5uZnryPRP7KYhd33oPDkbbvMziffBk` | RugCheck `creator` |
| Par creado | 01/10/2026 18:06 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 3,8 h / 3,8 h / 3,8 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 01/10/2026 21:55 UTC |
| Holders / top-10 | 8.746 / 9,25% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 01/10/2026 21:55 UTC |
| Holders efectivos del top-10 | 2,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 01/10/2026 21:55 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 01/10/2026 21:55 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7eQjxhGFZcjioSBX2GS72poE4XrqYYsyUBDryb36s6Ed · Solscan: https://solscan.io/token/4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump · pump.fun: https://pump.fun/coin/4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump · web: https://superacceleration.world · twitter: https://x.com/SolSuperAcc | consulta 01/10/2026 21:55 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 01/10/2026 21:55 UTC)
- **Historia:**
  - Par creado el 01/10/2026 18:06 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 01/10/2026 21:55 UTC, con el par a 3,8 h de creado: precio $0,0005801, mcap $575.060, liquidez $70.327.
  - Velas de 1 h de GeckoTerminal (4, desde 01/10/2026 18:00 UTC): apertura $0,0001037 · máximo $0,001340 (01/10/2026 20:00 UTC) · mínimo $0,0001037 (01/10/2026 18:00 UTC) · último cierre $0,0006057.
  - En la consulta 01/10/2026 21:55 UTC: precio $0,0006097, liquidez $72.154, FDV $604.422.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 01/10/2026 21:55 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0005801 |
| Liquidez | $70.327 |
| MCap | $575.060 |
| Volumen 24 h | $1.302.571 |
| Cambio 24 h | +459% |
| Cambio m5 / h1 | -8,1% / +25,2% |
| Volumen m5 / h1 | $19.929 / $228.447 |
| Trades m5 (compras / ventas) | 679 / 66 |
| Edad del par | 3,8 h |
| Score del feed (WS) | 75 |

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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 75 × 0,3 | +22,5 |
| MCap | ≥ $100K | $575.060 | +15 |
| Volumen 24 h | ≥ $1M | $1.302.571 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 91% | +25 |
| Edge temprano | edad < 4 h (par maduro) | edad 3,8 h | +8 |
| Volumen m5 | > $1K (par maduro) | $19.929 | +10 |
| Liquidez | ≥ $50K | $70.327 | +10 |
| Cambio 24 h | ≥ +50% | +459% | +10 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-01T21:55:14+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez decente, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 6 de 5.986 tokens analizados (0,10%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 01/10/2026 21:55 UTC, hasta 03/10/2026 21:55 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -8,1% · h1 +25,2% · h24 +459% · volumen m5/h1 0,09 · edad del par 3,8 h.
- **Precio de entrada** (alerta): $0,0005801.
- **Consulta 01/10/2026 21:55 UTC:** $0,0006097 (+5,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump_2026-10-01_215541.json` · blob `8c0b5b90505e9d4e6c726afca7065d6d0c03ba7e` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-01_215012.json` · blob `df0a35a45b0545c83d45b36962e407594ee6567b` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-01_215541`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump · registro · 01/10/2026 21:55 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump · HTTP 200 · 01/10/2026 21:55 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump/report · HTTP 200 · 01/10/2026 21:55 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump · HTTP 200 · 01/10/2026 21:55 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7eQjxhGFZcjioSBX2GS72poE4XrqYYsyUBDryb36s6Ed/ohlcv/hour?limit=1000 · HTTP 200 · 01/10/2026 21:55 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump · HTTP 404 · 01/10/2026 21:55 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SACCUSDT · HTTP 400 · 01/10/2026 21:55 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SACC-USD · HTTP 404 · 01/10/2026 21:55 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $72.154 vs $72.090 → 0,09%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0006097 vs $0,0006057 → 0,66%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump_2026-10-01_215541.json',encoding='utf-8'));d=d.get('4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump',d);p=mock.patch('time.time',return_value=1790891714);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 4K8V9yH6kKRLS46BTG68Te1QHLkb7an8J5YcWQ3ppump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 01/10/2026 21:55 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `a2f2f4311b98bcaa…`
