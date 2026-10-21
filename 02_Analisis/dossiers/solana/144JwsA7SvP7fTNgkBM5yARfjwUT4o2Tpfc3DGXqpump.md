# National American Future Fund (NAFF) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1595 · liquidez $1.104.927 · mcap $159.532.028 (al detectar)  
Detectado el 21/10/2026 18:36 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 95, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 23/10/2026 18:36 UTC (< 48 h) · vigente: quedan 47,3 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir NAFF

Estudio de cómo se adquiere NAFF, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 21/10/2026 19:20 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 21/10/2026 18:36 UTC | pumpswap `DypbVCm…vMB9` | $1.104.927 | 1% | 0,018% | 0,181% | 1,810% | $5.525 | $16.574 |
| consulta 21/10/2026 19:20 UTC | pumpswap `DypbVCm…vMB9` | $1.095.437 | 1% | 0,018% | 0,183% | 1,826% | $5.477 | $16.432 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump`
5. Configurar el slippage: 1% (liquidez $1.095.437, consulta 21/10/2026 19:20 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump) y el par en DexScreener (https://dexscreener.com/solana/DypbVCmDNjzYxoSSxr5rRiBBGkPYgQs5hSUKqngEvMB9); mint authority / freeze authority: revocada / revocada · holders 3.995 · top-10 0,58% (consulta 21/10/2026 19:20 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump
- Par en DexScreener: https://dexscreener.com/solana/DypbVCmDNjzYxoSSxr5rRiBBGkPYgQs5hSUKqngEvMB9
- Página del lanzamiento (pump.fun): https://pump.fun/coin/144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.995 · top-10 0,58% (consulta 21/10/2026 19:20 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | National American Future Fund / NAFF | registro de la detección (trending) |
| Mint / contrato | `144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DypbVCmDNjzYxoSSxr5rRiBBGkPYgQs5hSUKqngEvMB9` | DexScreener, al detectar (2 par(es) en la consulta 21/10/2026 19:20 UTC) |
| Deployer | `FDyxfJxNgoKQVvgzVZULdPk78Q82g8BCCZKKnZqbzT5V` | RugCheck `creator` |
| Par creado | 21/10/2026 17:35 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 61,1 min / 61,1 min / 104,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 21/10/2026 19:20 UTC |
| Holders / top-10 | 3.995 / 0,58% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 21/10/2026 19:20 UTC |
| Holders efectivos del top-10 | 2,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 21/10/2026 19:20 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 21/10/2026 19:20 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DypbVCmDNjzYxoSSxr5rRiBBGkPYgQs5hSUKqngEvMB9 · Solscan: https://solscan.io/token/144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump · pump.fun: https://pump.fun/coin/144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump · web / Telegram / X: no publicados en DexScreener | consulta 21/10/2026 19:20 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 21/10/2026 19:20 UTC)
- **Historia:**
  - Par creado el 21/10/2026 17:35 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 21/10/2026 18:36 UTC, con el par a 61,1 min de creado: precio $0,1595, mcap $159.532.028, liquidez $1.104.927.
  - Velas de 1 h de GeckoTerminal (3, desde 21/10/2026 17:00 UTC): apertura $0,1565 · máximo $0,1604 (21/10/2026 18:00 UTC) · mínimo $0,00004512 (21/10/2026 17:00 UTC) · último cierre $0,1582.
  - En la consulta 21/10/2026 19:20 UTC: precio $0,1586, liquidez $1.095.437, FDV $158.677.894.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 21/10/2026 18:36 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1595 |
| Liquidez | $1.104.927 |
| MCap | $159.532.028 |
| Volumen 24 h | $541.963 |
| Cambio 24 h | +353.596% |
| Cambio m5 / h1 | +0,1% / +1,9% |
| Volumen m5 / h1 | $352 / $4.743 |
| Trades m5 (compras / ventas) | 87 / 5 |
| Edad del par | 61,1 min |
| Score del feed (WS) | 90 |

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

Desglose reconstruido desde los motivos registrados; suma 95 = score registrado 95 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 90 × 0,3 | +27,0 |
| MCap | ≥ $1M | $159.532.028 | +25 |
| Volumen 24 h | ≥ $100K | $541.963 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 95% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,1% · h1 +1,9% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 61,1 min | +8 |
| Liquidez | ≥ $100K | $1.104.927 | +15 |
| Cambio 24 h | ≥ +50% | +353.596% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +353.596% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **95** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-21T18:36:50+00:00, sin estado previo): **95** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 72 de 43.186 tokens analizados (0,17%) quedan ≥ 56. Con score 95, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 21/10/2026 18:36 UTC, hasta 23/10/2026 18:36 UTC · vigente: quedan 47,3 h.
- **Aceleración al detectar:** cambio m5 +0,1% · h1 +1,9% · h24 +353.596% · volumen m5/h1 0,07 · edad del par 61,1 min.
- **Precio de entrada** (alerta): $0,1595.
- **Consulta 21/10/2026 19:20 UTC:** $0,1586 (-0,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump_2026-10-21_183650.json` · blob `f0e1d1082aad0e97e904ff5f6f039894fe4d5656` · commit `d94fbe5` (2026-10-21T19:10:35Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-21_174714.json` · blob `569e3c62708593b1778ec3542099470219e76d5f` · commit `d94fbe5` (2026-10-21T19:10:35Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-21_183650`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump · registro · 21/10/2026 18:36 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump · HTTP 200 · 21/10/2026 19:20 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump/report · HTTP 200 · 21/10/2026 19:20 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump · HTTP 200 · 21/10/2026 19:20 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DypbVCmDNjzYxoSSxr5rRiBBGkPYgQs5hSUKqngEvMB9/ohlcv/hour?limit=1000 · HTTP 200 · 21/10/2026 19:20 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump · HTTP 404 · 21/10/2026 19:20 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=NAFFUSDT · HTTP 400 · 21/10/2026 19:20 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/NAFF-USD · HTTP 404 · 21/10/2026 19:20 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.095.437 vs $1.097.427 → 0,18%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1586 vs $0,1582 → 0,27%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump_2026-10-21_183650.json',encoding='utf-8'));d=d.get('144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump',d);p=mock.patch('time.time',return_value=1792607810);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 144JwsA7SvP7fTNgkBM5yARfjwUT4o2Tpfc3DGXqpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 21/10/2026 19:20 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `de74b8e7cc93fa74…`
