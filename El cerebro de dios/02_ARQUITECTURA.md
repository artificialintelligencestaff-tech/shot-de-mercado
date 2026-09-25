---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Arquitectura — Cómo Funciona el Sistema

## Las 5 capas del pipeline
┌─────────────────────────────────────────────────────────────┐
│ CAPA 1 — PRE-LAUNCH (24-48h antes del listing) │
│ Fuentes: Metaplex, Clawnch, three.ws, airdrops.io, Dropstab │
│ Cadencia: cada 6h │
│ Output: TGEs y airdrops pre-listing │
└─────────────────────────────────────────────────────────────┘
↓
┌─────────────────────────────────────────────────────────────┐
│ CAPA 2 — DETECCIÓN T+0 (tiempo real) │
│ Fuentes: PumpPortal WS (25 tokens/min) │
│ Cadencia: continua │
│ Output: tokens en el instante de creación │
└─────────────────────────────────────────────────────────────┘
↓
┌─────────────────────────────────────────────────────────────┐
│ CAPA 3 — ENRIQUECIMIENTO + SCORING │
│ Fuentes: MadeOnSol, Dexscreener, Helius RPC, three.ws │
│ Cadencia: cada ciclo (20 min) │
│ Output: score + confianza por token │
└─────────────────────────────────────────────────────────────┘
↓
┌─────────────────────────────────────────────────────────────┐
│ CAPA 4 — ALERT + TRUST UPDATE │
│ Herramientas: Telegram Bot + trust scheduler (1h/6h/24h) │
│ Cadencia: ciclos + trust updates │
│ Output: alertas + actualizaciones de confianza │
└─────────────────────────────────────────────────────────────┘
↓
┌─────────────────────────────────────────────────────────────┐
│ CAPA 5 — FEEDBACK LOOP │
│ Fuentes: historial de alertas + precios reales + veredictos │
│ Cadencia: por cada alerta cerrada │
│ Output: precisión medida + ajuste de pesos del scoring │
└─────────────────────────────────────────────────────────────┘

text

## Estado de cada capa (2026-09-24)

| Capa | Estado | Notas |
|---|---|---|
| 1 — Pre-launch | 🟡 Operativo sin datos | Script 99 corre, 0 TGEs detectados |
| 2 — Detección T+0 | ✅ Operativo | ~400+ tokens por ciclo |
| 3 — Scoring | ✅ Operativo | Scoring v7, 9 validados / 30 filtrados |
| 4 — Alert + Trust | 🟡 Alert funcional, trust con bug | Bug de baseline conocido |
| 5 — Feedback | 🔴 No implementado | Requiere cerrar trust updates primero |

## Arquitectura actual vs. arquitectura objetivo

### Actual (local)

- Scripts ejecutados manualmente por Dirección en Windows.
- Estado en archivos JSON locales.
- Bot Telegram disparado desde scripts locales.
- Dependiente de la laptop encendida.

### Objetivo (serverless)
GitHub Repository (fuente canónica)
↓ (cron triggers)
GitHub Actions Runner (Ubuntu, gratis, efímero)
├── checkout repo
├── setup Python 3.11
├── pip install -r requirements.txt
├── ejecutar script correspondiente
└── commit estado modificado
↓
Output:
├── Telegram Bot → alertas
├── Repo → estado actualizado
└── GitHub Actions logs → auditoría

text

**Cero dependencia de hardware local.**

## Frecuencias objetivo (cron GitHub Actions)

| Workflow | Cron | Frecuencia |
|---|---|---|
| `pipeline_t0.yml` | `*/20 * * * *` | Cada 20 min |
| `trust_update.yml` | `*/20 * * * *` | Cada 20 min |
| `prelaunch.yml` | `0 */6 * * *` | Cada 6h |
| `watchlist.yml` | `*/5 * * * *` | Cada 5 min |
| `backup.yml` | `0 0 * * *` | Diario a medianoche |

## Componentes internos

### Captura T+0
- `script_55_pumpportal_ws.py`: WebSocket PumpPortal.
- `script_57_pumpportal_filter.py`: filtro primario.
- `script_59_pumpportal_filter_v2.py`: filtro v2 con Quality Gate.

### Enriquecimiento
- `script_71_madeonsol_kol.py`: KOL tracking (25 calls/ciclo).
- `script_58_enrich_candidates.py`: enriquece candidatos.
- `script_84` a `script_87`: detection v3-v6.
- `script_90_validate_v7.py`: scoring v7.

### Shadow modes
- `script_91_shadow_mode.py`: modo base.
- `script_92_shadow_v2.py` a `script_96_shadow_v5.py`: modos v2-v5.
- **Nota:** shadow_v4 y shadow_v5 activos simultáneamente. Consolidar en Ciclo 17.4+.

### Alertas
- `script_97_emit_alerts.py`: emite alertas vía Telegram.
- `script_20_telegram_alert.py`: cliente Telegram base.
- `script_40_telegram_panorama.py`: panorama completo.

### Trust
- `script_98_trust_scheduler.py`: trust update 1h/6h/24h.
- **Bug:** `prev_price = current_price` en primera pasada.

### Pre-launch
- `script_99_prelaunch.py`: pipeline pre-lanzamiento.

## Estado persistente (JSON)

| Archivo | Path | Contenido |
|---|---|---|
| `_all_alerts.json` | `02_Analisis\alerts\` | Registro canónico de alertas |
| `_precision_log.json` | raíz | Precisión acumulada |
| `_cycle_log.json` | raíz | Log de ciclos |
| `_accumulated.json` | `02_Analisis\shadow_vN\` | Estado por shadow mode |
| `_project_manifest.json` | raíz | Constraints + paths |
| `_state_manifest.json` | raíz | Hashes de archivos clave |

## VER TAMBIÉN

- [00_NUCLEO.md](00_NUCLEO.md) — propósito raíz
- [03_FLUJOS.md](03_FLUJOS.md) — workflows detallados
- [04_SCRIPTS_CATALOG.md](04_SCRIPTS_CATALOG.md) — catálogo de scripts
- [08_PIPELINE_ACTIVO.md](08_PIPELINE_ACTIVO.md) — cuál es el canónico hoy

## Changelog

- 2026-09-24 — v1.0 — Creación inicial (YANG, Ciclo 17.3)
