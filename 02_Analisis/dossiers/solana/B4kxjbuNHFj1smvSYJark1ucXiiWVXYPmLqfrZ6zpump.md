# Slime Intelligent (Slime) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000002937 · liquidez $3.190 · mcap $2.863 (al detectar)  
Detectado el 09/10/2026 23:57 UTC por: WS score muy alto, MCap bajo, Volumen masivo (score 89, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 11/10/2026 23:57 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Slime

Estudio de cómo se adquiere Slime, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 10/10/2026 00:15 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 09/10/2026 23:57 UTC | pumpswap `FusPEfr…7wx2` | $3.190 | 10% | 6,269% | 62,691% | 626,912% | $16 | $48 |
| consulta 10/10/2026 00:15 UTC | pumpswap `FusPEfr…7wx2` | $3.153 | 10% | 6,344% | 63,442% | 634,415% | $16 | $47 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump`
5. Configurar el slippage: 10% (liquidez $3.153, consulta 10/10/2026 00:15 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump) y el par en DexScreener (https://dexscreener.com/solana/FusPEfrJiQDXGMyL4ZkXKxVmUFe5HSa7sMvaTjAB7wx2); mint authority / freeze authority: revocada / revocada · holders 510 · top-10 98,52% (consulta 10/10/2026 00:15 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump
- Par en DexScreener: https://dexscreener.com/solana/FusPEfrJiQDXGMyL4ZkXKxVmUFe5HSa7sMvaTjAB7wx2
- Página del lanzamiento (pump.fun): https://pump.fun/coin/B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 510 · top-10 98,52% (consulta 10/10/2026 00:15 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Slime Intelligent / Slime | registro de la detección (trending) |
| Mint / contrato | `B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `FusPEfrJiQDXGMyL4ZkXKxVmUFe5HSa7sMvaTjAB7wx2` | DexScreener, al detectar (2 par(es) en la consulta 10/10/2026 00:15 UTC) |
| Deployer | `BX5fuoNkxwfLEHJH6MoY9FD3deeyUMTind46WVB95DDr` | RugCheck `creator` |
| Par creado | 09/10/2026 07:02 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 16,9 h / 16,9 h / 17,2 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 10/10/2026 00:15 UTC |
| Holders / top-10 | 510 / 98,52% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 10/10/2026 00:15 UTC |
| Holders efectivos del top-10 | 1,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 10/10/2026 00:15 UTC |
| Etiquetas de RugCheck | «Creator history of rugged tokens», «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 10/10/2026 00:15 UTC |
| Links | DexScreener: https://dexscreener.com/solana/FusPEfrJiQDXGMyL4ZkXKxVmUFe5HSa7sMvaTjAB7wx2 · Solscan: https://solscan.io/token/B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump · pump.fun: https://pump.fun/coin/B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump · web: https://slimesia.com/ · twitter: https://x.com/slime_intel | consulta 10/10/2026 00:15 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 10/10/2026 00:15 UTC)
- **Historia:**
  - Par creado el 09/10/2026 07:02 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 09/10/2026 23:57 UTC, con el par a 16,9 h de creado: precio $0,000002937, mcap $2.863, liquidez $3.190.
  - Velas de 1 h de GeckoTerminal (16, desde 09/10/2026 07:00 UTC): apertura $0,00007305 · máximo $0,0004334 (09/10/2026 08:00 UTC) · mínimo $0,000002726 (09/10/2026 10:00 UTC) · último cierre $0,000002898.
  - En la consulta 10/10/2026 00:15 UTC: precio $0,000002896, liquidez $3.153, FDV $2.822.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 09/10/2026 23:57 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000002937 |
| Liquidez | $3.190 |
| MCap | $2.863 |
| Volumen 24 h | $1.282.879 |
| Cambio 24 h | -95% |
| Cambio m5 / h1 | +0,0% / +0,0% |
| Volumen m5 / h1 | $2 / $4 |
| Trades m5 (compras / ventas) | 1 / 2 |
| Edad del par | 16,9 h |
| Score del feed (WS) | 88 |

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

Desglose no reproducible desde los motivos registrados (suma 86 vs score 89; motivos sin regla: Anticipación (lib_early_signals early-0.2): +3 — volume_acceleration: vol 5 min ×7.7 la tasa horaria → +3): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-09T23:57:20+00:00, sin estado previo): **86** · motivos: WS score muy alto, MCap bajo, Volumen masivo, Volumen acelerado (5m/1h > 50%), Trades acelerados (5m/1h > 50%), Momentum corto+medio positivo, Venta dominante (buy_pressure <40%), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 42 de 26.019 tokens analizados (0,16%) quedan ≥ 56. Con score 86, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 09/10/2026 23:57 UTC, hasta 11/10/2026 23:57 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +0,0% · h1 +0,0% · h24 -95% · volumen m5/h1 0,64 · edad del par 16,9 h.
- **Precio de entrada** (alerta): $0,000002937.
- **Consulta 10/10/2026 00:15 UTC:** $0,000002896 (-1,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump_2026-10-09_235720.json` · blob `1b6f6db38e4521518cc98f198739926e7a365107` · commit `63b0abf` (2026-10-10T00:07:37Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-09_234937.json` · blob `b6a17640aebc14a4aa9164510baeebb4dd5c28f6` · commit `63b0abf` (2026-10-10T00:07:37Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-09_235720`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump · registro · 09/10/2026 23:57 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump · HTTP 200 · 10/10/2026 00:15 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump/report · HTTP 200 · 10/10/2026 00:15 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump · HTTP 200 · 10/10/2026 00:15 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/FusPEfrJiQDXGMyL4ZkXKxVmUFe5HSa7sMvaTjAB7wx2/ohlcv/hour?limit=1000 · HTTP 200 · 10/10/2026 00:15 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump · HTTP 404 · 10/10/2026 00:15 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SLIMEUSDT · HTTP 400 · 10/10/2026 00:15 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SLIME-USD · HTTP 404 · 10/10/2026 00:15 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.153 vs $3.158 → 0,16%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002896 vs $0,000002898 → 0,08%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump_2026-10-09_235720.json',encoding='utf-8'));d=d.get('B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump',d);p=mock.patch('time.time',return_value=1791590240);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint B4kxjbuNHFj1smvSYJark1ucXiiWVXYPmLqfrZ6zpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 10/10/2026 00:15 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `97b32ff60d194cd9…`
