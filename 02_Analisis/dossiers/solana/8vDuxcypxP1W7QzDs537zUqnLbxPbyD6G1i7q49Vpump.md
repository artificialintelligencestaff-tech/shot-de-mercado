# XMAN (XMAN) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000002851 · liquidez $3.327 · mcap $2.791 (al detectar)  
Detectado el 05/10/2026 23:34 UTC por: WS score muy alto, MCap bajo, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 07/10/2026 23:34 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir XMAN

Estudio de cómo se adquiere XMAN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 05/10/2026 23:52 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 05/10/2026 23:34 UTC | pumpswap `CAgJ6EZ…8zUQ` | $3.327 | 10% | 6,011% | 60,106% | 601,061% | $17 | $50 |
| consulta 05/10/2026 23:51 UTC | pumpswap `CAgJ6EZ…8zUQ` | $3.327 | 10% | 6,011% | 60,106% | 601,061% | $17 | $50 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump`
5. Configurar el slippage: 10% (liquidez $3.327, consulta 05/10/2026 23:51 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump) y el par en DexScreener (https://dexscreener.com/solana/CAgJ6EZgBTAgh6NLMgunPkxJ81zWrVoNWfHJi87U8zUQ); mint authority / freeze authority: revocada / revocada · holders 240 · top-10 99,07% (consulta 05/10/2026 23:51 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump
- Par en DexScreener: https://dexscreener.com/solana/CAgJ6EZgBTAgh6NLMgunPkxJ81zWrVoNWfHJi87U8zUQ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 240 · top-10 99,07% (consulta 05/10/2026 23:51 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | XMAN / XMAN | registro de la detección (trending) |
| Mint / contrato | `8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `CAgJ6EZgBTAgh6NLMgunPkxJ81zWrVoNWfHJi87U8zUQ` | DexScreener, al detectar (2 par(es) en la consulta 05/10/2026 23:51 UTC) |
| Deployer | `BwsWYkNcXK1RTRhSgttVFKrMKMpRbTfnfEvbXVbzXZZJ` | RugCheck `creator` |
| Par creado | 05/10/2026 04:22 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 19,2 h / 19,2 h / 19,5 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 05/10/2026 23:51 UTC |
| Holders / top-10 | 240 / 99,07% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 05/10/2026 23:51 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 05/10/2026 23:51 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 05/10/2026 23:51 UTC |
| Links | DexScreener: https://dexscreener.com/solana/CAgJ6EZgBTAgh6NLMgunPkxJ81zWrVoNWfHJi87U8zUQ · Solscan: https://solscan.io/token/8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump · pump.fun: https://pump.fun/coin/8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump · web: https://xman.lol · twitter: https://x.com/xmanonsol · telegram: https://t.me/xmanonsol | consulta 05/10/2026 23:51 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 05/10/2026 23:51 UTC)
- **Historia:**
  - Par creado el 05/10/2026 04:22 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 05/10/2026 23:34 UTC, con el par a 19,2 h de creado: precio $0,000002851, mcap $2.791, liquidez $3.327.
  - Velas de 1 h de GeckoTerminal (16, desde 05/10/2026 04:00 UTC): apertura $0,00009560 · máximo $0,0009269 (05/10/2026 05:00 UTC) · mínimo $0,000002663 (05/10/2026 16:00 UTC) · último cierre $0,000002849.
  - En la consulta 05/10/2026 23:51 UTC: precio $0,000002851, liquidez $3.327, FDV $2.791.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 05/10/2026 23:34 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000002851 |
| Liquidez | $3.327 |
| MCap | $2.791 |
| Volumen 24 h | $2.240.063 |
| Cambio 24 h | -97% |
| Cambio m5 / h1 | +0,2% / +0,2% |
| Volumen m5 / h1 | $3 / $3 |
| Trades m5 (compras / ventas) | 1 / 0 |
| Edad del par | 19,2 h |
| Score del feed (WS) | 80 |

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
| Score del feed | score WS × 0,3 | WS 80 × 0,3 | +24,0 |
| MCap | < $50K | $2.791 | +0 |
| Volumen 24 h | ≥ $1M | $2.240.063 | +20 |
| Volumen m5/h1 | > 0,5 (par maduro) | 1,00 | +25 |
| Trades m5/h1 | > 0,5 (par maduro) | 1,00 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 100% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,2% · h1 +0,2% | +20 |
| Liquidez | < $20K | $3.327 | +0 |
| Cambio 24 h | ≤ −30% | -97% | -5 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-05T23:34:48+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap bajo, Volumen masivo, Volumen acelerado (5m/1h > 50%), Trades acelerados (5m/1h > 50%), Buy pressure >60%, Momentum corto+medio positivo, Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 17 de 13.583 tokens analizados (0,13%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 05/10/2026 23:34 UTC, hasta 07/10/2026 23:34 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +0,2% · h1 +0,2% · h24 -97% · volumen m5/h1 1,00 · edad del par 19,2 h.
- **Precio de entrada** (alerta): $0,000002851.
- **Consulta 05/10/2026 23:51 UTC:** $0,000002851 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump_2026-10-05_233448.json` · blob `67ee1b8e27f4f97196f6777d19a5f62c60607315` · commit `42de4b7` (2026-10-05T23:45:35Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-05_232819.json` · blob `d9ab2ac76858693392f4fa367b51df02e58c3ca6` · commit `42de4b7` (2026-10-05T23:45:35Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-05_233448`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump · registro · 05/10/2026 23:34 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump · HTTP 200 · 05/10/2026 23:51 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump/report · HTTP 200 · 05/10/2026 23:51 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump · HTTP 200 · 05/10/2026 23:51 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/CAgJ6EZgBTAgh6NLMgunPkxJ81zWrVoNWfHJi87U8zUQ/ohlcv/hour?limit=1000 · HTTP 200 · 05/10/2026 23:51 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump · HTTP 404 · 05/10/2026 23:51 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=XMANUSDT · HTTP 400 · 05/10/2026 23:51 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/XMAN-USD · HTTP 404 · 05/10/2026 23:51 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.327 vs $3.328 → 0,03%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002851 vs $0,000002849 → 0,06%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump_2026-10-05_233448.json',encoding='utf-8'));d=d.get('8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump',d);p=mock.patch('time.time',return_value=1791243288);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8vDuxcypxP1W7QzDs537zUqnLbxPbyD6G1i7q49Vpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 05/10/2026 23:52 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `b32e85da59b7a5bb…`
