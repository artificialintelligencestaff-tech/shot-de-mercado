# Aura Final Bull (KIMCHIBULL) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,004622 · liquidez $201.335 · mcap $4.609.702 (al detectar)  
Detectado el 22/10/2026 00:23 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 24/10/2026 00:23 UTC (< 48 h) · vigente: quedan 47,3 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir KIMCHIBULL

Estudio de cómo se adquiere KIMCHIBULL, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 22/10/2026 01:07 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 22/10/2026 00:23 UTC | pumpswap `Ds6CaQY…RWEM` | $201.335 | 5% | 0,099% | 0,993% | 9,934% | $1.007 | $3.020 |
| consulta 22/10/2026 01:07 UTC | pumpswap `Ds6CaQY…RWEM` | $204.443 | 5% | 0,098% | 0,978% | 9,783% | $1.022 | $3.067 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump`
5. Configurar el slippage: 5% (liquidez $204.443, consulta 22/10/2026 01:07 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump) y el par en DexScreener (https://dexscreener.com/solana/Ds6CaQYBQL7GjDATf9CVH189S9ef1mz7dkTrSoV7RWEM); mint authority / freeze authority: revocada / revocada · holders 6.525 · top-10 3,68% (consulta 22/10/2026 01:07 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump
- Par en DexScreener: https://dexscreener.com/solana/Ds6CaQYBQL7GjDATf9CVH189S9ef1mz7dkTrSoV7RWEM
- Página del lanzamiento (pump.fun): https://pump.fun/coin/GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 6.525 · top-10 3,68% (consulta 22/10/2026 01:07 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Aura Final Bull / KIMCHIBULL | registro de la detección (trending) |
| Mint / contrato | `GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Ds6CaQYBQL7GjDATf9CVH189S9ef1mz7dkTrSoV7RWEM` | DexScreener, al detectar (2 par(es) en la consulta 22/10/2026 01:07 UTC) |
| Deployer | `TiPRo64BSgn8Vya2yn8bTMZRBKTM2HhoRV3XU7dL2yZ` | RugCheck `creator` |
| Par creado | 21/10/2026 19:27 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 4,9 h / 4,9 h / 5,7 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 22/10/2026 01:07 UTC |
| Holders / top-10 | 6.525 / 3,68% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 22/10/2026 01:07 UTC |
| Holders efectivos del top-10 | 2,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 22/10/2026 01:07 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 22/10/2026 01:07 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Ds6CaQYBQL7GjDATf9CVH189S9ef1mz7dkTrSoV7RWEM · Solscan: https://solscan.io/token/GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump · pump.fun: https://pump.fun/coin/GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump · web: https://kimchifinalbull.com/ · twitter: https://x.com/KimchiFinalBull | consulta 22/10/2026 01:07 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 22/10/2026 01:07 UTC)
- **Historia:**
  - Par creado el 21/10/2026 19:27 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 22/10/2026 00:23 UTC, con el par a 4,9 h de creado: precio $0,004622, mcap $4.609.702, liquidez $201.335.
  - Velas de 1 h de GeckoTerminal (7, desde 21/10/2026 19:00 UTC): apertura $0,0002109 · máximo $0,01168 (21/10/2026 21:00 UTC) · mínimo $0,00005476 (21/10/2026 19:00 UTC) · último cierre $0,004749.
  - En la consulta 22/10/2026 01:07 UTC: precio $0,004750, liquidez $204.443, FDV $4.736.916.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 22/10/2026 00:23 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,004622 |
| Liquidez | $201.335 |
| MCap | $4.609.702 |
| Volumen 24 h | $5.354.490 |
| Cambio 24 h | +8.279% |
| Cambio m5 / h1 | -10,2% / -79,3% |
| Volumen m5 / h1 | $31.333 / $389.688 |
| Trades m5 (compras / ventas) | 457 / 66 |
| Edad del par | 4,9 h |
| Score del feed (WS) | 84 |

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
| Score del feed | score WS × 0,3 | WS 84 × 0,3 | +25,2 |
| MCap | ≥ $1M | $4.609.702 | +25 |
| Volumen 24 h | ≥ $1M | $5.354.490 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 87% | +25 |
| Volumen m5 | > $1K (par maduro) | $31.333 | +10 |
| Liquidez | ≥ $100K | $201.335 | +15 |
| Cambio 24 h | ≥ +50% | +8.279% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +8.279% · liq/mcap 4,4% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-22T00:23:30+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.4% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 74 de 43.589 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 22/10/2026 00:23 UTC, hasta 24/10/2026 00:23 UTC · vigente: quedan 47,3 h.
- **Aceleración al detectar:** cambio m5 -10,2% · h1 -79,3% · h24 +8.279% · volumen m5/h1 0,08 · edad del par 4,9 h.
- **Precio de entrada** (alerta): $0,004622.
- **Consulta 22/10/2026 01:07 UTC:** $0,004750 (+2,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump_2026-10-22_002330.json` · blob `253a189eb28a946e12d79f74fabc90b7aa44171a` · commit `ae2635b` (2026-10-22T00:59:21Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-22_001714.json` · blob `6a9799afc86abcb209b08affb823707db8035384` · commit `ae2635b` (2026-10-22T00:59:21Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-22_002330`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump · registro · 22/10/2026 00:23 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump · HTTP 200 · 22/10/2026 01:07 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump/report · HTTP 200 · 22/10/2026 01:07 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump · HTTP 200 · 22/10/2026 01:07 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Ds6CaQYBQL7GjDATf9CVH189S9ef1mz7dkTrSoV7RWEM/ohlcv/hour?limit=1000 · HTTP 200 · 22/10/2026 01:07 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump · HTTP 404 · 22/10/2026 01:07 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=KIMCHIBULLUSDT · HTTP 400 · 22/10/2026 01:07 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/KIMCHIBULL-USD · HTTP 404 · 22/10/2026 01:07 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $204.443 vs $204.243 → 0,10%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,004750 vs $0,004749 → 0,02%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump_2026-10-22_002330.json',encoding='utf-8'));d=d.get('GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump',d);p=mock.patch('time.time',return_value=1792628610);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint GNE7e774tkGyxMMzP36ofhNuRrUZ15H4e1LE1xekpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 22/10/2026 01:07 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `43d71fbeb97932a1…`
