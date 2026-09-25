---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Pipeline Activo — Cuál es el Canónico Hoy

Este archivo declara **cuál es el pipeline vigente** del proyecto y **cuáles son históricos**. Sirve para que cualquier agente sepa qué scripts correr y cuáles ignorar.

## 1. Problema que resuelve

En el directorio `04_Config\scripts\` conviven ~100 scripts. Muchos son variantes (`script_XXb`, `script_XXc`), algunos son exploratorios, otros están deprecados. Sin una declaración explícita de canonicidad, cada agente improvisa y el proyecto fragmenta.

Este archivo declara: **para cada función del pipeline, cuál es el script canónico.**

## 2. Pipeline activo (2026-09-24)

### 2.1 Capa 1 — Pre-launch (cada 6h)

| Función | Script canónico | Alternativas | Estado |
|---|---|---|---|
| TGEs Solana | `script_52_metaplex_api.py` | — | PARCIAL |
| Trending + airdrops | `script_53_threews_api.py` | `script_64_threews_crypto.py` | PARCIAL |
| Airdrops agregados | `script_56_airdrop_api.py` | `script_60_airdrops_json.py`, `script_62_airdrops_json.py` | PARCIAL |
| Token unlocks | `script_61_token_unlocks.py` | `script_63_token_unlocks.py` | PARCIAL |
| Pipeline maestro | `script_99_prelaunch.py` | — | sin datos |

**Nota:** Capa 1 no produce TGEs aún (0 detectados). Requiere activar fuentes.

### 2.2 Capa 2 — Detección T+0 (continuo)

| Función | Script canónico | Alternativas | Estado |
|---|---|---|---|
| Captura WS | `script_55_pumpportal_ws.py` | — | OK |
| Filtro primario | `script_57_pumpportal_filter.py` | — | OK |
| Quality Gate v2 | `script_59_pumpportal_filter_v2.py` | — | OK |

### 2.3 Capa 3 — Enriquecimiento + Scoring (cada 20 min)

| Función | Script canónico | Alternativas | Estado |
|---|---|---|---|
| KOL tracking | `script_71_madeonsol_kol.py` | `script_71b_madeonsol_kol_feed.py` | OK |
| Enriquecimiento | `script_58_enrich_candidates.py` | — | OK |
| Scoring v7 | `script_90_validate_v7.py` | — | OK |
| Shadow mode | `script_96_shadow_v5.py` | `script_95_shadow_v4.py` | ACTIVO |
| Pipeline maestro | `script_82_final_detection.py` | `script_81_pipeline_final.py` | OK |

**Nota:** shadow_v4 y shadow_v5 corren simultáneamente. **Decisión pendiente:** consolidar en uno solo (ver sección 5).

### 2.4 Capa 4 — Alert + Trust

| Función | Script canónico | Alternativas | Estado |
|---|---|---|---|
| Emisión de alertas | `script_97_emit_alerts.py` | — | OK |
| Telegram cliente | `script_20_telegram_alert.py` | `script_20b_telegram_fixed.py` | OK |
| Panorama Telegram | `script_40_telegram_panorama.py` | `script_40b_panorama_completo.py` | OK |
| Trust scheduler | `script_98_trust_scheduler.py` | `script_98b_trust_persistent.py` (¿existe?) | BUG |

**Nota:** el trust scheduler tiene bug de baseline. Ver `07_TRUST_UPDATE.md` y `12_TROUBLESHOOTING.md`.

### 2.5 Capa 5 — Feedback loop

| Función | Script canónico | Alternativas | Estado |
|---|---|---|---|
| Precisión | — | — | NO IMPLEMENTADO |
| Feedback loop | `script_104_feedback_loop.py` | — | PENDIENTE (no existe) |
| Watchlist | `script_101_watchlist.py` | — | PENDIENTE (no existe) |

## 3. Shadow modes — decisión pendiente

Existen varios shadow modes. Estado actual:

| Script | Estado | `_accumulated.json` | Mints rastreados |
|---|---|---|---|
| `script_91_shadow_mode.py` | ARCHIVADO | MISSING | — |
| `script_92_shadow_v2.py` | DEPRECADO | 2 B (vacío) | 0 |
| `script_93_shadow_v3.py` | MISSING | MISSING | — |
| `script_94_shadow_v3.py` | DEPRECADO | MISSING | — |
| `script_95_shadow_v4.py` | ACTIVO | 41 KB | 5 |
| `script_96_shadow_v5.py` | ACTIVO | 15 KB | 4 |

**Recomendación de YANG:** consolidar en **shadow_v5** (más reciente, estructura más limpia, 4 mints activos). Deprecar v4. Archivar v2, v3.

**Decisión pendiente de Dirección.**

## 4. Scripts deprecados o a archivar

Scripts que no pertenecen al pipeline activo y deberían moverse a `_archived/`:

- `script_01b_diagnostic_tops.py` — diagnóstico, ya cumplió.
- `script_01d_diagnostic_chainbase.py` — diagnóstico, ya cumplió.
- `script_09b_whale_alternatives.py` — exploración, descartado.
- `script_09c_verify_mcp.py` — verificación puntual.
- `script_09d_coinlobster.py` a `script_09g_coinlobster_auth.py` — CoinLobster no integrado.
- `script_10_santiment.py` — sin uso actual.
- `script_15_coinfuty.py`, `script_15b_coinfuty_corregido.py` — sin uso.
- `script_16_narrativescope.py` — sin uso.
- `script_19b_quantoracle.py`, `script_19d_quantoracle_corregido.py` — sin uso.
- `script_21_hoja_salida*.py` (4 variantes) — reemplazado por pipeline actual.
- `script_23_pipeline_maestro.py` — predecesor.
- `script_36_deep_dive_deficlaw.py`, `script_36b_deep_dive_verified.py` — puntual.
- `script_37_alert_catwifout.py` a `script_37d_alert_multipart.py` — pruebas de formato.
- `script_38b_tracking_degradacion.py` — exploratorio.
- `script_39b_panorama_multi.py`, `script_39c_extractor_robusto.py` — predecesores.
- `script_42_analisis_caso.py`, `script_43_historical_cases.py` — puntuales.
- `script_45_volume_anomaly.py`, `script_45b_volume_anomaly_v2.py` — sin uso actual.
- `script_46_early_detection.py` a `script_46c_adaptive_filter.py` — predecesores de detection v3-v6.
- `script_67_cryptoguard.py` — sin uso.
- `script_68_react_framework.py`, `script_69_questions_generator.py` — exploratorios.
- `script_73_orderly_whales.py`, `script_74_funding_anomaly.py` — no integrados.
- `script_75_crypto_signals.py`, `script_75b_crypto_signals_daemon.py` — exploratorios.
- `script_77_cryptowhale_insights.py` — sin uso.
- `script_78_pipeline_maestro_v2.py`, `script_80_pipeline_maestro_v3.py` — predecesores.
- `script_83_dual_scoring.py` — predecesor.
- `script_84_detection_v3.py` a `script_87_detection_v6.py` — predecesores de v7.

**Acción:** mover a `04_Config\scripts\_archived\` en Ciclo 17.10.

## 5. Plan de consolidación (Ciclo 17.10)

| Paso | Acción | Resultado |
|---|---|---|
| 1 | Confirmar shadow mode canónico (v5 recomendado) | 1 shadow activo |
| 2 | Mover scripts deprecados a `_archived/` | Menos ruido |
| 3 | Renombrar canónicos sin sufijos b/c/d | Nombres limpios |
| 4 | Actualizar `04_SCRIPTS_CATALOG.md` | Catálogo fiel |
| 5 | Actualizar este archivo (`08_PIPELINE_ACTIVO.md`) | Declaración vigente |

## 6. Cómo saber si un script es canónico

Reglas de decisión:

1. **Si está listado en la sección 2** de este archivo → es canónico.
2. **Si no está en la sección 2 pero existe** → consultar `04_SCRIPTS_CATALOG.md`.
3. **Si aparece en la sección 4** → deprecado, no ejecutar.
4. **Si no aparece en ningún archivo** → reportar a YANG para clasificación.

## 7. Próximas decisiones

| # | Decisión | Responsable | Plazo |
|---|---|---|---|
| 1 | Shadow mode canónico: ¿v5 o v4? | Dirección | inmediato |
| 2 | ¿Archivar deprecados ahora o tras migración a serverless? | Dirección | 17.10 |
| 3 | ¿Renombrar canónicos sin sufijos? | YANG + YIN | 17.10 |

## VER TAMBIÉN

- [03_FLUJOS.md](03_FLUJOS.md) — workflows que usan estos scripts
- [04_SCRIPTS_CATALOG.md](04_SCRIPTS_CATALOG.md) — catálogo completo de scripts
- [05_FUENTES.md](05_FUENTES.md) — fuentes que consume cada capa
- [07_TRUST_UPDATE.md](07_TRUST_UPDATE.md) — detalle del trust scheduler
- [12_TROUBLESHOOTING.md](12_TROUBLESHOOTING.md) — bugs conocidos

## Changelog

- 2026-09-24 — v1.0 — Creación inicial con declaración de canónicos (YANG, Ciclo 17.6.B)