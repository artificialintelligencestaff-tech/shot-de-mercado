# Neil the Seal (NEIL) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000002315 · liquidez $2.504 · mcap $2.281 (al detectar)  
Detectado el 14/10/2026 03:26 UTC por: WS score muy alto, MCap bajo, Volumen alto (score 59, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 16/10/2026 03:26 UTC (< 48 h) · vigente: quedan 47,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir NEIL

Estudio de cómo se adquiere NEIL, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 14/10/2026 04:00 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 14/10/2026 03:26 UTC | pumpswap `DNQ2Aed…AoM6` | $2.504 | 10% | 7,988% | 79,884% | 798,837% | $13 | $38 |
| consulta 14/10/2026 04:00 UTC | pumpswap `DNQ2Aed…AoM6` | $2.504 | 10% | 7,988% | 79,884% | 798,837% | $13 | $38 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump`
5. Configurar el slippage: 10% (liquidez $2.504, consulta 14/10/2026 04:00 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump) y el par en DexScreener (https://dexscreener.com/solana/DNQ2AedfzumLpMcSwegxuf3tSaX5KVBcVbdcETh9AoM6); mint authority / freeze authority: revocada / revocada · holders 195 · top-10 99,79% (consulta 14/10/2026 04:00 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump
- Par en DexScreener: https://dexscreener.com/solana/DNQ2AedfzumLpMcSwegxuf3tSaX5KVBcVbdcETh9AoM6
- Página del lanzamiento (pump.fun): https://pump.fun/coin/Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 195 · top-10 99,79% (consulta 14/10/2026 04:00 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Neil the Seal / NEIL | registro de la detección (trending) |
| Mint / contrato | `Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DNQ2AedfzumLpMcSwegxuf3tSaX5KVBcVbdcETh9AoM6` | DexScreener, al detectar (2 par(es) en la consulta 14/10/2026 04:00 UTC) |
| Deployer | `EUWymakBWCBgxYxGBqbzo1EZts4mJwHXCfmuFtCeC1kR` | RugCheck `creator` |
| Par creado | 13/10/2026 20:50 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 6,6 h / 6,6 h / 7,2 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 14/10/2026 04:00 UTC |
| Holders / top-10 | 195 / 99,79% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 14/10/2026 04:00 UTC |
| Holders efectivos del top-10 | 1,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 14/10/2026 04:00 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 14/10/2026 04:00 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DNQ2AedfzumLpMcSwegxuf3tSaX5KVBcVbdcETh9AoM6 · Solscan: https://solscan.io/token/Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump · pump.fun: https://pump.fun/coin/Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump · web: https://neilseal.fun · twitter: https://x.com/neilseal_x · telegram: https://t.me/neilseal_tg | consulta 14/10/2026 04:00 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 14/10/2026 04:00 UTC)
- **Historia:**
  - Par creado el 13/10/2026 20:50 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 14/10/2026 03:26 UTC, con el par a 6,6 h de creado: precio $0,000002315, mcap $2.281, liquidez $2.504.
  - Velas de 1 h de GeckoTerminal (7, desde 13/10/2026 20:00 UTC): apertura $0,00007823 · máximo $0,0002157 (13/10/2026 21:00 UTC) · mínimo $0,000002134 (13/10/2026 22:00 UTC) · último cierre $0,000002315.
  - En la consulta 14/10/2026 04:00 UTC: precio $0,000002315, liquidez $2.504, FDV $2.281.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 14/10/2026 03:26 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000002315 |
| Liquidez | $2.504 |
| MCap | $2.281 |
| Volumen 24 h | $823.334 |
| Cambio 24 h | -98% |
| Cambio m5 / h1 | -0,8% / -0,8% |
| Volumen m5 / h1 | $0 / $0 |
| Trades m5 (compras / ventas) | 0 / 1 |
| Edad del par | 6,6 h |
| Score del feed (WS) | 82 |

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

Desglose reconstruido desde los motivos registrados; suma 59 = score registrado 59 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 82 × 0,3 | +24,7 |
| MCap | < $50K | $2.281 | +0 |
| Volumen 24 h | ≥ $100K | $823.334 | +15 |
| Volumen m5/h1 | > 0,5 (par maduro) | 1,00 | +25 |
| Trades m5/h1 | > 0,5 (par maduro) | 1,00 | +20 |
| Venta dominante | buy pressure < 40% con volumen m5 | 0% | -20 |
| Liquidez | < $20K | $2.504 | +0 |
| Cambio 24 h | ≤ −30% | -98% | -5 |
| **Total** | recortado a 0–100 |  | **59** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-14T03:26:38+00:00, sin estado previo): **59** · motivos: WS score muy alto, MCap bajo, Volumen alto, Volumen acelerado (5m/1h > 50%), Trades acelerados (5m/1h > 50%), Venta dominante (buy_pressure <40%), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 55 de 34.394 tokens analizados (0,16%) quedan ≥ 56. Con score 59, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 14/10/2026 03:26 UTC, hasta 16/10/2026 03:26 UTC · vigente: quedan 47,4 h.
- **Aceleración al detectar:** cambio m5 -0,8% · h1 -0,8% · h24 -98% · volumen m5/h1 1,00 · edad del par 6,6 h.
- **Precio de entrada** (alerta): $0,000002315.
- **Consulta 14/10/2026 04:00 UTC:** $0,000002315 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump_2026-10-14_032638.json` · blob `412484668359e2ebda236ae04538bc72e48fefb9` · commit `03eb415` (2026-10-14T03:54:06Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-14_031954.json` · blob `5ed6a96cc3e07767ffa7cb2079b48ef157be0d89` · commit `03eb415` (2026-10-14T03:54:06Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-14_032638`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump · registro · 14/10/2026 03:26 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump · HTTP 200 · 14/10/2026 04:00 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump/report · HTTP 200 · 14/10/2026 04:00 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump · HTTP 200 · 14/10/2026 04:00 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DNQ2AedfzumLpMcSwegxuf3tSaX5KVBcVbdcETh9AoM6/ohlcv/hour?limit=1000 · HTTP 200 · 14/10/2026 04:00 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump · HTTP 404 · 14/10/2026 04:00 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=NEILUSDT · HTTP 400 · 14/10/2026 04:00 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/NEIL-USD · HTTP 404 · 14/10/2026 04:00 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.504 vs $2.458 → 1,81%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002315 vs $0,000002315 → 0,01%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump_2026-10-14_032638.json',encoding='utf-8'));d=d.get('Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump',d);p=mock.patch('time.time',return_value=1791948398);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint Ct6HvaYv79FVwyr73MrEYNvLdtQouLquVmmZnuEkpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 14/10/2026 04:00 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `6f64eb02d80e759e…`
