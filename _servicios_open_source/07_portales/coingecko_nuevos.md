# CoinGecko — monedas recién agregadas y trending (no hay "upcoming")

**Repo:** no aplica (servicio). Docs: https://docs.coingecko.com
**Licencia:** términos de uso de CoinGecko; datos públicos sin licencia abierta. Su API pública exige atribución [I].
**Gratis:** parcial (2026-10-04, D-087):
- `GET https://www.coingecko.com/en/new-cryptocurrencies` → 200, HTML de 1,3 MB, sin Cloudflare: tabla de unas 50 monedas recién agregadas [V].
- `GET https://api.coingecko.com/api/v3/search/trending` → 200 sin key: 15 monedas, NFT y categorías en tendencia [V].
- `GET https://api.coingecko.com/api/v3/coins/list/new` → **401**: es del plan Pro, pago [V].
- El plan "Demo" gratuito pide crear una cuenta para obtener la key [I]; el proyecto no crea cuentas.
**Requisitos:** `requests` y `re` para la tabla HTML (filas `<tr>`, link `/en/coins/<slug>`). Sin bs4.
**Tipo de dato:** por moneda: nombre, símbolo, precio, cadena, 1h/24h, volumen 24h, FDV y "Last added" en texto relativo ("about 6 hours") [V]. La tabla no trae contrato; está en la página de la moneda.
**Utilidad para pre-lanzamiento o anticipación:**
- CoinGecko **no tiene calendario de lanzamientos**: lo que hay es "recién listado en CoinGecko", que llega después del nacimiento on-chain [V/I].
- Sirve como **señal de legitimación**: listarse en CoinGecko suele coincidir con el primer salto de atención fuera de los DEX [H]. Cruzarlo con `token_nacido` (D-082) mide el retraso entre nacer y ser listado.
- Trending: confirma narrativa con demanda real de búsquedas, como contraste de `keyword_narrativa` (D-087) [H].
**Riesgos técnicos:** HTML sin contrato; el texto relativo de "Last added" se aproxima por hora. La API pública sin key tiene un límite bajo, no publicado [I].
**Recomendación:** P2. Receta `html_list` cada 60 min sobre `new-cryptocurrencies` y `search/trending` cada 30 min. No reemplaza a DexScreener/GeckoTerminal para nacimientos.
