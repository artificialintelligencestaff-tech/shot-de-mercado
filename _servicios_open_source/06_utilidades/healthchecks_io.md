# Healthchecks.io — vigilancia externa de crons (dead man's switch)

**Repo:** https://github.com/healthchecks/healthchecks
**Licencia:** BSD-3-Clause [V] (GitHub, push 2026-10-02). Se puede autohospedar con Django.
**Gratis:** sí. Plan hospedado Hobbyist: 20 checks y 100 entradas de log por check [I] (healthchecks.io y comparativas, 2026-10-03). Integraciones de alerta gratuitas: email, Telegram, Discord, Slack y otras [I].
**Requisitos:** cuenta gratuita y una URL de ping por check (la URL es un secreto → secret `HC_PING_<WF>`, creado por Dirección). Desde el workflow: `curl -fsS -m 10 --retry 3 "$HC_PING_URL"` al final del job, más `/fail` si falla.
**Qué hace:** cada check espera un ping cada N minutos. Si no llega en el periodo más el margen, alerta. Detecta crons que dejaron de correr, que es el fallo silencioso que nadie reporta.
**Por qué sirve al proyecto:**
- `bot_self_repair` corre en GitHub Actions, igual que todo lo que vigila [V]. Si Actions deja de disparar crons (repo inactivo 60 días, incidente de GitHub, cuota), el reparador también se detiene y nadie avisa: **quién vigila al vigilante**. [I]
- Un vigilante externo y gratuito cierra ese hueco con 1 línea por workflow. [I]
- 20 checks alcanzan para los workflows críticos: pipeline_t0, early_watch a/b, sources_orchestrator, sources_self_repair, sources_rss, telegram a/b. [V conteo]
- Alerta directa al chat de OPS (`TELEGRAM_OPS_CHAT_ID`) desde la integración de Telegram de Healthchecks, sin tocar el bot emisor. [I]
**Riesgos técnicos:** el ping agrega 1 request saliente por corrida. Si healthchecks.io cae, no bloquea nada (`|| true`). [I]
**Recomendación:** P1, por su mayor relación impacto/costo de esta tanda. Requiere que Dirección cree la cuenta y los secrets (yo no toco credenciales). Hay que modificar workflows en producción, así que se consulta antes. Propuesta: empezar por `sources_self_repair.yml` y `early_watch.yml`.
