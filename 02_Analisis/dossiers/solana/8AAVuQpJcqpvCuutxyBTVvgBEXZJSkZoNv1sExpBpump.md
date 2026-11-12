# Shiba Nobunaga (NOBUSHIBA) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001261 · liquidez $90.770 · mcap $1.244.937 (al detectar)  
Detectado el 12/11/2026 11:27 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 70, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 14/11/2026 11:27 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir NOBUSHIBA

Estudio de cómo se adquiere NOBUSHIBA, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 12/11/2026 11:27 UTC; CoinGecko sin pares de este contrato en esos exchanges).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 12/11/2026 11:27 UTC | pumpswap `Dagau7G…HfGF` | $90.770 | 5% | 0,220% | 2,203% | 22,034% | $454 | $1.362 |
| consulta 12/11/2026 11:27 UTC | pumpswap `Dagau7G…HfGF` | $90.770 | 5% | 0,220% | 2,203% | 22,034% | $454 | $1.362 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump`
5. Configurar el slippage: 5% (liquidez $90.770, consulta 12/11/2026 11:27 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump) y el par en DexScreener (https://dexscreener.com/solana/Dagau7G32pmkjf8ng2372xo2hyGfgenx5Yn7mWMkHfGF); mint authority / freeze authority: revocada / revocada · holders 8.608 · top-10 4,82% (consulta 12/11/2026 11:27 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump
- Par en DexScreener: https://dexscreener.com/solana/Dagau7G32pmkjf8ng2372xo2hyGfgenx5Yn7mWMkHfGF
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 8.608 · top-10 4,82% (consulta 12/11/2026 11:27 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Shiba Nobunaga / NOBUSHIBA | registro de la detección (trending) |
| Mint / contrato | `8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Dagau7G32pmkjf8ng2372xo2hyGfgenx5Yn7mWMkHfGF` | DexScreener, al detectar (1 par(es) en la consulta 12/11/2026 11:27 UTC) |
| Deployer | `E3Hj4iwGsvCyKmYpDVxxVsq9fN6jHG6Qgvzdr154Rtk5` | RugCheck `creator` |
| Par creado | 11/11/2026 01:26 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 34,0 h / 34,0 h / 34,0 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 12/11/2026 11:27 UTC |
| Holders / top-10 | 8.608 / 4,82% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 12/11/2026 11:27 UTC |
| Holders efectivos del top-10 | 1,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; orca 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 12/11/2026 11:27 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 12/11/2026 11:27 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Dagau7G32pmkjf8ng2372xo2hyGfgenx5Yn7mWMkHfGF · Solscan: https://solscan.io/token/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump · pump.fun: https://pump.fun/coin/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump · web: https://thenobushiba.space · twitter: https://x.com/thenobushiba | consulta 12/11/2026 11:27 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** CoinGecko: Solana Ecosystem, Pump.fun Ecosystem
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 12/11/2026 11:27 UTC)
- **Historia:**
  - Par creado el 11/11/2026 01:26 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 12/11/2026 11:27 UTC, con el par a 34,0 h de creado: precio $0,001261, mcap $1.244.937, liquidez $90.770.
  - Velas de 1 h de GeckoTerminal (35, desde 11/11/2026 01:00 UTC): apertura $0,00004591 · máximo $0,002461 (12/11/2026 04:00 UTC) · mínimo $0,00003595 (11/11/2026 01:00 UTC) · último cierre $0,001275.
  - En la consulta 12/11/2026 11:27 UTC: precio $0,001261, liquidez $90.770, FDV $1.244.937.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 12/11/2026 11:27 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001261 |
| Liquidez | $90.770 |
| MCap | $1.244.937 |
| Volumen 24 h | $1.269.339 |
| Cambio 24 h | +453% |
| Cambio m5 / h1 | -0,7% / +15,1% |
| Volumen m5 / h1 | $4.516 / $40.920 |
| Trades m5 (compras / ventas) | 536 / 101 |
| Edad del par | 34,0 h |
| Score del feed (WS) | 69 |

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

Desglose reconstruido desde los motivos registrados; suma 70 = score registrado 70 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 69 × 0,3 | +20,8 |
| MCap | ≥ $1M | $1.244.937 | +25 |
| Volumen 24 h | ≥ $1M | $1.269.339 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 84% | +25 |
| Volumen m5 | > $1K (par maduro) | $4.516 | +10 |
| Par viejo | edad > 24 h | edad 34,0 h | -50 |
| Liquidez | ≥ $50K | $90.770 | +10 |
| Cambio 24 h | ≥ +50% | +453% | +10 |
| **Total** | recortado a 0–100 |  | **70** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-12T11:27:27+00:00, sin estado previo): **70** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Par >24h, no nativo pump.fun, Liquidez decente, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 97 de 47.096 tokens analizados (0,21%) quedan ≥ 56. Con score 70, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 12/11/2026 11:27 UTC, hasta 14/11/2026 11:27 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -0,7% · h1 +15,1% · h24 +453% · volumen m5/h1 0,11 · edad del par 34,0 h.
- **Precio de entrada** (alerta): $0,001261.
- **Consulta 12/11/2026 11:27 UTC:** $0,001261 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump_2026-11-12_112737.json` · blob `972f86234903fdae6594f29dfb4bf0cbd1285105` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-12_112225.json` · blob `db040ef230160f3cba6a987c28a0f815393bbeb4` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-12_112737`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump · registro · 12/11/2026 11:27 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump · HTTP 200 · 12/11/2026 11:27 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump/report · HTTP 200 · 12/11/2026 11:27 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump · HTTP 200 · 12/11/2026 11:27 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Dagau7G32pmkjf8ng2372xo2hyGfgenx5Yn7mWMkHfGF/ohlcv/hour?limit=1000 · HTTP 200 · 12/11/2026 11:27 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump · HTTP 200 · 12/11/2026 11:27 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=NOBUSHIBAUSDT · HTTP 400 · 12/11/2026 11:27 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/NOBUSHIBA-USD · HTTP 404 · 12/11/2026 11:27 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $90.770 vs $90.658 → 0,12%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001261 vs $0,001275 → 1,06%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump_2026-11-12_112737.json',encoding='utf-8'));d=d.get('8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump',d);p=mock.patch('time.time',return_value=1794482847);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 12/11/2026 11:27 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `f49f9b2338ab7b8d…`
