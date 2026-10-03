# DexPaprika (CoinPaprika) — API DEX multichain

**Repo:** https://github.com/coinpaprika/dexpaprika-sdk-python (SDK oficial)
**Licencia:** MIT [V] (GitHub, push 2026-09-29)
**Gratis:** sí, sin key [V]. `GET https://api.dexpaprika.com/networks` y `/networks/solana/pools/search` respondieron 200 sin credenciales (2026-10-03).
**Requisitos:** `requests` (ya instalado). El SDK (`dexpaprika-sdk` 0.12.2) agrega `pydantic>=2` [V] → no hace falta para GET simples.
**Qué hace:** pools, tokens, precios y volumen de DEX en decenas de redes (Solana, Ethereum, BSC, Base, Robinhood Chain, Katana…) [V].
- `/networks/{red}/pools/search?order_by=created_at&sort=desc` devuelve los pools recién creados con `dex_id` (p. ej. `pumpfun`), `created_at`, `volume_usd_24h`, `transactions_24h` [V].
- Ojo: `/networks/{red}/pools?order_by=created_at` devuelve **410 endpoint_removed**; el reemplazo es `/pools/search` [V].
**Por qué sirve al proyecto:**
- Tercera fuente independiente de pools nuevos (además de DexScreener y GeckoTerminal) para el early watch: si una falla o se atrasa, hay respaldo. [I]
- Cubre redes que GeckoTerminal indexa tarde (Robinhood Chain, Katana) [V en `/networks`; cobertura comparada I].
- Señal de "nacimiento" por red y por DEX: conteo de pools nuevos por hora → baseline Poisson (doc 26) por cadena. [H]
**Riesgos técnicos:** no publica un límite de requests claro; usar ≤1 req/s y backoff ante 429. [I] El endpoint cambió en 2026 (410): fijar la ruta en un solo módulo. [V]
**Recomendación:** integrar como fuente de respaldo del early watch (pools nuevos por red) en un bot de fuentes nuevo `bot_dex_pools` con salida src-1. Prioridad P1. Sin SDK.
