---
owner: YANG
status: PARCIAL
last_updated: 2026-09-24
version: 0.9
---

# Catálogo de Scripts

Existen ~100 scripts en `04_Config\scripts\`. Este catálogo los clasifica por función. Los scripts sin documentación explícita se marcan como `[PENDIENTE]`.

**Nota:** catálogo en construcción. Se completa a medida que YIN audita cada script.

## Convención de nombres

- `script_NN_nombre.py` → script principal.
- `script_NNb_nombre.py` o `script_NNc_nombre.py` → variante o corrección.
- **Problema identificado:** proliferación de variantes sin consolidar. Ver Ciclo 17.5 para plan de consolidación.

## Bloque 1 — Exploración temprana (01-50)

Scripts fundacionales. Exploración de fuentes, pruebas de APIs, descarte de enfoques.

| Script | Función | Estado |
|---|---|---|
| script_01_tops_mcp.py | Chainbase Tops MCP — narrativas | ✅ |
| script_01b_diagnostic_tops.py | Diagnóstico Tops MCP | ✅ |
| script_01c_onvexia_mcp.py | Onvexia MCP | 🟡 |
| script_01d_diagnostic_chainbase.py | Diagnóstico Chainbase | ✅ |
| script_01f_onvexia_extractor.py | Extractor Onvexia | 🟡 |
| script_01g_alpha_mcp.py | Alpha MCP | ✅ |
| script_02_signalstack.py | SignalStack | ✅ |
| script_03_coingecko.py | CoinGecko precios | ✅ |
| script_04_alpha_mcp.py | Alpha MCP v2 | ✅ |
| script_05_deep_dive_movers.py | Movers del mercado | ✅ |
| script_06_historical_audit.py | Auditoría histórica | ✅ |
| script_09_deepblue_whales.py | DeepBlue ballenas | 🟡 |
| script_09b_whale_alternatives.py | Alternativas ballenas | 🟡 |
| script_09c_verify_mcp.py | Verificación MCP | ✅ |
| script_09d_coinlobster.py | CoinLobster | 🟡 |
| script_09e_deepblue.py | DeepBlue v2 | 🟡 |
| script_09f_coinlobster_porciones.py | CoinLobster porciones | 🟡 |
| script_09g_coinlobster_auth.py | CoinLobster auth | 🟡 |
| script_10_santiment.py | Santiment | 🟡 |
| script_11_apewisdom.py | ApeWisdom | ✅ |
| script_15_coinfuty.py | Coinfuty | 🟡 |
| script_15b_coinfuty_corregido.py | Coinfuty v2 | 🟡 |
| script_16_narrativescope.py | NarrativeScope | 🟡 |
| script_18_ai_agents_tokens.py | Tokens de agentes IA | ✅ |
| script_19b_quantoracle.py | QuantOracle | 🟡 |
| script_19d_quantoracle_corregido.py | QuantOracle v2 | 🟡 |
| script_20_telegram_alert.py | Telegram alert | ✅ |
| script_20b_telegram_fixed.py | Telegram fix | ✅ |
| script_21_hoja_salida.py | Hoja de salida | 🟡 |
| script_21b_hoja_salida_real.py | Hoja real | 🟡 |
| script_21c_hoja_salida_final.py | Hoja final | 🟡 |
| script_21d_hoja_auditada.py | Hoja auditada | 🟡 |
| script_23_pipeline_maestro.py | Pipeline maestro v1 | 🟡 |
| script_31_limpieza.py | Limpieza de datos | ✅ |
| script_32_verificar_paquetes.py | Verificación paquetes | ✅ |
| script_33_verificar_registries.py | Verificación registries | ✅ |
| script_34_mcp_stdio_client.py | Cliente MCP stdio | ✅ |
| script_34b_mcp_stdio_client.py | Cliente MCP v2 | ✅ |
| script_35_mcp_analytics.py | MCP analytics | ✅ |
| script_35b_mcp_analytics.py | MCP analytics v2 | ✅ |
| script_36_deep_dive_deficlaw.py | Deep dive DeFiClaw | 🟡 |
| script_36b_deep_dive_verified.py | Deep dive verificado | 🟡 |
| script_37_alert_catwifout.py | Alerta CATWIFOUT | ✅ |
| script_37b_alert_completa.py | Alerta completa | ✅ |
| script_37c_alert_profesional.py | Alerta profesional | ✅ |
| script_37d_alert_multipart.py | Alerta multipart | ✅ |
| script_38_price_tracker.py | Tracker de precio | ✅ |
| script_38b_tracking_degradacion.py | Tracking degradación | ✅ |
| script_39b_panorama_multi.py | Panorama multi | ✅ |
| script_39c_extractor_robusto.py | Extractor robusto | ✅ |
| script_40_telegram_panorama.py | Telegram panorama | ✅ |
| script_40b_panorama_completo.py | Panorama completo | ✅ |
| script_41_conflict_resolver.py | Resolver conflictos | ✅ |
| script_42_analisis_caso.py | Análisis de caso | ✅ |
| script_43_historical_cases.py | Casos históricos | ✅ |
| script_44_holder_analysis.py | Análisis holders | ✅ |
| script_44b_holder_rpc.py | Holders vía RPC | ✅ |
| script_45_volume_anomaly.py | Anomalía volumen | ✅ |
| script_45b_volume_anomaly_v2.py | Anomalía v2 | ✅ |
| script_46_early_detection.py | Detección temprana | ✅ |
| script_46b_early_filtered.py | Detección filtrada | ✅ |
| script_46c_adaptive_filter.py | Filtro adaptativo | ✅ |

## Bloque 2 — Pipeline activo (51-99)

Scripts del pipeline productivo.

### Pre-launch (51-56, 60-66)

| Script | Función | Estado |
|---|---|---|
| script_51_api_direct_launches.py | Launches directos | 🟡 |
| script_52_metaplex_api.py | Metaplex Genesis | 🟡 |
| script_53_threews_api.py | three.ws | 🟡 |
| script_54_clawnch_api.py | Clawnch | 🟡 |
| script_55_pumpportal_ws.py | PumpPortal WS | ✅ |
| script_56_airdrop_api.py | Airdrops API | 🟡 |
| script_60_airdrops_json.py | Airdrops JSON | 🟡 |
| script_61_token_unlocks.py | Token unlocks | 🟡 |
| script_62_airdrops_json.py | Airdrops JSON v2 | 🟡 |
| script_63_token_unlocks.py | Token unlocks v2 | 🟡 |
| script_64_threews_crypto.py | three.ws crypto | 🟡 |
| script_65_airdrop_tracker.py | Tracker de airdrops | 🟡 |
| script_66_crypto_early_radar.py | Early radar | ✅ |

### Enriquecimiento + scoring (57-59, 71, 84-90)

| Script | Función | Estado |
|---|---|---|
| script_57_pumpportal_filter.py | Filtro PumpPortal | ✅ |
| script_58_enrich_candidates.py | Enriquece candidatos | ✅ |
| script_59_pumpportal_filter_v2.py | Quality Gate v2 | ✅ |
| script_67_cryptoguard.py | CryptoGuard | ✅ |
| script_68_react_framework.py | React framework | 🟡 |
| script_69_questions_generator.py | Generador preguntas | 🟡 |
| script_70_news_aggregator.py | News aggregator | ✅ |
| script_71_madeonsol_kol.py | MadeOnSol KOL | ✅ |
| script_71b_madeonsol_kol_feed.py | KOL feed | ✅ |
| script_72_news_cv_corregido.py | News CV corregido | ✅ |
| script_73_orderly_whales.py | Orderly whales | 🟡 |
| script_74_funding_anomaly.py | Funding anomaly | 🟡 |
| script_75_crypto_signals.py | Crypto signals | 🟡 |
| script_75b_crypto_signals_daemon.py | Signals daemon | 🟡 |
| script_76_token_intel.py | Token intel | ✅ |
| script_77_cryptowhale_insights.py | CryptoWhale insights | 🟡 |
| script_84_detection_v3.py | Detection v3 | 🟡 |
| script_85_detection_v4.py | Detection v4 | 🟡 |
| script_86_detection_v5.py | Detection v5 | 🟡 |
| script_87_detection_v6.py | Detection v6 | 🟡 |
| script_90_validate_v7.py | Scoring v7 | ✅ |

### Pipelines maestros (78-83)

| Script | Función | Estado |
|---|---|---|
| script_78_pipeline_maestro_v2.py | Pipeline maestro v2 | 🟡 |
| script_79_inspect_threews.py | Inspección three.ws | ✅ |
| script_80_pipeline_maestro_v3.py | Pipeline maestro v3 | 🟡 |
| script_81_pipeline_final.py | Pipeline final v1 | 🟡 |
| script_82_final_detection.py | Final detection | ✅ |
| script_83_dual_scoring.py | Dual scoring | ✅ |

### Shadow modes (91-96)

| Script | Función | Estado |
|---|---|---|
| script_91_shadow_mode.py | Shadow base | 🟡 |
| script_92_shadow_v2.py | Shadow v2 | ❌ vacío |
| script_93_shadow_v3.py | Shadow v3 | ❌ MISSING |
| script_94_shadow_v3.py | Shadow v3 dup | 🟡 |
| script_95_shadow_v4.py | Shadow v4 | ✅ **activo** |
| script_96_shadow_v5.py | Shadow v5 | ✅ **activo** |

**Nota:** shadow_v4 y shadow_v5 activos simultáneamente. Consolidar en 17.5.

### Alertas + trust (97-99)

| Script | Función | Estado |
|---|---|---|
| script_97_emit_alerts.py | Emite alertas Telegram | ✅ |
| script_98_trust_scheduler.py | Trust update 1h/6h/24h | 🟡 **bug de baseline** |
| script_99_prelaunch.py | Pipeline pre-launch | 🟡 sin datos |

## Problemas identificados

1. **Proliferación de variantes:** `script_XXb`, `script_XXc`, `script_XXd` sin consolidar. Consolidar en 17.5.
2. **Shadow modes duplicados:** v4 y v5 activos. Elegir canónico.
3. **Bloque 1 (01-50):** la mitad son exploratorios. Se pueden archivar los fallidos.
4. **Falta catálogo completo:** este archivo es PARCIAL. Los scripts marcados `[PENDIENTE]` necesitan auditoría individual.

## Plan de consolidación (Ciclo 17.5)

1. Auditar shadow_v4 vs shadow_v5 → elegir canónico.
2. Archivar scripts exploratorios fallidos en `_archived/`.
3. Renombrar y documentar scripts activos.
4. Actualizar este catálogo a estado COMPLETO.

## VER TAMBIÉN

- [03_FLUJOS.md](03_FLUJOS.md) — workflows que usan estos scripts
- [08_PIPELINE_ACTIVO.md](08_PIPELINE_ACTIVO.md) — cuál es el canónico hoy
- [12_TROUBLESHOOTING.md](12_TROUBLESHOOTING.md) — errores conocidos

## Changelog

- 2026-09-24 — v0.9 — Creación inicial con clasificación por bloques (YANG, Ciclo 17.4)