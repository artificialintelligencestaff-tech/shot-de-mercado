# Digital American Water Supply (DAWS) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001712 · liquidez $112.088 · mcap $1.710.173 (al detectar)  
Detectado el 12/10/2026 18:10 UTC por: MCap > $1M, Volumen decente, Edge temprano (<4h) (score 73, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 14/10/2026 18:10 UTC (< 48 h) · vigente: quedan 47,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir DAWS

Estudio de cómo se adquiere DAWS, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 12/10/2026 18:45 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 12/10/2026 18:10 UTC | pumpswap `818G11H…yFDZ` | $112.088 | 5% | 0,178% | 1,784% | 17,843% | $560 | $1.681 |
| consulta 12/10/2026 18:45 UTC | pumpswap `818G11H…yFDZ` | $112.953 | 5% | 0,177% | 1,771% | 17,706% | $565 | $1.694 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump`
5. Configurar el slippage: 5% (liquidez $112.953, consulta 12/10/2026 18:45 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump) y el par en DexScreener (https://dexscreener.com/solana/818G11HuR3CLUeeRcTKidy4f4fAtjEqTtxDGRNNyyFDZ); mint authority / freeze authority: revocada / revocada · holders 1.949 · top-10 11,84% (consulta 12/10/2026 18:45 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump
- Par en DexScreener: https://dexscreener.com/solana/818G11HuR3CLUeeRcTKidy4f4fAtjEqTtxDGRNNyyFDZ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.949 · top-10 11,84% (consulta 12/10/2026 18:45 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Digital American Water Supply / DAWS | registro de la detección (pumpportal) |
| Mint / contrato | `kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `818G11HuR3CLUeeRcTKidy4f4fAtjEqTtxDGRNNyyFDZ` | DexScreener, al detectar (2 par(es) en la consulta 12/10/2026 18:45 UTC) |
| Deployer | `3KHkKTLwrmYu2kRGs9TpTR9EsTooaLYWGzxox7Q3GWiG` | PumpPortal (evento create), al detectar |
| Par creado | 12/10/2026 17:10 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,1 min / 60,1 min / 95,0 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 12/10/2026 18:45 UTC |
| Holders / top-10 | 1.949 / 11,84% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 12/10/2026 18:45 UTC |
| Holders efectivos del top-10 | 7,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 12/10/2026 18:45 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 12/10/2026 18:45 UTC |
| Links | DexScreener: https://dexscreener.com/solana/818G11HuR3CLUeeRcTKidy4f4fAtjEqTtxDGRNNyyFDZ · Solscan: https://solscan.io/token/kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump · pump.fun: https://pump.fun/coin/kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump · web / Telegram / X: no publicados en DexScreener | consulta 12/10/2026 18:45 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 12/10/2026 18:45 UTC)
- **Historia:**
  - Par creado el 12/10/2026 17:10 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 12/10/2026 18:10 UTC, con el par a 60,1 min de creado: precio $0,001712, mcap $1.710.173, liquidez $112.088.
  - Velas de 1 h de GeckoTerminal (2, desde 12/10/2026 17:00 UTC): apertura $0,00004485 · máximo $0,001744 (12/10/2026 18:00 UTC) · mínimo $0,00004485 (12/10/2026 17:00 UTC) · último cierre $0,001718.
  - En la consulta 12/10/2026 18:45 UTC: precio $0,001738, liquidez $112.953, FDV $1.736.947.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 12/10/2026 18:10 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001712 |
| Liquidez | $112.088 |
| MCap | $1.710.173 |
| Volumen 24 h | $52.210 |
| Cambio 24 h | +3.723% |
| Cambio m5 / h1 | -0,1% / +7,5% |
| Volumen m5 / h1 | $650 / $6.503 |
| Trades m5 (compras / ventas) | 11 / 9 |
| Edad del par | 60,1 min |
| Score del feed (WS) | n/d (feed sin score) |

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

Desglose reconstruido desde los motivos registrados; suma 73 = score registrado 73 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $1M | $1.710.173 | +25 |
| Volumen 24 h | ≥ $50K | $52.210 | +10 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,1 min | +8 |
| Volumen m5 | > $500 (par maduro) | $650 | +5 |
| Liquidez | ≥ $100K | $112.088 | +15 |
| Cambio 24 h | ≥ +50% | +3.723% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +3.723% · liq/mcap 6,6% | +0 |
| **Total** | recortado a 0–100 |  | **73** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-12T18:10:57+00:00, sin estado previo): **73** · motivos: MCap > $1M, Volumen decente, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=6.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 50 de 31.716 tokens analizados (0,16%) quedan ≥ 56. Con score 73, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 12/10/2026 18:10 UTC, hasta 14/10/2026 18:10 UTC · vigente: quedan 47,4 h.
- **Aceleración al detectar:** cambio m5 -0,1% · h1 +7,5% · h24 +3.723% · volumen m5/h1 0,10 · edad del par 60,1 min.
- **Precio de entrada** (alerta): $0,001712.
- **Consulta 12/10/2026 18:45 UTC:** $0,001738 (+1,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump_2026-10-12_181057.json` · blob `1d820d1c067ae744dcb38fb9aeddd389fb833e50` · commit `5da21a4` (2026-10-12T18:38:27Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-12_181057`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump · registro · 12/10/2026 18:10 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump · HTTP 200 · 12/10/2026 18:45 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump/report · HTTP 200 · 12/10/2026 18:45 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump · HTTP 200 · 12/10/2026 18:45 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/818G11HuR3CLUeeRcTKidy4f4fAtjEqTtxDGRNNyyFDZ/ohlcv/hour?limit=1000 · HTTP 200 · 12/10/2026 18:45 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump · HTTP 404 · 12/10/2026 18:45 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=DAWSUSDT · HTTP 400 · 12/10/2026 18:45 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/DAWS-USD · HTTP 404 · 12/10/2026 18:45 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $112.953 vs $112.303 → 0,58%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001738 vs $0,001718 → 1,15%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump_2026-10-12_181057.json',encoding='utf-8'));d=d.get('kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump',d);p=mock.patch('time.time',return_value=1791828657);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint kctxXiZbEtSTCxoCYL79sU8RqhiD6q9q8AzwGEZpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 12/10/2026 18:45 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `1747cd836ccaca45…`
