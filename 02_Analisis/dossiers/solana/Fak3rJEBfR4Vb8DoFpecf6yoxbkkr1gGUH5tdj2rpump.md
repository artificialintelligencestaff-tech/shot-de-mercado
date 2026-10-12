# MarsX (MarsX) — dossier

🎴 Memecoin en Solana (lanzada en pump.fun, migrada a pumpswap) · precio $0,0004249 · liquidez $62.875 · mcap $417.161 (al detectar)  
Detectado el 12/10/2026 18:38 UTC por: MCap > $100K, Volumen masivo, Buy pressure >55% (score 88, scorer 7.2.1+early-0.2)  
Cómo adquirirlo: Phantom → Jupiter · slippage 5%  
Ventana de la señal: hasta el 14/10/2026 18:38 UTC (< 48 h) · vigente: quedan 47,6 h  
Material educativo y documentación del método. No es asesoría financiera.  

---

## 🛒 1. Cómo adquirir MarsX

Estudio de cómo se adquiere MarsX, con los datos de su par.

**Ruta en Solana:** Phantom (https://phantom.app) o Solflare (https://solflare.com) → fondear con SOL o USDC → Jupiter (https://jup.ag) · alternativas: Raydium (https://raydium.io), Orca (https://www.orca.so)

La liquidez principal está en **pumpswap**; un agregador como Jupiter enruta la orden hacia ese pool.

Ruta por exchange centralizado: no cotiza en Binance ni en Coinbase (consulta 12/10/2026 19:05 UTC; CoinGecko sin ficha para este contrato).

### 1.1 Estudio de liquidez del par

| Momento | Pool principal | Liquidez (L) | Slippage sugerido | Impacto $100 | Impacto $1.000 | Impacto $10.000 | Orden con prima 1% | Orden con prima 3% |
|---|---|---|---|---|---|---|---|---|
| al detectar · 12/10/2026 18:38 UTC | pumpswap `9dsiuyd…PXuA` | $62.875 | 5% | 0,318% | 3,181% | 31,809% | $314 | $943 |
| consulta 12/10/2026 19:05 UTC | pumpswap `9dsiuyd…PXuA` | $52.977 | 5% | 0,378% | 3,775% | 37,753% | $265 | $795 |

Modelo: pool de producto constante sin comisiones, con la mitad de L del lado cotizado. La prima del precio promedio de ejecución sobre el spot es **2Δ/L**; el tamaño con prima x es **Δ = x·L/2**. Un agregador puede repartir la orden entre pools. Sin L conocida (bonding curve), el monto exacto lo muestra el DEX. Slippage por tramo de L [H, doc 24 §1.2].

### 1.2 Pasos

1. Instalar la wallet: Phantom (https://phantom.app) o Solflare (https://solflare.com)
2. Fondearla con SOL o USDC, comprados en Binance, Coinbase o Kraken y enviados a la dirección de la wallet. Dejar un resto de SOL para las comisiones de red
3. Conectar la wallet a Jupiter (https://jup.ag); la liquidez principal está en pumpswap
4. Pegar el mint y verificar que coincide carácter por carácter: `Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump`
5. Configurar el slippage: 5% (liquidez $52.977, consulta 12/10/2026 19:05 UTC)
6. Verificar el contrato en Solscan (https://solscan.io/token/Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump) y el par en DexScreener (https://dexscreener.com/solana/9dsiuydk5EFRCLk6VEywY95Nn3jjGbdWNijuACf1PXuA); mint authority / freeze authority: revocada / revocada · holders 9.571 · top-10 53,94% (consulta 12/10/2026 19:05 UTC)
7. Ejecutar el swap
8. Confirmar la transacción en Solscan. Si el token no aparece en la wallet, agregarlo pegando el mint

### 1.3 Verificación previa

- Contrato en Solscan: https://solscan.io/token/Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump
- Par en DexScreener: https://dexscreener.com/solana/9dsiuydk5EFRCLk6VEywY95Nn3jjGbdWNijuACf1PXuA
- Página del lanzamiento (pump.fun): https://pump.fun/coin/Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump
- Datos para comparar: mint authority / freeze authority: revocada / revocada · holders 9.571 · top-10 53,94% (consulta 12/10/2026 19:05 UTC)
- [P] enlaces de swap con el par precargado: pendientes de verificación manual de Dirección (doc 24 §1.5); hasta entonces, sitio oficial + mint para pegar

---

## 📊 2. Identificación del activo

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | MarsX / MarsX | registro de la detección (pumpportal) |
| Mint / contrato | `Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump` | registro de la detección |
| Chain / DEX / par | Solana / pumpswap / `9dsiuydk5EFRCLk6VEywY95Nn3jjGbdWNijuACf1PXuA` | DexScreener, al detectar (15 par(es) en la consulta 12/10/2026 19:05 UTC) |
| Deployer | `866SrsMfwKsErATZDCLAPbxH3NuqjKn7zQ1xXMqixoz1` | PumpPortal (evento create), al detectar |
| Par creado | 12/10/2026 17:38 UTC | DexScreener `pairCreatedAt` |
| Edad del par al detectar / al alertar / ahora | 60,3 min / 60,3 min / 87,2 min | cálculo con `pairCreatedAt` |
| Mint / freeze authority | revocada / revocada | RugCheck y GoPlus, consulta 12/10/2026 19:05 UTC |
| Holders / top-10 | 9.571 / 53,94% | RugCheck `totalHolders` y suma de `topHolders[:10].pct`, consulta 12/10/2026 19:05 UTC |
| Holders efectivos del top-10 | 4,4 | (Σp)² / Σp² sobre el top-10 de RugCheck: 10 = los diez con el mismo peso; 1 = uno concentra todo |
| Liquidez bloqueada | pump_fun_amm 100%; meteoraDlmm 0%; orca 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0%; meteora_damm_v2 0% | RugCheck `markets[].lp.lpLockedPct`, consulta 12/10/2026 19:05 UTC |
| Etiquetas de RugCheck | ninguna | RugCheck `risks[].name` (texto de la fuente), consulta 12/10/2026 19:05 UTC |
| Links | DexScreener: https://dexscreener.com/solana/9dsiuydk5EFRCLk6VEywY95Nn3jjGbdWNijuACf1PXuA · Solscan: https://solscan.io/token/Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump · pump.fun: https://pump.fun/coin/Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump · web: https://usepaid.app/token/Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump · twitter: https://x.com/imBilngineer/status/2109707804353446006?s=20 | consulta 12/10/2026 19:05 UTC |

---

## 🧬 3. Naturaleza del activo

- **Tipo:** Memecoin (grupo a: memecoins micro-cap, doc 23) · origen: lanzada en pump.fun, migrada a pumpswap
- **Categoría / narrativa:** n/d (CoinGecko sin ficha para este contrato; sin narrativa en el registro curado)
- **Qué promete / qué representa:** sin descripción publicada (RugCheck `fileMeta.description` (metadata del token), consulta 12/10/2026 19:05 UTC)
- **Historia:**
  - Par creado el 12/10/2026 17:38 UTC (DexScreener `pairCreatedAt`).
  - Detectado el 12/10/2026 18:38 UTC, con el par a 60,3 min de creado: precio $0,0004249, mcap $417.161, liquidez $62.875.
  - Velas de 1 h de GeckoTerminal (3, desde 12/10/2026 17:00 UTC): apertura $0,00003491 · máximo $0,0007604 (12/10/2026 18:00 UTC) · mínimo $0,00003359 (12/10/2026 17:00 UTC) · último cierre $0,0003017.
  - En la consulta 12/10/2026 19:05 UTC: precio $0,0003058, liquidez $52.977, FDV $300.257.

---

## 🔬 4. Método científico aplicado

**Score:** suma de componentes de `script_82.score_token`, recortada a 0–100. Registrado con el scorer **7.2.1+early-0.2**; vigente: **7.2.1**. Tabla de componentes: Anexo C del doc 24.

**Datos de entrada** (DexScreener vía script_82, al detectar: 12/10/2026 18:38 UTC):

| Dato | Valor |
|---|---|
| Precio | $0,0004249 |
| Liquidez | $62.875 |
| MCap | $417.161 |
| Volumen 24 h | $1.153.131 |
| Cambio 24 h | +877% |
| Cambio m5 / h1 | -3,0% / +664,0% |
| Volumen m5 / h1 | $21.656 / $1.138.115 |
| Trades m5 (compras / ventas) | 289 / 229 |
| Edad del par | 60,3 min |
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
| MCap | ≥ $100K | $417.161 | +15 |
| Volumen 24 h | ≥ $1M | $1.153.131 | +20 |
| Buy pressure m5 | > 55% (par maduro) | 56% | +15 |
| Edge temprano | edad < 4 h (par maduro) | edad 60,3 min | +8 |
| Volumen m5 | > $1K (par maduro) | $21.656 | +10 |
| Liquidez | ≥ $50K | $62.875 | +10 |
| Cambio 24 h | ≥ +50% | +877% | +10 |
| Sobrecompra | cambio 24 h > 500% con liq/mcap ≥ 3% | +877% · liq/mcap 15,1% | +0 |
| **Total** | recortado a 0–100 |  | **88** |

**Recalculado con el scorer vigente 7.2.1** sobre los mismos datos (reloj fijado en 2026-10-12T18:38:57+00:00, sin estado previo): **88** · motivos: MCap > $100K, Volumen masivo, Buy pressure >55%, Edge temprano (<4h), Volumen activo m5 (>$1K), Liquidez decente, Pump 24h, SOBRECOMPRA MEDIA (>500%) + liq/mcap=15.1% >=3% (sin penalización).

**Población** (scorer 7.2.1, 02_Analisis/shadow_v4/_accumulated.json): 50 de 31.764 tokens analizados (0,16%) quedan ≥ 56. Con score 88, este activo queda en el percentil 99,9 de esa población.
**Baseline de la primaria:** 10,5% (tasa de la población sin filtro, doc 22 §1.1).

---

## ⏱️ 6. Vigencia estimada

- **Ventana operativa:** < 48 h desde 12/10/2026 18:38 UTC, hasta 14/10/2026 18:38 UTC · vigente: quedan 47,6 h.
- **Aceleración al detectar:** cambio m5 -3,0% · h1 +664,0% · h24 +877% · volumen m5/h1 0,02 · edad del par 60,3 min.
- **Precio de entrada** (alerta): $0,0004249.
- **Consulta 12/10/2026 19:05 UTC:** $0,0003058 (-28,0% vs la entrada).
- **Métrica dual de este activo:** n/d (sin consulta de velas).
- **Duración histórica de eventos similares** (aciertos primarios del legado v7.1, n = 38 de 75 con velas, medianas): máximo +113% · mínimo posterior -99,6% · último precio a 48 h -99,5%.

---

## 📚 7. Fuentes verificables

- **Registro de la detección:** `02_Analisis/alerts/alert_Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump_2026-10-12_183857.json` · blob `83ad751572d17897106278fed450ec2767377b38` · commit `9ba3031` (2026-10-12T18:58:55Z)
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-10-12_183857`, status `active_tracking`.
- **Consultas:**
  - DexScreener (vía script_82): https://api.dexscreener.com/latest/dex/tokens/Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump · registro · 12/10/2026 18:38 UTC
  - DexScreener: https://api.dexscreener.com/latest/dex/tokens/Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump · HTTP 200 · 12/10/2026 19:05 UTC
  - RugCheck: https://api.rugcheck.xyz/v1/tokens/Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump/report · HTTP 200 · 12/10/2026 19:05 UTC
  - GoPlus: https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump · HTTP 200 · 12/10/2026 19:05 UTC
  - GeckoTerminal (velas 1 h): https://api.geckoterminal.com/api/v2/networks/solana/pools/9dsiuydk5EFRCLk6VEywY95Nn3jjGbdWNijuACf1PXuA/ohlcv/hour?limit=1000 · HTTP 200 · 12/10/2026 19:05 UTC
  - CoinGecko (ficha por contrato): https://api.coingecko.com/api/v3/coins/solana/contract/Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump · HTTP 404 · 12/10/2026 19:05 UTC
  - Binance (data-api): https://data-api.binance.vision/api/v3/exchangeInfo?symbol=MARSXUSDT · HTTP 400 · 12/10/2026 19:05 UTC
  - Coinbase (API pública): https://api.exchange.coinbase.com/products/MARSX-USD · HTTP 404 · 12/10/2026 19:05 UTC
- **Consistencia entre fuentes** (diferencia relativa):
  - Liquidez DexScreener vs RugCheck: $52.977 vs $78.594 → 32,59%
  - Precio DexScreener vs último cierre 1 h de GeckoTerminal: $0,0003058 vs $0,0003017 → 1,33%
- **Auditar el score** (desde la raíz del repo; reloj fijado en el momento de la detección):

  ```bash
  python -c "import json,importlib.util as u;from unittest import mock;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump_2026-10-12_183857.json',encoding='utf-8'));d=d.get('Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump',d);p=mock.patch('time.time',return_value=1791830337);p.start();print(m.SCORING_VERSION,m.score_token(d['token'],d.get('dexscreener')))"
  ```

- **Regenerar este dossier:** `python 04_Config/scripts/script_113_dossier_builder.py --mint Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump --chain solana --stdout`
- **Métrica dual de todas las alertas en sombra:** `python 04_Config/scripts/monitor_shadow.py`
- **Dossier:** versión 1.0 · armado 12/10/2026 19:05 UTC · modo live · huella de los datos de entrada (SHA-256 de `inputs` del .json): `2ada712120916cdd…`
