# RAMBO (RAMBO) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,01262 · liquidez $308.021 · mcap $12.447.822 (al detectar)  
Detectado el 12/11/2026 20:31 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 93, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 14/11/2026 20:31 UTC (< 48 h) · vigente: quedan 43,9 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir RAMBO

Estudio de cómo se adquiere RAMBO, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 13/11/2026 00:36 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 12/11/2026 20:31 UTC | pumpswap `Gz15vwS…cvFk` | $308.021 | 3% | 0,065% | 0,649% | 6,493% | $1.540 | $4.620 |
| consulta 13/11/2026 00:36 UTC | pumpswap `Gz15vwS…cvFk` | $303.511 | 3% | 0,066% | 0,659% | 6,590% | $1.518 | $4.553 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump`
5. Configurar el slippage: 3% (liquidez $303.511, consulta 13/11/2026 00:36 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump) y el par en DexScreener (https://dexscreener.com/solana/Gz15vwSPY9KFYNkrMPkoKp2h9yygVBovoXJsGwSJcvFk); mint authority / freeze authority: revocada / revocada · holders 38.894 · top-10 3,51% (consulta 13/11/2026 00:36 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump
- Par en DexScreener: https://dexscreener.com/solana/Gz15vwSPY9KFYNkrMPkoKp2h9yygVBovoXJsGwSJcvFk
- Página del lanzamiento (pump.fun): https://pump.fun/coin/KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 38.894 · top-10 3,51% (consulta 13/11/2026 00:36 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | RAMBO / RAMBO | registro de la detección (trending) |
| Mint / contrato | `KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `Gz15vwSPY9KFYNkrMPkoKp2h9yygVBovoXJsGwSJcvFk` | DexScreener, al detectar (2 par(es) en la consulta 13/11/2026 00:36 UTC) |
| Deployer | `ECe3TqwSdnqbyifvFzHKsce33wfQ8eG5t78b9ZV9rEdz` | RugCheck `creator` |
| Par creado | 03/11/2026 14:49 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 9,2 días / 9,2 días / 9,4 días | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 13/11/2026 00:36 UTC |
| Holders / top-10 | 38.894 / 3,51% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 13/11/2026 00:36 UTC |
| Holders efectivos del top-10 | 5,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0%; orca 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 13/11/2026 00:36 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 13/11/2026 00:36 UTC |
| Links | DexScreener: https://dexscreener.com/solana/Gz15vwSPY9KFYNkrMPkoKp2h9yygVBovoXJsGwSJcvFk · Solscan: https://solscan.io/token/KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump · pump.fun: https://pump.fun/coin/KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump · web: https://ramdefender.fun/ · twitter: https://x.com/ramdefender | consulta 13/11/2026 00:36 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 13/11/2026 00:36 UTC)
- **Historia:**
  - Par creado el 03/11/2026 14:49 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 12/11/2026 20:31 UTC, con el par a 9,2 días de creado: precio $0,01262, mcap $12.447.822, liquidez $308.021.
  - Velas de 1 h de GeckoTerminal (227, desde 03/11/2026 14:00 UTC): apertura $0,0001116 · máximo $0,01654 (12/11/2026 16:00 UTC) · mínimo $0,00009757 (03/11/2026 14:00 UTC) · último cierre $0,01230.
  - En la consulta 13/11/2026 00:36 UTC: precio $0,01224, liquidez $303.511, FDV $12.073.169.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 12/11/2026 20:31 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,01262 |
| Liquidez | $308.021 |
| MCap | $12.447.822 |
| Volumen 24 h | $3.537.058 |
| Cambio 24 h | +151% |
| Cambio m5 / h1 | +0,2% / +5,2% |
| Volumen m5 / h1 | $836 / $16.172 |
| Trades m5 (compras / ventas) | 10 / 2 |
| Edad del par | 9,2 días |
| Score del feed (WS) | 78 |

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

Desglose reconstruido desde los motivos registrados; suma 93 = score registrado 93 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 78 × 0,3 | +23,4 |
| MCap | ≥ $1M | $12.447.822 | +25 |
| Volumen 24 h | ≥ $1M | $3.537.058 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 83% | +25 |
| Momentum | m5 > 0 y h1 > 0 (par maduro) | m5 +0,2% · h1 +5,2% | +20 |
| Volumen m5 | > $500 (par maduro) | $836 | +5 |
| Par viejo | edad > 24 h | edad 9,2 días | -50 |
| Liquidez | ≥ $100K | $308.021 | +15 |
| Cambio 24 h | ≥ +50% | +151% | +10 |
| **Total** | recortado a 0–100 |  | **93** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-12T20:31:04+00:00, sin estado previo): **93** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Momentum corto+medio positivo, Volumen moderado m5, Par >24h, no nativo pump.fun, Liquidez alta, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 98 de 47.123 tokens analizados (0,21%) quedan ≥ 56. Con score 93, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 12/11/2026 20:31 UTC, hasta 14/11/2026 20:31 UTC · vigente: quedan 43,9 h.
- **Aceleración al detectar:** cambio m5 +0,2% · h1 +5,2% · h24 +151% · volumen m5/h1 0,05 · edad del par 9,2 días.
- **Precio de entrada** (alerta): $0,01262.
- **Consulta 13/11/2026 00:36 UTC:** $0,01224 (-3,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump_2026-11-12_203104.json` · blob `4778cd21fe35809f93a72e3ec364753091881489` · commit `abac0ca` (2026-11-13T00:29:26Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-12_203104`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump · registro · 12/11/2026 20:31 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump · HTTP 200 · 13/11/2026 00:36 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump/report · HTTP 200 · 13/11/2026 00:36 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump · HTTP 200 · 13/11/2026 00:36 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/Gz15vwSPY9KFYNkrMPkoKp2h9yygVBovoXJsGwSJcvFk/ohlcv/hour?limit=1000 · HTTP 200 · 13/11/2026 00:36 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump · HTTP 404 · 13/11/2026 00:36 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=RAMBOUSDT · HTTP 400 · 13/11/2026 00:36 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/RAMBO-USD · HTTP 404 · 13/11/2026 00:36 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $303.511 vs $304.158 → 0,21%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,01224 vs $0,01230 → 0,48%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump_2026-11-12_203104.json',encoding='utf-8'));d=d.get('KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump',d);p=mock.patch('time.time',return_value=1794515464);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint KMifrkYmDdAKtVXAVBEPEQxJ7qP2iLgUcfZjUZipump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 13/11/2026 00:36 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `f8e4c80474950c64…`
