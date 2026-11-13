# The Chud (CHUD) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00008700 · liquidez $21.026 · mcap $86.855 (al detectar)  
Detectado el 13/11/2026 17:11 UTC por: young-0.4 · edad 10.7 min · pesos info 60 / estructura 20 / precio 20 · info 14.6 · estructura 16.9 · precio/volumen 11.8 · cobertura 93/100, [info] narrative_wave: ola 'chud': 5 lanzamientos más en 1 h → +9.3, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 43, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 15/11/2026 17:11 UTC (< 48 h) · vigente: quedan 43,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir CHUD

Estudio de cómo se adquiere CHUD, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 13/11/2026 21:42 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 13/11/2026 17:11 UTC | pumpswap `E8LQz9r…8jtb` | $21.026 | 10% | 0,951% | 9,512% | 95,123% | $105 | $315 |
| consulta 13/11/2026 21:41 UTC | pumpswap `E8LQz9r…8jtb` | $1.658 | 10% | 12,065% | 120,654% | 1.206,542% | $8 | $25 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump`
5. Configurar el slippage: 10% (liquidez $1.658, consulta 13/11/2026 21:41 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump) y el par en DexScreener (https://dexscreener.com/solana/E8LQz9rbUvsytRzSUTVcGZFGz2EoXK5x5arWvtYy8jtb); mint authority / freeze authority: revocada / revocada · holders 288 · top-10 98,42% (consulta 13/11/2026 21:41 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump
- Par en DexScreener: https://dexscreener.com/solana/E8LQz9rbUvsytRzSUTVcGZFGz2EoXK5x5arWvtYy8jtb
- Página del lanzamiento (pump.fun): https://pump.fun/coin/JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 288 · top-10 98,42% (consulta 13/11/2026 21:41 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | The Chud / CHUD | registro de la detección (pumpportal_live) |
| Mint / contrato | `JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `E8LQz9rbUvsytRzSUTVcGZFGz2EoXK5x5arWvtYy8jtb` | DexScreener, al detectar (3 par(es) en la consulta 13/11/2026 21:41 UTC) |
| Deployer | `HS4vGvf3XTU7vkisWcSiFjdqadPF4QMf6Rf2Pzk6tJHf` | PumpPortal (evento create), al detectar |
| Par creado | 13/11/2026 17:01 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,7 min / 10,7 min / 4,7 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 13/11/2026 21:41 UTC |
| Holders / top-10 | 288 / 98,42% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 13/11/2026 21:41 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 13/11/2026 21:41 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 13/11/2026 21:41 UTC |
| Links | DexScreener: https://dexscreener.com/solana/E8LQz9rbUvsytRzSUTVcGZFGz2EoXK5x5arWvtYy8jtb · Solscan: https://solscan.io/token/JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump · pump.fun: https://pump.fun/coin/JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump · web / Telegram / X: no publicados en DexScreener | consulta 13/11/2026 21:41 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 13/11/2026 21:41 UTC)
- **Historia:**
  - Par creado el 13/11/2026 17:01 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 13/11/2026 17:11 UTC, con el par a 10,7 min de creado: precio $0,00008700, mcap $86.855, liquidez $21.026.
  - Velas de 1 h de GeckoTerminal (3, desde 13/11/2026 17:00 UTC): apertura $0,00003298 · máximo $0,0001105 (13/11/2026 17:00 UTC) · mínimo $0,000001602 (13/11/2026 21:00 UTC) · último cierre $0,000001602.
  - En la consulta 13/11/2026 21:41 UTC: precio $0,000001604, liquidez $1.658, FDV $1.548.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 13/11/2026 17:11 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00008700 |
| Liquidez | $21.026 |
| MCap | $86.855 |
| Volumen 24 h | $100.544 |
| Cambio 24 h | +164% |
| Cambio m5 / h1 | +65,7% / +164,0% |
| Volumen m5 / h1 | $37.228 / $100.544 |
| Trades m5 (compras / ventas) | 1.158 / 779 |
| Edad del par | 10,7 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 43; motivos sin regla: young-0.4 · edad 10.7 min · pesos info 60 / estructura 20 / precio 20 · info 14.6 · estructura 16.9 · precio/volumen 11.8 · cobertura 93/100, [info] narrative_wave: ola 'chud': 5 lanzamientos más en 1 h → +9.3, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 923 · top-10 20.4 % → +4.8, [estructura] dev_wallet: creador compró 3.1 % del supply → +2.1, [estructura] holder_to_txn_ratio: holders/txns 923/4850 = 0.19 → +0.3, [precio/volumen] volume_acceleration: vol 5 min ×4.4 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +59% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 617→923 (+51.0/min) · top10 27.1%→20.4% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=21025.5, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 43 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-13T17:11:51+00:00, sin estado previo): **40** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 100 de 47.172 tokens analizados (0,21%) quedan ≥ 56. Con score 40, este activo queda en el percentil 99,6 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 13/11/2026 17:11 UTC, hasta 15/11/2026 17:11 UTC · vigente: quedan 43,5 h.
- **Aceleración al detectar:** cambio m5 +65,7% · h1 +164,0% · h24 +164% · volumen m5/h1 0,37 · edad del par 10,7 min.
- **Precio de entrada** (alerta): $0,00008700.
- **Consulta 13/11/2026 21:41 UTC:** $0,000001604 (-98,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump_2026-11-13_171151.json` · blob `a1f4d976175184f9e1f047b91d650fd2b0378da8` · commit `afa809e` (2026-11-13T21:34:19Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-13_171151`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump · registro · 13/11/2026 17:11 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump · HTTP 200 · 13/11/2026 21:41 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump/report · HTTP 200 · 13/11/2026 21:42 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump · HTTP 200 · 13/11/2026 21:42 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/E8LQz9rbUvsytRzSUTVcGZFGz2EoXK5x5arWvtYy8jtb/ohlcv/hour?limit=1000 · HTTP 200 · 13/11/2026 21:42 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump · HTTP 404 · 13/11/2026 21:42 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=CHUDUSDT · HTTP 400 · 13/11/2026 21:42 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/CHUD-USD · HTTP 404 · 13/11/2026 21:42 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.658 vs $1.654 → 0,24%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000001604 vs $0,000001602 → 0,12%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump_2026-11-13_171151.json',encoding='utf-8'));d=d.get('JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump',d);p=mock.patch('time.time',return_value=1794589911);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint JBe58zq8soWT9cHkh2ZbqCQpDCYpdSW38fGDWYzEpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 13/11/2026 21:42 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `c63d818c39b2740f…`
