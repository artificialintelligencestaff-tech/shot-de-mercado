---
owner: Claude1 (generado)
status: GENERADO por gen_project_manifest.py --catalog (D-101)
last_updated: 2026-10-05
---

# 04 — Catálogo de scripts (generado)

No se edita a mano: `python 04_Config/scripts/gen_project_manifest.py --catalog`.

Resumen: 24 los corre un workflow · 15 los importa uno que corre · 121 sin uso (candidatos a `04_Config/scripts/_archivo/`).

## Los corre un workflow (24)

| Script | Workflow(s) |
|---|---|
| `audit_gate.py` | audit_gate.yml |
| `bot_autorepair.py` | autorepair_bot.yml |
| `bot_daily_summary.py` | daily_summary_bot.yml |
| `bot_genesis.py` | sources_genesis.yml |
| `bot_health_check.py` | health_check_bot.yml |
| `bot_influencer_tracker.py` | sources_x_influencers.yml |
| `bot_orchestrator.py` | sources_orchestrator.yml |
| `bot_prelaunch_calendar.py` | sources_prelaunch.yml |
| `bot_rss_news.py` | sources_rss.yml |
| `bot_runner.py` | sources_runner.yml |
| `bot_self_repair.py` | sources_self_repair.yml |
| `bot_telegram_public.py` | sources_telegram_a.yml, sources_telegram_b.yml |
| `dataset_builder.py` | datasets_build.yml |
| `early_review.py` | early_review.yml |
| `latency_analysis.py` | latency_analysis.yml |
| `monitor_shadow.py` | monitor_shadow_bot.yml |
| `probe_inventario.py` | probe_inventario.yml |
| `probe_narrative_sources.py` | probe_narrative_sources.yml |
| `script_114_multichain_scanner.py` | multichain_scanner.yml |
| `script_115_narrative_collector.py` | narrative_collector.yml |
| `script_116_early_watch.py` | early_watch.yml, early_watch_b.yml |
| `script_82_final_detection.py` | pipeline_t0.yml |
| `script_97_emit_alerts.py` | pipeline_t0.yml, telegram_test_send.yml |
| `script_98_trust_scheduler.py` | trust_update.yml |

## Importados por scripts vivos (15)

| Script | Workflow(s) |
|---|---|
| `calibrate_threshold_v72.py` | — |
| `lib_audit.py` | — |
| `lib_early_signals.py` | — |
| `lib_episodic_memory.py` | — |
| `lib_events.py` | — |
| `lib_info_signals.py` | — |
| `lib_knowledge_graph.py` | — |
| `lib_normalize.py` | — |
| `lib_ops.py` | — |
| `lib_persist.py` | — |
| `lib_repetition.py` | — |
| `lib_scoring_multichain.py` | — |
| `lib_scoring_young.py` | — |
| `lib_sources_store.py` | — |
| `script_113_dossier_builder.py` | — |

## Sin uso (ni workflow ni importado) (121)

| Script | Workflow(s) |
|---|---|
| `demo_gta6.py` | — |
| `gen_project_manifest.py` | — |
| `lib_adversarial_debate.py` | — |
| `lib_fusion.py` | — |
| `lib_narrative.py` | — |
| `lib_patrimonio.py` | — |
| `lib_reactive_state.py` | — |
| `lib_scientific_method.py` | — |
| `pilot_event_study_gaming.py` | — |
| `probe_grupos_activos.py` | — |
| `script_01_tops_mcp.py` | — |
| `script_01b_diagnostic_tops.py` | — |
| `script_01c_onvexia_mcp.py` | — |
| `script_01d_diagnostic_chainbase.py` | — |
| `script_01f_onvexia_extractor.py` | — |
| `script_01g_alpha_mcp.py` | — |
| `script_02_signalstack.py` | — |
| `script_03_coingecko.py` | — |
| `script_04_alpha_mcp.py` | — |
| `script_05_deep_dive_movers.py` | — |
| `script_06_historical_audit.py` | — |
| `script_09_deepblue_whales.py` | — |
| `script_09b_whale_alternatives.py` | — |
| `script_09c_verify_mcp.py` | — |
| `script_09d_coinlobster.py` | — |
| `script_09e_deepblue.py` | — |
| `script_09f_coinlobster_porciones.py` | — |
| `script_09g_coinlobster_auth.py` | — |
| `script_10_santiment.py` | — |
| `script_110_macro_context.py` | — |
| `script_112_signal_aggregator.py` | — |
| `script_11_apewisdom.py` | — |
| `script_15_coinfuty.py` | — |
| `script_15b_coinfuty_corregido.py` | — |
| `script_16_narrativescope.py` | — |
| `script_18_ai_agents_tokens.py` | — |
| `script_19b_quantoracle.py` | — |
| `script_19d_quantoracle_corregido.py` | — |
| `script_20_telegram_alert.py` | — |
| `script_20b_telegram_fixed.py` | — |
| `script_21_hoja_salida.py` | — |
| `script_21b_hoja_salida_real.py` | — |
| `script_21c_hoja_salida_final.py` | — |
| `script_21d_hoja_auditada.py` | — |
| `script_23_pipeline_maestro.py` | — |
| `script_31_limpieza.py` | — |
| `script_32_verificar_paquetes.py` | — |
| `script_33_verificar_registries.py` | — |
| `script_34_mcp_stdio_client.py` | — |
| `script_34b_mcp_stdio_client.py` | — |
| `script_35_mcp_analytics.py` | — |
| `script_35b_mcp_analytics.py` | — |
| `script_36_deep_dive_deficlaw.py` | — |
| `script_36b_deep_dive_verified.py` | — |
| `script_37_alert_catwifout.py` | — |
| `script_37b_alert_completa.py` | — |
| `script_37c_alert_profesional.py` | — |
| `script_37d_alert_multipart.py` | — |
| `script_38_price_tracker.py` | — |
| `script_38b_tracking_degradacion.py` | — |
| `script_39b_panorama_multi.py` | — |
| `script_39c_extractor_robusto.py` | — |
| `script_40_telegram_panorama.py` | — |
| `script_40b_panorama_completo.py` | — |
| `script_41_conflict_resolver.py` | — |
| `script_42_analisis_caso.py` | — |
| `script_43_historical_cases.py` | — |
| `script_44_holder_analysis.py` | — |
| `script_44b_holder_rpc.py` | — |
| `script_45_volume_anomaly.py` | — |
| `script_45b_volume_anomaly_v2.py` | — |
| `script_46_early_detection.py` | — |
| `script_46b_early_filtered.py` | — |
| `script_46c_adaptive_filter.py` | — |
| `script_51_api_direct_launches.py` | — |
| `script_52_metaplex_api.py` | — |
| `script_53_threews_api.py` | — |
| `script_54_clawnch_api.py` | — |
| `script_55_pumpportal_ws.py` | — |
| `script_56_airdrop_api.py` | — |
| `script_57_pumpportal_filter.py` | — |
| `script_58_enrich_candidates.py` | — |
| `script_59_pumpportal_filter_v2.py` | — |
| `script_60_airdrops_json.py` | — |
| `script_61_token_unlocks.py` | — |
| `script_62_airdrops_json.py` | — |
| `script_63_token_unlocks.py` | — |
| `script_64_threews_crypto.py` | — |
| `script_65_airdrop_tracker.py` | — |
| `script_66_crypto_early_radar.py` | — |
| `script_67_cryptoguard.py` | — |
| `script_68_react_framework.py` | — |
| `script_69_questions_generator.py` | — |
| `script_70_news_aggregator.py` | — |
| `script_71_madeonsol_kol.py` | — |
| `script_71b_madeonsol_kol_feed.py` | — |
| `script_72_news_cv_corregido.py` | — |
| `script_73_orderly_whales.py` | — |
| `script_74_funding_anomaly.py` | — |
| `script_75_crypto_signals.py` | — |
| `script_75b_crypto_signals_daemon.py` | — |
| `script_76_token_intel.py` | — |
| `script_77_cryptowhale_insights.py` | — |
| `script_79_inspect_threews.py` | — |
| `script_80_pipeline_maestro_v3.py` | — |
| `script_81_pipeline_final.py` | — |
| `script_83_dual_scoring.py` | — |
| `script_84_detection_v3.py` | — |
| `script_85_detection_v4.py` | — |
| `script_86_detection_v5.py` | — |
| `script_87_detection_v6.py` | — |
| `script_90_validate_v7.py` | — |
| `script_91_shadow_mode.py` | — |
| `script_92_shadow_v2.py` | — |
| `script_93_shadow_v3.py` | — |
| `script_94_shadow_v3.py` | — |
| `script_95_shadow_v4.py` | — |
| `script_96_shadow_v5.py` | — |
| `script_99_prelaunch.py` | prelaunch.yml |
| `update_doc35_hashes.py` | — |
| `young_watch_analysis.py` | — |

