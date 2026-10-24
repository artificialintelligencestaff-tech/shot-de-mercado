# dope wif sword (SWORDOPE) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,002628 · liquidez $147.788 · mcap $2.616.568 (al detectar)  
Detectado el 24/10/2026 23:45 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 26/10/2026 23:46 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SWORDOPE

Estudio de cómo se adquiere SWORDOPE, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 24/10/2026 23:46 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 24/10/2026 23:45 UTC | pumpswap `3tXP9X2…3MAq` | $147.788 | 5% | 0,135% | 1,353% | 13,533% | $739 | $2.217 |
| consulta 24/10/2026 23:46 UTC | pumpswap `3tXP9X2…3MAq` | $146.883 | 5% | 0,136% | 1,362% | 13,616% | $734 | $2.203 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump`
5. Configurar el slippage: 5% (liquidez $146.883, consulta 24/10/2026 23:46 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump) y el par en DexScreener (https://dexscreener.com/solana/3tXP9X2W1aL9jtZF1tuAwEZMuX4w3PWNvVAHPJjd3MAq); mint authority / freeze authority: revocada / revocada · holders 7.071 · top-10 11,78% (consulta 24/10/2026 23:46 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump
- Par en DexScreener: https://dexscreener.com/solana/3tXP9X2W1aL9jtZF1tuAwEZMuX4w3PWNvVAHPJjd3MAq
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 7.071 · top-10 11,78% (consulta 24/10/2026 23:46 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | dope wif sword / SWORDOPE | registro de la detección (trending) |
| Mint / contrato | `3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `3tXP9X2W1aL9jtZF1tuAwEZMuX4w3PWNvVAHPJjd3MAq` | DexScreener, al detectar (2 par(es) en la consulta 24/10/2026 23:46 UTC) |
| Deployer | `F6rvtDs1CWMjWK12RXisHWsppJFFNEPjLCHxbFfCSRxj` | RugCheck `creator` |
| Par creado | 24/10/2026 19:44 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 4,0 h / 4,0 h / 4,0 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 24/10/2026 23:46 UTC |
| Holders / top-10 | 7.071 / 11,78% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 24/10/2026 23:46 UTC |
| Holders efectivos del top-10 | 8,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 24/10/2026 23:46 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 24/10/2026 23:46 UTC |
| Links | DexScreener: https://dexscreener.com/solana/3tXP9X2W1aL9jtZF1tuAwEZMuX4w3PWNvVAHPJjd3MAq · Solscan: https://solscan.io/token/3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump · pump.fun: https://pump.fun/coin/3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump · web: https://swordope.fun · twitter: https://x.com/Swordope · telegram: https://t.me/swordope | consulta 24/10/2026 23:46 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 24/10/2026 23:46 UTC)
- **Historia:**
  - Par creado el 24/10/2026 19:44 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 24/10/2026 23:45 UTC, con el par a 4,0 h de creado: precio $0,002628, mcap $2.616.568, liquidez $147.788.
  - Velas de 1 h de GeckoTerminal (5, desde 24/10/2026 19:00 UTC): apertura $0,0003169 · máximo $0,003936 (24/10/2026 23:00 UTC) · mínimo $0,00005524 (24/10/2026 19:00 UTC) · último cierre $0,002600.
  - En la consulta 24/10/2026 23:46 UTC: precio $0,002596, liquidez $146.883, FDV $2.584.588.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 24/10/2026 23:45 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,002628 |
| Liquidez | $147.788 |
| MCap | $2.616.568 |
| Volumen 24 h | $3.817.538 |
| Cambio 24 h | +4.619% |
| Cambio m5 / h1 | -4,6% / +6,5% |
| Volumen m5 / h1 | $19.493 / $485.340 |
| Trades m5 (compras / ventas) | 713 / 233 |
| Edad del par | 4,0 h |
| Score del feed (WS) | 68 |

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
| Score del feed | score WS × 0,3 | WS 68 × 0,3 | +20,5 |
| MCap | ≥ $1M | $2.616.568 | +25 |
| Volumen 24 h | ≥ $1M | $3.817.538 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 75% | +25 |
| Volumen m5 | > $1K (par maduro) | $19.493 | +10 |
| Liquidez | ≥ $100K | $147.788 | +15 |
| Cambio 24 h | ≥ +50% | +4.619% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +4.619% · liq/mcap 5,6% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-24T23:45:51+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=5.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 76 de 45.847 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 24/10/2026 23:46 UTC, hasta 26/10/2026 23:46 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -4,6% · h1 +6,5% · h24 +4.619% · volumen m5/h1 0,04 · edad del par 4,0 h.
- **Precio de entrada** (alerta): $0,002628.
- **Consulta 24/10/2026 23:46 UTC:** $0,002596 (-1,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump_2026-10-24_234614.json` · blob `c8397be37ca412c40492d00d4897c2d5fc0a969c` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-24_234044.json` · blob `77df68de13efa8d799b8385f805e4c9af04f6c73` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-24_234614`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump · registro · 24/10/2026 23:45 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump · HTTP 200 · 24/10/2026 23:46 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump/report · HTTP 200 · 24/10/2026 23:46 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump · HTTP 200 · 24/10/2026 23:46 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/3tXP9X2W1aL9jtZF1tuAwEZMuX4w3PWNvVAHPJjd3MAq/ohlcv/hour?limit=1000 · HTTP 200 · 24/10/2026 23:46 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump · HTTP 404 · 24/10/2026 23:46 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SWORDOPEUSDT · HTTP 400 · 24/10/2026 23:46 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SWORDOPE-USD · HTTP 404 · 24/10/2026 23:46 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $146.883 vs $149.618 → 1,83%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002596 vs $0,002600 → 0,17%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump_2026-10-24_234614.json',encoding='utf-8'));d=d.get('3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump',d);p=mock.patch('time.time',return_value=1792885551);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 24/10/2026 23:46 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `3a624164b445ad83…`
