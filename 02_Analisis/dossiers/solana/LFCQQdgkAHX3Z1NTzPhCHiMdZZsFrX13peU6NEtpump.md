# Hooked (HOOKED) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001683 · liquidez $116.273 · mcap $1.681.199 (al detectar)  
Detectado el 01/10/2026 22:23 UTC por: MCap > $1M, Volumen decente, Buy pressure >55% (score 88, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 03/10/2026 22:23 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir HOOKED

Estudio de cómo se adquiere HOOKED, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 01/10/2026 22:34 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 01/10/2026 22:23 UTC | pumpswap `tyg2jPx…J2Vq` | $116.273 | 5% | 0,172% | 1,720% | 17,201% | $581 | $1.744 |
| consulta 01/10/2026 22:34 UTC | pumpswap `tyg2jPx…J2Vq` | $117.050 | 5% | 0,171% | 1,709% | 17,087% | $585 | $1.756 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump`
5. Configurar el slippage: 5% (liquidez $117.050, consulta 01/10/2026 22:34 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump) y el par en DexScreener (https://dexscreener.com/solana/tyg2jPx1Snzhfo4ssouAvP9pRNsEETVrfLc1RMbJ2Vq); mint authority / freeze authority: revocada / revocada · holders 3.029 · top-10 4,59% (consulta 01/10/2026 22:34 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump
- Par en DexScreener: https://dexscreener.com/solana/tyg2jPx1Snzhfo4ssouAvP9pRNsEETVrfLc1RMbJ2Vq
- Página del lanzamiento (pump.fun): https://pump.fun/coin/LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.029 · top-10 4,59% (consulta 01/10/2026 22:34 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Hooked / HOOKED | registro de la detección (pumpportal) |
| Mint / contrato | `LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `tyg2jPx1Snzhfo4ssouAvP9pRNsEETVrfLc1RMbJ2Vq` | DexScreener, al detectar (2 par(es) en la consulta 01/10/2026 22:34 UTC) |
| Deployer | `8xtVUYXoBiuaNdCAkcU6VtX4TMNG8tyN9ya3Bgp88ako` | PumpPortal (evento create), al detectar |
| Par creado | 01/10/2026 19:49 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 2,6 h / 2,6 h / 2,7 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 01/10/2026 22:34 UTC |
| Holders / top-10 | 3.029 / 4,59% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 01/10/2026 22:34 UTC |
| Holders efectivos del top-10 | 1,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 01/10/2026 22:34 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 01/10/2026 22:34 UTC |
| Links | DexScreener: https://dexscreener.com/solana/tyg2jPx1Snzhfo4ssouAvP9pRNsEETVrfLc1RMbJ2Vq · Solscan: https://solscan.io/token/LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump · pump.fun: https://pump.fun/coin/LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump · web / Telegram / X: no publicados en DexScreener | consulta 01/10/2026 22:34 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 01/10/2026 22:34 UTC)
- **Historia:**
  - Par creado el 01/10/2026 19:49 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 01/10/2026 22:23 UTC, con el par a 2,6 h de creado: precio $0,001683, mcap $1.681.199, liquidez $116.273.
  - Velas de 1 h de GeckoTerminal (4, desde 01/10/2026 19:00 UTC): apertura $0,00004900 · máximo $0,001708 (01/10/2026 22:00 UTC) · mínimo $0,00004900 (01/10/2026 19:00 UTC) · último cierre $0,001682.
  - En la consulta 01/10/2026 22:34 UTC: precio $0,001703, liquidez $117.050, FDV $1.701.485.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 01/10/2026 22:23 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001683 |
| Liquidez | $116.273 |
| MCap | $1.681.199 |
| Volumen 24 h | $67.925 |
| Cambio 24 h | +3.331% |
| Cambio m5 / h1 | -1,3% / -1,0% |
| Volumen m5 / h1 | $640 / $8.657 |
| Trades m5 (compras / ventas) | 13 / 10 |
| Edad del par | 2,6 h |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 1/1 (100,0%, IC90 27,0%–100,0%) · secundaria 0/0 resueltas (shadow_monitor.json).

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

Desglose reconstruido desde los motivos registrados; suma 88 = score registrado 88 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $1M | $1.681.199 | +25 |
| Volumen 24 h | ≥ $50K | $67.925 | +10 |
| Buy pressure m5 | > 55% (par maduro) | 57% | +15 |
| Edge temprano | edad < 4 h (par maduro) | edad 2,6 h | +8 |
| Volumen m5 | > $500 (par maduro) | $640 | +5 |
| Liquidez | ≥ $100K | $116.273 | +15 |
| Cambio 24 h | ≥ +50% | +3.331% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +3.331% · liq/mcap 6,9% | +0 |
| **Total** | recortado a 0–100 |  | **88** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-01T22:23:03+00:00, sin estado previo): **88** · motivos: MCap > $1M, Volumen decente, Buy pressure >55%, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=6.9% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 6 de 6.105 tokens analizados (0,10%) quedan ≥ 56. Con score 88, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 01/10/2026 22:23 UTC, hasta 03/10/2026 22:23 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -1,3% · h1 -1,0% · h24 +3.331% · volumen m5/h1 0,07 · edad del par 2,6 h.
- **Precio de entrada** (alerta): $0,001683.
- **Consulta 01/10/2026 22:34 UTC:** $0,001703 (+1,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump_2026-10-01_222303.json` · blob `1880c0561db36b28c9362da0f75f88ab80cddbc8` · commit `9fe807d` (2026-10-01T22:27:54Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-01_222303`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump · registro · 01/10/2026 22:23 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump · HTTP 200 · 01/10/2026 22:34 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump/report · HTTP 200 · 01/10/2026 22:34 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump · HTTP 200 · 01/10/2026 22:34 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/tyg2jPx1Snzhfo4ssouAvP9pRNsEETVrfLc1RMbJ2Vq/ohlcv/hour?limit=1000 · HTTP 200 · 01/10/2026 22:34 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump · HTTP 404 · 01/10/2026 22:34 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HOOKEDUSDT · HTTP 400 · 01/10/2026 22:34 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HOOKED-USD · HTTP 404 · 01/10/2026 22:34 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $117.050 vs $116.233 → 0,70%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001703 vs $0,001682 → 1,25%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump_2026-10-01_222303.json',encoding='utf-8'));d=d.get('LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump',d);p=mock.patch('time.time',return_value=1790893383);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint LFCQQdgkAHX3Z1NTzPhCHiMdZZsFrX13peU6NEtpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 01/10/2026 22:34 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `baff585ef603d502…`
