# Servicios Pendientes — Seguimiento por Categoría

Estado: `pendiente` | `en_curso` | `hecho` | `descartado`

## 01_news_mcp (P0)

| Servicio | Estado | Notas |
|----------|--------|-------|
| CryptoPanic | `hecho` | Free 20 req/min, API key opcional, integrable en script_115 |
| CoinDesk RSS Aggregator | `hecho` | 8 fuentes RSS, sin key, Python feedparser |
| CryptoControl SDK | `hecho` | 2000+ fuentes, ML categorization, free 100 req/día |
| CoinGecko News | `pendiente` | Verificar endpoint /news |
| Messari API | `pendiente` | Free tier 100 req/día, necesita key |
| The Block API | `pendiente` | Verificar si tiene free tier |

## 02_social_x (P0)

| Servicio | Estado | Notas |
|----------|--------|-------|
| Agent-Reach | `pendiente` | Cookies requeridas, inestable |
| Nitter instances | `pendiente` | Inestables, sin key |
| Reddit JSON API | `pendiente` | 429 en CryptoMoonShots/memecoins, OK en Solana/CryptoCurrency |
| Telegram t.me/s/ | `hecho` | HTML parseable, 200 OK, sin key |
| 4chan /biz/ | `pendiente` | Evaluar API pública |
| HN Algolia | `hecho` | 200 OK, sin key, usado en script_115 |

## 03_data_blockchain (P1)

| Servicio | Estado | Notas |
|----------|--------|-------|
| Helius (Solana) | `hecho` | Ficha `helius_free.md`: key gratuita (1M créditos/mes), reemplazo de Solscan. P2, requiere key de Dirección |
| Birdeye | `descartado` | Sin key → 401 [V 2026-10-03]. Free "Standard": 30k CU/mes a 1 rps [I]. DexPaprika + GeckoTerminal cubren lo mismo sin key |
| DexScreener | `hecho` | Sin key, rate limit OK |
| GeckoTerminal | `hecho` | Sin key, velas 1m/15m |
| Solscan | `descartado` | `pro-api` v2 → 401 "Token is missing"; `public-api` → 404 [V 2026-10-03]. Alternativa: Helius free |
| MadeOnSol | `pendiente` | Key en secret, endpoints no verificados |
| RugCheck | `hecho` | Sin key, holders/insiders |
| GoPlus Security | `hecho` | Ficha `goplus_security.md`: sin key [V], Solana + EVM, 30 req/min. P1 |
| DexPaprika | `hecho` | Ficha `dexpaprika.md`: sin key [V], pools nuevos por red (`/pools/search`). P1 |
| DefiLlama | `pendiente` | Sin key [V]: `/v2/chains`, `/protocols` (8.476, con categoría), `coins.llama.fi`. `/categories` → 402 (pago). Contexto narrativo por categoría/cadena |
| KyberSwap aggregator | `descartado` | Sin key 200 [V], 3 rps. Cotiza rutas: no aporta a la anticipación. Ningún otro agregador aporta más |

## 04_scrapers (P1)

| Servicio | Estado | Notas |
|----------|--------|-------|
| Crawlee/Apify | `pendiente` | Evaluar free tier |
| Playwright | `pendiente` | Headless browser, recurso intensivo |
| Selenium | `pendiente` | Legacy, más lento |
| Firecrawl | `pendiente` | API key requerida, 403 en search |
| Pump.fun (frontend API + PumpPortal) | `hecho` | Ficha `pumpfun_datos.md`: `/coins` sin key [V]; `/replies` y KOTH → 404 [V]; stream de lanzamientos gratis. P1 |
| Bitcointalk ANN | `hecho` | Ficha `bitcointalk_ann.md`: HTML público, 40 hilos/página con bs4 [V]. Parser propio. P2 |
| DEXTools | `hecho` | Ficha `dextools_api.md`: web = SPA `<app-root>` (scraping no viable) [V]; API Free con key. P3 |
| Scrapling | `pendiente` | BSD-3, muy activo [V]. Solo si hace falta un fetcher genérico; hoy bs4 alcanza |

## 05_analisis_sentiment (P2)

| Servicio | Estado | Notas |
|----------|--------|-------|
| VADER/NLTK | `hecho` | Ficha `vader_lexico_cripto.md`: 0 dependencias; cubre 3/19 términos cripto [V] → léxico propio. P2 |
| CryptoBERT | `hecho` | Ficha `cryptobert.md`: MIT, clasificador de 3 clases, torch CPU. P3, solo si VADER falla |
| FinBERT | `descartado` | Entrenado con prensa financiera, no con jerga cripto; CryptoBERT lo reemplaza |
| TextBlob | `descartado` | Su léxico viene de reseñas de productos; VADER (social) es mejor base y no tiene dependencias |
| Custom embeddings | `descartado` | Requiere GPU/entrenamiento; fuera de "100% gratis" en Actions |

## 06_utilidades (P2)

| Servicio | Estado | Notas |
|----------|--------|-------|
| Redis | `hecho` | Cache, rate limit, colas |
| SQLite | `hecho` | Persistencia local |
| deduplicación custom | `hecho` | En script_97, lib_repetition |
| Rate limiter token bucket | `pendiente` | Ficha `pyrate_limiter.md`: empezar con `lib_rate_limit.py` propio (sin dependencias) |
| requests-cache | `hecho` | Ficha `requests_cache.md`: caché SQLite + `stale_if_error`. Solo metadata y seguridad, nunca velas. P2 |
| Healthchecks.io | `hecho` | Ficha `healthchecks_io.md`: vigilante externo de crons (quién vigila al reparador). P1, requiere cuenta + secrets |
| Proxies públicos | `descartado` | Inestables, lentos y con riesgo de inyección (MITM) en datos de precio. Alternativa: respetar los límites con rate limiter + caché |