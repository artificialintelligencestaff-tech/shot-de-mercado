# UDR (UDR) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,2402 · liquidez $1.429.090 · mcap $240.282.108 (al detectar)  
Detectado el 04/10/2026 05:55 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 06/10/2026 05:55 UTC (< 48 h) · vigente: quedan 40,1 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir UDR

Estudio de cómo se adquiere UDR, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 04/10/2026 13:50 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 04/10/2026 05:55 UTC | pumpswap `78zo9ub…M5WU` | $1.429.090 | 1% | 0,014% | 0,140% | 1,399% | $7.145 | $21.436 |
| consulta 04/10/2026 13:50 UTC | pumpswap `78zo9ub…M5WU` | $1.842.186 | 1% | 0,011% | 0,109% | 1,086% | $9.211 | $27.633 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump`
5. Configurar el slippage: 1% (liquidez $1.842.186, consulta 04/10/2026 13:50 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump) y el par en DexScreener (https://dexscreener.com/solana/78zo9ubx8aFLoc6tQLTgNvtnPFHbHXTTe3Eyp89KM5WU); mint authority / freeze authority: revocada / revocada · holders 3.197 · top-10 1,14% (consulta 04/10/2026 13:50 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump
- Par en DexScreener: https://dexscreener.com/solana/78zo9ubx8aFLoc6tQLTgNvtnPFHbHXTTe3Eyp89KM5WU
- Página del lanzamiento (pump.fun): https://pump.fun/coin/yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.197 · top-10 1,14% (consulta 04/10/2026 13:50 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | UDR / UDR | registro de la detección (trending) |
| Mint / contrato | `yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `78zo9ubx8aFLoc6tQLTgNvtnPFHbHXTTe3Eyp89KM5WU` | DexScreener, al detectar (2 par(es) en la consulta 04/10/2026 13:50 UTC) |
| Deployer | `6YTG3Ph2aQDGBTq4D1XHTj1o691SmUsi2ue2TifKV2YH` | RugCheck `creator` |
| Par creado | 04/10/2026 04:08 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 106,8 min / 106,8 min / 9,7 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 04/10/2026 13:50 UTC |
| Holders / top-10 | 3.197 / 1,14% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 04/10/2026 13:50 UTC |
| Holders efectivos del top-10 | 3,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 04/10/2026 13:50 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 04/10/2026 13:50 UTC |
| Links | DexScreener: https://dexscreener.com/solana/78zo9ubx8aFLoc6tQLTgNvtnPFHbHXTTe3Eyp89KM5WU · Solscan: https://solscan.io/token/yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump · pump.fun: https://pump.fun/coin/yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump · web / Telegram / X: no publicados en DexScreener | consulta 04/10/2026 13:50 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 04/10/2026 13:50 UTC)
- **Historia:**
  - Par creado el 04/10/2026 04:08 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 04/10/2026 05:55 UTC, con el par a 106,8 min de creado: precio $0,2402, mcap $240.282.108, liquidez $1.429.090.
  - Velas de 1 h de GeckoTerminal (10, desde 04/10/2026 04:00 UTC): apertura $0,00005012 · máximo $0,3962 (04/10/2026 13:00 UTC) · mínimo $0,00005012 (04/10/2026 04:00 UTC) · último cierre $0,3961.
  - En la consulta 04/10/2026 13:50 UTC: precio $0,3959, liquidez $1.842.186, FDV $395.951.369.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 04/10/2026 05:55 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,2402 |
| Liquidez | $1.429.090 |
| MCap | $240.282.108 |
| Volumen 24 h | $837.110 |
| Cambio 24 h | +479.145% |
| Cambio m5 / h1 | +0,6% / +8,8% |
| Volumen m5 / h1 | $3.152 / $46.951 |
| Trades m5 (compras / ventas) | 173 / 5 |
| Edad del par | 106,8 min |
| Score del feed (WS) | 100 |

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
| Score del feed | score WS × 0,3 | WS 100 × 0,3 | +30 |
| MCap | ≥ $1M | $240.282.108 | +25 |
| Volumen 24 h | ≥ $100K | $837.110 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 97% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,6% · h1 +8,8% | +20 |
| Edge temprano | edad < 4 h (par maduro) | edad 106,8 min | +8 |
| Volumen m5 | > $1K (par maduro) | $3.152 | +10 |
| Liquidez | ≥ $100K | $1.429.090 | +15 |
| Cambio 24 h | ≥ +50% | +479.145% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +479.145% · liq/mcap 0,6% | -50 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-04T05:55:40+00:00, sin estado previo): **100** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 12 de 10.527 tokens analizados (0,11%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 04/10/2026 05:55 UTC, hasta 06/10/2026 05:55 UTC · vigente: quedan 40,1 h.
- **Aceleración al detectar:** cambio m5 +0,6% · h1 +8,8% · h24 +479.145% · volumen m5/h1 0,07 · edad del par 106,8 min.
- **Precio de entrada** (alerta): $0,2402.
- **Consulta 04/10/2026 13:50 UTC:** $0,3959 (+64,8% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump_2026-10-04_055540.json` · blob `4bd75f6d3477daf1425c419943d45a4c07e9616c` · commit `973a3ce` (2026-10-04T13:40:49Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-04_055540`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump · registro · 04/10/2026 05:55 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump · HTTP 200 · 04/10/2026 13:50 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump/report · HTTP 200 · 04/10/2026 13:50 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump · HTTP 200 · 04/10/2026 13:50 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/78zo9ubx8aFLoc6tQLTgNvtnPFHbHXTTe3Eyp89KM5WU/ohlcv/hour?limit=1000 · HTTP 200 · 04/10/2026 13:50 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump · HTTP 404 · 04/10/2026 13:50 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=UDRUSDT · HTTP 400 · 04/10/2026 13:50 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/UDR-USD · HTTP 404 · 04/10/2026 13:50 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.842.186 vs $1.843.743 → 0,08%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,3959 vs $0,3961 → 0,06%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump_2026-10-04_055540.json',encoding='utf-8'));d=d.get('yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump',d);p=mock.patch('time.time',return_value=1791093340);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint yXJ9cYmX2Mp7JFhwZWz9NESbVes3VFAEGPf3rgKpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 04/10/2026 13:50 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `573d94fa001fac4a…`
