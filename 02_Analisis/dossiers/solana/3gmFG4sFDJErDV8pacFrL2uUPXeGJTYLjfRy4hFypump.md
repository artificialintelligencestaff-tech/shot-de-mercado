# Norfeather (NORFEATH) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0002795 · liquidez $40.422 · mcap $279.555 (al detectar)  
Detectado el 26/11/2026 19:22 UTC por: WS score muy alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 28/11/2026 19:22 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir NORFEATH

Estudio de cómo se adquiere NORFEATH, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 26/11/2026 19:22 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 26/11/2026 19:22 UTC | pumpswap `FUzScAt…yqdj` | $40.422 | 10% | 0,495% | 4,948% | 49,478% | $202 | $606 |
| consulta 26/11/2026 19:22 UTC | pumpswap `FUzScAt…yqdj` | $41.388 | 10% | 0,483% | 4,832% | 48,323% | $207 | $621 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump`
5. Configurar el slippage: 10% (liquidez $41.388, consulta 26/11/2026 19:22 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) y el par en DexScreener (https://dexscreener.com/solana/FUzScAtZzSt9rzMtt2pCDLPpJ1ikYC5LgDNjYtfWyqdj); mint authority / freeze authority: revocada / revocada · holders 10.360 · top-10 1,04% (consulta 26/11/2026 19:22 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump
- Par en DexScreener: https://dexscreener.com/solana/FUzScAtZzSt9rzMtt2pCDLPpJ1ikYC5LgDNjYtfWyqdj
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 10.360 · top-10 1,04% (consulta 26/11/2026 19:22 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Norfeather / NORFEATH | registro de la detección (trending) |
| Mint / contrato | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `FUzScAtZzSt9rzMtt2pCDLPpJ1ikYC5LgDNjYtfWyqdj` | DexScreener, al detectar (3 par(es) en la consulta 26/11/2026 19:22 UTC) |
| Deployer | `9kyz6d3YupUb512wfakLUTCZpyCyhK6sviGUDzehhjD8` | RugCheck `creator` |
| Par creado | 25/11/2026 21:05 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 22,3 h / 22,3 h / 22,3 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 26/11/2026 19:22 UTC |
| Holders / top-10 | 10.360 / 1,04% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 26/11/2026 19:22 UTC |
| Holders efectivos del top-10 | 9,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 26/11/2026 19:22 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 26/11/2026 19:22 UTC |
| Links | DexScreener: https://dexscreener.com/solana/FUzScAtZzSt9rzMtt2pCDLPpJ1ikYC5LgDNjYtfWyqdj · Solscan: https://solscan.io/token/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump · pump.fun: https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump · web: https://norfeather.lol · twitter: https://x.com/flynorfeather | consulta 26/11/2026 19:22 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 26/11/2026 19:22 UTC)
- **Historia:**
  - Par creado el 25/11/2026 21:05 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 26/11/2026 19:22 UTC, con el par a 22,3 h de creado: precio $0,0002795, mcap $279.555, liquidez $40.422.
  - Velas de 1 h de GeckoTerminal (23, desde 25/11/2026 21:00 UTC): apertura $0,00004586 · máximo $0,001031 (26/11/2026 08:00 UTC) · mínimo $0,00004586 (25/11/2026 21:00 UTC) · último cierre $0,0002682.
  - En la consulta 26/11/2026 19:22 UTC: precio $0,0002926, liquidez $41.388, FDV $292.561.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 26/11/2026 19:22 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0002795 |
| Liquidez | $40.422 |
| MCap | $279.555 |
| Volumen 24 h | $2.672.820 |
| Cambio 24 h | +509% |
| Cambio m5 / h1 | -8,2% / -6,4% |
| Volumen m5 / h1 | $14.511 / $62.174 |
| Trades m5 (compras / ventas) | 744 / 229 |
| Edad del par | 22,3 h |
| Score del feed (WS) | 89 |

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
| Score del feed | score WS × 0,3 | WS 89 × 0,3 | +26,8 |
| MCap | ≥ $100K | $279.555 | +15 |
| Volumen 24 h | ≥ $1M | $2.672.820 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 76% | +25 |
| Volumen m5 | > $1K (par maduro) | $14.511 | +10 |
| Liquidez | ≥ $20K | $40.422 | +5 |
| Cambio 24 h | ≥ +50% | +509% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +509% · liq/mcap 14,5% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-26T19:22:00+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez mínima, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=14.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 111 de 47.708 tokens analizados (0,23%) quedan ≥ 56. Con score 100, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 26/11/2026 19:22 UTC, hasta 28/11/2026 19:22 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -8,2% · h1 -6,4% · h24 +509% · volumen m5/h1 0,23 · edad del par 22,3 h.
- **Precio de entrada** (alerta): $0,0002795.
- **Consulta 26/11/2026 19:22 UTC:** $0,0002926 (+4,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump_2026-11-26_192216.json` · blob `7f21a41711fb284301489ad5d68ebcd9d354dbe9` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-26_191653.json` · blob `1ec6f4dbbc02c751e136b3739de2fca7316b0b92` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-26_192216`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump · registro · 26/11/2026 19:22 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump · HTTP 200 · 26/11/2026 19:22 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump/report · HTTP 200 · 26/11/2026 19:22 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump · HTTP 200 · 26/11/2026 19:22 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/FUzScAtZzSt9rzMtt2pCDLPpJ1ikYC5LgDNjYtfWyqdj/ohlcv/hour?limit=1000 · HTTP 200 · 26/11/2026 19:22 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump · HTTP 404 · 26/11/2026 19:22 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=NORFEATHUSDT · HTTP 400 · 26/11/2026 19:22 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/NORFEATH-USD · HTTP 404 · 26/11/2026 19:22 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $41.388 vs $41.274 → 0,28%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0002926 vs $0,0002682 → 8,34%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump_2026-11-26_192216.json',encoding='utf-8'));d=d.get('3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump',d);p=mock.patch('time.time',return_value=1795720920);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 26/11/2026 19:22 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `46ff0192607caeb9…`
