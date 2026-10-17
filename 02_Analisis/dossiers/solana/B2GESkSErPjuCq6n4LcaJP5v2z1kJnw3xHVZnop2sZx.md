# Elon Coin (ELON) — dossier

🎴 n/d en Solana · precio $0,001999 · liquidez $139.660 · mcap $1.999.616 (al detectar)  
Detectado el 17/10/2026 15:49 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 99, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 19/10/2026 15:49 UTC (< 48 h) · vigente: quedan 47,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ELON

Estudio de cómo se adquiere ELON, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **raydium**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 17/10/2026 16:50 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 17/10/2026 15:49 UTC | raydium `CnHqem7…b7zf` | $139.660 | 5% | 0,143% | 1,432% | 14,320% | $698 | $2.095 |
| consulta 17/10/2026 16:50 UTC | raydium `CnHqem7…b7zf` | $141.869 | 5% | 0,141% | 1,410% | 14,097% | $709 | $2.128 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en raydium
4. Pegar el mint y verificar que coincide carácter por carácter: `B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx`
5. Configurar el slippage: 5% (liquidez $141.869, consulta 17/10/2026 16:50 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx) y el par en DexScreener (https://dexscreener.com/solana/CnHqem7jPbjA5p2xHBGPHQG7E9NkZWcQr9q6R9YWb7zf); mint authority / freeze authority: revocada / revocada · holders 9.914 · top-10 26,02% (consulta 17/10/2026 16:50 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx
- Par en DexScreener: https://dexscreener.com/solana/CnHqem7jPbjA5p2xHBGPHQG7E9NkZWcQr9q6R9YWb7zf
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 9.914 · top-10 26,02% (consulta 17/10/2026 16:50 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Elon Coin / ELON | registro de la detección (trending) |
| Mint / contrato | `B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx` | registro de la detección |
| Chain / DEX / par | Solana / raydium / `CnHqem7jPbjA5p2xHBGPHQG7E9NkZWcQr9q6R9YWb7zf` | DexScreener, al detectar (14 par(es) en la consulta 17/10/2026 16:50 UTC) |
| Deployer | n/d | n/d (fuente: RugCheck `creator`) |
| Par creado | 16/10/2026 17:30 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 22,3 h / 22,3 h / 23,3 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 17/10/2026 16:50 UTC |
| Holders / top-10 | 9.914 / 26,02% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 17/10/2026 16:50 UTC |
| Holders efectivos del top-10 | 9,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | raydium_cpmm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 17/10/2026 16:50 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 17/10/2026 16:50 UTC |
| Links | DexScreener: https://dexscreener.com/solana/CnHqem7jPbjA5p2xHBGPHQG7E9NkZWcQr9q6R9YWb7zf · Solscan: https://solscan.io/token/B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx · twitter: https://x.com/search?q=$ELON | consulta 17/10/2026 16:50 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** n/d
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 17/10/2026 16:50 UTC)
- **Historia:**
  - Par creado el 16/10/2026 17:30 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 17/10/2026 15:49 UTC, con el par a 22,3 h de creado: precio $0,001999, mcap $1.999.616, liquidez $139.660.
  - Velas de 1 h de GeckoTerminal (24, desde 16/10/2026 17:00 UTC): apertura $0,00005083 · máximo $0,002618 (17/10/2026 14:00 UTC) · mínimo $0,00004511 (16/10/2026 17:00 UTC) · último cierre $0,002006.
  - En la consulta 17/10/2026 16:50 UTC: precio $0,002076, liquidez $141.869, FDV $2.076.165.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 17/10/2026 15:49 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001999 |
| Liquidez | $139.660 |
| MCap | $1.999.616 |
| Volumen 24 h | $5.207.372 |
| Cambio 24 h | +4.340% |
| Cambio m5 / h1 | -0,0% / +5,1% |
| Volumen m5 / h1 | $12.484 / $602.628 |
| Trades m5 (compras / ventas) | 80 / 102 |
| Edad del par | 22,3 h |
| Score del feed (WS) | 65 |

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

Desglose reconstruido desde los motivos registrados; suma 99 = score registrado 99 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 65 × 0,3 | +19,6 |
| MCap | ≥ $1M | $1.999.616 | +25 |
| Volumen 24 h | ≥ $1M | $5.207.372 | +20 |
| Volumen m5 | > $1K (par maduro) | $12.484 | +10 |
| Liquidez | ≥ $100K | $139.660 | +15 |
| Cambio 24 h | ≥ +50% | +4.340% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +4.340% · liq/mcap 7,0% | +0 |
| **Total** | recortado a 0–100 |  | **99** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-17T15:49:04+00:00, sin estado previo): **99** · motivos: WS score alto, MCap > $1M, Volumen masivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=7.0% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 64 de 38.586 tokens analizados (0,17%) quedan ≥ 56. Con score 99, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 17/10/2026 15:49 UTC, hasta 19/10/2026 15:49 UTC · vigente: quedan 47,0 h.
- **Aceleración al detectar:** cambio m5 -0,0% · h1 +5,1% · h24 +4.340% · volumen m5/h1 0,02 · edad del par 22,3 h.
- **Precio de entrada** (alerta): $0,001999.
- **Consulta 17/10/2026 16:50 UTC:** $0,002076 (+3,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx_2026-10-17_154904.json` · blob `c8361a38d729d4053614ad4460d43c60ba9b4483` · commit `34c9424` (2026-10-17T16:43:35Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-17_154247.json` · blob `492975649012ff2ab4f7ec1f66dcdf9c50822f72` · commit `34c9424` (2026-10-17T16:43:35Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-17_154904`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx · registro · 17/10/2026 15:49 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx · HTTP 200 · 17/10/2026 16:50 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx/report · HTTP 200 · 17/10/2026 16:50 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx · HTTP 200 · 17/10/2026 16:50 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/CnHqem7jPbjA5p2xHBGPHQG7E9NkZWcQr9q6R9YWb7zf/ohlcv/hour?limit=1000 · HTTP 200 · 17/10/2026 16:50 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx · HTTP 404 · 17/10/2026 16:50 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ELONUSDT · HTTP 400 · 17/10/2026 16:50 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ELON-USD · HTTP 404 · 17/10/2026 16:50 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $141.869 vs $170.214 → 16,65%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002076 vs $0,002006 → 3,37%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx_2026-10-17_154904.json',encoding='utf-8'));d=d.get('B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx',d);p=mock.patch('time.time',return_value=1792252144);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint B2GESkSErPjuCq6n4LcaJP5v2z1kJnw3xHVZnop2sZx --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 17/10/2026 16:50 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `11a5314237f853c1…`
