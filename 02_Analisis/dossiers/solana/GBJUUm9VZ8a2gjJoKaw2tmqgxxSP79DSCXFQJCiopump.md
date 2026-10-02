# Intelligent Neural Unit (INU) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0004237 · liquidez $63.681 · mcap $423.792 (al detectar)  
Detectado el 02/10/2026 12:51 UTC por: MCap > $100K, Volumen masivo, Liquidez decente (score 60, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 04/10/2026 12:51 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir INU

Estudio de cómo se adquiere INU, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 13:01 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 12:51 UTC | pumpswap `7sLwf1S…sU1h` | $63.681 | 5% | 0,314% | 3,141% | 31,406% | $318 | $955 |
| consulta 02/10/2026 13:01 UTC | pumpswap `7sLwf1S…sU1h` | $4.545 | 10% | 4,401% | 44,009% | 440,087% | $23 | $68 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump`
5. Configurar el slippage: 10% (liquidez $4.545, consulta 02/10/2026 13:01 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump) y el par en DexScreener (https://dexscreener.com/solana/7sLwf1SCcbZ1w6pMkwbwnWAyppyJpPSnoAZoQcvCsU1h); mint authority / freeze authority: revocada / revocada · holders 1.182 · top-10 95,35% (consulta 02/10/2026 13:01 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump
- Par en DexScreener: https://dexscreener.com/solana/7sLwf1SCcbZ1w6pMkwbwnWAyppyJpPSnoAZoQcvCsU1h
- Página del lanzamiento (pump.fun): https://pump.fun/coin/GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.182 · top-10 95,35% (consulta 02/10/2026 13:01 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Intelligent Neural Unit / INU | registro de la detección (pumpportal_live) |
| Mint / contrato | `GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7sLwf1SCcbZ1w6pMkwbwnWAyppyJpPSnoAZoQcvCsU1h` | DexScreener, al detectar (3 par(es) en la consulta 02/10/2026 13:01 UTC) |
| Deployer | `CgwrhDkZtNGXPLciWNGYUZRQQmfkVd4UbDtsk21f6AGN` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 12:39 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,3 min / 11,3 min / 21,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 13:01 UTC |
| Holders / top-10 | 1.182 / 95,35% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 13:01 UTC |
| Holders efectivos del top-10 | 1,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 13:01 UTC |
| Etiquetas de RugCheck | «Creator history of rugged tokens», «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 13:01 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7sLwf1SCcbZ1w6pMkwbwnWAyppyJpPSnoAZoQcvCsU1h · Solscan: https://solscan.io/token/GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump · pump.fun: https://pump.fun/coin/GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump · web / Telegram / X: no publicados en DexScreener | consulta 02/10/2026 13:01 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 13:01 UTC)
- **Historia:**
  - Par creado el 02/10/2026 12:39 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 12:51 UTC, con el par a 11,3 min de creado: precio $0,0004237, mcap $423.792, liquidez $63.681.
  - Velas de 1 h de GeckoTerminal (2, desde 02/10/2026 12:00 UTC): apertura $0,00005265 · máximo $0,0006063 (02/10/2026 12:00 UTC) · mínimo $0,000003644 (02/10/2026 12:00 UTC) · último cierre $0,000004220.
  - En la consulta 02/10/2026 13:01 UTC: precio $0,000004170, liquidez $4.545, FDV $4.170.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 12:51 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0004237 |
| Liquidez | $63.681 |
| MCap | $423.792 |
| Volumen 24 h | $1.868.883 |
| Cambio 24 h | +733% |
| Cambio m5 / h1 | +81,6% / +733,0% |
| Volumen m5 / h1 | $906.342 / $1.868.883 |
| Trades m5 (compras / ventas) | 3.565 / 2.099 |
| Edad del par | 11,3 min |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 1/2 (50,0%, IC90 12,1%–87,9%) · secundaria 0/1 resueltas (shadow_monitor.json).

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

Desglose no reproducible desde los motivos registrados (suma 55 vs score 60; motivos sin regla: Anticipación (lib_early_signals early-0.2): +5 — volume_acceleration: vol 5 min ×5.8 la tasa horaria → +3; buy_pressure_shift: compras 63% en 5 min vs 59% en 1 h → +0.36; liquidity_inflow: liquidez +107% en 8 min → +2): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T12:51:12+00:00, sin estado previo): **55** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen masivo, Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=15.0% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 8 de 7.463 tokens analizados (0,11%) quedan ≥ 56. Con score 55, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 12:51 UTC, hasta 04/10/2026 12:51 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 +81,6% · h1 +733,0% · h24 +733% · volumen m5/h1 0,48 · edad del par 11,3 min.
- **Precio de entrada** (alerta): $0,0004237.
- **Consulta 02/10/2026 13:01 UTC:** $0,000004170 (-99,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump_2026-10-02_125112.json` · blob `e8c769483259696a71dab36d01e4bad819dda7a4` · commit `c50e49f` (2026-10-02T12:54:25Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_125112`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump · registro · 02/10/2026 12:51 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump · HTTP 200 · 02/10/2026 13:01 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump/report · HTTP 200 · 02/10/2026 13:01 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump · HTTP 200 · 02/10/2026 13:01 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7sLwf1SCcbZ1w6pMkwbwnWAyppyJpPSnoAZoQcvCsU1h/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 13:01 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump · HTTP 404 · 02/10/2026 13:01 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=INUUSDT · HTTP 400 · 02/10/2026 13:01 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/INU-USD · HTTP 404 · 02/10/2026 13:01 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $4.545 vs $4.586 → 0,91%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000004170 vs $0,000004220 → 1,18%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump_2026-10-02_125112.json',encoding='utf-8'));d=d.get('GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump',d);p=mock.patch('time.time',return_value=1790945472);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint GBJUUm9VZ8a2gjJoKaw2tmqgxxSP79DSCXFQJCiopump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 13:01 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `14bbf13b57d06cf7…`
