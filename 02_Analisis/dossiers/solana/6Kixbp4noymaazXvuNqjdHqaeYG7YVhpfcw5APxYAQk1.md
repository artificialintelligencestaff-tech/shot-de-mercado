# Launchpad (LAUNCHPAD) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001793 · liquidez $37.682 · mcap $179.318 (al detectar)  
Detectado el 04/10/2026 18:39 UTC por: young-0.4 · edad 20.5 min · pesos info 55 / estructura 23 / precio 23 · info 14.4 · estructura 14.1 · precio/volumen 13.2 · cobertura 94/100, [info] narrative_wave: ola 'launchpad': 4 lanzamientos más en 1 h → +6.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +4.9 (score 42, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 06/10/2026 18:39 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir LAUNCHPAD

Estudio de cómo se adquiere LAUNCHPAD, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 04/10/2026 18:57 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 04/10/2026 18:39 UTC | pumpswap `Es1Sdha…TuRS` | $37.682 | 10% | 0,531% | 5,308% | 53,076% | $188 | $565 |
| consulta 04/10/2026 18:57 UTC | pumpswap `Es1Sdha…TuRS` | $34.750 | 10% | 0,576% | 5,755% | 57,554% | $174 | $521 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1`
5. Configurar el slippage: 10% (liquidez $34.750, consulta 04/10/2026 18:57 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1) y el par en DexScreener (https://dexscreener.com/solana/Es1SdhajsFJStNtHpPs7g2rdnMFXL2UNa4vtxSWHTuRS); mint authority / freeze authority: revocada / revocada · holders 1.453 · top-10 40,87% (consulta 04/10/2026 18:57 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1
- Par en DexScreener: https://dexscreener.com/solana/Es1SdhajsFJStNtHpPs7g2rdnMFXL2UNa4vtxSWHTuRS
- Página del lanzamiento (pump.fun): https://pump.fun/coin/6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.453 · top-10 40,87% (consulta 04/10/2026 18:57 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Launchpad / LAUNCHPAD | registro de la detección (pumpportal_live) |
| Mint / contrato | `6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Es1SdhajsFJStNtHpPs7g2rdnMFXL2UNa4vtxSWHTuRS` | DexScreener, al detectar (2 par(es) en la consulta 04/10/2026 18:57 UTC) |
| Deployer | `CNnZmRb1TCwSDqqhNvshnJaGYTb9sYTTusoae7KqJUYN` | PumpPortal (evento create), al detectar |
| Par creado | 04/10/2026 18:18 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 20,5 min / 20,5 min / 39,2 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 04/10/2026 18:57 UTC |
| Holders / top-10 | 1.453 / 40,87% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 04/10/2026 18:57 UTC |
| Holders efectivos del top-10 | 5,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 04/10/2026 18:57 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 04/10/2026 18:57 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Es1SdhajsFJStNtHpPs7g2rdnMFXL2UNa4vtxSWHTuRS · Solscan: https://solscan.io/token/6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1 · pump.fun: https://pump.fun/coin/6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1 · twitter: https://x.com/Launchpadtoken | consulta 04/10/2026 18:57 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 04/10/2026 18:57 UTC)
- **Historia:**
  - Par creado el 04/10/2026 18:18 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 04/10/2026 18:39 UTC, con el par a 20,5 min de creado: precio $0,0001793, mcap $179.318, liquidez $37.682.
  - Velas de 1 h de GeckoTerminal (1, desde 04/10/2026 18:00 UTC): apertura $0,00004456 · máximo $0,0002697 (04/10/2026 18:00 UTC) · mínimo $0,00002016 (04/10/2026 18:00 UTC) · último cierre $0,0001265.
  - En la consulta 04/10/2026 18:57 UTC: precio $0,0001516, liquidez $34.750, FDV $151.671.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 04/10/2026 18:39 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001793 |
| Liquidez | $37.682 |
| MCap | $179.318 |
| Volumen 24 h | $304.369 |
| Cambio 24 h | +282% |
| Cambio m5 / h1 | +175,0% / +282,0% |
| Volumen m5 / h1 | $105.337 / $304.369 |
| Trades m5 (compras / ventas) | 621 / 811 |
| Edad del par | 20,5 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 42; motivos sin regla: young-0.4 · edad 20.5 min · pesos info 55 / estructura 23 / precio 23 · info 14.4 · estructura 14.1 · precio/volumen 13.2 · cobertura 94/100, [info] narrative_wave: ola 'launchpad': 4 lanzamientos más en 1 h → +6.8, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 35 caracteres → +4.9, [info] dex_profile: perfil pago en DexScreener → +2.7, [estructura] bonding_progress: graduado (pumpswap) → +10.9, [estructura] holders_struct: holders 1217 · top-10 39.0 % → +2.7, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1217/4604 = 0.26 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×4.2 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +67% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 839→1217 (+31.5/min) · top10 39.9%→39.0% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=37682.11, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=13824.5, score 42 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-04T18:39:08+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 13 de 10.601 tokens analizados (0,12%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 04/10/2026 18:39 UTC, hasta 06/10/2026 18:39 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +175,0% · h1 +282,0% · h24 +282% · volumen m5/h1 0,35 · edad del par 20,5 min.
- **Precio de entrada** (alerta): $0,0001793.
- **Consulta 04/10/2026 18:57 UTC:** $0,0001516 (-15,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1_2026-10-04_183908.json` · blob `a0f1487d5a9eb71e1faea0a759160b8bd0ea1bdb` · commit `281cac2` (2026-10-04T18:50:20Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-04_183908`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1 · registro · 04/10/2026 18:39 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1 · HTTP 200 · 04/10/2026 18:57 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1/report · HTTP 200 · 04/10/2026 18:57 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1 · HTTP 200 · 04/10/2026 18:57 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Es1SdhajsFJStNtHpPs7g2rdnMFXL2UNa4vtxSWHTuRS/ohlcv/hour?limit=1000 · HTTP 200 · 04/10/2026 18:57 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1 · HTTP 404 · 04/10/2026 18:57 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=LAUNCHPADUSDT · HTTP 400 · 04/10/2026 18:57 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/LAUNCHPAD-USD · HTTP 404 · 04/10/2026 18:57 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $34.750 vs $33.771 → 2,82%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001516 vs $0,0001265 → 16,55%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1_2026-10-04_183908.json',encoding='utf-8'));d=d.get('6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1',d);p=mock.patch('time.time',return_value=1791139148);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 6Kixbp4noymaazXvuNqjdHqaeYG7YVhpfcw5APxYAQk1 --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 04/10/2026 18:57 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `d8aa8f24e2937435…`
