# FxEmbed (fxtwitter) — API pública de perfil y publicación, sin login

**Repo:** https://github.com/FxEmbed/FxEmbed
**Licencia:** MIT [V] (GitHub: 5.650 estrellas, push 2026-10-04, no archivado)
**Gratis:** sí, sin cuenta ni key [V] (2026-10-03):
- `GET https://api.fxtwitter.com/<cuenta>` → 200 con `followers`, `following`, `likes`, `media_count`, `tweets`, fecha de alta;
- `GET https://api.fxtwitter.com/status/<id>` → 200 con `created_at`, `likes`, `retweets`, `replies`, `views` y texto.
- `GET https://api.fxtwitter.com/2/profile/<cuenta>/statuses` → 200 con las ~20 publicaciones más recientes (`id`, `created_timestamp`, texto con URLs ya expandidas, `likes`, `reposts`, `replies`, `views`, `reposted_by`) y `cursor` [V, 2026-10-04, D-087].
**Requisitos:** `requests`. Se puede autohospedar: Cloudflare Workers, MIT.
**Qué hace:** proxy que normaliza datos públicos de X en JSON: perfil de una cuenta, métricas de una publicación puntual y **timeline de una cuenta** (`/2/profile/<cuenta>/statuses`) [V]. No hay búsqueda.
**Timeline medido (D-087, 2026-10-04) [V]:** fresco donde syndication está congelado — `lookonchain` 20 posts (el más nuevo de hace 4 h; syndication: 330 días), `arkham`, `toly`, `mert`, `EmberCN`, `binance`: el más nuevo de hace menos de 1 día. Handle inexistente o renombrado → 404 (perfil y timeline). En ~120 requests a 1/s no apareció ninguna cabecera de límite ni un 429.
**Por qué sirve al proyecto:**
- **Crecimiento de seguidores** de la cuenta oficial de un activo no nacido, tomado cada 6 h: una aceleración antes del TGE es una señal medible para el método del doc 36. [H]
- **Tracción de una publicación concreta** (vistas, reposts) para las publicaciones que trae el timeline de syndication (ficha hermana): permite separar un anuncio con eco de uno ignorado. [H]
- Combina con `x_syndication_timeline.md`: el timeline da los ids y FxEmbed, las métricas.
**Riesgos técnicos:** es un servicio de terceros y gratuito, sin SLA publicado [I]. Si cae, se puede autohospedar con el mismo código (MIT) [V licencia].
**Recomendación:** P0 para el timeline: mecanismo primario de `bot_influencer_tracker` (D-087). P1 para el resto: snapshots de perfil cada 6 h para las cuentas del calendario de preventa (`02_Analisis/prelaunch/`) y métricas por publicación para las de alta señal. Serie de seguidores en `m` (src-1, sin texto).
