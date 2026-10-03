# PyrateLimiter — rate limiter (familia leaky bucket)

**Repo:** https://github.com/vutran1710/PyrateLimiter
**Licencia:** MIT [V] (GitHub, push 2026-09-23)
**Gratis:** sí, local.
**Requisitos:** `pyrate-limiter` 4.5.0 (PyPI, 2026-08-30). Sin dependencias obligatorias: `redis`, `postgres` y `filelock` son extras opcionales [V].
**Qué hace:** limita llamadas por ventana (p. ej. 30/min y 2/s a la vez) con varios buckets. Backends en memoria, SQLite, Redis o Postgres. Funciona como decorador o con `try_acquire()` bloqueante.
**Por qué sirve al proyecto:**
- Cada API nueva trae su propio límite: GoPlus 30/min [V], KyberSwap 3 rps [I], DEXTools Free 40/min [I], Helius DAS 2 rps [I]. Hoy cada bot implementa sus propias pausas (`pause_s` en `telegram.yaml`, sleeps en `bot_rss_news`) [V].
- Un limitador común, configurado desde YAML por fuente, evita bans y unifica la política. Los 429 se reflejarían en `_health.json` en vez de repararse a ciegas. [I]
- El backend SQLite permite que los procesos de un mismo job compartan el presupuesto. [I]
**Alternativa sin dependencia:** un token bucket propio de unas 40 líneas en `lib_rate_limit.py` (figura como pendiente en `_PENDIENTES.md`). Para bots de un solo proceso con 1–3 límites, alcanza. [I]
**Recomendación:** P2. Empezar con el `lib_rate_limit.py` propio, sin dependencia: cumple "lo que no sirve se elimina" y evita supply chain. Pasar a PyrateLimiter solo si hacen falta límites compuestos entre procesos (instalación pineada con hashes).
