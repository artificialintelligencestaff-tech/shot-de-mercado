# ConConAI (ConConAI) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,002787 · liquidez $148.915 · mcap $2.785.312 (al detectar)  
Detectado el 07/10/2026 14:17 UTC por: MCap > $1M, Volumen decente, Buy pressure >55% (score 88, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 09/10/2026 14:17 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir ConConAI

Estudio de cómo se adquiere ConConAI, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 07/10/2026 14:40 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 07/10/2026 14:17 UTC | pumpswap `C8Vr7AF…M312` | $148.915 | 5% | 0,134% | 1,343% | 13,430% | $745 | $2.234 |
| consulta 07/10/2026 14:40 UTC | pumpswap `C8Vr7AF…M312` | $149.697 | 5% | 0,134% | 1,336% | 13,360% | $748 | $2.245 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump`
5. Configurar el slippage: 5% (liquidez $149.697, consulta 07/10/2026 14:40 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump) y el par en DexScreener (https://dexscreener.com/solana/C8Vr7AFWJMZZAbnyxc5Em7VtMJgCVFXpC3G7GxLwM312); mint authority / freeze authority: revocada / revocada · holders 3.994 · top-10 2,93% (consulta 07/10/2026 14:40 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump
- Par en DexScreener: https://dexscreener.com/solana/C8Vr7AFWJMZZAbnyxc5Em7VtMJgCVFXpC3G7GxLwM312
- Página del lanzamiento (pump.fun): https://pump.fun/coin/pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 3.994 · top-10 2,93% (consulta 07/10/2026 14:40 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | ConConAI / ConConAI | registro de la detección (pumpportal) |
| Mint / contrato | `pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `C8Vr7AFWJMZZAbnyxc5Em7VtMJgCVFXpC3G7GxLwM312` | DexScreener, al detectar (2 par(es) en la consulta 07/10/2026 14:40 UTC) |
| Deployer | `9eTtqcRaK8eezi8oBq26Y5AJmvAnx1e1SqDdJUWa33by` | PumpPortal (evento create), al detectar |
| Par creado | 07/10/2026 13:16 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 61,2 min / 61,2 min / 84,4 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 07/10/2026 14:40 UTC |
| Holders / top-10 | 3.994 / 2,93% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 07/10/2026 14:40 UTC |
| Holders efectivos del top-10 | 1,2 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 07/10/2026 14:40 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 07/10/2026 14:40 UTC |
| Links | DexScreener: https://dexscreener.com/solana/C8Vr7AFWJMZZAbnyxc5Em7VtMJgCVFXpC3G7GxLwM312 · Solscan: https://solscan.io/token/pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump · pump.fun: https://pump.fun/coin/pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump · web / Telegram / X: no publicados en DexScreener | consulta 07/10/2026 14:40 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 07/10/2026 14:40 UTC)
- **Historia:**
  - Par creado el 07/10/2026 13:16 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 07/10/2026 14:17 UTC, con el par a 61,2 min de creado: precio $0,002787, mcap $2.785.312, liquidez $148.915.
  - Velas de 1 h de GeckoTerminal (2, desde 07/10/2026 13:00 UTC): apertura $0,0003578 · máximo $0,002825 (07/10/2026 14:00 UTC) · mínimo $0,00004830 (07/10/2026 13:00 UTC) · último cierre $0,002821.
  - En la consulta 07/10/2026 14:40 UTC: precio $0,002820, liquidez $149.697, FDV $2.818.317.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 07/10/2026 14:17 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,002787 |
| Liquidez | $148.915 |
| MCap | $2.785.312 |
| Volumen 24 h | $70.519 |
| Cambio 24 h | +5.676% |
| Cambio m5 / h1 | -1,1% / +4,4% |
| Volumen m5 / h1 | $675 / $7.166 |
| Trades m5 (compras / ventas) | 14 / 10 |
| Edad del par | 61,2 min |
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

Desglose reconstruido desde los motivos registrados; suma 88 = score registrado 88 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| MCap | ≥ $1M | $2.785.312 | +25 |
| Volumen 24 h | ≥ $50K | $70.519 | +10 |
| Buy pressure m5 | > 55% (par maduro) | 58% | +15 |
| Edge temprano | edad < 4 h (par maduro) | edad 61,2 min | +8 |
| Volumen m5 | > $500 (par maduro) | $675 | +5 |
| Liquidez | ≥ $100K | $148.915 | +15 |
| Cambio 24 h | ≥ +50% | +5.676% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +5.676% · liq/mcap 5,3% | +0 |
| **Total** | recortado a 0–100 |  | **88** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-07T14:17:17+00:00, sin estado previo): **88** · motivos: MCap > $1M, Volumen decente, Buy pressure >55%, Edge temprano (<4h), Volumen moderado m5, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=5.3% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 29 de 18.841 tokens analizados (0,15%) quedan ≥ 56. Con score 88, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 07/10/2026 14:17 UTC, hasta 09/10/2026 14:17 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 -1,1% · h1 +4,4% · h24 +5.676% · volumen m5/h1 0,09 · edad del par 61,2 min.
- **Precio de entrada** (alerta): $0,002787.
- **Consulta 07/10/2026 14:40 UTC:** $0,002820 (+1,2% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump_2026-10-07_141717.json` · blob `6ae154b63e8b908fff7f8bd907c31e55d6da9535` · commit `ff65746` (2026-10-07T14:33:14Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-07_141717`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump · registro · 07/10/2026 14:17 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump · HTTP 200 · 07/10/2026 14:40 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump/report · HTTP 200 · 07/10/2026 14:40 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump · HTTP 200 · 07/10/2026 14:40 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/C8Vr7AFWJMZZAbnyxc5Em7VtMJgCVFXpC3G7GxLwM312/ohlcv/hour?limit=1000 · HTTP 200 · 07/10/2026 14:40 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump · HTTP 404 · 07/10/2026 14:40 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=CONCONAIUSDT · HTTP 400 · 07/10/2026 14:40 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/CONCONAI-USD · HTTP 404 · 07/10/2026 14:40 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $149.697 vs $148.992 → 0,47%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,002820 vs $0,002821 → 0,03%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump_2026-10-07_141717.json',encoding='utf-8'));d=d.get('pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump',d);p=mock.patch('time.time',return_value=1791382637);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint pmGXrmpvbWJJebWxE3RBAkdUbY1VPuwRZuU27Nepump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 07/10/2026 14:40 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `ba0bcc9cabde6de8…`
