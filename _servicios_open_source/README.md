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

## Protocolo

1. **YIN investiga** → crea `.md` en la carpeta correspondiente
2. **Claude integra** → cuando Yang lo indica, mueve a `_INSTALADOS.md`
3. **Criterios de inclusión**: gratis, sin key obligatoria, licencia permisiva (MIT/Apache/BSD), activo (<6 meses sin commits), documentado
4. **Formato .md**: nombre, repo, licencia, gratis, requisitos, qué hace, por qué sirve, recomendación