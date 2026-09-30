---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: PENDIENTE_AUDITORIA
last_updated: 2026-09-30
version: 1.0
---

# Fix de deduplicación y robustez — `script_97_emit_alerts.py`

Rama `claude/fix-dedup-97` (sin pushear). Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente.

## 1. Método

| Paso | Contenido |
|---|---|
| Hipótesis inicial | "La dedup por mint de script_97 falla y duplicó PARASITE en `_all_alerts.json`" |
| Datos | `_all_alerts.json` (9 registros), `git log -S <mint>`, Jupiter `/tokens/v2/search`, logs de GitHub Actions (`gh run view`) |
| Test | Buscar mints repetidos exactos; reproducir cada bug en un test que **falle con el script original** y pase con el fix |
| Resultado | **Hipótesis refutada** para el archivo; se encontraron 3 mecanismos reales de duplicación/pérdida en el envío |

## 2. Hallazgos

### 2.1 "PARASITE duplicado" = dos tokens distintos con el mismo símbolo [V]

| Mint | Alertado | Creado (Jupiter) | Holders | Dev | Organic score |
|---|---|---|---|---|---|
| `8ed8xX8TVRDdeyyUwq7Kyo8VwxMWZ6c5J6ertxaBpump` | 2026-09-29 16:51 UTC (commit `85a70bd`) | 2026-09-29 16:48 | 2197 | `ECeMhE…` | 0 |
| `3kmygWKZBkCYrgZHKfiuB9UFKTcDLTFFsKo3BWpmpump` | 2026-09-29 17:55 UTC (commit `8841205`) | 2026-09-29 00:57 | 8963 | `8RXNzg…` | 75 |

- La dedup por mint **funcionó**: 0 mints repetidos en el historial [V].
- Ambos se llaman "Parasite", pero tienen devs distintos. Cuál es la copia es [I] ambiguo.
- El riesgo real es para el usuario: dos alertas "PARASITE" sin ningún aviso, y puede comprar el token equivocado.

### 2.2 Mecanismos reales de duplicación / pérdida [V]

| # | Bug | Evidencia | Efecto |
|---|---|---|---|
| 1 | `_precision_log.json` pasó a formato curado (dict); con 10 alertas `precision_log.append` explota **después** de enviar y escribir | run `36651496249` (00:40 UTC): `Alerta enviada a Telegram exitosamente` → `AttributeError: 'dict' object has no attribute 'append'` | step falla → commit salteado → la alerta no se persiste → **se reenvía** en el ciclo siguiente; la detección del ciclo tampoco se commitea |
| 2 | `send_telegram` se llamaba **antes** de validar el precio; sin precio → `continue` sin registrar | código (L163 vs L169-174 del original) + test `test_sin_precio_no_se_envia_ni_se_registra` falla con el original | el token se reenvía **en cada ciclo** mientras siga en los primeros 3 candidatos |
| 3 | `except: pass` al leer `_all_alerts.json` → lista vacía → el `json.dump` final **sobrescribe el historial** | experimento con el original: `[SI, OURA` truncado → queda `[C3]` (1 registro) | pérdida total del historial + re-alertas de todo |

### 2.3 Estado de la pausa de emisiones [V]

- Hasta el push de `c19c60c` (≈01:02 UTC del 30/09), "Emit alerts" corría y **enviaba a Telegram**: `PAUSE_EMISSIONS` no existía en el workflow de `origin/main`, y `script_97` tampoco lee esa variable.
- Desde el push, el step queda `skipped`: run `36653761882`, 01:09 UTC.
- Consecuencia [I]: mientras esté pausado **no se registra ninguna alerta nueva**. No hay modo sombra, y el trust loop no recibe casos.

## 3. Fix (solo `script_97`)

1. **Dedup por mint normalizado**, sobre todo el historial (activas y cerradas):
   - saca espacios;
   - pasa las direcciones EVM `0x…` a minúsculas;
   - Base58 se compara exacto, porque distingue mayúsculas.
2. **Colisión de símbolo**: el mint nuevo se registra igual (no es un duplicado), pero además:
   - agrega `symbol_collision: [otros mints]` al registro;
   - suma una advertencia al mensaje: "Ya alertamos OTRO token con el símbolo X…";
   - agrega un evento `symbol_collision` en `_cycle_log.json`.
3. **Orden seguro**: precio válido → registro persistido (escritura atómica) → envío → `telegram_sent`. Un fallo posterior ya no produce reenvíos.
4. **Historial ilegible o que no es una lista**: no envía, **no sobrescribe**, registra `corrupt_alerts_file` y devuelve exit 1. El job falla a la vista, en lugar de borrar datos.
5. **Precision log**: solo agrega el placeholder si el archivo es una lista y hubo emisiones en el ciclo. Nunca tumba el step.
6. **`_cycle_log.json`**:
   - eventos nuevos en `dedup_events` (`symbol_collision`, `existing_duplicates`, `intra_cycle_duplicates`, `corrupt_alerts_file`);
   - idempotentes por `key`: el mismo hallazgo no se repite en cada corrida;
   - no toca `cycles`.

Sin cambios: umbral score ≥ 50, máximo 3 por ciclo, formato del mensaje (salvo la línea de colisión), campos existentes del registro.
Campos nuevos: `symbol_collision` (opcional) y `telegram_sent`.

## 4. Tests — `04_Config/scripts/test_script_97_dedup.py`

15 tests con `unittest`, sobre un directorio temporal y con Telegram interceptado. Nunca tocan los JSON canónicos.

| Grupo | Casos |
|---|---|
| Dedup | mint ya alertado (activo y cerrado) no se reenvía · mismo símbolo con distinto mint **sí** se registra y queda marcado · sin colisión no agrega campo · variantes de espacios y mayúsculas EVM · Base58 distingue mayúsculas · dos corridas idempotentes |
| Robustez | JSON corrupto y JSON que no es lista: no emite ni sobrescribe · archivo inexistente = primera corrida · sin precio no envía ni registra · Telegram fallido queda registrado y no se reenvía · precision log curado no tumba el step (reproduce el crash de producción) · duplicados preexistentes se reportan una vez y no se borran · `_cycle_log` conserva `cycles` · la escritura atómica no deja `.tmp` |

| Versión | Resultado |
|---|---|
| Fix | **15/15 OK** |
| Original (`.bak3`) | 12/15 fallan: 5 por bugs reales (crash del precision log, envío sin precio, variantes EVM y de espacios, colisión sin marcar, corrupto → sobrescritura) y el resto por interfaz (el original devuelve `None` y no tiene las funciones ni los eventos nuevos) |

## 5. Pendiente / decisiones

- **[P] Reactivar emisiones:** con el fix se puede, pero la decisión es de Dirección. Primero conviene resolver el flood del scoring v7.2 (38/61 = 62% ALERTA en la primera corrida de producción).
- **[P] Pausa dentro del script:** `script_97` sigue sin leer `PAUSE_EMISSIONS` y hoy depende solo del `if:` del workflow. Se puede sumar como defensa en profundidad si YANG lo aprueba.
- **[P] Modo sombra:** ¿registrar alertas sin enviarlas mientras esté pausado? Hoy no se registra nada.
- **[P] Causa de las otras fallas de `pipeline_t0`:** 23:07, 23:28 y 00:11 UTC fallaron en "Emit alerts", pero los logs no traen la salida del step.
- **Deuda:** `candidates[:3]` ocupa cupos con tokens sin precio que después se saltean. Hoy no generan reenvíos, pero pueden bloquear alertas válidas.
