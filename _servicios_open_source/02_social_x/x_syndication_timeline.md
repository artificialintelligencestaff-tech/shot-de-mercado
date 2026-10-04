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
**Recomendación:** P1. Bot `bot_x_accounts` o receta nueva `kind: x_timeline` en bot_runner, con una lista de cuentas en YAML. Empezar por las cuentas oficiales de los activos `confirmado` del calendario.
