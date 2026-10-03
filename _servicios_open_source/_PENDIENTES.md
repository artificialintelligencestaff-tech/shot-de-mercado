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
| Helius (Solana) | `pendiente` | Key requerida, free tier |
| Birdeye | `pendiente` | Key requerida, 401 actual |
| DexScreener | `hecho` | Sin key, rate limit OK |
| GeckoTerminal | `hecho` | Sin key, velas 1m/15m |
| Solscan | `pendiente` | Key Pro requerida |
| MadeOnSol | `pendiente` | Key en secret, endpoints no verificados |
| RugCheck | `hecho` | Sin key, holders/insiders |

## 04_scrapers (P1)

| Servicio | Estado | Notas |
|----------|--------|-------|
| Crawlee/Apify | `pendiente` | Evaluar free tier |
| Playwright | `pendiente` | Headless browser, recurso intensivo |
| Selenium | `pendiente` | Legacy, más lento |
| Firecrawl | `pendiente` | API key requerida, 403 en search |

## 05_analisis_sentiment (P2)

| Servicio | Estado | Notas |
|----------|--------|-------|
| VADER/NLTK | `pendiente` | Python, rule-based |
| FinBERT | `pendiente` | HuggingFace, financiero |
| TextBlob | `pendiente` | Simple, rápido |
| Custom embeddings | `pendiente` | Requiere GPU/entrenamiento |

## 06_utilidades (P2)

| Servicio | Estado | Notas |
|----------|--------|-------|
| Redis | `hecho` | Cache, rate limit, colas |
| SQLite | `hecho` | Persistencia local |
| deduplicación custom | `hecho` | En script_97, lib_repetition |
| Rate limiter token bucket | `pendiente` | Implementar genérico |