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
