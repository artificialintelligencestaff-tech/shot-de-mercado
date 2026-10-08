# Trump Oil Reserve (OIL) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,000002035 · liquidez $2.049 · mcap $2.036 (al detectar)  
Detectado el 08/10/2026 02:35 UTC por: MCap bajo, Volumen alto, Edge temprano (<4h) (score 60, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 10/10/2026 02:35 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir OIL

Estudio de cómo se adquiere OIL, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 08/10/2026 03:08 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 08/10/2026 02:35 UTC | pumpswap `wZ3c25r…kBk2` | $2.049 | 10% | 9,759% | 97,589% | 975,886% | $10 | $31 |
| consulta 08/10/2026 03:07 UTC | pumpswap `wZ3c25r…kBk2` | $2.049 | 10% | 9,759% | 97,589% | 975,886% | $10 | $31 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump`
5. Configurar el slippage: 10% (liquidez $2.049, consulta 08/10/2026 03:07 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump) y el par en DexScreener (https://dexscreener.com/solana/wZ3c25r8NwkzPPdSmvGviGEvhGPJBMwhPMb87QPkBk2); mint authority / freeze authority: revocada / revocada · holders 20 · top-10 100,00% (consulta 08/10/2026 03:07 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump
- Par en DexScreener: https://dexscreener.com/solana/wZ3c25r8NwkzPPdSmvGviGEvhGPJBMwhPMb87QPkBk2
- Página del lanzamiento (pump.fun): https://pump.fun/coin/Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 20 · top-10 100,00% (consulta 08/10/2026 03:07 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Trump Oil Reserve / OIL | registro de la detección (pumpportal) |
| Mint / contrato | `Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `wZ3c25r8NwkzPPdSmvGviGEvhGPJBMwhPMb87QPkBk2` | DexScreener, al detectar (2 par(es) en la consulta 08/10/2026 03:07 UTC) |
| Deployer | `DMGPkrb3VAqryGH4kJXULiy71uF7KACU1reWvr6pg4eJ` | PumpPortal (evento create), al detectar |
| Par creado | 08/10/2026 01:34 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 61,7 min / 61,7 min / 93,8 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 08/10/2026 03:07 UTC |
| Holders / top-10 | 20 / 100,00% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 08/10/2026 03:07 UTC |
| Holders efectivos del top-10 | 1,0 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 08/10/2026 03:07 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 08/10/2026 03:07 UTC |
| Links | DexScreener: https://dexscreener.com/solana/wZ3c25r8NwkzPPdSmvGviGEvhGPJBMwhPMb87QPkBk2 · Solscan: https://solscan.io/token/Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump · pump.fun: https://pump.fun/coin/Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump · web / Telegram / X: no publicados en DexScreener | consulta 08/10/2026 03:07 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 08/10/2026 03:07 UTC)
- **Historia:**
  - Par creado el 08/10/2026 01:34 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 08/10/2026 02:35 UTC, con el par a 61,7 min de creado: precio $0,000002035, mcap $2.036, liquidez $2.049.
  - Velas de 1 h de GeckoTerminal (2, desde 08/10/2026 01:00 UTC): apertura $0,00004840 · máximo $0,003095 (08/10/2026 01:00 UTC) · mínimo $0,000002003 (08/10/2026 01:00 UTC) · último cierre $0,000002034.
  - En la consulta 08/10/2026 03:07 UTC: precio $0,000002035, liquidez $2.049, FDV $2.036.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 08/10/2026 02:35 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,000002035 |
| Liquidez | $2.049 |
| MCap | $2.036 |
| Volumen 24 h | $147.141 |
| Cambio 24 h | -96% |
| Cambio m5 / h1 | +0,0% / -99,9% |
| Volumen m5 / h1 | $0 / $80.045 |
| Trades m5 (compras / ventas) | 0 / 0 |
| Edad del par | 61,7 min |
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

Desglose no reproducible desde los motivos registrados (suma 18 vs score 60; motivos sin regla: score de detección 60 (script_82, hace 57 min) > re-score 18: vale el de detección (paridad con script_97)): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-08T02:35:53+00:00, sin estado previo): **18** · motivos: MCap bajo, Volumen alto, Edge temprano (<4h), Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 32 de 20.635 tokens analizados (0,16%) quedan ≥ 56. Con score 18, este activo queda en el percentil 97,4 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 08/10/2026 02:35 UTC, hasta 10/10/2026 02:35 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 +0,0% · h1 -99,9% · h24 -96% · volumen m5/h1 0,00 · edad del par 61,7 min.
- **Precio de entrada** (alerta): $0,000002035.
- **Consulta 08/10/2026 03:07 UTC:** $0,000002035 (+0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump_2026-10-08_023553.json` · blob `8c81383ed84e46aa35367e784bf479dd8cc6bcb9` · commit `579d875` (2026-10-08T03:07:06Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-08_023553`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump · registro · 08/10/2026 02:35 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump · HTTP 200 · 08/10/2026 03:07 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump/report · HTTP 200 · 08/10/2026 03:07 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump · HTTP 200 · 08/10/2026 03:07 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/wZ3c25r8NwkzPPdSmvGviGEvhGPJBMwhPMb87QPkBk2/ohlcv/hour?limit=1000 · HTTP 200 · 08/10/2026 03:07 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump · HTTP 404 · 08/10/2026 03:07 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=OILUSDT · HTTP 400 · 08/10/2026 03:07 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/OIL-USD · HTTP 404 · 08/10/2026 03:08 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.049 vs $2.147 → 4,56%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002035 vs $0,000002034 → 0,07%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump_2026-10-08_023553.json',encoding='utf-8'));d=d.get('Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump',d);p=mock.patch('time.time',return_value=1791426953);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint Abpn1v5oQyX34iDvAiv3whsNciQ6YPdtuJYRCePpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 08/10/2026 03:08 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `a057a452cdb4dcfe…`
