# Bully (BULLY) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00005649 · liquidez $19.098 · mcap $56.492 (al detectar)  
Detectado el 20/10/2026 00:45 UTC por: young-0.4 · edad 11.3 min · pesos info 59 / estructura 20 / precio 20 · info 17.8 · estructura 12.9 · precio/volumen 11.9 · cobertura 84/100, [info] narrative_wave: ola 'bully': 10 lanzamientos más en 1 h → +14.8, [info] dex_profile: perfil pago en DexScreener → +3.0 (score 43, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 22/10/2026 00:45 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir BULLY

Estudio de cómo se adquiere BULLY, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 20/10/2026 01:12 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 20/10/2026 00:45 UTC | pumpswap `31ZPBi5…R8Qg` | $19.098 | 10% | 1,047% | 10,472% | 104,721% | $95 | $286 |
| consulta 20/10/2026 01:12 UTC | pumpswap `31ZPBi5…R8Qg` | $7.852 | 10% | 2,547% | 25,470% | 254,703% | $39 | $118 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump`
5. Configurar el slippage: 10% (liquidez $7.852, consulta 20/10/2026 01:12 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump) y el par en DexScreener (https://dexscreener.com/solana/31ZPBi5ZPvu82HH7nFVgESLNmwi1rfWzt2hWk6qbR8Qg); mint authority / freeze authority: revocada / revocada · holders 1.354 · top-10 63,28% (consulta 20/10/2026 01:12 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump
- Par en DexScreener: https://dexscreener.com/solana/31ZPBi5ZPvu82HH7nFVgESLNmwi1rfWzt2hWk6qbR8Qg
- Página del lanzamiento (pump.fun): https://pump.fun/coin/6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.354 · top-10 63,28% (consulta 20/10/2026 01:12 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Bully / BULLY | registro de la detección (pumpportal_live) |
| Mint / contrato | `6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `31ZPBi5ZPvu82HH7nFVgESLNmwi1rfWzt2hWk6qbR8Qg` | DexScreener, al detectar (2 par(es) en la consulta 20/10/2026 01:12 UTC) |
| Deployer | `DJQwtiowTJmAvAu4vhCaFgPiS3nnKD5r5agZgBQEdHK2` | PumpPortal (evento create), al detectar |
| Par creado | 20/10/2026 00:34 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,3 min / 11,3 min / 38,3 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 20/10/2026 01:12 UTC |
| Holders / top-10 | 1.354 / 63,28% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 20/10/2026 01:12 UTC |
| Holders efectivos del top-10 | 2,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 20/10/2026 01:12 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 20/10/2026 01:12 UTC |
| Links | DexScreener: https://dexscreener.com/solana/31ZPBi5ZPvu82HH7nFVgESLNmwi1rfWzt2hWk6qbR8Qg · Solscan: https://solscan.io/token/6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump · pump.fun: https://pump.fun/coin/6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump · web: https://github.com/oh-ashen-one/bully-remake · twitter: https://x.com/Bymotionn/status/2112340654017609852 | consulta 20/10/2026 01:12 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 20/10/2026 01:12 UTC)
- **Historia:**
  - Par creado el 20/10/2026 00:34 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 20/10/2026 00:45 UTC, con el par a 11,3 min de creado: precio $0,00005649, mcap $56.492, liquidez $19.098.
  - Velas de 1 h de GeckoTerminal (2, desde 20/10/2026 00:00 UTC): apertura $0,00004485 · máximo $0,00007610 (20/10/2026 00:00 UTC) · mínimo $0,00001126 (20/10/2026 01:00 UTC) · último cierre $0,00001359.
  - En la consulta 20/10/2026 01:12 UTC: precio $0,00001231, liquidez $7.852, FDV $11.596.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 20/10/2026 00:45 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00005649 |
| Liquidez | $19.098 |
| MCap | $56.492 |
| Volumen 24 h | $117.450 |
| Cambio 24 h | +25% |
| Cambio m5 / h1 | +10,5% / +24,7% |
| Volumen m5 / h1 | $42.784 / $117.450 |
| Trades m5 (compras / ventas) | 713 / 521 |
| Edad del par | 11,3 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 43; motivos sin regla: young-0.4 · edad 11.3 min · pesos info 59 / estructura 20 / precio 20 · info 17.8 · estructura 12.9 · precio/volumen 11.9 · cobertura 84/100, [info] narrative_wave: ola 'bully': 10 lanzamientos más en 1 h → +14.8, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 1026 · top-10 44.8 % → +2.4, [estructura] dev_wallet: creador compró 9.6 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1026/2920 = 0.35 → +0.6, [precio/volumen] volume_acceleration: vol 5 min ×4.4 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +35% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 601→1026 (+70.8/min) · top10 46.5%→44.8% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=19098.39, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 43 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-20T00:45:25+00:00, sin estado previo): **30** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen alto, Liquidez baja, Subida 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 67 de 41.480 tokens analizados (0,16%) quedan ≥ 56. Con score 30, este activo queda en el percentil 97,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 20/10/2026 00:45 UTC, hasta 22/10/2026 00:45 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +10,5% · h1 +24,7% · h24 +25% · volumen m5/h1 0,36 · edad del par 11,3 min.
- **Precio de entrada** (alerta): $0,00005649.
- **Consulta 20/10/2026 01:12 UTC:** $0,00001231 (-78,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump_2026-10-20_004525.json` · blob `8acad0d27c9b76fc27fc26080eaa2f21cf47bd2a` · commit `e51f1cf` (2026-10-20T01:05:45Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-20_004525`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump · registro · 20/10/2026 00:45 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump · HTTP 200 · 20/10/2026 01:12 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump/report · HTTP 200 · 20/10/2026 01:12 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump · HTTP 200 · 20/10/2026 01:12 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/31ZPBi5ZPvu82HH7nFVgESLNmwi1rfWzt2hWk6qbR8Qg/ohlcv/hour?limit=1000 · HTTP 200 · 20/10/2026 01:12 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump · HTTP 404 · 20/10/2026 01:12 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BULLYUSDT · HTTP 400 · 20/10/2026 01:12 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BULLY-USD · HTTP 404 · 20/10/2026 01:12 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $7.852 vs $8.144 → 3,58%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00001231 vs $0,00001359 → 9,45%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump_2026-10-20_004525.json',encoding='utf-8'));d=d.get('6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump',d);p=mock.patch('time.time',return_value=1792457125);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 6tgusToBREdH1PqFhAgjo8hrBrXmYjpUzJm4mDWnpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 20/10/2026 01:12 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `e0904f36f50c715d…`
