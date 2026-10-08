# creator capital (cc) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001795 · liquidez $118.726 · mcap $1.793.001 (al detectar)  
Detectado el 08/10/2026 06:56 UTC por: MCap > $1M, Volumen decente, Buy pressure >60% (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 10/10/2026 06:56 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir cc

Estudio de cómo se adquiere cc, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/10/2026 07:16 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/10/2026 06:56 UTC | pumpswap `HRtmqrr…rUHE` | $118.726 | 5% | 0,168% | 1,685% | 16,846% | $594 | $1.781 |
| consulta 08/10/2026 07:16 UTC | pumpswap `HRtmqrr…rUHE` | $119.080 | 5% | 0,168% | 1,680% | 16,795% | $595 | $1.786 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump`
5. Configurar el slippage: 5% (liquidez $119.080, consulta 08/10/2026 07:16 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump) y el par en DexScreener (https://dexscreener.com/solana/HRtmqrrq1JE5ktVoQYLz4D5wpgo7PPoKpEorpkLhrUHE); mint authority / freeze authority: revocada / revocada · holders 4.002 · top-10 4,14% (consulta 08/10/2026 07:16 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump
- Par en DexScreener: https://dexscreener.com/solana/HRtmqrrq1JE5ktVoQYLz4D5wpgo7PPoKpEorpkLhrUHE
- Página del lanzamiento (pump.fun): https://pump.fun/coin/z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 4.002 · top-10 4,14% (consulta 08/10/2026 07:16 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | creator capital / cc | registro de la detección (pumpportal) |
| Mint / contrato | `z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HRtmqrrq1JE5ktVoQYLz4D5wpgo7PPoKpEorpkLhrUHE` | DexScreener, al detectar (2 par(es) en la consulta 08/10/2026 07:16 UTC) |
| Deployer | `88wqWk4YZFXZTzqLqDSxWhsajsbEVi4nxNhEtpZqRJTo` | PumpPortal (evento create), al detectar |
| Par creado | 08/10/2026 05:55 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,2 min / 60,2 min / 80,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/10/2026 07:16 UTC |
| Holders / top-10 | 4.002 / 4,14% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/10/2026 07:16 UTC |
| Holders efectivos del top-10 | 1,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/10/2026 07:16 UTC |
| Etiquetas de RugCheck | «High holder correlation», «Copycat token» | RugCheck `risks[].name` (texto de la fuente), consulta 08/10/2026 07:16 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HRtmqrrq1JE5ktVoQYLz4D5wpgo7PPoKpEorpkLhrUHE · Solscan: https://solscan.io/token/z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump · pump.fun: https://pump.fun/coin/z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump · web / Telegram / X: no publicados en DexScreener | consulta 08/10/2026 07:16 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/10/2026 07:16 UTC)
- **Historia:**
  - Par creado el 08/10/2026 05:55 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/10/2026 06:56 UTC, con el par a 60,2 min de creado: precio $0,001795, mcap $1.793.001, liquidez $118.726.
  - Velas de 1 h de GeckoTerminal (3, desde 08/10/2026 05:00 UTC): apertura $0,00004779 · máximo $0,001806 (08/10/2026 07:00 UTC) · mínimo $0,00004779 (08/10/2026 05:00 UTC) · último cierre $0,001780.
  - En la consulta 08/10/2026 07:16 UTC: precio $0,001803, liquidez $119.080, FDV $1.801.570.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/10/2026 06:56 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001795 |
| Liquidez | $118.726 |
| MCap | $1.793.001 |
| Volumen 24 h | $55.199 |
| Cambio 24 h | +3.653% |
| Cambio m5 / h1 | +1,2% / +8,6% |
| Volumen m5 / h1 | $541 / $7.212 |
| Trades m5 (compras / ventas) | 13 / 8 |
| Edad del par | 60,2 min |
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
| MCap | ≥ $1M | $1.793.001 | +25 |
| Volumen 24 h | ≥ $50K | $55.199 | +10 |
| Buy pressure m5 | > 60% (par maduro) | 62% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +1,2% · h1 +8,6% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,2 min | +8 |
| Volumen m5 | > $500 (par maduro) | $541 | +5 |
| Liquidez | ≥ $100K | $118.726 | +15 |
| Cambio 24 h | ≥ +50% | +3.653% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +3.653% · liq/mcap 6,6% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-08T06:56:05+00:00, sin estado previo): **100** · motivos: MCap > $1M, Volumen decente, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=6.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 33 de 21.037 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/10/2026 06:56 UTC, hasta 10/10/2026 06:56 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +1,2% · h1 +8,6% · h24 +3.653% · volumen m5/h1 0,08 · edad del par 60,2 min.
- **Precio de entrada** (alerta): $0,001795.
- **Consulta 08/10/2026 07:16 UTC:** $0,001803 (+0,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump_2026-10-08_065605.json` · blob `f5877808b29bf7d2a9bea0e55e6c7329c8d796b2` · commit `e5ce92e` (2026-10-08T07:07:32Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-08_065605`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump · registro · 08/10/2026 06:56 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump · HTTP 200 · 08/10/2026 07:16 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump/report · HTTP 200 · 08/10/2026 07:16 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump · HTTP 200 · 08/10/2026 07:16 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HRtmqrrq1JE5ktVoQYLz4D5wpgo7PPoKpEorpkLhrUHE/ohlcv/hour?limit=1000 · HTTP 200 · 08/10/2026 07:16 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump · HTTP 404 · 08/10/2026 07:16 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=CCUSDT · HTTP 400 · 08/10/2026 07:16 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/CC-USD · HTTP 404 · 08/10/2026 07:16 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $119.080 vs $118.267 → 0,68%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001803 vs $0,001780 → 1,26%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump_2026-10-08_065605.json',encoding='utf-8'));d=d.get('z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump',d);p=mock.patch('time.time',return_value=1791442565);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint z2AXUxNXdr32KrQQSAxo3D4asJFQUs1wFQBugJqpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/10/2026 07:16 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `e7e08e585aa7195f…`
