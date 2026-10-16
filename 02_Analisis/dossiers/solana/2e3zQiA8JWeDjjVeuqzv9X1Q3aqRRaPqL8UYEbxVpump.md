# Nubi (NUBI) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001834 · liquidez $123.150 · mcap $1.827.199 (al detectar)  
Detectado el 16/10/2026 22:55 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 18/10/2026 22:55 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir NUBI

Estudio de cómo se adquiere NUBI, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 16/10/2026 23:20 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 16/10/2026 22:55 UTC | pumpswap `265GQ6Q…t73M` | $123.150 | 5% | 0,162% | 1,624% | 16,240% | $616 | $1.847 |
| consulta 16/10/2026 23:20 UTC | pumpswap `265GQ6Q…t73M` | $132.631 | 5% | 0,151% | 1,508% | 15,079% | $663 | $1.989 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump`
5. Configurar el slippage: 5% (liquidez $132.631, consulta 16/10/2026 23:20 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump) y el par en DexScreener (https://dexscreener.com/solana/265GQ6QKcEGwNCWsL8CsJzD3iDDRuzwj7K9Pa7vst73M); mint authority / freeze authority: revocada / revocada · holders 5.584 · top-10 6,69% (consulta 16/10/2026 23:20 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump
- Par en DexScreener: https://dexscreener.com/solana/265GQ6QKcEGwNCWsL8CsJzD3iDDRuzwj7K9Pa7vst73M
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.584 · top-10 6,69% (consulta 16/10/2026 23:20 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Nubi / NUBI | registro de la detección (trending) |
| Mint / contrato | `2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `265GQ6QKcEGwNCWsL8CsJzD3iDDRuzwj7K9Pa7vst73M` | DexScreener, al detectar (3 par(es) en la consulta 16/10/2026 23:20 UTC) |
| Deployer | `4atbpBHGnMo7cNriiQQRPWXry4Djf2K8Jh7x8bDZ3X8U` | RugCheck `creator` |
| Par creado | 16/10/2026 20:33 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 2,4 h / 2,4 h / 2,8 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 16/10/2026 23:20 UTC |
| Holders / top-10 | 5.584 / 6,69% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 16/10/2026 23:20 UTC |
| Holders efectivos del top-10 | 3,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 16/10/2026 23:20 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 16/10/2026 23:20 UTC |
| Links | DexScreener: https://dexscreener.com/solana/265GQ6QKcEGwNCWsL8CsJzD3iDDRuzwj7K9Pa7vst73M · Solscan: https://solscan.io/token/2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump · pump.fun: https://pump.fun/coin/2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump · web: https://nubilaunch.online · twitter: https://x.com/NubiLaunchSOL | consulta 16/10/2026 23:20 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 16/10/2026 23:20 UTC)
- **Historia:**
  - Par creado el 16/10/2026 20:33 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 16/10/2026 22:55 UTC, con el par a 2,4 h de creado: precio $0,001834, mcap $1.827.199, liquidez $123.150.
  - Velas de 1 h de GeckoTerminal (4, desde 16/10/2026 20:00 UTC): apertura $0,00009455 · máximo $0,003761 (16/10/2026 21:00 UTC) · mínimo $0,00005663 (16/10/2026 20:00 UTC) · último cierre $0,002175.
  - En la consulta 16/10/2026 23:20 UTC: precio $0,002118, liquidez $132.631, FDV $2.109.811.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 16/10/2026 22:55 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001834 |
| Liquidez | $123.150 |
| MCap | $1.827.199 |
| Volumen 24 h | $3.732.869 |
| Cambio 24 h | +3.117% |
| Cambio m5 / h1 | -3,9% / -27,1% |
| Volumen m5 / h1 | $13.796 / $680.316 |
| Trades m5 (compras / ventas) | 588 / 326 |
| Edad del par | 2,4 h |
| Score del feed (WS) | 78 |

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
| Score del feed | score WS × 0,3 | WS 78 × 0,3 | +23,3 |
| MCap | ≥ $1M | $1.827.199 | +25 |
| Volumen 24 h | ≥ $1M | $3.732.869 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 64% | +25 |
| Edge temprano | edad < 4 h (par maduro) | edad 2,4 h | +8 |
| Volumen m5 | > $1K (par maduro) | $13.796 | +10 |
| Liquidez | ≥ $100K | $123.150 | +15 |
| Cambio 24 h | ≥ +50% | +3.117% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +3.117% · liq/mcap 6,7% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-16T22:55:53+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=6.7% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 61 de 37.781 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 16/10/2026 22:55 UTC, hasta 18/10/2026 22:55 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 -3,9% · h1 -27,1% · h24 +3.117% · volumen m5/h1 0,02 · edad del par 2,4 h.
- **Precio de entrada** (alerta): $0,001834.
- **Consulta 16/10/2026 23:20 UTC:** $0,002118 (+15,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump_2026-10-16_225553.json` · blob `5605c560e8f8e892e6480a3d1788f7025d7f941f` · commit `1a84db9` (2026-10-16T23:10:04Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-16_224935.json` · blob `25e5c07791c652225eb1e06ce583097fa44691da` · commit `1a84db9` (2026-10-16T23:10:04Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-16_225553`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump · registro · 16/10/2026 22:55 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump · HTTP 200 · 16/10/2026 23:20 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump/report · HTTP 200 · 16/10/2026 23:20 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump · HTTP 200 · 16/10/2026 23:20 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/265GQ6QKcEGwNCWsL8CsJzD3iDDRuzwj7K9Pa7vst73M/ohlcv/hour?limit=1000 · HTTP 200 · 16/10/2026 23:20 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump · HTTP 404 · 16/10/2026 23:20 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=NUBIUSDT · HTTP 400 · 16/10/2026 23:20 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/NUBI-USD · HTTP 404 · 16/10/2026 23:20 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $132.631 vs $133.206 → 0,43%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002118 vs $0,002175 → 2,60%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump_2026-10-16_225553.json',encoding='utf-8'));d=d.get('2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump',d);p=mock.patch('time.time',return_value=1792191353);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 16/10/2026 23:20 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `28a4b5fbbeb59bf8…`
