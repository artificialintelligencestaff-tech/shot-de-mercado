# Samur•ai (Samur•ai) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000002557 · liquidez $2.889 · mcap $2.475 (al detectar)  
Detectado el 11/10/2026 02:39 UTC por: WS score muy alto, MCap bajo, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 13/10/2026 02:39 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Samur•ai

Estudio de cómo se adquiere Samur•ai, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/10/2026 02:57 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 11/10/2026 02:39 UTC | pumpswap `GPBdLUE…JVz9` | $2.889 | 10% | 6,922% | 69,218% | 692,183% | $14 | $43 |
| consulta 11/10/2026 02:57 UTC | pumpswap `GPBdLUE…JVz9` | $2.889 | 10% | 6,922% | 69,218% | 692,183% | $14 | $43 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump`
5. Configurar el slippage: 10% (liquidez $2.889, consulta 11/10/2026 02:57 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump) y el par en DexScreener (https://dexscreener.com/solana/GPBdLUEeBWqL7EyQpu8VVaUZwF4thFPJAYma3vPtJVz9); mint authority / freeze authority: revocada / revocada · holders 433 · top-10 98,53% (consulta 11/10/2026 02:57 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump
- Par en DexScreener: https://dexscreener.com/solana/GPBdLUEeBWqL7EyQpu8VVaUZwF4thFPJAYma3vPtJVz9
- Página del lanzamiento (pump.fun): https://pump.fun/coin/CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 433 · top-10 98,53% (consulta 11/10/2026 02:57 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Samur•ai / Samur•ai | registro de la detección (trending) |
| Mint / contrato | `CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `GPBdLUEeBWqL7EyQpu8VVaUZwF4thFPJAYma3vPtJVz9` | DexScreener, al detectar (2 par(es) en la consulta 11/10/2026 02:57 UTC) |
| Deployer | `HAuzNyUad1xF3WeiMww9pFENpxSWtfXPUJHarH4GDsGK` | RugCheck `creator` |
| Par creado | 10/10/2026 03:57 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 22,7 h / 22,7 h / 23,0 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/10/2026 02:57 UTC |
| Holders / top-10 | 433 / 98,53% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/10/2026 02:57 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/10/2026 02:57 UTC |
| Etiquetas de RugCheck | «Creator history of rugged tokens», «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 11/10/2026 02:57 UTC |
| Links | DexScreener: https://dexscreener.com/solana/GPBdLUEeBWqL7EyQpu8VVaUZwF4thFPJAYma3vPtJVz9 · Solscan: https://solscan.io/token/CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump · pump.fun: https://pump.fun/coin/CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump · web: https://samur-ai.pro/ · twitter: https://x.com/SamurAI_onchain | consulta 11/10/2026 02:57 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/10/2026 02:57 UTC)
- **Historia:**
  - Par creado el 10/10/2026 03:57 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 11/10/2026 02:39 UTC, con el par a 22,7 h de creado: precio $0,000002557, mcap $2.475, liquidez $2.889.
  - Velas de 1 h de GeckoTerminal (21, desde 10/10/2026 03:00 UTC): apertura $0,00004505 · máximo $0,0003702 (10/10/2026 05:00 UTC) · mínimo $0,000002469 (10/10/2026 21:00 UTC) · último cierre $0,000002558.
  - En la consulta 11/10/2026 02:57 UTC: precio $0,000002557, liquidez $2.889, FDV $2.475.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 11/10/2026 02:39 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000002557 |
| Liquidez | $2.889 |
| MCap | $2.475 |
| Volumen 24 h | $1.365.324 |
| Cambio 24 h | -94% |
| Cambio m5 / h1 | +0,0% / +1,6% |
| Volumen m5 / h1 | $0 / $8 |
| Trades m5 (compras / ventas) | 0 / 0 |
| Edad del par | 22,7 h |
| Score del feed (WS) | 96 |

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

Desglose no reproducible desde los motivos registrados (suma 13 vs score 100; motivos sin regla: score de detección 100 (script_82, hace 1 min) > re-score 13: vale el de detección (paridad con script_97)): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-11T02:39:26+00:00, sin estado previo): **13** · motivos: WS score muy alto, MCap bajo, Volumen masivo, Detección tardía (sin datos m5, >4h), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 46 de 28.367 tokens analizados (0,16%) quedan ≥ 56. Con score 13, este activo queda en el percentil 97,3 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 11/10/2026 02:39 UTC, hasta 13/10/2026 02:39 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +0,0% · h1 +1,6% · h24 -94% · volumen m5/h1 0,00 · edad del par 22,7 h.
- **Precio de entrada** (alerta): $0,000002557.
- **Consulta 11/10/2026 02:57 UTC:** $0,000002557 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump_2026-10-11_023926.json` · blob `794b866e9e159a29826ff144590ff13d7a99535b` · commit `7fcee06` (2026-10-11T02:49:54Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-11_023252.json` · blob `72166aeed161fa0b040c5f34a0e5c19546bbe4c5` · commit `7fcee06` (2026-10-11T02:49:54Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-11_023926`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump · registro · 11/10/2026 02:39 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump · HTTP 200 · 11/10/2026 02:57 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump/report · HTTP 200 · 11/10/2026 02:57 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump · HTTP 200 · 11/10/2026 02:57 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/GPBdLUEeBWqL7EyQpu8VVaUZwF4thFPJAYma3vPtJVz9/ohlcv/hour?limit=1000 · HTTP 200 · 11/10/2026 02:57 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump · HTTP 404 · 11/10/2026 02:57 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.889 vs $2.890 → 0,02%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002557 vs $0,000002558 → 0,04%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump_2026-10-11_023926.json',encoding='utf-8'));d=d.get('CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump',d);p=mock.patch('time.time',return_value=1791686366);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint CB4f3tTUckrtSJxfyCvsURLYhedkdkKPCm1mewbVpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/10/2026 02:57 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `5303907acf958a16…`
