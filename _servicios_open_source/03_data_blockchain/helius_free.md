# Helius (Solana) — plan Free

**Repo:** https://github.com/helius-labs/helius-sdk (TypeScript; no hay SDK Python oficial) · cliente Python genérico: https://github.com/michaelhly/solana-py
**Licencia:** helius-sdk MIT [V]; solana-py MIT [V] (GitHub, 2026-10-03)
**Gratis:** sí, con **key gratuita** (cuenta sin tarjeta). Free: 1M créditos/mes, RPC 10 req/s, DAS/Enhanced 2 req/s [I] (helius.dev/docs/billing/plans, consultado 2026-10-03).
**Requisitos:** key en secret (`HELIUS_API_KEY`), creada por Dirección. `requests` alcanza (JSON-RPC por POST). `solana` 0.40.3 trae `solders`, `httpx2`, `pydantic`, `websockets` [V] → no instalar si basta con JSON-RPC.
**Qué hace:** RPC de Solana con APIs propias:
- DAS (`getAsset`, `getTokenAccounts`) → holders y metadata de cualquier mint;
- transacciones parseadas (swaps, mints, transfers) por dirección;
- webhooks por dirección (en el free, limitados).
**Por qué sirve al proyecto:**
- Reemplaza a Solscan, que exige key Pro paga: `pro-api.solscan.io/v2.0` responde 401 "Token is missing" y `public-api.solscan.io` responde 404 [V] (2026-10-03).
- Permite medir concentración de holders y actividad del deployer sin depender solo de RugCheck. [I]
- El RPC público `api.mainnet-beta.solana.com` existe pero tiene límites agresivos y no ofrece DAS. [I]
**Riesgos técnicos:** 1M créditos/mes ≈ 33k/día; `getProgramAccounts` y DAS consumen más créditos por llamada → presupuesto diario obligatorio. [I]
**Recomendación:** P2. Integrar solo si Dirección crea la key gratuita. Uso acotado: holders/deployer de los candidatos que ya pasaron el scorer (no barrido). Si no hay key: seguir con RugCheck + GoPlus (sin key).

## Receta (bot_genesis, D-067)

Creaciones de token del programa de pump.fun vía Enhanced Transactions API [I: ruta `GET
/v0/addresses/{address}/transactions` y tipo `CREATE` según la referencia de Helius; host y forma exacta sin verificar
porque requiere key]. Necesita el secret `HELIUS_API_KEY` (lo crea Dirección): sin él, bot_genesis la deja en
probation con ese motivo y el runner no hace ninguna request. Con la key, la valida el fetch en seco.

```yaml
recipe:
  kind: json_api
  url_base: https://api.helius.xyz/v0/addresses/6EF8rrecthR5Dkzon8Nwu78hRvfCx9DgSHeSDkPRv8vD6P/transactions?api-key={secreto}&type=CREATE&limit=50
  secreto: HELIUS_API_KEY
  cadencia_min: 15
  src_kind: token
  grupo: a
  limite: 50
  extractores:
    - items: "$[*]"
    - id: "$.signature"
    - ts: "$.timestamp"
    - text: ["$.tokenTransfers[*].mint", "$.description"]
    - meta.type: "$.type"
    - meta.source: "$.source"
```
