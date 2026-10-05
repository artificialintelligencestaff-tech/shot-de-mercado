# American Dividend Trust Fund (ADTF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,002808 · liquidez $152.263 · mcap $2.806.175 (al detectar)  
Detectado el 05/10/2026 04:09 UTC por: MCap > $1M, Volumen decente, Buy pressure >60% (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 07/10/2026 04:09 UTC (< 48 h) · vigente: quedan 47,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ADTF

Estudio de cómo se adquiere ADTF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 05/10/2026 04:15 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 05/10/2026 04:09 UTC | pumpswap `83qKzZ4…cqhB` | $152.263 | 5% | 0,131% | 1,314% | 13,135% | $761 | $2.284 |
| consulta 05/10/2026 04:15 UTC | pumpswap `83qKzZ4…cqhB` | $152.184 | 5% | 0,131% | 1,314% | 13,142% | $761 | $2.283 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump`
5. Configurar el slippage: 5% (liquidez $152.184, consulta 05/10/2026 04:15 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump) y el par en DexScreener (https://dexscreener.com/solana/83qKzZ4p212UkyBNm3WQtkr8vGLT6ka18q54g44tcqhB); mint authority / freeze authority: revocada / revocada · holders 1.901 · top-10 11,50% (consulta 05/10/2026 04:15 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump
- Par en DexScreener: https://dexscreener.com/solana/83qKzZ4p212UkyBNm3WQtkr8vGLT6ka18q54g44tcqhB
- Página del lanzamiento (pump.fun): https://pump.fun/coin/oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.901 · top-10 11,50% (consulta 05/10/2026 04:15 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | American Dividend Trust Fund / ADTF | registro de la detección (pumpportal) |
| Mint / contrato | `oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `83qKzZ4p212UkyBNm3WQtkr8vGLT6ka18q54g44tcqhB` | DexScreener, al detectar (2 par(es) en la consulta 05/10/2026 04:15 UTC) |
| Deployer | `5qQzvZoWj9Ktqdi13jRKBgkCGfurkMxQoW6Xp1tBDvRc` | PumpPortal (evento create), al detectar |
| Par creado | 05/10/2026 03:09 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,1 min / 60,1 min / 66,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 05/10/2026 04:15 UTC |
| Holders / top-10 | 1.901 / 11,50% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 05/10/2026 04:15 UTC |
| Holders efectivos del top-10 | 8,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 05/10/2026 04:15 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 05/10/2026 04:15 UTC |
| Links | DexScreener: https://dexscreener.com/solana/83qKzZ4p212UkyBNm3WQtkr8vGLT6ka18q54g44tcqhB · Solscan: https://solscan.io/token/oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump · pump.fun: https://pump.fun/coin/oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump · web / Telegram / X: no publicados en DexScreener | consulta 05/10/2026 04:15 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 05/10/2026 04:15 UTC)
- **Historia:**
  - Par creado el 05/10/2026 03:09 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 05/10/2026 04:09 UTC, con el par a 60,1 min de creado: precio $0,002808, mcap $2.806.175, liquidez $152.263.
  - Velas de 1 h de GeckoTerminal (2, desde 05/10/2026 03:00 UTC): apertura $0,002624 · máximo $0,002816 (05/10/2026 03:00 UTC) · mínimo $0,00005025 (05/10/2026 03:00 UTC) · último cierre $0,002777.
  - En la consulta 05/10/2026 04:15 UTC: precio $0,002805, liquidez $152.184, FDV $2.803.015.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 05/10/2026 04:09 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,002808 |
| Liquidez | $152.263 |
| MCap | $2.806.175 |
| Volumen 24 h | $72.285 |
| Cambio 24 h | +5.482% |
| Cambio m5 / h1 | +1,2% / +5.482,0% |
| Volumen m5 / h1 | $750 / $72.285 |
| Trades m5 (compras / ventas) | 14 / 9 |
| Edad del par | 60,1 min |
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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $1M | $2.806.175 | +25 |
| Volumen 24 h | ≥ $50K | $72.285 | +10 |
| Buy pressure m5 | > 60% (par maduro) | 61% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +1,2% · h1 +5.482,0% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,1 min | +8 |
| Volumen m5 | > $500 (par maduro) | $750 | +5 |
| Liquidez | ≥ $100K | $152.263 | +15 |
| Cambio 24 h | ≥ +50% | +5.482% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +5.482% · liq/mcap 5,4% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-05T04:09:05+00:00, sin estado previo): **100** · motivos: MCap > $1M, Volumen decente, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=5.4% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 15 de 11.414 tokens analizados (0,13%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 05/10/2026 04:09 UTC, hasta 07/10/2026 04:09 UTC · vigente: quedan 47,9 h.
- **Aceleración al detectar:** cambio m5 +1,2% · h1 +5.482,0% · h24 +5.482% · volumen m5/h1 0,01 · edad del par 60,1 min.
- **Precio de entrada** (alerta): $0,002808.
- **Consulta 05/10/2026 04:15 UTC:** $0,002805 (-0,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump_2026-10-05_040905.json` · blob `e18e8dc488c7ef1f7a167a5b615925506f0d1bd5` · commit `3e5a90e` (2026-10-05T04:09:26Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-05_040905`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump · registro · 05/10/2026 04:09 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump · HTTP 200 · 05/10/2026 04:15 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump/report · HTTP 200 · 05/10/2026 04:15 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump · HTTP 200 · 05/10/2026 04:15 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/83qKzZ4p212UkyBNm3WQtkr8vGLT6ka18q54g44tcqhB/ohlcv/hour?limit=1000 · HTTP 200 · 05/10/2026 04:15 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump · HTTP 404 · 05/10/2026 04:15 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ADTFUSDT · HTTP 400 · 05/10/2026 04:15 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ADTF-USD · HTTP 404 · 05/10/2026 04:15 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $152.184 vs $152.106 → 0,05%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002805 vs $0,002777 → 1,02%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump_2026-10-05_040905.json',encoding='utf-8'));d=d.get('oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump',d);p=mock.patch('time.time',return_value=1791173345);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint oJasFBxCqCYuzHmxggsyy4jripUtF3RfvKNPvSHpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 05/10/2026 04:15 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `8a50adb8fd2667c6…`
