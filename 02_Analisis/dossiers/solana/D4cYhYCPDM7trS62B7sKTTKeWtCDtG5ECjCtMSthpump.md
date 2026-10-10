# 泣きじゃくる犬 (SOBDOG) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0001669 · liquidez $35.429 · mcap $166.979 (al detectar)  
Detectado el 10/10/2026 08:50 UTC por: young-0.4 · edad 13.0 min · pesos info 59 / estructura 21 / precio 21 · info 17.3 · estructura 15.8 · precio/volumen 12.1 · cobertura 93/100, [info] narrative_wave: ola 'sobdog': 5 lanzamientos más en 1 h → +9.1, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.2 (score 45, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 12/10/2026 08:50 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SOBDOG

Estudio de cómo se adquiere SOBDOG, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 10/10/2026 09:12 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 10/10/2026 08:50 UTC | pumpswap `85GXpjw…kcvr` | $35.429 | 10% | 0,565% | 5,645% | 56,452% | $177 | $531 |
| consulta 10/10/2026 09:11 UTC | pumpswap `85GXpjw…kcvr` | $33.397 | 10% | 0,599% | 5,989% | 59,886% | $167 | $501 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump`
5. Configurar el slippage: 10% (liquidez $33.397, consulta 10/10/2026 09:11 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump) y el par en DexScreener (https://dexscreener.com/solana/85GXpjwt31qLTUxyRVMjQZdKtBSAkFsdHNmuW41kcvr); mint authority / freeze authority: revocada / revocada · holders 2.795 · top-10 30,51% (consulta 10/10/2026 09:11 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump
- Par en DexScreener: https://dexscreener.com/solana/85GXpjwt31qLTUxyRVMjQZdKtBSAkFsdHNmuW41kcvr
- Página del lanzamiento (pump.fun): https://pump.fun/coin/D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.795 · top-10 30,51% (consulta 10/10/2026 09:11 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | 泣きじゃくる犬 / SOBDOG | registro de la detección (pumpportal_live) |
| Mint / contrato | `D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `85GXpjwt31qLTUxyRVMjQZdKtBSAkFsdHNmuW41kcvr` | DexScreener, al detectar (4 par(es) en la consulta 10/10/2026 09:11 UTC) |
| Deployer | `FvWSzwt1eEyVUHwxk5FuMdqJK2eopbLpZzvbB7dVbCYP` | PumpPortal (evento create), al detectar |
| Par creado | 10/10/2026 08:37 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 13,0 min / 13,0 min / 34,7 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 10/10/2026 09:11 UTC |
| Holders / top-10 | 2.795 / 30,51% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 10/10/2026 09:11 UTC |
| Holders efectivos del top-10 | 5,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 10/10/2026 09:11 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 10/10/2026 09:11 UTC |
| Links | DexScreener: https://dexscreener.com/solana/85GXpjwt31qLTUxyRVMjQZdKtBSAkFsdHNmuW41kcvr · Solscan: https://solscan.io/token/D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump · pump.fun: https://pump.fun/coin/D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump · web: https://x.com/search?q=%E3%81%AA%E3%81%9C&src=typed_query · twitter: https://x.com/Bertn2if/status/2108837324658524590 | consulta 10/10/2026 09:11 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 10/10/2026 09:11 UTC)
- **Historia:**
  - Par creado el 10/10/2026 08:37 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 10/10/2026 08:50 UTC, con el par a 13,0 min de creado: precio $0,0001669, mcap $166.979, liquidez $35.429.
  - Velas de 1 h de GeckoTerminal (2, desde 10/10/2026 08:00 UTC): apertura $0,00004375 · máximo $0,0002239 (10/10/2026 08:00 UTC) · mínimo $0,00003908 (10/10/2026 08:00 UTC) · último cierre $0,0001388.
  - En la consulta 10/10/2026 09:11 UTC: precio $0,0001467, liquidez $33.397, FDV $146.743.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 10/10/2026 08:50 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0001669 |
| Liquidez | $35.429 |
| MCap | $166.979 |
| Volumen 24 h | $187.477 |
| Cambio 24 h | +277% |
| Cambio m5 / h1 | +19,0% / +277,0% |
| Volumen m5 / h1 | $95.442 / $187.477 |
| Trades m5 (compras / ventas) | 737 / 625 |
| Edad del par | 13,0 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 45; motivos sin regla: young-0.4 · edad 13.0 min · pesos info 59 / estructura 21 / precio 21 · info 17.3 · estructura 15.8 · precio/volumen 12.1 · cobertura 93/100, [info] narrative_wave: ola 'sobdog': 5 lanzamientos más en 1 h → +9.1, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.2, [info] dex_profile: perfil pago en DexScreener → +2.9, [estructura] bonding_progress: graduado (pumpswap) → +10.0, [estructura] holders_struct: holders 2097 · top-10 29.6 % → +5.0, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 2097/3373 = 0.62 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×6.1 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +53% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1355→2097 (+123.7/min) · top10 33.0%→29.6% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=35428.58, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 45 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-10T08:50:23+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 43 de 26.863 tokens analizados (0,16%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 10/10/2026 08:50 UTC, hasta 12/10/2026 08:50 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +19,0% · h1 +277,0% · h24 +277% · volumen m5/h1 0,51 · edad del par 13,0 min.
- **Precio de entrada** (alerta): $0,0001669.
- **Consulta 10/10/2026 09:11 UTC:** $0,0001467 (-12,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump_2026-10-10_085023.json` · blob `0eb3bfec2a797f41de05b62b0d7bfecd07946b04` · commit `c5ee3f1` (2026-10-10T09:04:16Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-10_085023`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump · registro · 10/10/2026 08:50 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump · HTTP 200 · 10/10/2026 09:11 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump/report · HTTP 200 · 10/10/2026 09:11 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump · HTTP 200 · 10/10/2026 09:11 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/85GXpjwt31qLTUxyRVMjQZdKtBSAkFsdHNmuW41kcvr/ohlcv/hour?limit=1000 · HTTP 200 · 10/10/2026 09:11 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump · HTTP 404 · 10/10/2026 09:12 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SOBDOGUSDT · HTTP 400 · 10/10/2026 09:12 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SOBDOG-USD · HTTP 404 · 10/10/2026 09:12 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $33.397 vs $32.341 → 3,16%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0001467 vs $0,0001388 → 5,37%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump_2026-10-10_085023.json',encoding='utf-8'));d=d.get('D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump',d);p=mock.patch('time.time',return_value=1791622223);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint D4cYhYCPDM7trS62B7sKTTKeWtCDtG5ECjCtMSthpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 10/10/2026 09:12 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `f25d775c4f6a0493…`
