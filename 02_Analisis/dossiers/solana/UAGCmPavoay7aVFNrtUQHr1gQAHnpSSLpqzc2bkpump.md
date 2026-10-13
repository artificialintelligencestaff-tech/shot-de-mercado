# SpxNyxo (SPX) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003688 · liquidez $164.482 · mcap $3.686.865 (al detectar)  
Detectado el 13/10/2026 02:56 UTC por: MCap > $1M, Volumen decente, Buy pressure >55% (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 15/10/2026 02:56 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SPX

Estudio de cómo se adquiere SPX, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 13/10/2026 03:15 UTC; CoinGecko sin ficha para este contrato). Coinbase tiene un par SPX-USD, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza.

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 13/10/2026 02:56 UTC | pumpswap `5K1DgWp…bAZb` | $164.482 | 5% | 0,122% | 1,216% | 12,159% | $822 | $2.467 |
| consulta 13/10/2026 03:15 UTC | pumpswap `5K1DgWp…bAZb` | $164.696 | 5% | 0,121% | 1,214% | 12,144% | $823 | $2.470 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump`
5. Configurar el slippage: 5% (liquidez $164.696, consulta 13/10/2026 03:15 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump) y el par en DexScreener (https://dexscreener.com/solana/5K1DgWpuj9GFUBVBahpKfvVLQdjzuNvAbyYUohjBbAZb); mint authority / freeze authority: revocada / revocada · holders 4.047 · top-10 2,54% (consulta 13/10/2026 03:15 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump
- Par en DexScreener: https://dexscreener.com/solana/5K1DgWpuj9GFUBVBahpKfvVLQdjzuNvAbyYUohjBbAZb
- Página del lanzamiento (pump.fun): https://pump.fun/coin/UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.047 · top-10 2,54% (consulta 13/10/2026 03:15 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | SpxNyxo / SPX | registro de la detección (pumpportal) |
| Mint / contrato | `UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `5K1DgWpuj9GFUBVBahpKfvVLQdjzuNvAbyYUohjBbAZb` | DexScreener, al detectar (2 par(es) en la consulta 13/10/2026 03:15 UTC) |
| Deployer | `ejsz5GEaS9Z8gprPcHfD6odpZBPnNFw6VJruCP4BNw8` | PumpPortal (evento create), al detectar |
| Par creado | 13/10/2026 01:55 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,4 min / 60,4 min / 79,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 13/10/2026 03:15 UTC |
| Holders / top-10 | 4.047 / 2,54% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 13/10/2026 03:15 UTC |
| Holders efectivos del top-10 | 1,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 13/10/2026 03:15 UTC |
| Etiquetas de RugCheck | «High holder correlation», «Copycat token» | RugCheck `risks[].name` (texto de la fuente), consulta 13/10/2026 03:15 UTC |
| Links | DexScreener: https://dexscreener.com/solana/5K1DgWpuj9GFUBVBahpKfvVLQdjzuNvAbyYUohjBbAZb · Solscan: https://solscan.io/token/UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump · pump.fun: https://pump.fun/coin/UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump · web / Telegram / X: no publicados en DexScreener | consulta 13/10/2026 03:15 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 13/10/2026 03:15 UTC)
- **Historia:**
  - Par creado el 13/10/2026 01:55 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 13/10/2026 02:56 UTC, con el par a 60,4 min de creado: precio $0,003688, mcap $3.686.865, liquidez $164.482.
  - Velas de 1 h de GeckoTerminal (3, desde 13/10/2026 01:00 UTC): apertura $0,003440 · máximo $0,003739 (13/10/2026 02:00 UTC) · mínimo $0,00004372 (13/10/2026 01:00 UTC) · último cierre $0,003692.
  - En la consulta 13/10/2026 03:15 UTC: precio $0,003695, liquidez $164.696, FDV $3.693.082.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 13/10/2026 02:56 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003688 |
| Liquidez | $164.482 |
| MCap | $3.686.865 |
| Volumen 24 h | $77.084 |
| Cambio 24 h | +8.341% |
| Cambio m5 / h1 | +0,5% / +6,1% |
| Volumen m5 / h1 | $687 / $6.126 |
| Trades m5 (compras / ventas) | 11 / 8 |
| Edad del par | 60,4 min |
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
| MCap | ≥ $1M | $3.686.865 | +25 |
| Volumen 24 h | ≥ $50K | $77.084 | +10 |
| Buy pressure m5 | > 55% (par maduro) | 58% | +15 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,5% · h1 +6,1% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,4 min | +8 |
| Volumen m5 | > $500 (par maduro) | $687 | +5 |
| Liquidez | ≥ $100K | $164.482 | +15 |
| Cambio 24 h | ≥ +50% | +8.341% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +8.341% · liq/mcap 4,5% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-13T02:56:10+00:00, sin estado previo): **100** · motivos: MCap > $1M, Volumen decente, Buy pressure >55%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 52 de 32.569 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 13/10/2026 02:56 UTC, hasta 15/10/2026 02:56 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +0,5% · h1 +6,1% · h24 +8.341% · volumen m5/h1 0,11 · edad del par 60,4 min.
- **Precio de entrada** (alerta): $0,003688.
- **Consulta 13/10/2026 03:15 UTC:** $0,003695 (+0,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump_2026-10-13_025610.json` · blob `f93bc7be56f892cb5abc80f145569f60d2815829` · commit `c2ed490` (2026-10-13T03:07:14Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-13_025610`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump · registro · 13/10/2026 02:56 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump · HTTP 200 · 13/10/2026 03:15 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump/report · HTTP 200 · 13/10/2026 03:15 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump · HTTP 200 · 13/10/2026 03:15 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/5K1DgWpuj9GFUBVBahpKfvVLQdjzuNvAbyYUohjBbAZb/ohlcv/hour?limit=1000 · HTTP 200 · 13/10/2026 03:15 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump · HTTP 404 · 13/10/2026 03:15 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SPXUSDT · HTTP 400 · 13/10/2026 03:15 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SPX-USD · HTTP 200 · 13/10/2026 03:15 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $164.696 vs $164.591 → 0,06%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003695 vs $0,003692 → 0,09%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump_2026-10-13_025610.json',encoding='utf-8'));d=d.get('UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump',d);p=mock.patch('time.time',return_value=1791860170);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint UAGCmPavoay7aVFNrtUQHr1gQAHnpSSLpqzc2bkpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 13/10/2026 03:15 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `069c08aa2ea07edf…`
