---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: INVENTARIO v1.0 (Fase 8, T1); verificación en vivo en T2 (probe_inventario.yml)
last_updated: 2026-10-01
version: 1.0
---

# 28 — Inventario completo de servicios gratuitos

Rótulos: [V] verificado (HTTP o archivo en esta sesión o en un doc anterior, citado) · [I] inferido · [H] hipótesis · [P] pendiente de verificar (lo prueba T2 desde Actions).

**Fuente única:** `04_Config/inventario.json`. De ahí salen este documento y la lista de endpoints que prueba `probe_inventario.py` (workflow manual `probe_inventario.yml`, salida `02_Analisis/diagnostics/inventario_probe.json`). Agregar un servicio = agregar una entrada al JSON.

**Criterio del proyecto** (doc 22 §3): 100% gratuito, sin key o con key gratuita sin tarjeta, licencia permisiva para código que se use, actividad < 6 meses, supply chain revisada. Lo que no cumple igual se lista con el motivo: sirve para no volver a evaluarlo.

## 0. Resumen

- **Servicios inventariados: 91** · con endpoint de prueba para T2: **68** · sin key: **77** · ya verificados en docs/fases anteriores: **58**.
- **Grupos cubiertos: 9/9** (a memecoins, b preventa, c gobernanza, d sintéticos, e DePIN, f L1/L2, g RWA, h blue chips, i establecidos).
- **Datasets públicos:** MemeChain (CC-BY-4.0, etiquetas de rug) y Binance public data (velas históricas masivas) son los dos integrables primero; MELT es no comercial (solo metodología).
- **MCP servers:** ninguno aporta datos de mercado que el pipeline no obtenga ya por HTTP directo; los relevados se listan con su veredicto. No se buscaron repos nuevos fuera del alcance de la sesión: el relevamiento de directorios (awesome-mcp-servers, mcp.so, npm) queda [P] con el checklist del doc 25.
- **Lo que sigue pago o con key** (no se usa): DefiLlama derivatives y emissions (402), Tally (401), RWA.xyz (404 sin key), Token Terminal, CryptoRank, CoinMarketCal, CryptoPanic, Etherscan v2, Solscan, CoinCap v3. Cada uno tiene su alternativa gratuita en la tabla de §1.

| Categoría | Servicios |
|---|---|
| Precios y mercado | 11 |
| DEX, launchpads y seguridad de contratos | 9 |
| Exploradores y RPC | 7 |
| DeFi (TVL, fees, yields) | 9 |
| Derivados | 6 |
| Gobernanza | 2 |
| RWA | 1 |
| Sentimiento | 2 |
| Noticias | 7 |
| Social | 6 |
| Calendario y atención | 6 |
| MCP servers | 10 |
| Repos con lógica especial | 9 |
| Datasets públicos | 6 |

## 1. Cobertura por grupo (qué fuente gratuita alimenta cada componente del doc 27)

| Grupo | Fuentes sin key (P0/P1) | Hueco / alternativa |
|---|---|---|
| a memecoins | DexScreener API, GeckoTerminal API v2, DexPaprika API, PumpPortal WebSocket, RugCheck API, GoPlus Security API, Honeypot.is, Blockscout API, Reddit RSS … | holders históricos (Blockscout / RPC público [P]) |
| b preventa | Hyperliquid info API, Aevo API, Google News RSS, CoinDesk RSS, Cointelegraph RSS, Decrypt RSS, The Block RSS, Wikipedia Pageviews, Wikidata SPARQL … | calendario de TGEs: CryptoRank y CoinMarketCal piden key; three.ws (script_99) hoy devuelve vacío [V]; DefiLlama raises [P] como proxy |
| c gobernanza | CoinGecko API pública, CoinPaprika, Binance data-api, Coinbase Exchange API pública, Blockscout API, DefiLlama TVL, DefiLlama fees y DEX por chain/protocolo, DefiLlama yields, Snapshot GraphQL … | Tally pide key; unlocks de pago → proxy FDV/mcap |
| d sintéticos | CoinGecko API pública, CoinPaprika, Binance data-api, Coinbase Exchange API pública, DefiLlama stablecoins, Hyperliquid info API, dYdX v4 indexer, Aevo API, Reddit RSS … | DefiLlama derivatives 402 → Hyperliquid + dYdX |
| e DePIN | CoinGecko API pública, CoinPaprika, Binance data-api, Coinbase Exchange API pública, DefiLlama TVL, DefiLlama fees y DEX por chain/protocolo, Google News RSS, CoinDesk RSS, Cointelegraph RSS … | nodos/ingresos por proyecto (DePINscan sin API) → fees de DefiLlama solo para 9 protocolos |
| f L1/L2 | CoinGecko API pública, CoinPaprika, Binance data-api, Coinbase Exchange API pública, GeckoTerminal API v2, DexPaprika API, Blockscout API, DefiLlama TVL, DefiLlama fees y DEX por chain/protocolo … | staking flows sin fuente gratuita verificada |
| g RWA | CoinGecko API pública, CoinPaprika, Binance data-api, Coinbase Exchange API pública, Blockscout API, DefiLlama TVL, DefiLlama fees y DEX por chain/protocolo, DefiLlama yields, Google News RSS … | RWA.xyz sin key → DefiLlama RWA + yields |
| h blue chips | CoinGecko API pública, CoinPaprika, Binance data-api, Coinbase Exchange API pública, Kraken API pública, Hyperliquid info API, Deribit API pública, alternative.me Fear & Greed, Google News RSS … | DVOL de Deribit (gratuito, falta conectarlo) |
| i establecidos | DexScreener API, RugCheck API, GoPlus Security API, Blockscout API, DefiLlama TVL | holders con historia (Blockscout / RPC [P]) |

## 2. Servicios

Formato por entrada: URL · licencia · API key · cobertura (grupos) · uso propuesto · prioridad · verificación. El endpoint de prueba es el que usa T2.

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

### 2.3 Exploradores y RPC

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

### 2.12 MCP servers

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

### 2.13 Repos con lógica especial

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

### 2.14 Datasets públicos

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

## 3. Prioridades de integración (lo que más cobertura agrega por esfuerzo)

1. **Deribit DVOL** (P1, sin key): completa la energía M del grupo h (hoy M = 1).
2. **Blockscout** (P1, sin key) en Base / Optimism / Arbitrum: holders y transferencias EVM para los grupos a e i sin depender de Etherscan con key.
3. **DefiLlama yields** (P1): yield por pool para g y c, mejor que fees/TVL.
4. **DexPaprika** (P1): respaldo de GeckoTerminal cuando da 429.
5. **Binance public data** (P1, dataset): velas históricas para validar el scorer h fuera de muestra (walk-forward) sin gastar llamadas de API.
6. **MemeChain** (P1, dataset CC-BY-4.0): etiquetas de rug para calibrar a e i (doc 18 H2).
7. **ApeWisdom y Google News RSS** (P1): menciones por ticker para el colector (doc 26), en especial para grupos c, e, f, g, h donde los RSS cripto ya están.

## 4. Pendientes

- [P] Correr `probe_inventario.yml` (manual) desde Actions: estado, latencia y si pide auth de cada endpoint. Requiere que el workflow esté en main (YIN).
- [P] Relevar los directorios MCP (awesome-mcp-servers, mcp.so, npm `mcp-server`) con el checklist del doc 25; ningún MCP entra al pipeline sin esa auditoría.
- [P] Revisar los ToS de uso comercial de cada API (este inventario verifica acceso técnico, no términos).
