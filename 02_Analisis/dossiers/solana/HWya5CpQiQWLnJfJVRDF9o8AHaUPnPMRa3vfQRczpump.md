# A MIHAO CAT (AMC) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,004505 · liquidez $159.702 · mcap $4.478.268 (al detectar)  
Detectado el 14/11/2026 08:31 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 16/11/2026 08:31 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir AMC

Estudio de cómo se adquiere AMC, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 14/11/2026 08:31 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 14/11/2026 08:31 UTC | pumpswap `DxbQyPT…p3Gh` | $159.702 | 5% | 0,125% | 1,252% | 12,523% | $799 | $2.396 |
| consulta 14/11/2026 08:31 UTC | pumpswap `DxbQyPT…p3Gh` | $159.702 | 5% | 0,125% | 1,252% | 12,523% | $799 | $2.396 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump`
5. Configurar el slippage: 5% (liquidez $159.702, consulta 14/11/2026 08:31 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump) y el par en DexScreener (https://dexscreener.com/solana/DxbQyPTjckQTSUWyUqJB11HpupPyLGJZ5x4z7ufHp3Gh); mint authority / freeze authority: revocada / revocada · holders 11.664 · top-10 10,49% (consulta 14/11/2026 08:31 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump
- Par en DexScreener: https://dexscreener.com/solana/DxbQyPTjckQTSUWyUqJB11HpupPyLGJZ5x4z7ufHp3Gh
- Página del lanzamiento (pump.fun): https://pump.fun/coin/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 11.664 · top-10 10,49% (consulta 14/11/2026 08:31 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | A MIHAO CAT / AMC | registro de la detección (trending) |
| Mint / contrato | `HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DxbQyPTjckQTSUWyUqJB11HpupPyLGJZ5x4z7ufHp3Gh` | DexScreener, al detectar (3 par(es) en la consulta 14/11/2026 08:31 UTC) |
| Deployer | `DjAW8MZH7mtthogZxxxKmZKdGzh77KTca2kT3xzP48Dz` | RugCheck `creator` |
| Par creado | 13/11/2026 18:39 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 13,9 h / 13,9 h / 13,9 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 14/11/2026 08:31 UTC |
| Holders / top-10 | 11.664 / 10,49% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 14/11/2026 08:31 UTC |
| Holders efectivos del top-10 | 9,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 14/11/2026 08:31 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 14/11/2026 08:31 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DxbQyPTjckQTSUWyUqJB11HpupPyLGJZ5x4z7ufHp3Gh · Solscan: https://solscan.io/token/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump · pump.fun: https://pump.fun/coin/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump · web: https://amihaocat.space · twitter: https://x.com/amihaocat | consulta 14/11/2026 08:31 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 14/11/2026 08:31 UTC)
- **Historia:**
  - Par creado el 13/11/2026 18:39 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 14/11/2026 08:31 UTC, con el par a 13,9 h de creado: precio $0,004505, mcap $4.478.268, liquidez $159.702.
  - Velas de 1 h de GeckoTerminal (15, desde 13/11/2026 18:00 UTC): apertura $0,00005702 · máximo $0,005883 (14/11/2026 07:00 UTC) · mínimo $0,00003976 (13/11/2026 18:00 UTC) · último cierre $0,004513.
  - En la consulta 14/11/2026 08:31 UTC: precio $0,004505, liquidez $159.702, FDV $4.478.268.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 14/11/2026 08:31 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,004505 |
| Liquidez | $159.702 |
| MCap | $4.478.268 |
| Volumen 24 h | $2.007.973 |
| Cambio 24 h | +11.142% |
| Cambio m5 / h1 | +3,5% / -20,6% |
| Volumen m5 / h1 | $2.576 / $66.233 |
| Trades m5 (compras / ventas) | 924 / 427 |
| Edad del par | 13,9 h |
| Score del feed (WS) | 71 |

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
| Score del feed | score WS × 0,3 | WS 71 × 0,3 | +21,4 |
| MCap | ≥ $1M | $4.478.268 | +25 |
| Volumen 24 h | ≥ $1M | $2.007.973 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 68% | +25 |
| Volumen m5 | > $1K (par maduro) | $2.576 | +10 |
| Liquidez | ≥ $100K | $159.702 | +15 |
| Cambio 24 h | ≥ +50% | +11.142% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +11.142% · liq/mcap 3,6% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-14T08:31:06+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=3.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 101 de 47.195 tokens analizados (0,21%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 14/11/2026 08:31 UTC, hasta 16/11/2026 08:31 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +3,5% · h1 -20,6% · h24 +11.142% · volumen m5/h1 0,04 · edad del par 13,9 h.
- **Precio de entrada** (alerta): $0,004505.
- **Consulta 14/11/2026 08:31 UTC:** $0,004505 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump_2026-11-14_083117.json` · blob `0eea9696241d3895c7ef52a38a232476cea8a648` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-14_082603.json` · blob `c350b503981bc81a3a7ec9e920a438549d2c15a4` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-14_083117`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump · registro · 14/11/2026 08:31 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump · HTTP 200 · 14/11/2026 08:31 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump/report · HTTP 200 · 14/11/2026 08:31 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump · HTTP 200 · 14/11/2026 08:31 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DxbQyPTjckQTSUWyUqJB11HpupPyLGJZ5x4z7ufHp3Gh/ohlcv/hour?limit=1000 · HTTP 200 · 14/11/2026 08:31 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump · HTTP 404 · 14/11/2026 08:31 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=AMCUSDT · HTTP 400 · 14/11/2026 08:31 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/AMC-USD · HTTP 404 · 14/11/2026 08:31 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $159.702 vs $159.097 → 0,38%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,004505 vs $0,004513 → 0,17%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump_2026-11-14_083117.json',encoding='utf-8'));d=d.get('HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump',d);p=mock.patch('time.time',return_value=1794645066);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 14/11/2026 08:31 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `0255024c44159530…`
