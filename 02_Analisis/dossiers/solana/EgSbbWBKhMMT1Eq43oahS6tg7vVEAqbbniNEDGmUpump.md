# World Oil Supply Exchange (WOSE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,002658 · liquidez $145.630 · mcap $2.655.961 (al detectar)  
Detectado el 07/10/2026 12:54 UTC por: MCap > $1M, Volumen decente, Buy pressure >60% (score 93, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 09/10/2026 12:54 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir WOSE

Estudio de cómo se adquiere WOSE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/10/2026 13:17 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/10/2026 12:54 UTC | pumpswap `DNGD1Sw…zynC` | $145.630 | 5% | 0,137% | 1,373% | 13,733% | $728 | $2.184 |
| consulta 07/10/2026 13:17 UTC | pumpswap `DNGD1Sw…zynC` | $146.306 | 5% | 0,137% | 1,367% | 13,670% | $732 | $2.195 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump`
5. Configurar el slippage: 5% (liquidez $146.306, consulta 07/10/2026 13:17 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump) y el par en DexScreener (https://dexscreener.com/solana/DNGD1SwQU8CkXaQGQCxmPErTf9XwgQ36zu38gHbtzynC); mint authority / freeze authority: revocada / revocada · holders 3.026 · top-10 3,54% (consulta 07/10/2026 13:17 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump
- Par en DexScreener: https://dexscreener.com/solana/DNGD1SwQU8CkXaQGQCxmPErTf9XwgQ36zu38gHbtzynC
- Página del lanzamiento (pump.fun): https://pump.fun/coin/EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.026 · top-10 3,54% (consulta 07/10/2026 13:17 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | World Oil Supply Exchange / WOSE | registro de la detección (pumpportal) |
| Mint / contrato | `EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DNGD1SwQU8CkXaQGQCxmPErTf9XwgQ36zu38gHbtzynC` | DexScreener, al detectar (2 par(es) en la consulta 07/10/2026 13:17 UTC) |
| Deployer | `qVgHyLXLdJUQHHZpCCAV8jTWJcSM6f6cd64hXQyMgkd` | PumpPortal (evento create), al detectar |
| Par creado | 07/10/2026 11:53 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,2 min / 60,2 min / 83,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/10/2026 13:17 UTC |
| Holders / top-10 | 3.026 / 3,54% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/10/2026 13:17 UTC |
| Holders efectivos del top-10 | 1,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/10/2026 13:17 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 07/10/2026 13:17 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DNGD1SwQU8CkXaQGQCxmPErTf9XwgQ36zu38gHbtzynC · Solscan: https://solscan.io/token/EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump · pump.fun: https://pump.fun/coin/EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump · web / Telegram / X: no publicados en DexScreener | consulta 07/10/2026 13:17 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/10/2026 13:17 UTC)
- **Historia:**
  - Par creado el 07/10/2026 11:53 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/10/2026 12:54 UTC, con el par a 60,2 min de creado: precio $0,002658, mcap $2.655.961, liquidez $145.630.
  - Velas de 1 h de GeckoTerminal (3, desde 07/10/2026 11:00 UTC): apertura $0,00004866 · máximo $0,002720 (07/10/2026 13:00 UTC) · mínimo $0,00004866 (07/10/2026 11:00 UTC) · último cierre $0,002689.
  - En la consulta 07/10/2026 13:17 UTC: precio $0,002689, liquidez $146.306, FDV $2.687.630.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/10/2026 12:54 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,002658 |
| Liquidez | $145.630 |
| MCap | $2.655.961 |
| Volumen 24 h | $64.906 |
| Cambio 24 h | +5.359% |
| Cambio m5 / h1 | -0,9% / +8,0% |
| Volumen m5 / h1 | $307 / $3.754 |
| Trades m5 (compras / ventas) | 9 / 5 |
| Edad del par | 60,2 min |
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

Desglose reconstruido desde los motivos registrados; suma 93 = score registrado 93 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $1M | $2.655.961 | +25 |
| Volumen 24 h | ≥ $50K | $64.906 | +10 |
| Buy pressure m5 | > 60% (par maduro) | 64% | +25 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,2 min | +8 |
| Liquidez | ≥ $100K | $145.630 | +15 |
| Cambio 24 h | ≥ +50% | +5.359% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +5.359% · liq/mcap 5,5% | +0 |
| **Total** | recortado a 0–100 |  | **93** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-07T12:54:01+00:00, sin estado previo): **93** · motivos: MCap > $1M, Volumen decente, Buy pressure >60%, Edge temprano (<4h), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=5.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 29 de 18.646 tokens analizados (0,16%) quedan ≥ 56. Con score 93, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/10/2026 12:54 UTC, hasta 09/10/2026 12:54 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 -0,9% · h1 +8,0% · h24 +5.359% · volumen m5/h1 0,08 · edad del par 60,2 min.
- **Precio de entrada** (alerta): $0,002658.
- **Consulta 07/10/2026 13:17 UTC:** $0,002689 (+1,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump_2026-10-07_125401.json` · blob `0e5e6b0c176b9151578558088e7915294459634d` · commit `0a5c6a9` (2026-10-07T13:08:26Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-07_125401`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump · registro · 07/10/2026 12:54 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump · HTTP 200 · 07/10/2026 13:17 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump/report · HTTP 200 · 07/10/2026 13:17 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump · HTTP 200 · 07/10/2026 13:17 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DNGD1SwQU8CkXaQGQCxmPErTf9XwgQ36zu38gHbtzynC/ohlcv/hour?limit=1000 · HTTP 200 · 07/10/2026 13:17 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump · HTTP 404 · 07/10/2026 13:17 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=WOSEUSDT · HTTP 400 · 07/10/2026 13:17 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/WOSE-USD · HTTP 404 · 07/10/2026 13:17 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $146.306 vs $146.487 → 0,12%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002689 vs $0,002689 → 0,01%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump_2026-10-07_125401.json',encoding='utf-8'));d=d.get('EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump',d);p=mock.patch('time.time',return_value=1791377641);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint EgSbbWBKhMMT1Eq43oahS6tg7vVEAqbbniNEDGmUpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/10/2026 13:17 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `62bb7fcdfa0a8db1…`
