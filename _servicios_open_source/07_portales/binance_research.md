# Binance Research — informes de proyectos y sectores

**Repo:** no aplica (servicio). https://research.binance.com
**Licencia:** términos de Binance [I].
**Gratis:** el contenido es público, pero **el acceso sin navegador está bloqueado** (2026-10-04, D-087):
- `GET https://research.binance.com/en/analysis` → **202 con cuerpo vacío**: challenge de AWS WAF [V].
- `GET https://research.binance.com/en/rss.xml` y `https://www.binance.com/en/research/analysis` → igual, 202 vacío [V].
- Antecedente: el CMS de anuncios de Binance (fuente del calendario, D-079) responde **451** desde los runners de EE. UU. [V, doc 34 §15].
**Requisitos:** navegador real (JavaScript del WAF). Queda fuera de las reglas (no se sortean controles anti-bot).
**Tipo de dato:** informes de proyectos antes y después del listing, informes de sector y resúmenes mensuales [I].
**Utilidad para pre-lanzamiento o anticipación:** un informe de Binance Research sobre un proyecto suele preceder o acompañar su listing en Binance [I]. Hoy no es accesible.
**Riesgos técnicos:** bloqueo activo.
**Recomendación:** descartado. Cubre lo esencial la cuenta `BinanceWallet` (Binance Alpha y TGE) y `binance` en `influencers.yaml`, vía FxEmbed (D-087). Ver `x_syndication_timeline.md` y `fxembed_api.md`.
