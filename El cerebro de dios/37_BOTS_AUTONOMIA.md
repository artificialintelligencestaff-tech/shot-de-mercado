---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: DISEÑO — D-091 T3 (sin implementar)
last_updated: 2026-10-04
version: 0.1
complementa: doc 34 (sistema multibot, §5 config, §11 self_repair, §14 audit_gate, §17 patrimonio, §18 X), doc 36 (método científico)
---

# 37 — Bots de autonomía — diseño

Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente.

## 0. Para qué (principio 6)

**El proyecto tiene que poder seguir sin el proceso que lo creó.** Hoy, una persona (Dirección/YANG) o un implementador (Claude) hace cuatro trabajos a mano en cada directiva:

1. Busca servicios nuevos (D-055, D-087 T2): probar endpoints, leer licencias, escribir fichas.
2. Mide qué fuente sirve (D-089-R, D-091): frescura, aporte y "sin aporte ≠ sin valor".
3. Integra lo que sirve (D-067, D-089-R T4): receta YAML o código, tests y estado.
4. Audita lo que cambió (audit_gate, revisiones de YIN): prohibidos, gitlinks, secretos, rutas.

Los cuatro bots de este documento hacen mañana esos trabajos, con **una sola decisión humana en el circuito: Yang aprueba o rechaza una propuesta**. Ningún bot activa, borra ni apaga nada por su cuenta (D-089-R: los umbrales son señales).

```
                 ┌──────────────┐  candidatos   ┌───────────────┐  propuesta alta/baja  ┌────────────────┐
  GitHub, RSS,   │  bot_scout   │──────────────▶│ bot_evaluator │──────────────────────▶│ bot_integrator │
  APIs abiertas ▶│ (descubre)   │  fichas borr. │ (mide aporte) │  métricas por fuente  │ (receta YAML)  │
                 └──────────────┘               └───────────────┘                       └───────┬────────┘
                                                        ▲ diarios src-1, eventos,               │ propuesta lista
                                                        │ alertas y resultados                  ▼
                                                ┌───────┴────────┐  hallazgos   ┌──────────────────────────┐
                                                │  bot_auditor   │◀─────────────│ Yang: aprobaciones.yaml  │
                                                │ (audita todo)  │──────────────▶ aprueba / rechaza (único  │
                                                └────────────────┘  escalaciones│ paso humano)             │
                                                                                └──────────────────────────┘
```

## 1. Reglas comunes

- **Cero IA generativa en producción** (doc 34). Todo es determinista: regex, umbrales [H], pruebas HTTP y estadística (lib_scientific_method). Un bot no "entiende" un servicio: lo prueba.
- **Un dueño por archivo y commits con rutas explícitas.** Cada bot commitea solo su carpeta, con `pull --rebase` y 4 reintentos, como los bots de fuentes. Nunca hace `git add -A` sin ruta.
- **Nada se activa sin aprobación.** La única vía de activación es una aprobación de Yang en `04_Config/autonomia/aprobaciones.yaml`, un archivo que solo edita Yang (`{id, decision: aprobar|rechazar, motivo, fecha}`).
  - Hoy `bot_genesis` habilita solo toda receta de ficha que pasa la validación [V doc 34]. Por eso **ningún bot de autonomía escribe un bloque `recipe:` en una ficha** hasta que haya una aprobación.
- **Las bajas tampoco son automáticas.** El evaluador propone; Yang decide. La única acción automática que sigue existiendo es el apagado temporal por fallas HTTP (self_repair, 6 h), que se reintenta solo.
- **100% gratis:** solo GET públicos, `GITHUB_TOKEN` del propio workflow y ningún secret nuevo. Un servicio que pide key queda como candidato con nota "requiere cuenta" (decide Dirección).
- **Salidas:**
  - Todas en `02_Analisis/autonomia/<bot>/`, una entrada nueva del inventario de patrimonio (§17 doc 34) que se anota cuando se implemente.
  - Los eventos van por lib_events, con tipos nuevos que hay que sumar a la lista cerrada `TYPES`: `fuente_candidata`, `fuente_evaluada`, `propuesta_lista`, `auditoria_hallazgo`.
  - Los episodios van por lib_episodic_memory.
- **Registro:** los cuatro se registran en `04_Config/sources/_bots.yaml`, así el orquestador y self_repair los vigilan como a cualquier bot.

## 2. bot_scout — descubre servicios nuevos

**Propósito.** Encontrar servicios gratuitos que el proyecto todavía no usa y dejarlos como **candidatos** con evidencia probada (HTTP, licencia, actividad), para que el evaluador y Yang no partan de cero. Reemplaza la búsqueda manual de D-055 y D-087 T2.

**Entradas:**
- **GitHub Search API** (`GET /search/repositories`): por topics (`solana`, `defi`, `depin`, `rwa`, `memecoin`, `onchain-data`, `crypto-api`, `mcp-server` + `crypto`), con `pushed:>` hace 180 días, ordenados por estrellas.
- **Feeds RSS de releases y awesome-lists:** `releases.atom` de los repos de servicios ya instalados, porque un endpoint nuevo de un proveedor conocido es el candidato más barato de probar. También los commits de listas curadas, como `public-apis/public-apis`.
- **APIs abiertas conocidas:** índices de endpoints de proveedores ya verificados (DexPaprika `/networks`, GeckoTerminal), para detectar redes o rutas nuevas.
- **Lo que ya existe, para no repetir:** fichas en `_servicios_open_source/*/`, `_PENDIENTES.md` (incluye los descartados con motivo) y `04_Config/inventario.json`.

**Salidas** (dueño: scout):
- `02_Analisis/autonomia/scout/_candidatos.jsonl`: una línea por candidato con `{id, fuente, url, repo, licencia, estrellas, ultimo_push, archivado, keywords, endpoints_probados: [{url, status, bytes, json, cloudflare}], requiere_key, puntaje [H], motivo}`.
- `_servicios_open_source/_candidatos/<id>.md`: ficha **borrador** en el formato de la casa, **sin bloque `recipe:`**.
  - Lo que impide que `bot_genesis` la active es justamente esa falta de bloque. La carpeta con `_` no alcanza: `fichas()` recorre `*/*.md` y solo saltea los **archivos** que empiezan con `_` [V código].
  - El auditor verifica que ningún archivo de `_candidatos/` tenga un bloque `recipe:` (§5).
- `_scout_state.json`: repos y URLs ya vistos (dedup, 180 días) y el cupo de la API usado.
- Evento `fuente_candidata` (subject = id del candidato) para el evaluador.

**Algoritmo:**
1. Buscar y filtrar: licencia en `{MIT, Apache-2.0, BSD-2/3, ISC, MPL-2.0}`, no archivado, push < 180 días, ≥ N estrellas [H].
2. Puntuar por keywords del README y la descripción, contra `keywords.yaml` grupos a–i y el vocabulario de fuentes ("api", "free", "no key", "rss", "websocket").
3. Para los mejores K por corrida, probar los endpoints que aparezcan en el README: GET sin key, guardando estado, tipo de contenido, tamaño, si es JSON y si hay challenge de Cloudflare. Es la misma prueba que hice a mano en D-087 T2.

**Dependencias:** `requests`, `GITHUB_TOKEN` del workflow, `lib_events`, `lib_sources_store` (`load_keywords`) y el parser de fichas de `bot_genesis` (`fichas()`, para el dedup).

**Límites reales:**
- **GitHub Search:** 30 requests/min autenticado y como máximo 1.000 resultados por consulta. Con `GITHUB_TOKEN`, 1.000 requests/h por repositorio [I, documentación de GitHub]. Alcanza para ~20 consultas por día con margen.
- **No puede leer términos de servicio ni juzgar utilidad:** sin IA, "sirve para anticipar" no se infiere de un README. El scout solo deja evidencia; la utilidad la mide el evaluador con datos.
- **Probar un endpoint no prueba que sea estable:** un 200 hoy puede ser 429 mañana (como syndication, D-087). Se reprueba en la evaluación.
- **Ruido:** la búsqueda por topics trae bots de trading, wrappers vacíos y forks. El puntaje [H] se calibra con lo que Yang aprueba o rechaza (su historial es la etiqueta).
- **Fuera de alcance:** servicios sin repo ni feed (portales como ICO Drops) solo aparecen si alguna lista curada los nombra.

**Cadencia:** diaria, de madrugada, con concurrency propia.

## 3. bot_evaluator — mide el aporte real por fuente

**Propósito.** Calificar cada fuente activa y cada candidato por su **aporte al fin** (señal actual sobre activo vigente, D-089-R), no por su fecha ni por su volumen. Con eso propone altas y bajas, que decide Yang. Generaliza a todas las fuentes la evaluación de D-089-R/D-091, que hoy existe solo para X.

**Entradas:**
- **Diarios src-1 de 30 días** de todos los bots (`02_Analisis/sources/*/<fecha>*.jsonl`): rss, telegram a/b, recetas del runner, x_influencers. El almacén fusionado (`_merged.jsonl`) cubre solo 48 h y no alcanza.
- **Activos vigentes** de `bot_influencer_tracker.vigentes()`: calendario, alertas de 30 días, multichain, perps HL y early watch. Se mueve a una biblioteca común `lib_vigentes`.
- **Resultados:** `02_Analisis/alerts/_all_alerts.json` (alertas con trust y resultado), eventos `alerta_emitida`, `resultado_medido` y `prelaunch_nacido`, y el calendario de preventa.
- **Salud:** `_state.json` de cada bot (estado HTTP, fallas) y `_health.json` del orquestador.
- **Candidatos:** muestras en sombra de las propuestas del integrador (§4).

**Métricas por fuente** (fuente = feed, canal, receta o cuenta de X), todas [H] hasta calibrar:

| Métrica | Definición | Desde |
|---|---|---|
| `frescura` | 1.0 / 0.5 / 0.2 según la edad del último ítem (< 7 d, 7–30 d, > 30 d) | D-089-R |
| `aporte` | ítems de 30 d con `calculate_aporte > 0`: los 5 tipos de D-091. En fuentes sin `m.sg` se usan `c`, `a`, `k` y título | D-091 |
| `novedad` | ítems cuyo activo esa fuente nombró **primero**, ≥ 1 h antes que cualquier otra (lead-lag por activo) | nuevo |
| `anticipacion` | menciones de un activo antes de su alerta (`alerta_emitida`) o de su nacimiento (`prelaunch_nacido`), comparadas con una línea base por permutación (lib_scientific_method, test exacto como en D-058) | nuevo |
| `redundancia` | fracción de ítems cuyo activo y hora ya trajo otra fuente | nuevo |
| `salud` | días con estado 200 / días consultados | doc 34 §8 |

**Salidas** (dueño: evaluator):
- `02_Analisis/autonomia/evaluator/_evaluacion.json`, por fuente: `{metricas, ventana, n_items, decision_sugerida: mantener|alta|baja|revisar, motivo, evidencia}`. Las bajas sugeridas llevan siempre el detalle: qué faltó y durante cuánto tiempo.
- Una línea por semana en `_evaluacion_log.jsonl`, y `_evaluacion_semanal.md` para Yang, con el mismo formato que `_evaluar_semanal.md` de X.
- Evento `fuente_evaluada`.
- Hipótesis en el registro de lib_scientific_method ("la fuente F anticipa alertas"), con el veredicto del debate adversarial (lib_adversarial_debate): una propuesta de alta o baja pasa por el debate antes de llegar a Yang.

**Dependencias:** `lib_sources_store` (lectura de diarios), `lib_vigentes`, `lib_scientific_method`, `lib_adversarial_debate`, `lib_events` y `lib_episodic_memory`.

**Límites reales:**
- **Muestra:** se necesitan ≥ 30 días de diarios para juzgar una fuente. Una fuente nueva queda en `revisar` hasta tenerlos. Con n chico, el test exacto da `insuficiente`, que es un resultado válido (D-058).
- **Sesgo de selección:** solo se mide lo que el sistema ya sigue. Una fuente que anticipa activos que nunca entran al universo vigente sale con aporte 0, el mismo caso "sin aporte ≠ sin valor" de D-089-R. Por eso `novedad` y `anticipacion` son métricas aparte, y nunca hay bajas automáticas.
- **Texto no guardado:** las fuentes src-1 viejas no tienen `m.sg` ni extracto, así que su aporte se mide solo con cashtags, direcciones y keywords, y queda subestimado. X sí guarda extracto desde D-089-R.
- **Causalidad:** anticipar una alerta no significa causarla. La métrica es lead-lag, no efecto.
- **Costo:** leer 30 días de diarios de todos los bots son decenas de MB por corrida, y está bien una vez por semana.

**Cadencia:** métricas diarias (baratas) y propuestas semanales.

## 4. bot_integrator — de la propuesta a la receta, sin activar

**Propósito.** Convertir un candidato del scout, o un alta sugerida por el evaluador, en una **receta YAML validada y lista para aprobar**, y aplicar solo lo que Yang aprobó. Reemplaza el trabajo manual de D-067 T5 y D-089-R T4 en los casos que se resuelven con configuración.

**Entradas:**
- `_candidatos.jsonl` del scout (con `endpoints_probados`) y `_evaluacion.json` del evaluador (altas y bajas sugeridas).
- El esquema de recetas de `bot_runner` (`validate_recipe`, kinds `rss`, `html_list`, `json_api`, `telegram_preview`) y `04_Config/recipes/README.md`.
- `04_Config/autonomia/aprobaciones.yaml`, escrito por Yang.

**Salidas** (dueño: integrator):
- `02_Analisis/autonomia/integrator/propuestas/<id>.yaml`: receta propuesta, con la cabecera `PROPUESTA — no la lee bot_runner`, su origen (candidato o evaluación), la validación (esquema, dominio no duplicado, fetch en seco, ≥ 5 ítems, como en `bot_genesis`) y una **muestra en sombra**.
  - La muestra en sombra son los ítems de 3 fetch en seco en días distintos, con las métricas que el evaluador necesita: frescura, aporte contra vigentes y solapamiento con otras fuentes.
  - **No entra al almacén de fuentes**, así que no toca scorers.
- `_propuestas.json`, con el estado de cada propuesta: `borrador → validada → en_sombra → lista → aprobada|rechazada → aplicada`.
- **Al aprobarse,** el integrador agrega el bloque `recipe:` a la ficha correspondiente. Si es un candidato del scout, primero mueve la ficha de `_candidatos/` a su categoría. Desde ahí, `bot_genesis` la valida y la habilita como siempre.
  - Las bajas aprobadas ponen `enabled: false` en la receta o en el YAML de la fuente. No se borra la ficha: queda como descartada con su motivo en `_PENDIENTES.md`.
- Evento `propuesta_lista` (subject = id) para el reporte de Yang.

**Dependencias:** `bot_runner` (validación y fetch en seco), las funciones de validación de `bot_genesis`, `lib_vigentes`, `lib_events` y el YAML de aprobaciones.

**Límites reales:**
- **Solo configuración:** si una fuente no entra en los 4 kinds del runner, el integrador lo marca `requiere_codigo` y no avanza. Pasa con un WebSocket, un JSON embebido en `__NEXT_DATA__` con lógica, o una página de detalle por ítem como ICO Drops. El código lo escribe un implementador con directiva.
- **Inferir selectores no es confiable:** para `json_api` se puede proponer el JSONPath del primer array de objetos con campos de fecha e id; para `html_list`, los selectores CSS solo salen con una plantilla conocida (Discourse, phpBB, WordPress). Sin plantilla: `requiere_revision`.
- **No crea secrets ni workflows:** una receta con `{secreto}` queda `requiere_secret` hasta que Dirección lo cargue, igual que helius en probation [V doc 34].
- **No modifica fuentes de producción del pipeline** (script_97, 116, 114): esas fuentes no son recetas.

**Cadencia:** diaria, después del scout. La aplicación de aprobaciones corre en la misma corrida.

## 5. bot_auditor — audita lo que cambian los otros bots

**Propósito.** Que cada commit al repo, de bots o de personas, cumpla las reglas del proyecto. Hoy `audit_gate` corre **solo en pull requests** (doc 34 §14), pero los bots pushean directo a `main`, y esos commits no los audita nadie.

**Entradas:**
- Los commits nuevos de `main` desde el último SHA auditado (`git log --raw` y `git diff`).
- El mapa de dueños:
  - las rutas que commitea cada workflow, leídas de sus pasos `git add -- <ruta>`;
  - `_bots.yaml`;
  - el campo `dueno` del inventario de patrimonio (§17).
- Las reglas de `audit_gate` (`PROHIBITED`, patrones de secretos, `TELEGRAM_CHAT_ID`) y `04_Config/autonomia/dominios.yaml`: qué secrets puede referenciar cada workflow.

**Reglas que revisa:**

| Regla | Detecta | Antecedente |
|---|---|---|
| Gitlinks | entradas con modo `160000` en `git diff --raw`, porque un submódulo huérfano rompe el checkout | `bfa6907d` agregó el gitlink `toolsresearch/nkd077_research`; `48c79901` lo removió [V] |
| Fuera de dominio | un commit de bot que toca rutas fuera de las suyas, según el mapa de dueños | un dueño por archivo (doc 34) |
| `git add -A` sin ruta | en workflows nuevos o modificados | hoy lo usan `pipeline_t0.yml:81` y `trust_update.yml:68` (heredados) [V]; los demás usan `git add -A -- <ruta>` |
| Prohibidos | `--force`, `reset --hard`, `TELEGRAM_CHAT_ID` en código, `.env` | audit_gate |
| Secretos fuera de dominio | un workflow que referencia un secret que no le corresponde, o un valor con forma de secreto en el diff | dominios hoy [V]: `TELEGRAM_OPS_CHAT_ID` solo en bots de sistema; `TELEGRAM_PUBLIC_CHAT_ID` en early watch, pipeline y trust; `HELIUS_API_KEY` en runner, genesis y pipeline |
| Doc 35 | hashes del inventario contra el blob | audit_gate doc35 |
| Patrimonio | carpeta nueva de primer nivel en `02_Analisis/` sin entrada | lib_patrimonio |
| Tamaño | un archivo de más de 5 MB o un diario que crece > 10× su mediana [H] | — |
| Rutas de los bots de autonomía | integrator escribiendo `recipe:` sin una aprobación con su id, o un bloque `recipe:` en `_candidatos/` | §1, §2 |

**Salidas** (dueño: auditor):
- `02_Analisis/autonomia/auditor/_auditoria.jsonl`: una línea por commit, con `{sha, autor, workflow, reglas_ok, hallazgos: [{regla, ruta, detalle, severidad}]}`.
- `_auditor_state.json` (último SHA auditado).
- Evento `auditoria_hallazgo` (severidad 2–3) para los hallazgos.
- Escalación por el mecanismo de self_repair (bloque en `_INSTALADOS.md`). Los de severidad 3 (gitlink, secreto) van además por el canal de ops que ya usan los bots de sistema.

**Prevención, no solo registro:** el auditor viene con una biblioteca `lib_guard.check_staged()` que cada workflow de bot llama justo antes de `git commit`. Aplica las mismas reglas al diff staged y aborta el push si encuentra un gitlink, un secreto o una ruta fuera de dominio. Es la única forma de **frenar** un commit directo a `main` sin protección de rama.

**Dependencias:** `git` (en el checkout del workflow, con `fetch-depth` suficiente para el rango a auditar), `audit_gate` (reglas reutilizadas), `lib_patrimonio`, `_bots.yaml`, `lib_events` y self_repair (escalación).

**Límites reales:**
- **Post-hoc:** sobre lo que ya entró a `main`, el auditor solo registra y escala. No revierte nada: revertir es una decisión humana, y `--force` está prohibido. Frenar antes de entrar exige `lib_guard` en cada workflow, o protección de rama, que es [P] de Dirección (doc 34 §14).
- **Secretos por patrón:** detecta formatos conocidos (tokens de Telegram, GitHub, AWS, claves privadas). Un secreto sin forma reconocible pasa (falso negativo).
- **Mapa de dueños incompleto:** los workflows heredados con `git add -A` (`pipeline_t0`, `trust_update`) no declaran sus rutas. Para ellos, "fuera de dominio" se aproxima con el inventario de patrimonio y se marca [I].
- **No audita lo que pasa fuera del repo:** mensajes de Telegram, APIs externas o secrets cargados en GitHub. Solo lo que queda en commits.

**Cadencia:** cada 15 min (cron) sobre los commits nuevos, más `lib_guard` en cada push de bot.

## 6. Orden de implementación y archivos

| Orden | Pieza | Por qué primero |
|---|---|---|
| 1 | `lib_guard` + bot_auditor | frena gitlinks y secretos ya, y protege a los otros tres bots mientras se construyen |
| 2 | `lib_vigentes` (se extrae de `bot_influencer_tracker`) + bot_evaluator | con 30 días de diarios ya hay datos para medir las fuentes actuales |
| 3 | bot_integrator (propuestas + muestras en sombra + `aprobaciones.yaml`) | cierra el circuito con Yang |
| 4 | bot_scout | sin integrador ni evaluador, los candidatos se acumulan sin destino |

**Archivos nuevos** (un dueño por archivo):
- `04_Config/autonomia/aprobaciones.yaml` (Yang) y `dominios.yaml` (Dirección);
- `02_Analisis/autonomia/{scout,evaluator,integrator,auditor}/` (un bot cada una);
- `_servicios_open_source/_candidatos/` (scout);
- workflows `autonomia_scout.yml`, `autonomia_evaluator.yml`, `autonomia_integrator.yml` y `autonomia_auditor.yml`, cada uno con su concurrency y sus rutas explícitas.

**Antes de implementar, [P] Dirección:**
1. Confirmar que Yang es quien escribe `aprobaciones.yaml`, y si una aprobación necesita una segunda firma.
2. Definir `dominios.yaml`: qué secrets corresponden a cada workflow.
3. Decidir si `lib_guard` entra también a los workflows de producción heredados (`pipeline_t0`, `trust_update`), que hoy usan `git add -A`. Tocarlos es cambiar producción.
4. Protección de rama en `main` exigiendo los checks de `audit_gate` (pendiente desde D-067).
