# fPad (FPAD) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0007179 · liquidez $75.662 · mcap $715.016 (al detectar)  
Detectado el 14/10/2026 01:21 UTC por: MCap > $100K, Volumen masivo, Buy pressure >60% (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 16/10/2026 01:21 UTC (< 48 h) · vigente: quedan 47,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir FPAD

Estudio de cómo se adquiere FPAD, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 14/10/2026 02:23 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 14/10/2026 01:21 UTC | pumpswap `5DbEYwd…zTxU` | $75.662 | 5% | 0,264% | 2,643% | 26,433% | $378 | $1.135 |
| consulta 14/10/2026 02:23 UTC | pumpswap `5DbEYwd…zTxU` | $3.789 | 10% | 5,278% | 52,785% | 527,847% | $19 | $57 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump`
5. Configurar el slippage: 10% (liquidez $3.789, consulta 14/10/2026 02:23 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump) y el par en DexScreener (https://dexscreener.com/solana/5DbEYwdjsteByrDgJe5xWFrVbwuotEANdQTFcYA1zTxU); mint authority / freeze authority: revocada / revocada · holders 2.925 · top-10 90,17% (consulta 14/10/2026 02:23 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump
- Par en DexScreener: https://dexscreener.com/solana/5DbEYwdjsteByrDgJe5xWFrVbwuotEANdQTFcYA1zTxU
- Página del lanzamiento (pump.fun): https://pump.fun/coin/8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.925 · top-10 90,17% (consulta 14/10/2026 02:23 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | fPad / FPAD | registro de la detección (pumpportal) |
| Mint / contrato | `8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `5DbEYwdjsteByrDgJe5xWFrVbwuotEANdQTFcYA1zTxU` | DexScreener, al detectar (4 par(es) en la consulta 14/10/2026 02:23 UTC) |
| Deployer | `5HS5s4UEoEmvUbpTXcAmPd7QTbHV4azriWs1iw2wQTCn` | PumpPortal (evento create), al detectar |
| Par creado | 14/10/2026 00:20 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,3 min / 60,3 min / 2,1 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 14/10/2026 02:23 UTC |
| Holders / top-10 | 2.925 / 90,17% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 14/10/2026 02:23 UTC |
| Holders efectivos del top-10 | 1,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 14/10/2026 02:23 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 14/10/2026 02:23 UTC |
| Links | DexScreener: https://dexscreener.com/solana/5DbEYwdjsteByrDgJe5xWFrVbwuotEANdQTFcYA1zTxU · Solscan: https://solscan.io/token/8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump · pump.fun: https://pump.fun/coin/8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump · web: https://www.fpad.fun · twitter: https://x.com/fpadsolana | consulta 14/10/2026 02:23 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 14/10/2026 02:23 UTC)
- **Historia:**
  - Par creado el 14/10/2026 00:20 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 14/10/2026 01:21 UTC, con el par a 60,3 min de creado: precio $0,0007179, mcap $715.016, liquidez $75.662.
  - Velas de 1 h de GeckoTerminal (3, desde 14/10/2026 00:00 UTC): apertura $0,0004261 · máximo $0,0009527 (14/10/2026 01:00 UTC) · mínimo $0,000002698 (14/10/2026 02:00 UTC) · último cierre $0,000003663.
  - En la consulta 14/10/2026 02:23 UTC: precio $0,000003695, liquidez $3.789, FDV $3.681.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 14/10/2026 01:21 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0007179 |
| Liquidez | $75.662 |
| MCap | $715.016 |
| Volumen 24 h | $1.572.228 |
| Cambio 24 h | +970% |
| Cambio m5 / h1 | +8,6% / +64,5% |
| Volumen m5 / h1 | $65.702 / $1.526.786 |
| Trades m5 (compras / ventas) | 4.342 / 1.574 |
| Edad del par | 60,3 min |
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
| MCap | ≥ $100K | $715.016 | +15 |
| Volumen 24 h | ≥ $1M | $1.572.228 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 73% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +8,6% · h1 +64,5% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,3 min | +8 |
| Volumen m5 | > $1K (par maduro) | $65.702 | +10 |
| Liquidez | ≥ $50K | $75.662 | +10 |
| Cambio 24 h | ≥ +50% | +970% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +970% · liq/mcap 10,6% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-14T01:21:04+00:00, sin estado previo): **100** · motivos: MCap > $100K, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=10.6% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 54 de 34.329 tokens analizados (0,16%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 14/10/2026 01:21 UTC, hasta 16/10/2026 01:21 UTC · vigente: quedan 47,0 h.
- **Aceleración al detectar:** cambio m5 +8,6% · h1 +64,5% · h24 +970% · volumen m5/h1 0,04 · edad del par 60,3 min.
- **Precio de entrada** (alerta): $0,0007179.
- **Consulta 14/10/2026 02:23 UTC:** $0,000003695 (-99,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump_2026-10-14_012104.json` · blob `78ce9df2bf77cd4f98a6697ed5371350ea7d0329` · commit `163d1db` (2026-10-14T02:15:40Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-14_012104`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump · registro · 14/10/2026 01:21 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump · HTTP 200 · 14/10/2026 02:23 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump/report · HTTP 200 · 14/10/2026 02:23 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump · HTTP 200 · 14/10/2026 02:23 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/5DbEYwdjsteByrDgJe5xWFrVbwuotEANdQTFcYA1zTxU/ohlcv/hour?limit=1000 · HTTP 200 · 14/10/2026 02:23 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump · HTTP 404 · 14/10/2026 02:23 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=FPADUSDT · HTTP 400 · 14/10/2026 02:23 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/FPAD-USD · HTTP 404 · 14/10/2026 02:23 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $3.789 vs $3.691 → 2,59%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000003695 vs $0,000003663 → 0,86%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump_2026-10-14_012104.json',encoding='utf-8'));d=d.get('8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump',d);p=mock.patch('time.time',return_value=1791940864);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 8L9bgqk34bsM1QVWQPuxHbvFAorg25wCjgGKh2cQpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 14/10/2026 02:23 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `9ae7e3ecd5cbc3ea…`
