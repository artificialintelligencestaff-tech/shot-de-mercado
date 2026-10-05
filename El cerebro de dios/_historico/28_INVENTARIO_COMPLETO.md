---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: INVENTARIO v1.1 (Fase 9: +83 servicios, 22 MCP nuevos); verificación en vivo con probe_inventario.yml
last_updated: 2026-10-01
version: 1.1
---

# 28 — Inventario completo de servicios gratuitos

Rótulos: [V] verificado (HTTP, archivo o búsqueda en esta sesión o en un doc anterior, citado) · [I] inferido · [P] pendiente (licencia/actividad/acceso sin auditar; T2 prueba los endpoints desde Actions).

**Fuente única:** `04_Config/inventario.json`. De ahí salen este documento y la lista que prueba `probe_inventario.py`. Agregar un servicio = agregar una entrada al JSON.

**Criterio del proyecto** (doc 22 §3): 100% gratuito, sin key o con key gratuita sin tarjeta, licencia permisiva para el código que se use, actividad < 6 meses, supply chain revisada (doc 25). Lo que no cumple se lista igual, con el motivo.

## 0. Resumen

- **Servicios inventariados: 174** (v1.0: 91 · Fase 9: +83) · con endpoint de prueba: **74** · sin key: **130** · verificados: **62**.
- **Grupos cubiertos: 9/9.**
- **MCP nuevos (Fase 9): 22**, más 6 directorios. El único sin key y oficial es el **MCP remoto de CoinGecko** (`mcp.api.coingecko.com`). Ninguno se integra al pipeline: el pipeline ya usa las mismas APIs por HTTP directo; los MCP sirven para investigación manual.
- **Datasets:** integrados **MemeChain** (CC-BY-4.0, tasas base por chain y narrativa) y **Binance histórico** (velas diarias desde 2017). Prioridad P0 nueva: **jocry/Pumpfun_Memecoin_Corpus** en Hugging Face (798.430 lanzamientos de pump.fun de junio–julio 2026, con graduación etiquetada): es el universo exacto del grupo a.

| Categoría | Servicios |
|---|---|
| Precios y mercado | 17 |
| DEX, launchpads y seguridad de contratos | 14 |
| Exploradores, RPC y datos on-chain | 17 |
| DeFi (TVL, fees, yields) | 9 |
| Derivados | 10 |
| Gobernanza | 2 |
| RWA | 5 |
| Sentimiento | 4 |
| Noticias | 7 |
| Social | 6 |
| Calendario y atención | 8 |
| MCP servers y directorios | 38 |
| Repos con lógica especial (NLP, régimen, modelos) | 19 |
| Papers con código o datos | 6 |
| Datasets públicos | 12 |

## 1. Cobertura por grupo

| Grupo | Fuentes sin key (P0/P1) | Hueco / alternativa |
|---|---|---|
| a memecoins | DexScreener API, GeckoTerminal API v2, DexPaprika API, PumpPortal WebSocket, RugCheck API, GoPlus Security API, Honeypot.is, Blockscout API, Reddit RSS … | holders históricos (Blockscout / RPC público [P]); calibración: MemeChain (integrado) + Pumpfun Corpus (P0) |
| b preventa | Hyperliquid info API, Aevo API, Google News RSS, CoinDesk RSS, Cointelegraph RSS, Decrypt RSS, The Block RSS, Wikipedia Pageviews, Wikidata SPARQL … | calendario de TGEs: CryptoRank, CoinMarketCal y Coindar piden key; three.ws (script_99) hoy vacío [V]; Apify unlocks (key gratuita) |
| c gobernanza | CoinGecko API pública, CoinPaprika, Binance data-api, Coinbase Exchange API pública, Blockscout API, DefiLlama TVL, DefiLlama fees y DEX por chain/protocolo, DefiLlama yields, Snapshot GraphQL … | Tally pide key; unlocks de pago → proxy FDV/mcap |
| d sintéticos | CoinGecko API pública, CoinPaprika, Binance data-api, Coinbase Exchange API pública, DefiLlama stablecoins, Hyperliquid info API, dYdX v4 indexer, Aevo API, Reddit RSS … | DefiLlama derivatives 402 → Hyperliquid (integrado) + dYdX + Gains + Drift |
| e DePIN | CoinGecko API pública, CoinPaprika, Binance data-api, Coinbase Exchange API pública, DefiLlama TVL, DefiLlama fees y DEX por chain/protocolo, Google News RSS, CoinDesk RSS, Cointelegraph RSS … | nodos/ingresos por proyecto (DePINscan sin API) → fees de DefiLlama para 9 protocolos |
| f L1/L2 | CoinGecko API pública, CoinPaprika, Binance data-api, Coinbase Exchange API pública, GeckoTerminal API v2, DexPaprika API, Blockscout API, DefiLlama TVL, DefiLlama fees y DEX por chain/protocolo … | staking flows sin fuente gratuita verificada |
| g RWA | CoinGecko API pública, CoinPaprika, Binance data-api, Coinbase Exchange API pública, Blockscout API, DefiLlama TVL, DefiLlama fees y DEX por chain/protocolo, DefiLlama yields, Google News RSS … | RWA.xyz sin key → DefiLlama RWA + Ondo / Centrifuge [P] |
| h blue chips | CoinGecko API pública, CoinPaprika, Binance data-api, Coinbase Exchange API pública, Kraken API pública, Hyperliquid info API, Deribit API pública, alternative.me Fear & Greed, Google News RSS … | DVOL de Deribit (gratuito, falta conectarlo); historia completa: dataset Binance (integrado) |
| i establecidos | DexScreener API, RugCheck API, GoPlus Security API, Blockscout API, DefiLlama TVL | holders con historia (Blockscout / RPC [P]) |

## 2. Servicios

Formato por entrada: URL · licencia · API key · cobertura · uso propuesto · prioridad · verificación (· endpoint de prueba de T2).

### 2.1 Precios y mercado

#### CoinGecko API pública
- URL: https://www.coingecko.com/en/api
- Licencia: ToS CoinGecko
- API key: no
- Cobertura: c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: mercado, categorías, tickers (rutas CEX), trending
- Prioridad: P0
- Verificado: [V] doc 23 / Fase 7
- Endpoint de prueba (T2): `GET https://api.coingecko.com/api/v3/ping`

#### CoinPaprika
- URL: https://api.coinpaprika.com
- Licencia: ToS CoinPaprika
- API key: no
- Cobertura: c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: verificación cruzada de precios, beta, first_data_at
- Prioridad: P1
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://api.coinpaprika.com/v1/global`

#### CoinCap API 3.0
- URL: https://pro.coincap.io/api-docs
- Licencia: ToS CoinCap
- API key: sí (gratuita con registro)
- Cobertura: c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: precios; la v3 pide key [I]
- Prioridad: P3
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://rest.coincap.io/v3/assets?limit=1`

#### CryptoCompare min-api (CoinDesk Data)
- URL: https://min-api.cryptocompare.com
- Licencia: ToS CoinDesk Data
- API key: no
- Cobertura: h (blue chips)
- Uso propuesto: precios y OHLCV históricos sin key con límite [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD`

#### Binance data-api (spot público)
- URL: https://data-api.binance.vision
- Licencia: ToS Binance
- API key: no
- Cobertura: h (blue chips), c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA)
- Uso propuesto: velas diarias (GARCH/ATR/Bollinger), exchangeInfo, precio del trust loop CEX
- Prioridad: P0
- Verificado: [V] doc 23 / Fase 7
- Endpoint de prueba (T2): `GET https://data-api.binance.vision/api/v3/ping`

#### Coinbase Exchange API pública
- URL: https://docs.cdp.coinbase.com/exchange
- Licencia: ToS Coinbase
- API key: no
- Cobertura: h (blue chips), c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA)
- Uso propuesto: verificación de par y precio del trust loop CEX
- Prioridad: P0
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://api.exchange.coinbase.com/products/BTC-USD/ticker`

#### Kraken API pública
- URL: https://docs.kraken.com/api
- Licencia: ToS Kraken
- API key: no
- Cobertura: h (blue chips)
- Uso propuesto: precio del trust loop CEX (respaldo)
- Prioridad: P1
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://api.kraken.com/0/public/Ticker?pair=XBTUSD`

#### OKX API v5 (market)
- URL: https://www.okx.com/docs-v5
- Licencia: ToS OKX
- API key: no
- Cobertura: h (blue chips), d (sintéticos)
- Uso propuesto: ruta CEX adicional y funding [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT`

#### Bybit API v5 (market)
- URL: https://bybit-exchange.github.io/docs/v5/intro
- Licencia: ToS Bybit
- API key: no
- Cobertura: h (blue chips), d (sintéticos)
- Uso propuesto: funding y OI; puede bloquear IPs de EE.UU. [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://api.bybit.com/v5/market/tickers?category=spot&symbol=BTCUSDT`

#### KuCoin API pública
- URL: https://www.kucoin.com/docs
- Licencia: ToS KuCoin
- API key: no
- Cobertura: c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA)
- Uso propuesto: cotización de altcoins que no están en Binance/Coinbase [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT`

#### Gate API v4
- URL: https://www.gate.io/docs/developers/apiv4
- Licencia: ToS Gate
- API key: no
- Cobertura: a (memecoins), c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA)
- Uso propuesto: listados de tokens chicos (ruta CEX) [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://api.gateio.ws/api/v4/spot/tickers?currency_pair=BTC_USDT`

#### Pyth Hermes (precios de oráculo) — Fase 9
- URL: https://docs.pyth.network
- Licencia: ToS del proveedor
- API key: no
- Cobertura: d (sintéticos), h (blue chips), g (RWA)
- Uso propuesto: precios de oráculo (basis contra spot)
- Prioridad: P1
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://hermes.pyth.network/v2/price_feeds?query=btc&asset_type=crypto`

#### Chainlink price feeds (on-chain vía RPC) — Fase 9
- URL: https://docs.chain.link/data-feeds
- Licencia: ToS del proveedor
- API key: no
- Cobertura: d (sintéticos), g (RWA), h (blue chips)
- Uso propuesto: precio de referencia on-chain
- Prioridad: P3
- Verificado: [P]

#### Blockchair API — Fase 9
- URL: https://blockchair.com/api/docs
- Licencia: ToS del proveedor
- API key: no
- Cobertura: h (blue chips)
- Uso propuesto: estadísticas de Bitcoin sin key con límite [I]
- Prioridad: P3
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://api.blockchair.com/bitcoin/stats`

#### Mobula API — Fase 9
- URL: https://docs.mobula.io
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), c (gobernanza), e (DePIN), f (L1/L2), g (RWA)
- Uso propuesto: datos de mercado multi-chain
- Prioridad: P3
- Verificado: [P]

#### Messari API — Fase 9
- URL: https://docs.messari.io
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: métricas de activos y research
- Prioridad: P3
- Verificado: [P]

#### CoinMarketCap API — Fase 9
- URL: https://coinmarketcap.com/api/documentation/v1
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: mercado y categorías (plan gratuito con key)
- Prioridad: P3
- Verificado: [P]

### 2.2 DEX, launchpads y seguridad de contratos

#### DexScreener API
- URL: https://docs.dexscreener.com
- Licencia: ToS DexScreener
- API key: no
- Cobertura: a (memecoins), i (establecidos)
- Uso propuesto: pares, m5/h1, pairCreatedAt (pipeline Solana)
- Prioridad: P0
- Verificado: [V] producción
- Endpoint de prueba (T2): `GET https://api.dexscreener.com/latest/dex/search?q=SOL`

#### GeckoTerminal API v2
- URL: https://www.geckoterminal.com/dex-api
- Licencia: ToS CoinGecko
- API key: no
- Cobertura: a (memecoins), f (L1/L2)
- Uso propuesto: pools en tendencia y nuevos por red, OHLCV de la métrica dual
- Prioridad: P0
- Verificado: [V] producción
- Endpoint de prueba (T2): `GET https://api.geckoterminal.com/api/v2/networks?page=1`

#### DexPaprika API
- URL: https://docs.dexpaprika.com
- Licencia: ToS CoinPaprika
- API key: no
- Cobertura: a (memecoins), f (L1/L2)
- Uso propuesto: pools y tokens multi-chain sin key [I]; respaldo de GeckoTerminal
- Prioridad: P1
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://api.dexpaprika.com/networks`

#### Jupiter API (api.jup.ag)
- URL: https://dev.jup.ag
- Licencia: ToS Jupiter
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins)
- Uso propuesto: datos de token Solana; lite-api.jup.ag prohibido (deprecado)
- Prioridad: P2
- Verificado: [V] doc 22 (V2)
- Endpoint de prueba (T2): `GET https://api.jup.ag/tokens/v2/search?query=SOL`

#### Raydium API v3
- URL: https://api-v3.raydium.io/docs
- Licencia: ToS Raydium
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: pools de Raydium (Solana) [I]
- Prioridad: P3
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://api-v3.raydium.io/main/info`

#### PumpPortal WebSocket
- URL: https://pumpportal.fun
- Licencia: ToS PumpPortal
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: lanzamientos en pump.fun (producción)
- Prioridad: P0
- Verificado: [V] producción
- Endpoint de prueba (T2): `GET https://pumpportal.fun`

#### RugCheck API
- URL: https://api.rugcheck.xyz/swagger
- Licencia: ToS RugCheck
- API key: no
- Cobertura: a (memecoins), i (establecidos)
- Uso propuesto: authorities, holders, LP (dossier)
- Prioridad: P0
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://api.rugcheck.xyz/v1/stats/recent`

#### GoPlus Security API
- URL: https://docs.gopluslabs.io
- Licencia: ToS GoPlus
- API key: no
- Cobertura: a (memecoins), i (establecidos)
- Uso propuesto: seguridad de contratos Solana/EVM (dossier)
- Prioridad: P0
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://api.gopluslabs.io/api/v1/supported_chains`

#### Honeypot.is
- URL: https://honeypot.is
- Licencia: ToS Honeypot.is
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: simulación compra/venta EVM
- Prioridad: P1
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://api.honeypot.is/v2/IsHoneypot?address=0x4200000000000000000000000000000000000006&chainID=8453`

#### Orca API (Whirlpools) — Fase 9
- URL: https://docs.orca.so
- Licencia: ToS del proveedor
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: pools de Orca en Solana [I]
- Prioridad: P3
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://api.orca.so/v2/solana/tokens?limit=1`

#### Meteora DLMM API — Fase 9
- URL: https://docs.meteora.ag
- Licencia: ToS del proveedor
- API key: no
- Cobertura: a (memecoins), i (establecidos)
- Uso propuesto: pools de Meteora (arc tiene su liquidez ahí [V])
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://dlmm-api.meteora.ag/pair/all_with_pagination?limit=1`

#### Birdeye API — Fase 9
- URL: https://docs.birdeye.so
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins)
- Uso propuesto: datos de tokens Solana/EVM
- Prioridad: P3
- Verificado: [P]

#### DEXTools API — Fase 9
- URL: https://developer.dextools.io
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins)
- Uso propuesto: pools y auditorías DEX
- Prioridad: P3
- Verificado: [P]

#### Defined.fi API — Fase 9
- URL: https://docs.defined.fi
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins)
- Uso propuesto: datos DEX en tiempo real
- Prioridad: P3
- Verificado: [P]

### 2.3 Exploradores, RPC y datos on-chain

#### Etherscan API v2 (multi-chain: Ethereum, Base, Arbitrum, Optimism, Blast)
- URL: https://docs.etherscan.io
- Licencia: ToS Etherscan
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), c (gobernanza), f (L1/L2), g (RWA)
- Uso propuesto: holders y transferencias EVM; pide key gratuita [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://api.etherscan.io/v2/api?chainid=1&module=stats&action=ethprice`

#### Blockscout API (instancias públicas)
- URL: https://docs.blockscout.com
- Licencia: GPL-3.0 (código)
- API key: no
- Cobertura: a (memecoins), c (gobernanza), f (L1/L2), g (RWA), i (establecidos)
- Uso propuesto: holders y transferencias EVM sin key [I]: alternativa a Etherscan
- Prioridad: P1
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://base.blockscout.com/api/v2/stats`

#### Solscan Pro API
- URL: https://pro-api.solscan.io
- Licencia: ToS Solscan
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), i (establecidos)
- Uso propuesto: holders Solana; la pública pide key [I]
- Prioridad: P3
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://public-api.solscan.io/chaininfo`

#### Solana RPC público
- URL: https://solana.com/docs/rpc
- Licencia: ToS Solana Foundation
- API key: no
- Cobertura: a (memecoins), i (establecidos)
- Uso propuesto: getTokenLargestAccounts (holders) con límite estricto [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `POST https://api.mainnet-beta.solana.com`

#### Helius RPC/DAS
- URL: https://docs.helius.dev
- Licencia: ToS Helius
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), i (establecidos)
- Uso propuesto: DAS y webhooks (1M req/mes gratis)
- Prioridad: P3
- Verificado: [V] doc 13 (key)
- Endpoint de prueba (T2): `GET https://mainnet.helius-rpc.com`

#### mempool.space
- URL: https://mempool.space/docs/api
- Licencia: AGPL-3.0 (código)
- API key: no
- Cobertura: h (blue chips)
- Uso propuesto: fees y actividad de Bitcoin
- Prioridad: P2
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://mempool.space/api/v1/fees/recommended`

#### Blockstream Esplora
- URL: https://github.com/Blockstream/esplora/blob/master/API.md
- Licencia: MIT (código)
- API key: no
- Cobertura: h (blue chips)
- Uso propuesto: altura y actividad on-chain de Bitcoin [I]
- Prioridad: P3
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://blockstream.info/api/blocks/tip/height`

#### Moralis API — Fase 9
- URL: https://docs.moralis.com
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), i (establecidos)
- Uso propuesto: holders y transferencias EVM/Solana
- Prioridad: P3
- Verificado: [P]

#### GoldRush (Covalent) API — Fase 9
- URL: https://goldrush.dev/docs
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), i (establecidos)
- Uso propuesto: balances y transferencias multi-chain
- Prioridad: P3
- Verificado: [P]

#### Alchemy API — Fase 9
- URL: https://docs.alchemy.com
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), i (establecidos)
- Uso propuesto: RPC y datos de tokens
- Prioridad: P3
- Verificado: [P]

#### Bitquery API — Fase 9
- URL: https://docs.bitquery.io
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), i (establecidos)
- Uso propuesto: GraphQL on-chain multi-chain
- Prioridad: P3
- Verificado: [P]

#### Dune API — Fase 9
- URL: https://docs.dune.com/api-reference
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: consultas SQL on-chain
- Prioridad: P3
- Verificado: [P]

#### Flipside API — Fase 9
- URL: https://docs.flipsidecrypto.xyz
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: consultas SQL on-chain
- Prioridad: P3
- Verificado: [P]

#### The Graph (subgraphs) — Fase 9
- URL: https://thegraph.com/docs
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: c (gobernanza), d (sintéticos), g (RWA)
- Uso propuesto: subgraphs de protocolos (Uniswap, Aave)
- Prioridad: P3
- Verificado: [P]

#### Arkham Intelligence API — Fase 9
- URL: https://arkham.com
- Licencia: ToS del proveedor
- API key: sí (de pago)
- Cobertura: a (memecoins), h (blue chips)
- Uso propuesto: etiquetas de entidades (ballenas)
- Prioridad: P3
- Verificado: [P]

#### Glassnode API — Fase 9
- URL: https://docs.glassnode.com
- Licencia: ToS del proveedor
- API key: sí (de pago)
- Cobertura: h (blue chips)
- Uso propuesto: métricas on-chain de BTC/ETH
- Prioridad: P3
- Verificado: [P]

#### CryptoQuant API — Fase 9
- URL: https://cryptoquant.com/docs
- Licencia: ToS del proveedor
- API key: sí (de pago)
- Cobertura: h (blue chips)
- Uso propuesto: flujos de exchanges
- Prioridad: P3
- Verificado: [P]

### 2.4 DeFi (TVL, fees, yields)

#### DefiLlama TVL (chains, protocols)
- URL: https://defillama.com/docs/api
- Licencia: API pública (adapters sin licencia)
- API key: no
- Cobertura: c (gobernanza), e (DePIN), f (L1/L2), g (RWA), i (establecidos)
- Uso propuesto: TVL por chain y protocolo (f, c, g, e, i)
- Prioridad: P0
- Verificado: [V] Fase 7
- Endpoint de prueba (T2): `GET https://api.llama.fi/v2/chains`

#### DefiLlama fees y DEX por chain/protocolo
- URL: https://defillama.com/docs/api
- Licencia: API pública
- API key: no
- Cobertura: c (gobernanza), e (DePIN), f (L1/L2), g (RWA)
- Uso propuesto: fees (c, e, g) y volumen DEX (f)
- Prioridad: P0
- Verificado: [V] Fase 7
- Endpoint de prueba (T2): `GET https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true`

#### DefiLlama stablecoins
- URL: https://defillama.com/docs/api
- Licencia: API pública
- API key: no
- Cobertura: d (sintéticos)
- Uso propuesto: peg y circulante (d2: stables algorítmicas)
- Prioridad: P1
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://stablecoins.llama.fi/stablecoins?includePrices=false`

#### DefiLlama yields
- URL: https://defillama.com/docs/api
- Licencia: API pública
- API key: no
- Cobertura: c (gobernanza), g (RWA)
- Uso propuesto: APY por pool (yield de RWA y DeFi) [I]
- Prioridad: P1
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://yields.llama.fi/pools`

#### DefiLlama derivatives overview
- URL: https://defillama.com/pro-api
- Licencia: de pago
- API key: sí (de pago)
- Cobertura: d (sintéticos)
- Uso propuesto: volumen de derivados: 402
- Prioridad: P3
- Verificado: [V] doc 23 (402)
- Endpoint de prueba (T2): `GET https://api.llama.fi/overview/derivatives?excludeTotalDataChart=true`

#### DefiLlama emissions (unlocks)
- URL: https://defillama.com/pro-api
- Licencia: de pago
- API key: sí (de pago)
- Cobertura: c (gobernanza), e (DePIN)
- Uso propuesto: unlocks: 402 (se usa FDV/mcap como proxy)
- Prioridad: P3
- Verificado: [V] doc 23 (402)
- Endpoint de prueba (T2): `GET https://api.llama.fi/emissions`

#### growthepie
- URL: https://docs.growthepie.xyz
- Licencia: MIT (código)
- API key: no
- Cobertura: f (L1/L2)
- Uso propuesto: métricas de L2 (actividad, fees)
- Prioridad: P1
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://api.growthepie.xyz/v1/master.json`

#### L2BEAT
- URL: https://l2beat.com
- Licencia: MIT (código)
- API key: no
- Cobertura: f (L1/L2)
- Uso propuesto: TVS y riesgo de L2
- Prioridad: P1
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://l2beat.com/api/scaling/summary`

#### Token Terminal
- URL: https://tokenterminal.com
- Licencia: de pago
- API key: sí (de pago)
- Cobertura: c (gobernanza), e (DePIN), f (L1/L2)
- Uso propuesto: ingresos por protocolo: requiere plan
- Prioridad: P3
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://api.tokenterminal.com/v2/projects`

### 2.5 Derivados

#### Hyperliquid info API
- URL: https://hyperliquid.gitbook.io
- Licencia: API pública
- API key: no
- Cobertura: b (preventa), d (sintéticos), h (blue chips)
- Uso propuesto: funding, OI, basis de todos los perps (d, h)
- Prioridad: P0
- Verificado: [V] doc 23 / Fase 8
- Endpoint de prueba (T2): `POST https://api.hyperliquid.xyz/info`

#### dYdX v4 indexer
- URL: https://docs.dydx.exchange
- Licencia: API pública (código propietario)
- API key: no
- Cobertura: d (sintéticos)
- Uso propuesto: perps: OI y funding (respaldo)
- Prioridad: P1
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://indexer.dydx.trade/v4/perpetualMarkets`

#### GMX Arbitrum API
- URL: https://docs.gmx.io
- Licencia: API pública (código BUSL)
- API key: no
- Cobertura: d (sintéticos)
- Uso propuesto: precios de perps de GMX
- Prioridad: P2
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://arbitrum-api.gmxinfra.io/prices/tickers`

#### Deribit API pública (DVOL)
- URL: https://docs.deribit.com
- Licencia: API pública
- API key: no
- Cobertura: h (blue chips)
- Uso propuesto: volatilidad implícita (energía M de h)
- Prioridad: P1
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://www.deribit.com/api/v2/public/get_index_price?index_name=btc_usd`

#### Aevo API
- URL: https://api-docs.aevo.xyz
- Licencia: API pública
- API key: no
- Cobertura: b (preventa), d (sintéticos)
- Uso propuesto: pre-IPO / pre-lanzamiento (b)
- Prioridad: P1
- Verificado: [V] doc 23 / Fase 8
- Endpoint de prueba (T2): `GET https://api.aevo.xyz/markets`

#### Binance Futures (fapi)
- URL: https://binance-docs.github.io/apidocs/futures
- Licencia: ToS Binance
- API key: no
- Cobertura: d (sintéticos), h (blue chips)
- Uso propuesto: funding; suele dar 451 desde EE.UU. [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://fapi.binance.com/fapi/v1/premiumIndex?symbol=BTCUSDT`

#### Gains Network (gTrade) backend API — Fase 9
- URL: https://docs.gains.trade/developer/integrators/backend
- Licencia: [P]
- API key: no
- Cobertura: d (sintéticos), h (blue chips)
- Uso propuesto: OI por par, funding, skew (perps sintéticos de cripto, forex y acciones)
- Prioridad: P1
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Drift Protocol data API (Solana perps) — Fase 9
- URL: https://data.api.drift.trade
- Licencia: [P]
- API key: no
- Cobertura: d (sintéticos)
- Uso propuesto: funding y OI de perps en Solana [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://data.api.drift.trade/stats/markets`

#### CoinGlass API — Fase 9
- URL: https://docs.coinglass.com
- Licencia: ToS CoinGlass
- API key: sí (gratuita con registro)
- Cobertura: d (sintéticos), h (blue chips)
- Uso propuesto: funding/OI/liquidaciones agregadas: pide key
- Prioridad: P3
- Verificado: [P]

#### Kaiko — Fase 9
- URL: https://docs.kaiko.com
- Licencia: ToS del proveedor
- API key: sí (de pago)
- Cobertura: d (sintéticos), h (blue chips)
- Uso propuesto: datos institucionales de mercado
- Prioridad: P3
- Verificado: [P]

### 2.6 Gobernanza

#### Snapshot GraphQL
- URL: https://docs.snapshot.box
- Licencia: MIT (código archivado)
- API key: no
- Cobertura: c (gobernanza)
- Uso propuesto: propuestas activas (evento de gobernanza de c)
- Prioridad: P0
- Verificado: [V] doc 23 / Fase 8
- Endpoint de prueba (T2): `POST https://hub.snapshot.org/graphql`

#### Tally API
- URL: https://docs.tally.xyz
- Licencia: ToS Tally
- API key: sí (gratuita con registro)
- Cobertura: c (gobernanza)
- Uso propuesto: gobernanza on-chain: pide key (401)
- Prioridad: P3
- Verificado: [V] doc 23 (401)
- Endpoint de prueba (T2): `POST https://api.tally.xyz/query`

### 2.7 RWA

#### RWA.xyz
- URL: https://rwa.xyz
- Licencia: ToS RWA.xyz
- API key: sí (gratuita con registro)
- Cobertura: g (RWA)
- Uso propuesto: activos tokenizados: sin acceso sin key (404)
- Prioridad: P3
- Verificado: [V] doc 23 (404)
- Endpoint de prueba (T2): `GET https://api.rwa.xyz/v3/assets`

#### Ondo Finance API — Fase 9
- URL: https://docs.ondo.finance/api-reference/overview
- Licencia: [P]
- API key: sí (gratuita con registro)
- Cobertura: g (RWA)
- Uso propuesto: Ondo Stocks (acciones tokenizadas) y portafolios: spec OpenAPI pública
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Centrifuge API — Fase 9
- URL: https://docs.centrifuge.io
- Licencia: [P]
- API key: no
- Cobertura: g (RWA)
- Uso propuesto: pools de crédito tokenizado (TVL, NAV) [P]
- Prioridad: P2
- Verificado: [P]

#### Polymesh (SubQuery / API pública) — Fase 9
- URL: https://developers.polymesh.network
- Licencia: [P]
- API key: no
- Cobertura: g (RWA)
- Uso propuesto: activos de seguridad tokenizados [P]
- Prioridad: P3
- Verificado: [P]

#### Maple Finance API — Fase 9
- URL: https://docs.maple.finance
- Licencia: [P]
- API key: no
- Cobertura: g (RWA)
- Uso propuesto: préstamos institucionales on-chain [P]
- Prioridad: P3
- Verificado: [P]

### 2.8 Sentimiento

#### alternative.me Fear & Greed
- URL: https://alternative.me/crypto/fear-and-greed-index
- Licencia: ToS alternative.me
- API key: no
- Cobertura: h (blue chips)
- Uso propuesto: sentimiento contrarian (h)
- Prioridad: P0
- Verificado: [V] doc 23
- Endpoint de prueba (T2): `GET https://api.alternative.me/fng/?limit=1`

#### CoinGecko trending
- URL: https://www.coingecko.com/en/api
- Licencia: ToS CoinGecko
- API key: no
- Cobertura: a (memecoins), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: atención (búsquedas 24 h)
- Prioridad: P0
- Verificado: [V] doc 26
- Endpoint de prueba (T2): `GET https://api.coingecko.com/api/v3/search/trending`

#### Santiment API — Fase 9
- URL: https://academy.santiment.net/sanapi
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: métricas sociales y on-chain
- Prioridad: P3
- Verificado: [P]

#### LunarCrush API — Fase 9
- URL: https://lunarcrush.com/developers
- Licencia: ToS del proveedor
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: atención social por activo
- Prioridad: P3
- Verificado: [P]

### 2.9 Noticias

#### GDELT DOC 2.0
- URL: https://blog.gdeltproject.org
- Licencia: abierto
- API key: no
- Cobertura: b (preventa), h (blue chips)
- Uso propuesto: volumen de noticias (429 frecuente desde Actions)
- Prioridad: P2
- Verificado: [V] doc 26
- Endpoint de prueba (T2): `GET https://api.gdeltproject.org/api/v2/doc/doc?query=bitcoin&mode=timelinevolraw&format=json&timespan=24h`

#### Google News RSS
- URL: https://news.google.com
- Licencia: ToS Google
- API key: no
- Cobertura: b (preventa), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: menciones en noticias por activo [I]
- Prioridad: P1
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://news.google.com/rss/search?q=bitcoin&hl=en-US&gl=US&ceid=US:en`

#### CryptoPanic API
- URL: https://cryptopanic.com/developers/api
- Licencia: ToS CryptoPanic
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: agregador de noticias cripto: pide key gratuita [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://cryptopanic.com/api/v1/posts/?public=true`

#### CoinDesk RSS
- URL: https://www.coindesk.com
- Licencia: ToS CoinDesk
- API key: no
- Cobertura: b (preventa), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: menciones (colector T1)
- Prioridad: P0
- Verificado: [V] doc 26
- Endpoint de prueba (T2): `GET https://www.coindesk.com/arc/outboundfeeds/rss/`

#### Cointelegraph RSS
- URL: https://cointelegraph.com
- Licencia: ToS Cointelegraph
- API key: no
- Cobertura: b (preventa), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: menciones (colector T1)
- Prioridad: P0
- Verificado: [V] doc 26
- Endpoint de prueba (T2): `GET https://cointelegraph.com/rss`

#### Decrypt RSS
- URL: https://decrypt.co
- Licencia: ToS Decrypt
- API key: no
- Cobertura: b (preventa), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: menciones (colector T1)
- Prioridad: P0
- Verificado: [V] doc 26
- Endpoint de prueba (T2): `GET https://decrypt.co/feed`

#### The Block RSS
- URL: https://www.theblock.co
- Licencia: ToS The Block
- API key: no
- Cobertura: b (preventa), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: menciones (colector T1)
- Prioridad: P0
- Verificado: [V] doc 26
- Endpoint de prueba (T2): `GET https://www.theblock.co/rss.xml`

### 2.10 Social

#### Reddit RSS
- URL: https://www.reddit.com
- Licencia: ToS Reddit
- API key: no
- Cobertura: a (memecoins), c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: menciones; 429 por IP desde Actions
- Prioridad: P1
- Verificado: [V] doc 26
- Endpoint de prueba (T2): `GET https://www.reddit.com/r/CryptoCurrency/new/.rss`

#### Telegram t.me/s (canales públicos)
- URL: https://t.me
- Licencia: ToS Telegram
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: menciones (colector T1)
- Prioridad: P0
- Verificado: [V] doc 26
- Endpoint de prueba (T2): `GET https://t.me/s/pumpfun`

#### Hacker News (Algolia)
- URL: https://hn.algolia.com/api
- Licencia: ToS Algolia
- API key: no
- Cobertura: c (gobernanza), e (DePIN), f (L1/L2), h (blue chips)
- Uso propuesto: atención técnica (L1/L2, infra)
- Prioridad: P1
- Verificado: [V] doc 26
- Endpoint de prueba (T2): `GET https://hn.algolia.com/api/v1/search_by_date?query=crypto&tags=story&hitsPerPage=1`

#### 4chan /biz/
- URL: https://github.com/4chan/4chan-API
- Licencia: ToS 4chan
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: menciones de CA (memecoins)
- Prioridad: P1
- Verificado: [V] doc 26
- Endpoint de prueba (T2): `GET https://a.4cdn.org/biz/catalog.json`

#### Bluesky búsqueda pública
- URL: https://docs.bsky.app
- Licencia: ToS Bluesky
- API key: no
- Cobertura: a (memecoins), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: menciones: 403 sin auth
- Prioridad: P3
- Verificado: [V] doc 26 (403)
- Endpoint de prueba (T2): `GET https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts?q=bitcoin&limit=1`

#### ApeWisdom
- URL: https://apewisdom.io/api
- Licencia: ToS ApeWisdom
- API key: no
- Cobertura: a (memecoins), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: ranking de menciones en Reddit/4chan por ticker (hay capturas en 01_Datos_Crudos/social/apewisdom)
- Prioridad: P1
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://apewisdom.io/api/v1.0/filter/all-crypto/page/1`

### 2.11 Calendario y atención

#### Wikipedia Pageviews
- URL: https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews
- Licencia: CC0 (datos)
- API key: no
- Cobertura: b (preventa), h (blue chips)
- Uso propuesto: atención temática (lib_narrative)
- Prioridad: P1
- Verificado: [V] doc 18
- Endpoint de prueba (T2): `GET https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Bitcoin/daily/20260901/20260930`

#### Wikidata SPARQL
- URL: https://query.wikidata.org
- Licencia: CC0 (datos)
- API key: no
- Cobertura: b (preventa)
- Uso propuesto: fechas de eventos (calendario narrativo)
- Prioridad: P1
- Verificado: [V] doc 18
- Endpoint de prueba (T2): `GET https://query.wikidata.org/sparql?query=SELECT%20%3Fx%20WHERE%20%7B%20wd%3AQ131723%20wdt%3AP31%20%3Fx%20%7D%20LIMIT%201&format=json`

#### CryptoRank API
- URL: https://api.cryptorank.io/docs
- Licencia: ToS CryptoRank
- API key: sí (gratuita con registro)
- Cobertura: b (preventa)
- Uso propuesto: calendario de TGEs y preventas: pide key [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://api.cryptorank.io/v2/currencies?limit=1`

#### CoinMarketCal
- URL: https://coinmarketcal.com/en/api
- Licencia: ToS CoinMarketCal
- API key: sí (gratuita con registro)
- Cobertura: b (preventa), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: eventos por activo (upgrades, listings): pide key [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://developers.coinmarketcal.com/v1/events`

#### three.ws Crypto API
- URL: https://three.ws
- Licencia: ToS three.ws
- API key: no
- Cobertura: a (memecoins), b (preventa)
- Uso propuesto: trending y airdrops (script_82, script_99)
- Prioridad: P1
- Verificado: [V] doc 13
- Endpoint de prueba (T2): `GET https://three.ws/api/crypto/trending`

#### DefiLlama raises
- URL: https://defillama.com/docs/api
- Licencia: API pública (posible pago)
- API key: no
- Cobertura: b (preventa)
- Uso propuesto: rondas de financiación: proxy de TGEs futuros [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://api.llama.fi/raises`

#### Apify: token unlocks calendar (actores gratuitos) — Fase 9
- URL: https://apify.com/foxlabs/token-unlocks-calendar/api
- Licencia: ToS Apify
- API key: sí (gratuita con registro)
- Cobertura: b (preventa), c (gobernanza), e (DePIN)
- Uso propuesto: calendario de unlocks (~326 proyectos, base DefiLlama emissions)
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Coindar — Fase 9
- URL: https://coindar.org/en/api
- Licencia: ToS Coindar
- API key: sí (gratuita con registro)
- Cobertura: b (preventa), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: eventos por activo [P]
- Prioridad: P3
- Verificado: [P]

### 2.12 MCP servers y directorios

#### modelcontextprotocol/servers (fetch, time, memory, git, filesystem)
- URL: https://github.com/modelcontextprotocol/servers
- Licencia: MIT [I]
- API key: no
- Cobertura: herramienta / transversal
- Uso propuesto: referencia oficial; no aporta datos de mercado (uso: herramientas de investigación)
- Prioridad: P3
- Verificado: [P]

#### punkpeye/awesome-mcp-servers (directorio)
- URL: https://github.com/punkpeye/awesome-mcp-servers
- Licencia: MIT [I]
- API key: no
- Cobertura: herramienta / transversal
- Uso propuesto: directorio para relevar MCP cripto: cada uno pasa el checklist del doc 25
- Prioridad: P2
- Verificado: [P]

#### mcp.so (directorio)
- URL: https://mcp.so
- Licencia: ToS mcp.so
- API key: no
- Cobertura: herramienta / transversal
- Uso propuesto: directorio web de MCP servers
- Prioridad: P3
- Verificado: [P]

#### npm keyword mcp-server
- URL: https://www.npmjs.com/search?q=keywords:mcp-server
- Licencia: varía por paquete
- API key: no
- Cobertura: herramienta / transversal
- Uso propuesto: descubrimiento; revisar postinstall antes de cualquier uso (doc 25)
- Prioridad: P3
- Verificado: [P]

#### CoinGecko MCP (@coingecko/coingecko-mcp)
- URL: https://github.com/coingecko/coingecko-typescript
- Licencia: Apache-2.0
- API key: no
- Cobertura: c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: consultas manuales de investigación (no para el pipeline)
- Prioridad: P3
- Verificado: [V] doc 23

#### GoPlusSecurity/goplus-mcp
- URL: https://github.com/GoPlusSecurity/goplus-mcp
- Licencia: Apache-2.0
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: descartado: sin push desde 2025-05
- Prioridad: P3
- Verificado: [V] doc 23

#### caiovicentino/hyperliquid-mcp-server
- URL: https://github.com/caiovicentino/hyperliquid-mcp-server
- Licencia: MIT
- API key: no
- Cobertura: d (sintéticos)
- Uso propuesto: descartado: inactivo > 6 meses
- Prioridad: P3
- Verificado: [V] doc 23

#### hypurrquant/perp-cli
- URL: https://github.com/hypurrquant/perp-cli
- Licencia: MIT
- API key: no
- Cobertura: d (sintéticos)
- Uso propuesto: orientado a operar: solo referencia de lectura
- Prioridad: P3
- Verificado: [V] doc 23

#### vibeforge1111/dexscreener-cli-mcp-tool
- URL: https://github.com/vibeforge1111/dexscreener-cli-mcp-tool
- Licencia: sin licencia
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: descartado: sin licencia
- Prioridad: P3
- Verificado: [V] doc 23

#### DefiLlama/defillama-skills
- URL: https://github.com/DefiLlama/defillama-skills
- Licencia: sin licencia
- API key: no
- Cobertura: c (gobernanza), e (DePIN), f (L1/L2), g (RWA)
- Uso propuesto: descartado: inactivo y sin licencia
- Prioridad: P3
- Verificado: [V] doc 23

#### CoinGecko MCP remoto (free keyless) — Fase 9
- URL: https://docs.coingecko.com/ai-integration/mcp-server
- Licencia: oficial CoinGecko
- API key: no
- Cobertura: c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: MCP oficial sin key (límite compartido): consultas de investigación
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)
- Endpoint de prueba (T2): `GET https://mcp.api.coingecko.com/`

#### Kukapay MCP suite — Fase 9
- URL: https://github.com/kukapay/kukapay-mcp-servers
- Licencia: [P]
- API key: no
- Cobertura: a (memecoins), c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: suite de >100 MCP cripto; índice para elegir uno por fuente
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Kukapay dexscreener-mcp — Fase 9
- URL: https://github.com/kukapay/dexscreener-mcp
- Licencia: [P]
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: pares y tokens de DexScreener vía MCP
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Kukapay crypto-feargreed-mcp — Fase 9
- URL: https://github.com/kukapay/crypto-feargreed-mcp
- Licencia: [P]
- API key: no
- Cobertura: h (blue chips)
- Uso propuesto: Fear & Greed vía MCP
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Kukapay whale-tracker-mcp — Fase 9
- URL: https://github.com/kukapay/whale-tracker-mcp
- Licencia: [P]
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), h (blue chips)
- Uso propuesto: transacciones de ballenas (fuente subyacente con key [I])
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Kukapay crypto-sentiment-mcp (Santiment) — Fase 9
- URL: https://github.com/kukapay/crypto-sentiment-mcp
- Licencia: [P]
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: sentimiento social de Santiment
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Kukapay funding-rates-mcp — Fase 9
- URL: https://github.com/kukapay/funding-rates-mcp
- Licencia: [P]
- API key: no
- Cobertura: d (sintéticos), h (blue chips)
- Uso propuesto: funding de varios exchanges (comparar con Hyperliquid)
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Kukapay defi-yields-mcp — Fase 9
- URL: https://github.com/kukapay/defi-yields-mcp
- Licencia: [P]
- API key: no
- Cobertura: c (gobernanza), g (RWA)
- Uso propuesto: yields de DefiLlama vía MCP
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Kukapay crypto-projects-mcp (Mobula) — Fase 9
- URL: https://github.com/kukapay/crypto-projects-mcp
- Licencia: [P]
- API key: sí (gratuita con registro)
- Cobertura: c (gobernanza), e (DePIN), f (L1/L2), g (RWA)
- Uso propuesto: datos de proyectos de Mobula
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### IQAI mcp-defillama — Fase 9
- URL: https://github.com/IQAIcom/mcp-defillama
- Licencia: [P]
- API key: no
- Cobertura: c (gobernanza), e (DePIN), f (L1/L2), g (RWA)
- Uso propuesto: TVL, DEX, stablecoins, yields de DefiLlama
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### dcSpark mcp-server-defillama — Fase 9
- URL: https://github.com/dcSpark/mcp-server-defillama
- Licencia: [P]
- API key: no
- Cobertura: c (gobernanza), e (DePIN), f (L1/L2), g (RWA)
- Uso propuesto: DefiLlama vía MCP
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### defillama-mcp (proxy de la API pública) — Fase 9
- URL: https://github.com/nic0xflamel/defillama-mcp
- Licencia: [P]
- API key: no
- Cobertura: c (gobernanza), e (DePIN), f (L1/L2), g (RWA)
- Uso propuesto: DefiLlama vía MCP
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### bitcoin-mcp (Bitcoin y Lightning) — Fase 9
- URL: https://github.com/AbdelStark/bitcoin-mcp
- Licencia: [P]
- API key: no
- Cobertura: h (blue chips)
- Uso propuesto: consultas on-chain de Bitcoin
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Tatum blockchain-mcp (130+ redes) — Fase 9
- URL: https://github.com/tatumio/blockchain-mcp
- Licencia: [P]
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), c (gobernanza), f (L1/L2), h (blue chips)
- Uso propuesto: RPC y datos multi-red
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Armor crypto MCP — Fase 9
- URL: https://github.com/armorwallet/armor-crypto-mcp
- Licencia: [P]
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins)
- Uso propuesto: orientado a wallets y swaps: solo referencia
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Impa hyperliquid-mcp — Fase 9
- URL: https://github.com/Impa-Ventures/hyperliquid-mcp
- Licencia: [P]
- API key: no
- Cobertura: d (sintéticos)
- Uso propuesto: datos de Hyperliquid vía MCP
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### edkdev hyperliquid-mcp — Fase 9
- URL: https://github.com/edkdev/hyperliquid-mcp
- Licencia: [P]
- API key: no
- Cobertura: d (sintéticos)
- Uso propuesto: SDK oficial de Hyperliquid vía MCP (incluye trading)
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### HypeDexer MCP — Fase 9
- URL: https://github.com/Hypedexer/hypedexer-mcp
- Licencia: [P]
- API key: sí (gratuita con registro)
- Cobertura: d (sintéticos)
- Uso propuesto: datos históricos de Hyperliquid (API HypeDexer)
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### defi-yield-scanner-mcp — Fase 9
- URL: https://github.com/34t34f3/defi-yield-scanner-mcp
- Licencia: [P]
- API key: no
- Cobertura: a (memecoins), c (gobernanza), g (RWA)
- Uso propuesto: yields + riesgo de token (DexScreener + DefiLlama)
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Octav API MCP — Fase 9
- URL: https://github.com/Octav-Labs/octav-api-mcp
- Licencia: [P]
- API key: sí (gratuita con registro)
- Cobertura: c (gobernanza), g (RWA)
- Uso propuesto: portafolios y DeFi en 20+ chains
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Smithery: DefiLlama API Proxy (Kryptoskatt) — Fase 9
- URL: https://smithery.ai/servers/Kryptoskatt/mcp-server
- Licencia: [P]
- API key: no
- Cobertura: c (gobernanza), e (DePIN), f (L1/L2), g (RWA)
- Uso propuesto: DefiLlama con tools generados desde su OpenAPI
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Smithery: cat-dexscreener — Fase 9
- URL: https://smithery.ai/servers/catwhisperingninja/cat-dexscreener
- Licencia: [P]
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: pares de DexScreener por chain/dirección
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### TensorBlock awesome-mcp-servers (finance & crypto) — Fase 9
- URL: https://github.com/TensorBlock/awesome-mcp-servers
- Licencia: [P]
- API key: no
- Cobertura: herramienta / transversal
- Uso propuesto: directorio para relevar MCP cripto
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### DeMCP awesome-web3-mcp-servers — Fase 9
- URL: https://github.com/demcp/awesome-web3-mcp-servers
- Licencia: [P]
- API key: no
- Cobertura: herramienta / transversal
- Uso propuesto: directorio para relevar MCP cripto
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Hive awesome-crypto-mcp-servers — Fase 9
- URL: https://github.com/hive-intel/awesome-crypto-mcp-servers
- Licencia: [P]
- API key: no
- Cobertura: herramienta / transversal
- Uso propuesto: directorio para relevar MCP cripto
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### PulseMCP (directorio) — Fase 9
- URL: https://www.pulsemcp.com
- Licencia: ToS del sitio
- API key: no
- Cobertura: herramienta / transversal
- Uso propuesto: directorio / registro de MCP
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Glama MCP (directorio) — Fase 9
- URL: https://glama.ai/mcp/servers
- Licencia: ToS del sitio
- API key: no
- Cobertura: herramienta / transversal
- Uso propuesto: directorio / registro de MCP
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Smithery (registro de MCP) — Fase 9
- URL: https://smithery.ai
- Licencia: ToS del sitio
- API key: no
- Cobertura: herramienta / transversal
- Uso propuesto: directorio / registro de MCP
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

### 2.13 Repos con lógica especial (NLP, régimen, modelos)

#### bashtage/arch (GARCH, HAR)
- URL: https://github.com/bashtage/arch
- Licencia: NCSA
- API key: no
- Cobertura: h (blue chips)
- Uso propuesto: EGARCH/HAR cuando el GARCH en Python puro no alcance
- Prioridad: P2
- Verificado: [V] doc 23

#### deepcharles/ruptures (changepoint detection)
- URL: https://github.com/deepcharles/ruptures
- Licencia: BSD-2-Clause [I]
- API key: no
- Cobertura: f (L1/L2), h (blue chips)
- Uso propuesto: detección de régimen (cambios de nivel/varianza) en h y f [I]
- Prioridad: P2
- Verificado: [P]

#### MAPIE (intervalos conformales)
- URL: https://github.com/scikit-learn-contrib/MAPIE
- Licencia: BSD-3-Clause
- API key: no
- Cobertura: h (blue chips)
- Uso propuesto: intervalos con cobertura garantizada
- Prioridad: P3
- Verificado: [V] doc 23

#### crepes (conformal, liviano)
- URL: https://github.com/henrikbostrom/crepes
- Licencia: BSD-3-Clause
- API key: no
- Cobertura: h (blue chips)
- Uso propuesto: ídem, sin scikit-learn completo
- Prioridad: P3
- Verificado: [V] doc 23

#### ProsusAI/finbert (sentimiento financiero)
- URL: https://github.com/ProsusAI/finBERT
- Licencia: Apache-2.0 [I]
- API key: no
- Cobertura: b (preventa), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: sentimiento de titulares (requiere torch: pesado para Actions) [I]
- Prioridad: P3
- Verificado: [P]

#### pyahocorasick
- URL: https://github.com/WojciechMula/pyahocorasick
- Licencia: BSD-3-Clause
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: matching de miles de identificadores en el colector
- Prioridad: P2
- Verificado: [V] doc 18

#### GLiNER (NER zero-shot)
- URL: https://github.com/urchade/GLiNER
- Licencia: Apache-2.0
- API key: no
- Cobertura: b (preventa)
- Uso propuesto: extraer entidades de noticias (requiere torch)
- Prioridad: P3
- Verificado: [V] doc 18

#### D4Vinci/Scrapling
- URL: https://github.com/D4Vinci/Scrapling
- Licencia: BSD-3-Clause
- API key: no
- Cobertura: a (memecoins), b (preventa)
- Uso propuesto: scraping condicional (solo núcleo)
- Prioridad: P3
- Verificado: [V] doc 25

#### statsmodels
- URL: https://github.com/statsmodels/statsmodels
- Licencia: BSD-3-Clause [I]
- API key: no
- Cobertura: f (L1/L2), h (blue chips)
- Uso propuesto: tests de estacionariedad y event studies
- Prioridad: P3
- Verificado: [P]

#### AI4Finance FinGPT — Fase 9
- URL: https://github.com/AI4Finance-Foundation/FinGPT
- Licencia: MIT [web]
- API key: no
- Cobertura: b (preventa), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: LLM financiero abierto (sentimiento de titulares)
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### ElKulako/cryptobert (Hugging Face) — Fase 9
- URL: https://huggingface.co/ElKulako/cryptobert
- Licencia: [P]
- API key: no
- Cobertura: a (memecoins), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: sentimiento bullish/bearish/neutral de posts cripto (3,2 M posts)
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### vaderSentiment — Fase 9
- URL: https://github.com/cjhutto/vaderSentiment
- Licencia: MIT [I]
- API key: no
- Cobertura: a (memecoins), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: sentimiento por reglas, liviano (sin torch)
- Prioridad: P2
- Verificado: [P]

#### cardiffnlp/twitter-roberta-base-sentiment — Fase 9
- URL: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest
- Licencia: [P]
- API key: no
- Cobertura: a (memecoins), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: sentimiento de texto social (requiere torch)
- Prioridad: P3
- Verificado: [P]

#### bayesian_changepoint_detection (bayescd) — Fase 9
- URL: https://github.com/hildensia/bayesian_changepoint_detection
- Licencia: [P]
- API key: no
- Cobertura: f (L1/L2), h (blue chips)
- Uso propuesto: detección de régimen en h y f (cambios de nivel/varianza)
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### ChangePointLab (BOCPD, PELT, E-Divisive, HSMM) — Fase 9
- URL: https://github.com/DiogoRibeiro7/ChangePointLab
- Licencia: [P]
- API key: no
- Cobertura: f (L1/L2), h (blue chips)
- Uso propuesto: detección de régimen en h y f (cambios de nivel/varianza)
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### bocd (Adams & MacKay 2007, PyPI) — Fase 9
- URL: https://pypi.org/project/bocd/
- Licencia: [P]
- API key: no
- Cobertura: f (L1/L2), h (blue chips)
- Uso propuesto: detección de régimen en h y f (cambios de nivel/varianza)
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### JackKelly/bayesianchangepoint — Fase 9
- URL: https://github.com/JackKelly/bayesianchangepoint
- Licencia: [P]
- API key: no
- Cobertura: f (L1/L2), h (blue chips)
- Uso propuesto: detección de régimen en h y f (cambios de nivel/varianza)
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Rbeast (BEAST: cambios y descomposición) — Fase 9
- URL: https://pypi.org/project/rbeast/
- Licencia: [P]
- API key: no
- Cobertura: f (L1/L2), h (blue chips)
- Uso propuesto: detección de régimen en h y f (cambios de nivel/varianza)
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### hmmlearn (HMM: regímenes ocultos) — Fase 9
- URL: https://github.com/hmmlearn/hmmlearn
- Licencia: BSD-3-Clause [I]
- API key: no
- Cobertura: f (L1/L2), h (blue chips)
- Uso propuesto: detección de régimen en h y f (cambios de nivel/varianza)
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

### 2.14 Papers con código o datos

#### gridcp: Fast Online Changepoint Detection in Python (arXiv 2608.18695) — Fase 9
- URL: https://arxiv.org/abs/2608.18695
- Licencia: paper (código en el paper) [P]
- API key: no
- Cobertura: f (L1/L2), h (blue chips)
- Uso propuesto: changepoint online rápido para regímenes intradía
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### focus / focus-cpt: Fast Online Changepoint Detection (arXiv 2607.19961) — Fase 9
- URL: https://arxiv.org/abs/2607.19961
- Licencia: paper [P]
- API key: no
- Cobertura: f (L1/L2), h (blue chips)
- Uso propuesto: changepoint online (R y Python)
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Catching the Rug (arXiv 2608.20271): XGBoost con 5 min de trading, 6,4 M tokens — Fase 9
- URL: https://arxiv.org/abs/2608.20271
- Licencia: paper
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: features de los primeros 5 min para el riesgo del grupo a
- Prioridad: P1
- Verificado: [V] búsqueda web / alphaXiv 01/10

#### Predicting the success of new crypto-tokens: the Pump.fun case (arXiv 2602.14860) — Fase 9
- URL: https://arxiv.org/abs/2602.14860
- Licencia: paper
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: predictores de graduación en pump.fun
- Prioridad: P1
- Verificado: [V] búsqueda web / alphaXiv 01/10

#### A Midsummer Meme's Dream: manipulaciones en memecoins (arXiv 2507.01963) — Fase 9
- URL: https://arxiv.org/abs/2507.01963
- Licencia: paper
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: secuencia crecimiento artificial -> exit scam (usa MemeChain)
- Prioridad: P2
- Verificado: [V] búsqueda web / alphaXiv 01/10

#### CoinCLIP: viabilidad multimodal de memecoins (arXiv 2412.07591) — Fase 9
- URL: https://arxiv.org/abs/2412.07591
- Licencia: paper
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: logo + texto como señal de viabilidad
- Prioridad: P3
- Verificado: [V] búsqueda web / alphaXiv 01/10

### 2.15 Datasets públicos

#### MemeChain (Zenodo 18246856)
- URL: https://zenodo.org/records/18246856
- Licencia: CC-BY-4.0
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: etiquetas de rug multi-chain para calibrar (709,6 MB)
- Prioridad: P1
- Verificado: [V] doc 18

#### MELT (git-disl/MELT)
- URL: https://github.com/git-disl/MELT
- Licencia: CC BY-NC 4.0
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: no comercial: solo metodología
- Prioridad: P3
- Verificado: [V] doc 23

#### Binance public data (data.binance.vision)
- URL: https://github.com/binance/binance-public-data
- Licencia: ToS Binance
- API key: no
- Cobertura: c (gobernanza), d (sintéticos), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: velas históricas masivas para backtests sin límite de API [I]
- Prioridad: P1
- Verificado: [P]
- Endpoint de prueba (T2): `GET https://data.binance.vision/?prefix=data/spot/daily/klines/BTCUSDT/1d/`

#### Kaggle (datasets cripto)
- URL: https://www.kaggle.com/datasets?search=crypto
- Licencia: varía (muchos CC0/CC-BY)
- API key: sí (gratuita con registro)
- Cobertura: a (memecoins), c (gobernanza), e (DePIN), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: históricos; requiere cuenta para la API [I]
- Prioridad: P3
- Verificado: [P]

#### GDELT 2.0 archivos crudos
- URL: http://data.gdeltproject.org/gdeltv2/lastupdate.txt
- Licencia: abierto
- API key: no
- Cobertura: b (preventa), h (blue chips)
- Uso propuesto: volumen de noticias sin el límite de la API DOC [I]
- Prioridad: P2
- Verificado: [P]
- Endpoint de prueba (T2): `GET http://data.gdeltproject.org/gdeltv2/lastupdate.txt`

#### Wikimedia pageview dumps
- URL: https://dumps.wikimedia.org/other/pageviews/
- Licencia: CC0
- API key: no
- Cobertura: b (preventa), h (blue chips)
- Uso propuesto: atención histórica completa
- Prioridad: P3
- Verificado: [P]

#### jocry/Pumpfun_Memecoin_Corpus (798.430 lanzamientos, 33,58 M trades, graduación etiquetada, jun–jul 2026) — Fase 9
- URL: https://huggingface.co/datasets/jocry/Pumpfun_Memecoin_Corpus
- Licencia: [P] (ver la tarjeta del dataset)
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: calibración del grupo a: graduación vs abandono, concentración, historial del creador
- Prioridad: P0
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### linxy/CryptoCoin (Binance, 2018–2025, actualizado a diario) — Fase 9
- URL: https://huggingface.co/datasets/linxy/CryptoCoin
- Licencia: [P] (ver la tarjeta del dataset)
- API key: no
- Cobertura: d (sintéticos), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: velas históricas multi-activo para c, e, f, g, h
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### Wrigggy/crypto-ohlcv-1m (90 días a 1 min) — Fase 9
- URL: https://huggingface.co/datasets/Wrigggy/crypto-ohlcv-1m
- Licencia: [P] (ver la tarjeta del dataset)
- API key: no
- Cobertura: d (sintéticos), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: vol realizada intradía (HAR-RV) para h
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### arthurneuron/crypto-futures-ohlcv-1m — Fase 9
- URL: https://huggingface.co/datasets/arthurneuron/crypto-futures-ohlcv-1m
- Licencia: [P] (ver la tarjeta del dataset)
- API key: no
- Cobertura: d (sintéticos), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: perps a 1 min para d y h
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### tradecatlabs/binance-futures-ohlcv-2018-2026 — Fase 9
- URL: https://huggingface.co/datasets/tradecatlabs/binance-futures-ohlcv-2018-2026
- Licencia: [P] (ver la tarjeta del dataset)
- API key: no
- Cobertura: d (sintéticos), f (L1/L2), g (RWA), h (blue chips)
- Uso propuesto: histórico de futuros para d y h
- Prioridad: P2
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

#### masonmarker/memecoins-chart-data-low-mc — Fase 9
- URL: https://huggingface.co/datasets/masonmarker/memecoins-chart-data-low-mc
- Licencia: [P] (ver la tarjeta del dataset)
- API key: no
- Cobertura: a (memecoins)
- Uso propuesto: 40.000 puntos de memecoins de baja mcap (Photon)
- Prioridad: P3
- Verificado: [P] hallado por búsqueda web 01/10 (existencia [V]; licencia/actividad sin auditar)

## 3. Prioridades de integración

1. **jocry/Pumpfun_Memecoin_Corpus** (P0, Hugging Face): calibrar el grupo a con graduación vs abandono sobre 798 mil lanzamientos de 2026.
2. **Deribit DVOL** (P1, sin key): completa la energía M del grupo h.
3. **Gains Network backend** y **Drift** (P1/P2): más perps para d.
4. **Blockscout** (P1, sin key): holders EVM para a e i.
5. **Pyth Hermes** (P1, sin key): precio de oráculo para el basis de d.
6. **Paper Catching the Rug** (P1): features de los primeros 5 minutos para el riesgo del grupo a.

## 4. Pendientes

- [P] Correr `probe_inventario.yml` desde Actions (requiere el workflow en main).
- [P] Auditar licencia, actividad y `postinstall` de los MCP de la Fase 9 con el checklist del doc 25 antes de cualquier uso.
- [P] Revisar ToS de uso comercial de cada API.
