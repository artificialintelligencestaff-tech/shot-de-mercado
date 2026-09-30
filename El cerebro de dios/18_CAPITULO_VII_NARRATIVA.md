---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: PROTOTIPO_PENDIENTE_AUDITORIA
last_updated: 2026-09-30
version: 0.1
---

# Capítulo VII — Capa de Anticipación Narrativa

Rama `claude/cap-vii-narrativa`, construida sobre `claude/prom-cap-ii` rebaseada sobre `main`. Sin pushear.
Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente.
Todo parámetro de este capítulo es **heurístico no calibrado**, salvo que se indique la evidencia que lo calibra.

## 0. Resumen ejecutivo

1. **La hipótesis motivadora se probó con datos reales y no se sostiene para tokens establecidos.**
   - H1: "atención masiva sobre videojuegos → los tokens gaming suben".
   - Datos: 75 picos de atención (Wikipedia, 20 juegos, 2022-2026) contra una canasta IMX/AXS/SAND/MANA/GALA, con BTC como referencia.
   - Resultado: hit rate a 48 h de **46,7% (IC90 37,3-56,0%) contra un placebo de 42,5%**, y retorno anormal medio de **−0,50%**. **H1 rechazada** [V].
   - El subconjunto GTA VI tampoco muestra efecto: n=8, hit rate 25%.
2. **En el caso GTA VI, lo que sí "va a explotar" son las copias.**
   - Hoy ya hay **28 tokens con "GTA" en el símbolo** para la búsqueda "GTA6" (cota inferior): 15 tienen menos de $10k de liquidez y 19 tienen menos de 30 días [V].
   - La literatura mide ≥10% de copycats en pump.fun (arXiv 2609.10246) y rug en la mayoría de los tokens nuevos (arXiv 2608.20271).
   - Consecuencia de diseño: la capa narrativa **protege al usuario de las copias** antes de intentar predecir pumps.
3. **El prototipo funciona de punta a punta, y en dry-run reproduce las respuestas reales capturadas** [V]. Calendario (Wikidata: GTA VI → **2026-11-19**) → atención → mapeo → lupa en 3 chains → fusión con `lib_fusion`.
4. **El ciclo científico queda operativo:** hipótesis → medición → calibración.
   - El registro guarda el override `thematic = 0.0` para gaming, junto con la evidencia que lo justifica.
   - Si una hipótesis nueva se valida, el peso se actualiza con su propia evidencia.

## 1. Método científico

| | H1 (probada) | H2 (formalizada, pendiente) | H3 (formalizada, pendiente) |
|---|---|---|---|
| **Hipótesis** | Un pico de atención (Wikipedia) sobre un videojuego masivo → la canasta gaming supera a BTC en las 48 h posteriores a la detección, con p > 55% | Un pico de atención sobre un tema X → los tokens `name_match` creados dentro de ±7 días hacen +20% en 48 h **y** rugean dentro de los 7 días (bombeo y descarga) | En la ventana de anticipación (−14 a −1 días) de un evento programado, los tokens `direct` superan a su sector |
| **Datos** | Wikipedia Pageviews (sin key) + Binance data-api (sin key), 2022-01 → 2026-09 | Pageviews + OHLCV de GeckoTerminal por pool (multi-chain) + MemeChain (CC-BY-4.0) para las etiquetas de rug | Wikidata P577 + precios de tokens con vínculo `direct` (hay que curarlos: hoy no existe ninguno para GTA VI) |
| **Método** | Estudio de eventos; ventanas [−1,+1], **[+1,+3]** y [−8,−1]; retorno anormal = canasta − BTC | Estudio de eventos por token; rug = TVL −99% u 80% del tiempo inactivo (definición de arXiv 2608.20271) | Estudio de eventos contra el índice sectorial |
| **Test** | Hit rate con IC90 por bootstrap contra el placebo (días a más de 7 días de cualquier evento); retorno anormal medio con IC | Proporción con IC90 contra tokens de la misma edad sin narrativa | Igual que H1 |
| **Validación** | Umbrales fijados a priori (sin ajuste, así que el test queda fuera de muestra por construcción); estabilidad por bloques anuales con purga de 48 h | Walk-forward con purga de 48 h | Walk-forward con purga de 48 h |
| **Aceptación** | n ≥ 20 · hit > 55% · cota inferior del IC90 > placebo | Idem | Idem |
| **Estado** | **Rechazada** [V] | [P] requiere OHLCV histórico de pools chicos | [P] requiere curar vínculos `direct` |

Dónde vive cada paso en el código (`lib_narrative.py`):
- `detect_narrative_emerging`: usa solo datos previos a t (sin look-ahead). La invariancia está verificada con un test, y la mutación que introduce look-ahead lo hace fallar.
- `event_study`, `placebo_days`, `bootstrap_ci`, `walk_forward_splits`, `merge_close_events` y `evaluate_hypothesis` implementan los demás pasos.
- `pilot_event_study_gaming.py` es la corrida reproducible de H1.

## 2. Arquitectura (evaluación de la propuesta de Dirección)

```
A Calendario ──┐
               ├─> fase del evento (lejano · anticipación · evento · post)
B Atención ────┤─> pico / ratio actual contra la mediana de 28 días
               │
C Mapeo ───────┴─> vínculos: direct · thematic · name_match (este último solo aporta riesgo)
                    │
D Lupa ─────────────┴─> ¿hay flujo real y absorbible? (liquidez, rotación, compras/ventas, edad)
                    │
E Fusión ───────────┴─> lib_fusion: fuente "narrative" + lupa (en el lugar de dexscreener)
```

| Capa | Propuesta original | Qué cambié y por qué |
|---|---|---|
| A | TGEs, upgrades, macro, lanzamientos virales | Se implementó **Wikidata** para videojuegos y películas [V], filtrando por popularidad (sitelinks ≥ 15: GTA VI aparece primero con 66). Los eventos macro (FOMC, CPI) y los TGEs van a un calendario manual [P], porque no encontré una fuente gratuita verificada |
| B | GDELT, Google Trends, Reddit, Telegram, RSS | **Google Trends se descarta**: `pytrends` está archivado [V] y la API oficial no es de acceso abierto [I]. **Wikipedia Pageviews lo reemplaza** [V]: es oficial, gratuita y tiene historia desde 2015, así que habilita backtests. GDELT queda como secundaria: esta sesión devolvió límite de tasa (texto) 2 veces y HTTP 429 una vez [V]. Reddit RSS y `t.me/s` quedan [P] |
| C | pyahocorasick + GLiNER + base narrativa → tokens | **Registro curado** con tipo de vínculo y evidencia por vínculo, más `name_match` generado en tiempo de ejecución, que solo resta. La extracción usa `KeywordMatcher` con la biblioteca estándar; **pyahocorasick** (BSD-3) reemplaza a ese matcher sin cambios de interfaz cuando haya miles de patrones. **GLiNER** (Apache-2.0) queda como opcional [P], porque necesita torch |
| D | Liquidez, holders, volumen, momentum | DexScreener `/tokens` **filtrado por la chain pedida** [V]. **Limitación** [V]: solo ve DEX, e IMX muestra $53 de volumen 24 h en su par de ethereum porque su flujo está en CEX y en su propia chain. Para los Universos A y B hay que sumar el volumen total de CoinGecko [P] |
| E | Fuente adicional en lib_fusion | Fuente `narrative` + lupa ocupando el lugar de `dexscreener` (para no contar DexScreener dos veces) |

## 3. Interfaces (JSON)

```jsonc
// Evento (Capa A)
{"id": "wikidata:Q23648408", "title": "Grand Theft Auto VI", "date": "2026-11-19", "category": "game_release",
 "popularity_sitelinks": 66, "source": "wikidata", "source_url": "...", "date_quality": "single|multiple",
 "label_quality": "ok|sin_etiqueta_en", "phase": "lejano", "days_to_event": 50, "evidence": "[V] ..."}

// Serie de atención (Capa B) y detección
{"topic": "gta6", "source": "wikipedia_pageviews", "status": "ok", "points": [{"date": "2026-09-28", "value": 9984}]}
{"topic": "gta6", "spikes": [{"date": "2026-08-28", "value": 96567, "baseline_median": ..., "ratio": 11.06, "robust_z": ...}],
 "latest": {...}, "emerging_now": false, "params": {...}}

// Vínculo narrativa → token (Capa C)
{"chain": "solana", "address": "ATLAS...", "symbol": "ATLAS", "link_type": "thematic|direct|name_match",
 "evidence": ["[V] CoinGecko categories: Gaming (GameFi)"], "risk_flags": ["copycat_suspect", "new_token", "low_liquidity"]}

// Lupa (Capa D) — mismo contrato de evidencia que script_112
{"chain": "base", "address": "0xfa98...", "status": "ok|sin_par_en_chain|error", "metrics": {"liquidity_usd": ..., "volume_24h_usd": ...,
 "price_change_24h_pct": ..., "buys_24h": ..., "sells_24h": ..., "pair_age_days": ...},
 "evidence": {"source": "lupa", "label": "HEURISTICA_NO_CALIBRADA", "llr_raw": -0.25, "components": [...], "verdict": "flujo_confirmado|sin_confirmar|riesgo|sin_datos"}}

// Evidencia narrativa (Capa E) → lib_fusion.fuse(chain, address, {"narrative": llr, "dexscreener": lupa_llr, ...})
{"source": "narrative", "label": "HEURISTICA_NO_CALIBRADA", "llr_raw": 0.452, "components": [...]}
```

El registro de narrativas vive en `04_Config/narrative_registry.json` (versionado). Contiene las keywords, los ítems de Wikidata, los artículos de Wikipedia, la query de GDELT, los tokens con su evidencia y `link_weight_overrides` con la evidencia de calibración.

## 4. Parámetros (heurísticos no calibrados)

| Parámetro | Valor | Nota |
|---|---|---|
| `SPIKE_RATIO` / `SPIKE_ROBUST_Z` / `SPIKE_BASELINE_DAYS` | 5,0 / 3,5 / 28 | Fijados antes del piloto. Detectan el Trailer 1 (ratio 6153x) y el pico del 28/08/2026 (11x) |
| `MIN_BASELINE` (pageviews) | 50 vistas | Evita leer ruido en artículos chicos |
| `ANTICIPATION_DAYS` / `POST_EVENT_DAYS` | 14 / 7 | Sin evidencia todavía (lo mide H3) |
| `LINK_WEIGHTS` | direct 1,0 · thematic 0,5 · name_match 0 | **gta6: thematic = 0,0 calibrado por el piloto H1** |
| `NARRATIVE_LLR_MAX` | 1,0 nats | Después, `lib_fusion` recorta a ±2 |
| `COPYCAT_LLR` | −1,0 | name_match con menos de 30 días |
| Lupa | liquidez < $10k → −0,75 · ≥ $100k → +0,25 · rotación ≥ 1 con precio al alza → +0,5 · rotación < 5% → −0,25 · compras/ventas > 1,2 → +0,25, < 0,8 → −0,25 · par < 7 días → −0,5 | |
| Prior de la fusión | Beta(116, 8577), media 1,33% | [V] frecuencia de +20% en 48 h por token-día en la canasta gaming (2022-2026) |

## 5. Ejemplo trabajado: GTA VI (`demo_gta6.py`)

Datos reales capturados el 2026-09-30 (fixtures). En dry-run el resultado es idéntico al de la corrida en vivo [V].

**Escenario `real_hoy` (2026-09-30):**

1. **A.** Wikidata indica que GTA VI (Q23648408) sale el **2026-11-19**. Faltan 50 días, así que la fase es `lejano`.
2. **B.** Wikipedia registra 9984 vistas el 28/09, con ratio 0,82x (sin pico actual). En los últimos 120 días hubo 3 picos reales, el 27, 28 y 29 de agosto (el máximo, 96.567 vistas y 11x). GDELT: 429.
3. **C.** Hay 4 vínculos temáticos curados en 3 chains:
   - IMX en ethereum;
   - PRIME en base y en ethereum;
   - ATLAS en solana.

   Además aparecen 28 `name_match`, todos marcados `copycat_suspect`; 19 son `new_token` y 15 son `low_liquidity`.
4. **D.** Resultado de la lupa por token:

   | Token | Liquidez | Volumen 24 h | Veredicto |
   |---|---|---|---|
   | IMX (ethereum) | $87.721 | $53 | `sin_confirmar` |
   | PRIME (base) | $18.574 | $956 | `sin_confirmar` |
   | ATLAS (solana) | $156.914 | $41.463 | `sin_confirmar` |
5. **E.** La P de +20% en 48 h da **1,27%** (IC90 1,08-1,47%) para IMX y PRIME, y **1,33%** (1,14-1,55%) para ATLAS. Hay 2 fuentes activas de 5 o 6 (narrativa y lupa).

**Escenario `simulado_anticipacion` (2026-11-12, 7 días antes del lanzamiento).** La serie se completa con un shock SIMULADO de 3x, 5x y 8x en los últimos 3 días, que es el patrón del Trailer 1:

- **B.** Pico en el último día (8x, emergente = sí).
- **E heurístico:** LLR narrativo de +0,452, que lleva P a **1,39%** (IC90 1,17-1,62%) para IMX y PRIME, y a **1,44%** para ATLAS.
- **E calibrado (thematic = 0):** LLR 0, así que P vuelve a la base: **1,27%**.

**Lectura para el usuario final:** "GTA VI sale el 19/11. Ninguna crypto es de Rockstar. En 4,7 años, los picos de atención sobre videojuegos no movieron a los tokens gaming establecidos. Los tokens 'GTA6' que vas a ver son de terceros: 28 hoy, la mayoría nuevos y sin liquidez. Esto no es una señal de compra."

## 6. Resultados del piloto H1 (`pilot_event_study_gaming.json`)

Período 2022-01-01 → 2026-09-29. Se detectaron 348 picos en 20 artículos, que quedaron en **75 eventos** después de fusionar los que estaban a 7 días o menos entre sí (7 en 2022, 15 en 2023, 17 en 2024, 26 en 2025 y 10 en 2026). El placebo tiene entre 829 y 832 días según la ventana.

| Ventana | n | Hit rate (IC90) | Placebo | Retorno anormal medio (IC90) | Placebo | Vertical (+20%) | Placebo |
|---|---|---|---|---|---|---|---|
| Concurrente [−1,+1] | 75 | 45,3% (36,0-54,7) | 43,4% | +0,31% (−0,69; +1,34) | −0,17% | 8,0% | 5,4% |
| **Operable [+1,+3]** | 75 | **46,7% (37,3-56,0)** | 42,5% | **−0,50% (−1,28; +0,30)** | −0,38% | 2,7% | 5,2% |
| Anticipación [−8,−1] | 75 | 38,7% (29,3-48,0) | 39,3% | −2,92% (−4,49; −1,33) | −0,45% | 18,7% | 17,1% |

- **Estabilidad** (bloques anuales con purga de 2 días): el hit rate operable fue 0,50, 0,33, 0,55 y 0,33. Sin consistencia.
- **Subconjunto GTA VI** (exploratorio): n=8, hit rate 25%, retorno anormal medio −0,15%, IC90 (−2,5%; +2,5%).
  - Los dos trailers dieron +7,2% (4/12/2023) y +6,9% (8/5/2025).
  - Las postergaciones y noticias dieron negativo.
  - **Mirar solo el top 3 ("2 de 3 son GTA VI") habría sido cherry-picking.**
- **Anticipación** [I, exploratorio]: el retorno anormal cae a −2,9% contra −0,45% del placebo, con IC que excluye al placebo.
  - No era la hipótesis principal y hubo 3 ventanas (comparaciones múltiples), así que hay que replicarlo antes de usarlo.
  - Explicación candidata [H]: los picos de atención de juegos coinciden con fases de fortaleza relativa de BTC.

**Limitaciones del piloto:**
- Los 20 juegos se eligieron a priori pero a mano (sesgo de selección).
- La canasta tiene solo 5 tokens listados en Binance (sesgo de supervivencia: excluye tokens deslistados).
- Precios diarios: el efecto intradía no se mide.
- Pageviews de en.wikipedia solamente.
- La publicación de pageviews tiene un día de demora (por eso la ventana operable arranca en t+1).
- BTC es la única referencia.

## 7. Extensión multi-chain y multi-universo

**No cambia:**
- `lib_narrative` no tiene ninguna chain fija (lo verifica un test).
- Toda la red pasa por el fetcher.
- Los vínculos son (chain, address) con normalización por formato (0x en minúsculas).
- La lupa filtra pares por `chainId`.
- La evidencia usa el mismo contrato que `script_112`, y la fusión es `lib_fusion`.

**Cambia por universo:**

| | Universo C (memes, Base, Blast, Monad) | Universo B (UNI, ICP, APT, PSG) | Universo A (BTC, ETH, SOL) |
|---|---|---|---|
| Narrativas típicas | Cultura pop, virales, política | Upgrades, gobernanza, deportes (PSG) | Macro, ETF, regulación |
| Capa A | Wikidata (juegos, películas) | Calendarios de gobernanza (Snapshot [P]); fixture de partidos (PSG) [P] | FOMC/CPI (manual) [P]; flujos de ETF [P] |
| Vínculos | Casi siempre `thematic` o `name_match` → foco en riesgo | Muchos `direct` (el token ES del protocolo o del club) → H3 aplicable | `direct` |
| Lupa | DexScreener (DEX) | DEX + volumen CEX (CoinGecko) [P] | Volumen CEX + derivados; la nota de §7 de la directiva habilita GARCH/ATR aquí |
| Prior | Tasa de rug alta (MemeChain: 5,15% muere en menos de 24 h) | Por sector | Por activo |

Chains nuevas: solo requieren que DexScreener, GeckoTerminal y GoPlus las soporten, más los alias de chain en el colector. El registro acepta cualquier slug de chain.

## 8. Fuentes investigadas

| Fuente | Tipo | Licencia/acceso | Actividad | Verificación | Veredicto |
|---|---|---|---|---|---|
| Wikipedia Pageviews (Wikimedia REST) | API | Gratis, sin key | Oficial | [V] series 2015→ayer; Trailer 1: 341.519 vistas | **P0 — adoptada** |
| Wikidata SPARQL | API | Gratis, sin key (datos CC0 [I]) | Oficial | [V] GTA VI → 2026-11-19; hay fechas múltiples por ítem | **P0 — adoptada** (Capa A) |
| Binance data-api.binance.vision | API | Gratis, sin key (ToS de Binance) | Oficial | [V] 1725-1744 velas diarias por símbolo | **P0 para backtests**; [P] probar desde runners de EE.UU. |
| DexScreener `/tokens`, `/search` | API | Gratis, sin key | — | [V] multi-chain, búsqueda con tope de 30 pares | P0 (lupa y name_match) |
| CoinGecko `/coins/categories/list`, `/markets?category=`, `/coins/{id}` | API | Gratis sin key, con límite de tasa | — | [V] 1040 categorías; plataformas por chain | P1 (curar vínculos) |
| GDELT DOC 2.0 | API | Gratis, sin key | — | [V] 2 respuestas de límite de tasa y 1 HTTP 429 en esta sesión | P2 (reintentos, o archivos crudos de GDELT 2.0 [P]) |
| Google Trends / pytrends | Librería | — | **Archivada** (2024-08) [V] | — | **Descartada** |
| trendspy · gdelt-doc-api · python-mwviews | Librerías | MIT | Último push 2024-12 / 2025-04 / 2022-03 [V] | — | Descartadas (actividad mayor a 6 meses); la biblioteca estándar alcanza |
| pyahocorasick | Librería | BSD-3 | 2026-04, 1126★ [V] | — | P2 (con miles de keywords) |
| GLiNER | Librería | Apache-2.0 | 2026-09, 3966★ [V] | — | P2 (NER zero-shot; requiere torch) |
| MemeChain (Zenodo 18246856) | Dataset | **CC-BY-4.0**, abierto, 709,6 MB [V] | Enero 2026 | — | **P1** (etiquetas de rug multi-chain para calibrar) |
| Repos "memecoin narrative" en GitHub | Código | Mayormente sin licencia, 0-1★ [V] | 2026 | — | No usar (sin auditar) |

## 9. Riesgos

- **Manipulación narrativa:** el 23,5% de los tokens de pump.fun se crean después de posts en Twitter o Truth Social, y hay bots en Telegram y Twitter (arXiv 2609.10246). Una señal de atención se puede fabricar. Wikipedia es más difícil de manipular que las redes, pero no es inmune [I].
- **Dirigir al usuario hacia copias:** mitigado con `name_match` = solo riesgo.
- **La lupa, al ver solo DEX, subestima el flujo de los tokens grandes** [V con IMX].
- **Fuentes con límite de tasa:** GDELT [V]. Los ToS de Binance y CoinGecko pueden cambiar.
- **Wikidata:** fechas múltiples o provisorias, y etiquetas faltantes [V].
- **Comparaciones múltiples:** el hallazgo de la ventana de anticipación no está preregistrado.
- **Prior muy informativo** (n=8691): P casi no se mueve con 1 o 2 fuentes. Es correcto dada la evidencia, pero puede parecer "inútil" si no se explica.

## 10. Pendientes

- [P] H2: OHLCV histórico de pools chicos (probar GeckoTerminal OHLCV) + etiquetas de MemeChain.
- [P] H3: curar vínculos `direct` (tokens oficiales de juegos, protocolos y clubes).
- [P] Capa A: calendario manual (FOMC, CPI, TGEs) y gobernanza (Snapshot).
- [P] Capa B: Reddit RSS y `t.me/s` con conteo por `KeywordMatcher`; GDELT con reintentos.
- [P] Lupa: volumen CEX (CoinGecko `total_volume`).
- [P] Workflow: correr `demo_gta6` o una versión productiva a diario (requiere autorización: toca workflows).

## 11. Cómo ejecutar

```bash
python 04_Config/scripts/test_lib_narrative.py              # 28 tests, sin red
python 04_Config/scripts/demo_gta6.py                       # dry-run con respuestas reales capturadas
python 04_Config/scripts/demo_gta6.py --live                # APIs reales
python 04_Config/scripts/demo_gta6.py --capture-fixtures    # renueva las fixtures
python 04_Config/scripts/pilot_event_study_gaming.py        # piloto H1 (~2 min, solo lectura)
```
