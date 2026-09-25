---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Flujos — Workflows del Sistema

Este archivo describe cada workflow del sistema: qué lo dispara, qué hace, qué produce, y cómo se verifica. Sirve para que cualquier agente entienda **qué corre cuándo** sin tener que leer los ~100 scripts.

## Workflow 1 — Pipeline T+0

**Disparador:** cron `*/20 * * * *` (cada 20 min).
**Objetivo:** capturar tokens en el instante de creación y filtrarlos por calidad.

**Pasos:**
```
1. script_55_pumpportal_ws.py         → conecta WS, captura tokens
2. script_57_pumpportal_filter.py     → filtro primario
3. script_59_pumpportal_filter_v2.py  → Quality Gate (solAmount >=5 OR MCap >=50)
4. script_58_enrich_candidates.py     → enriquece con MadeOnSol, Dexscreener
5. script_90_validate_v7.py           → scoring v7
6. script_97_emit_alerts.py           → si score >= umbral, emite alerta Telegram
7. Escribe _all_alerts.json           → persiste alertas nuevas
8. Escribe _accumulated.json          → estado acumulado del ciclo
```

**Inputs:** PumpPortal WS, MadeOnSol API, Dexscreener API, Helius RPC.
**Outputs:** alertas Telegram + `_all_alerts.json` actualizado + `_accumulated.json`.
**Duración esperada:** ~3-5 min por ciclo.
**Exit codes:** 0 exito, 1 sin candidatos, 2 API failure, 3 write failure.

## Workflow 2 — Trust Update

**Disparador:** cron `*/20 * * * *` (cada 20 min).
**Objetivo:** actualizar confianza de alertas activas en t+1h, t+6h, t+24h.

**Pasos:**
```
1. script_98_trust_scheduler.py       → lee _all_alerts.json
2. Para cada alerta con status=active_tracking:
   a. Consulta precio actual (Dexscreener)
   b. Calcula price_change_pct vs. baseline
   c. Aplica reglas de veredicto (ACIERTO/FALLO/FALSO POSITIVO/NEUTRAL)
   d. Actualiza confianza segun delta
   e. Escribe trust_<mint>.json
3. Si cambio significativo (>=10 pts) -> notifica via Telegram
4. Si stage == t+24h -> fija veredicto final
5. Actualiza _all_alerts.json y _scheduler_log.json
```

**Inputs:** `_all_alerts.json`, Dexscreener API.
**Outputs:** `trust_<mint>.json`, `_scheduler_log.json`, `_all_alerts.json` actualizado, notificaciones Telegram.
**Bug conocido:** `prev_price = current_price` en primera pasada. Ver `12_TROUBLESHOOTING.md`.
**Exit codes:** 0 exito, 1 sin alertas pendientes, 2 API failure, 3 write failure.

## Workflow 3 — Pre-launch

**Disparador:** cron `0 */6 * * *` (cada 6h).
**Objetivo:** detectar TGEs, airdrops y activos pre-listing.

**Pasos:**
```
1. script_99_prelaunch.py             → pipeline pre-launch
2. Consulta fuentes:
   - script_52_metaplex_api.py
   - script_53_threews_api.py
   - script_54_clawnch_api.py
   - script_56_airdrop_api.py
3. Consolida candidatos pre-listing
4. Escribe _prelaunch_accumulated.json
5. Si hay candidato con potencial -> notifica via Telegram
```

**Inputs:** Metaplex, three.ws, Clawnch, airdrops.io.
**Outputs:** `_prelaunch_accumulated.json`, notificaciones.
**Estado actual:** ejecutado, 0 TGEs detectados (faltan fuentes activas).
**Exit codes:** 0 exito, 1 sin TGEs, 2 API failure, 3 write failure.

## Workflow 4 — Watchlist (futuro, Fase 2)

**Disparador:** cron `*/5 * * * *` (cada 5 min).
**Objetivo:** seguimiento continuo de tokens en WATCH REAL (score 50-69) que no llegaron a ALERTA.

**Pasos:** (a disenar en Ciclo 18.A)
```
1. script_101_watchlist.py            -> lee _all_alerts.json
2. Para cada token WATCH:
   a. Consulta precio y volumen actuales
   b. Detecta cambios subitos
   c. Si sube a umbral ALERTA -> promueve y notifica
3. Escribe _watchlist_state.json
```

## Workflow 5 — Backup (futuro, Fase 2)

**Disparador:** cron `0 0 * * *` (diario medianoche).
**Objetivo:** snapshot diario del estado canonico.

**Pasos:** (a disenar en Ciclo 18.B)
```
1. Copia _all_alerts.json, _precision_log.json, _cycle_log.json,
   _state_manifest.json, _project_manifest.json
2. Empaqueta en _backups/YYYY-MM-DD.zip
3. Aplica retencion: 7 diarios, 4 semanales, 12 mensuales
4. Si excede retencion, elimina los mas antiguos
```

## Workflow 6 — Feedback Loop (futuro, Fase 2)

**Disparador:** manual o al cerrar cada alerta (veredicto final t+24h).
**Objetivo:** calcular precision acumulada y ajustar pesos del scoring.

**Pasos:** (a disenar en Ciclo 18.C)
```
1. script_104_feedback_loop.py        -> lee _all_alerts.json
2. Cuenta alertas con veredicto_final != PENDIENTE
3. Calcula precision = aciertos / total
4. Si n >= 10 y precision < 50% -> propone ajuste de pesos
5. Escribe _precision_log.json
```

## Mapa visual de workflows

```
CRON */20 * * * *
    |- pipeline_t0     -> captura + scoring + alertas
    |- trust_update    -> actualiza confianza

CRON 0 */6 * * * *
    |- prelaunch       -> TGEs y airdrops

CRON */5 * * * *
    |- watchlist       -> seguimiento continuo (Fase 2)

CRON 0 0 * * *
    |- backup          -> snapshot diario (Fase 2)

MANUAL / EVENTO
    |- feedback_loop   -> precision + ajuste (Fase 2)
```

## VER TAMBIEN

- [02_ARQUITECTURA.md](02_ARQUITECTURA.md) — arquitectura general
- [04_SCRIPTS_CATALOG.md](04_SCRIPTS_CATALOG.md) — scripts por workflow
- [07_TRUST_UPDATE.md](07_TRUST_UPDATE.md) — reglas de trust update
- [08_PIPELINE_ACTIVO.md](08_PIPELINE_ACTIVO.md) — cual es el canonico hoy

## Changelog

- 2026-09-24 — v1.0 — Creacion inicial (YANG, Ciclo 17.4)

"Escribí este contenido en D:\Proyecto Shot de mercado\El cerebro de dios\03_FLUJOS.md. Reportá tamaño y SHA-256."