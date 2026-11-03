# 1win Token (1WIN) — dossier

🎴 n/d en Solana · precio $0,06674 · liquidez $1.133.099 · mcap $17.821.214 (al detectar)  
Detectado el 03/11/2026 12:39 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 99, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 05/11/2026 12:39 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir 1WIN

Estudio de cómo se adquiere 1WIN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **meteora**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 03/11/2026 12:39 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 03/11/2026 12:39 UTC | meteora `3Uq381E…vLeK` | $1.133.099 | 1% | 0,018% | 0,177% | 1,765% | $5.665 | $16.996 |
| consulta 03/11/2026 12:39 UTC | meteora `3Uq381E…vLeK` | $1.133.465 | 1% | 0,018% | 0,176% | 1,765% | $5.667 | $17.002 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en meteora
4. Pegar el mint y verificar que coincide carácter por carácter: `FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win`
5. Configurar el slippage: 1% (liquidez $1.133.465, consulta 03/11/2026 12:39 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win) y el par en DexScreener (https://dexscreener.com/solana/3Uq381E8SfUit1AG5zXMQC9VmjJJJDMzenPm26DkvLeK); mint authority / freeze authority: revocada / revocada · holders 8.058 · top-10 83,81% (consulta 03/11/2026 12:39 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win
- Par en DexScreener: https://dexscreener.com/solana/3Uq381E8SfUit1AG5zXMQC9VmjJJJDMzenPm26DkvLeK
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 8.058 · top-10 83,81% (consulta 03/11/2026 12:39 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | 1win Token / 1WIN | registro de la detección (trending) |
| Mint / contrato | `FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win` | registro de la detección |
| Chain / DEX / par | Solana / meteora / `3Uq381E8SfUit1AG5zXMQC9VmjJJJDMzenPm26DkvLeK` | DexScreener, al detectar (23 par(es) en la consulta 03/11/2026 12:39 UTC) |
| Deployer | `4K5xxirCw8WD5uKGcu5kP3qdh5ZkBanNbm6BVoKD8vcf` | RugCheck `creator` |
| Par creado | 02/11/2026 20:53 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 15,8 h / 15,8 h / 15,8 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 03/11/2026 12:39 UTC |
| Holders / top-10 | 8.058 / 83,81% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 03/11/2026 12:39 UTC |
| Holders efectivos del top-10 | 5,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; raydium_clmm 74%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; raydium_clmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteoraDlmm 0%; meteora_damm_v2 0%; orca 0%; meteoraDlmm 0%; meteoraDlmm 0%; orca 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; orca 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 03/11/2026 12:39 UTC |
| Etiquetas de RugCheck | «Top 10 holders high ownership», «Single holder ownership», «High ownership», «Mutable metadata» | RugCheck `risks[].name` (texto de la fuente), consulta 03/11/2026 12:39 UTC |
| Links | DexScreener: https://dexscreener.com/solana/3Uq381E8SfUit1AG5zXMQC9VmjJJJDMzenPm26DkvLeK · Solscan: https://solscan.io/token/FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win · web: https://1wintoken.com · web: https://1win-tokenomics.gitbook.io/1win-token-litepaper · twitter: https://x.com/1winToken · telegram: https://t.me/token_1win | consulta 03/11/2026 12:39 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** n/d
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 03/11/2026 12:39 UTC)
- **Historia:**
  - Par creado el 02/11/2026 20:53 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 03/11/2026 12:39 UTC, con el par a 15,8 h de creado: precio $0,06674, mcap $17.821.214, liquidez $1.133.099.
  - Velas de 1 h de GeckoTerminal (17, desde 02/11/2026 20:00 UTC): apertura $0,03329 · máximo $0,09103 (02/11/2026 21:00 UTC) · mínimo $0,03329 (02/11/2026 20:00 UTC) · último cierre $0,06656.
  - En la consulta 03/11/2026 12:39 UTC: precio $0,06678, liquidez $1.133.465, FDV $66.789.246.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 03/11/2026 12:39 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,06674 |
| Liquidez | $1.133.099 |
| MCap | $17.821.214 |
| Volumen 24 h | $3.001.175 |
| Cambio 24 h | +100% |
| Cambio m5 / h1 | -1,4% / -1,9% |
| Volumen m5 / h1 | $21.569 / $359.111 |
| Trades m5 (compras / ventas) | 10 / 13 |
| Edad del par | 15,8 h |
| Score del feed (WS) | 66 |

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
| Score del feed | score WS × 0,3 | WS 66 × 0,3 | +19,7 |
| MCap | ≥ $1M | $17.821.214 | +25 |
| Volumen 24 h | ≥ $1M | $3.001.175 | +20 |
| Volumen m5 | > $1K (par maduro) | $21.569 | +10 |
| Liquidez | ≥ $100K | $1.133.099 | +15 |
| Cambio 24 h | ≥ +50% | +100% | +10 |
| **Total** | recortado a 0–100 |  | **99** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-03T12:39:05+00:00, sin estado previo): **99** · motivos: WS score alto, MCap > $1M, Volumen masivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 88 de 46.585 tokens analizados (0,19%) quedan ≥ 56. Con score 99, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 03/11/2026 12:39 UTC, hasta 05/11/2026 12:39 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -1,4% · h1 -1,9% · h24 +100% · volumen m5/h1 0,06 · edad del par 15,8 h.
- **Precio de entrada** (alerta): $0,06674.
- **Consulta 03/11/2026 12:39 UTC:** $0,06678 (+0,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win_2026-11-03_123929.json` · blob `86fabe63f7ca10f6af9745cbc383151e8a13b897` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-03_123402.json` · blob `d7deb0ab3082b3dfd233f535471f7ec141218a86` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-03_123929`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win · registro · 03/11/2026 12:39 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win · HTTP 200 · 03/11/2026 12:39 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win/report · HTTP 200 · 03/11/2026 12:39 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win · HTTP 200 · 03/11/2026 12:39 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/3Uq381E8SfUit1AG5zXMQC9VmjJJJDMzenPm26DkvLeK/ohlcv/hour?limit=1000 · HTTP 200 · 03/11/2026 12:39 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win · HTTP 404 · 03/11/2026 12:39 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=1WINUSDT · HTTP 400 · 03/11/2026 12:39 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/1WIN-USD · HTTP 404 · 03/11/2026 12:39 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.133.465 vs $354.522 → 68,72%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,06678 vs $0,06656 → 0,33%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win_2026-11-03_123929.json',encoding='utf-8'));d=d.get('FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win',d);p=mock.patch('time.time',return_value=1793709545);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 03/11/2026 12:39 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `326e794dab693cb5…`
