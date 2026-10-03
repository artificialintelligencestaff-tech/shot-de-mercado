# Bitcointalk — tablero de anuncios de altcoins (ANN)

**Repo de referencia:** https://github.com/financiallyruined/BitcoinTalk-ANN-Thread-Notifier. Sin licencia y sin commits desde 2024-10 [V]: sirve como referencia y **no se copia**. https://github.com/gogogoutham/bitcointalk-scraper (crawler de mensajes, antiguo). Lo práctico es un parser propio de ~80 líneas.
**Licencia:** parser propio (repo del proyecto). bs4 MIT [V], ya fijado con hashes en `04_Config/requirements/sources_telegram.txt`.
**Gratis:** sí, HTML público sin login [V]. `GET https://bitcointalk.org/index.php?board=159.0` → 200, 115 KB (2026-10-03). `robots.txt` solo declara el sitemap [V].
**Requisitos:** `requests` + `beautifulsoup4` (los dos ya están en el proyecto).
**Qué hace:** el tablero 159 (Announcements, Altcoins) es donde los proyectos nuevos publican su hilo [ANN].
- Selector [V]: `span[id^=msg_] a` devuelve 40 hilos por página (los primeros son fijos de reglas: se filtran por id de tema o por posición).
- Paginación: `board=159.40`, `159.80`…
- Por hilo: título, `topic=<id>`, respuestas y vistas (columnas de la tabla).
**Por qué sirve al proyecto:**
- Fuente de "nacimiento declarado" para proyectos fuera de los launchpads de memecoins (grupos de infraestructura o PoW), con la ticker en el título (`[ANN] … $XYZ`). [I]
- Aceleración de respuestas o vistas por hilo = atención temprana medible, con el mismo baseline Poisson del doc 26. [H]
**Riesgos técnicos:** el foro limita a los clientes agresivos: 1 request cada ≥2 s y 1 página por corrida alcanzan (el ritmo de hilos nuevos es bajo). [I] El HTML de SMF es antiguo pero estable. [I]
**Recomendación:** P2. Implementarlo como fuente `forums` (hoy en "diseño" en `_bots.yaml`): `bot_forums` con Bitcointalk ANN, cada 60 min, salida src-1 con `kind="thread"` y cashtag extraído del título con `lib_normalize.cashtag`. No guardar el cuerpo del post.
