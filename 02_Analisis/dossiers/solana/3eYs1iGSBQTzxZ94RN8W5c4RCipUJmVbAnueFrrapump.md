# Cure Cancer (MIRIAM) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0002250 · liquidez $42.307 · mcap $224.628 (al detectar)  
Detectado el 19/10/2026 17:54 UTC por: young-0.4 · edad 11.1 min · pesos info 59 / estructura 20 / precio 20 · info 23.1 · estructura 15.1 · precio/volumen 11.8 · cobertura 93/100, [info] narrative_wave: ola 'miriam': 10 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 50, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 21/10/2026 17:54 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir MIRIAM

Estudio de cómo se adquiere MIRIAM, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 19/10/2026 18:26 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 19/10/2026 17:54 UTC | pumpswap `9NG25Yw…uZjN` | $42.307 | 10% | 0,473% | 4,727% | 47,274% | $212 | $635 |
| consulta 19/10/2026 18:26 UTC | pumpswap `9NG25Yw…uZjN` | $20.721 | 10% | 0,965% | 9,652% | 96,522% | $104 | $311 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump`
5. Configurar el slippage: 10% (liquidez $20.721, consulta 19/10/2026 18:26 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump) y el par en DexScreener (https://dexscreener.com/solana/9NG25YwUEH5UHrMfckFxjfeLaMPNSxEKLdnFLBxbuZjN); mint authority / freeze authority: revocada / revocada · holders 3.537 · top-10 41,46% (consulta 19/10/2026 18:26 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump
- Par en DexScreener: https://dexscreener.com/solana/9NG25YwUEH5UHrMfckFxjfeLaMPNSxEKLdnFLBxbuZjN
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.537 · top-10 41,46% (consulta 19/10/2026 18:26 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Cure Cancer / MIRIAM | registro de la detección (pumpportal_live) |
| Mint / contrato | `3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `9NG25YwUEH5UHrMfckFxjfeLaMPNSxEKLdnFLBxbuZjN` | DexScreener, al detectar (7 par(es) en la consulta 19/10/2026 18:26 UTC) |
| Deployer | `8NJ7Ujpji8uMF2675mqaTSEm2DCbfJA7fiRKtiaqkaLN` | PumpPortal (evento create), al detectar |
| Par creado | 19/10/2026 17:43 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,1 min / 11,1 min / 42,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 19/10/2026 18:26 UTC |
| Holders / top-10 | 3.537 / 41,46% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 19/10/2026 18:26 UTC |
| Holders efectivos del top-10 | 3,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 19/10/2026 18:26 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 19/10/2026 18:26 UTC |
| Links | DexScreener: https://dexscreener.com/solana/9NG25YwUEH5UHrMfckFxjfeLaMPNSxEKLdnFLBxbuZjN · Solscan: https://solscan.io/token/3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump · pump.fun: https://pump.fun/coin/3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump · web / Telegram / X: no publicados en DexScreener | consulta 19/10/2026 18:26 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 19/10/2026 18:26 UTC)
- **Historia:**
  - Par creado el 19/10/2026 17:43 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 19/10/2026 17:54 UTC, con el par a 11,1 min de creado: precio $0,0002250, mcap $224.628, liquidez $42.307.
  - Velas de 1 h de GeckoTerminal (2, desde 19/10/2026 17:00 UTC): apertura $0,00003815 · máximo $0,0002357 (19/10/2026 17:00 UTC) · mínimo $0,00002991 (19/10/2026 17:00 UTC) · último cierre $0,00005701.
  - En la consulta 19/10/2026 18:26 UTC: precio $0,00006193, liquidez $20.721, FDV $60.079.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 19/10/2026 17:54 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0002250 |
| Liquidez | $42.307 |
| MCap | $224.628 |
| Volumen 24 h | $415.357 |
| Cambio 24 h | +419% |
| Cambio m5 / h1 | +76,7% / +419,0% |
| Volumen m5 / h1 | $149.138 / $415.357 |
| Trades m5 (compras / ventas) | 1.610 / 1.558 |
| Edad del par | 11,1 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 50; motivos sin regla: young-0.4 · edad 11.1 min · pesos info 59 / estructura 20 / precio 20 · info 23.1 · estructura 15.1 · precio/volumen 11.8 · cobertura 93/100, [info] narrative_wave: ola 'miriam': 10 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] mentions: menciones 1 h 1 (1 familias) · 26 h 1 → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 2296 · top-10 23.6 % → +4.9, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 2296/8862 = 0.26 → +0.4, [precio/volumen] volume_acceleration: vol 5 min ×4.3 la tasa horaria (s 1.00), [precio/volumen] liquidity_inflow: liquidez +132% en 8 min (s 1.00), [precio/volumen] holder_accumulation: holders 1186→2296 (+185.0/min) · top10 39.1%→23.6% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=42306.93, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 50 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-19T17:54:25+00:00, sin estado previo): **45** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $100K, Volumen alto, Liquidez mínima, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 67 de 41.049 tokens analizados (0,16%) quedan ≥ 56. Con score 45, este activo queda en el percentil 99,8 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 19/10/2026 17:54 UTC, hasta 21/10/2026 17:54 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +76,7% · h1 +419,0% · h24 +419% · volumen m5/h1 0,36 · edad del par 11,1 min.
- **Precio de entrada** (alerta): $0,0002250.
- **Consulta 19/10/2026 18:26 UTC:** $0,00006193 (-72,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump_2026-10-19_175425.json` · blob `d6a1d9585336828d4a11c4c43749e68530a37d99` · commit `dbb8bc1` (2026-10-19T18:19:12Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-19_175425`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump · registro · 19/10/2026 17:54 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump · HTTP 200 · 19/10/2026 18:26 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump/report · HTTP 200 · 19/10/2026 18:26 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump · HTTP 200 · 19/10/2026 18:26 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/9NG25YwUEH5UHrMfckFxjfeLaMPNSxEKLdnFLBxbuZjN/ohlcv/hour?limit=1000 · HTTP 200 · 19/10/2026 18:26 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump · HTTP 404 · 19/10/2026 18:26 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MIRIAMUSDT · HTTP 400 · 19/10/2026 18:26 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MIRIAM-USD · HTTP 404 · 19/10/2026 18:26 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $20.721 vs $19.657 → 5,13%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00006193 vs $0,00005701 → 7,94%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump_2026-10-19_175425.json',encoding='utf-8'));d=d.get('3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump',d);p=mock.patch('time.time',return_value=1792432465);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3eYs1iGSBQTzxZ94RN8W5c4RCipUJmVbAnueFrrapump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 19/10/2026 18:26 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `e214bc20a0132e44…`
