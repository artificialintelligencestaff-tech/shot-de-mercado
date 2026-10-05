# DEXTools — API v2 plan Free (en lugar de scraper)

**Repo:** https://github.com/alb2001/dextools-python (wrapper Python de la API v1/v2)
**Licencia:** MIT [V]. Último push 2025-01, última versión en PyPI 0.3.2 (2024-11-22) [V] → **fuera del criterio de actividad** (<6 meses).
**Gratis:** con **key gratuita**. Plan Free: 50k créditos/mes, 40 req/min [I] (descripción del wrapper y de la web de DEXTools). Sin key, `public-api.dextools.io/free/v2/...` → 403 Forbidden [V] (2026-10-03).
**Requisitos:** key en secret (Dirección). `requests`. El wrapper agrega `aiohttp` [V] → no hace falta: son GET con header `X-API-Key`.
**Qué hace:** token, pool, precio, liquidez, "hot pools" y ranking por red (80+ redes) [I].
**Scraping del sitio: no viable.**
- `www.dextools.io/app/...` devuelve 200 con 9 KB que solo contienen `<app-root>` (SPA de Angular), sin datos en el HTML [V].
- Hacer scraping exige un navegador headless (Playwright) en cada corrida y está detrás de Cloudflare [V redirect cloudflare]. Es caro en minutos de Actions y frágil.
**Por qué sirve al proyecto:** el ranking "hot pairs" de DEXTools es una señal de atención de traders minoristas que DexScreener no expone igual. [H] Con 40 req/min alcanza para 1 consulta por red cada 10 min. [I]
**Alternativa sin key:** DexScreener + GeckoTerminal + DexPaprika (ficha en 03) ya cubren pools, precio y volumen sin key [V]. Lo único exclusivo de DEXTools es su ranking propio. [I]
**Recomendación:** P3. No implementar scraper. Usar la API Free solo si Dirección crea la key y el método por grupo (doc 36) muestra que el ranking hot de DEXTools agrega señal sobre DexScreener (test placebo previo). No usar el wrapper (inactivo): bastan 30 líneas con `requests`.
