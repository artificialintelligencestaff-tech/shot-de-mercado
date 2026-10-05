# CoinMarketCap — recién agregados y calendario ICO (data-api pública del sitio)

**Repo:** no aplica (servicio). API oficial: https://coinmarketcap.com/api/documentation/v1/
**Licencia:** términos de uso de CoinMarketCap; la data-api es la que usa el propio sitio, no un contrato público [I].
**Gratis:** sí para la data-api y las páginas, sin key y **sin Cloudflare** en esta prueba [V] (2026-10-04, D-087):
- `GET https://api.coinmarketcap.com/data-api/v3/cryptocurrency/spotlight?dataType=8&limit=10` → 200 JSON con `recentlyAddedList` (y `upcoming`, vacío hoy) [V].
- `GET https://coinmarketcap.com/new/` → 200: `__NEXT_DATA__` trae 100 recién agregados con `addedDate` (ISO), `platforms` (cadena) y `marketCap` [V].
- `GET https://coinmarketcap.com/ico-calendar/` → 200: `__NEXT_DATA__` con `ongoing`, `upcoming` y `ended`. Cada entrada trae `start`/`end`, `icoPriceUsd`, `goalUsd`, launchpad y cripto. Hoy: 1 en curso, 0 próximas, 10 terminadas [V].
- La API oficial (`pro-api.coinmarketcap.com`) responde **401** sin key. El plan Basic es gratuito pero pide cuenta [V 401 / I plan].
**Requisitos:** `requests`, `json` y `re` (`__NEXT_DATA__`). Sin bs4.
**Tipo de dato:** listados nuevos con fecha exacta de alta, cadena y market cap; ventas de tokens con fechas, precio de preventa y meta.
**Utilidad para pre-lanzamiento o anticipación:**
- **Precio de preventa** (`icoPriceUsd`) y ventana de la venta: es justo el dato que la alerta PRE-LANZAMIENTO de D-082 muestra ("precio preventa $X"). Una fuente más para el calendario de `bot_prelaunch_calendar` [I].
- `addedDate` exacta: mide el retraso entre nacer on-chain y listarse en CMC, igual que con CoinGecko [H].
- El calendario ICO de CMC tiene **poca cobertura** (0 próximas hoy) [V]: es un complemento, no la fuente principal.
**Riesgos técnicos:** la data-api no está documentada y puede cambiar de ruta o de forma. Si CMC activa Cloudflare para clientes sin navegador, se pierde [I].
**Recomendación:** P1. Sumar `ico-calendar` (con precio de preventa) como séptima fuente de `bot_prelaunch_calendar`, cada 6 h, y `spotlight` como receta `json_api` de recién agregados cada 60 min.
