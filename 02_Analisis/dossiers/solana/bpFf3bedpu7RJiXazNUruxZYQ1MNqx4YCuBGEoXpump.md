# United States Oil Supply (USOS) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,003776 · liquidez $168.633 · mcap $3.774.348 (al detectar)  
Detectado el 11/10/2026 08:38 UTC por: MCap > $1M, Volumen decente, Buy pressure >55% (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 13/10/2026 08:38 UTC (< 48 h) · vigente: quedan 47,4 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir USOS

Estudio de cómo se adquiere USOS, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/10/2026 09:12 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 11/10/2026 08:38 UTC | pumpswap `H929cLP…HL9U` | $168.633 | 5% | 0,119% | 1,186% | 11,860% | $843 | $2.529 |
| consulta 11/10/2026 09:12 UTC | pumpswap `H929cLP…HL9U` | $170.770 | 5% | 0,117% | 1,171% | 11,712% | $854 | $2.562 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump`
5. Configurar el slippage: 5% (liquidez $170.770, consulta 11/10/2026 09:12 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump) y el par en DexScreener (https://dexscreener.com/solana/H929cLPccozKMFskzvsbLsUUQjnUJ87KQybQZqEdHL9U); mint authority / freeze authority: revocada / revocada · holders 4.051 · top-10 7,49% (consulta 11/10/2026 09:12 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump
- Par en DexScreener: https://dexscreener.com/solana/H929cLPccozKMFskzvsbLsUUQjnUJ87KQybQZqEdHL9U
- Página del lanzamiento (pump.fun): https://pump.fun/coin/bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.051 · top-10 7,49% (consulta 11/10/2026 09:12 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | United States Oil Supply / USOS | registro de la detección (pumpportal) |
| Mint / contrato | `bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `H929cLPccozKMFskzvsbLsUUQjnUJ87KQybQZqEdHL9U` | DexScreener, al detectar (2 par(es) en la consulta 11/10/2026 09:12 UTC) |
| Deployer | `pz5W2mFH1T22YZejwshqhzbHiUEqzbFAMiVU6T3iFZ5` | PumpPortal (evento create), al detectar |
| Par creado | 11/10/2026 07:37 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 61,1 min / 61,1 min / 95,5 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/10/2026 09:12 UTC |
| Holders / top-10 | 4.051 / 7,49% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/10/2026 09:12 UTC |
| Holders efectivos del top-10 | 1,8 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/10/2026 09:12 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 11/10/2026 09:12 UTC |
| Links | DexScreener: https://dexscreener.com/solana/H929cLPccozKMFskzvsbLsUUQjnUJ87KQybQZqEdHL9U · Solscan: https://solscan.io/token/bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump · pump.fun: https://pump.fun/coin/bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump · web / Telegram / X: no publicados en DexScreener | consulta 11/10/2026 09:12 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/10/2026 09:12 UTC)
- **Historia:**
  - Par creado el 11/10/2026 07:37 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 11/10/2026 08:38 UTC, con el par a 61,1 min de creado: precio $0,003776, mcap $3.774.348, liquidez $168.633.
  - Velas de 1 h de GeckoTerminal (3, desde 11/10/2026 07:00 UTC): apertura $0,003575 · máximo $0,003871 (11/10/2026 09:00 UTC) · mínimo $0,00004544 (11/10/2026 07:00 UTC) · último cierre $0,003871.
  - En la consulta 11/10/2026 09:12 UTC: precio $0,003864, liquidez $170.770, FDV $3.862.238.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 11/10/2026 08:38 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,003776 |
| Liquidez | $168.633 |
| MCap | $3.774.348 |
| Volumen 24 h | $80.651 |
| Cambio 24 h | +8.203% |
| Cambio m5 / h1 | +0,2% / +3,9% |
| Volumen m5 / h1 | $607 / $6.665 |
| Trades m5 (compras / ventas) | 12 / 8 |
| Edad del par | 61,1 min |
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

Desglose reconstruido desde los motivos registrados; suma 100 = score registrado 100 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $1M | $3.774.348 | +25 |
| Volumen 24 h | ≥ $50K | $80.651 | +10 |
| Buy pressure m5 | > 55% (par maduro) | 60% | +15 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,2% · h1 +3,9% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 61,1 min | +8 |
| Volumen m5 | > $500 (par maduro) | $607 | +5 |
| Liquidez | ≥ $100K | $168.633 | +15 |
| Cambio 24 h | ≥ +50% | +8.203% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +8.203% · liq/mcap 4,5% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-11T08:38:18+00:00, sin estado previo): **100** · motivos: MCap > $1M, Volumen decente, Buy pressure >55%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=4.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 47 de 28.832 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 11/10/2026 08:38 UTC, hasta 13/10/2026 08:38 UTC · vigente: quedan 47,4 h.
- **Aceleración al detectar:** cambio m5 +0,2% · h1 +3,9% · h24 +8.203% · volumen m5/h1 0,09 · edad del par 61,1 min.
- **Precio de entrada** (alerta): $0,003776.
- **Consulta 11/10/2026 09:12 UTC:** $0,003864 (+2,3% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump_2026-10-11_083818.json` · blob `bbe3907cc3310c8c0ef17eda8cd3ec9ddf0b7272` · commit `7b1d233` (2026-10-11T09:05:06Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-11_083818`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump · registro · 11/10/2026 08:38 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump · HTTP 200 · 11/10/2026 09:12 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump/report · HTTP 200 · 11/10/2026 09:12 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump · HTTP 200 · 11/10/2026 09:12 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/H929cLPccozKMFskzvsbLsUUQjnUJ87KQybQZqEdHL9U/ohlcv/hour?limit=1000 · HTTP 200 · 11/10/2026 09:12 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump · HTTP 404 · 11/10/2026 09:12 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=USOSUSDT · HTTP 400 · 11/10/2026 09:12 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/USOS-USD · HTTP 404 · 11/10/2026 09:12 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $170.770 vs $170.289 → 0,28%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003864 vs $0,003871 → 0,19%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump_2026-10-11_083818.json',encoding='utf-8'));d=d.get('bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump',d);p=mock.patch('time.time',return_value=1791707898);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint bpFf3bedpu7RJiXazNUruxZYQ1MNqx4YCuBGEoXpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/10/2026 09:12 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `1c268b66144e3312…`
