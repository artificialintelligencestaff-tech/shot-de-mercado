# Ripple USD (RLUSD) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,008114 · liquidez $258.159 · mcap $8.114.797 (al detectar)  
Detectado el 02/10/2026 23:21 UTC por: MCap > $1M, Volumen alto, Liquidez alta (score 65, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 04/10/2026 23:21 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir RLUSD

Estudio de cómo se adquiere RLUSD, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 23:33 UTC; CoinGecko sin ficha para este contrato). Binance tiene un par RLUSDUSDT, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza.

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 23:21 UTC | pumpswap `DCgDEd8…Xoy8` | $258.159 | 3% | 0,077% | 0,775% | 7,747% | $1.291 | $3.872 |
| consulta 02/10/2026 23:33 UTC | pumpswap `DCgDEd8…Xoy8` | $258.902 | 3% | 0,077% | 0,772% | 7,725% | $1.295 | $3.884 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump`
5. Configurar el slippage: 3% (liquidez $258.902, consulta 02/10/2026 23:33 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump) y el par en DexScreener (https://dexscreener.com/solana/DCgDEd8WYCaeMuCTHkChpwaAJruam1ymihL3oPCNXoy8); mint authority / freeze authority: revocada / revocada · holders 2.018 · top-10 3,84% (consulta 02/10/2026 23:33 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump
- Par en DexScreener: https://dexscreener.com/solana/DCgDEd8WYCaeMuCTHkChpwaAJruam1ymihL3oPCNXoy8
- Página del lanzamiento (pump.fun): https://pump.fun/coin/G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.018 · top-10 3,84% (consulta 02/10/2026 23:33 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Ripple USD / RLUSD | registro de la detección (pumpportal_live) |
| Mint / contrato | `G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DCgDEd8WYCaeMuCTHkChpwaAJruam1ymihL3oPCNXoy8` | DexScreener, al detectar (2 par(es) en la consulta 02/10/2026 23:33 UTC) |
| Deployer | `7mDqSknHavV7NC277c3XHemPoQ8zAbGuFZScBxnuRfsD` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 23:10 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,2 min / 11,2 min / 23,0 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 23:33 UTC |
| Holders / top-10 | 2.018 / 3,84% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 23:33 UTC |
| Holders efectivos del top-10 | 4,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 23:33 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 23:33 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DCgDEd8WYCaeMuCTHkChpwaAJruam1ymihL3oPCNXoy8 · Solscan: https://solscan.io/token/G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump · pump.fun: https://pump.fun/coin/G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump · web / Telegram / X: no publicados en DexScreener | consulta 02/10/2026 23:33 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 23:33 UTC)
- **Historia:**
  - Par creado el 02/10/2026 23:10 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 23:21 UTC, con el par a 11,2 min de creado: precio $0,008114, mcap $8.114.797, liquidez $258.159.
  - Velas de 1 h de GeckoTerminal (1, desde 02/10/2026 23:00 UTC): apertura $0,0006218 · máximo $0,008155 (02/10/2026 23:00 UTC) · mínimo $0,00004919 (02/10/2026 23:00 UTC) · último cierre $0,008148.
  - En la consulta 02/10/2026 23:33 UTC: precio $0,008154, liquidez $258.902, FDV $8.154.178.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 23:21 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,008114 |
| Liquidez | $258.159 |
| MCap | $8.114.797 |
| Volumen 24 h | $120.633 |
| Cambio 24 h | +16.381% |
| Cambio m5 / h1 | +0,5% / +16.381,0% |
| Volumen m5 / h1 | $977 / $120.633 |
| Trades m5 (compras / ventas) | 487 / 13 |
| Edad del par | 11,2 min |
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

Desglose reconstruido desde los motivos registrados; suma 65 = score registrado 65 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| Gate de edad v7.2.1 | edad < 60 min o desconocida: sin bonos temporales | edad 11,2 min | +0 |
| MCap | ≥ $1M | $8.114.797 | +25 |
| Volumen 24 h | ≥ $100K | $120.633 | +15 |
| Liquidez | ≥ $100K | $258.159 | +15 |
| Cambio 24 h | ≥ +50% | +16.381% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +16.381% · liq/mcap 3,2% | +0 |
| **Total** | recortado a 0–100 |  | **65** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T23:21:53+00:00, sin estado previo): **65** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen alto, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=3.2% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 11 de 9.152 tokens analizados (0,12%) quedan ≥ 56. Con score 65, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 23:21 UTC, hasta 04/10/2026 23:21 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +0,5% · h1 +16.381,0% · h24 +16.381% · volumen m5/h1 0,01 · edad del par 11,2 min.
- **Precio de entrada** (alerta): $0,008114.
- **Consulta 02/10/2026 23:33 UTC:** $0,008154 (+0,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump_2026-10-02_232153.json` · blob `0febd14c55620414d2de64fae7ff84d84953fc3e` · commit `00f2835` (2026-10-02T23:26:32Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_232153`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump · registro · 02/10/2026 23:21 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump · HTTP 200 · 02/10/2026 23:33 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump/report · HTTP 200 · 02/10/2026 23:33 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump · HTTP 200 · 02/10/2026 23:33 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DCgDEd8WYCaeMuCTHkChpwaAJruam1ymihL3oPCNXoy8/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 23:33 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump · HTTP 404 · 02/10/2026 23:33 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=RLUSDUSDT · HTTP 200 · 02/10/2026 23:33 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/RLUSD-USD · HTTP 404 · 02/10/2026 23:33 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $258.902 vs $258.924 → 0,01%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,008154 vs $0,008148 → 0,07%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump_2026-10-02_232153.json',encoding='utf-8'));d=d.get('G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump',d);p=mock.patch('time.time',return_value=1790983313);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint G8L269Ev4mdS3PJGUBQJVpVHjyzKANrCasC7HRppump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 23:33 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `76e0b4688bf0c97b…`
