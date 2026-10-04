# RWA.xyz — analítica de activos reales tokenizados

**Repo:** no aplica (servicio). https://app.rwa.xyz
**Licencia:** términos de RWA.xyz. La API (`api.rwa.xyz`) es para clientes con key [I].
**Gratis:** el sitio sí, sin cuenta [V] (2026-10-04, D-087):
- `GET https://app.rwa.xyz/` → 200, unos 10,7 MB de HTML con `__NEXT_DATA__` de unos 10 MB y datos completos. Trae un script de Cloudflare, pero no un challenge.
- `GET https://api.rwa.xyz/v3/assets` → 404 sin key [V].
**Requisitos:** `requests`, `json` y `re` (`__NEXT_DATA__`). La descarga pesa: 1 vez por día alcanza.
**Tipo de dato:** en `pageProps` [V]:
- `assets`: 3.459 activos con clase (bonos del Tesoro, commodities, crédito, inmuebles) y emisor;
- `latestAssets`: los **recién agregados**;
- `netFlowsByAsset`, `netFlowsByAssetClass` y `netFlowsByManager`: mints netos de 7 días, 30 días, etc.;
- `tickerGroups` (BUIDL, USYC, USDY…) y una serie de la tasa SOFR.
**Utilidad para pre-lanzamiento o anticipación:**
- **Sector RWA (grupo g de keywords):** `latestAssets` adelanta tokenizaciones nuevas antes de que tengan mercado secundario [I].
- **Flujos netos por emisor:** una entrada fuerte en los productos de Ondo, Securitize o Plume anticipa narrativa RWA y le da contexto a las cuentas `ondo`, `centrifuge` y `maplefinance` de `influencers.yaml` [H].
**Riesgos técnicos:** 10 MB por request. Si RWA.xyz mueve los datos a la API con key, el `__NEXT_DATA__` se vacía [I].
**Recomendación:** P2. Un snapshot diario (`latestAssets` + flujos netos de 7 días) a `02_Analisis/patrimonio/informativo/rwa/`, sin guardar el HTML. Señal de sector, no de token individual.
