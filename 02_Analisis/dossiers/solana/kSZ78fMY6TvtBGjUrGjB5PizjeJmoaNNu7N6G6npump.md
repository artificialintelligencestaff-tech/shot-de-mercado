# USOR/SOL (USOR/SOL) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,008100 · liquidez $258.274 · mcap $8.100.464 (al detectar)  
Detectado el 02/10/2026 00:28 UTC por: MCap > $1M, Volumen alto, Liquidez alta (score 65, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 3%  
Ventana de la señal: hasta el 04/10/2026 00:28 UTC (< 48 h) · vigente: quedan 47,7 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir USOR/SOL

Estudio de cómo se adquiere USOR/SOL, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 02/10/2026 00:44 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 02/10/2026 00:28 UTC | pumpswap `FZTe3Nw…jZRn` | $258.274 | 3% | 0,077% | 0,774% | 7,744% | $1.291 | $3.874 |
| consulta 02/10/2026 00:44 UTC | pumpswap `FZTe3Nw…jZRn` | $258.133 | 3% | 0,077% | 0,775% | 7,748% | $1.291 | $3.872 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump`
5. Configurar el slippage: 3% (liquidez $258.133, consulta 02/10/2026 00:44 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump) y el par en DexScreener (https://dexscreener.com/solana/FZTe3NwPDRcpsAB4xJYyCQmFP2sDEQPoozDc7CeXjZRn); mint authority / freeze authority: revocada / revocada · holders 2.020 · top-10 4,36% (consulta 02/10/2026 00:44 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump
- Par en DexScreener: https://dexscreener.com/solana/FZTe3NwPDRcpsAB4xJYyCQmFP2sDEQPoozDc7CeXjZRn
- Página del lanzamiento (pump.fun): https://pump.fun/coin/kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 2.020 · top-10 4,36% (consulta 02/10/2026 00:44 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | USOR/SOL / USOR/SOL | registro de la detección (pumpportal_live) |
| Mint / contrato | `kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `FZTe3NwPDRcpsAB4xJYyCQmFP2sDEQPoozDc7CeXjZRn` | DexScreener, al detectar (2 par(es) en la consulta 02/10/2026 00:44 UTC) |
| Deployer | `4ousZAywjQYGtNjCtd8boMCEskXuhiQ3wubAjc6FtFzh` | PumpPortal (evento create), al detectar |
| Par creado | 02/10/2026 00:17 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 11,0 min / 11,0 min / 27,2 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 02/10/2026 00:44 UTC |
| Holders / top-10 | 2.020 / 4,36% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 02/10/2026 00:44 UTC |
| Holders efectivos del top-10 | 4,5 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100% | RugCheck `markets[].lp.lpLockedPct`, consulta 02/10/2026 00:44 UTC |
| Etiquetas de RugCheck | «High holder correlation» | RugCheck `risks[].name` (texto de la fuente), consulta 02/10/2026 00:44 UTC |
| Links | DexScreener: https://dexscreener.com/solana/FZTe3NwPDRcpsAB4xJYyCQmFP2sDEQPoozDc7CeXjZRn · Solscan: https://solscan.io/token/kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump · pump.fun: https://pump.fun/coin/kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump · web / Telegram / X: no publicados en DexScreener | consulta 02/10/2026 00:44 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 02/10/2026 00:44 UTC)
- **Historia:**
  - Par creado el 02/10/2026 00:17 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 02/10/2026 00:28 UTC, con el par a 11,0 min de creado: precio $0,008100, mcap $8.100.464, liquidez $258.274.
  - Velas de 1 h de GeckoTerminal (1, desde 02/10/2026 00:00 UTC): apertura $0,00004922 · máximo $0,008158 (02/10/2026 00:00 UTC) · mínimo $0,00004922 (02/10/2026 00:00 UTC) · último cierre $0,008154.
  - En la consulta 02/10/2026 00:44 UTC: precio $0,008098, liquidez $258.133, FDV $8.098.118.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 02/10/2026 00:28 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,008100 |
| Liquidez | $258.274 |
| MCap | $8.100.464 |
| Volumen 24 h | $119.758 |
| Cambio 24 h | +16.340% |
| Cambio m5 / h1 | -0,0% / +16.340,0% |
| Volumen m5 / h1 | $724 / $119.758 |
| Trades m5 (compras / ventas) | 420 / 12 |
| Edad del par | 11,0 min |
| Score del feed (WS) | n/d (feed sin score) |

**Probabilidades** (definiciones del doc 19; IC90 de Wilson):

- Scorer 7.2.1: **en validación** (veredicto con n ≥ 20 primarias resueltas). En sombra hasta ahora: primaria 1/1 (100,0%, IC90 27,0%–100,0%) · secundaria 0/0 resueltas (shadow_monitor.json).

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

Desglose reconstruido desde los motivos registrados; suma 65 = score registrado 65 [V].

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | score WS × 0,3 | WS 0 × 0,3 | +0 |
| Gate de edad v7.2.1 | edad < 60 min o desconocida: sin bonos temporales | edad 11,0 min | +0 |
| MCap | ≥ $1M | $8.100.464 | +25 |
| Volumen 24 h | ≥ $100K | $119.758 | +15 |
| Liquidez | ≥ $100K | $258.274 | +15 |
| Cambio 24 h | ≥ +50% | +16.340% | +10 |
| Sobrecompra | cambio 24 h > 5.000% con liq/mcap ≥ 3% | +16.340% · liq/mcap 3,2% | +0 |
| **Total** | recortado a 0–100 |  | **65** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-02T00:28:26+00:00, sin estado previo): **65** · motivos: v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta), MCap > $1M, Volumen alto, Liquidez alta, Pump 24h, SOBRECOMPRA ALTA (>5,000%) + liq/mcap=3.2% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 6 de 6.334 tokens analizados (0,09%) quedan ≥ 56. Con score 65, este activo queda en el percentil 100,0 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 02/10/2026 00:28 UTC, hasta 04/10/2026 00:28 UTC · vigente: quedan 47,7 h.
- **Aceleración al detectar:** cambio m5 -0,0% · h1 +16.340,0% · h24 +16.340% · volumen m5/h1 0,01 · edad del par 11,0 min.
- **Precio de entrada** (alerta): $0,008100.
- **Consulta 02/10/2026 00:44 UTC:** $0,008098 (-0,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump_2026-10-02_002826.json` · blob `4831461a8cddd8e877d79588806bbd0a2891ea4a` · commit `ef4e54a` (2026-10-02T00:38:02Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-02_002826`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump · registro · 02/10/2026 00:28 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump · HTTP 200 · 02/10/2026 00:44 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump/report · HTTP 200 · 02/10/2026 00:44 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump · HTTP 200 · 02/10/2026 00:44 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/FZTe3NwPDRcpsAB4xJYyCQmFP2sDEQPoozDc7CeXjZRn/ohlcv/hour?limit=1000 · HTTP 200 · 02/10/2026 00:44 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump · HTTP 404 · 02/10/2026 00:44 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $258.133 vs $259.309 → 0,45%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,008098 vs $0,008154 → 0,69%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump_2026-10-02_002826.json',encoding='utf-8'));d=d.get('kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump',d);p=mock.patch('time.time',return_value=1790900906);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint kSZ78fMY6TvtBGjUrGjB5PizjeJmoaNNu7N6G6npump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 02/10/2026 00:44 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `4b739dfcb4ee83f4…`
