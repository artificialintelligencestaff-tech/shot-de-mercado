# CoinDesk RSS Aggregator (community)

**Repo:** https://github.com/coindesk/rss-aggregator
**Licencia:** Apache-2.0
**Gratis:** sí (RSS público, sin key)
**Requisitos:** Python, feedparser
**Qué hace:** Scraper de feeds RSS de CoinDesk, The Block, Decrypt, Bitcoin Magazine, CryptoSlate, BeInCrypto. Normaliza a JSON, deduplica por URL/title, categorías (markets, tech, regulation, defi, nfts).
**Por qué sirve al proyecto:** 8 fuentes RSS verificadas (ver D-017: Coindesk 308 redirect, Decrypt 200, BitcoinMagazine 200, CryptoSlate 200, BeInCrypto 200). Sin keys, solo HTTP GET + parse. Compatible con script_115 news_rss.
**Recomendación:** integrar como fallback RSS robusto; evaluar rate limits