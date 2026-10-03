# Servicios Open Source — Índice

Estructura de investigación de servicios open source gratuitos para el pipeline Shot de Mercado.

## Categorías

| Cat | Carpeta | Foco | Prioridad |
|-----|---------|------|-----------|
| 01 | `01_news_mcp/` | Agregadores de noticias crypto (RSS, API, MCP) | P0 |
| 02 | `02_social_x/` | Scrapers X/Twitter, Reddit, Telegram, Discord | P0 |
| 03 | `03_data_blockchain/` | Indexers, RPC, explorers, on-chain analytics | P1 |
| 04 | `04_scrapers/` | Scrapers web genéricos, Selenium, Playwright | P1 |
| 05 | `05_analisis_sentiment/` | NLP, sentiment, topic modeling, embeddings | P2 |
| 06 | `06_utilidades/` | Herramientas auxiliares (caché, rate limit, dedup) | P2 |

## Fichas

| Cat | Ficha | Key | Prioridad |
|-----|-------|-----|-----------|
| 01 | `cryptopanic.md`, `coindesk_rss_aggregator.md`, `cryptocontrol.md` | — | — |
| 03 | `goplus_security.md` | no | P1 |
| 03 | `dexpaprika.md` | no | P1 |
| 03 | `helius_free.md` | gratuita | P2 |
| 04 | `pumpfun_datos.md` | no | P1 |
| 04 | `bitcointalk_ann.md` | no | P2 |
| 04 | `dextools_api.md` | gratuita | P3 |
| 05 | `vader_lexico_cripto.md` | no | P2 |
| 05 | `cryptobert.md` | no | P3 |
| 06 | `healthchecks_io.md` | cuenta gratuita | P1 |
| 06 | `requests_cache.md` | no | P2 |
| 06 | `pyrate_limiter.md` | no | P2 |

Fichas de D-055: endpoints probados en vivo el 2026-10-03 (rótulo [V]). Estado y descartes en `_PENDIENTES.md`.

## Protocolo

1. **YIN investiga** → crea `.md` en la carpeta correspondiente
2. **Claude integra** → cuando Yang lo indica, mueve a `_INSTALADOS.md`
3. **Criterios de inclusión**: gratis, sin key obligatoria, licencia permisiva (MIT/Apache/BSD), activo (<6 meses sin commits), documentado
4. **Formato .md**: nombre, repo, licencia, gratis, requisitos, qué hace, por qué sirve, recomendación