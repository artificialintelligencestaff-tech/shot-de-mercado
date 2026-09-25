---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Fuentes — Catálogo de Fuentes Gratuitas

Este archivo lista **todas** las fuentes gratuitas que el proyecto consulta o puede consultar. Cada fuente incluye: nombre, URL, datos que provee, rate limit, autenticación, y estado dentro del proyecto.

**Constraint obligatorio:** todas son gratuitas. Si una fuente requiere pago obligatorio, se marca como DESCARTADA.

## Leyenda de estado

| Estado | Significado |
|---|---|
| ACTIVA | En uso productivo, con script asignado |
| VIABLE | Verificada como gratuita, pendiente de integrar |
| EXPLORADA | Probada en el pasado, sin uso actual |
| DESCARTADA | No cumple constraint free-only o no sirve al proyecto |
| CAIDA | Estuvo activa, ya no responde |

## 1. Fuentes de mercado (precios, market cap, liquidez)

| Fuente | URL | Datos | Rate limit | Auth | Estado |
|---|---|---|---|---|---|
| CoinGecko Public | api.coingecko.com/api/v3 | Precios, mcap, volumen, narrativas | 30 req/min | No | ACTIVA |
| CoinGecko Demo | pro-api.coingecko.com | Igual + más endpoints | 30 req/min, 10K/mes | Sí (key gratis) | VIABLE |
| Dexscreener | api.dexscreener.com/latest/dex | Precios, liquidez, pares | 300 req/min | No | ACTIVA |
| DIA Free | api.diadata.org | Precios 3000+ activos | 100 req/día | No | VIABLE |
| CoinPaprika | api.coinpaprika.com | Precios, mcap, históricos | 20K/mes free | No | VIABLE |
| Binance Public | api.binance.com/api/v3 | Precios, orderbook, klines | Sin límite | No | EXPLORADA |
| Binance Vision | data.binance.vision | Datos históricos completos | Sin límite | No | EXPLORADA |
| Alternative.me | api.alternative.me/fng/ | Fear & Greed Index | Sin límite | No | VIABLE |
| DeFiLlama | api.llama.fi | TVL, yields, DEX volume | Sin límite | No | VIABLE |
| Orderly Network | api.orderly.org | Perps, funding rates | Sin límite | No | EXPLORADA |

## 2. Fuentes on-chain

| Fuente | URL | Datos | Rate limit | Auth | Estado |
|---|---|---|---|---|---|
| Helius RPC | rpc.helius.xyz | Solana on-chain | 100K/día | Sí (key gratis) | ACTIVA |
| PumpPortal WS | pumpportal.fun/api/data | WS de nuevos tokens | Sin límite | No | ACTIVA |
| MadeOnSol | madeonsol.com/api | KOL tracking, deployer | 200/día | Sí (key gratis) | ACTIVA |
| Solscan | public-api.solscan.io | Explorador Solana | 100 req/día | No | VIABLE |
| Birdeye | public-api.birdeye.so | Solana analytics | 30 req/min | Sí (key gratis) | VIABLE |
| whalecli | github.com/clawinfra/whalecli | Ballenas ETH/BTC | Local | No | EXPLORADA |
| pump-dump-crypto-screener | github.com/aleks-ent | 500+ pares cada 3s | Local | No | EXPLORADA |

## 3. Fuentes sociales y de sentimiento

| Fuente | URL | Datos | Rate limit | Auth | Estado |
|---|---|---|---|---|---|
| ApeWisdom | apewisdom.io/api | Menciones Reddit | Sin límite | No | ACTIVA |
| free-crypto-news | fcn.dev/api | Sentimiento X + Reddit | Sin límite | No | VIABLE |
| Adanos Sentiment | adanos.org | Sentimiento cross-platform | 250/mes | Sí | VIABLE |
| Reddit JSON | reddit.com/r/X.json | Posts de subreddits | 60 req/min | No | VIABLE |
| Santiment | api.santiment.net | Sentimiento + on-chain | 100/mes | Sí | EXPLORADA |
| CoinLobster | coinlobster.com | Social metrics | Sin definir | No | EXPLORADA |

## 4. Fuentes de noticias

| Fuente | URL | Datos | Rate limit | Auth | Estado |
|---|---|---|---|---|---|
| CryptoPanic | cryptopanic.com/api/v1 | Noticias agregadas | 200/día | No | VIABLE |
| CoinDesk RSS | coindesk.com/arc/outboundfeeds/rss | Noticias | Sin límite | No | VIABLE |
| The Block RSS | theblock.co/rss.xml | Noticias | Sin límite | No | VIABLE |
| Decrypt RSS | decrypt.co/feed | Noticias | Sin límite | No | VIABLE |
| Cointelegraph RSS | cointelegraph.com/rss | Noticias | Sin límite | No | VIABLE |

## 5. Fuentes pre-lanzamiento (TGEs, airdrops)

| Fuente | URL | Datos | Rate limit | Auth | Estado |
|---|---|---|---|---|---|
| Metaplex Genesis | api.metaplex.com | TGEs Solana | 429 si excede | No | ACTIVA |
| three.ws | three.ws/api | Trending, airdrops | 20 req/min | No | ACTIVA |
| Clawnch | clawnch.com/api | Airdrops | Sin definir | No | EXPLORADA |
| airdrops.io | airdrops.io/api | Airdrops agregados | Sin límite | No | VIABLE |
| Dropstab | dropstab.com/api | TGE calendar | Sin definir | No | VIABLE |
| CoinMarketCal | coinmarketcal.com/api | Eventos cripto | 100/día | Sí | VIABLE |

## 6. Fuentes académicas y profesionales

| Fuente | URL | Datos | Rate limit | Auth | Estado |
|---|---|---|---|---|---|
| arXiv API | export.arxiv.org/api | Papers crypto/blockchain | Sin límite | No | VIABLE |
| SSRN | ssrn.com | Papers finanzas | Sin API pública | No | EXPLORADA |
| NBER | nber.org/api | Papers economía | Sin límite | No | VIABLE |
| Google Scholar | scholar.google.com | Meta-búsqueda | Bloquea scraping | No | EXPLORADA |

**Nota:** la academia es **brújula**, no evidencia. Sirve para saber dónde buscar datos, no para validar señales ya detectadas.

## 7. Servidores MCP (Model Context Protocol)

| Fuente | URL | Datos | Rate limit | Auth | Estado |
|---|---|---|---|---|---|
| Chainbase Tops MCP | mcp.chainbase.com | Narrativas, topics | 600 req/h | No | VIABLE |
| Tavily MCP | github.com/tavily-ai/tavily-mcp | Búsqueda web IA | 1000/mes | Sí (key gratis) | VIABLE |
| Brave Search MCP | github.com/modelcontextprotocol/servers | Búsqueda web | 2000/mes | Sí (key gratis) | VIABLE |
| Fetch MCP | github.com/modelcontextprotocol/servers | Descarga webs | Sin límite | No | VIABLE |
| CoinPaprika MCP | github.com/coinpaprika/mcp | Precios, mcap | (hereda CoinPaprika) | No | VIABLE |
| DeFi MCP OpenSource | github.com/topics/mcp-server | Protocolos DeFi | Variable | No | VIABLE |

## 8. Comunicación

| Fuente | URL | Datos | Rate limit | Auth | Estado |
|---|---|---|---|---|---|
| Telegram Bot API | api.telegram.org/bot<token> | Envío de mensajes | 30 msg/s | Sí (token) | ACTIVA |

## 9. Schedulers y serverless

| Herramienta | URL | Función | Costo | Estado |
|---|---|---|---|---|
| GitHub Actions | github.com/features/actions | Ejecución cron en nube | Free 2000 min/mes privado / ilimitado público | VIABLE |
| Cron-job.org | cron-job.org | Cron externo gratuito | Free | VIABLE |
| UptimeRobot | uptimerobot.com | Healthcheck + cron | Free 50 monitors | VIABLE |

## 10. Herramientas de cálculo y persistencia

| Herramienta | Uso | Estado |
|---|---|---|
| Python 3.11 built-in | json, os, time, hashlib, base64, sqlite3 | ACTIVA |
| requests | HTTP calls | ACTIVA |
| websockets | PumpPortal WS | ACTIVA |
| python-dotenv | Gestión de .env | ACTIVA |
| SQLite | Persistencia alternativa | VIABLE |

## Reglas de uso

1. **Nunca** una fuente paga obligatoria. Si se necesita una temporalmente, se marca como EXCEPCIÓN y requiere autorización de Dirección.
2. **Siempre** documentar rate limits respetados.
3. **Cada fuente nueva** se prueba con un script pequeño antes de integrarla al pipeline.
4. **Rotación de fallbacks:** si una fuente falla, hay al menos una alternativa marcada como VIABLE.
5. **Auditoría trimestral:** cada fuente se re-verifica como gratuita.

## Fuentes pendientes de investigar

- MCPs específicos para Solana (búsqueda en GitHub topics).
- APIs de TGE calendar más completas.
- Scrapers de influencers cripto (X, YouTube).
- Datasets públicos de pump.fun graduations (RED-PUMP-2026-v1).

## VER TAMBIÉN

- [02_ARQUITECTURA.md](02_ARQUITECTURA.md) — arquitectura general
- [03_FLUJOS.md](03_FLUJOS.md) — qué fuentes usa cada workflow
- [04_SCRIPTS_CATALOG.md](04_SCRIPTS_CATALOG.md) — scripts que consultan cada fuente
- [06_SCORING.md](06_SCORING.md) — cómo se usan las señales de cada fuente

## Changelog

- 2026-09-24 — v1.0 — Creación inicial con 50+ fuentes categorizadas (YANG, Ciclo 17.5.A)