# MAMESUKE (MAMESUKE) — dossier

🎴 n/d en Solana · precio $0,0008147 · liquidez $168.322 · mcap $814.722 (al detectar)  
Detectado el 02/11/2026 23:59 UTC por: WS score alto, MCap > $100K, Volumen alto (score 86, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 04/11/2026 23:59 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir MAMESUKE

Estudio de cómo se adquiere MAMESUKE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **meteora**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 03/11/2026 00:00 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/11/2026 23:59 UTC | meteora `fMKswmD…tc7A` | $168.322 | 5% | 0,119% | 1,188% | 11,882% | $842 | $2.525 |
| consulta 02/11/2026 23:59 UTC | meteora `fMKswmD…tc7A` | $170.090 | 5% | 0,118% | 1,176% | 11,758% | $850 | $2.551 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en meteora
4. Pegar el mint y verificar que coincide carácter por carácter: `SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK`
5. Configurar el slippage: 5% (liquidez $170.090, consulta 02/11/2026 23:59 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK) y el par en DexScreener (https://dexscreener.com/solana/fMKswmDKwstG3jm6V5PKeXE5LkcW3ny84QrhDCKtc7A); mint authority / freeze authority: revocada / revocada · holders 11.707 · top-10 34,78% (consulta 02/11/2026 23:59 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK
- Par en DexScreener: https://dexscreener.com/solana/fMKswmDKwstG3jm6V5PKeXE5LkcW3ny84QrhDCKtc7A
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 11.707 · top-10 34,78% (consulta 02/11/2026 23:59 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | MAMESUKE / MAMESUKE | registro de la detección (trending) |
| Mint / contrato | `SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK` | registro de la detección |
| Chain / DEX / par | Solana / meteora / `fMKswmDKwstG3jm6V5PKeXE5LkcW3ny84QrhDCKtc7A` | DexScreener, al detectar (12 par(es) en la consulta 02/11/2026 23:59 UTC) |
| Deployer | n/d | n/d (fuente: RugCheck `creator`) |
| Par creado | 02/11/2026 11:41 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 12,3 h / 12,3 h / 12,3 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/11/2026 23:59 UTC |
| Holders / top-10 | 11.707 / 34,78% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/11/2026 23:59 UTC |
| Holders efectivos del top-10 | 2,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | meteoraDlmm 0%; raydium_cpmm 100%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; manifest 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/11/2026 23:59 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 02/11/2026 23:59 UTC |
| Links | DexScreener: https://dexscreener.com/solana/fMKswmDKwstG3jm6V5PKeXE5LkcW3ny84QrhDCKtc7A · Solscan: https://solscan.io/token/SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK · web: https://themamesuke.com/ · twitter: https://x.com/mamesukeshow · telegram: https://t.me/mamesukeTG | consulta 02/11/2026 23:59 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** n/d
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/11/2026 23:59 UTC)
- **Historia:**
  - Par creado el 02/11/2026 11:41 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/11/2026 23:59 UTC, con el par a 12,3 h de creado: precio $0,0008147, mcap $814.722, liquidez $168.322.
  - Velas de 1 h de GeckoTerminal (13, desde 02/11/2026 11:00 UTC): apertura $0,0002348 · máximo $0,002023 (02/11/2026 18:00 UTC) · mínimo $0,0001659 (02/11/2026 11:00 UTC) · último cierre $0,0008144.
  - En la consulta 02/11/2026 23:59 UTC: precio $0,0008147, liquidez $170.090, FDV $814.725.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/11/2026 23:59 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0008147 |
| Liquidez | $168.322 |
| MCap | $814.722 |
| Volumen 24 h | $752.836 |
| Cambio 24 h | +240% |
| Cambio m5 / h1 | -7,2% / -4,7% |
| Volumen m5 / h1 | $1.235 / $16.798 |
| Trades m5 (compras / ventas) | 2 / 2 |
| Edad del par | 12,3 h |
| Score del feed (WS) | 71 |

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

Desglose reconstruido desde los motivos registrados; suma 86 = score registrado 86 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 71 × 0,3 | +21,3 |
| MCap | ≥ $100K | $814.722 | +15 |
| Volumen 24 h | ≥ $100K | $752.836 | +15 |
| Volumen m5 | > $1K (par maduro) | $1.235 | +10 |
| Liquidez | ≥ $100K | $168.322 | +15 |
| Cambio 24 h | ≥ +50% | +240% | +10 |
| **Total** | recortado a 0–100 |  | **86** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-02T23:59:31+00:00, sin estado previo): **86** · motivos: WS score alto, MCap > $100K, Volumen alto, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 87 de 46.541 tokens analizados (0,19%) quedan ≥ 56. Con score 86, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/11/2026 23:59 UTC, hasta 04/11/2026 23:59 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -7,2% · h1 -4,7% · h24 +240% · volumen m5/h1 0,07 · edad del par 12,3 h.
- **Precio de entrada** (alerta): $0,0008147.
- **Consulta 02/11/2026 23:59 UTC:** $0,0008147 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK_2026-11-02_235956.json` · blob `7dd5abaf8cae7f9832ea858c6d293799c7a4967e` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-02_235425.json` · blob `482d9ff4a373d233fc09a454d918d226a77da77f` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-02_235956`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK · registro · 02/11/2026 23:59 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK · HTTP 200 · 02/11/2026 23:59 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK/report · HTTP 200 · 02/11/2026 23:59 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK · HTTP 200 · 03/11/2026 00:00 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/fMKswmDKwstG3jm6V5PKeXE5LkcW3ny84QrhDCKtc7A/ohlcv/hour?limit=1000 · HTTP 200 · 03/11/2026 00:00 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK · HTTP 404 · 03/11/2026 00:00 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MAMESUKEUSDT · HTTP 400 · 03/11/2026 00:00 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MAMESUKE-USD · HTTP 404 · 03/11/2026 00:00 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $170.090 vs $268.602 → 36,68%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0008147 vs $0,0008144 → 0,04%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK_2026-11-02_235956.json',encoding='utf-8'));d=d.get('SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK',d);p=mock.patch('time.time',return_value=1793663971);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 03/11/2026 00:00 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `ea01ed7491950d13…`
