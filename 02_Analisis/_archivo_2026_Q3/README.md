# Archivo 2026-Q3 (D-089-R)

Carpetas y archivos de `02_Analisis/` **sin escritor activo**, movidos acá el 2026-10-04 con `git mv` (la historia de
cada archivo se conserva: `git log --follow <ruta>`). No se borró nada.

**Qué es.** Salidas de la etapa de investigación de septiembre de 2026 (scripts numerados de un solo uso: detecciones
v3–v6, modos sombra, deep dives, panoramas, pruebas de MCP) y logs del pipeline anterior que ya tienen reemplazo vivo.

**Por qué se archivó.** El patrimonio de datos (D-087, `02_Analisis/patrimonio/_inventario.json`) las marcó `legado`:
ningún workflow las escribe y ningún script en producción las lee como insumo. Dirección ordenó archivarlas (D-089-R)
para que el primer nivel de `02_Analisis/` muestre solo lo vivo. El criterio fue el aporte al fin, no la fecha.

**Antes de mover se verificó** (grep en `04_Config/scripts`, workflows y tests):
- `_cycle_log.json` y `_precision_log.json` de la raíz: script_97, script_98 y monitor_shadow usan los de `alerts/`, no estos.
- `pre_launch/`: script_97 lee `pre_launch/_prelaunch_accumulated.json` para el grupo b de `lib_scoring_multichain`.
  El archivo tenía las tres listas vacías, el grupo b es solo de registro (nunca emite) y su escritor (script_99) está
  deprecado desde D-079. Sin el archivo, `_read_json_file` devuelve `None`: el resultado es el mismo que con listas vacías.
  El reemplazo es el calendario de `02_Analisis/prelaunch/` (bot_prelaunch_calendar).
- `riesgo`, `tracking`: en el código activo aparecen como palabras o claves de diccionario, no como rutas.

**Si un script viejo se vuelve a correr**, recrea su carpeta en `02_Analisis/` y `test_lib_patrimonio` lo marca: hay que
anotarla en el inventario o devolver el script a este archivo.

## Cuantitativo (17)

| Ruta | Qué es | Quién escribía | Archivos |
|---|---|---|---|
| `detection_v3/` | detección v3 | script_84_detection_v3 | 1 |
| `detection_v4/` | detección v4 | script_85_detection_v4 | 2 |
| `detection_v5/` | detección v5 | script_86_detection_v5 | 1 |
| `detection_v6/` | detección v6 (parciales) | script_87_detection_v6 | 12 |
| `dual_scoring/` | scoring dual | script_83_dual_scoring | 1 |
| `early_detection/` | filtros adaptativos de detección temprana | script_46_early_detection, script_46b/46c | 3 |
| `early_radar/` | radar temprano | script_66_crypto_early_radar | 1 |
| `enriched_candidates/` | candidatos enriquecidos | script_58_enrich_candidates | 1 |
| `holder_analysis/` | análisis de holders | script_44_holder_analysis, script_44b_holder_rpc | 1 |
| `riesgo/` | herramientas de riesgo y tamaño de posición | script_19*_honest_risk / quantoracle / zarq | 3 |
| `risk_check/` | chequeo de riesgo (cryptoguard) | script_67_cryptoguard | 1 |
| `shadow_mode/` | candidatos en modo sombra | script_91_shadow_mode | 1 |
| `shadow_v2/` | modo sombra v2 | script_92_shadow_v2 | 21 |
| `shadow_v3/` | modo sombra v3 (caché) | script_93_shadow_v3, script_94_shadow_v3 | 2 |
| `shadow_v5/` | modo sombra v5 | script_96_shadow_v5 | 2 |
| `tracking/` | seguimiento de precio y degradación | script_38_price_tracker, script_38b_tracking_degradacion | 2 |
| `volume_anomaly/` | anomalías de volumen | script_45_volume_anomaly, script_45b | 1 |

## Informativo (6)

| Ruta | Qué es | Quién escribía | Archivos |
|---|---|---|---|
| `crypto_signals/` | señales de un daemon externo | script_75_crypto_signals, script_75b (daemon) | 2 |
| `cryptowhale_insights/` | insights de ballenas | script_77_cryptowhale_insights | 1 |
| `inspect_threews/` | inspección puntual | script_79_inspect_threews | 1 |
| `mcp_stdio/` | herramientas MCP probadas | script_34_mcp_stdio_client, script_34b | 1 |
| `narrativas/` | narrativescope y tokens de agentes IA | script_16_narrativescope, script_18_ai_agents_tokens | 4 |
| `token_intel/` | inteligencia por token | script_76_token_intel | 1 |

## Calendario (3)

| Ruta | Qué es | Quién escribía | Archivos |
|---|---|---|---|
| `airdrops_parsed/` | airdrops parseados (API y Selenium) | script_56_airdrop_api, script_50_parse_airdrops | 3 |
| `pre_launch/` | acumulado del calendario viejo | script_99_prelaunch + prelaunch.yml (deprecados en D-079) | 1 |
| `tge_parsed/` | TGE parseados (Selenium) | script_49_parse_tge | 2 |

## Resultados (12)

| Ruta | Qué es | Quién escribía | Archivos |
|---|---|---|---|
| `_contracts/` | contrato de salida de script_98 | corrida de script_98 (contrato de salida) | 1 |
| `_cycle_log.json` | log de ciclos anterior al de alerts/ | pipeline anterior a alerts/_cycle_log.json | 1 |
| `_evidence/` | evidencia de corridas de script_98 | corrida de script_98 del 2026-09-24 | 1 |
| `_precision_log.json` | precisión anterior al de alerts/ | script_98 anterior a alerts/_precision_log.json | 1 |
| `_state_manifest.json` | manifiesto de estado de 2026-09-24 | sin escritor en el código actual | 1 |
| `auditorias/` | deep dive de movers y auditoría histórica | script_05_deep_dive_movers, script_06_historical_audit | 2 |
| `casos_historicos/` | casos históricos | script_43_historical_cases | 1 |
| `deep_dive_deficlaw/` | deep dive puntual | script_36_deep_dive_deficlaw | 1 |
| `deep_dive_verified/` | deep dive verificado | script_36b_deep_dive_verified | 2 |
| `panorama/` | panorama y candidatos | script_39b/39c, script_40/40b (panorama) | 3 |
| `validation_v7/` | validación de v7 | script_90_validate_v7 | 3 |
| `verificacion_paquetes/` | verificación de paquetes y registries (supply chain) | script_33_verificar_registries | 2 |
