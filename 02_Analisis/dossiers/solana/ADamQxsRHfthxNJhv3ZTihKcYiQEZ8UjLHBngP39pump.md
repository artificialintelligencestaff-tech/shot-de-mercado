# GOIF (GOIF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1636 · liquidez $1.126.727 · mcap $163.675.820 (al detectar)  
Detectado el 09/10/2026 06:33 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 11/10/2026 06:33 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir GOIF

Estudio de cómo se adquiere GOIF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 09/10/2026 06:46 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 09/10/2026 06:33 UTC | pumpswap `2kagob1…LXdS` | $1.126.727 | 1% | 0,018% | 0,178% | 1,775% | $5.634 | $16.901 |
| consulta 09/10/2026 06:46 UTC | pumpswap `2kagob1…LXdS` | $1.132.108 | 1% | 0,018% | 0,177% | 1,767% | $5.661 | $16.982 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump`
5. Configurar el slippage: 1% (liquidez $1.132.108, consulta 09/10/2026 06:46 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump) y el par en DexScreener (https://dexscreener.com/solana/2kagob1yBq4xzbrQxynHegqmc7q75XkJGMa2JVbuLXdS); mint authority / freeze authority: revocada / revocada · holders 2.265 · top-10 0,82% (consulta 09/10/2026 06:46 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump
- Par en DexScreener: https://dexscreener.com/solana/2kagob1yBq4xzbrQxynHegqmc7q75XkJGMa2JVbuLXdS
- Página del lanzamiento (pump.fun): https://pump.fun/coin/ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.265 · top-10 0,82% (consulta 09/10/2026 06:46 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | GOIF / GOIF | registro de la detección (trending) |
| Mint / contrato | `ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `2kagob1yBq4xzbrQxynHegqmc7q75XkJGMa2JVbuLXdS` | DexScreener, al detectar (2 par(es) en la consulta 09/10/2026 06:46 UTC) |
| Deployer | `DHq6YJozK8FBzKxyewo9gMJjpkB4CWHowWqGJ29iJ2QT` | RugCheck `creator` |
| Par creado | 09/10/2026 05:32 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,2 min / 60,2 min / 73,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 09/10/2026 06:46 UTC |
| Holders / top-10 | 2.265 / 0,82% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 09/10/2026 06:46 UTC |
| Holders efectivos del top-10 | 4,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 09/10/2026 06:46 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 09/10/2026 06:46 UTC |
| Links | DexScreener: https://dexscreener.com/solana/2kagob1yBq4xzbrQxynHegqmc7q75XkJGMa2JVbuLXdS · Solscan: https://solscan.io/token/ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump · pump.fun: https://pump.fun/coin/ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump · web / Telegram / X: no publicados en DexScreener | consulta 09/10/2026 06:46 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 09/10/2026 06:46 UTC)
- **Historia:**
  - Par creado el 09/10/2026 05:32 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 09/10/2026 06:33 UTC, con el par a 60,2 min de creado: precio $0,1636, mcap $163.675.820, liquidez $1.126.727.
  - Velas de 1 h de GeckoTerminal (2, desde 09/10/2026 05:00 UTC): apertura $0,002717 · máximo $0,1650 (09/10/2026 06:00 UTC) · mínimo $0,00004595 (09/10/2026 05:00 UTC) · último cierre $0,1650.
  - En la consulta 09/10/2026 06:46 UTC: precio $0,1648, liquidez $1.132.108, FDV $164.863.957.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 09/10/2026 06:33 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1636 |
| Liquidez | $1.126.727 |
| MCap | $163.675.820 |
| Volumen 24 h | $579.172 |
| Cambio 24 h | +356.248% |
| Cambio m5 / h1 | +0,2% / +3,1% |
| Volumen m5 / h1 | $2.634 / $33.030 |
| Trades m5 (compras / ventas) | 149 / 9 |
| Edad del par | 60,2 min |
| Score del feed (WS) | 99 |

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
| Score del feed | score WS × 0,3 | WS 99 × 0,3 | +29,6 |
| MCap | ≥ $1M | $163.675.820 | +25 |
| Volumen 24 h | ≥ $100K | $579.172 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 94% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,2% · h1 +3,1% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,2 min | +8 |
| Volumen m5 | > $1K (par maduro) | $2.634 | +10 |
| Liquidez | ≥ $100K | $1.126.727 | +15 |
| Cambio 24 h | ≥ +50% | +356.248% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +356.248% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-09T06:33:00+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 41 de 24.132 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 09/10/2026 06:33 UTC, hasta 11/10/2026 06:33 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +0,2% · h1 +3,1% · h24 +356.248% · volumen m5/h1 0,08 · edad del par 60,2 min.
- **Precio de entrada** (alerta): $0,1636.
- **Consulta 09/10/2026 06:46 UTC:** $0,1648 (+0,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump_2026-10-09_063300.json` · blob `7189db6b9a5abee91c0566094a8c50269debf525` · commit `1a2f50d` (2026-10-09T06:40:04Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-09_053412.json` · blob `6c0e51ec065c86c31c5d4c4125eee508b9c91397` · commit `1a2f50d` (2026-10-09T06:40:04Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-09_063300`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump · registro · 09/10/2026 06:33 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump · HTTP 200 · 09/10/2026 06:46 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump/report · HTTP 200 · 09/10/2026 06:46 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump · HTTP 200 · 09/10/2026 06:46 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/2kagob1yBq4xzbrQxynHegqmc7q75XkJGMa2JVbuLXdS/ohlcv/hour?limit=1000 · HTTP 200 · 09/10/2026 06:46 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump · HTTP 404 · 09/10/2026 06:46 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=GOIFUSDT · HTTP 400 · 09/10/2026 06:46 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/GOIF-USD · HTTP 404 · 09/10/2026 06:46 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.132.108 vs $1.132.330 → 0,02%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1648 vs $0,1650 → 0,12%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump_2026-10-09_063300.json',encoding='utf-8'));d=d.get('ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump',d);p=mock.patch('time.time',return_value=1791527580);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint ADamQxsRHfthxNJhv3ZTihKcYiQEZ8UjLHBngP39pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 09/10/2026 06:46 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `8d080b2a42a30273…`
