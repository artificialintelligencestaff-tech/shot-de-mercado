# 4CHAN (4CHAN) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00001840 · liquidez $9.846 · mcap $18.382 (al detectar)  
Detectado el 15/10/2026 00:45 UTC por: young-0.4 · edad 14.8 min · pesos info 58 / estructura 21 / precio 21 · info 22.4 · estructura 11.2 · precio/volumen 7.5 · cobertura 88/100, [info] narrative_wave: ola '4chan': 8 lanzamientos más en 1 h → +14.4, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.1 (score 41, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 17/10/2026 00:45 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir 4CHAN

Estudio de cómo se adquiere 4CHAN, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 15/10/2026 01:04 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 15/10/2026 00:45 UTC | pumpswap `igVE963…L5VD` | $9.846 | 10% | 2,031% | 20,313% | 203,125% | $49 | $148 |
| consulta 15/10/2026 01:04 UTC | pumpswap `igVE963…L5VD` | $9.129 | 10% | 2,191% | 21,909% | 219,086% | $46 | $137 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump`
5. Configurar el slippage: 10% (liquidez $9.129, consulta 15/10/2026 01:04 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump) y el par en DexScreener (https://dexscreener.com/solana/igVE963bkUEfxGbZfNXme33NyeUccRc94CWx3wML5VD); mint authority / freeze authority: revocada / revocada · holders 513 · top-10 85,51% (consulta 15/10/2026 01:04 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump
- Par en DexScreener: https://dexscreener.com/solana/igVE963bkUEfxGbZfNXme33NyeUccRc94CWx3wML5VD
- Página del lanzamiento (pump.fun): https://pump.fun/coin/9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 513 · top-10 85,51% (consulta 15/10/2026 01:04 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | 4CHAN / 4CHAN | registro de la detección (pumpportal_live) |
| Mint / contrato | `9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `igVE963bkUEfxGbZfNXme33NyeUccRc94CWx3wML5VD` | DexScreener, al detectar (9 par(es) en la consulta 15/10/2026 01:04 UTC) |
| Deployer | `8Bwg6XhcQS6g1CikNB4zqJF8tSVm9TpxfWsHTGnm8L2b` | PumpPortal (evento create), al detectar |
| Par creado | 15/10/2026 00:30 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 14,8 min / 14,8 min / 34,1 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 15/10/2026 01:04 UTC |
| Holders / top-10 | 513 / 85,51% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 15/10/2026 01:04 UTC |
| Holders efectivos del top-10 | 3,6 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | n/d | RugCheck `markets[].lp.lpLockedPct`, consulta 15/10/2026 01:04 UTC |
| Etiquetas de RugCheck | «Single holder ownership», «High holder concentration» | RugCheck `risks[].name` (texto de la fuente), consulta 15/10/2026 01:04 UTC |
| Links | DexScreener: https://dexscreener.com/solana/igVE963bkUEfxGbZfNXme33NyeUccRc94CWx3wML5VD · Solscan: https://solscan.io/token/9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump · pump.fun: https://pump.fun/coin/9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump · twitter: https://x.com/idkthelore/status/2110526660764213621 | consulta 15/10/2026 01:04 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 15/10/2026 01:04 UTC)
- **Historia:**
  - Par creado el 15/10/2026 00:30 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 15/10/2026 00:45 UTC, con el par a 14,8 min de creado: precio $0,00001840, mcap $18.382, liquidez $9.846.
  - Velas de 1 h de GeckoTerminal (2, desde 15/10/2026 00:00 UTC): apertura $0,00004031 · máximo $0,00004321 (15/10/2026 00:00 UTC) · mínimo $0,000005629 (15/10/2026 00:00 UTC) · último cierre $0,00001569.
  - En la consulta 15/10/2026 01:04 UTC: precio $0,00001593, liquidez $9.129, FDV $15.916.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 15/10/2026 00:45 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00001840 |
| Liquidez | $9.846 |
| MCap | $18.382 |
| Volumen 24 h | $105.916 |
| Cambio 24 h | -57% |
| Cambio m5 / h1 | +147,0% / -57,3% |
| Volumen m5 / h1 | $21.230 / $105.916 |
| Trades m5 (compras / ventas) | 315 / 159 |
| Edad del par | 14,8 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 41; motivos sin regla: young-0.4 · edad 14.8 min · pesos info 58 / estructura 21 / precio 21 · info 22.4 · estructura 11.2 · precio/volumen 7.5 · cobertura 88/100, [info] narrative_wave: ola '4chan': 8 lanzamientos más en 1 h → +14.4, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.1, [info] dex_profile: perfil pago en DexScreener → +2.9, [estructura] bonding_progress: graduado (pumpswap) → +10.2, [estructura] dev_wallet: creador compró 6.7 % del supply → +1.0, [precio/volumen] volume_acceleration: vol 5 min ×2.4 la tasa horaria (s 0.36), [precio/volumen] buy_pressure_shift: compras 66% en 5 min vs 55% en 1 h (s 0.56), [precio/volumen] liquidity_inflow: liquidez +54% en 8 min (s 1.00), [flag, no suma] tradable=True, liquidity_usd=9846.13, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 41 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-15T00:45:33+00:00, sin estado previo): **10** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 60 de 35.512 tokens analizados (0,17%) quedan ≥ 56. Con score 10, este activo queda en el percentil 93,6 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 15/10/2026 00:45 UTC, hasta 17/10/2026 00:45 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 +147,0% · h1 -57,3% · h24 -57% · volumen m5/h1 0,20 · edad del par 14,8 min.
- **Precio de entrada** (alerta): $0,00001840.
- **Consulta 15/10/2026 01:04 UTC:** $0,00001593 (-13,4% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump_2026-10-15_004533.json` · blob `d0d7f9c1d501ef109af9d5c891a7fa88d56f4ff6` · commit `2a78cf2` (2026-10-15T00:56:34Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-15_004533`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump · registro · 15/10/2026 00:45 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump · HTTP 200 · 15/10/2026 01:04 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump/report · HTTP 200 · 15/10/2026 01:04 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump · HTTP 200 · 15/10/2026 01:04 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/igVE963bkUEfxGbZfNXme33NyeUccRc94CWx3wML5VD/ohlcv/hour?limit=1000 · HTTP 200 · 15/10/2026 01:04 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump · HTTP 404 · 15/10/2026 01:04 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=4CHANUSDT · HTTP 400 · 15/10/2026 01:04 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/4CHAN-USD · HTTP 404 · 15/10/2026 01:04 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,00001593 vs $0,00001569 → 1,54%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump_2026-10-15_004533.json',encoding='utf-8'));d=d.get('9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump',d);p=mock.patch('time.time',return_value=1792025133);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 9QnJtF4W6nkcnYhzmXRbNvxPhbWhTWNDUQgYH2bUpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 15/10/2026 01:04 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `096c4303137c5f32…`
