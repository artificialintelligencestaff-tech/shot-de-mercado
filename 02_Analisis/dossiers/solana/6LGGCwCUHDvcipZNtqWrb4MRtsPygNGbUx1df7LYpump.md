# King Odie (ODIE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001591 · liquidez $116.267 · mcap $1.581.999 (al detectar)  
Detectado el 23/10/2026 14:27 UTC por: WS score muy alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 25/10/2026 14:27 UTC (< 48 h) · vigente: quedan 47,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ODIE

Estudio de cómo se adquiere ODIE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 23/10/2026 15:02 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 23/10/2026 14:27 UTC | pumpswap `DNm2wAS…tLgs` | $116.267 | 5% | 0,172% | 1,720% | 17,202% | $581 | $1.744 |
| consulta 23/10/2026 15:02 UTC | pumpswap `DNm2wAS…tLgs` | $173.242 | 5% | 0,115% | 1,154% | 11,545% | $866 | $2.599 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump`
5. Configurar el slippage: 5% (liquidez $173.242, consulta 23/10/2026 15:02 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump) y el par en DexScreener (https://dexscreener.com/solana/DNm2wASF4PP9XivPucrwm3CV9AnAsuugEgANqUDtLgs); mint authority / freeze authority: revocada / revocada · holders 7.212 · top-10 4,95% (consulta 23/10/2026 15:02 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump
- Par en DexScreener: https://dexscreener.com/solana/DNm2wASF4PP9XivPucrwm3CV9AnAsuugEgANqUDtLgs
- Página del lanzamiento (pump.fun): https://pump.fun/coin/6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 7.212 · top-10 4,95% (consulta 23/10/2026 15:02 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | King Odie / ODIE | registro de la detección (trending) |
| Mint / contrato | `6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DNm2wASF4PP9XivPucrwm3CV9AnAsuugEgANqUDtLgs` | DexScreener, al detectar (2 par(es) en la consulta 23/10/2026 15:02 UTC) |
| Deployer | `Eoxb3mTQVTbNAuUT6fNZVnHvF3EoyRsQ2AT4ibSFrr1X` | RugCheck `creator` |
| Par creado | 23/10/2026 13:00 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 86,6 min / 86,6 min / 2,0 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 23/10/2026 15:02 UTC |
| Holders / top-10 | 7.212 / 4,95% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 23/10/2026 15:02 UTC |
| Holders efectivos del top-10 | 3,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 23/10/2026 15:02 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 23/10/2026 15:02 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DNm2wASF4PP9XivPucrwm3CV9AnAsuugEgANqUDtLgs · Solscan: https://solscan.io/token/6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump · pump.fun: https://pump.fun/coin/6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump · web: https://kingodie.dog · twitter: https://x.com/KingOdieX | consulta 23/10/2026 15:02 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 23/10/2026 15:02 UTC)
- **Historia:**
  - Par creado el 23/10/2026 13:00 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 23/10/2026 14:27 UTC, con el par a 86,6 min de creado: precio $0,001591, mcap $1.581.999, liquidez $116.267.
  - Velas de 1 h de GeckoTerminal (3, desde 23/10/2026 13:00 UTC): apertura $0,00009495 · máximo $0,004034 (23/10/2026 14:00 UTC) · mínimo $0,00005688 (23/10/2026 13:00 UTC) · último cierre $0,003390.
  - En la consulta 23/10/2026 15:02 UTC: precio $0,003395, liquidez $173.242, FDV $3.374.954.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 23/10/2026 14:27 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001591 |
| Liquidez | $116.267 |
| MCap | $1.581.999 |
| Volumen 24 h | $3.485.410 |
| Cambio 24 h | +2.674% |
| Cambio m5 / h1 | +2,6% / +125,0% |
| Volumen m5 / h1 | $90.136 / $2.114.117 |
| Trades m5 (compras / ventas) | 1.346 / 469 |
| Edad del par | 86,6 min |
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
| Score del feed | score WS × 0,3 | WS 86 × 0,3 | +25,7 |
| MCap | ≥ $1M | $1.581.999 | +25 |
| Volumen 24 h | ≥ $1M | $3.485.410 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 74% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +2,6% · h1 +125,0% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 86,6 min | +8 |
| Volumen m5 | > $1K (par maduro) | $90.136 | +10 |
| Liquidez | ≥ $100K | $116.267 | +15 |
| Cambio 24 h | ≥ +50% | +2.674% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +2.674% · liq/mcap 7,3% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-23T14:27:17+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=7.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 75 de 44.938 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 23/10/2026 14:27 UTC, hasta 25/10/2026 14:27 UTC · vigente: quedan 47,4 h.
- **Aceleración al detectar:** cambio m5 +2,6% · h1 +125,0% · h24 +2.674% · volumen m5/h1 0,04 · edad del par 86,6 min.
- **Precio de entrada** (alerta): $0,001591.
- **Consulta 23/10/2026 15:02 UTC:** $0,003395 (+113,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump_2026-10-23_142717.json` · blob `158aad334767c5655351cb02753d97c847d70a4e` · commit `8830656` (2026-10-23T14:54:00Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-23_141951.json` · blob `a622ba8cf2eacec2a8ce4c6f6aa8926247a21e1a` · commit `8830656` (2026-10-23T14:54:00Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-23_142717`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump · registro · 23/10/2026 14:27 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump · HTTP 200 · 23/10/2026 15:02 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump/report · HTTP 200 · 23/10/2026 15:02 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump · HTTP 200 · 23/10/2026 15:02 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DNm2wASF4PP9XivPucrwm3CV9AnAsuugEgANqUDtLgs/ohlcv/hour?limit=1000 · HTTP 200 · 23/10/2026 15:02 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump · HTTP 404 · 23/10/2026 15:02 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ODIEUSDT · HTTP 400 · 23/10/2026 15:02 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ODIE-USD · HTTP 404 · 23/10/2026 15:02 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $173.242 vs $174.212 → 0,56%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003395 vs $0,003390 → 0,16%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump_2026-10-23_142717.json',encoding='utf-8'));d=d.get('6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump',d);p=mock.patch('time.time',return_value=1792765637);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 6LGGCwCUHDvcipZNtqWrb4MRtsPygNGbUx1df7LYpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 23/10/2026 15:02 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `b8c22c38b9053b49…`
