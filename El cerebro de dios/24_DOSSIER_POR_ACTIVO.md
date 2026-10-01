---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: DISEÑO (no implementado)
last_updated: 2026-10-01
version: 1.0
---

# 24 — Dossier por activo (diseño) + integración multi-chain

Rótulos: [V] verificado (archivo del repo, cálculo reproducido o consulta HTTP en esta sesión) · [I] inferido · [H] hipótesis · [P] pendiente.

---

## 1. Propósito

Que cada alerta llegue con un documento que permita entender qué es el activo, por qué el sistema lo detectó, con qué datos y cálculos, durante cuánto tiempo aplica la señal, cómo se adquiere y cómo auditar cada número: **material educativo y documentación científica, no asesoría financiera.** El dossier informa; no juzga, no advierte, no recomienda. El lector decide.

**Formato de entrega**
- Archivo Markdown, uno por alerta: `02_Analisis/dossiers/dossier_<SYMBOL>_<mint8>_<YYYY-mm-dd_HHMMSS>.md`.
- Va adjunto al mensaje de la alerta con `sendDocument` al grupo (`TELEGRAM_PUBLIC_CHAT_ID`), con un caption de ≤ 1024 caracteres: nombre, score, ventana y un link.
- Lo desconocido se escribe `n/d` con la fuente que lo resolvería. **Nunca** se rellena con valores por defecto, la misma regla que el template de alertas.
- Cada dato lleva su **fuente** y su **momento**: "al detectar" (archivo de detección) o "consulta del <fecha>" (dato actual).

---

## 2. Estructura del dossier (7 secciones)

### Sección 1 — Identificación del activo

| Campo | Fuente (gratuita, sin key) | Estado hoy |
|---|---|---|
| Nombre, symbol, mint/contrato | `token` del detector (PumpPortal / trending) · DexScreener `baseToken` | [V] en el archivo de detección |
| Chain | pipeline (`solana`) · DexScreener `chainId` · `token.chain` (multi-chain) | [V] |
| DEX principal y par principal | DexScreener `dexId`, `pairAddress` (par de mayor liquidez, igual que script_82) | [V] |
| Deployer (wallet) | `token.traderPublicKey` (PumpPortal create) · RugCheck `creator` | [V] / [V] consulta |
| Fecha de creación del par, edad al detectar y edad actual | DexScreener `pairCreatedAt` (ms) vs `detected_at` | [V] (`pairCreatedAt` se guarda desde v7.2) |
| Auditoría on-chain: mint / freeze authority | GoPlus Solana `mintable` / `freezable` · RugCheck `mintAuthority` / `freezeAuthority` · (EVM: GoPlus `is_mintable`, `owner_address`, Honeypot.is) | [P] no se guarda: consulta al armar el dossier |
| Holders y concentración top-10 | RugCheck `totalHolders`, `topHolders[].pct` (suma de los 10 primeros), `insider` | [P] ídem |
| Liquidez bloqueada | RugCheck `markets[].lp.lpLockedPct` (cruzar con el resumen: pueden diferir, ver §4) | [P] ídem |
| Links | DexScreener (par), explorador (Solscan / Etherscan / BaseScan / BlastScan), página del launchpad (pump.fun), web / Telegram / X desde DexScreener `info.websites` / `info.socials` o la metadata del token (`token.uri`) | [V] los de DexScreener y explorador |

### Sección 2 — Naturaleza del activo

| Campo | Cómo se obtiene |
|---|---|
| ¿Qué es? (memecoin, DeFi, L1, L2, RWA, DePIN, sintético) | Pipeline Solana pump.fun → memecoin (por origen del lanzamiento). Multi-chain → grupo `a..h` del doc 23 + categorías de CoinGecko (`coins/{id}` → `categories`). |
| ¿A qué pertenece? (categoría, narrativa) | Categorías de CoinGecko; para memes, la capa narrativa (`lib_narrative`, Cap. VII). La capa temática hoy vale 0: se informa la etiqueta, no se puntúa. |
| ¿Qué promete? / ¿Qué representa? | Descripción oficial citada **textual y atribuida**: `description` de la metadata del token o la web oficial. Si no existe: "sin descripción publicada". |
| Historia breve | Creación del par, migración (bonding curve de pump.fun → AMM), máximo y mínimo desde el lanzamiento (OHLCV de GeckoTerminal). |

### Sección 3 — Método científico aplicado

1. **Fórmula del score (scorer vigente v7.2.1, `script_82.score_token`)**: suma de componentes, recortada a 0–100. Ver tabla completa en el Anexo C.
2. **Datos de entrada**: precio, liquidez, mcap, volumen 24 h, m5 / h1 (volumen, trades, compras/ventas, cambio de precio), edad del par y score del feed (WS / trending). Cada uno con su valor y su fuente.
3. **Probabilidades** (definiciones del doc 19):
   - **Primaria**: tocar +20% antes de caer −30% desde la entrada, dentro de 48 h (velas OHLC en orden conservador open → low → high → close).
   - **Secundaria**: cierre ≥ +20% a las 48 h.
   - **Post +20%**: fracción de los que tocaron +20% y después llegaron a ≤ −99% dentro de las 48 h. Es una métrica, no una advertencia (doc 21).
   - Se publican con **IC90 de Wilson**. Mientras `emission_calibration.json` no tenga `validated: true`, el dossier muestra "en validación" y la cifra histórica rotulada con su versión y su n.
4. **Fórmula del IC90 (Wilson)**, con z = 1,645:
   `p̂ = k/n`
   `centro = (p̂ + z²/(2n)) / (1 + z²/n)`
   `radio = z·√(p̂(1−p̂)/n + z²/(4n²)) / (1 + z²/n)`
   `IC90 = [centro − radio, centro + radio]`
5. **Cómo auditarlo**: el dossier trae
   - el archivo de detección (ruta + blob git + commit);
   - la versión del scorer;
   - el comando que recalcula el score con el código del repo (ejemplo en §4.7).

   Con el mismo archivo y la misma versión, el resultado tiene que ser idéntico.

### Sección 4 — Fundamento de la detección

- **Score final con desglose**: cada componente con su condición, el valor observado y los puntos (+/−). Hoy `script_82` guarda los motivos (`reasons`), no los puntos. El desglose se reconstruye con la tabla del Anexo C.
  - [P] Agregar `score_breakdown` en `script_82` para no depender de la reconstrucción.
- **Señales activadas** con sus valores numéricos. Ejemplo: "MCap $172.160.515 ≥ $1M → +25".
- **Comparación con el baseline poblacional**:
  - qué fracción de los tokens analizados en la misma ventana superó el umbral (v7.2.1: 1,4% de los tokens ≥ 56, doc 20);
  - baseline de la primaria: 10,5% (doc 22 §1.1);
  - cifras históricas por tramo de score (doc 19 y doc 21).

### Sección 5 — Vigencia estimada de la señal

- **Ventana operativa: < 48 h** desde la detección (horizonte de la métrica dual).
- **Velocidad de la aceleración detectada**:
  - cambio de precio m5 / h1 / h24;
  - cociente de volumen m5/h1 y de trades m5/h1 (las "derivadas" de `script_82`);
  - edad del par al detectar.
- **Duración histórica de eventos similares**: lo que se mide hoy son los extremos y el cierre a 48 h de los aciertos primarios. Muestra legado v7.1, n = 38 aciertos sobre 75 tokens con datos [V]:

  | Medida | Mediana |
  |---|---|
  | Máximo | +113% |
  | Mínimo posterior | −99,6% |
  | Último precio a 48 h | −99,5% |

  [P] **Tiempo hasta el +20%** y **tiempo desde el +20% hasta el mínimo**: no se guardan. Se calculan con las mismas velas de `calibrate_threshold_v72.CandleSource` (primer índice de vela con `high ≥ 1,2·entrada`; primer índice posterior con `low ≤ 0,01·entrada`) y se publican como mediana con IQR.

### Sección 6 — Cómo adquirir el activo (paso a paso)

| Chain | Wallet | Swap | Verificación del contrato |
|---|---|---|---|
| Solana | Phantom (phantom.app) o Solflare (solflare.com) | Jupiter (jup.ag): pegar el mint | Solscan (`solscan.io/token/<mint>`) + par en DexScreener |
| Ethereum / Base / Blast | MetaMask o Rabby | Uniswap (app.uniswap.org) o 1inch (1inch.io): pegar el contrato | Etherscan / BaseScan / BlastScan + par en DexScreener |
| Monad | MetaMask o Rabby (red Monad) | [P] verificar qué agregador soporta Monad antes de publicarlo | [P] explorador de Monad a verificar |

Pasos:
1. Instalar la wallet de la chain.
2. Fondearla con el activo nativo (SOL / ETH / MON) desde un exchange.
3. Abrir el swap y pegar el mint/contrato. Verificar que coincide **carácter por carácter** con el del dossier y con el explorador.
4. Slippage 5–10% (memecoins de baja liquidez); 0,5–1% en activos líquidos.
5. Ejecutar el swap y verificar la transacción en el explorador.

### Sección 7 — Fuentes verificables y trazabilidad

- Lista de todas las URLs consultadas, con el momento de cada consulta.
- Timestamp de la detección (`detected_at`) y de la alerta.
- Archivo de detección: ruta en el repo + **blob git** (`git hash-object`) + commit.
- Versión del scorer y del template (`scoring_version`, versión del dossier).
- Cómo auditar: comandos para recalcular el score y para medir la métrica dual del activo (§4.7).

---

## 3. Template vacío

```markdown
# Dossier — {{NOMBRE}} ({{SYMBOL}})
Dossier v1 · generado {{GENERADO_UTC}} · alerta {{ALERTA_UTC}} · scorer v{{SCORING_VERSION}}
Material educativo y documentación del método. No es asesoría financiera.

## 1. Identificación
| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | {{NOMBRE}} / {{SYMBOL}} | {{FUENTE}} |
| Mint / contrato | `{{MINT}}` | {{FUENTE}} |
| Chain | {{CHAIN}} | {{FUENTE}} |
| DEX / par principal | {{DEX}} / `{{PAIR}}` | DexScreener, al detectar |
| Deployer | `{{DEPLOYER}}` | {{FUENTE}} |
| Par creado | {{PAR_CREADO_UTC}} | DexScreener pairCreatedAt |
| Edad al detectar / actual | {{EDAD_DETECCION}} / {{EDAD_ACTUAL}} | cálculo |
| Mint authority / freeze authority | {{MINT_AUTH}} / {{FREEZE_AUTH}} | GoPlus / RugCheck, consulta {{FECHA}} |
| Holders / top-10 | {{HOLDERS}} / {{TOP10_PCT}} | RugCheck, consulta {{FECHA}} |
| Liquidez bloqueada | {{LP_LOCKED}} | RugCheck, consulta {{FECHA}} |
| Links | {{DEXSCREENER_URL}} · {{EXPLORER_URL}} · {{LAUNCHPAD_URL}} · {{WEB}} · {{TELEGRAM}} · {{X}} | — |

## 2. Naturaleza del activo
- Tipo: {{TIPO}} (grupo {{GRUPO}}, doc 23)
- Categoría / narrativa: {{CATEGORIAS}}
- Qué promete / qué representa: {{DESCRIPCION_OFICIAL_TEXTUAL}} — fuente: {{FUENTE_DESCRIPCION}}
- Historia: {{HISTORIA}}

## 3. Método
- Score: suma de componentes de `script_82.score_token` (v{{SCORING_VERSION}}), recortada a 0–100 (Anexo C del doc 24).
- Datos de entrada (al detectar): {{TABLA_INPUTS}}
- Primaria (tocar +20% antes de −30%, ≤48 h): {{P1}} (IC90 {{P1_IC}}, n={{P1_N}})
- Secundaria (cierre ≥ +20% a 48 h): {{P2}} (IC90 {{P2_IC}}, n={{P2_N}})
- Después de tocar +20%, llegar a ≤ −99% (≤48 h): {{P3}} (IC90 {{P3_IC}}, n={{P3_N}})

## 4. Fundamento
| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
{{FILAS_DESGLOSE}}
| **Total** | recortado a 0–100 | | **{{SCORE}}** |
- Población: {{BASELINE}}

## 5. Vigencia
- Ventana operativa: < 48 h desde {{DETECTADO_UTC}} (hasta {{VENCE_UTC}})
- Aceleración al detectar: m5 {{PC_M5}} · h1 {{PC_H1}} · h24 {{PC_H24}} · vol m5/h1 {{VOL_RATIO}} · trades m5/h1 {{TRADES_RATIO}}
- Histórico de eventos similares: {{DURACION_HISTORICA}}

## 6. Cómo adquirirlo
{{PASOS_POR_CHAIN}}

## 7. Fuentes y trazabilidad
- Detección: `{{ARCHIVO_DETECCION}}` · blob {{BLOB}} · commit {{COMMIT}}
- Fuentes: {{LISTA_URLS_CON_MOMENTO}}
- Auditar el score: {{COMANDO_RECALCULO}}
```

---

## 4. Ejemplo completo — VSOF (activo real del repo)

Datos al detectar tomados de `02_Analisis/alerts/alert_6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump_2026-09-29_171330.json`, `_all_alerts.json` y `detection_2026-09-29_170818.json`. Consultas actuales del 2026-10-01 ~00:50 UTC. Todo [V] salvo lo marcado.

> **Dossier — VSOF (VSOF)**
> Dossier v1 (ejemplo) · alerta 2026-09-29 17:13:30 UTC · scorer de ese momento: v7.2 previo a R1, sin `scoring_version` registrado.
> Material educativo y documentación del método. No es asesoría financiera.

### 4.1 Identificación

| Campo | Valor | Fuente / momento |
|---|---|---|
| Nombre / symbol | VSOF / VSOF | feed trending (ventana 1h, score WS 100), al detectar |
| Mint | `6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump` | detección |
| Chain | Solana | pipeline |
| DEX / par principal | pumpswap / `5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx` | DexScreener, al detectar (único par en la consulta del 01/10) |
| Deployer | `BYBkmcyrsF2ZADiTJyGYuYvXhuGFitLiBnCAoiBDAm56` | RugCheck `creator`, consulta 01/10 (el feed trending no trae `traderPublicKey`) |
| Par creado | 2026-09-29 17:06:53 UTC | DexScreener `pairCreatedAt` = 1790701613000 (RugCheck `detectedAt` 17:06:54) |
| Edad al detectar / al alertar | ~1,4 min (corrida 17:08:18) / ~6,6 min (alerta 17:13:30) | cálculo |
| Mint authority / freeze authority | revocadas / revocadas · metadata inmutable | GoPlus (`mintable`, `freezable`, `metadata_mutable` en status 0) y RugCheck (`mintAuthority` = `freezeAuthority` = null), consulta 01/10 |
| Holders / top-10 | 2.813 / 10,02% (cada uno de los 10 figura con 1,00%; 0 marcados como insider) | RugCheck report, consulta 01/10 |
| Liquidez bloqueada | **inconsistente entre endpoints**: `report/summary` → `lpLockedPct` 0; `report` → mercado `pump_fun_amm` con `lpLockedPct` 100 | RugCheck, consulta 01/10 |
| Riesgos que lista RugCheck | "High market cap per holder", "High holder correlation" (`score_normalised` 54) | RugCheck summary, consulta 01/10 |
| Links | https://dexscreener.com/solana/5pav7s4VP6pRkma7kMzzFhj298KXTx6WHkrpwsVfRGdx · https://solscan.io/token/6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump · https://pump.fun/coin/6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump · web / Telegram / X: **no publicados** (DexScreener `info` vacío) | consulta 01/10 |

### 4.2 Naturaleza del activo

- **Tipo:** memecoin (lanzamiento en el launchpad pump.fun, migrado a su AMM pumpswap). Grupo **a** del doc 23.
- **Categoría / narrativa:** `n/d` (sin categoría en CoinGecko verificada para este mint; capa narrativa sin etiqueta) [P].
- **Qué promete / representa:** sin descripción publicada en DexScreener. [P] Falta leer `description` de la metadata del token; no se consultó.
- **Historia:**
  - Par creado el 29/09 a las 17:06:53 UTC.
  - Detectado ~1,4 min después, ya con mcap de $172 M. El `priceChange24h` de +350.628% refleja el salto desde la bonding curve.
  - Al 01/10, liquidez de $2.120.738 y FDV de $540,2 M.

### 4.3 Método

**Datos de entrada (al detectar):**

| Dato | Valor |
|---|---|
| Precio | $0,1721 |
| Liquidez | $1.195.183,55 |
| MCap | $172.160.515 |
| Volumen 24 h | $586.622,08 |
| Cambio 24 h | +350.628% |
| Score WS (trending) | 100 |

Los campos m5/h1 y `pairCreatedAt` no existían en el registro de esa versión. Las derivadas quedan en 0 y la edad en `n/d`.

**Probabilidades:**
- **En validación** para v7.2.1.
- Histórico (legado v7.1, score ≥ 56) [V]:

  | Métrica | Valor | n |
  |---|---|---|
  | Primaria | 60,0% | 35 |
  | Secundaria | 8,6% | 35 |
  | Después de tocar +20%, llegar a ≤ −99% | 76,2% (IC90 58,5–87,9) | 21 |

  Fuentes: doc 19 §4.2 y doc 21.

### 4.4 Fundamento (desglose reproducido)

| Componente | Condición | Valor observado | Puntos |
|---|---|---|---|
| Score del feed | WS × 0,3 | 100 × 0,3 | +30 |
| MCap | ≥ $1M | $172.160.515 | +25 |
| Volumen 24 h | ≥ $100K (< $1M) | $586.622 | +15 |
| Liquidez | ≥ $100K | $1.195.184 | +15 |
| Cambio 24 h | ≥ +50% | +350.628% | +10 |
| **Total (scorer de ese momento)** | | | **95** = score registrado [V] |

- **Recalculado con el scorer vigente v7.2.1** sobre los mismos datos: **45** [V], por dos razones:
  - se suma **SOBRECOMPRA EXTREMA (> 50.000%) −50**;
  - los bonos temporales se omiten porque la edad no se conoce.

  Hoy no superaría el umbral de 56, y la edad del par (~1,4 min < 30 min) también lo excluiría.
- **Por qué importa:** el mismo dato da scores distintos según la versión. Por eso el dossier fija `scoring_version` y el archivo exacto.
- **Población:** con v7.2.1, el 1,4% de los tokens analizados queda ≥ 56 (doc 20). Baseline de la primaria: 10,5% (doc 22 §1.1).

### 4.5 Vigencia

- **Ventana operativa:** < 48 h desde las 17:13 UTC del 29/09, o sea hasta las 17:13 UTC del 01/10.
- **Seguimiento registrado** (trust loop, precio contra la entrada de $0,1721) [V]:

  | Momento | Precio | Cambio | Registro |
  |---|---|---|---|
  | t+1h | $0,1819 | +5,69% | |
  | t+6h | $0,2303 | +33,82% | |
  | t+24h | $0,4448 | +158,45% | `final_verdict` NEUTRAL |

- **Consulta del 01/10 (~31,5 h):** $0,5401 (+213,8%).
- **Métrica dual de VSOF:**
  - Primaria: [P] las fotos t+1h/6h/24h muestran que superó +20%, pero sin velas no se puede descartar una caída a −30% intermedia.
  - Secundaria: [P] se resuelve después de las 17:13 UTC del 01/10.
- **Velocidad de la aceleración:** m5 / h1 `n/d` (el registro de esa versión no los guardaba).

### 4.6 Cómo adquirirlo (Solana)

1. Instalar Phantom (phantom.app) o Solflare (solflare.com).
2. Fondear la wallet con SOL desde un exchange.
3. Abrir Jupiter (jup.ag) y pegar el mint `6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump`.
4. Verificar en Solscan y en DexScreener que el mint y el par (`5pav7s4…RGdx`, pumpswap) coinciden.
5. Slippage 5–10%.
6. Ejecutar el swap y verificar la transacción en Solscan.

### 4.7 Fuentes y trazabilidad

- **Detección:**
  - archivo `01_Datos_Crudos/final_detection/detection_2026-09-29_170818.json`;
  - blob `3eae871029a40334fee5b69efe8e4adeeea15068`;
  - commit `be8e7d3` (2026-09-29 17:13:31 UTC).
- **Alerta:** `02_Analisis/alerts/_all_alerts.json`, timestamp `2026-09-29_171330`, `status: active_tracking`, `confidence` 64.
- **Consultas (01/10):**
  - `api.dexscreener.com/latest/dex/tokens/<mint>`
  - `api.rugcheck.xyz/v1/tokens/<mint>/report` y `/report/summary`
  - `api.gopluslabs.io/api/v1/solana/token_security?contract_addresses=<mint>`
- **Auditar el score** desde la raíz del repo:

  ```bash
  python -c "import json,importlib.util as u;s=u.spec_from_file_location('s82','04_Config/scripts/script_82_final_detection.py');m=u.module_from_spec(s);s.loader.exec_module(m);d=json.load(open('02_Analisis/alerts/alert_6BfTBNYJcZW9AnxRQ7aAx4Luf2K4BpmWpR7FWTPZpump_2026-09-29_171330.json'));print(m.SCORING_VERSION, m.score_token(d['token'], d['dexscreener']))"
  ```

  Con el código de hoy devuelve `7.2.1 (45, …)` [V]. Para reproducir el 95, mismo comando con el `script_82` del commit de la detección (`git show be8e7d3:04_Config/scripts/script_82_final_detection.py > s82_be8e7d3.py`): devuelve `(95, ['WS score muy alto', 'MCap > $1M', 'Volumen alto', 'Liquidez alta', 'Pump 24h'])` [V, reproducido el 01/10].

---

## 5. Anexo A — Checklist de campos por sección

| Sección | Campo | Obligatorio | Si falta |
|---|---|---|---|
| 1 | nombre, symbol, mint, chain | sí | no se genera el dossier |
| 1 | DEX y par principal, `pairCreatedAt` | sí | `n/d` + motivo |
| 1 | deployer | sí | `n/d` (fuente: RugCheck `creator`) |
| 1 | mint / freeze authority, holders, top-10, LP bloqueada | sí | `n/d` + fuente que lo resolvería |
| 1 | explorador + DexScreener | sí | — (siempre se pueden construir con el mint) |
| 1 | web / Telegram / X | no | "no publicados" |
| 2 | tipo y grupo (doc 23) | sí | — |
| 2 | categoría / narrativa | no | `n/d` |
| 2 | descripción oficial (textual, atribuida) | no | "sin descripción publicada" |
| 2 | historia (creación, migración, extremos) | sí | parcial con lo disponible |
| 3 | versión del scorer + tabla de componentes | sí | no se genera |
| 3 | datos de entrada con valor y fuente | sí | `n/d` por campo |
| 3 | primaria / secundaria / post +20% con IC90 y n | sí | "en validación" + histórico rotulado |
| 4 | desglose por componente que suma el score registrado | sí | si no cuadra: marcar "desglose no reproducible" y no publicar |
| 4 | baseline poblacional | sí | cifra histórica rotulada |
| 5 | ventana y vencimiento | sí | — |
| 5 | derivadas m5 / h1 / h24 | sí | `n/d` |
| 5 | duración histórica | no (hoy [P]) | "no medido aún" |
| 6 | wallet, swap, slippage y verificación por chain | sí | chain sin guía verificada: [P] y no se publica la sección |
| 7 | archivo de detección + blob + commit | sí | no se genera |
| 7 | URLs consultadas con momento | sí | — |
| 7 | comando de recálculo | sí | — |

---

## 6. Anexo B — Integración multi-chain (diseño, sin implementar)

### 6.1 Estado actual

- **Ruta rápida Solana** (`pipeline_t0`, cada 20 min): `script_82` (PumpPortal + trending → score v7.2.1) → `shadow_v4/_accumulated.json` → `script_97` (emisión; en sombra).
- **Scanner multi-chain v0** (`script_114`, en main desde `3694aa8`):
  - fuentes: CoinGecko sin key para los grupos h, f, c, g, d, e y GeckoTerminal para a (solana, base, eth, blast, monad);
  - solo recolecta y marca aceleración [H] (24 h ≥ +20% o 1 h ≥ +10%);
  - no está enganchado a ningún workflow.

### 6.2 Arquitectura propuesta

```
multichain_scan.yml  (cron cada 30–60 min; concurrency propia; commitea solo sus archivos)
   script_114 → 02_Analisis/multichain/scan_latest.json (+ histórico diario comprimido)
   script_115_multichain_score.py (tentativo) → 02_Analisis/multichain/_accumulated.json
        cada candidato: universe, group (a–h), chain, address, scoring_version "mc-<grupo>-x.y", detected_at
pipeline_t0.yml (sin cambios en la ruta Solana)
   script_97 lee DOS fuentes de candidatos: shadow_v4/_accumulated.json (Solana) y multichain/_accumulated.json
        umbral, edad mínima y frescura POR GRUPO · dedup por chain:address (normalize_mint ya baja a minúsculas el EVM)
        status "shadow" con campo `group` hasta validar cada grupo por separado
monitor_shadow.py → métrica dual POR GRUPO (y por versión) · el veredicto por grupo habilita la emisión de ese grupo
```

Cómo convive con `script_82`:
- **No lo toca.** La ruta Solana sigue siendo la rápida (20 min). La multi-chain es lenta (30–60 min), porque CoinGecko sin key admite ~1 request cada 15 s [V doc 23].
- **Archivos separados** de acumulado. No hay escrituras cruzadas ni conflictos de rebase entre workflows.
- **Un solo emisor** (`script_97`) y un solo formato de alerta y de dossier. El template ya soporta `chain`, exploradores EVM y DexScreener por chain (T4).
- **Memes EVM** (grupo a en Base / Monad): misma lógica que Solana (edad, liquidez, volumen, m5/h1), alimentada por GeckoTerminal `new_pools` / `trending_pools`. Blast sin actividad: 0 pools nuevos [V doc 23].

### 6.3 Orden de activación (prioridad de Dirección)

| Paso | Grupo | Fuentes | Requisito para pasar al siguiente |
|---|---|---|---|
| 1 | **h** blue chips (BTC/ETH/SOL) | Binance data-api (velas desde 2017), Coinbase / Kraken (cruce), Deribit DVOL, Fear & Greed, funding (fallback Hyperliquid / dYdX si Binance devuelve 451 desde Actions) | Acceso verificado **desde Actions**; walk-forward con purga; ≥ 20 eventos resueltos en sombra |
| 2 | **f** L1/L2 emergentes | CoinGecko layer-1 / layer-2, DefiLlama (TVL y fees por cadena), growthepie, L2BEAT | ídem |
| 3 | **c** gobernanza DeFi | CoinGecko governance, DefiLlama `/protocols` (`listedAt` < 90 días), Snapshot (eventos) | ídem |
| 4 | **e / g** DePIN y RWA | CoinGecko depin / real-world-assets-rwa, DefiLlama (fees, TVL, categoría RWA) | ídem |
| 5 | **b / d** preventa y sintéticos | Hyperliquid (premium, OI, HIP-3), Aevo (pre-IPO), DefiLlama stablecoins (`pegMechanism`), dYdX v4, GMX | ídem; preventa cripto sin fuente gratuita estable [V doc 23] |
| — | **a** memes EVM | GeckoTerminal por red | después de que la ruta Solana valide v7.2.1 |

### 6.4 Scoring por tipo de activo [H, a validar grupo por grupo]

| Grupo | Evento a medir (métrica dual adaptada) | Señales del score | Modelos permitidos |
|---|---|---|---|
| h | tocar +kσ antes de −kσ (σ diaria GARCH), k a calibrar; en blue chips un +20% en 48 h es raro | z de retorno vs σ GARCH, DVOL − vol realizada, funding en percentil extremo, Fear & Greed ≤ 20 / ≥ 80, ruptura de Bollinger con volumen, ATR | **GARCH / EGARCH / HAR-RV, ATR, Bollinger** (permitidos en Universo A; `arch`, licencia NCSA) |
| f | +20% en 48 h relativo a ETH/SOL | momentum relativo, aceleración de TVL (2.ª derivada 7 d), fees/TVL en percentil alto, protocolos nuevos por semana | GARCH solo con ≥ 365 velas |
| c | +20% en 48 h alrededor del cierre de propuestas | protocolo < 90 días, fees en ascenso, mcap/TVL bajo, propuestas de emisiones o fee switch | event study + placebo |
| e / g | +20% en 48 h | divergencia precio vs fees 30 d, FDV/mcap, TVL creciendo más rápido que el mcap (RWA) | event study; no modelar el precio de tesorerías tokenizadas |
| b | convergencia del premium al listar | premium mark/oracle, crecimiento de OI | sin GARCH (no hay historia) |
| d | desvío del peg y su reversión | \|precio − 1\|, caída del circulante semanal, funding extremo | reversión a la media (OU) [H] |
| a | +20% antes de −30% (igual que Solana) | edad, liquidez, volumen, m5/h1; datos de riesgo (GoPlus / Honeypot) como **dato del dossier**, no del score, hasta testearlos (propuesta I-2) | **sin GARCH / ATR / Bollinger** (prohibido en memecoins) |

**Reglas comunes:**
- Cada grupo tiene su `scoring_version`, su umbral y su veredicto en sombra con n ≥ 20, IC90 de Wilson y baseline propio.
- Ningún grupo emite fuera de sombra sin decisión de Dirección.
- El dossier de cada grupo usa las mismas 7 secciones. La sección 3 explica la fórmula de ese grupo.

### 6.5 Presupuesto y riesgos

- **Una corrida del scanner:** ~13 llamadas en ~2,5 min. A una corrida cada 30 min son ~620 llamadas/día a CoinGecko sin key, con espaciado de 15 s [I: el límite diario sin key no está documentado; si aparecen 429 persistentes, bajar a cada 60 min].
- **IP de los runners de EE.UU.:** Binance derivados puede devolver 451. Cada fuente se verifica desde Actions antes de depender de ella (deuda del doc 23).
- **Fuentes que pasan a pago** (ya pasó con DefiLlama: 402): la sonda de deriva de fuentes (propuesta I-5 del doc 23) lo detecta.

---

## Anexo C — Componentes del score v7.2.1 (`script_82.score_token`) [V, leído del código]

| Componente | Condición | Puntos |
|---|---|---|
| Score del feed | `ws_score × 0,3` | 0 a +30 |
| MCap | ≥ $1M / ≥ $100K / ≥ $50K / menor | +25 / +15 / +10 / 0 |
| Volumen 24 h | ≥ $1M / ≥ $100K / ≥ $50K / menor | +20 / +15 / +10 / 0 |
| Liquidez | ≥ $100K / ≥ $50K / ≥ $20K / menor | +15 / +10 / +5 / 0 |
| Cambio 24 h | ≥ +50% / ≥ +20% / ≤ −30% | +10 / +5 / −5 |
| Buy pressure dinámica (`bp_delta` vs la corrida anterior) | ≤ −0,10 / ≥ +0,10 (solo par maduro) | −15 / +15 |
| **Solo par maduro (edad ≥ 60 min, gate v7.2.1):** | | |
| · Volumen m5/h1 | > 0,5 / > 0,25 | +25 / +15 |
| · Trades m5/h1 | > 0,5 / > 0,25 | +20 / +10 |
| · Buy pressure m5 | > 60% / > 55% | +25 / +15 |
| · Momentum | m5 > 0 y h1 > 0 / m5 > 0 y h1 > −5% | +20 / +10 |
| · Edge temprano | edad < 4 h | +8 |
| · Volumen m5 | > $1K / > $500 | +10 / +5 |
| Detección tardía | sin volumen m5 y edad > 4 h | −30 |
| Par viejo | edad > 24 h | −50 |
| Venta dominante | buy pressure < 40% con volumen m5 | −20 (el tramo < 30%, −35, está detrás del de < 40% y no se alcanza) [V] |
| Sobrecompra | cambio 24 h > 50.000% | −50 |
| | > 5.000% con liq/mcap < 1% / < 3% | −50 / −15 |
| | > 500% con liq/mcap < 1% / < 3% | −30 / −10 |
| Kill switch | edad < 5 min y cambio 24 h > 10.000% | −50 |
| **Final** | `min(100, max(0, int(suma)))` | 0–100 |

Filtros de emisión (`script_97`):
- score ≥ 56;
- scoring de los últimos 60 min (R1);
- edad del par ≥ 30 min (edad desconocida = no emite);
- dedup por mint.
