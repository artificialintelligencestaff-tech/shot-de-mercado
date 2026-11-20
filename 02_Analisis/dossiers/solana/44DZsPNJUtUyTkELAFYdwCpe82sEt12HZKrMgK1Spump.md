# Apple AI Agent (iAgent) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001510 · liquidez $94.096 · mcap $1.505.703 (al detectar)  
Detectado el 20/11/2026 07:29 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 22/11/2026 07:29 UTC (< 48 h) · vigente: quedan 39,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir iAgent

Estudio de cómo se adquiere iAgent, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 20/11/2026 16:26 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 20/11/2026 07:29 UTC | pumpswap `BB8PP1b…FAKp` | $94.096 | 5% | 0,213% | 2,125% | 21,255% | $470 | $1.411 |
| consulta 20/11/2026 16:26 UTC | pumpswap `BB8PP1b…FAKp` | $2.356 | 10% | 8,487% | 84,875% | 848,745% | $12 | $35 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump`
5. Configurar el slippage: 10% (liquidez $2.356, consulta 20/11/2026 16:26 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump) y el par en DexScreener (https://dexscreener.com/solana/BB8PP1b4rYR9BGm59ju1wMQpwqa42kuyno5SmhLJFAKp); mint authority / freeze authority: revocada / revocada · holders 455 · top-10 99,03% (consulta 20/11/2026 16:26 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump
- Par en DexScreener: https://dexscreener.com/solana/BB8PP1b4rYR9BGm59ju1wMQpwqa42kuyno5SmhLJFAKp
- Página del lanzamiento (pump.fun): https://pump.fun/coin/44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 455 · top-10 99,03% (consulta 20/11/2026 16:26 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Apple AI Agent / iAgent | registro de la detección (trending) |
| Mint / contrato | `44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `BB8PP1b4rYR9BGm59ju1wMQpwqa42kuyno5SmhLJFAKp` | DexScreener, al detectar (6 par(es) en la consulta 20/11/2026 16:26 UTC) |
| Deployer | `ZXezTa6K1KEtbZwodqu6ScPWraVVdu1Y1AjotR5se5p` | RugCheck `creator` |
| Par creado | 20/11/2026 01:06 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 6,4 h / 6,4 h / 15,3 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 20/11/2026 16:26 UTC |
| Holders / top-10 | 455 / 99,03% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 20/11/2026 16:26 UTC |
| Holders efectivos del top-10 | 1,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0%; meteoraDlmm 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 20/11/2026 16:26 UTC |
| Etiquetas de RugCheck | «Creator history of rugged tokens», «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 20/11/2026 16:26 UTC |
| Links | DexScreener: https://dexscreener.com/solana/BB8PP1b4rYR9BGm59ju1wMQpwqa42kuyno5SmhLJFAKp · Solscan: https://solscan.io/token/44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump · pump.fun: https://pump.fun/coin/44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump · web: https://appleaiagent.online · twitter: https://x.com/iAgentSOL | consulta 20/11/2026 16:26 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 20/11/2026 16:26 UTC)
- **Historia:**
  - Par creado el 20/11/2026 01:06 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 20/11/2026 07:29 UTC, con el par a 6,4 h de creado: precio $0,001510, mcap $1.505.703, liquidez $94.096.
  - En la consulta 20/11/2026 16:26 UTC: precio $0,000002132, liquidez $2.356, FDV $2.125.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 20/11/2026 07:29 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001510 |
| Liquidez | $94.096 |
| MCap | $1.505.703 |
| Volumen 24 h | $3.240.386 |
| Cambio 24 h | +1.254% |
| Cambio m5 / h1 | -14,7% / -40,0% |
| Volumen m5 / h1 | $7.981 / $75.027 |
| Trades m5 (compras / ventas) | 339 / 175 |
| Edad del par | 6,4 h |
| Score del feed (WS) | 69 |

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
| Score del feed | score WS × 0,3 | WS 69 × 0,3 | +20,8 |
| MCap | ≥ $1M | $1.505.703 | +25 |
| Volumen 24 h | ≥ $1M | $3.240.386 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 66% | +25 |
| Volumen m5 | > $1K (par maduro) | $7.981 | +10 |
| Liquidez | ≥ $50K | $94.096 | +10 |
| Cambio 24 h | ≥ +50% | +1.254% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.254% · liq/mcap 6,2% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-20T07:29:36+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=6.2% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 108 de 47.489 tokens analizados (0,23%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 20/11/2026 07:29 UTC, hasta 22/11/2026 07:29 UTC · vigente: quedan 39,0 h.
- **Aceleración al detectar:** cambio m5 -14,7% · h1 -40,0% · h24 +1.254% · volumen m5/h1 0,11 · edad del par 6,4 h.
- **Precio de entrada** (alerta): $0,001510.
- **Consulta 20/11/2026 16:26 UTC:** $0,000002132 (-99,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump_2026-11-20_072936.json` · blob `be086ce76812af4a84ced6227a0fa4e334d75a17` · commit `1f2ca90` (2026-11-20T16:12:41Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-20_072257.json` · blob `70ce5f32e00f14399b8720c6695f5de5086cef9b` · commit `1f2ca90` (2026-11-20T16:12:41Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-20_072936`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump · registro · 20/11/2026 07:29 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump · HTTP 200 · 20/11/2026 16:26 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump/report · HTTP 200 · 20/11/2026 16:26 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump · HTTP 200 · 20/11/2026 16:26 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/BB8PP1b4rYR9BGm59ju1wMQpwqa42kuyno5SmhLJFAKp/ohlcv/hour?limit=1000 · HTTP 429 · 20/11/2026 16:26 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump · HTTP 404 · 20/11/2026 16:26 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=IAGENTUSDT · HTTP 400 · 20/11/2026 16:26 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/IAGENT-USD · HTTP 404 · 20/11/2026 16:26 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.356 vs $2.357 → 0,03%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump_2026-11-20_072936.json',encoding='utf-8'));d=d.get('44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump',d);p=mock.patch('time.time',return_value=1795159776);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 44DZsPNJUtUyTkELAFYdwCpe82sEt12HZKrMgK1Spump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 20/11/2026 16:26 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `7c53253104977b94…`
