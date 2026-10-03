---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: DISEÑO + implementación parcial — D-041 T6/T7; D-055 (#2 registro, #8 debate, #12 episodios)
last_updated: 2026-10-03
version: 0.2
complementa: doc 27 (fórmulas y eventos por grupo), doc 32 (scorer joven), doc 34 (fuentes)
---

# 36 — Método científico por grupo (a–i) + Dossier v2

Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente.

## 0. Fundamento

**No todos los activos se interpretan igual.**
- Una memecoin de 5 minutos no tiene historia de precio: solo información (menciones, estructura, liquidez).
- Un blue chip tiene 9 años de velas y un mercado de derivados que anticipa volatilidad.
- Una preventa no cotiza: lo único medible es la promesa y el evento de listing.

Aplicar el mismo método a los tres produce ruido. El doc 27 fija, para cada grupo, **qué se puntúa** (componentes, pesos, evento). Este documento fija **cómo se prueba** (patrón #2, método científico automatizado):
- qué hipótesis se pone a prueba;
- con qué fuente;
- con qué métrica;
- con qué criterio se acepta o se descarta.

Un grupo no gana el derecho a pesar en el score por diseño: lo gana cuando su hipótesis supera al baseline con datos propios.

## 1. Protocolo común (el mismo para los 9 grupos)

| Paso | Qué se hace | Dónde vive |
|---|---|---|
| 1. Preregistro | La hipótesis se escribe **antes** de mirar los resultados: enunciado, evento, métrica, n mínimo, α y criterio. No se edita después; una variante es una hipótesis nueva. | `02_Analisis/hypotheses/_registry.jsonl` (append-only, `lib_scientific_method`, D-055) [V] |
| 2. Evento | El evento del grupo (doc 27 §3.1): ventana de 48 h, orden intra-vela conservador (open → low → high → close). | `lib_scoring_multichain.EVENTS` [V] |
| 3. Baseline | Tasa del evento en **todo** el universo del grupo, no solo en lo alertado. Sin baseline, una tasa alta no significa nada. | por grupo [P] |
| 4. Métrica | Tasa del evento con IC90 de Wilson. Para hipótesis comparativas (señal sí / no), Fisher exacto unilateral con α = 0,10, como H-0 (doc 32). | `calibrate_threshold_v72.wilson` [V] |
| 5. Controles | **Placebo:** fechas desplazadas ±6–24 h; la señal no debe rendir igual. **Walk-forward** semanal con purga de 48 h. **Contrafactual:** los +20% no alertados y qué señales tenían (doc 35 §6.5). | [P] |
| 6. Refutación (#8, debate adversario) | Antes de aceptar, un segundo evaluador automático intenta romper el resultado: placebo, permutación de etiquetas, submuestras por chain y por semana. Si una submuestra invierte el signo, no se acepta. | `lib_adversarial_debate` (§4.1, D-055) [V] |
| 7. Decisión | **Acepta:** la señal pasa a pesar en el score con su LLR estimado (doc 27 §4.1). **Rechaza:** sale (#18, poda cognitiva; P-13). **Inconcluso:** sigue midiendo hasta el n máximo y después se rechaza. | memoria episódica (#12) |
| 8. Episodio (#12) | Cada hipótesis cerrada deja un episodio con hipótesis, datos usados (hash), resultado, decisión y fecha. Es la memoria que impide re-probar lo ya descartado. | `02_Analisis/sources/_episodes.jsonl` + `_episodes_<writer>.jsonl` (`lib_episodic_memory`, D-055) [V] |

**Pizarra compartida (#5).** Ninguna hipótesis consulta fuentes por su cuenta. Lee lo que ya escriben los bots:
- `_merged.jsonl` y `_index.json` (menciones normalizadas, #19);
- `_graph.json` (co-mención, #7);
- `02_Analisis/multichain/<chain>.json` (mercado);
- `_health.json` (si una fuente estuvo caída, la ventana se marca y no cuenta).

## 2. Tabla por grupo

| Grupo | Hipótesis principal [H] | Evento (doc 27) | Fuentes | Métrica | Acepta si | n mín. |
|---|---|---|---|---|---|---|
| a memecoins | La aceleración de menciones (sorpresa de Poisson, doc 26) más el cluster de co-mención anticipan el evento | +20% antes de −30%, 48 h | PumpPortal WS, DexScreener, Telegram (dexscreener_trending, pumpfun, BinanceKillers), 4chan, `_graph.json` | tasa primaria; Fisher señal sí/no | p < 0,10 **y** diferencia ≥ 10 pp sobre el baseline del grupo | 40 |
| b preventa | Un anuncio de listing en un exchange grande anticipa el rendimiento del primer día | precio al listar ≥ +20% sobre la referencia | canales de anuncios (binance_announcements, OKXAnnouncements, CoinMarketCapAnnouncements), RSS | rendimiento a 24 h desde el listing | mediana > 0 con IC90 que no cruza 0 | 20 |
| c gobernanza | Una propuesta de fee switch, buyback o emisiones, con fees en ascenso, anticipa una revalorización | +20% antes de −15%, 48 h | DefiLlama (fees, `listedAt`), Snapshot, keywords `governance` / `dao` | event study alrededor del cierre de la propuesta | retorno anormal acumulado > 0 con IC90 y placebo nulo | 20 |
| d sintéticos | Un funding extremo con OI en crecimiento anticipa continuación; un desvío de peg, reversión | +20% antes de −15%, 48 h (peg: vuelta a la banda) | Hyperliquid, dYdX v4, DefiLlama stablecoins | tasa por régimen de funding | régimen extremo > baseline, p < 0,10 | 20 |
| e DePIN | Fees o revenue que crecen más rápido que el mcap anticipan una revalorización | +20% antes de −15%, 48 h | DefiLlama fees, CoinGecko depin, feed `gnews_depin` | tasa por cuartil de (Δfees − Δmcap) | cuartil superior > inferior, p < 0,10 | 20 |
| f L1/L2 | El momentum de TVL, la cuota de volumen de DEX y la cantidad de trending pools anticipan el token de la chain (relativo a ETH/SOL) | +20% antes de −15%, 48 h, relativo | `multichain/<chain>.json` (script_114 v0.2), DefiLlama chains, L2BEAT | tasa por percentil de momentum | percentil ≥ 80 > baseline, p < 0,10 | 20 |
| g RWA | Un TVL que crece más rápido que el mcap anticipa una revalorización del token de la plataforma | +20% antes de −15%, 48 h | DefiLlama RWA, CoinGecko real-world-assets-rwa, feed `gnews_rwa` | tasa por cuartil de (ΔTVL − Δmcap) | cuartil superior > inferior, p < 0,10 | 20 |
| h blue chips | Un z de retorno extremo contra la σ del GARCH, con DVOL − vol realizada y funding en percentil extremo, anticipa ±2σ | tocar +2σ₄₈ antes de −2σ₄₈ | Binance data-api, Deribit DVOL, Fear & Greed, funding | tasa del evento por régimen | régimen extremo > baseline, p < 0,10; walk-forward estable 4 semanas | 30 |
| i establecidos | Una reactivación (pico de menciones + pico de volumen tras > 30 días de calma) anticipa el evento | +20% antes de −15%, 48 h (solo registro) | `_merged.jsonl`, `_graph.json`, CoinGecko | tasa con reactivación vs sin | p < 0,10 (registro; no emite por decisión de Dirección) | 20 |

**Modelos por grupo** (doc 27 §3, sin cambios): GARCH, EGARCH, ATR y Bollinger **solo** en h, y en f con ≥ 365 velas; **nunca** en a. El scorer joven (doc 32) cubre a < 60 min.

## 3. Detalle por grupo

### a — Memecoins
- **Por qué se interpreta distinto.**
  - El token nace sin historia: la información precede al precio.
  - El evento útil es tocar +20%. El cierre a 48 h es mayormente un −99% (doc 21: 76,2% después de tocar +20%), así que el método mide la primaria y reporta la post-+20% como métrica.
- **H-a1 (mención acelerada).** Sorpresa de Poisson ≥ 4,6 nats en la hora anterior a la detección (doc 26 v0.1, sobre `_merged.jsonl`) contra < 4,6. Fisher unilateral.
- **H-a2 (cluster).** Un token con un vecino a dos saltos en `_graph.json.related()` que tocó +20% en las 24 h previas, contra uno sin ese vecino.
- **Controles.** Gate de edad (doc 31). Kill switches. Las ventanas con `rss` o `telegram` en estado `caído` en `_health.json` no cuentan para la señal.
- **No contamina H-0.** H-0 (doc 32) usa la señal informacional del scorer joven. H-a1 y H-a2 se miden sobre un conjunto separado por fecha (posterior al cierre de H-0).

### b — Preventa
- **Por qué se interpreta distinto.** No hay precio antes del listing: no existe "aceleración", existe la distancia entre la promesa y el primer precio.
- **H-b1.** Los activos con un anuncio de listing en Binance, OKX o CoinMarketCap (canales de T5, 15 canales [V]) tienen rendimiento a 24 h desde el listing con mediana > 0.
- **Medición.**
  - Referencia = primer precio del par.
  - Solo registro: sin ruta de compra antes del listing (regla núcleo, doc 24).

### c — Gobernanza DeFi
- **H-c1.** Event study con ventana [−2 d, +2 d] alrededor del cierre de propuestas con keywords de valor (`fee switch`, `buyback`, `emission`; `GOV_KEYWORDS` [V]). Placebo: las mismas fechas en tokens de gobernanza sin propuesta.
- **Fuente nueva.** Keywords `governance` / `dao` en `_merged.jsonl` como proxy temprano de discusión.

### d — Sintéticos
- **H-d1 (perps).** Funding por encima del percentil 95 con OI creciendo > 20% en 24 h → continuación en 48 h.
- **H-d2 (pegs).** Desvío |p − 1| > 1% → vuelta a la banda en 48 h, con un modelo de reversión a la media (OU) [H].
- Sin GARCH: no hay historia suficiente en la mayoría.

### e — DePIN
- **H-e1.** Cuartil superior de (crecimiento de fees a 30 d − crecimiento de mcap a 30 d) contra el cuartil inferior.
- El feed `gnews_depin` (rss, 17 ítems nuevos en una corrida [V]) da el contexto del dossier, no el score.

### f — L1/L2 emergentes
- **H-f1.** Percentil de momentum compuesto: ΔTVL 7 d + cuota de volumen de DEX + cantidad de trending pools en `multichain/<chain>.json`.
- El evento se mide **relativo** a ETH (L2) o a SOL: un +20% del token cuando ETH hizo +18% no es una señal propia.

### g — RWA
- **H-g1.** Igual que e, con TVL de colateral en lugar de fees.
- El activo tokenizado estable no se puntúa (doc 27 §2.1): solo el token de la plataforma.

### h — Blue chips
- **H-h1.** El evento es simétrico en σ (±2σ₄₈ del GARCH(1,1)): un +20% en 48 h en BTC es raro y no sirve como evento.
- Regímenes:
  - z del retorno de 24 h > 2;
  - DVOL − vol realizada en el percentil 90;
  - funding en el percentil 5 o 95;
  - Fear & Greed ≤ 20 o ≥ 80.
- Walk-forward de 4 semanas estable antes de aceptar. Es el grupo con más datos y el que más fácil se sobreajusta.

### i — Establecidos sin grupo
- **H-i1.** Reactivación: menciones 24 h > 5× la mediana de 28 días (criterio de pico de `lib_narrative`, SPIKE_RATIO) **y** volumen 24 h > 3× la mediana, tras más de 30 días sin evento.
- Solo registro: alimenta el contrafactual y puede promover un activo a un grupo emisible.

## 4. Automatización y patrones del enjambre

| Patrón | Cómo entra en el método |
|---|---|
| #2 Método científico automatizado | Protocolo §1: preregistro → evento → baseline → métrica → controles → decisión |
| #5 Blackboard | Las hipótesis leen la pizarra (`_merged`, `_index`, `_graph`, `_health`, `multichain/`); no consultan fuentes |
| #7 Knowledge Graph | H-a2 (cluster de co-mención) y el contexto del dossier |
| #8 Debate adversario | advocate contra challenger con reglas explícitas: placebo, permutación, submuestras y estabilidad antes de aceptar (§4.1) [V] |
| #12 Memoria episódica | `_episodes.jsonl` + fragmentos por escritor. Tipos: `hipotesis_evaluada` (cada evaluación persistida), `feed_caido` y `bot_reparado` (bot_self_repair, solo transiciones), `alerta_emitida` (constructor listo; falta cablearlo en el emisor, que es producción) [V] |
| #18 Poda cognitiva | Una señal rechazada o inconclusa al n máximo se retira del score (P-13) |
| #19 Normalización | Todas las comparaciones usan la forma canónica de `lib_normalize` |

**Implementado (D-055) [V]: `lib_scientific_method.py`**
- `register_hypothesis(id, statement, prediction, acceptance, rejection)`: preregistro inmutable. El mismo id con otro contenido da error, porque una variante es un id nuevo.
- `evaluate_hypothesis(id, data)`: corre la prueba preregistrada (`fisher_one_sided`, `rate_vs_baseline` o `median_ci`) y decide con reglas explícitas `{all|any: [[campo, op, valor]]}`. Veredicto: pendiente (n < mín.) · aceptada · rechazada · inconclusa. Guarda `data_hash`.
- La H-0 está migrada como referencia (registrada el 2026-10-02; mismos parámetros). Reproduce el veredicto y el p-valor de `early_review.evaluate_h0`, que sigue siendo su evaluador de producción.

**Implementación pendiente [P]**
- `method_runner.py`: diario. Lee los preregistros, arma las filas y las filas placebo desde la pizarra, llama a `evaluate_hypothesis` y después a `run_debate` (§4.1), y escribe episodios.
- ~~`method_refuter.py`~~: lo reemplaza `lib_adversarial_debate` (§4.1).
- Ninguno toca el score directamente: la promoción de una señal al score la decide Dirección a partir de los episodios.

### 4.1 Debate formalizado (patrón #8, D-055) [V]

**Qué es.** Es el paso 6 del protocolo hecho código (`lib_adversarial_debate.run_debate(hypothesis_id, evidence_set)`). Dos roles discuten sobre **la misma evidencia**. Cada argumento sale de una regla explícita con su peso: sin LLM, determinista.

**Afirmación en debate:** "el efecto que predice la hipótesis es real":
- `fisher_one_sided`: tasa A − tasa B > 0;
- `rate_vs_baseline`: tasa − baseline > 0;
- `median_ci`: mediana > 0.

Para la H-0, que es una nula, "sostenida" equivale a "H-0 rechazada con robustez".

**Evidencia:** `{"rows": [...], "placebo_rows": [...], "subsample_fields": ["chain", "week"]}`.
- Las filas son las mismas de `evaluate_hypothesis`.
- Las filas placebo son las mismas alertas medidas con fechas desplazadas ±6–24 h; las arma quien tiene las velas, no el debate.
- `week` se deriva de `t0`, `ts` o `alert_ts`.
- Un campo con una sola submuestra evaluable no vota. Una submuestra necesita ≥ 10 filas resueltas.

| Rol | Regla | Argumento | Peso |
|---|---|---|---|
| advocate | A1 | efecto significativo (p < 0,10; Wilson IC90 sobre el baseline; IC90 de la mediana > 0) | 2 |
| advocate | A2 | efecto ≥ 10 pp (criterio de §2) | 1 |
| advocate | A3 | n ≥ 2 × mínimo preregistrado | 1 |
| advocate | A4 | el signo se repite en ≥ 75 % de las submuestras | 1 |
| advocate | A5 | placebo no significativo y con menos de la mitad del efecto | 1 |
| advocate | A6 | permutación de etiquetas (500, semilla = hash de los datos) con p < 0,10; solo dos grupos | 1 |
| advocate | A7 | las dos mitades del periodo tienen el signo predicho | 1 |
| challenger | C1 | n < mínimo → **insuficiente** (no hay debate) | fatal |
| challenger | C2 | no significativo | 2 |
| challenger | C3 / C3b | efecto < 5 pp / efecto en la dirección contraria | 1 / 2 |
| challenger | C4 | **una submuestra invierte el signo** | fatal |
| challenger | C5 | **el placebo rinde parecido** (significativo o ≥ la mitad del efecto) | fatal |
| challenger | C6 | la permutación da efectos parecidos (p ≥ 0,10) | 1 |
| challenger | C7 | el signo cambia entre la primera y la segunda mitad | 2 |
| challenger | C8 | faltan resultados en más del 30 % de las filas (sesgo de selección) | 1 |
| challenger | C9 | sin la submuestra más grande el efecto no se sostiene | 2 |
| challenger | C10 | no hay control placebo | 1 |

**Veredicto y confianza**
- **insuficiente:** C1.
- **refutada:** algún argumento fatal, o peso del challenger ≥ peso del advocate, o falta significancia.
- **sostenida:** en cualquier otro caso.
- Confianza = peso del lado ganador / peso total.
- Las razones listan los argumentos fatales o, si no hay, los del lado ganador ordenados por peso.

**Regla de decisión con el paso 7.** Una hipótesis cuya aceptación implica un efecto se acepta solo si `evaluate_hypothesis` dice *aceptada* **y** el debate dice *sostenida*. Ejemplo verificado en los tests: el total pasa Fisher (p < 0,001, +40 pp: solana +70 pp), pero la submuestra `chain=base` invierte el signo (−20 pp), así que el resultado queda *refutada* y no se acepta.

---

## 5. Dossier v2 — "obra informativa" (D-041 T7)

**Objetivo.** El dossier v1 (doc 24, `script_113`) es completo pero se lee como un log: tablas una tras otra. El v2 conserva todos los datos y cambia la forma: un texto editorial que se lee de corrido, con la compra primero (regla núcleo) y los números como respaldo, no como cuerpo.

**Estructura**

| Parte | Qué cuenta | De dónde sale (v1) |
|---|---|---|
| 1. Adquisición | Cómo se compra este activo, hoy, en esta chain: wallet, fondeo, DEX, los 8 pasos, el slippage que corresponde a su liquidez y cuánto mueve una orden de $100 / $1.000 / $10.000. Va siempre primero. | §1 (sin cambios de contenido) |
| 2. Método | Por qué el sistema lo detectó, en prosa: "El scorer v7.2.1 le dio 72 sobre 100. El mayor aporte vino de…". Qué mide el evento del grupo y qué significa la probabilidad mostrada, con su n y su IC90. | §4 + §5 |
| 3. Evidencia | Los datos que sostienen la detección: desglose del score, menciones en las últimas 24 h (cuántas, de qué fuentes, sorpresa de Poisson), vecinos en el grafo de co-mención, consistencia entre fuentes. | §2 + §5 + `_merged` + `_graph` |
| 4. Contexto | Qué es el activo y de dónde viene: grupo (a–i), categoría, narrativa, historia del par, eventos parecidos del histórico del grupo y cómo terminaron (mediana e IQR). | §3 + §6 |
| 5. Cierre | La ventana de la señal (hasta cuándo aplica), qué se va a medir y cuándo se sabe el resultado, y dónde verificar cada número (fuentes, blob, comando de recálculo). | §6 + §7 |

**Reglas de estilo**
- Prosa breve en castellano. Cada número con su fuente y su momento en la misma oración ("liquidez de $141.633 en DexScreener al detectar").
- Una tabla por parte, como máximo. El resto, texto.
- Nada se inventa: lo que falta se dice ("sin descripción publicada"), igual que en v1.
- Sin juicios ni recomendaciones: el dossier informa; el lector decide (doc 22, principio de producto).
- El grupo cambia el relato: una memecoin se cuenta por menciones y estructura; un blue chip por volatilidad y derivados (§2).

**Implementación propuesta [P]**
- `script_113.render_markdown_v2(dossier)` sobre el mismo dict de `build_dossier`, que no cambia.
- Párrafos con plantillas por grupo (sin IA generativa en producción: reglas y texto fijo con datos insertados).
- Convive con v1 detrás de un flag (`DOSSIER_STYLE=v2`) hasta que Dirección compare los dos sobre las mismas alertas.
- Tests: los mismos campos obligatorios del Anexo A del doc 24, el orden de las 5 partes y la ausencia de juicios.
- **Estado:** solo diseño en D-041 (P2).
