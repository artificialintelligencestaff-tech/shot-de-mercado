# Sand Witch Kitten (SNDWITCH) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0003110 · liquidez $52.342 · mcap $308.355 (al detectar)  
Detectado el 06/10/2026 23:37 UTC por: WS score alto, MCap > $100K, Volumen masivo (score 100, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 08/10/2026 23:37 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir SNDWITCH

Estudio de cómo se adquiere SNDWITCH, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 06/10/2026 23:54 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 06/10/2026 23:37 UTC | pumpswap `HU22UBa…ugDB` | $52.342 | 5% | 0,382% | 3,821% | 38,211% | $262 | $785 |
| consulta 06/10/2026 23:53 UTC | pumpswap `HU22UBa…ugDB` | $51.013 | 5% | 0,392% | 3,921% | 39,206% | $255 | $765 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump`
5. Configurar el slippage: 5% (liquidez $51.013, consulta 06/10/2026 23:53 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump) y el par en DexScreener (https://dexscreener.com/solana/HU22UBaTZa7AjMkDJaSyoDHtfFw6XVS6d9bSXLt9ugDB); mint authority / freeze authority: revocada / revocada · holders 5.608 · top-10 11,56% (consulta 06/10/2026 23:53 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump
- Par en DexScreener: https://dexscreener.com/solana/HU22UBaTZa7AjMkDJaSyoDHtfFw6XVS6d9bSXLt9ugDB
- Página del lanzamiento (pump.fun): https://pump.fun/coin/J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 5.608 · top-10 11,56% (consulta 06/10/2026 23:53 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Sand Witch Kitten / SNDWITCH | registro de la detección (trending) |
| Mint / contrato | `J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `HU22UBaTZa7AjMkDJaSyoDHtfFw6XVS6d9bSXLt9ugDB` | DexScreener, al detectar (2 par(es) en la consulta 06/10/2026 23:53 UTC) |
| Deployer | `7MaWuUDBFwasCZGXZ3qyoE97UNTKEkUSKjA4AheVaxev` | RugCheck `creator` |
| Par creado | 06/10/2026 19:37 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 4,0 h / 4,0 h / 4,3 h | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 06/10/2026 23:53 UTC |
| Holders / top-10 | 5.608 / 11,56% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 06/10/2026 23:53 UTC |
| Holders efectivos del top-10 | 1,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 06/10/2026 23:53 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 06/10/2026 23:53 UTC |
| Links | DexScreener: https://dexscreener.com/solana/HU22UBaTZa7AjMkDJaSyoDHtfFw6XVS6d9bSXLt9ugDB · Solscan: https://solscan.io/token/J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump · pump.fun: https://pump.fun/coin/J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump · web: https://www.sndwitch.fun · twitter: https://x.com/sndwitch_sol | consulta 06/10/2026 23:53 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 06/10/2026 23:53 UTC)
- **Historia:**
  - Par creado el 06/10/2026 19:37 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 06/10/2026 23:37 UTC, con el par a 4,0 h de creado: precio $0,0003110, mcap $308.355, liquidez $52.342.
  - Velas de 1 h de GeckoTerminal (5, desde 06/10/2026 19:00 UTC): apertura $0,0002321 · máximo $0,0008196 (06/10/2026 20:00 UTC) · mínimo $0,00006676 (06/10/2026 19:00 UTC) · último cierre $0,0002947.
  - En la consulta 06/10/2026 23:53 UTC: precio $0,0002947, liquidez $51.013, FDV $292.185.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 06/10/2026 23:37 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0003110 |
| Liquidez | $52.342 |
| MCap | $308.355 |
| Volumen 24 h | $1.563.150 |
| Cambio 24 h | +365% |
| Cambio m5 / h1 | -1,9% / +11,3% |
| Volumen m5 / h1 | $4.840 / $71.565 |
| Trades m5 (compras / ventas) | 228 / 93 |
| Edad del par | 4,0 h |
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
| MCap | ≥ $100K | $308.355 | +15 |
| Volumen 24 h | ≥ $1M | $1.563.150 | +20 |
| Buy pressure m5 | > 60% (par maduro) | 71% | +25 |
| Volumen m5 | > $1K (par maduro) | $4.840 | +10 |
| Liquidez | ≥ $50K | $52.342 | +10 |
| Cambio 24 h | ≥ +50% | +365% | +10 |
| **Total** | recortado a 0–100 |  | **100** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-06T23:37:12+00:00, sin estado previo): **100** · motivos: WS score alto, MCap > $100K, Volumen masivo, Buy pressure >60%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez decente, Pump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 21 de 17.284 tokens analizados (0,12%) quedan ≥ 56. Con score 100, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 06/10/2026 23:37 UTC, hasta 08/10/2026 23:37 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -1,9% · h1 +11,3% · h24 +365% · volumen m5/h1 0,07 · edad del par 4,0 h.
- **Precio de entrada** (alerta): $0,0003110.
- **Consulta 06/10/2026 23:53 UTC:** $0,0002947 (-5,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump_2026-10-06_233712.json` · blob `65c08101d0a1f2de5e72818153c6b5b431ba71bb` · commit `e2cfee3` (2026-10-06T23:47:41Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-06_233031.json` · blob `6b7cd684c6e29360dcd5629a16fea099ffd0b121` · commit `e2cfee3` (2026-10-06T23:47:41Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-06_233712`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump · registro · 06/10/2026 23:37 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump · HTTP 200 · 06/10/2026 23:53 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump/report · HTTP 200 · 06/10/2026 23:54 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump · HTTP 200 · 06/10/2026 23:54 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/HU22UBaTZa7AjMkDJaSyoDHtfFw6XVS6d9bSXLt9ugDB/ohlcv/hour?limit=1000 · HTTP 200 · 06/10/2026 23:54 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump · HTTP 404 · 06/10/2026 23:54 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=SNDWITCHUSDT · HTTP 400 · 06/10/2026 23:54 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/SNDWITCH-USD · HTTP 404 · 06/10/2026 23:54 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $51.013 vs $51.122 → 0,21%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0002947 vs $0,0002947 → 0,02%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump_2026-10-06_233712.json',encoding='utf-8'));d=d.get('J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump',d);p=mock.patch('time.time',return_value=1791329832);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint J9qzFhTLYnmf3tZYvHBaF96rH3YKToELAAVMzz66pump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 06/10/2026 23:54 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `82a4b6200a211cc2…`
