# DOTF (D O T ) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,3597 · liquidez $1.747.530 · mcap $359.693.314 (al detectar)  
Detectado el 06/10/2026 08:58 UTC por: WS score muy alto, MCap > $1M, Volumen alto (score 94, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 1%  
Ventana de la señal: hasta el 08/10/2026 08:58 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir D O T 

Estudio de cómo se adquiere D O T , con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 09:13 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 08:58 UTC | pumpswap `HHWweFK…2BPs` | $1.747.530 | 1% | 0,011% | 0,114% | 1,144% | $8.738 | $26.213 |
| consulta 06/10/2026 09:13 UTC | pumpswap `HHWweFK…2BPs` | $1.765.552 | 1% | 0,011% | 0,113% | 1,133% | $8.828 | $26.483 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump`
5. Configurar el slippage: 1% (liquidez $1.765.552, consulta 06/10/2026 09:13 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump) y el par en DexScreener (https://dexscreener.com/solana/HHWweFKzhuexnvGtz9SvKS62viE2WAJBC9AVqwxD2BPs); mint authority / freeze authority: revocada / revocada · holders 2.283 · top-10 5,47% (consulta 06/10/2026 09:13 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump
- Par en DexScreener: https://dexscreener.com/solana/HHWweFKzhuexnvGtz9SvKS62viE2WAJBC9AVqwxD2BPs
- Página del lanzamiento (pump.fun): https://pump.fun/coin/3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.283 · top-10 5,47% (consulta 06/10/2026 09:13 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | DOTF / D O T  | registro de la detección (trending) |
| Mint / contrato | `3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HHWweFKzhuexnvGtz9SvKS62viE2WAJBC9AVqwxD2BPs` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 09:13 UTC) |
| Deployer | `5SFrCriMdFuhhyzAfr2CE55ZreHjdPTeoWAUitSHSCSG` | RugCheck `creator` |
| Par creado | 06/10/2026 02:46 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 6,2 h / 6,2 h / 6,4 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 09:13 UTC |
| Holders / top-10 | 2.283 / 5,47% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 09:13 UTC |
| Holders efectivos del top-10 | 9,1 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 09:13 UTC |
| Etiquetas de RugCheck | «High market cap per holder», «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 09:13 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HHWweFKzhuexnvGtz9SvKS62viE2WAJBC9AVqwxD2BPs · Solscan: https://solscan.io/token/3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump · pump.fun: https://pump.fun/coin/3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump · web / Telegram / X: no publicados en DexScreener | consulta 06/10/2026 09:13 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 09:13 UTC)
- **Historia:**
  - Par creado el 06/10/2026 02:46 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 08:58 UTC, con el par a 6,2 h de creado: precio $0,3597, mcap $359.693.314, liquidez $1.747.530.
  - Velas de 1 h de GeckoTerminal (8, desde 06/10/2026 02:00 UTC): apertura $0,01076 · máximo $0,3668 (06/10/2026 09:00 UTC) · mínimo $0,00005000 (06/10/2026 02:00 UTC) · último cierre $0,3668.
  - En la consulta 06/10/2026 09:13 UTC: precio $0,3673, liquidez $1.765.552, FDV $367.284.795.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 08:58 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,3597 |
| Liquidez | $1.747.530 |
| MCap | $359.693.314 |
| Volumen 24 h | $883.346 |
| Cambio 24 h | +718.455% |
| Cambio m5 / h1 | +0,5% / +9,1% |
| Volumen m5 / h1 | $2.613 / $39.992 |
| Trades m5 (compras / ventas) | 31 / 5 |
| Edad del par | 6,2 h |
| Score del feed (WS) | 82 |

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

Desglose reconstruido desde los motivos registrados; suma 94 = score registrado 94 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 82 × 0,3 | +24,5 |
| MCap | ≥ $1M | $359.693.314 | +25 |
| Volumen 24 h | ≥ $100K | $883.346 | +15 |
| Buy pressure m5 | > 60% (par maduro) | 86% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,5% · h1 +9,1% | +20 |
| Volumen m5 | > $1K (par maduro) | $2.613 | +10 |
| Liquidez | ≥ $100K | $1.747.530 | +15 |
| Cambio 24 h | ≥ +50% | +718.455% | +10 |
| Sobrecompra | cambio 24 h > 50.000% | +718.455% · liq/mcap 0,5% | -50 |
| **Total** | recortado a 0–100 |  | **94** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T08:58:25+00:00, sin estado previo): **94** · motivos: WS score muy alto, MCap > $1M, Volumen alto, Buy pressure >60%, Momentum corto+medio positivo, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA EXTREMA (>50,000%).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 18 de 14.742 tokens analizados (0,12%) quedan ≥ 56. Con score 94, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 08:58 UTC, hasta 08/10/2026 08:58 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +0,5% · h1 +9,1% · h24 +718.455% · volumen m5/h1 0,07 · edad del par 6,2 h.
- **Precio de entrada** (alerta): $0,3597.
- **Consulta 06/10/2026 09:13 UTC:** $0,3673 (+2,1% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump_2026-10-06_085825.json` · blob `3b0a2de8b7ea811783c348c5413c8fba43be6d24` · commit `f572d01` (2026-10-06T09:05:55Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-06_085214.json` · blob `6bc7e519723cb7bb87ab91b2df7ae4b2d80fca74` · commit `f572d01` (2026-10-06T09:05:55Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_085825`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump · registro · 06/10/2026 08:58 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump · HTTP 200 · 06/10/2026 09:13 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump/report · HTTP 200 · 06/10/2026 09:13 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump · HTTP 200 · 06/10/2026 09:13 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HHWweFKzhuexnvGtz9SvKS62viE2WAJBC9AVqwxD2BPs/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 09:13 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump · HTTP 404 · 06/10/2026 09:13 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $1.765.552 vs $1.762.100 → 0,20%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,3673 vs $0,3668 → 0,13%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump_2026-10-06_085825.json',encoding='utf-8'));d=d.get('3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump',d);p=mock.patch('time.time',return_value=1791277105);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 3oa5Gy38GwD5aRZHuitScfVfGafhYPPn7D5XYFgPpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 09:13 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `640df9798e4bdcd3…`
