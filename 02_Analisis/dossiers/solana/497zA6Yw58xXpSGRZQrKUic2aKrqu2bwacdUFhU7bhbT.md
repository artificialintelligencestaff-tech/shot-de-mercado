# Magnifica Humanitas (Humanitas) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00004143 · liquidez $16.802 · mcap $41.437 (al detectar)  
Detectado el 07/10/2026 13:28 UTC por: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 20.3 · estructura 12.6 · precio/volumen 8.6 · cobertura 93/100, [info] narrative_wave: ola 'magnifica': 13 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 42, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 09/10/2026 13:28 UTC (< 48 h) · vigente: quedan 47,8 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir Humanitas

Estudio de cómo se adquiere Humanitas, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/10/2026 13:41 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/10/2026 13:28 UTC | pumpswap `DFxU7pH…Dhxd` | $16.802 | 10% | 1,190% | 11,903% | 119,034% | $84 | $252 |
| consulta 07/10/2026 13:41 UTC | pumpswap `DFxU7pH…Dhxd` | $5.925 | 10% | 3,375% | 33,753% | 337,529% | $30 | $89 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT`
5. Configurar el slippage: 10% (liquidez $5.925, consulta 07/10/2026 13:41 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT) y el par en DexScreener (https://dexscreener.com/solana/DFxU7pH9oXgdTZS4CSH7qhT2UQCbZJSEDe1nmuzpDhxd); mint authority / freeze authority: revocada / revocada · holders 2.071 · top-10 70,48% (consulta 07/10/2026 13:41 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT
- Par en DexScreener: https://dexscreener.com/solana/DFxU7pH9oXgdTZS4CSH7qhT2UQCbZJSEDe1nmuzpDhxd
- Página del lanzamiento (pump.fun): https://pump.fun/coin/497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.071 · top-10 70,48% (consulta 07/10/2026 13:41 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Magnifica Humanitas / Humanitas | registro de la detección (pumpportal_live) |
| Mint / contrato | `497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DFxU7pH9oXgdTZS4CSH7qhT2UQCbZJSEDe1nmuzpDhxd` | DexScreener, al detectar (2 par(es) en la consulta 07/10/2026 13:41 UTC) |
| Deployer | `CXoUJHtBGnuNR6zJ3zm8nTnNzCwXxFViXh29d1kTJQmK` | PumpPortal (evento create), al detectar |
| Par creado | 07/10/2026 13:18 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,4 min / 10,4 min / 22,9 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/10/2026 13:41 UTC |
| Holders / top-10 | 2.071 / 70,48% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/10/2026 13:41 UTC |
| Holders efectivos del top-10 | 1,7 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/10/2026 13:41 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 07/10/2026 13:41 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DFxU7pH9oXgdTZS4CSH7qhT2UQCbZJSEDe1nmuzpDhxd · Solscan: https://solscan.io/token/497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT · pump.fun: https://pump.fun/coin/497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT · web / Telegram / X: no publicados en DexScreener | consulta 07/10/2026 13:41 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/10/2026 13:41 UTC)
- **Historia:**
  - Par creado el 07/10/2026 13:18 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/10/2026 13:28 UTC, con el par a 10,4 min de creado: precio $0,00004143, mcap $41.437, liquidez $16.802.
  - Velas de 1 h de GeckoTerminal (1, desde 07/10/2026 13:00 UTC): apertura $0,00004309 · máximo $0,0001370 (07/10/2026 13:00 UTC) · mínimo $0,000006895 (07/10/2026 13:00 UTC) · último cierre $0,000006895.
  - En la consulta 07/10/2026 13:41 UTC: precio $0,000007384, liquidez $5.925, FDV $7.385.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/10/2026 13:28 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00004143 |
| Liquidez | $16.802 |
| MCap | $41.437 |
| Volumen 24 h | $352.080 |
| Cambio 24 h | -9% |
| Cambio m5 / h1 | -60,6% / -9,3% |
| Volumen m5 / h1 | $147.003 / $352.080 |
| Trades m5 (compras / ventas) | 1.655 / 1.292 |
| Edad del par | 10,4 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 42; motivos sin regla: young-0.4 · edad 10.4 min · pesos info 60 / estructura 20 / precio 20 · info 20.3 · estructura 12.6 · precio/volumen 8.6 · cobertura 93/100, [info] narrative_wave: ola 'magnifica': 13 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 2091 · top-10 43.5 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 2091/6954 = 0.30 → +0.5, [precio/volumen] volume_acceleration: vol 5 min ×5.0 la tasa horaria (s 1.00), [precio/volumen] buy_pressure_shift: compras 56% en 5 min vs 55% en 1 h (s 0.08), [precio/volumen] holder_accumulation: holders 1342→2091 (+124.8/min) · top10 30.4%→43.5% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=16801.92, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 42 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-07T13:28:53+00:00, sin estado previo): **15** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 29 de 18.711 tokens analizados (0,15%) quedan ≥ 56. Con score 15, este activo queda en el percentil 97,3 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/10/2026 13:28 UTC, hasta 09/10/2026 13:28 UTC · vigente: quedan 47,8 h.
- **Aceleración al detectar:** cambio m5 -60,6% · h1 -9,3% · h24 -9% · volumen m5/h1 0,42 · edad del par 10,4 min.
- **Precio de entrada** (alerta): $0,00004143.
- **Consulta 07/10/2026 13:41 UTC:** $0,000007384 (-82,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT_2026-10-07_132853.json` · blob `72c5493c6305e50595640d4c64284e263823bc72` · commit `13b06ca` (2026-10-07T13:33:52Z)
- **Archivo de la corrida:** `01_Datos_Crudos/final_detection/detection_2026-10-07_131146.json` · blob `ca40d2d6e50542cdd5a2ac904c0bb1b224791fd8` · commit `13b06ca` (2026-10-07T13:33:52Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-07_132853`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT · registro · 07/10/2026 13:28 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT · HTTP 200 · 07/10/2026 13:41 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT/report · HTTP 200 · 07/10/2026 13:41 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT · HTTP 200 · 07/10/2026 13:41 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DFxU7pH9oXgdTZS4CSH7qhT2UQCbZJSEDe1nmuzpDhxd/ohlcv/hour?limit=1000 · HTTP 200 · 07/10/2026 13:41 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT · HTTP 404 · 07/10/2026 13:41 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=HUMANITASUSDT · HTTP 400 · 07/10/2026 13:41 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/HUMANITAS-USD · HTTP 404 · 07/10/2026 13:41 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $5.925 vs $5.965 → 0,67%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000007384 vs $0,000006895 → 6,62%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT_2026-10-07_132853.json',encoding='utf-8'));d=d.get('497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT',d);p=mock.patch('time.time',return_value=1791379733);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 497zA6Yw58xXpSGRZQrKUic2aKrqu2bwacdUFhU7bhbT --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/10/2026 13:41 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `2dbf35a14c9ece09…`
