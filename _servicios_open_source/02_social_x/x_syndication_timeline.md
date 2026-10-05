# X — timeline de syndication (widget de inserción), sin login

**Repo:** no hay cliente oficial: es el endpoint público que usa el widget de inserción de X. Referencia de uso: https://github.com/vercel/react-tweet (MIT) usa la misma familia de endpoints (`syndication`).
**Licencia:** n/a (endpoint del servicio). El parser es propio (repo del proyecto).
**Gratis:** sí, sin cuenta, sin cookies y sin key [V]. `GET https://syndication.twitter.com/srv/timeline-profile/screen-name/<cuenta>` → 200, unos 130 KB de HTML con `__NEXT_DATA__` (2026-10-03).
**Requisitos:** `requests` y `json`/`re` (el JSON va embebido en `<script id="__NEXT_DATA__">`). Sin bs4.
**Qué hace:** devuelve las ~20 publicaciones más recientes de una cuenta, con `id_str`, `created_at` y texto completo, incluidos los reposts [V].
- Prueba real con `solana`: 20 entradas y la más nueva era del mismo día (2026-10-03 12:00 UTC).
- Es por cuenta: **no hay búsqueda**. No sirve para "quién menciona $XYZ", sí para "qué publicó esta cuenta".
**Por qué sirve al proyecto:**
- Monitorear las cuentas oficiales de los activos del calendario de preventa (D-079): anuncios de TGE, contrato, fecha de listing. Es la fuente más directa de "nacimiento declarado". [I]
- Lista de cuentas de alta señal (proyectos, launchpads, exchanges): por cada cuenta, 1 request cada 30–60 min. [I]
- El texto se usa para extraer direcciones, cashtags y keywords y no se guarda (src-1). [V convención]
**Riesgos técnicos:** endpoint no documentado; X lo cambió en 2023 y puede volver a cambiarlo [I]. Ritmo prudente: ≤ 1 request/s y caché por cuenta [I].
**Medición D-087 (2026-10-04) [V]:**
- **Límite:** cabeceras `x-rate-limit-limit: 30`, ventana de 15 min (`x-rate-limit-reset`), por cliente. Agotado → 429 con cuerpo `Rate limit exceeded`. Alcanza para 30 cuentas cada 15 min, no para 50 cada 30 min.
- **Frescura desigual:** de 8 cuentas probadas, 2 frescas (`solana`, `binance`: 20 posts de las últimas horas), 1 a medias (`whale_alert`), 3 **congeladas** (`cobie`, `lookonchain`, `zachxbt`: ~100 entradas, la más nueva de hace ~330 días) y 3 vacías (`aeyakovenko`, `pumpdotfun`, `spotonchain`). Variantes de URL (`showReplies`, mayúsculas) no cambian el resultado.
- La ficha decía "las ~20 más recientes": vale solo para algunas cuentas (orgs verificadas, al parecer [I]).
**Recomendación:** P1 como **respaldo**. `bot_influencer_tracker` (D-087) usa FxEmbed `/2/profile/<cuenta>/statuses` como mecanismo primario (fresco para casi todas las cuentas activas, ver `fxembed_api.md`) y syndication solo si FxEmbed falla o trae lo viejo, con cupo por corrida y respeto de `x-rate-limit-remaining`.

## Variante por publicación: `tweet-result` (react-tweet) — fusionada en D-101

Misma familia de endpoints (syndication), otra forma de uso: una publicación por id en lugar del timeline de una
cuenta. Antes era la ficha `react_tweet_syndication.md`.

**Repo:** https://github.com/vercel/react-tweet
**Licencia:** MIT [V] (GitHub: 1.883 estrellas, push 2026-09-24)
**Gratis:** sí, sin cuenta ni key [V]. `GET https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=<t>&lang=en` → 200 (2026-10-03), con `created_at`, `favorite_count`, `conversation_count` y el autor.
**Requisitos:** `requests`. El `token` se calcula del id, sin secretos: `((id / 1e15) · π)` en base 36, sin ceros ni punto, igual que `getToken` de react-tweet [V: probado con un id real].
**Qué hace:** el JSON de una publicación individual, el mismo que usan las inserciones de Vercel/Next.js. Es una sola publicación por id [V].
**Por qué sirve al proyecto:**
- Respaldo de FxEmbed para las métricas de una publicación: si una de las dos fuentes cae, la otra sigue. [I]
- Viene directo de la CDN de X, sin intermediarios. [V host]
**Riesgos técnicos:** endpoint no documentado; si X cambia la fórmula del token, react-tweet se actualiza (repo activo) y basta copiar el cambio [I].
**Recomendación:** P2. Respaldo de `fxembed_api.md` para las métricas por publicación. Implementación de unas 15 líneas (token + GET), sin dependencia de Node.
