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

- **[P] Reactivar emisiones:** con el fix se puede, pero la decisión es de Dirección. Primero hay que recalibrar el scoring v7.2 (ver `19_CALIBRACION_V72.md`).
- **Deuda:** `candidates[:3]` ocupa cupos con tokens sin precio que después se saltean. Hoy no generan reenvíos, pero pueden bloquear alertas válidas.

## 6. Actualización 2026-09-30 — modo sombra, pausa en el script y causa raíz de las fallas

Rama `claude/shadow-mode`. Push a main pendiente de autorización.

### 6.1 Fallas de `pipeline_t0` [V]

Logs crudos de los jobs obtenidos con `gh api .../actions/jobs/{id}/logs`:

| Run | UTC | Salida del step "Emit alerts" |
|---|---|---|
| 36605565563 | 29/09 17:31 | 2× "Alerta enviada a Telegram exitosamente" → `AttributeError` |
| 36619954659 | 29/09 19:32 | falla en "Emit alerts"; el log no trae la línea de error [P] |
| 36621908935 | 29/09 19:49 | 1 envío → `AttributeError` |
| 36631163189 | 29/09 21:07 | 1 envío → `AttributeError` |
| 36643482173 | 29/09 23:07 | 1 envío → `AttributeError` |
| 36645384707 | 29/09 23:28 | 1 envío → `AttributeError` |
| 36649102256 | 30/09 00:11 | 1 envío → `AttributeError` |
| 36651496249 | 30/09 00:40 | 1 envío → `AttributeError` |

**Causa raíz única:** el crash del precision log (§2.2, bug 1). En total hay **al menos 8 envíos a Telegram que nunca quedaron registrados.** El loop terminó con el push de `c19c60c`, cuando el step pasó a quedar `skipped`, y el bug quedó corregido en `main` con `81b07d3`.

### 6.2 Autoría de `_precision_log.json` [V]

- Hay un único commit: `6480f95`, del 2026-09-28 19:23 UTC, con el mensaje "state: crear _precision_log.json + _cycle_log.json (archivos canónicos faltantes)".
- **Nació como dict**; nunca fue una lista.
- La identidad es `Shot de Mercado Bot <bot@shotdemercado.local>`, la configuración local del repo. El bot de CI firma `shot-de-mercado-bot`, así que el commit **no** es de Actions.
- [I] Probablemente YIN: el `created_at` coincide al segundo con el cierre del ciclo 18.6 en `_cycle_log.json`. La identidad no permite distinguir entre humano y agente.

### 6.3 Diseño implementado

| Variable (env) | Efecto |
|---|---|
| `PAUSE_EMISSIONS=true` | `script_97` sale al inicio: **no procesa nada** (no registra, no envía). Tiene precedencia sobre `SHADOW_MODE` |
| `SHADOW_MODE=true` | Registra las alertas exactamente como se emitirían (mismo umbral, máximo 3 por ciclo, dedup), con `status="shadow"` y `telegram_sent=false`. **No llama a Telegram** |
| ambas en false o ausentes | Emisión normal (`active_tracking` + Telegram) |

- **Al reactivar** (`SHADOW_MODE=false`), las alertas sombra quedan como histórico y **la dedup las incluye**: un mint alertado en sombra no se re-emite más tarde. Las alertas nuevas van a `active_tracking` con envío.
- **`script_98` (guarda nueva):** solo procesa `status == "active_tracking"`; sin `status` se trata como activa (legado).
  - [V] Antes procesaba **todas** las alertas y notificaba por Telegram cuando |Δconfianza| ≥ 10.
  - Sin esta guarda, las alertas sombra habrían generado **notificaciones de alertas que el usuario nunca recibió**.
  - **La guarda de `script_98` tiene que desplegarse antes o junto con `SHADOW_MODE=true`.**
- **Cómo se mide la sombra:** el trust loop la ignora (por diseño de Dirección). Sus resultados a 48 h se miden fuera de línea con `calibrate_threshold_v72.py` (OHLCV de GeckoTerminal), sin Telegram y sin tocar `script_98`.

### 6.4 Cambio de workflow necesario (NO aplicado: requiere autorización)

Hoy el step "Emit alerts" se saltea (`if:` + `PAUSE_EMISSIONS: "true"`), así que `script_97` **no corre** y el modo sombra no puede registrar nada. Propuesta para `.github/workflows/pipeline_t0.yml`:

```diff
       - name: Emit alerts
-        if: env.PAUSE_EMISSIONS != 'true'
         env:
           ...
-          PAUSE_EMISSIONS: "true"
+          PAUSE_EMISSIONS: "false"   # la pausa ahora la resuelve el propio script
+          SHADOW_MODE: "true"        # registrar sin enviar hasta recalibrar v7.2
```

Orden de despliegue: (1) push de `script_98` y `script_97` de esta rama → (2) cambio del workflow.
Para volver a pausar del todo, alcanza con `PAUSE_EMISSIONS: "true"`, sin tocar el `if:`.

### 6.5 Tests

- `test_script_97_dedup.py`: **20/20** (15 anteriores + 5 de modos: sombra sin Telegram, envío normal, pausa con precedencia, reactivación, valores de las flags).
- `test_script_98_shadow.py`: **3/3**. **Mutación:** con el `script_98` original (sin la guarda) fallan 2 de 3.
