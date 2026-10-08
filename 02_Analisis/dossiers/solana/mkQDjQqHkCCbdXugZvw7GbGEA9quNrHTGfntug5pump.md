# Federal Private Equity System (FPES) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,004013 · liquidez $178.194 · mcap $4.011.019 (al detectar)  
Detectado el 08/10/2026 08:56 UTC por: MCap > $1M, Volumen decente, Buy pressure >55% (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 10/10/2026 08:56 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir FPES

Estudio de cómo se adquiere FPES, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/10/2026 09:14 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/10/2026 08:56 UTC | pumpswap `D4dhti1…HWSA` | $178.194 | 5% | 0,112% | 1,122% | 11,224% | $891 | $2.673 |
| consulta 08/10/2026 09:14 UTC | pumpswap `D4dhti1…HWSA` | $178.972 | 5% | 0,112% | 1,117% | 11,175% | $895 | $2.685 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump`
5. Configurar el slippage: 5% (liquidez $178.972, consulta 08/10/2026 09:14 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump) y el par en DexScreener (https://dexscreener.com/solana/D4dhti1fRwfaGKFenapvo5EikqDpBeLGueDjw8xLHWSA); mint authority / freeze authority: revocada / revocada · holders 4.046 · top-10 2,46% (consulta 08/10/2026 09:14 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump
- Par en DexScreener: https://dexscreener.com/solana/D4dhti1fRwfaGKFenapvo5EikqDpBeLGueDjw8xLHWSA
- Página del lanzamiento (pump.fun): https://pump.fun/coin/mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.046 · top-10 2,46% (consulta 08/10/2026 09:14 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Federal Private Equity System / FPES | registro de la detección (pumpportal) |
| Mint / contrato | `mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `D4dhti1fRwfaGKFenapvo5EikqDpBeLGueDjw8xLHWSA` | DexScreener, al detectar (2 par(es) en la consulta 08/10/2026 09:14 UTC) |
| Deployer | `9ah9ghAeGKcKao9HokAHQVG9T7aYhqEfSbWw9hLnKPoZ` | PumpPortal (evento create), al detectar |
| Par creado | 08/10/2026 07:56 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,3 min / 60,3 min / 78,6 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/10/2026 09:14 UTC |
| Holders / top-10 | 4.046 / 2,46% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/10/2026 09:14 UTC |
| Holders efectivos del top-10 | 1,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/10/2026 09:14 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 08/10/2026 09:14 UTC |
| Links | DexScreener: https://dexscreener.com/solana/D4dhti1fRwfaGKFenapvo5EikqDpBeLGueDjw8xLHWSA · Solscan: https://solscan.io/token/mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump · pump.fun: https://pump.fun/coin/mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump · web / Telegram / X: no publicados en DexScreener | consulta 08/10/2026 09:14 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/10/2026 09:14 UTC)
- **Historia:**
  - Par creado el 08/10/2026 07:56 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/10/2026 08:56 UTC, con el par a 60,3 min de creado: precio $0,004013, mcap $4.011.019, liquidez $178.194.
  - Velas de 1 h de GeckoTerminal (3, desde 08/10/2026 07:00 UTC): apertura $0,00004780 · máximo $0,004038 (08/10/2026 09:00 UTC) · mínimo $0,00004780 (08/10/2026 07:00 UTC) · último cierre $0,004038.
  - En la consulta 08/10/2026 09:14 UTC: precio $0,004039, liquidez $178.972, FDV $4.037.259.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/10/2026 08:56 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,004013 |
| Liquidez | $178.194 |
| MCap | $4.011.019 |
| Volumen 24 h | $84.881 |
| Cambio 24 h | +8.296% |
| Cambio m5 / h1 | +0,0% / +5,5% |
| Volumen m5 / h1 | $585 / $7.245 |
| Trades m5 (compras / ventas) | 12 / 9 |
| Edad del par | 60,3 min |
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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $1M | $4.011.019 | +25 |
| Volumen 24 h | ≥ $50K | $84.881 | +10 |
| Buy pressure m5 | > 55% (par maduro) | 57% | +15 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,0% · h1 +5,5% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,3 min | +8 |
| Volumen m5 | > $500 (par maduro) | $585 | +5 |
| Liquidez | ≥ $100K | $178.194 | +15 |
| Cambio 24 h | ≥ +50% | +8.296% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +8.296% · liq/mcap 4,4% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-08T08:56:24+00:00, sin estado previo): **100** · motivos: MCap > $1M, Volumen decente, Buy pressure >55%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.4% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 36 de 21.293 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/10/2026 08:56 UTC, hasta 10/10/2026 08:56 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +0,0% · h1 +5,5% · h24 +8.296% · volumen m5/h1 0,08 · edad del par 60,3 min.
- **Precio de entrada** (alerta): $0,004013.
- **Consulta 08/10/2026 09:14 UTC:** $0,004039 (+0,6% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump_2026-10-08_085624.json` · blob `1365283ceda7bed955e0fea8efa76bf685665693` · commit `8798c1f` (2026-10-08T09:06:26Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-08_085624`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump · registro · 08/10/2026 08:56 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump · HTTP 200 · 08/10/2026 09:14 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump/report · HTTP 200 · 08/10/2026 09:14 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump · HTTP 200 · 08/10/2026 09:14 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/D4dhti1fRwfaGKFenapvo5EikqDpBeLGueDjw8xLHWSA/ohlcv/hour?limit=1000 · HTTP 200 · 08/10/2026 09:14 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump · HTTP 404 · 08/10/2026 09:14 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=FPESUSDT · HTTP 400 · 08/10/2026 09:14 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/FPES-USD · HTTP 404 · 08/10/2026 09:14 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $178.972 vs $178.960 → 0,01%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,004039 vs $0,004038 → 0,02%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump_2026-10-08_085624.json',encoding='utf-8'));d=d.get('mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump',d);p=mock.patch('time.time',return_value=1791449784);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint mkQDjQqHkCCbdXugZvw7GbGEA9quNrHTGfntug5pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/10/2026 09:14 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `7f5be23c3eb87dee…`
