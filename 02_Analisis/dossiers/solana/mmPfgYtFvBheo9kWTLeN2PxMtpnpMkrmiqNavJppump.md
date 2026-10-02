# NTDA (NTDA) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,005770 · liquidez $219.300 · mcap $5.770.002 (al detectar)  
Detectado el 02/10/2026 14:59 UTC por: MCap > $1M, Volumen alto, Liquidez alta (score 65, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 04/10/2026 14:59 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir NTDA

Estudio de cómo se adquiere NTDA, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 15:13 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 14:59 UTC | pumpswap `C39ymwJ…1Den` | $219.300 | 5% | 0,091% | 0,912% | 9,120% | $1.097 | $3.290 |
| consulta 02/10/2026 15:13 UTC | pumpswap `C39ymwJ…1Den` | $217.928 | 5% | 0,092% | 0,918% | 9,177% | $1.090 | $3.269 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump`
5. Configurar el slippage: 5% (liquidez $217.928, consulta 02/10/2026 15:13 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump) y el par en DexScreener (https://dexscreener.com/solana/C39ymwJqRbkwZaHuerFdvKVMi2AN4Sy4HynMAEs31Den); mint authority / freeze authority: revocada / revocada · holders 3.804 · top-10 10,74% (consulta 02/10/2026 15:13 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump
- Par en DexScreener: https://dexscreener.com/solana/C39ymwJqRbkwZaHuerFdvKVMi2AN4Sy4HynMAEs31Den
- Página del lanzamiento (pump.fun): https://pump.fun/coin/mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.804 · top-10 10,74% (consulta 02/10/2026 15:13 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | NTDA / NTDA | registro de la detección (pumpportal_live) |
| Mint / contrato | `mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `C39ymwJqRbkwZaHuerFdvKVMi2AN4Sy4HynMAEs31Den` | DexScreener, al detectar (2 par(es) en la consulta 02/10/2026 15:13 UTC) |
| Deployer | `hed5R9ore54QTN5DaeQqTdoS22THqgVcPmyjYLj7aRv` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 14:48 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,9 min / 10,9 min / 25,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 15:13 UTC |
| Holders / top-10 | 3.804 / 10,74% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 15:13 UTC |
| Holders efectivos del top-10 | 9,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 15:13 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 15:13 UTC |
| Links | DexScreener: https://dexscreener.com/solana/C39ymwJqRbkwZaHuerFdvKVMi2AN4Sy4HynMAEs31Den · Solscan: https://solscan.io/token/mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump · pump.fun: https://pump.fun/coin/mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump · web / Telegram / X: no publicados en DexScreener | consulta 02/10/2026 15:13 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 15:13 UTC)
- **Historia:**
  - Par creado el 02/10/2026 14:48 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 14:59 UTC, con el par a 10,9 min de creado: precio $0,005770, mcap $5.770.002, liquidez $219.300.
  - Velas de 1 h de GeckoTerminal (2, desde 02/10/2026 14:00 UTC): apertura $0,005583 · máximo $0,005782 (02/10/2026 15:00 UTC) · mínimo $0,00005051 (02/10/2026 14:00 UTC) · último cierre $0,005753.
  - En la consulta 02/10/2026 15:13 UTC: precio $0,005717, liquidez $217.928, FDV $5.717.540.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 14:59 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,005770 |
| Liquidez | $219.300 |
| MCap | $5.770.002 |
| Volumen 24 h | $100.019 |
| Cambio 24 h | +11.331% |
| Cambio m5 / h1 | +0,5% / +11.331,0% |
| Volumen m5 / h1 | $243 / $100.019 |
| Trades m5 (compras / ventas) | 8 / 6 |
| Edad del par | 10,9 min |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 1/2 (50,0%, IC90 12,1%–87,9%) · secundaria 0/1 resueltas (shadow_monitor.json).

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
| Gate de edad v7.2.1 | edad < 60 min o desconocida: sin bonos temporales | edad 10,9 min | +0 |
| MCap | ≥ $1M | $5.770.002 | +25 |
| Volumen 24 h | ≥ $100K | $100.019 | +15 |
| Liquidez | ≥ $100K | $219.300 | +15 |
| Cambio 24 h | ≥ +50% | +11.331% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +11.331% · liq/mcap 3,8% | +0 |
| **Total** | recortado a 0–100 |  | **65** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T14:59:14+00:00, sin estado previo): **65** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen alto, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=3.8% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 10 de 7.878 tokens analizados (0,13%) quedan ≥ 56. Con score 65, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 14:59 UTC, hasta 04/10/2026 14:59 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +0,5% · h1 +11.331,0% · h24 +11.331% · volumen m5/h1 0,00 · edad del par 10,9 min.
- **Precio de entrada** (alerta): $0,005770.
- **Consulta 02/10/2026 15:13 UTC:** $0,005717 (-0,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump_2026-10-02_145914.json` · blob `7cbc4d0c7dfbccda978c51557dcc40fd86816f3a` · commit `a38ee5a` (2026-10-02T15:04:58Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_145914`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump · registro · 02/10/2026 14:59 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump · HTTP 200 · 02/10/2026 15:13 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump/report · HTTP 200 · 02/10/2026 15:13 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump · HTTP 200 · 02/10/2026 15:13 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/C39ymwJqRbkwZaHuerFdvKVMi2AN4Sy4HynMAEs31Den/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 15:13 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump · HTTP 404 · 02/10/2026 15:13 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=NTDAUSDT · HTTP 400 · 02/10/2026 15:13 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/NTDA-USD · HTTP 404 · 02/10/2026 15:13 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $217.928 vs $218.674 → 0,34%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,005717 vs $0,005753 → 0,62%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump_2026-10-02_145914.json',encoding='utf-8'));d=d.get('mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump',d);p=mock.patch('time.time',return_value=1790953154);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint mmPfgYtFvBheo9kWTLeN2PxMtpnpMkrmiqNavJppump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 15:13 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `5e5616af4a51af3b…`
