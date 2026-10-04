# Dune Analytics — consultas SQL sobre datos on-chain

**Repo:** https://github.com/duneanalytics/dune-client (cliente Python)
**Licencia:** cliente Apache-2.0 [I]; datos y servicio bajo los términos de Dune.
**Gratis:** **la API ya no** (2026-10-04, D-087):
- `GET https://api.dune.com/api/v1/query/1/results` → **401** sin key [V].
- Docs oficiales, en `docs.dune.com/api-reference/overview/rate-limits` y `/billing`: "Free access is view-only; API usage requires an active trial or a paid plan". El plan Free figura como "API access: Not available" [V, texto de las docs].
- El sitio (`dune.com`) se puede ver sin cuenta, pero no exporta datos sin API [I].
**Requisitos:** plan pago o trial, más key.
**Tipo de dato:** cualquier consulta SQL sobre tablas decodificadas (DEX trades, transferencias, lanzamientos de pump.fun, etc.) [I].
**Utilidad para pre-lanzamiento o anticipación:** alta (consultas a medida de wallets de insiders o de pools nuevos por launchpad), pero **paga** [V].
**Recomendación:** descartado por la regla "100% gratis". Para pools nuevos, el proyecto ya usa DexScreener, GeckoTerminal y DexPaprika (gratis); para wallets de insiders, las cuentas de analistas on-chain de `influencers.yaml`.
