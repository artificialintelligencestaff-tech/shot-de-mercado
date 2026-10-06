# Do not Redeem it (REDEEM) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00001687 · liquidez $10.112 · mcap $16.341 (al detectar)  
Detectado el 06/10/2026 23:10 UTC por: MCap bajo, Volumen alto, Buy pressure >60% (score 63, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 08/10/2026 23:10 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir REDEEM

Estudio de cómo se adquiere REDEEM, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 23:36 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 23:10 UTC | pumpswap `288A9LQ…gVpf` | $10.112 | 10% | 1,978% | 19,779% | 197,794% | $51 | $152 |
| consulta 06/10/2026 23:36 UTC | pumpswap `288A9LQ…gVpf` | $9.527 | 10% | 2,099% | 20,994% | 209,940% | $48 | $143 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump`
5. Configurar el slippage: 10% (liquidez $9.527, consulta 06/10/2026 23:36 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump) y el par en DexScreener (https://dexscreener.com/solana/288A9LQSqhnY6fJ6x7GPTven9tRvQqvt8L77kvBxgVpf); mint authority / freeze authority: revocada / revocada · holders 737 · top-10 54,44% (consulta 06/10/2026 23:36 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump
- Par en DexScreener: https://dexscreener.com/solana/288A9LQSqhnY6fJ6x7GPTven9tRvQqvt8L77kvBxgVpf
- Página del lanzamiento (pump.fun): https://pump.fun/coin/kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 737 · top-10 54,44% (consulta 06/10/2026 23:36 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Do not Redeem it / REDEEM | registro de la detección (pumpportal) |
| Mint / contrato | `kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `288A9LQSqhnY6fJ6x7GPTven9tRvQqvt8L77kvBxgVpf` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 23:36 UTC) |
| Deployer | `BBLLCaPA7k2j1aRc4AHk1r4Lgnj6gACtUuoamBtVZ64x` | PumpPortal (evento create), al detectar |
| Par creado | 06/10/2026 21:35 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 94,5 min / 94,5 min / 2,0 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 23:36 UTC |
| Holders / top-10 | 737 / 54,44% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 23:36 UTC |
| Holders efectivos del top-10 | 1,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 23:36 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 23:36 UTC |
| Links | DexScreener: https://dexscreener.com/solana/288A9LQSqhnY6fJ6x7GPTven9tRvQqvt8L77kvBxgVpf · Solscan: https://solscan.io/token/kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump · pump.fun: https://pump.fun/coin/kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump · web / Telegram / X: no publicados en DexScreener | consulta 06/10/2026 23:36 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 23:36 UTC)
- **Historia:**
  - Par creado el 06/10/2026 21:35 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 23:10 UTC, con el par a 94,5 min de creado: precio $0,00001687, mcap $16.341, liquidez $10.112.
  - Velas de 1 h de GeckoTerminal (3, desde 06/10/2026 21:00 UTC): apertura $0,00005045 · máximo $0,0002960 (06/10/2026 21:00 UTC) · mínimo $0,00001483 (06/10/2026 22:00 UTC) · último cierre $0,00001647.
  - En la consulta 06/10/2026 23:36 UTC: precio $0,00001531, liquidez $9.527, FDV $14.826.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 23:10 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00001687 |
| Liquidez | $10.112 |
| MCap | $16.341 |
| Volumen 24 h | $396.448 |
| Cambio 24 h | -67% |
| Cambio m5 / h1 | +4,7% / +2,4% |
| Volumen m5 / h1 | $258 / $3.285 |
| Trades m5 (compras / ventas) | 7 / 1 |
| Edad del par | 94,5 min |
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

Desglose reconstruido desde los motivos registrados; suma 63 = score registrado 63 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | < $50K | $16.341 | +0 |
| Volumen 24 h | ≥ $100K | $396.448 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 88% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +4,7% · h1 +2,4% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 94,5 min | +8 |
| Liquidez | < $20K | $10.112 | +0 |
| Cambio 24 h | ≤ −30% | -67% | -5 |
| **Total** | recortado a 0–100 |  | **63** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T23:10:15+00:00, sin estado previo): **63** · motivos: MCap bajo, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 21 de 17.226 tokens analizados (0,12%) quedan ≥ 56. Con score 63, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 23:10 UTC, hasta 08/10/2026 23:10 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 +4,7% · h1 +2,4% · h24 -67% · volumen m5/h1 0,08 · edad del par 94,5 min.
- **Precio de entrada** (alerta): $0,00001687.
- **Consulta 06/10/2026 23:36 UTC:** $0,00001531 (-9,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump_2026-10-06_231015.json` · blob `7e7108de3d54526f3fbd918392b47752576f531d` · commit `e3df118` (2026-10-06T23:29:41Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_231015`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump · registro · 06/10/2026 23:10 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump · HTTP 200 · 06/10/2026 23:36 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump/report · HTTP 200 · 06/10/2026 23:36 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump · HTTP 200 · 06/10/2026 23:36 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/288A9LQSqhnY6fJ6x7GPTven9tRvQqvt8L77kvBxgVpf/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 23:36 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump · HTTP 404 · 06/10/2026 23:36 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=REDEEMUSDT · HTTP 400 · 06/10/2026 23:36 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/REDEEM-USD · HTTP 404 · 06/10/2026 23:36 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $9.527 vs $9.741 → 2,20%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00001531 vs $0,00001647 → 7,04%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump_2026-10-06_231015.json',encoding='utf-8'));d=d.get('kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump',d);p=mock.patch('time.time',return_value=1791328215);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint kzK6etp3DNUJvUT5c4hTHuvMfJ9o9hdDutpiY2xpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 23:36 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `8d17b5b5f08d3129…`
