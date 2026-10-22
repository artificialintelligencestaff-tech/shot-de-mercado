# Moonoween (Moonoween) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,1574 · liquidez $1.070.147 · mcap $157.422.880 (al detectar)  
Detectado el 22/10/2026 18:44 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 24/10/2026 18:44 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Moonoween

Estudio de cómo se adquiere Moonoween, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 22/10/2026 19:09 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 22/10/2026 18:44 UTC | pumpswap `6gUrudc…MKmm` | $1.070.147 | 1% | 0,019% | 0,187% | 1,869% | $5.351 | $16.052 |
| consulta 22/10/2026 19:09 UTC | pumpswap `6gUrudc…MKmm` | $1.070.263 | 1% | 0,019% | 0,187% | 1,869% | $5.351 | $16.054 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump`
5. Configurar el slippage: 1% (liquidez $1.070.263, consulta 22/10/2026 19:09 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump) y el par en DexScreener (https://dexscreener.com/solana/6gUrudcuzXTTowoeL5p7z65cMK6wU6z5pyHDRNR2MKmm); mint authority / freeze authority: revocada / revocada · holders 4.044 · top-10 1,25% (consulta 22/10/2026 19:09 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump
- Par en DexScreener: https://dexscreener.com/solana/6gUrudcuzXTTowoeL5p7z65cMK6wU6z5pyHDRNR2MKmm
- Página del lanzamiento (pump.fun): https://pump.fun/coin/nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.044 · top-10 1,25% (consulta 22/10/2026 19:09 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Moonoween / Moonoween | registro de la detección (trending) |
| Mint / contrato | `nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `6gUrudcuzXTTowoeL5p7z65cMK6wU6z5pyHDRNR2MKmm` | DexScreener, al detectar (2 par(es) en la consulta 22/10/2026 19:09 UTC) |
| Deployer | `GjojLRkNvg76Me9pANSjznZXv9qmG6qUbhA2XNpGnhBp` | RugCheck `creator` |
| Par creado | 22/10/2026 17:44 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,1 min / 60,1 min / 85,3 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 22/10/2026 19:09 UTC |
| Holders / top-10 | 4.044 / 1,25% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 22/10/2026 19:09 UTC |
| Holders efectivos del top-10 | 2,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 22/10/2026 19:09 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 22/10/2026 19:09 UTC |
| Links | DexScreener: https://dexscreener.com/solana/6gUrudcuzXTTowoeL5p7z65cMK6wU6z5pyHDRNR2MKmm · Solscan: https://solscan.io/token/nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump · pump.fun: https://pump.fun/coin/nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump · web / Telegram / X: no publicados en DexScreener | consulta 22/10/2026 19:09 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 22/10/2026 19:09 UTC)
- **Historia:**
  - Par creado el 22/10/2026 17:44 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 22/10/2026 18:44 UTC, con el par a 60,1 min de creado: precio $0,1574, mcap $157.422.880, liquidez $1.070.147.
  - Velas de 1 h de GeckoTerminal (3, desde 22/10/2026 17:00 UTC): apertura $0,1553 · máximo $0,1578 (22/10/2026 18:00 UTC) · mínimo $0,00004311 (22/10/2026 17:00 UTC) · último cierre $0,1577.
  - En la consulta 22/10/2026 19:09 UTC: precio $0,1577, liquidez $1.070.263, FDV $157.727.784.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 22/10/2026 18:44 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,1574 |
| Liquidez | $1.070.147 |
| MCap | $157.422.880 |
| Volumen 24 h | $530.584 |
| Cambio 24 h | +365.353% |
| Cambio m5 / h1 | +0,5% / +365.353,0% |
| Volumen m5 / h1 | $629 / $530.584 |
| Trades m5 (compras / ventas) | 97 / 7 |
| Edad del par | 60,1 min |
| Score del feed (WS) | 100 |

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
| Score del feed | score WS × 0,3 | WS 100 × 0,3 | +30 |
| MCap | ≥ $1M | $157.422.880 | +25 |
| Volumen 24 h | ≥ $100K | $530.584 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 93% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,5% · h1 +365.353,0% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,1 min | +8 |
| Volumen m5 | > $500 (par maduro) | $629 | +5 |
| Liquidez | ≥ $100K | $1.070.147 | +15 |
| Cambio 24 h | ≥ +50% | +365.353% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +365.353% · liq/mcap 0,7% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-22T18:44:09+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 74 de 44.174 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 22/10/2026 18:44 UTC, hasta 24/10/2026 18:44 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +0,5% · h1 +365.353,0% · h24 +365.353% · volumen m5/h1 0,00 · edad del par 60,1 min.
- **Precio de entrada** (alerta): $0,1574.
- **Consulta 22/10/2026 19:09 UTC:** $0,1577 (+0,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump_2026-10-22_184409.json` · blob `078ae07344afb1c3d91b98152274584c8186f724` · commit `96b2b7c` (2026-10-22T19:02:35Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-22_174532.json` · blob `683ad95b19abd383e611541c60e9f87b431eaa01` · commit `96b2b7c` (2026-10-22T19:02:35Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-22_184409`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump · registro · 22/10/2026 18:44 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump · HTTP 200 · 22/10/2026 19:09 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump/report · HTTP 200 · 22/10/2026 19:09 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump · HTTP 200 · 22/10/2026 19:09 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/6gUrudcuzXTTowoeL5p7z65cMK6wU6z5pyHDRNR2MKmm/ohlcv/hour?limit=1000 · HTTP 200 · 22/10/2026 19:09 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump · HTTP 404 · 22/10/2026 19:09 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MOONOWEENUSDT · HTTP 400 · 22/10/2026 19:09 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MOONOWEEN-USD · HTTP 404 · 22/10/2026 19:09 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.070.263 vs $1.069.013 → 0,12%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,1577 vs $0,1577 → 0,03%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump_2026-10-22_184409.json',encoding='utf-8'));d=d.get('nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump',d);p=mock.patch('time.time',return_value=1792694649);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint nh9wgfvvgPkX69pQbGVao8dpPzmVFRuECjL6Hwhpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 22/10/2026 19:09 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `f2fc079a1ec3c216…`
