# ICO Drops — calendario de ventas, TGE y distribuciones

**Repo:** no aplica (sitio). https://icodrops.com
**Licencia:** términos del sitio; datos públicos sin licencia abierta [I].
**Gratis:** sí, sin cuenta ni key [V] (2026-10-04, D-087):
- `GET https://icodrops.com/` → 200, 250 KB de HTML, sin Cloudflare.
- `GET https://icodrops.com/category/upcoming-ico/` → 200, 231 KB.
**Requisitos:** `requests` y `re` o bs4 (las tarjetas tienen clases estables: nombre, etapa, monto recaudado, categoría).
**Tipo de dato:** proyectos con etapa — en la portada de hoy: `Upcoming` 52, `Active` 45, `TGE and Distribution` 40, `Token Sale` 3, `Funding Round` 1 [V] — más monto recaudado ("$15 M"), categoría y página por proyecto.
**Utilidad para pre-lanzamiento o anticipación:**
- Es la **fuente con más cobertura de activos no nacidos** de esta tanda: unos 90 en `Upcoming` y `TGE and Distribution`, frente a 0 próximas en el calendario de CMC [V].
- La etapa `TGE and Distribution` marca un nacimiento inminente: es el candidato natural a `token_anunciado` en el calendario de D-079 [I].
- El monto recaudado sirve para priorizar: una ronda de $15 M con TGE próximo pesa más que una preventa sin fondos [H].
**Riesgos técnicos:** HTML sin API: un rediseño rompe el parser. Fechas exactas solo en la página de cada proyecto (1 request por proyecto) [I]. Sin contrato hasta el TGE (match por nombre y símbolo, como en el calendario).
**Recomendación:** P1. Octava fuente de `bot_prelaunch_calendar` (cada 6 h, solo `Upcoming` y `TGE and Distribution`, con página de detalle solo para los nuevos), con match por nombre y símbolo y el mismo umbral de ≥ 2 fuentes para `confirmado`.
