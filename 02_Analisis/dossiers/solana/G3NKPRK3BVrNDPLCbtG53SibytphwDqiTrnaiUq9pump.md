# Roadster (ROADSTER) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003445 · liquidez $166.179 · mcap $3.432.503 (al detectar)  
Detectado el 16/10/2026 17:26 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 18/10/2026 17:26 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ROADSTER

Estudio de cómo se adquiere ROADSTER, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 16/10/2026 17:55 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 16/10/2026 17:26 UTC | pumpswap `2kDUw5G…8Up7` | $166.179 | 5% | 0,120% | 1,204% | 12,035% | $831 | $2.493 |
| consulta 16/10/2026 17:55 UTC | pumpswap `2kDUw5G…8Up7` | $181.319 | 5% | 0,110% | 1,103% | 11,030% | $907 | $2.720 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump`
5. Configurar el slippage: 5% (liquidez $181.319, consulta 16/10/2026 17:55 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump) y el par en DexScreener (https://dexscreener.com/solana/2kDUw5GUbiaPpZhzD8gTzLkn9pUqhmwKEAv5F4rc8Up7); mint authority / freeze authority: revocada / revocada · holders 5.191 · top-10 5,34% (consulta 16/10/2026 17:55 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump
- Par en DexScreener: https://dexscreener.com/solana/2kDUw5GUbiaPpZhzD8gTzLkn9pUqhmwKEAv5F4rc8Up7
- Página del lanzamiento (pump.fun): https://pump.fun/coin/G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.191 · top-10 5,34% (consulta 16/10/2026 17:55 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Roadster / ROADSTER | registro de la detección (trending) |
| Mint / contrato | `G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `2kDUw5GUbiaPpZhzD8gTzLkn9pUqhmwKEAv5F4rc8Up7` | DexScreener, al detectar (3 par(es) en la consulta 16/10/2026 17:55 UTC) |
| Deployer | `8ky5xXNzbjhkQ9Eh8Y4vtpdmw5p7UZ6ejwXZJYqRpun9` | RugCheck `creator` |
| Par creado | 16/10/2026 16:02 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 84,2 min / 84,2 min / 113,0 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 16/10/2026 17:55 UTC |
| Holders / top-10 | 5.191 / 5,34% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 16/10/2026 17:55 UTC |
| Holders efectivos del top-10 | 4,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 16/10/2026 17:55 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 16/10/2026 17:55 UTC |
| Links | DexScreener: https://dexscreener.com/solana/2kDUw5GUbiaPpZhzD8gTzLkn9pUqhmwKEAv5F4rc8Up7 · Solscan: https://solscan.io/token/G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump · pump.fun: https://pump.fun/coin/G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump · web: https://roadstersol.fun · twitter: https://x.com/RoadsterMemeX · telegram: https://t.me/roadstersol | consulta 16/10/2026 17:55 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 16/10/2026 17:55 UTC)
- **Historia:**
  - Par creado el 16/10/2026 16:02 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 16/10/2026 17:26 UTC, con el par a 84,2 min de creado: precio $0,003445, mcap $3.432.503, liquidez $166.179.
  - Velas de 1 h de GeckoTerminal (2, desde 16/10/2026 16:00 UTC): apertura $0,0003827 · máximo $0,005869 (16/10/2026 16:00 UTC) · mínimo $0,00006159 (16/10/2026 16:00 UTC) · último cierre $0,003983.
  - En la consulta 16/10/2026 17:55 UTC: precio $0,004056, liquidez $181.319, FDV $4.041.715.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 16/10/2026 17:26 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003445 |
| Liquidez | $166.179 |
| MCap | $3.432.503 |
| Volumen 24 h | $3.517.023 |
| Cambio 24 h | +5.443% |
| Cambio m5 / h1 | +1,6% / +3,7% |
| Volumen m5 / h1 | $13.321 / $1.970.559 |
| Trades m5 (compras / ventas) | 586 / 248 |
| Edad del par | 84,2 min |
| Score del feed (WS) | 79 |

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
| Score del feed | score WS × 0,3 | WS 79 × 0,3 | +23,6 |
| MCap | ≥ $1M | $3.432.503 | +25 |
| Volumen 24 h | ≥ $1M | $3.517.023 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 70% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +1,6% · h1 +3,7% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 84,2 min | +8 |
| Volumen m5 | > $1K (par maduro) | $13.321 | +10 |
| Liquidez | ≥ $100K | $166.179 | +15 |
| Cambio 24 h | ≥ +50% | +5.443% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +5.443% · liq/mcap 4,8% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-16T17:26:32+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.8% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 60 de 37.406 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 16/10/2026 17:26 UTC, hasta 18/10/2026 17:26 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +1,6% · h1 +3,7% · h24 +5.443% · volumen m5/h1 0,01 · edad del par 84,2 min.
- **Precio de entrada** (alerta): $0,003445.
- **Consulta 16/10/2026 17:55 UTC:** $0,004056 (+17,7% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump_2026-10-16_172632.json` · blob `bb6d6266c48fa291775f74cfe9ec61073a2c7357` · commit `7a6131c` (2026-10-16T17:45:49Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-16_171921.json` · blob `479c54370de5eb9f59aca1d60ed014e2e35648a8` · commit `7a6131c` (2026-10-16T17:45:49Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-16_172632`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump · registro · 16/10/2026 17:26 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump · HTTP 200 · 16/10/2026 17:55 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump/report · HTTP 200 · 16/10/2026 17:55 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump · HTTP 200 · 16/10/2026 17:55 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/2kDUw5GUbiaPpZhzD8gTzLkn9pUqhmwKEAv5F4rc8Up7/ohlcv/hour?limit=1000 · HTTP 200 · 16/10/2026 17:55 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump · HTTP 404 · 16/10/2026 17:55 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ROADSTERUSDT · HTTP 400 · 16/10/2026 17:55 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ROADSTER-USD · HTTP 404 · 16/10/2026 17:55 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $181.319 vs $181.358 → 0,02%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,004056 vs $0,003983 → 1,79%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump_2026-10-16_172632.json',encoding='utf-8'));d=d.get('G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump',d);p=mock.patch('time.time',return_value=1792171592);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint G3NKPRK3BVrNDPLCbtG53SibytphwDqiTrnaiUq9pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 16/10/2026 17:55 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `9fa9ddfcc3e3070c…`
