# Yi Long Ma (YILONGMA) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0006869 · liquidez $72.017 · mcap $684.080 (al detectar)  
Detectado el 17/10/2026 21:49 UTC por: WS score muy alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 19/10/2026 21:49 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir YILONGMA

Estudio de cómo se adquiere YILONGMA, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 17/10/2026 22:17 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 17/10/2026 21:49 UTC | pumpswap `18g3EYK…vQhN` | $72.017 | 5% | 0,278% | 2,777% | 27,771% | $360 | $1.080 |
| consulta 17/10/2026 22:17 UTC | pumpswap `18g3EYK…vQhN` | $79.300 | 5% | 0,252% | 2,522% | 25,221% | $397 | $1.190 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump`
5. Configurar el slippage: 5% (liquidez $79.300, consulta 17/10/2026 22:17 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump) y el par en DexScreener (https://dexscreener.com/solana/18g3EYKu5PksAdTRFoTbraCL6gT5o2qmxJ1ERQtvQhN); mint authority / freeze authority: revocada / revocada · holders 5.227 · top-10 6,28% (consulta 17/10/2026 22:17 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump
- Par en DexScreener: https://dexscreener.com/solana/18g3EYKu5PksAdTRFoTbraCL6gT5o2qmxJ1ERQtvQhN
- Página del lanzamiento (pump.fun): https://pump.fun/coin/DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.227 · top-10 6,28% (consulta 17/10/2026 22:17 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Yi Long Ma / YILONGMA | registro de la detección (trending) |
| Mint / contrato | `DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `18g3EYKu5PksAdTRFoTbraCL6gT5o2qmxJ1ERQtvQhN` | DexScreener, al detectar (3 par(es) en la consulta 17/10/2026 22:17 UTC) |
| Deployer | `BtHsQv38cwN7LRkZTT6GraSiC4ciwxMVNFSPnvep4NJM` | RugCheck `creator` |
| Par creado | 17/10/2026 16:25 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 5,4 h / 5,4 h / 5,9 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 17/10/2026 22:17 UTC |
| Holders / top-10 | 5.227 / 6,28% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 17/10/2026 22:17 UTC |
| Holders efectivos del top-10 | 1,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 17/10/2026 22:17 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 17/10/2026 22:17 UTC |
| Links | DexScreener: https://dexscreener.com/solana/18g3EYKu5PksAdTRFoTbraCL6gT5o2qmxJ1ERQtvQhN · Solscan: https://solscan.io/token/DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump · pump.fun: https://pump.fun/coin/DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump · web: https://yilongma.live/ · twitter: https://x.com/yilongmameme | consulta 17/10/2026 22:17 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 17/10/2026 22:17 UTC)
- **Historia:**
  - Par creado el 17/10/2026 16:25 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 17/10/2026 21:49 UTC, con el par a 5,4 h de creado: precio $0,0006869, mcap $684.080, liquidez $72.017.
  - Velas de 1 h de GeckoTerminal (7, desde 17/10/2026 16:00 UTC): apertura $0,0004314 · máximo $0,001746 (17/10/2026 19:00 UTC) · mínimo $0,0002540 (17/10/2026 20:00 UTC) · último cierre $0,0008020.
  - En la consulta 17/10/2026 22:17 UTC: precio $0,0008229, liquidez $79.300, FDV $819.543.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 17/10/2026 21:49 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0006869 |
| Liquidez | $72.017 |
| MCap | $684.080 |
| Volumen 24 h | $1.755.737 |
| Cambio 24 h | +1.193% |
| Cambio m5 / h1 | -10,7% / -1,2% |
| Volumen m5 / h1 | $8.188 / $130.768 |
| Trades m5 (compras / ventas) | 312 / 91 |
| Edad del par | 5,4 h |
| Score del feed (WS) | 86 |

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
| Score del feed | score WS × 0,3 | WS 86 × 0,3 | +25,8 |
| MCap | ≥ $100K | $684.080 | +15 |
| Volumen 24 h | ≥ $1M | $1.755.737 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 77% | +25 |
| Volumen m5 | > $1K (par maduro) | $8.188 | +10 |
| Liquidez | ≥ $50K | $72.017 | +10 |
| Cambio 24 h | ≥ +50% | +1.193% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +1.193% · liq/mcap 10,5% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-17T21:49:34+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=10.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 65 de 38.889 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 17/10/2026 21:49 UTC, hasta 19/10/2026 21:49 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -10,7% · h1 -1,2% · h24 +1.193% · volumen m5/h1 0,06 · edad del par 5,4 h.
- **Precio de entrada** (alerta): $0,0006869.
- **Consulta 17/10/2026 22:17 UTC:** $0,0008229 (+19,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump_2026-10-17_214934.json` · blob `f6a59d0be2a7b2f49936da353ddb6fb3aeddf103` · commit `259ad34` (2026-10-17T22:11:13Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-17_214311.json` · blob `7b3643d049a012f6c8715454ddae76ed904b88f9` · commit `259ad34` (2026-10-17T22:11:13Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-17_214934`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump · registro · 17/10/2026 21:49 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump · HTTP 200 · 17/10/2026 22:17 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump/report · HTTP 200 · 17/10/2026 22:17 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump · HTTP 200 · 17/10/2026 22:17 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/18g3EYKu5PksAdTRFoTbraCL6gT5o2qmxJ1ERQtvQhN/ohlcv/hour?limit=1000 · HTTP 200 · 17/10/2026 22:17 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump · HTTP 404 · 17/10/2026 22:17 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=YILONGMAUSDT · HTTP 400 · 17/10/2026 22:17 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/YILONGMA-USD · HTTP 404 · 17/10/2026 22:17 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $79.300 vs $79.327 → 0,03%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0008229 vs $0,0008020 → 2,53%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump_2026-10-17_214934.json',encoding='utf-8'));d=d.get('DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump',d);p=mock.patch('time.time',return_value=1792273774);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint DrLF1dG1K4U6ggx5BZ6bSwzGcPNVrQwYoTJzRDyZpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 17/10/2026 22:17 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `0c3159d2c8270eea…`
