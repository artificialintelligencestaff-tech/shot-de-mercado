# requests-cache — caché HTTP persistente

**Repo:** https://github.com/requests-cache/requests-cache
**Licencia:** BSD-2-Clause [V] (GitHub, push 2026-10-02)
**Gratis:** sí, local.
**Requisitos:** `requests-cache` 1.3.3 (PyPI, 2026-07-03). Depende de `attrs`, `cattrs`, `platformdirs`, `url-normalize` y `urllib3` [V]: 5 dependencias transitivas, a pinear con hashes.
**Qué hace:** reemplaza `requests.Session` por `CachedSession`. Guarda las respuestas en SQLite, filesystem o Redis, con expiración por URL o patrón, respeta `Cache-Control` y `ETag` y permite modo `stale_if_error` (sirve lo cacheado si la API falla).
**Por qué sirve al proyecto:**
- Varias rutas consultan el mismo contrato muchas veces por hora (RugCheck, GoPlus, DexScreener por token). Con caché de 5–30 min se recortan los requests sin perder frescura útil. [I]
- `stale_if_error` es tolerancia a fallos (patrón #20): si una API da 5xx, el bot sigue con el último dato y lo marca en `_health.json`. [I]
- Con `actions/cache` la base SQLite sobrevive entre corridas del mismo workflow. [I]
**Riesgos técnicos:** cachear lo que debe ser fresco (precio del early watch) rompe la detección. Hay que cachear por patrón de URL y nunca las rutas de velas o precio. [I]
**Recomendación:** P2. Integrarlo primero en el enriquecimiento de candidatos (seguridad del contrato y metadata), que cambia lento, con TTL de 6 h. No usarlo en el scorer ni en velas.
