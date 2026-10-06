# Mintro (MINTRO) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003234 · liquidez $175.898 · mcap $3.212.094 (al detectar)  
Detectado el 05/10/2026 23:52 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 07/10/2026 23:52 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir MINTRO

Estudio de cómo se adquiere MINTRO, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 00:14 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 05/10/2026 23:52 UTC | pumpswap `8t34p7n…Uzbn` | $175.898 | 5% | 0,114% | 1,137% | 11,370% | $879 | $2.638 |
| consulta 06/10/2026 00:14 UTC | pumpswap `8t34p7n…Uzbn` | $160.159 | 5% | 0,125% | 1,249% | 12,488% | $801 | $2.402 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump`
5. Configurar el slippage: 5% (liquidez $160.159, consulta 06/10/2026 00:14 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump) y el par en DexScreener (https://dexscreener.com/solana/8t34p7n94man8wcmFdHedYkJaWEhA9nKGJMLZyZUzbn); mint authority / freeze authority: revocada / revocada · holders 5.342 · top-10 4,12% (consulta 06/10/2026 00:14 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump
- Par en DexScreener: https://dexscreener.com/solana/8t34p7n94man8wcmFdHedYkJaWEhA9nKGJMLZyZUzbn
- Página del lanzamiento (pump.fun): https://pump.fun/coin/BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.342 · top-10 4,12% (consulta 06/10/2026 00:14 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Mintro / MINTRO | registro de la detección (trending) |
| Mint / contrato | `BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `8t34p7n94man8wcmFdHedYkJaWEhA9nKGJMLZyZUzbn` | DexScreener, al detectar (4 par(es) en la consulta 06/10/2026 00:14 UTC) |
| Deployer | `3CxkxNpC6Ys4JngaP94hiCGmipBBU8VzRys8sM7cU7HC` | RugCheck `creator` |
| Par creado | 05/10/2026 18:37 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 5,3 h / 5,3 h / 5,6 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 00:14 UTC |
| Holders / top-10 | 5.342 / 4,12% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 00:14 UTC |
| Holders efectivos del top-10 | 1,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; manifest 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 00:14 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 00:14 UTC |
| Links | DexScreener: https://dexscreener.com/solana/8t34p7n94man8wcmFdHedYkJaWEhA9nKGJMLZyZUzbn · Solscan: https://solscan.io/token/BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump · pump.fun: https://pump.fun/coin/BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump · web: https://mintro.site · twitter: https://x.com/MintroLaunchApp | consulta 06/10/2026 00:14 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 00:14 UTC)
- **Historia:**
  - Par creado el 05/10/2026 18:37 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 05/10/2026 23:52 UTC, con el par a 5,3 h de creado: precio $0,003234, mcap $3.212.094, liquidez $175.898.
  - Velas de 1 h de GeckoTerminal (7, desde 05/10/2026 18:00 UTC): apertura $0,0001245 · máximo $0,003792 (05/10/2026 23:00 UTC) · mínimo $0,0001245 (05/10/2026 18:00 UTC) · último cierre $0,002670.
  - En la consulta 06/10/2026 00:14 UTC: precio $0,002667, liquidez $160.159, FDV $2.649.100.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 05/10/2026 23:52 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003234 |
| Liquidez | $175.898 |
| MCap | $3.212.094 |
| Volumen 24 h | $3.099.121 |
| Cambio 24 h | +2.499% |
| Cambio m5 / h1 | -1,8% / +66,4% |
| Volumen m5 / h1 | $81.515 / $943.991 |
| Trades m5 (compras / ventas) | 567 / 245 |
| Edad del par | 5,3 h |
| Score del feed (WS) | 79 |

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
| Score del feed | score WS × 0,3 | WS 79 × 0,3 | +23,6 |
| MCap | ≥ $1M | $3.212.094 | +25 |
| Volumen 24 h | ≥ $1M | $3.099.121 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 70% | +25 |
| Volumen m5 | > $1K (par maduro) | $81.515 | +10 |
| Liquidez | ≥ $100K | $175.898 | +15 |
| Cambio 24 h | ≥ +50% | +2.499% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +2.499% · liq/mcap 5,5% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-05T23:52:48+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=5.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 17 de 13.636 tokens analizados (0,12%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 05/10/2026 23:52 UTC, hasta 07/10/2026 23:52 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 -1,8% · h1 +66,4% · h24 +2.499% · volumen m5/h1 0,09 · edad del par 5,3 h.
- **Precio de entrada** (alerta): $0,003234.
- **Consulta 06/10/2026 00:14 UTC:** $0,002667 (-17,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump_2026-10-05_235248.json` · blob `907f2b6bda67806e504cad5d8e11402952582bf6` · commit `25474d8` (2026-10-06T00:07:20Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-05_234626.json` · blob `fb1af13b32a521a16f86eca0479289e97dd95533` · commit `25474d8` (2026-10-06T00:07:20Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-05_235248`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump · registro · 05/10/2026 23:52 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump · HTTP 200 · 06/10/2026 00:14 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump/report · HTTP 200 · 06/10/2026 00:14 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump · HTTP 200 · 06/10/2026 00:14 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/8t34p7n94man8wcmFdHedYkJaWEhA9nKGJMLZyZUzbn/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 00:14 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump · HTTP 404 · 06/10/2026 00:14 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MINTROUSDT · HTTP 400 · 06/10/2026 00:14 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MINTRO-USD · HTTP 404 · 06/10/2026 00:14 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $160.159 vs $160.606 → 0,28%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002667 vs $0,002670 → 0,10%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump_2026-10-05_235248.json',encoding='utf-8'));d=d.get('BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump',d);p=mock.patch('time.time',return_value=1791244368);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint BrUimx7KncgRNTggAdZdaX2s5XUqQyR6XMRmEg4mpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 00:14 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `56e53a99cf0f2bda…`
