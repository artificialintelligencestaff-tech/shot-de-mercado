# CryptoRank — ventas de tokens, unlocks y fondos

**Repo:** no aplica (servicio). Docs: https://api.cryptorank.io/docs
**Licencia:** términos de CryptoRank [I].
**Gratis:** **no utilizable sin cuenta** (2026-10-04, D-087):
- `GET https://cryptorank.io/upcoming-ico` → **403**, con challenge de Cloudflare [V].
- `GET https://api.cryptorank.io/v1/currencies` y `/v2/currencies` → **401**, página HTML que pide key [V].
- La API tiene un plan gratuito, pero pide registrarse para la key [I].
**Requisitos:** key (cuenta) para la API. El sitio no es accesible para un cliente sin navegador.
**Tipo de dato:** ventas de tokens (IDO/IEO/ICO) con fechas y precio, unlocks, fondos y rondas [I, según su documentación].
**Utilidad para pre-lanzamiento o anticipación:** alta en teoría (precio de preventa, fecha de TGE y fondos detrás), pero **inaccesible hoy** sin cuenta [V].
**Riesgos técnicos:** bloqueo activo con Cloudflare. Saltarlo implica navegador automatizado o resolver challenges, lo cual queda fuera de las reglas.
**Recomendación:** descartado mientras no haya key. Si Dirección crea una cuenta gratuita y carga el secret `CRYPTORANK_API_KEY`, se reevalúa como fuente del calendario (P2). Mientras tanto, cubren lo mismo ICO Drops (`icodrops.md`) y el calendario ICO de CMC (`coinmarketcap_nuevos.md`).
