# Super Market Inu (SUPMKT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001152 · liquidez $96.622 · mcap $1.144.787 (al detectar)  
Detectado el 11/10/2026 01:39 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 13/10/2026 01:39 UTC (< 48 h) · vigente: quedan 47,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SUPMKT

Estudio de cómo se adquiere SUPMKT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/10/2026 02:12 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 11/10/2026 01:39 UTC | pumpswap `94tupYk…9mAB` | $96.622 | 5% | 0,207% | 2,070% | 20,699% | $483 | $1.449 |
| consulta 11/10/2026 02:12 UTC | pumpswap `94tupYk…9mAB` | $105.262 | 5% | 0,190% | 1,900% | 19,000% | $526 | $1.579 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump`
5. Configurar el slippage: 5% (liquidez $105.262, consulta 11/10/2026 02:12 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump) y el par en DexScreener (https://dexscreener.com/solana/94tupYk7hinha9fU2NQEkfh6jkykx88nTUbVQC2V9mAB); mint authority / freeze authority: revocada / revocada · holders 5.660 · top-10 7,22% (consulta 11/10/2026 02:12 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump
- Par en DexScreener: https://dexscreener.com/solana/94tupYk7hinha9fU2NQEkfh6jkykx88nTUbVQC2V9mAB
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.660 · top-10 7,22% (consulta 11/10/2026 02:12 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Super Market Inu / SUPMKT | registro de la detección (trending) |
| Mint / contrato | `3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `94tupYk7hinha9fU2NQEkfh6jkykx88nTUbVQC2V9mAB` | DexScreener, al detectar (8 par(es) en la consulta 11/10/2026 02:12 UTC) |
| Deployer | `24swTk2h4bQSEGCF9XANRhgXXTpUpJucktYbC3uZhG8r` | RugCheck `creator` |
| Par creado | 10/10/2026 23:26 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 2,2 h / 2,2 h / 2,8 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/10/2026 02:12 UTC |
| Holders / top-10 | 5.660 / 7,22% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/10/2026 02:12 UTC |
| Holders efectivos del top-10 | 3,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/10/2026 02:12 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 11/10/2026 02:12 UTC |
| Links | DexScreener: https://dexscreener.com/solana/94tupYk7hinha9fU2NQEkfh6jkykx88nTUbVQC2V9mAB · Solscan: https://solscan.io/token/3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump · pump.fun: https://pump.fun/coin/3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump · web: https://www.supmkt.lol · twitter: https://x.com/supmkt_meme | consulta 11/10/2026 02:12 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/10/2026 02:12 UTC)
- **Historia:**
  - Par creado el 10/10/2026 23:26 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 11/10/2026 01:39 UTC, con el par a 2,2 h de creado: precio $0,001152, mcap $1.144.787, liquidez $96.622.
  - Velas de 1 h de GeckoTerminal (4, desde 10/10/2026 23:00 UTC): apertura $0,0002781 · máximo $0,001413 (11/10/2026 02:00 UTC) · mínimo $0,00006517 (10/10/2026 23:00 UTC) · último cierre $0,001364.
  - En la consulta 11/10/2026 02:12 UTC: precio $0,001358, liquidez $105.262, FDV $1.349.139.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 11/10/2026 01:39 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001152 |
| Liquidez | $96.622 |
| MCap | $1.144.787 |
| Volumen 24 h | $1.222.634 |
| Cambio 24 h | +1.667% |
| Cambio m5 / h1 | -0,4% / +95,9% |
| Volumen m5 / h1 | $22.848 / $391.881 |
| Trades m5 (compras / ventas) | 318 / 158 |
| Edad del par | 2,2 h |
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
| Score del feed | score WS × 0,3 | WS 80 × 0,3 | +24,1 |
| MCap | ≥ $1M | $1.144.787 | +25 |
| Volumen 24 h | ≥ $1M | $1.222.634 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 67% | +25 |
| Edge temprano | edad < 4 h (par maduro) | edad 2,2 h | +8 |
| Volumen m5 | > $1K (par maduro) | $22.848 | +10 |
| Liquidez | ≥ $50K | $96.622 | +10 |
| Cambio 24 h | ≥ +50% | +1.667% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.667% · liq/mcap 8,4% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-11T01:39:11+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=8.4% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 45 de 28.243 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 11/10/2026 01:39 UTC, hasta 13/10/2026 01:39 UTC · vigente: quedan 47,4 h.
- **Aceleración al detectar:** cambio m5 -0,4% · h1 +95,9% · h24 +1.667% · volumen m5/h1 0,06 · edad del par 2,2 h.
- **Precio de entrada** (alerta): $0,001152.
- **Consulta 11/10/2026 02:12 UTC:** $0,001358 (+17,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump_2026-10-11_013911.json` · blob `11c2a8905d766e4ba0781c083f34e11334a5c125` · commit `aa200af` (2026-10-11T02:05:32Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-11_013216.json` · blob `38910434a1c68b7d8f3fcf077497a61adb3f22df` · commit `aa200af` (2026-10-11T02:05:32Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-11_013911`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump · registro · 11/10/2026 01:39 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump · HTTP 200 · 11/10/2026 02:12 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump/report · HTTP 200 · 11/10/2026 02:12 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump · HTTP 200 · 11/10/2026 02:12 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/94tupYk7hinha9fU2NQEkfh6jkykx88nTUbVQC2V9mAB/ohlcv/hour?limit=1000 · HTTP 200 · 11/10/2026 02:12 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump · HTTP 404 · 11/10/2026 02:12 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SUPMKTUSDT · HTTP 400 · 11/10/2026 02:12 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SUPMKT-USD · HTTP 404 · 11/10/2026 02:12 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $105.262 vs $103.919 → 1,28%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001358 vs $0,001364 → 0,44%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump_2026-10-11_013911.json',encoding='utf-8'));d=d.get('3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump',d);p=mock.patch('time.time',return_value=1791682751);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3Y9QZ7TR3WUD1ZDsrjWe2uNAdXESZEBo2XacPw7Vpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/10/2026 02:12 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `5c192f22e412b7ee…`
