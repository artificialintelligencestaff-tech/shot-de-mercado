# Pump.fun — API del frontend + PumpPortal (stream)

**Repo:** no hay repo oficial abierto: son APIs públicas. Referencia de uso: https://pumpportal.fun/data-api/real-time/
**Licencia:** n/a (servicio). Uso de datos públicos.
**Gratis:** sí.
- `frontend-api-v3.pump.fun`: sin key, 200 [V] (2026-10-03).
- PumpPortal `wss://pumpportal.fun/api/data`: `subscribeNewToken` y `subscribeMigration` son gratis [V]. `subscribeTokenTrade` y `subscribeAccountTrade` cuestan 0,01 SOL cada 10k mensajes [V] → **no usar**.
**Requisitos:** `requests` para REST; `websockets` 17.1 (BSD-3, sin dependencias) [V] solo si se usa el stream.
**Qué hace:**
- REST [V]: `GET /coins?offset=0&limit=N&sort=created_timestamp&order=DESC&includeNsfw=false` lista los tokens recién creados con `mint`, `creator`, `created_timestamp`, `market_cap_usd`, `ath_market_cap`, `reply_count`, `complete` (graduado), `twitter`, `website`, `is_currently_live`. `GET /coins/currently-live` lista los tokens con stream activo.
- Rutas que NO existen hoy [V]: `/replies/{mint}` → 404 y `/coins/king-of-the-hill` → 404. Los comentarios ya no salen por esta API: solo queda el conteo `reply_count`.
- Stream [V]: un evento por token nuevo y uno por migración (graduación a PumpSwap). Regla publicada: "una sola conexión websocket a la vez"; abrir muchas causa ban de 1 h.
**Por qué sirve al proyecto:**
- Es la fuente más temprana posible para el grupo de memecoins de Solana: el nacimiento del token, antes de que DexScreener o GeckoTerminal lo indexen. [I]
- `reply_count`, `is_currently_live`, `twitter` y `website` son features sociales tempranas para el scorer joven (`script_116`). [H]
- Las migraciones marcan el paso de bonding curve a DEX, un evento natural para el método por grupo (doc 36). [I]
**Riesgos técnicos:** API no documentada: puede cambiar sin aviso (ya cambiaron replies y KOTH) [V]. El stream exige un proceso persistente: en Actions, un job de ≤50 min como el bot de Telegram. [I]
**Recomendación:** P1.
- Bot `bot_pumpfun` en REST: poll cada 2–4 min de `/coins` ordenado por creación; salida src-1 con `kind="token_launch"` y `author=creator`; sin guardar `description`, solo `reply_count` en `m`.
- Stream PumpPortal: solo si el poll REST pierde lanzamientos (medir primero).
- No usar los métodos de trades: son pagos.

## Receta (bot_genesis, D-067)

Lanzamientos de pump.fun por orden de creación, sin key [V 2026-10-03: 50 ítems con `mint`, `symbol`,
`created_timestamp` en ms, `usd_market_cap`, `reply_count`, `complete`, `creator`]. No guarda `description` (src-1).

```yaml
recipe:
  kind: json_api
  url_base: https://frontend-api-v3.pump.fun/coins?offset=0&limit=50&sort=created_timestamp&order=DESC&includeNsfw=false
  cadencia_min: 10
  src_kind: token
  grupo: a
  limite: 50
  extractores:
    - items: "$[*]"
    - id: "$.mint"
    - title: "$.name"
    - ts: "$.created_timestamp"
    - author: "$.creator"
    - text: "$.mint"
    - meta.symbol: "$.symbol"
    - meta.usd_market_cap: "$.usd_market_cap"
    - meta.reply_count: "$.reply_count"
    - meta.complete: "$.complete"
    - meta.is_currently_live: "$.is_currently_live"
    - meta.twitter: "$.twitter"
```
