---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: FASE 0 IMPLEMENTADA (script_115 + narrative_collector.yml, rama claude/zealous-tesla-3ua19i); Fase 1 pendiente
last_updated: 2026-10-01
version: 0.3
---

# 26 — Métrica de repetición mediática ("masa social ansiosa")

Rótulos: [V] verificado (consulta HTTP o cálculo en esta sesión, 01/10/2026 ~03:00 UTC) · [I] inferido · [H] hipótesis · [P] pendiente.
Todos los umbrales de este documento son **heurísticos, no calibrados**. Se calibran en sombra (§6).

---

## 1. Propósito

Medir, por activo y por hora, **cuánto se repite su nombre en fuentes públicas, en cuántas fuentes distintas y a qué velocidad crece**. Es un dato cuantitativo más para el scoring y el dossier, con el mismo protocolo que el resto: sombra, métrica dual, IC90 de Wilson y n ≥ 20.

**Relación con la capa narrativa (`lib_narrative`, Capítulo VII, doc 18):**
- la capa narrativa detecta **temas** con resolución **diaria** (Wikipedia Pageviews, GDELT; pico = 5× la mediana de 28 días con z robusto ≥ 3,5);
- esta métrica mide **un activo concreto** con resolución **horaria**.

Son complementarias. La capa temática sigue pesando 0 en el score.

---

## 2. Definición operativa

**Mención:** un ítem público con timestamp (post, artículo, mensaje de canal, hilo) que contiene un identificador del activo.

| Identificador | Ejemplo | Peso | Motivo |
|---|---|---|---|
| Mint / contrato exacto | `6BfTBNYJ…Zpump`, `0x…` | **1,0** | inequívoco; en memecoins circula como "CA: …" |
| Cashtag | `$VSOF` | 0,5 | ambiguo: hay colisiones de símbolo (`script_97` ya las registra) |
| Nombre | "Weird Cat" | 0,25 | solo para nombres de ≥ 2 palabras sin colisión en el acumulado |

**Ventanas y reglas de conteo:**
- Conteo en buckets de 5 min, en UTC.
- Ventana actual: la última hora completa. Baseline: las 24 h anteriores, sin incluir la ventana actual.
- **Deduplicación:** un mismo texto normalizado (minúsculas, sin URLs ni espacios repetidos, SHA-1) cuenta una vez por fuente. Así un mensaje reenviado 50 veces no se lee como 50 menciones.
- **Autores:** se guarda un hash con sal del autor, nunca el nombre ni el handle (privacidad). Sirve para medir diversidad de autores.

**Las tres componentes de la directiva:**
1. menciones por hora, `m_1h` (ponderadas por la tabla de arriba);
2. diversidad de fuentes, `S_1h` = fuentes distintas con ≥ 1 mención en la hora;
3. velocidad de crecimiento, `g` = cociente entre la hora actual y la anterior.

---

## 3. Fórmula

### 3.1 Fórmula de la directiva (v0)

```
intensity = (menciones_1h / menciones_promedio_24h) × (fuentes_distintas / fuentes_baseline)
```

- `menciones_promedio_24h` = media de menciones por hora en las 24 h previas;
- `fuentes_baseline` = media de fuentes distintas por hora en esas 24 h.

**Problemas de la v0** [V, cálculo]:
- **División por cero:** un token nuevo no tiene 24 h de historia, `m̄_24h = 0` e `intensity = ∞`.
- **Ruido de conteos chicos:** 2 menciones contra una media de 0,5 da 4×, pero con un proceso de Poisson de media 0,5 ver ≥ 2 en una hora tiene probabilidad 0,090. Pasa 1 de cada 11 horas por puro azar.
- **Una fuente dominante cuenta igual que varias parejas.**

### 3.2 Fórmula propuesta (v0.1) [H]

```
ratio      = (m_1h + α) / (m̄_24h + α)                      α = 1 (suavizado: sin ∞ y con menos ruido)
diversidad = S_eff,1h / max(1, S̄_eff,24h)                  S_eff = exp(H), H = entropía de Shannon del reparto por fuente
velocidad  = ((m_1h + α) / (m_prev1h + α)) ^ β              β = 0,5 (acompaña sin dominar)
intensity  = ratio × diversidad × velocidad
sorpresa   = −ln P(X ≥ m_1h | X ~ Poisson(λ)),  λ = max(m̄_24h, λ_min),  λ_min = 0,25
autores    = autores distintos / menciones de la hora       (< 0,3 → repetición concentrada en pocas cuentas)
```

- **`S_eff` en lugar del conteo de fuentes.** Con 24 menciones repartidas 12/6/4/2 entre 4 fuentes, S_eff = 3,32; con 21/1/1/1, S_eff = 1,67 [V]. Mide fuentes "efectivas", no fuentes con una mención suelta.
- **La sorpresa de Poisson** da significancia: separa el pico real del ruido de conteos chicos.

### 3.3 Ejemplos trabajados [V, cálculo]

| Caso | Datos | v0 directiva | v0.1 ratio | Sorpresa (p) | Lectura |
|---|---|---|---|---|---|
| A — token con historia | m_1h = 24, m̄_24h = 3, S_1h = 4, S̄ = 1,5, m_prev = 8 | **21,3** | 6,25 × div 2,67 × vel 1,67 = **27,8** | p = 2,6·10⁻¹⁴ (31,3 nats) | pico real |
| B — ruido | m_1h = 2, m̄_24h = 0,5 | **4,0** | 2,0 | p = 0,090 | no es pico (p ≥ 0,01) |
| C — token nuevo | m_1h = 6, sin historia | **∞** | 7,0 | p = 2,7·10⁻⁷ (λ_min = 0,25) | pico, sin división por cero |

(El 27,8 del caso A supone S̄_eff ≈ S̄ = 1,5 y S_eff,1h = 4; con el reparto 12/6/4/2, S_eff,1h = 3,32 y la intensidad baja a 23,1.)

---

## 4. Fuentes (gratuitas, sin key, sin cuentas)

Sonda del 01/10/2026 ~03:00 UTC desde IP local. **Desde Actions se verifica antes de depender** [P].

| Fuente | Endpoint | Estado [V] | Qué aporta | Límite |
|---|---|---|---|---|
| Reddit (RSS) | `https://www.reddit.com/r/<sub>/new/.rss` | **200**, Atom | posts nuevos por subreddit (r/solana, r/CryptoCurrency, r/CryptoMoonShots, r/SatoshiStreetBets, r/memecoins) | encabezados `x-ratelimit-*` (199 restantes por ventana en la sonda); 1 request cada ≥ 6 s por precaución [I] |
| Reddit (JSON anónimo) | `/r/<sub>/new.json` | **403** | — | bloqueado: no usar |
| Telegram, canales públicos | `https://t.me/s/<canal>` (vista web) | **200**, HTML; `robots.txt` responde 404 | mensajes recientes con timestamp. **El CA circula acá** | sin límite publicado; ≥ 5 min por canal [H]. **Sin Telethon / Pyrogram / pyrofork** (prohibidos) |
| 4chan /biz/ | `https://a.4cdn.org/biz/catalog.json` | **200**, JSON | hilos activos del tablero cripto; el CA aparece seguido | reglas de su API: ≤ 1 request/s y `If-Modified-Since` [I] |
| Noticias (RSS) | CoinDesk `/arc/outboundfeeds/rss/` · Cointelegraph `/rss` · Decrypt `/feed` · The Block `/rss.xml` | **200** las cuatro | cobertura de medios (útil para blue chips y narrativas; rara vez memecoins) | cada 15–30 min |
| GDELT DOC 2.0 | `api.gdeltproject.org/api/v2/doc/doc?mode=timelinevolraw` | **429**: "limit requests to one every 5 seconds" | volumen de noticias global cada 15 min | 1 request / 5 s; ya falló 2/2 en la capa narrativa (doc 18). Solo para Universos A/B |
| HN (Algolia) | `hn.algolia.com/api/v1/search_by_date` | **200**, JSON | atención técnica (L1/L2, infra) | generoso [I] |
| CoinGecko trending | `api.coingecko.com/api/v3/search/trending` | **200**, JSON | top de búsquedas de 24 h: atención, no menciones | ~1 request / 15 s sin key (doc 23) |
| Bluesky (búsqueda pública) | `public.api.bsky.app/xrpc/app.bsky.feed.searchPosts` | **403** | — | no disponible sin auth |
| X / Twitter | — | sin API gratuita | — | **fuera de alcance**: la única vía gratuita usa cookies de una cuenta (doc 25) |

**Sesgo de cobertura** [I]: X es donde más circulan las memecoins y no se mide. La métrica mide la repetición en las fuentes abiertas, y el dossier lo dice así.

**Presupuesto por corrida** (cada 20 min) [H]: 5 subreddits + ≤ 10 canales de Telegram + 1 catálogo de 4chan + 4 RSS de noticias ≈ 20 requests, ~2 min con pausas.

---

## 5. Integración al scoring v7.2.1 como bonus (por fases)

### Fase 0 — Registro en sombra, sin efecto en el score

- Nuevo `script_116_social_scan.py` (tentativo) en un workflow propio (`social_scan.yml`, cada 20 min, concurrency propia; commitea solo sus archivos). Consultar antes de crearlo.
- **Salida:**
  - `02_Analisis/social/mentions_<fecha>.jsonl`: una línea por mención con `ts`, `source`, `item_hash`, `author_hash`, `match` (`ca` / `cashtag` / `name`) y `token_key`. Sin textos ni handles.
  - `02_Analisis/social/_intensity.json`: por token, `m_1h`, `m̄_24h`, `S_eff`, `ratio`, `velocidad`, `intensity`, `sorpresa`, `autores` y `version: "rep-0.1"`.
- `script_82` **no cambia**. `script_113` (dossier) muestra el bloque como dato en 🔬 Método y ⏱️ Vigencia.

### Fase 1 — Medición (event study, a dos colas)

- Población: tokens con score ≥ 56 en sombra y, aparte, todos los que tengan DexScreener.
- Partición por tramo de intensidad al detectar (§7).
- Métrica dual por tramo, con IC90 de Wilson:
  - primaria y secundaria;
  - además, la tasa "después de +20%, llegar a ≤ −99%".
- **El signo es una pregunta empírica:**
  - la repetición alta puede anticipar la aceleración;
  - o puede marcar el final del movimiento. El histórico registra que después de tocar +20%, el 76% llegó a ≤ −99% (doc 21).
  - Se testean las dos direcciones.
- Controles:
  - **placebo** (timestamps desplazados al azar ±6–24 h, como `lib_narrative.placebo_days`);
  - **walk-forward** por semana;
  - **mínimo n ≥ 20 por tramo**.

### Fase 2 — Bonus en el score

Solo si la Fase 1 muestra un efecto con IC90 que no cruza el baseline del tramo bajo.

| Condición al detectar | Ajuste | Notas |
|---|---|---|
| `intensity ≥ 3` y `sorpresa ≥ 4,6 nats` (p ≤ 0,01) y `S_eff ≥ 2` y `autores ≥ 0,3` | **+5** | |
| ídem con `intensity ≥ 6` | **+10** | |
| ídem con `intensity ≥ 10` | **+15** | tope |
| Si la Fase 1 da efecto negativo | los mismos tramos con signo **−** | |

- El ajuste entra como componente nueva y registrada en `reasons` ("Repetición mediática: intensidad X, p = Y"), para que el desglose del dossier la reconstruya.
- Nuevo `scoring_version: "7.3-rep"` en sombra, con veredicto propio (n ≥ 20, criterios del doc 22 §1.1). v7.2.1 sigue intacto hasta que Dirección decida.

**Alternativa preferida para el largo plazo:** entrar como **evidencia en nats en `lib_fusion`**, con el mismo contrato que `script_112` y la capa narrativa:
- `LLR_rep = clip(ln(P(intensity | acierto) / P(intensity | fallo)), ±2)`, estimado con la muestra en sombra;
- la fusión lo pondera con las demás fuentes en lugar de sumar puntos fijos.

---

## 6. Umbrales iniciales (heurísticos, no calibrados)

| Parámetro | Valor inicial | Por qué |
|---|---|---|
| α (suavizado) | 1 | evita ∞ y amortigua conteos de 1–3 |
| λ_min (piso de Poisson) | 0,25 menciones/h | un token nuevo sin historia |
| β (peso de la velocidad) | 0,5 | la velocidad acompaña; no domina |
| Mínimo absoluto | `m_1h ≥ 5` | debajo, ningún ratio se lee |
| Pico significativo | sorpresa ≥ 4,6 nats (p ≤ 0,01) | |
| Diversidad mínima | `S_eff ≥ 2` | al menos dos fuentes efectivas |
| Diversidad de autores | ≥ 0,3 | debajo, repetición concentrada (raids, bots) |
| Tramos de intensidad | < 3 normal · 3–6 alta · 6–10 muy alta · ≥ 10 saturación | para el event study de la Fase 1 |

---

## 7. Límites y riesgos

- **Manipulación:** las campañas coordinadas inflan las menciones. Lo mitigan la deduplicación por texto, la diversidad de autores y `S_eff`. No se elimina.
- **Cobertura:** sin X ni Discord. La métrica es "repetición en fuentes abiertas".
- **IPs de Actions:** Reddit y GDELT pueden responder distinto que desde una IP residencial. Se verifica desde Actions antes de la Fase 0 [P].
- **Términos de uso:** solo endpoints públicos pensados para lectura (RSS, JSON públicos, vista web de canales públicos), con `robots.txt` y límites respetados. Sin cuentas ni cookies (doc 25).
- **Privacidad:** no se guardan textos ni autores; solo hashes con sal y conteos.

---

## 8. Pendientes

1. ~~Verificar desde Actions~~ **Hecho** (run `36818939038`): 5/6 familias, 12/17 endpoints; falla GDELT [V].
2. [P] Lista curada de canales públicos de Telegram y de subreddits, con criterio explícito (volumen, idioma, foco en Solana/Base). Dirección la valida.
3. ~~Parsers, deduplicación, `S_eff`, sorpresa de Poisson y casos A/B/C~~ → hechos en `lib_repetition.py` (15 tests, §9). ~~Falta el colector de la Fase 0~~ → `script_115` (§10).
4. [P] Fase 1 cuando haya ≥ 20 tokens por tramo.

---

## 9. Librería, sonda y sonda local (Fase 4)

**`lib_repetition.py`** (solo stdlib, sin red, **no conectada al pipeline**):
- parsers de RSS/Atom, vista web de Telegram, catálogo de 4chan, HN, CoinGecko trending y GDELT;
- coincidencia ponderada (contrato 1,0 · cashtag 0,5 · nombre 0,25) con deduplicación por fuente + texto normalizado;
- `effective_sources`, `poisson_log_sf` / `surprise` (estable en espacio log), `intensity_v0`, `intensity_v01`;
- `repetition_snapshot`: última hora contra las 24 previas.
- Los tests reproducen los números de §3.3 (21,3 · 27,8 · 31,3 nats · p = 0,090 · 2,7·10⁻⁷ · S_eff 3,32 / 1,67) [V].

**`probe_narrative_sources.py` + `probe_narrative_sources.yml`** (workflow manual, sin secretos):
- por endpoint registra estado, latencia, tamaño, encabezados de límite de tasa e **ítems parseados** con su antigüedad. Una fuente vale si responde 200 **y** trae ítems;
- guarda `02_Analisis/diagnostics/narrative_sources_probe.json` con historial de 20 corridas, para comparar IP local vs Actions;
- criterio: Fase 0 habilitada por la sonda si ≥ 3 familias de fuentes de menciones están OK.

**Sonda local** (01/10 ~04:30 UTC, IP residencial) [V]: **6/6 familias, 14/17 endpoints**.

| Familia | Resultado |
|---|---|
| Reddit RSS | 2/5 (las otras tres respondieron 429: Reddit limita el RSS anónimo por IP después de varias requests; pausa ahora de 10 s) |
| Telegram `t.me/s` | 4/4: `cointelegraph`, `WatcherGuru`, `whale_alert_io`, `pumpfun`. Otros canales (`solana`, `coindesk`, `dexscreener`, `solanafloor`) redirigen sin vista previa |
| 4chan /biz/ | 201 hilos |
| HN Algolia | OK |
| Noticias RSS | 4/4 |
| GDELT | OK en esta corrida (12,6 s; antes, 429) |
| CoinGecko trending | OK |

- **User-Agent:** con un User-Agent **no ASCII** ("investigación"), 4chan, Cointelegraph, Decrypt y The Block respondían **403**; con ASCII, 200 [V]. Queda fijado en ASCII, con un test que lo vigila.
- **Profundidad de los feeds:** el RSS de un subreddit trae 25 posts. En r/CryptoMoonShots eso cubrió ~17 h; en subreddits activos cubre menos. La vista de Telegram trae ~20 mensajes. **Un baseline de 24 h necesita un colector continuo**: una consulta en el momento de la alerta no alcanza.

**Fase 0, ubicación propuesta** (la directiva la deja a criterio del implementador):
- un **colector propio**: workflow cada 20 min, como los bots, con concurrency propia y commit solo de sus archivos. **No** dentro de `script_82` ni de `script_97`, para no sumar latencia ni puntos de falla a la emisión.
- **Por ítem guarda** los identificadores extraídos (direcciones base58 / `0x…` y cashtags encontrados), `ts`, fuente, hash del texto normalizado y hash con sal del autor. **Sin texto ni handles.**
- `script_97` / `script_113` solo **leen** el snapshot (`02_Analisis/narrative/<mint>.json`) y lo muestran en el dossier. El score no cambia.
- **Se habilita** cuando la sonda desde Actions dé ≥ 3 familias OK y Dirección apruebe el workflow nuevo.

---

## 10. Fase 0 implementada — `script_115_narrative_collector.py` (Fase 5, T1)

**Condición cumplida [V]:** la sonda desde Actions dio 5 familias de menciones OK (criterio: ≥ 3). Dirección aprobó el workflow nuevo (directiva Fase 5).

**Workflow** `narrative_collector.yml`: cada 20 min, en los minutos 7/27/47 (desfasado de `pipeline_t0`). Concurrency propia `ops-narrative_collector`, sin secretos y sin envíos. Commitea solo `02_Analisis/narrative/`. No toca `script_82`, `script_97` ni el score.

**Qué hace cada corrida**

1. **Candidatos.** Tokens de `shadow_v4/_accumulated.json` con **score ≥ 40**, puntuados en las últimas **48 h** y **con el scorer vigente**. La versión vigente es la del registro más reciente; hoy, 7.2.1.
   - Un token que entra se sigue 48 h desde su entrada, aunque después baje su score: la Fase 1 necesita la serie completa.
   - [V] Sin el filtro de versión entraban 59 tokens, 45 de ellos puntuados por v7.2 el 30/09 (los 100 inflados del doc 20). Con el filtro quedan **14**, entre ellos DEGEN y arc, las dos alertas reales del 01/10.
2. **Fuentes.** Las familias que la sonda marcó OK (`narrative_sources_probe.json`); sin sonda, todas.
   - GDELT queda fuera siempre: da volumen agregado de noticias, no menciones de un activo.
   - CoinGecko trending se guarda como dato de atención. Hay coincidencia solo si coinciden el símbolo **y** el nombre.
3. **Almacén rodante de 26 h** (`_items.json`). De cada ítem se guardan solo sus identificadores:
   - **qué contiene:** direcciones base58 (32–44 caracteres) y `0x…` en minúsculas, cashtags y nombres de los candidatos encontrados;
   - **cuándo y de dónde:** timestamp y fuente;
   - **huellas:** clave `fuente|sha1(texto normalizado)` (la misma deduplicación que `lib_repetition`) y hash con sal del autor;
   - **qué no:** **textos y handles**;
   - se guardan solo los ítems con al menos un identificador. Las direcciones y los cashtags se cuentan retroactivamente para un token que entra después; los nombres, solo mientras el ítem siga en el feed.
4. **Métrica por token.** `lib_repetition.repetition_snapshot` (v0.1 de §3.2) sobre las menciones del almacén, con los pesos de §2: contrato 1,0, cashtag 0,5, nombre 0,25.
   - Salida: `02_Analisis/narrative/<mint>.json` con la foto actual, la **primera foto** (≈ intensidad al detectar, para la Fase 1), el historial de 24 h, el desglose por fuente y por tipo de coincidencia, y el trending.
   - Además, `_index.json` con el estado de cada endpoint, las familias usadas y descartadas, el resumen por token y las últimas 72 corridas.

**Exclusiones de identificadores** (registradas por token en `identifiers.excluded`):
- **Cashtag:**
  - símbolo vacío, de 1 carácter o fuera de `[A-Za-z0-9]` (por ejemplo `C@T`);
  - o símbolo de la lista de majors, stablecoins y fiat (`$SOL`, `$USDC`, `$BTC`…): esas menciones casi nunca son del memecoin.
- **Nombre:**
  - de menos de 2 palabras;
  - o compartido por más de un token del acumulado.

**Límites [I]**
- El baseline arranca vacío: `baseline_coverage_h` dice cuántas horas de historia hay (tope 24). Hasta las 24 h, la intensidad sobreestima y la sorpresa usa λ_min.
- Los feeds traen ~20–25 ítems: lo que entra y sale entre dos corridas (20 min) se pierde.
- X y Discord no se miden (§4). Reddit desde Actions dio 1/5 en la sonda.
- Sal del hash de autor: `NARRATIVE_AUTHOR_SALT` si existe; si no, una sal fija pública. Es un seudónimo, no anonimato. No se guardan handles.

**Tests** (`test_script_115_collector.py`, sin red): 20/20.
- Cubren: paridad con `lib_repetition.match_weight`, el caso C de §3.3 reproducido, deduplicación, privacidad, la ventana de 48 h, el filtro de versión, las exclusiones, el tope por score, la corrida completa (escribe solo en `narrative/`, no modifica el acumulado, no consulta GDELT), la segunda corrida, el historial de 24 h, el comportamiento sin red y el dry-run.
- **Mutation testing: 10/10 mutaciones muertas.**

**Uso:** `python 04_Config/scripts/script_115_narrative_collector.py [--dry-run] [--families reddit_rss,4chan_biz] [--min-score 40] [--track-hours 48]`
