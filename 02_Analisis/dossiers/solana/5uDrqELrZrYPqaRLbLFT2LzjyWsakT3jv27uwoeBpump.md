# Claude Buddies (BUDDIES) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,00001052 · liquidez $7.462 · mcap $10.524 (al detectar)  
Detectado el 17/10/2026 11:49 UTC por: young-0.4 · edad 10.9 min · pesos info 60 / estructura 20 / precio 20 · info 23.1 · estructura 12.8 · precio/volumen 8.4 · cobertura 93/100, [info] narrative_wave: ola 'claude': 11 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3 (score 44, scorer young-0.4)  
Cómo adquirirlo: Phantom → Jupiter · slippage 10%  
Ventana de la señal: hasta el 19/10/2026 11:49 UTC (< 48 h) · vigente: quedan 47,5 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir BUDDIES

Estudio de cómo se adquiere BUDDIES, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 17/10/2026 12:20 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 17/10/2026 11:49 UTC | pumpswap `DQKg9TA…Cb5b` | $7.462 | 10% | 2,680% | 26,804% | 268,043% | $37 | $112 |
| consulta 17/10/2026 12:20 UTC | pumpswap `DQKg9TA…Cb5b` | $2.819 | 10% | 7,095% | 70,952% | 709,517% | $14 | $42 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump`
5. Configurar el slippage: 10% (liquidez $2.819, consulta 17/10/2026 12:20 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump) y el par en DexScreener (https://dexscreener.com/solana/DQKg9TAKNxkdeBc3iYb4t8bUJvwFumj5cJUxy7PYCb5b); mint authority / freeze authority: revocada / revocada · holders 1.450 · top-10 94,24% (consulta 17/10/2026 12:20 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump
- Par en DexScreener: https://dexscreener.com/solana/DQKg9TAKNxkdeBc3iYb4t8bUJvwFumj5cJUxy7PYCb5b
- Página del lanzamiento (pump.fun): https://pump.fun/coin/5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 1.450 · top-10 94,24% (consulta 17/10/2026 12:20 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | Claude Buddies / BUDDIES | registro de la detección (pumpportal_live) |
| Mint / contrato | `5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `DQKg9TAKNxkdeBc3iYb4t8bUJvwFumj5cJUxy7PYCb5b` | DexScreener, al detectar (5 par(es) en la consulta 17/10/2026 12:20 UTC) |
| Deployer | `46zGJ2ATgfXdiUXGJE3qZrWs9jerrmvgAodAKY79haGU` | PumpPortal (evento create), al detectar |
| Par creado | 17/10/2026 11:38 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 10,9 min / 10,9 min / 41,5 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 17/10/2026 12:20 UTC |
| Holders / top-10 | 1.450 / 94,24% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 17/10/2026 12:20 UTC |
| Holders efectivos del top-10 | 1,3 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 17/10/2026 12:20 UTC |
| Etiquetas de RugCheck | «Low Liquidity» | RugCheck `risks[].name` (texto de la fuente), consulta 17/10/2026 12:20 UTC |
| Links | DexScreener: https://dexscreener.com/solana/DQKg9TAKNxkdeBc3iYb4t8bUJvwFumj5cJUxy7PYCb5b · Solscan: https://solscan.io/token/5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump · pump.fun: https://pump.fun/coin/5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump · web: https://otcdesks.cash/coin/5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump · twitter: https://twitter.com/0xDutty/status/2111420191297147348 | consulta 17/10/2026 12:20 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 17/10/2026 12:20 UTC)
- **Historia:**
  - Par creado el 17/10/2026 11:38 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 17/10/2026 11:49 UTC, con el par a 10,9 min de creado: precio $0,00001052, mcap $10.524, liquidez $7.462.
  - Velas de 1 h de GeckoTerminal (2, desde 17/10/2026 11:00 UTC): apertura $0,00004099 · máximo $0,00006330 (17/10/2026 11:00 UTC) · mínimo $0,000002897 (17/10/2026 12:00 UTC) · último cierre $0,000002897.
  - En la consulta 17/10/2026 12:20 UTC: precio $0,000002895, liquidez $2.819, FDV $2.779.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **young-0.4**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 17/10/2026 11:49 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,00001052 |
| Liquidez | $7.462 |
| MCap | $10.524 |
| Volumen 24 h | $151.687 |
| Cambio 24 h | -76% |
| Cambio m5 / h1 | -81,8% / -75,9% |
| Volumen m5 / h1 | $58.153 / $151.687 |
| Trades m5 (compras / ventas) | 886 / 930 |
| Edad del par | 10,9 min |
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

Desglose no reproducible desde los motivos registrados (suma 0 vs score 44; motivos sin regla: young-0.4 · edad 10.9 min · pesos info 60 / estructura 20 / precio 20 · info 23.1 · estructura 12.8 · precio/volumen 8.4 · cobertura 93/100, [info] narrative_wave: ola 'claude': 11 lanzamientos más en 1 h → +14.9, [info] metadata_socials: enlaces ['twitter', 'website'] · descripción 0 caracteres → +5.3, [info] dex_profile: perfil pago en DexScreener → +3.0, [estructura] bonding_progress: graduado (pumpswap) → +9.7, [estructura] holders_struct: holders 1571 · top-10 39.5 % → +2.4, [estructura] dev_wallet: creador compró 9.8 % del supply → +0.1, [estructura] holder_to_txn_ratio: holders/txns 1571/4410 = 0.36 → +0.6, [precio/volumen] volume_acceleration: vol 5 min ×4.6 la tasa horaria (s 1.00), [precio/volumen] holder_accumulation: holders 1179→1571 (+65.3/min) · top10 36.7%→39.5% (s 1.00), [flag, no suma] tradable=True, liquidity_usd=7461.5, buy_route=pumpswap (AMM) vía Jupiter o el DEX, initial_liquidity_usd=0.0, score 44 (umbral 40, info mínima 5) → EMITE): no se publica.

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-17T11:49:42+00:00, sin estado previo): **10** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap bajo, Volumen alto, Liquidez baja, Dump 24h.

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 62 de 38.247 tokens analizados (0,16%) quedan ≥ 56. Con score 10, este activo queda en el percentil 93,6 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 17/10/2026 11:49 UTC, hasta 19/10/2026 11:49 UTC · vigente: quedan 47,5 h.
- **Aceleración al detectar:** cambio m5 -81,8% · h1 -75,9% · h24 -76% · volumen m5/h1 0,38 · edad del par 10,9 min.
- **Precio de entrada** (alerta): $0,00001052.
- **Consulta 17/10/2026 12:20 UTC:** $0,000002895 (-72,5% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump_2026-10-17_114942.json` · blob `dfe88904a079fd6c19311aeaba1f15ab8217a73d` · commit `a6d644d` (2026-10-17T12:08:19Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-17_114942`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump · registro · 17/10/2026 11:49 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump · HTTP 200 · 17/10/2026 12:20 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump/report · HTTP 200 · 17/10/2026 12:20 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump · HTTP 200 · 17/10/2026 12:20 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/DQKg9TAKNxkdeBc3iYb4t8bUJvwFumj5cJUxy7PYCb5b/ohlcv/hour?limit=1000 · HTTP 200 · 17/10/2026 12:20 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump · HTTP 404 · 17/10/2026 12:20 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BUDDIESUSDT · HTTP 400 · 17/10/2026 12:20 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/BUDDIES-USD · HTTP 404 · 17/10/2026 12:20 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $2.819 vs $2.821 → 0,07%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,000002895 vs $0,000002897 → 0,07%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump_2026-10-17_114942.json',encoding='utf-8'));d=d.get('5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump',d);p=mock.patch('time.time',return_value=1792237782);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint 5uDrqELrZrYPqaRLbLFT2LzjyWsakT3jv27uwoeBpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 17/10/2026 12:20 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `8712b89bfdb6570b…`
