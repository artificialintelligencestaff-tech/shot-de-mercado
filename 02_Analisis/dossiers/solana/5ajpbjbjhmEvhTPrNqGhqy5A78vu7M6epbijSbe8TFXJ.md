# The Solana Fox (Fox) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00001580 · liquidez $9.626 · mcap $15.801 (al detectar)  
Detectado el 06/10/2026 09:41 UTC por: young-0.4 · edad 11.2 min · pesos info 59 / estructura 20 / precio 20 · info 23.1 · estructura 13.7 · precio/volumen 8.5 · cobertura 93/100, [info] narrative_wave: ola 'fox': 15 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 45, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 08/10/2026 09:41 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Fox

Estudio de cómo se adquiere Fox, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 09:57 UTC; CoinGecko sin ficha para este contrato). Coinbase tiene un par FOX-USD, pero CoinGecko no lo vincula a este contrato (puede ser otro token con el mismo símbolo): no se enlaza.

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 09:41 UTC | pumpswap `HB6mjqo…niin` | $9.626 | 10% | 2,078% | 20,778% | 207,776% | $48 | $144 |
| consulta 06/10/2026 09:57 UTC | pumpswap `HB6mjqo…niin` | $15.431 | 10% | 1,296% | 12,961% | 129,611% | $77 | $231 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ`
5. Configurar el slippage: 10% (liquidez $15.431, consulta 06/10/2026 09:57 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ) y el par en DexScreener (https://dexscreener.com/solana/HB6mjqob8hb3x5cWngmSQHtGiFwJfwgPkEfKEoJQniin); mint authority / freeze authority: revocada / revocada · holders 1.606 · top-10 42,37% (consulta 06/10/2026 09:57 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ
- Par en DexScreener: https://dexscreener.com/solana/HB6mjqob8hb3x5cWngmSQHtGiFwJfwgPkEfKEoJQniin
- Página del lanzamiento (pump.fun): https://pump.fun/coin/5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.606 · top-10 42,37% (consulta 06/10/2026 09:57 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | The Solana Fox / Fox | registro de la detección (pumpportal_live) |
| Mint / contrato | `5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HB6mjqob8hb3x5cWngmSQHtGiFwJfwgPkEfKEoJQniin` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 09:57 UTC) |
| Deployer | `3hWXW8BJoy1awjywwebcRgyLvKqNqjC7yxEMfzu6UYfd` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 09:30 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,2 min / 11,2 min / 27,3 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 09:57 UTC |
| Holders / top-10 | 1.606 / 42,37% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 09:57 UTC |
| Holders efectivos del top-10 | 3,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 09:57 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 09:57 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HB6mjqob8hb3x5cWngmSQHtGiFwJfwgPkEfKEoJQniin · Solscan: https://solscan.io/token/5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ · pump.fun: https://pump.fun/coin/5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ · twitter: https://twitter.com/Stally_P/status/2107402013067690362 · instagram: https://www.instagram.com/p/Dd_ipmBIKZW/?utm_source=ig_embed&ig_rid=AUqE9chJwqXPOGq95WIDIUu&img_index=2 | consulta 06/10/2026 09:57 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 09:57 UTC)
- **Historia:**
  - Par creado el 06/10/2026 09:30 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 09:41 UTC, con el par a 11,2 min de creado: precio $0,00001580, mcap $15.801, liquidez $9.626.
  - Velas de 1 h de GeckoTerminal (1, desde 06/10/2026 09:00 UTC): apertura $0,00004930 · máximo $0,00009283 (06/10/2026 09:00 UTC) · mínimo $0,00001446 (06/10/2026 09:00 UTC) · último cierre $0,00004657.
  - En la consulta 06/10/2026 09:57 UTC: precio $0,00003528, liquidez $15.431, FDV $35.280.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 09:41 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00001580 |
| Liquidez | $9.626 |
| MCap | $15.801 |
| Volumen 24 h | $232.064 |
| Cambio 24 h | -68% |
| Cambio m5 / h1 | -72,9% / -67,8% |
| Volumen m5 / h1 | $82.821 / $232.064 |
| Trades m5 (compras / ventas) | 1.055 / 823 |
| Edad del par | 11,2 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 45; motivos sin regla: young-0.4 · edad 11.2 min · pesos info 59 / estructura 20 / precio 20 · info 23.1 · estructura 13.7 · precio/volumen 8.5 · cobertura 93/100, [info] narrative_wave: ola 'fox': 15 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1400 · top-10 42.7 % → +2.4, [estructura] dev_wallet: creador compró 6.7 % del supply → +1.0, [estructura] holder_to_txn_ratio: holders/txns 1400/4687 = 0.30 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×4.3 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 56% en 5 min vs 56% en 1 h (s 0.02), [precio/volumen] holder_accumulation: holders 820→1400 (+96.7/min) · top10 38.1%→42.7% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=9625.73, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 45 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T09:41:13+00:00, sin estado previo): **10** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 18 de 14.848 tokens analizados (0,12%) quedan ≥ 56. Con score 10, este activo queda en el percentil 93,5 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 09:41 UTC, hasta 08/10/2026 09:41 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -72,9% · h1 -67,8% · h24 -68% · volumen m5/h1 0,36 · edad del par 11,2 min.
- **Precio de entrada** (alerta): $0,00001580.
- **Consulta 06/10/2026 09:57 UTC:** $0,00003528 (+123,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ_2026-10-06_094113.json` · blob `94aa4b4d608a77a809c114fde75d7a13f5286e40` · commit `0dadfa7` (2026-10-06T09:51:08Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_094113`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ · registro · 06/10/2026 09:41 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ · HTTP 200 · 06/10/2026 09:57 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ/report · HTTP 200 · 06/10/2026 09:57 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ · HTTP 200 · 06/10/2026 09:57 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HB6mjqob8hb3x5cWngmSQHtGiFwJfwgPkEfKEoJQniin/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 09:57 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ · HTTP 404 · 06/10/2026 09:57 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=FOXUSDT · HTTP 400 · 06/10/2026 09:57 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/FOX-USD · HTTP 200 · 06/10/2026 09:57 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $15.431 vs $15.493 → 0,40%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00003528 vs $0,00004657 → 24,25%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ_2026-10-06_094113.json',encoding='utf-8'));d=d.get('5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ',d);p=mock.patch('time.time',return_value=1791279673);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 5ajpbjbjhmEvhTPrNqGhqy5A78vu7M6epbijSbe8TFXJ --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 09:57 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `9deb03c9bb38ab36…`
