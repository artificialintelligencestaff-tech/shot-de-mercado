# GoPlus Security API

**Repo:** https://github.com/GoPlusSecurity/goplus-sdk-python (SDK oficial; la API se usa también con `requests` directo)
**Licencia:** Apache-2.0 [V] (GitHub, 2026-10-03)
**Gratis:** sí. Sin key para uso básico: `GET /api/v1/solana/token_security` y `/api/v1/token_security/{chain_id}` respondieron 200 `code=1` sin credenciales [V] (2026-10-03). Límite publicado: 30 llamadas/min [V] (docs.gopluslabs.io/reference/support).
**Requisitos:** `requests` (ya instalado). El SDK (`goplus` 0.2.6, 2026-08-21) arrastra `six`, `urllib3`, `python_dateutil`, `certifi` [V] → no hace falta: la API es un GET.
**Qué hace:** chequeo de seguridad de token por contrato, en Solana (SPL/SPL-2022) y EVM (ETH, BSC=56, Base=8453, Arbitrum, etc.).
- Solana [V]: `mintable`, `freezable`, `closable`, `transfer_fee`, `transfer_hook`, `metadata_mutable`, `holders`, `lp_holders`, `holder_count`, `dex`, `trusted_token`.
- EVM [V]: `is_honeypot`, `cannot_buy`, `transfer_tax`, `is_mintable`, `hidden_owner`, `can_take_back_ownership`, `owner_percent`, `creator_percent`, `is_in_cex`, `honeypot_with_same_creator`.
**Por qué sirve al proyecto:**
- RugCheck solo cubre Solana [V] (doc 34). GoPlus da la misma clase de verificación para los grupos EVM (b, c, e…) con una sola API y sin key. [I]
- `honeypot_with_same_creator` y `creator_percent` son features de autor que hoy no tenemos fuera de Solana. [V]
- Encaja como chequeo de "adquisición" (¿se puede comprar y vender?) antes del dossier. [I]
**Riesgos técnicos:** 30 req/min alcanza para validar candidatos, no para barrer todos los pools. [V] Respuesta en strings (`"0"`/`"1"`): hay que normalizar. [V]
**Recomendación:** integrar como enriquecedor de candidatos EVM en la ruta del dossier (`script_113`), con caché de 6 h por contrato y presupuesto ≤20 req/min. Prioridad P1. Sin SDK: `requests` + normalización propia.
