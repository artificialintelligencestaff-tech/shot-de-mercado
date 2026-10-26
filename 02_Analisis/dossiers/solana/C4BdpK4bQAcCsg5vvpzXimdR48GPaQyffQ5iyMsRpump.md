# Trust in Trump (TIT) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0005802 · liquidez $66.675 · mcap $578.331 (al detectar)  
Detectado el 26/10/2026 02:42 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 28/10/2026 02:42 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir TIT

Estudio de cómo se adquiere TIT, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 26/10/2026 02:42 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 26/10/2026 02:42 UTC | pumpswap `4CnX9xk…MuiQ` | $66.675 | 5% | 0,300% | 3,000% | 29,996% | $333 | $1.000 |
| consulta 26/10/2026 02:42 UTC | pumpswap `4CnX9xk…MuiQ` | $66.270 | 5% | 0,302% | 3,018% | 30,180% | $331 | $994 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump`
5. Configurar el slippage: 5% (liquidez $66.270, consulta 26/10/2026 02:42 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump) y el par en DexScreener (https://dexscreener.com/solana/4CnX9xktKXKckBHGwiNjCXhpVcf2F4xXcaE5CrA7MuiQ); mint authority / freeze authority: revocada / revocada · holders 5.997 · top-10 8,79% (consulta 26/10/2026 02:42 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump
- Par en DexScreener: https://dexscreener.com/solana/4CnX9xktKXKckBHGwiNjCXhpVcf2F4xXcaE5CrA7MuiQ
- Página del lanzamiento (pump.fun): https://pump.fun/coin/C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.997 · top-10 8,79% (consulta 26/10/2026 02:42 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Trust in Trump / TIT | registro de la detección (trending) |
| Mint / contrato | `C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `4CnX9xktKXKckBHGwiNjCXhpVcf2F4xXcaE5CrA7MuiQ` | DexScreener, al detectar (2 par(es) en la consulta 26/10/2026 02:42 UTC) |
| Deployer | `ENaDEVTsYMBbn1129MHxHGzuQUaUBg56mMANDYSejjYA` | RugCheck `creator` |
| Par creado | 26/10/2026 00:48 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 113,5 min / 113,7 min / 113,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 26/10/2026 02:42 UTC |
| Holders / top-10 | 5.997 / 8,79% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 26/10/2026 02:42 UTC |
| Holders efectivos del top-10 | 1,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 26/10/2026 02:42 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 26/10/2026 02:42 UTC |
| Links | DexScreener: https://dexscreener.com/solana/4CnX9xktKXKckBHGwiNjCXhpVcf2F4xXcaE5CrA7MuiQ · Solscan: https://solscan.io/token/C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump · pump.fun: https://pump.fun/coin/C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump · web: https://trustintrump.site · twitter: https://x.com/TrustInTrumpX | consulta 26/10/2026 02:42 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 26/10/2026 02:42 UTC)
- **Historia:**
  - Par creado el 26/10/2026 00:48 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 26/10/2026 02:42 UTC, con el par a 113,5 min de creado: precio $0,0005802, mcap $578.331, liquidez $66.675.
  - Velas de 1 h de GeckoTerminal (3, desde 26/10/2026 00:00 UTC): apertura $0,00006004 · máximo $0,002262 (26/10/2026 01:00 UTC) · mínimo $0,00006004 (26/10/2026 00:00 UTC) · último cierre $0,0005006.
  - En la consulta 26/10/2026 02:42 UTC: precio $0,0005732, liquidez $66.270, FDV $571.389.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 26/10/2026 02:42 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0005802 |
| Liquidez | $66.675 |
| MCap | $578.331 |
| Volumen 24 h | $2.789.292 |
| Cambio 24 h | +859% |
| Cambio m5 / h1 | -1,1% / -54,0% |
| Volumen m5 / h1 | $37.706 / $459.561 |
| Trades m5 (compras / ventas) | 1.353 / 190 |
| Edad del par | 113,5 min |
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
| Score del feed | score WS × 0,3 | WS 79 × 0,3 | +23,8 |
| MCap | ≥ $100K | $578.331 | +15 |
| Volumen 24 h | ≥ $1M | $2.789.292 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 88% | +25 |
| Edge temprano | edad < 4 h (par maduro) | edad 113,5 min | +8 |
| Volumen m5 | > $1K (par maduro) | $37.706 | +10 |
| Liquidez | ≥ $50K | $66.675 | +10 |
| Cambio 24 h | ≥ +50% | +859% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +859% · liq/mcap 11,5% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-26T02:42:29+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=11.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 77 de 45.974 tokens analizados (0,17%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 26/10/2026 02:42 UTC, hasta 28/10/2026 02:42 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -1,1% · h1 -54,0% · h24 +859% · volumen m5/h1 0,08 · edad del par 113,5 min.
- **Precio de entrada** (alerta): $0,0005802.
- **Consulta 26/10/2026 02:42 UTC:** $0,0005732 (-1,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump_2026-10-26_024242.json` · blob `aa52c720c389e9189523a9aee45f9834e9e806b7` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-26_023726.json` · blob `c05f552b4ddc6769e765522267f6ae3d8e67e3e5` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-26_024242`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump · registro · 26/10/2026 02:42 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump · HTTP 200 · 26/10/2026 02:42 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump/report · HTTP 200 · 26/10/2026 02:42 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump · HTTP 200 · 26/10/2026 02:42 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/4CnX9xktKXKckBHGwiNjCXhpVcf2F4xXcaE5CrA7MuiQ/ohlcv/hour?limit=1000 · HTTP 200 · 26/10/2026 02:42 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump · HTTP 404 · 26/10/2026 02:42 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=TITUSDT · HTTP 400 · 26/10/2026 02:42 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/TIT-USD · HTTP 404 · 26/10/2026 02:42 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $66.270 vs $62.240 → 6,08%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0005732 vs $0,0005006 → 12,66%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump_2026-10-26_024242.json',encoding='utf-8'));d=d.get('C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump',d);p=mock.patch('time.time',return_value=1792982549);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint C4BdpK4bQAcCsg5vvpzXimdR48GPaQyffQ5iyMsRpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 26/10/2026 02:42 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `1f5d5b538b9e03bb…`
