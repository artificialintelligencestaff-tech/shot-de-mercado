# The Dime Lover (ROWDY) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000003556 · liquidez $3.367 · mcap $2.817 (al detectar)  
Detectado el 21/10/2026 01:58 UTC por: MCap bajo, Volumen alto, Volumen acelerado (5m/1h > 50%) (score 68, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 23/10/2026 01:58 UTC (< 48 h) · vigente: quedan 47,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ROWDY

Estudio de cómo se adquiere ROWDY, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 21/10/2026 02:59 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 21/10/2026 01:58 UTC | pumpswap `GpUVSim…kzgy` | $3.367 | 10% | 5,940% | 59,396% | 593,962% | $17 | $51 |
| consulta 21/10/2026 02:59 UTC | pumpswap `GpUVSim…kzgy` | $3.426 | 10% | 5,837% | 58,373% | 583,730% | $17 | $51 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump`
5. Configurar el slippage: 10% (liquidez $3.426, consulta 21/10/2026 02:59 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump) y el par en DexScreener (https://dexscreener.com/solana/GpUVSimbikD4nMENDHeSSP5xUAmb3YhWoa8QYJpKkzgy); mint authority / freeze authority: revocada / revocada · holders 337 · top-10 99,69% (consulta 21/10/2026 02:59 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump
- Par en DexScreener: https://dexscreener.com/solana/GpUVSimbikD4nMENDHeSSP5xUAmb3YhWoa8QYJpKkzgy
- Página del lanzamiento (pump.fun): https://pump.fun/coin/6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 337 · top-10 99,69% (consulta 21/10/2026 02:59 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | The Dime Lover / ROWDY | registro de la detección (pumpportal) |
| Mint / contrato | `6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `GpUVSimbikD4nMENDHeSSP5xUAmb3YhWoa8QYJpKkzgy` | DexScreener, al detectar (2 par(es) en la consulta 21/10/2026 02:59 UTC) |
| Deployer | `yHCxHBEaJW5tbndqC8JciSThr7U1cqLpdcsvHcx6PRe` | PumpPortal (evento create), al detectar |
| Par creado | 20/10/2026 23:46 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 2,2 h / 2,2 h / 3,2 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 21/10/2026 02:59 UTC |
| Holders / top-10 | 337 / 99,69% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 21/10/2026 02:59 UTC |
| Holders efectivos del top-10 | 1,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 21/10/2026 02:59 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 21/10/2026 02:59 UTC |
| Links | DexScreener: https://dexscreener.com/solana/GpUVSimbikD4nMENDHeSSP5xUAmb3YhWoa8QYJpKkzgy · Solscan: https://solscan.io/token/6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump · pump.fun: https://pump.fun/coin/6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump · web / Telegram / X: no publicados en DexScreener | consulta 21/10/2026 02:59 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 21/10/2026 02:59 UTC)
- **Historia:**
  - Par creado el 20/10/2026 23:46 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 21/10/2026 01:58 UTC, con el par a 2,2 h de creado: precio $0,000003556, mcap $2.817, liquidez $3.367.
  - Velas de 1 h de GeckoTerminal (4, desde 20/10/2026 23:00 UTC): apertura $0,0001124 · máximo $0,0002858 (20/10/2026 23:00 UTC) · mínimo $0,000003123 (20/10/2026 23:00 UTC) · último cierre $0,000003642.
  - En la consulta 21/10/2026 02:59 UTC: precio $0,000003645, liquidez $3.426, FDV $2.887.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 21/10/2026 01:58 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000003556 |
| Liquidez | $3.367 |
| MCap | $2.817 |
| Volumen 24 h | $175.503 |
| Cambio 24 h | -94% |
| Cambio m5 / h1 | +13,4% / +12,8% |
| Volumen m5 / h1 | $633 / $633 |
| Trades m5 (compras / ventas) | 6 / 10 |
| Edad del par | 2,2 h |
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

Desglose reconstruido desde los motivos registrados; suma 68 = score registrado 68 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | < $50K | $2.817 | +0 |
| Volumen 24 h | ≥ $100K | $175.503 | +15 |
| Volumen m5/h1 | > 0,5 (par maduro) | 1,00 | +25 |
| Trades m5/h1 | > 0,5 (par maduro) | 0,94 | +20 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +13,4% · h1 +12,8% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 2,2 h | +8 |
| Volumen m5 | > $500 (par maduro) | $633 | +5 |
| Venta dominante | buy pressure < 40% con volumen m5 | 38% | -20 |
| Liquidez | < $20K | $3.367 | +0 |
| Cambio 24 h | ≤ −30% | -94% | -5 |
| **Total** | recortado a 0–100 |  | **68** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-21T01:58:23+00:00, sin estado previo): **68** · motivos: MCap bajo, Volumen alto, Volumen acelerado (5m/1h > 50%), Trades acelerados (5m/1h > 50%), Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Venta dominante (buy_pressure <40%), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 71 de 42.672 tokens analizados (0,17%) quedan ≥ 56. Con score 68, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 21/10/2026 01:58 UTC, hasta 23/10/2026 01:58 UTC · vigente: quedan 47,0 h.
- **Aceleración al detectar:** cambio m5 +13,4% · h1 +12,8% · h24 -94% · volumen m5/h1 1,00 · edad del par 2,2 h.
- **Precio de entrada** (alerta): $0,000003556.
- **Consulta 21/10/2026 02:59 UTC:** $0,000003645 (+2,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump_2026-10-21_015823.json` · blob `2ed3da33db2d307aa9c9e654cca90346e6069b63` · commit `49726ad` (2026-10-21T02:52:08Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-21_015823`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump · registro · 21/10/2026 01:58 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump · HTTP 200 · 21/10/2026 02:59 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump/report · HTTP 200 · 21/10/2026 02:59 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump · HTTP 200 · 21/10/2026 02:59 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/GpUVSimbikD4nMENDHeSSP5xUAmb3YhWoa8QYJpKkzgy/ohlcv/hour?limit=1000 · HTTP 200 · 21/10/2026 02:59 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump · HTTP 404 · 21/10/2026 02:59 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ROWDYUSDT · HTTP 400 · 21/10/2026 02:59 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ROWDY-USD · HTTP 404 · 21/10/2026 02:59 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.426 vs $3.370 → 1,63%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000003645 vs $0,000003642 → 0,08%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump_2026-10-21_015823.json',encoding='utf-8'));d=d.get('6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump',d);p=mock.patch('time.time',return_value=1792547903);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 6XN3Pgptq79SA13iTSS4TtQngkGVYAN2b6ToE2eYpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 21/10/2026 02:59 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `c95091445a669439…`
