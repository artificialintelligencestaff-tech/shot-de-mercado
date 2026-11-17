# Vice City Bawsaq (BAWSAQ) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,001883 · liquidez $102.350 · mcap $1.874.338 (al detectar)  
Detectado el 17/11/2026 03:15 UTC por: WS score alto, MCap > $1M, Volumen masivo (score 100, scorer 7.2.1)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 19/11/2026 03:15 UTC (< 48 h) · vigente: quedan 48,0 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir BAWSAQ

Estudio de cómo se adquiere BAWSAQ, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 17/11/2026 03:15 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 17/11/2026 03:15 UTC | pumpswap `B8a1mw1…1jqv` | $102.350 | 5% | 0,195% | 1,954% | 19,541% | $512 | $1.535 |
| consulta 17/11/2026 03:15 UTC | pumpswap `B8a1mw1…1jqv` | $101.893 | 5% | 0,196% | 1,963% | 19,628% | $509 | $1.528 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump`
5. Configurar el slippage: 5% (liquidez $101.893, consulta 17/11/2026 03:15 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) y el par en DexScreener (https://dexscreener.com/solana/B8a1mw1vfm5pnm4RgUd8zhbtBnkPB2fBMdikU33Z1jqv); mint authority / freeze authority: revocada / revocada · holders 3.676 · top-10 20,54% (consulta 17/11/2026 03:15 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump
- Par en DexScreener: https://dexscreener.com/solana/B8a1mw1vfm5pnm4RgUd8zhbtBnkPB2fBMdikU33Z1jqv
- Página del lanzamiento (pump.fun): https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.676 · top-10 20,54% (consulta 17/11/2026 03:15 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Vice City Bawsaq / BAWSAQ | registro de la detección (trending) |
| Mint / contrato | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `B8a1mw1vfm5pnm4RgUd8zhbtBnkPB2fBMdikU33Z1jqv` | DexScreener, al detectar (3 par(es) en la consulta 17/11/2026 03:15 UTC) |
| Deployer | `ZXezTa6K1KEtbZwodqu6ScPWraVVdu1Y1AjotR5se5p` | RugCheck `creator` |
| Par creado | 16/11/2026 20:03 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 7,2 h / 7,2 h / 7,2 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 17/11/2026 03:15 UTC |
| Holders / top-10 | 3.676 / 20,54% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 17/11/2026 03:15 UTC |
| Holders efectivos del top-10 | 9,9 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 17/11/2026 03:15 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 17/11/2026 03:15 UTC |
| Links | DexScreener: https://dexscreener.com/solana/B8a1mw1vfm5pnm4RgUd8zhbtBnkPB2fBMdikU33Z1jqv · Solscan: https://solscan.io/token/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump · pump.fun: https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump · web: https://gtabawsaq.fun · twitter: https://x.com/VCBawsaqSOL | consulta 17/11/2026 03:15 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 17/11/2026 03:15 UTC)
- **Historia:**
  - Par creado el 16/11/2026 20:03 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 17/11/2026 03:15 UTC, con el par a 7,2 h de creado: precio $0,001883, mcap $1.874.338, liquidez $102.350.
  - Velas de 1 h de GeckoTerminal (8, desde 16/11/2026 20:00 UTC): apertura $0,00008469 · máximo $0,003247 (16/11/2026 21:00 UTC) · mínimo $0,00008469 (16/11/2026 20:00 UTC) · último cierre $0,001835.
  - En la consulta 17/11/2026 03:15 UTC: precio $0,001866, liquidez $101.893, FDV $1.857.816.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 17/11/2026 03:15 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,001883 |
| Liquidez | $102.350 |
| MCap | $1.874.338 |
| Volumen 24 h | $1.822.281 |
| Cambio 24 h | +2.110% |
| Cambio m5 / h1 | -0,2% / +23,1% |
| Volumen m5 / h1 | $4.291 / $112.971 |
| Trades m5 (compras / ventas) | 369 / 218 |
| Edad del par | 7,2 h |
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
| Score del feed | score WS × 0,3 | WS 79 × 0,3 | +23,6 |
| MCap | ≥ $1M | $1.874.338 | +25 |
| Volumen 24 h | ≥ $1M | $1.822.281 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 63% | +25 |
| Volumen m5 | > $1K (par maduro) | $4.291 | +10 |
| Liquidez | ≥ $100K | $102.350 | +15 |
| Cambio 24 h | ≥ +50% | +2.110% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +2.110% · liq/mcap 5,5% | +0 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-11-17T03:15:09+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $1M, Volumen masivo, Buy pressure >60%, Volumen activo m5 (>$1K), Liquidez alta, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=5.5% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 104 de 47.357 tokens analizados (0,22%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 17/11/2026 03:15 UTC, hasta 19/11/2026 03:15 UTC · vigente: quedan 48,0 h.
- **Aceleración al detectar:** cambio m5 -0,2% · h1 +23,1% · h24 +2.110% · volumen m5/h1 0,04 · edad del par 7,2 h.
- **Precio de entrada** (alerta): $0,001883.
- **Consulta 17/11/2026 03:15 UTC:** $0,001866 (-0,9% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump_2026-11-17_031532.json` · blob `881458b0baaf0d8eed336c2c9e0c520ad2e0ab7e` · commit pendiente (archivo sin commitear)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-11-17_031004.json` · blob `9cb74dc6e5d1cb014aa79a06f796de78f77ce76d` · commit pendiente (archivo sin commitear)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-11-17_031532`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump · registro · 17/11/2026 03:15 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump · HTTP 200 · 17/11/2026 03:15 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump/report · HTTP 200 · 17/11/2026 03:15 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump · HTTP 200 · 17/11/2026 03:15 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/B8a1mw1vfm5pnm4RgUd8zhbtBnkPB2fBMdikU33Z1jqv/ohlcv/hour?limit=1000 · HTTP 200 · 17/11/2026 03:15 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump · HTTP 404 · 17/11/2026 03:15 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BAWSAQUSDT · HTTP 400 · 17/11/2026 03:15 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BAWSAQ-USD · HTTP 404 · 17/11/2026 03:15 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $101.893 vs $102.391 → 0,49%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,001866 vs $0,001835 → 1,64%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump_2026-11-17_031532.json',encoding='utf-8'));d=d.get('D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump',d);p=mock.patch('time.time',return_value=1794885309);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 17/11/2026 03:15 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `a813c3ff5dd46511…`
