# _TOOLS_CATALOG.md
# Catálogo de repositorios gratuitos aplicables al pipeline Shot de Mercado
# Actualizado: 2026-09-29

## MCP Servers (npm/pip) Gratuitos

### 1. @three-ws/pumpfun-mcp
- **URL**: https://npm.im/@three-ws/pumpfun-mcp
- **Repo**: github.com/nirholas/three.ws
- **Licencia**: Apache-2.0
- **Requisitos**: Node.js, npm
- **Capa pipeline**: Pre-launch / Early detection (T+0 a T+2h)
- **Estado**: VERIFICADO (v0.2.6, publicado 2026-09-11)
- **Herramientas**: token discovery, bonding-curve analysis, holder analysis, SNS resolution, KOL signals, swap quotes
- **API Key**: NO requerida

### 2. @pipeworx/mcp-solscan
- **URL**: https://npm.im/@pipeworx/mcp-solscan
- **Licencia**: MIT
- **Requisitos**: Node.js, Solscan Pro API key (opcional para v2)
- **Capa pipeline**: Enrichment / On-chain verification
- **Estado**: POR-VERIFICAR (v0.1.2, publicado 2026-09-26)
- **Herramientas**: Solana block-explorer API, token accounts, transactions

### 3. pumpfun-claims-bot
- **URL**: https://npm.im/pumpfun-claims-bot
- **Licencia**: MIT
- **Requisitos**: Node.js, Telegram bot token (opcional)
- **Capa pipeline**: Social / KOL tracking
- **Estado**: POR-VERIFICAR (v1.0.5, publicado 2026-09-13)
- **Herramientas**: PumpFun on-chain intelligence, Telegram feed, creator fee claims, GitHub social

### 4. @modelcontextprotocol/sdk (base)
- **URL**: https://npm.im/@modelcontextprotocol/sdk
- **Licencia**: MIT
- **Requisitos**: TypeScript/Node.js
- **Capa pipeline**: Infrastructure
- **Estado**: VERIFICADO (v1.31.0)

---

## RSS Feeds Cripto (Gratuitos)

### 5. CoinDesk RSS
- **URL**: https://www.coindesk.com/arc/outboundfeeds/rss/
- **Licencia**: Términos de uso CoinDesk
- **Requisitos**: Parser RSS/Atom
- **Capa pipeline**: Macro / News sentiment
- **Estado**: POR-VERIFICAR

### 6. Decrypt RSS
- **URL**: https://decrypt.co/feed
- **Licencia**: Términos de uso Decrypt
- **Capa pipeline**: Macro / News sentiment
- **Estado**: POR-VERIFICAR

### 7. The Block RSS
- **URL**: https://www.theblock.co/rss
- **Licencia**: Términos de uso The Block
- **Capa pipeline**: Macro / Institutional flows
- **Estado**: POR-VERIFICAR

### 8. CoinTelegraph RSS
- **URL**: https://cointelegraph.com/rss
- **Licencia**: Términos de uso CoinTelegraph
- **Capa pipeline**: Macro / News sentiment
- **Estado**: POR-VERIFICAR

---

## APIs Sociales (Gratuitas / Freemium)

### 9. Reddit API (Pushshift / Oficial)
- **URL**: https://www.reddit.com/dev/api/
- **Licencia**: Reddit API Terms
- **Requisitos**: App registration, OAuth2
- **Capa pipeline**: Social sentiment / Community signals
- **Estado**: VERIFICADO (uso histórico en pipeline)
- **Límites**: 60 req/min (authenticated)

### 10. StockTwits API
- **URL**: https://api.stocktwits.com/developers/docs
- **Licencia**: StockTwits Developer Agreement
- **Requisitos**: API Key (gratuito)
- **Capa pipeline**: Social sentiment / Trending tickers
- **Estado**: POR-VERIFICAR

### 11. CryptoPanic API
- **URL**: https://cryptopanic.com/developers/api/
- **Licencia**: Free tier disponible
- **Requisitos**: API Key (gratuito)
- **Capa pipeline**: News aggregation / Alertas
- **Estado**: VERIFICADO (Free tier: 10 req/min)

---

## Herramientas On-Chain (Gratuitas)

### 12. Solscan Public API
- **URL**: https://public-api.solscan.io/
- **Licencia**: Solscan Terms
- **Requisitos**: API Key opcional (rate limit mayor con key)
- **Capa pipeline**: Enrichment / Holder analysis / Transaction tracking
- **Estado**: VERIFICADO (uso en script_82, script_97)
- **Endpoints**: /token/holders, /token/transactions, /account/tokens

### 13. Solwatch
- **URL**: https://solwatch.io/
- **Licencia**: Propietario (free tier)
- **Requisitos**: API Key
- **Capa pipeline**: Real-time monitoring / Whale alerts
- **Estado**: POR-VERIFICAR (MCP server no encontrado en npm)

### 14. Helius RPC (Free tier)
- **URL**: https://www.helius.dev/
- **Licencia**: Helius Terms
- **Requisitos**: API Key (Free: 1M req/mes)
- **Capa pipeline**: Enhanced RPC / Webhooks / DAS API
- **Estado**: VERIFICADO (API Key configurada en secrets)

### 15. DexScreener API
- **URL**: https://api.dexscreener.com/
- **Licencia**: Gratuito, sin API key
- **Requisitos**: HTTP client
- **Capa pipeline**: Market data / Price / Liquidity / Pair info
- **Estado**: VERIFICADO (uso intensivo en pipeline)
- **Endpoints**: /latest/dex/tokens/{mint}, /token-pairs/v1/solana/{mint}

### 16. PumpPortal WebSocket
- **URL**: wss://pumpportal.fun/api/data
- **Licencia**: Gratuito
- **Requisitos**: WebSocket client
- **Capa pipeline**: Real-time new token detection (T+0)
- **Estado**: VERIFICADO (script_82)

### 17. Three.ws Crypto API
- **URL**: https://three.ws/api/crypto
- **Licencia**: Gratuito
- **Requisitos**: HTTP client
- **Capa pipeline**: Trending / Launches / Airdrops / Token details
- **Estado**: VERIFICADO (script_79, script_80, script_82)
- **Endpoints**: /trending, /launches, /airdrops, /token/{address}

---

## Resumen por Capa del Pipeline

| Capa | Herramientas Principales | Estado |
|------|-------------------------|--------|
| **Pre-launch (T-48h a T-0)** | three.ws /airdrops, PumpPortal WS, @three-ws/pumpfun-mcp | VERIFICADO |
| **Early Detection (T+0 a T+2h)** | PumpPortal WS, DexScreener, three.ws /trending | VERIFICADO |
| **Enrichment (T+2h a T+24h)** | Solscan, Helius, DexScreener, three.ws /token | VERIFICADO |
| **Social/KOL** | CryptoPanic, Reddit, pumpfun-claims-bot, @three-ws KOL signals | PARCIAL |
| **Macro/News** | CoinDesk RSS, CryptoPanic, CoinGecko | PARCIAL |
| **Trust/Verification** | Solscan, Helius, trust_update scheduler | VERIFICADO |

---

## Próximos Pasos (Backlog)

1. **Integrar @three-ws/pumpfun-mcp** como MCP server oficial para KOL signals y holder analysis
2. **Configurar CryptoPanic API** para news aggregation en trust_update
3. **Evaluar @pipeworx/mcp-solscan** para holder distribution analysis
4. **Implementar RSS parser** para macro signals (CoinDesk, Decrypt)
5. **Crear script_112_signal_aggregator** que unifique todas las fuentes