# IOF (IOF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1182 · liquidez $1.002.494 · mcap $118.268.074 (al detectar)  
Detectado el 06/10/2026 01:08 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 08/10/2026 01:08 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir IOF

Estudio de cómo se adquiere IOF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 01:37 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 01:08 UTC | pumpswap `ECVuPno…w6ug` | $1.002.494 | 1% | 0,020% | 0,200% | 1,995% | $5.012 | $15.037 |
| consulta 06/10/2026 01:36 UTC | pumpswap `ECVuPno…w6ug` | $1.012.381 | 1% | 0,020% | 0,198% | 1,976% | $5.062 | $15.186 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump`
5. Configurar el slippage: 1% (liquidez $1.012.381, consulta 06/10/2026 01:36 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump) y el par en DexScreener (https://dexscreener.com/solana/ECVuPnoq3AiQ92WyPxBU9fHpqq3SLbFz8Y8Du81fw6ug); mint authority / freeze authority: revocada / revocada · holders 3.056 · top-10 2,57% (consulta 06/10/2026 01:36 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump
- Par en DexScreener: https://dexscreener.com/solana/ECVuPnoq3AiQ92WyPxBU9fHpqq3SLbFz8Y8Du81fw6ug
- Página del lanzamiento (pump.fun): https://pump.fun/coin/4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.056 · top-10 2,57% (consulta 06/10/2026 01:36 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | IOF / IOF | registro de la detección (trending) |
| Mint / contrato | `4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `ECVuPnoq3AiQ92WyPxBU9fHpqq3SLbFz8Y8Du81fw6ug` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 01:36 UTC) |
| Deployer | `GoYjkc523BEqtCjbbTwSi1svT9dFf6EsyYh2VSLSgJy7` | RugCheck `creator` |
| Par creado | 06/10/2026 00:08 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,3 min / 60,3 min / 88,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 01:36 UTC |
| Holders / top-10 | 3.056 / 2,57% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 01:36 UTC |
| Holders efectivos del top-10 | 9,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 01:36 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 01:36 UTC |
| Links | DexScreener: https://dexscreener.com/solana/ECVuPnoq3AiQ92WyPxBU9fHpqq3SLbFz8Y8Du81fw6ug · Solscan: https://solscan.io/token/4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump · pump.fun: https://pump.fun/coin/4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump · web / Telegram / X: no publicados en DexScreener | consulta 06/10/2026 01:36 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 01:36 UTC)
- **Historia:**
  - Par creado el 06/10/2026 00:08 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 01:08 UTC, con el par a 60,3 min de creado: precio $0,1182, mcap $118.268.074, liquidez $1.002.494.
  - Velas de 1 h de GeckoTerminal (2, desde 06/10/2026 00:00 UTC): apertura $0,002390 · máximo $0,1206 (06/10/2026 01:00 UTC) · mínimo $0,00005022 (06/10/2026 00:00 UTC) · último cierre $0,1205.
  - En la consulta 06/10/2026 01:36 UTC: precio $0,1207, liquidez $1.012.381, FDV $120.743.691.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 01:08 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1182 |
| Liquidez | $1.002.494 |
| MCap | $118.268.074 |
| Volumen 24 h | $489.074 |
| Cambio 24 h | +235.164% |
| Cambio m5 / h1 | +0,4% / +5,0% |
| Volumen m5 / h1 | $991 / $9.992 |
| Trades m5 (compras / ventas) | 253 / 0 |
| Edad del par | 60,3 min |
| Score del feed (WS) | 98 |

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
| Score del feed | score WS × 0,3 | WS 98 × 0,3 | +29,4 |
| MCap | ≥ $1M | $118.268.074 | +25 |
| Volumen 24 h | ≥ $100K | $489.074 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 100% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,4% · h1 +5,0% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,3 min | +8 |
| Volumen m5 | > $500 (par maduro) | $991 | +5 |
| Liquidez | ≥ $100K | $1.002.494 | +15 |
| Cambio 24 h | ≥ +50% | +235.164% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +235.164% · liq/mcap 0,8% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T01:08:39+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 17 de 13.789 tokens analizados (0,12%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 01:08 UTC, hasta 08/10/2026 01:08 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +0,4% · h1 +5,0% · h24 +235.164% · volumen m5/h1 0,10 · edad del par 60,3 min.
- **Precio de entrada** (alerta): $0,1182.
- **Consulta 06/10/2026 01:36 UTC:** $0,1207 (+2,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump_2026-10-06_010839.json` · blob `034f62d70eb0552773e3cf526d97c052be23462b` · commit `0332ef0` (2026-10-06T01:30:44Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-06_000909.json` · blob `380ddbb678a51a74042e42e1db268bf5d7ff975a` · commit `0332ef0` (2026-10-06T01:30:44Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_010839`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump · registro · 06/10/2026 01:08 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump · HTTP 200 · 06/10/2026 01:36 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump/report · HTTP 200 · 06/10/2026 01:36 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump · HTTP 200 · 06/10/2026 01:36 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/ECVuPnoq3AiQ92WyPxBU9fHpqq3SLbFz8Y8Du81fw6ug/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 01:36 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump · HTTP 404 · 06/10/2026 01:37 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=IOFUSDT · HTTP 400 · 06/10/2026 01:37 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/IOF-USD · HTTP 404 · 06/10/2026 01:37 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.012.381 vs $1.010.073 → 0,23%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1207 vs $0,1205 → 0,14%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump_2026-10-06_010839.json',encoding='utf-8'));d=d.get('4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump',d);p=mock.patch('time.time',return_value=1791248919);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 4BQRLLYacsUXmw3mn3v3LknZZvN4HbXdZhgHSGfUpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 01:37 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `754846e90956012f…`
