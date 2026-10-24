# Trump Coin (TRUMP) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0003107 · liquidez $50.501 · mcap $309.550 (al detectar)  
Detectado el 24/10/2026 16:44 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 26/10/2026 16:44 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir TRUMP

Estudio de cómo se adquiere TRUMP, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 24/10/2026 16:44 UTC; CoinGecko sin ficha para este contrato). Binance tiene un par TRUMPUSDT, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza. Coinbase tiene un par TRUMP-USD, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza.

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 24/10/2026 16:44 UTC | pumpswap `7Yk7UAs…iavU` | $50.501 | 5% | 0,396% | 3,960% | 39,603% | $253 | $758 |
| consulta 24/10/2026 16:44 UTC | pumpswap `7Yk7UAs…iavU` | $42.450 | 10% | 0,471% | 4,711% | 47,114% | $212 | $637 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump`
5. Configurar el slippage: 10% (liquidez $42.450, consulta 24/10/2026 16:44 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump) y el par en DexScreener (https://dexscreener.com/solana/7Yk7UAsViEvP5wkyfapAFS7KySmCnJtpvamxmCMKiavU); mint authority / freeze authority: revocada / revocada · holders 8.667 · top-10 11,54% (consulta 24/10/2026 16:44 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump
- Par en DexScreener: https://dexscreener.com/solana/7Yk7UAsViEvP5wkyfapAFS7KySmCnJtpvamxmCMKiavU
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 8.667 · top-10 11,54% (consulta 24/10/2026 16:44 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Trump Coin / TRUMP | registro de la detección (trending) |
| Mint / contrato | `3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `7Yk7UAsViEvP5wkyfapAFS7KySmCnJtpvamxmCMKiavU` | DexScreener, al detectar (2 par(es) en la consulta 24/10/2026 16:44 UTC) |
| Deployer | `B7gFQrKLtFuJ43N5jPe4YJLcMCH1NbAMKVUv5PAhkzY7` | RugCheck `creator` |
| Par creado | 24/10/2026 02:52 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 13,9 h / 13,9 h / 13,9 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 24/10/2026 16:44 UTC |
| Holders / top-10 | 8.667 / 11,54% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 24/10/2026 16:44 UTC |
| Holders efectivos del top-10 | 1,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 24/10/2026 16:44 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 24/10/2026 16:44 UTC |
| Links | DexScreener: https://dexscreener.com/solana/7Yk7UAsViEvP5wkyfapAFS7KySmCnJtpvamxmCMKiavU · Solscan: https://solscan.io/token/3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump · pump.fun: https://pump.fun/coin/3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump · web: https://trumpcoin.fit · twitter: https://x.com/SolTrumpCoinX · telegram: https://t.me/SolTrumpCoinPortal | consulta 24/10/2026 16:44 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** scanner multi-chain: grupo a (memecoins micro-cap, trending_pools de solana)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 24/10/2026 16:44 UTC)
- **Historia:**
  - Par creado el 24/10/2026 02:52 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 24/10/2026 16:44 UTC, con el par a 13,9 h de creado: precio $0,0003107, mcap $309.550, liquidez $50.501.
  - Velas de 1 h de GeckoTerminal (15, desde 24/10/2026 02:00 UTC): apertura $0,0004097 · máximo $0,001941 (24/10/2026 04:00 UTC) · mínimo $0,00005101 (24/10/2026 02:00 UTC) · último cierre $0,0002341.
  - En la consulta 24/10/2026 16:44 UTC: precio $0,0002216, liquidez $42.450, FDV $220.749.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 24/10/2026 16:44 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0003107 |
| Liquidez | $50.501 |
| MCap | $309.550 |
| Volumen 24 h | $4.057.342 |
| Cambio 24 h | +504% |
| Cambio m5 / h1 | +78,2% / -42,0% |
| Volumen m5 / h1 | $103.336 / $236.500 |
| Trades m5 (compras / ventas) | 714 / 428 |
| Edad del par | 13,9 h |
| Score del feed (WS) | 67 |

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
| Score del feed | score WS × 0,3 | WS 67 × 0,3 | +20,1 |
| MCap | ≥ $100K | $309.550 | +15 |
| Volumen 24 h | ≥ $1M | $4.057.342 | +20 |
| Volumen m5/h1 | > 0,25 (par maduro) | 0,44 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 63% | +25 |
| Volumen m5 | > $1K (par maduro) | $103.336 | +10 |
| Liquidez | ≥ $50K | $50.501 | +10 |
| Cambio 24 h | ≥ +50% | +504% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +504% · liq/mcap 16,3% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-24T16:44:04+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Volumen en aceleración (5m/1h > 25%), Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=16.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 76 de 45.724 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 24/10/2026 16:44 UTC, hasta 26/10/2026 16:44 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 +78,2% · h1 -42,0% · h24 +504% · volumen m5/h1 0,44 · edad del par 13,9 h.
- **Precio de entrada** (alerta): $0,0003107.
- **Consulta 24/10/2026 16:44 UTC:** $0,0002216 (-28,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump_2026-10-24_164431.json` · blob `7ced6c08f5286fc37ff3659488fa8b5efef86c1c` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-24_163859.json` · blob `9a17f47282eb65959f946ba198e022b72a8badfe` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-24_164431`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump · registro · 24/10/2026 16:44 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump · HTTP 200 · 24/10/2026 16:44 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump/report · HTTP 200 · 24/10/2026 16:44 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump · HTTP 200 · 24/10/2026 16:44 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/7Yk7UAsViEvP5wkyfapAFS7KySmCnJtpvamxmCMKiavU/ohlcv/hour?limit=1000 · HTTP 200 · 24/10/2026 16:44 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump · HTTP 404 · 24/10/2026 16:44 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=TRUMPUSDT · HTTP 200 · 24/10/2026 16:44 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/TRUMP-USD · HTTP 200 · 24/10/2026 16:44 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $42.450 vs $43.651 → 2,75%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0002216 vs $0,0002341 → 5,32%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump_2026-10-24_164431.json',encoding='utf-8'));d=d.get('3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump',d);p=mock.patch('time.time',return_value=1792860244);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3YYqFkPaob7SzUCyk59DGVhPZK1LN9odKMJc1uy3pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 24/10/2026 16:44 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `e1cca837bbb6ebb1…`
