# react-tweet (Vercel) — endpoint `tweet-result` de syndication, sin login

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
