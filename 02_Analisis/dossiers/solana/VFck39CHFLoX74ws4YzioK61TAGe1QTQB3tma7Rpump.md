# Anthropic IPO (ANT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,002555 · liquidez $142.586 · mcap $2.547.258 (al detectar)  
Detectado el 26/10/2026 15:20 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 92, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 28/10/2026 15:20 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ANT

Estudio de cómo se adquiere ANT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 26/10/2026 15:20 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 26/10/2026 15:20 UTC | pumpswap `CqGjKAH…9jc8` | $142.586 | 5% | 0,140% | 1,403% | 14,027% | $713 | $2.139 |
| consulta 26/10/2026 15:20 UTC | pumpswap `CqGjKAH…9jc8` | $141.597 | 5% | 0,141% | 1,412% | 14,125% | $708 | $2.124 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump`
5. Configurar el slippage: 5% (liquidez $141.597, consulta 26/10/2026 15:20 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump) y el par en DexScreener (https://dexscreener.com/solana/CqGjKAH8VaRfsVHaJ5We1pdYvBv842qcYimTpf1k9jc8); mint authority / freeze authority: revocada / revocada · holders 6.696 · top-10 6,81% (consulta 26/10/2026 15:20 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump
- Par en DexScreener: https://dexscreener.com/solana/CqGjKAH8VaRfsVHaJ5We1pdYvBv842qcYimTpf1k9jc8
- Página del lanzamiento (pump.fun): https://pump.fun/coin/VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 6.696 · top-10 6,81% (consulta 26/10/2026 15:20 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Anthropic IPO / ANT | registro de la detección (trending) |
| Mint / contrato | `VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `CqGjKAH8VaRfsVHaJ5We1pdYvBv842qcYimTpf1k9jc8` | DexScreener, al detectar (3 par(es) en la consulta 26/10/2026 15:20 UTC) |
| Deployer | `Dqw2YmxX6UQmd63UGRHu7sVF8PAG8wLgrJduiAnV9Upb` | RugCheck `creator` |
| Par creado | 26/10/2026 14:20 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 59,4 min / 59,7 min / 60,1 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 26/10/2026 15:20 UTC |
| Holders / top-10 | 6.696 / 6,81% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 26/10/2026 15:20 UTC |
| Holders efectivos del top-10 | 4,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 26/10/2026 15:20 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 26/10/2026 15:20 UTC |
| Links | DexScreener: https://dexscreener.com/solana/CqGjKAH8VaRfsVHaJ5We1pdYvBv842qcYimTpf1k9jc8 · Solscan: https://solscan.io/token/VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump · pump.fun: https://pump.fun/coin/VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump · twitter: https://x.com/AnthropicIPOX | consulta 26/10/2026 15:20 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 26/10/2026 15:20 UTC)
- **Historia:**
  - Par creado el 26/10/2026 14:20 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 26/10/2026 15:20 UTC, con el par a 59,4 min de creado: precio $0,002555, mcap $2.547.258, liquidez $142.586.
  - Velas de 1 h de GeckoTerminal (2, desde 26/10/2026 14:00 UTC): apertura $0,0001893 · máximo $0,003561 (26/10/2026 15:00 UTC) · mínimo $0,00006045 (26/10/2026 14:00 UTC) · último cierre $0,002480.
  - En la consulta 26/10/2026 15:20 UTC: precio $0,002520, liquidez $141.597, FDV $2.512.671.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 26/10/2026 15:20 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,002555 |
| Liquidez | $142.586 |
| MCap | $2.547.258 |
| Volumen 24 h | $3.101.608 |
| Cambio 24 h | +4.109% |
| Cambio m5 / h1 | -1,9% / +4.109,0% |
| Volumen m5 / h1 | $56.547 / $3.101.608 |
| Trades m5 (compras / ventas) | 914 / 481 |
| Edad del par | 59,4 min |
| Score del feed (WS) | 76 |

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

Desglose reconstruido desde los motivos registrados; suma 92 = score registrado 92 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 76 × 0,3 | +22,7 |
| Gate de edad v7.2.1 | edad < 60 min o desconocida: sin bonos temporales | edad 59,4 min | +0 |
| MCap | ≥ $1M | $2.547.258 | +25 |
| Volumen 24 h | ≥ $1M | $3.101.608 | +20 |
| Liquidez | ≥ $100K | $142.586 | +15 |
| Cambio 24 h | ≥ +50% | +4.109% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +4.109% · liq/mcap 5,6% | +0 |
| **Total** | recortado a 0–100 |  | **92** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-26T15:20:12+00:00, sin estado previo): **92** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), WS score alto, MCap > $1M, Volumen masivo, Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=5.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 78 de 46.003 tokens analizados (0,17%) quedan ≥ 56. Con score 92, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 26/10/2026 15:20 UTC, hasta 28/10/2026 15:20 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -1,9% · h1 +4.109,0% · h24 +4.109% · volumen m5/h1 0,02 · edad del par 59,4 min.
- **Precio de entrada** (alerta): $0,002555.
- **Consulta 26/10/2026 15:20 UTC:** $0,002520 (-1,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump_2026-10-26_152034.json` · blob `3faf24b557e4461665e250dd7d0e05ced6439ee8` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-26_151509.json` · blob `d4c04ad57a69bcb477612842de8709a31fc3b0a8` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-26_152034`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump · registro · 26/10/2026 15:20 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump · HTTP 200 · 26/10/2026 15:20 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump/report · HTTP 200 · 26/10/2026 15:20 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump · HTTP 200 · 26/10/2026 15:20 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/CqGjKAH8VaRfsVHaJ5We1pdYvBv842qcYimTpf1k9jc8/ohlcv/hour?limit=1000 · HTTP 200 · 26/10/2026 15:20 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump · HTTP 404 · 26/10/2026 15:20 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=ANTUSDT · HTTP 200 · 26/10/2026 15:20 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/ANT-USD · HTTP 200 · 26/10/2026 15:20 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $141.597 vs $140.543 → 0,74%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002520 vs $0,002480 → 1,58%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump_2026-10-26_152034.json',encoding='utf-8'));d=d.get('VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump',d);p=mock.patch('time.time',return_value=1793028012);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint VFck39CHFLoX74ws4YzioK61TAGe1QTQB3tma7Rpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 26/10/2026 15:20 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `8e1c08d7ff2552b4…`
