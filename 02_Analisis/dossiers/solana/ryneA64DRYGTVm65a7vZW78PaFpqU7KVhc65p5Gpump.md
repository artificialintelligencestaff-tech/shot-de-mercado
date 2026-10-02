# peaq (PEAQ) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,005791 · liquidez $220.840 · mcap $5.791.019 (al detectar)  
Detectado el 02/10/2026 14:18 UTC por: MCap > $1M, Volumen alto, Liquidez alta (score 65, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 04/10/2026 14:18 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir PEAQ

Estudio de cómo se adquiere PEAQ, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 14:40 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 14:18 UTC | pumpswap `DjPbqHE…J28A` | $220.840 | 5% | 0,091% | 0,906% | 9,056% | $1.104 | $3.313 |
| consulta 02/10/2026 14:40 UTC | pumpswap `DjPbqHE…J28A` | $221.644 | 5% | 0,090% | 0,902% | 9,023% | $1.108 | $3.325 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump`
5. Configurar el slippage: 5% (liquidez $221.644, consulta 02/10/2026 14:40 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump) y el par en DexScreener (https://dexscreener.com/solana/DjPbqHEmGXaLxd1Vtj9AggHzidvmUMzxtW1odjg8J28A); mint authority / freeze authority: revocada / revocada · holders 3.792 · top-10 10,73% (consulta 02/10/2026 14:40 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump
- Par en DexScreener: https://dexscreener.com/solana/DjPbqHEmGXaLxd1Vtj9AggHzidvmUMzxtW1odjg8J28A
- Página del lanzamiento (pump.fun): https://pump.fun/coin/ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.792 · top-10 10,73% (consulta 02/10/2026 14:40 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | peaq / PEAQ | registro de la detección (pumpportal_live) |
| Mint / contrato | `ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DjPbqHEmGXaLxd1Vtj9AggHzidvmUMzxtW1odjg8J28A` | DexScreener, al detectar (2 par(es) en la consulta 02/10/2026 14:40 UTC) |
| Deployer | `7jo54MKB68zswzV7UDFAt1RkwBBJHCjN4mNF71pcExNf` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 14:08 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,3 min / 10,3 min / 32,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 14:40 UTC |
| Holders / top-10 | 3.792 / 10,73% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 14:40 UTC |
| Holders efectivos del top-10 | 9,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 14:40 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 14:40 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DjPbqHEmGXaLxd1Vtj9AggHzidvmUMzxtW1odjg8J28A · Solscan: https://solscan.io/token/ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump · pump.fun: https://pump.fun/coin/ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump · web / Telegram / X: no publicados en DexScreener | consulta 02/10/2026 14:40 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 14:40 UTC)
- **Historia:**
  - Par creado el 02/10/2026 14:08 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 14:18 UTC, con el par a 10,3 min de creado: precio $0,005791, mcap $5.791.019, liquidez $220.840.
  - Velas de 1 h de GeckoTerminal (1, desde 02/10/2026 14:00 UTC): apertura $0,005597 · máximo $0,005887 (02/10/2026 14:00 UTC) · mínimo $0,00005063 (02/10/2026 14:00 UTC) · último cierre $0,005804.
  - En la consulta 02/10/2026 14:40 UTC: precio $0,005855, liquidez $221.644, FDV $5.855.718.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 14:18 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,005791 |
| Liquidez | $220.840 |
| MCap | $5.791.019 |
| Volumen 24 h | $101.112 |
| Cambio 24 h | +11.312% |
| Cambio m5 / h1 | +0,0% / +11.312,0% |
| Volumen m5 / h1 | $628 / $101.112 |
| Trades m5 (compras / ventas) | 13 / 12 |
| Edad del par | 10,3 min |
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

Desglose reconstruido desde los motivos registrados; suma 65 = score registrado 65 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| Gate de edad v7.2.1 | edad < 60 min o desconocida: sin bonos temporales | edad 10,3 min | +0 |
| MCap | ≥ $1M | $5.791.019 | +25 |
| Volumen 24 h | ≥ $100K | $101.112 | +15 |
| Liquidez | ≥ $100K | $220.840 | +15 |
| Cambio 24 h | ≥ +50% | +11.312% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +11.312% · liq/mcap 3,8% | +0 |
| **Total** | recortado a 0–100 |  | **65** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T14:18:34+00:00, sin estado previo): **65** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen alto, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=3.8% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 11 de 7.754 tokens analizados (0,14%) quedan ≥ 56. Con score 65, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 14:18 UTC, hasta 04/10/2026 14:18 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +0,0% · h1 +11.312,0% · h24 +11.312% · volumen m5/h1 0,01 · edad del par 10,3 min.
- **Precio de entrada** (alerta): $0,005791.
- **Consulta 02/10/2026 14:40 UTC:** $0,005855 (+1,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump_2026-10-02_141834.json` · blob `78e0ac6cae19b39131584ae2c2778c718ff8e29b` · commit `39390b1` (2026-10-02T14:33:51Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_141834`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump · registro · 02/10/2026 14:18 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump · HTTP 200 · 02/10/2026 14:40 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump/report · HTTP 200 · 02/10/2026 14:40 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump · HTTP 200 · 02/10/2026 14:40 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DjPbqHEmGXaLxd1Vtj9AggHzidvmUMzxtW1odjg8J28A/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 14:40 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump · HTTP 404 · 02/10/2026 14:40 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=PEAQUSDT · HTTP 400 · 02/10/2026 14:40 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/PEAQ-USD · HTTP 404 · 02/10/2026 14:40 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $221.644 vs $221.563 → 0,04%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,005855 vs $0,005804 → 0,88%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump_2026-10-02_141834.json',encoding='utf-8'));d=d.get('ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump',d);p=mock.patch('time.time',return_value=1790950714);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint ryneA64DRYGTVm65a7vZW78PaFpqU7KVhc65p5Gpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 14:40 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `3a6167922297da58…`
