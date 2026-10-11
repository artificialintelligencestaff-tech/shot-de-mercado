# Quantum Tiger (QT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,002975 · liquidez $156.016 · mcap $2.940.258 (al detectar)  
Detectado el 11/10/2026 04:40 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 13/10/2026 04:40 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir QT

Estudio de cómo se adquiere QT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 11/10/2026 04:57 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 11/10/2026 04:40 UTC | pumpswap `FkkNXVY…vRAt` | $156.016 | 5% | 0,128% | 1,282% | 12,819% | $780 | $2.340 |
| consulta 11/10/2026 04:57 UTC | pumpswap `FkkNXVY…vRAt` | $157.688 | 5% | 0,127% | 1,268% | 12,683% | $788 | $2.365 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump`
5. Configurar el slippage: 5% (liquidez $157.688, consulta 11/10/2026 04:57 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump) y el par en DexScreener (https://dexscreener.com/solana/FkkNXVYbRt22BQEf9mbmSwiW35oiG5ion2QmnAsfvRAt); mint authority / freeze authority: revocada / revocada · holders 10.337 · top-10 4,99% (consulta 11/10/2026 04:57 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump
- Par en DexScreener: https://dexscreener.com/solana/FkkNXVYbRt22BQEf9mbmSwiW35oiG5ion2QmnAsfvRAt
- Página del lanzamiento (pump.fun): https://pump.fun/coin/9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 10.337 · top-10 4,99% (consulta 11/10/2026 04:57 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Quantum Tiger / QT | registro de la detección (trending) |
| Mint / contrato | `9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `FkkNXVYbRt22BQEf9mbmSwiW35oiG5ion2QmnAsfvRAt` | DexScreener, al detectar (2 par(es) en la consulta 11/10/2026 04:57 UTC) |
| Deployer | `74pgQAzMk2adZPYNYE8Ubxio9B12qhfnfwWTEdUx3Rpe` | RugCheck `creator` |
| Par creado | 10/10/2026 18:22 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,3 h / 10,3 h / 10,6 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 11/10/2026 04:57 UTC |
| Holders / top-10 | 10.337 / 4,99% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 11/10/2026 04:57 UTC |
| Holders efectivos del top-10 | 3,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 11/10/2026 04:57 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 11/10/2026 04:57 UTC |
| Links | DexScreener: https://dexscreener.com/solana/FkkNXVYbRt22BQEf9mbmSwiW35oiG5ion2QmnAsfvRAt · Solscan: https://solscan.io/token/9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump · pump.fun: https://pump.fun/coin/9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump · web: https://thequantumtiger.site · twitter: https://x.com/theqtiger | consulta 11/10/2026 04:57 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 11/10/2026 04:57 UTC)
- **Historia:**
  - Par creado el 10/10/2026 18:22 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 11/10/2026 04:40 UTC, con el par a 10,3 h de creado: precio $0,002975, mcap $2.940.258, liquidez $156.016.
  - Velas de 1 h de GeckoTerminal (11, desde 10/10/2026 18:00 UTC): apertura $0,0001282 · máximo $0,003104 (11/10/2026 04:00 UTC) · mínimo $0,00005842 (10/10/2026 18:00 UTC) · último cierre $0,003030.
  - En la consulta 11/10/2026 04:57 UTC: precio $0,003033, liquidez $157.688, FDV $2.997.531.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 11/10/2026 04:40 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,002975 |
| Liquidez | $156.016 |
| MCap | $2.940.258 |
| Volumen 24 h | $1.577.815 |
| Cambio 24 h | +2.244% |
| Cambio m5 / h1 | -2,2% / +66,0% |
| Volumen m5 / h1 | $5.621 / $154.533 |
| Trades m5 (compras / ventas) | 76 / 26 |
| Edad del par | 10,3 h |
| Score del feed (WS) | 75 |

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
| Score del feed | score WS × 0,3 | WS 75 × 0,3 | +22,4 |
| MCap | ≥ $1M | $2.940.258 | +25 |
| Volumen 24 h | ≥ $1M | $1.577.815 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 75% | +25 |
| Volumen m5 | > $1K (par maduro) | $5.621 | +10 |
| Liquidez | ≥ $100K | $156.016 | +15 |
| Cambio 24 h | ≥ +50% | +2.244% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +2.244% · liq/mcap 5,3% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-11T04:40:23+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=5.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 46 de 28.525 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 11/10/2026 04:40 UTC, hasta 13/10/2026 04:40 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -2,2% · h1 +66,0% · h24 +2.244% · volumen m5/h1 0,04 · edad del par 10,3 h.
- **Precio de entrada** (alerta): $0,002975.
- **Consulta 11/10/2026 04:57 UTC:** $0,003033 (+1,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump_2026-10-11_044023.json` · blob `ac6e9624b503561003d169d2e1ae8c248b36b02a` · commit `3e1637a` (2026-10-11T04:51:08Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-11_043347.json` · blob `5811617833846f4ee017d3eefe3397efc6b1f631` · commit `3e1637a` (2026-10-11T04:51:08Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-11_044023`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump · registro · 11/10/2026 04:40 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump · HTTP 200 · 11/10/2026 04:57 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump/report · HTTP 200 · 11/10/2026 04:57 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump · HTTP 200 · 11/10/2026 04:57 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/FkkNXVYbRt22BQEf9mbmSwiW35oiG5ion2QmnAsfvRAt/ohlcv/hour?limit=1000 · HTTP 200 · 11/10/2026 04:57 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump · HTTP 404 · 11/10/2026 04:57 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=QTUSDT · HTTP 400 · 11/10/2026 04:57 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/QT-USD · HTTP 404 · 11/10/2026 04:57 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $157.688 vs $157.425 → 0,17%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,003033 vs $0,003030 → 0,10%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump_2026-10-11_044023.json',encoding='utf-8'));d=d.get('9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump',d);p=mock.patch('time.time',return_value=1791693623);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 9LAHK5YvCqQCzX5CBw6xF5yFVUzXqoAHWtoofqk2pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 11/10/2026 04:57 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `91da152ed2ffc207…`
