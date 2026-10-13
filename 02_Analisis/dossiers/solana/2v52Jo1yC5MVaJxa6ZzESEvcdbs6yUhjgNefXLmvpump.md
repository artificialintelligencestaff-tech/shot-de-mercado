# The Revolut Files (Revolut) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00006618 · liquidez $21.288 · mcap $66.183 (al detectar)  
Detectado el 13/10/2026 09:54 UTC por: young-0.4 · edad 11.8 min · pesos info 59 / estructura 20 / precio 20 · info 14.8 · estructura 14.1 · precio/volumen 13.9 · cobertura 93/100, [info] narrative_wave: ola 'revolut': 5 lanzamientos más en 1 h → +9.2, [info] metadata_socials: enlaces ['twitter'] · descripción 29 caracteres → +2.6 (score 43, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 15/10/2026 09:54 UTC (< 48 h) · vigente: quedan 47,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Revolut

Estudio de cómo se adquiere Revolut, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 13/10/2026 10:01 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 13/10/2026 09:54 UTC | pumpswap `EtY35iY…qmED` | $21.288 | 10% | 0,940% | 9,395% | 93,951% | $106 | $319 |
| consulta 13/10/2026 10:01 UTC | pumpswap `EtY35iY…qmED` | $24.207 | 10% | 0,826% | 8,262% | 82,619% | $121 | $363 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump`
5. Configurar el slippage: 10% (liquidez $24.207, consulta 13/10/2026 10:01 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump) y el par en DexScreener (https://dexscreener.com/solana/EtY35iYEu9YRMbiw6mCrFt4PrEnvAdBqtcTLW8GAqmED); mint authority / freeze authority: revocada / revocada · holders 1.856 · top-10 33,42% (consulta 13/10/2026 10:01 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump
- Par en DexScreener: https://dexscreener.com/solana/EtY35iYEu9YRMbiw6mCrFt4PrEnvAdBqtcTLW8GAqmED
- Página del lanzamiento (pump.fun): https://pump.fun/coin/2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.856 · top-10 33,42% (consulta 13/10/2026 10:01 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | The Revolut Files / Revolut | registro de la detección (pumpportal_live) |
| Mint / contrato | `2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `EtY35iYEu9YRMbiw6mCrFt4PrEnvAdBqtcTLW8GAqmED` | DexScreener, al detectar (3 par(es) en la consulta 13/10/2026 10:01 UTC) |
| Deployer | `4khTDC81icSpJbewzf3dm3gncMgiBZQhHLZcHMbftG8d` | PumpPortal (evento create), al detectar |
| Par creado | 13/10/2026 09:43 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,8 min / 11,8 min / 18,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 13/10/2026 10:01 UTC |
| Holders / top-10 | 1.856 / 33,42% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 13/10/2026 10:01 UTC |
| Holders efectivos del top-10 | 3,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 13/10/2026 10:01 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 13/10/2026 10:01 UTC |
| Links | DexScreener: https://dexscreener.com/solana/EtY35iYEu9YRMbiw6mCrFt4PrEnvAdBqtcTLW8GAqmED · Solscan: https://solscan.io/token/2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump · pump.fun: https://pump.fun/coin/2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump · twitter: https://x.com/search?q=Revolut%20leaked&src=typed_query | consulta 13/10/2026 10:01 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 13/10/2026 10:01 UTC)
- **Historia:**
  - Par creado el 13/10/2026 09:43 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 13/10/2026 09:54 UTC, con el par a 11,8 min de creado: precio $0,00006618, mcap $66.183, liquidez $21.288.
  - Velas de 1 h de GeckoTerminal (2, desde 13/10/2026 09:00 UTC): apertura $0,00004442 · máximo $0,00009646 (13/10/2026 10:00 UTC) · mínimo $0,00003897 (13/10/2026 09:00 UTC) · último cierre $0,00008392.
  - En la consulta 13/10/2026 10:01 UTC: precio $0,00008726, liquidez $24.207, FDV $87.263.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 13/10/2026 09:54 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00006618 |
| Liquidez | $21.288 |
| MCap | $66.183 |
| Volumen 24 h | $47.975 |
| Cambio 24 h | +54% |
| Cambio m5 / h1 | -3,7% / +54,3% |
| Volumen m5 / h1 | $18.983 / $47.975 |
| Trades m5 (compras / ventas) | 428 / 277 |
| Edad del par | 11,8 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 43; motivos sin regla: young-0.4 · edad 11.8 min · pesos info 59 / estructura 20 / precio 20 · info 14.8 · estructura 14.1 · precio/volumen 13.9 · cobertura 93/100, [info] narrative_wave: ola 'revolut': 5 lanzamientos más en 1 h → +9.2, [info] metadata_socials: enlaces ['twitter'] · descripción 29 caracteres → +2.6, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.8, [estructura] holders_struct: holders 1528 · top-10 35.7 % → +2.5, [estructura] dev_wallet: creador compró 6.6 % del supply → +1.0, [estructura] holder_to_txn_ratio: holders/txns 1528/1618 = 0.94 → +0.8, [precio/volumen] volume_acceleration: vol 5 min ×4.7 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 61% en 5 min vs 60% en 1 h (s 0.01), [precio/volumen] quiet_accumulation: precio quieto (m5 -3.7%) con vol ×4.7 y compras 61% (s 0.52), [precio/volumen] liquidity_inflow: liquidez +24% en 8 min (s 0.80), [precio/volumen] holder_accumulation: holders 497→1528 (+85.9/min) · top10 49.2%→35.7% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=21287.76, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 43 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-13T09:54:50+00:00, sin estado previo): **25** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $50K, Volumen bajo, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 52 de 33.026 tokens analizados (0,16%) quedan ≥ 56. Con score 25, este activo queda en el percentil 97,6 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 13/10/2026 09:54 UTC, hasta 15/10/2026 09:54 UTC · vigente: quedan 47,9 h.
- **Aceleración al detectar:** cambio m5 -3,7% · h1 +54,3% · h24 +54% · volumen m5/h1 0,40 · edad del par 11,8 min.
- **Precio de entrada** (alerta): $0,00006618.
- **Consulta 13/10/2026 10:01 UTC:** $0,00008726 (+31,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump_2026-10-13_095450.json` · blob `7b781a70e95e8008852777eb84e3631410b83c62` · commit `6d35a9c` (2026-10-13T09:55:01Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-13_095450`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump · registro · 13/10/2026 09:54 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump · HTTP 200 · 13/10/2026 10:01 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump/report · HTTP 200 · 13/10/2026 10:01 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump · HTTP 200 · 13/10/2026 10:01 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/EtY35iYEu9YRMbiw6mCrFt4PrEnvAdBqtcTLW8GAqmED/ohlcv/hour?limit=1000 · HTTP 200 · 13/10/2026 10:01 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump · HTTP 404 · 13/10/2026 10:01 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=REVOLUTUSDT · HTTP 400 · 13/10/2026 10:01 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/REVOLUT-USD · HTTP 404 · 13/10/2026 10:01 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $24.207 vs $23.802 → 1,67%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00008726 vs $0,00008392 → 3,83%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump_2026-10-13_095450.json',encoding='utf-8'));d=d.get('2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump',d);p=mock.patch('time.time',return_value=1791885290);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 2v52Jo1yC5MVaJxa6ZzESEvcdbs6yUhjgNefXLmvpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 13/10/2026 10:01 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `bcd4388297973c36…`
