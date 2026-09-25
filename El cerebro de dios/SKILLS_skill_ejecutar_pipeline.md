---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
skill_role: ejecutor
---

# Skill — Ejecutar el Pipeline

**Cuándo usar este skill:** cuando se te pide ejecutar el pipeline del proyecto (detección, scoring, alertas, trust update). Si sos YIN, este es tu skill principal.

## 1. Antes de ejecutar — checklist

- [ ] El path canónico existe: `D:\Proyecto Shot de mercado\`.
- [ ] Estás en el directorio correcto: `cd "D:\Proyecto Shot de mercado"`.
- [ ] El `.env` en `04_Config\.env` tiene `TELEGRAM_BOT_TOKEN` y `TELEGRAM_CHAT_ID`.
- [ ] Sabés qué script canónico corresponde (ver `08_PIPELINE_ACTIVO.md`).
- [ ] Tenés el permiso de Dirección para ejecutar (excepto si es operación rutinaria ya autorizada).

Si falta cualquier punto → NO ejecutar. Reportar a YANG.

## 2. Scripts canónicos por workflow

### Workflow 1 — Pipeline T+0

```bash
python 04_Config/scripts/script_55_pumpportal_ws.py         # captura
python 04_Config/scripts/script_57_pumpportal_filter.py     # filtro primario
python 04_Config/scripts/script_59_pumpportal_filter_v2.py  # Quality Gate
python 04_Config/scripts/script_58_enrich_candidates.py     # enriquecimiento
python 04_Config/scripts/script_90_validate_v7.py           # scoring v7
python 04_Config/scripts/script_97_emit_alerts.py           # alertas Telegram
```

### Workflow 2 — Trust Update

```bash
python 04_Config/scripts/script_98_trust_scheduler.py
```

**Nota:** tiene bug de baseline. Ver `12_TROUBLESHOOTING.md` Error 1.

### Workflow 3 — Pre-launch

```bash
python 04_Config/scripts/script_99_prelaunch.py
```

## 3. Cómo ejecutar — paso a paso

### 3.1 Ejecución simple

```bash
cd "D:\Proyecto Shot de mercado"
python 04_Config/scripts/<script_canonico>.py
```

Capturar:
- Timestamp de inicio.
- Timestamp de fin.
- Exit code.
- stdout completo.
- stderr completo.

### 3.2 Ejecución con evidencia

Para cada ejecución, generar un Evidence Bundle (JSON) según el formato:

```json
{
  "bundle_id": "YYYYMMDDTHHMMSSZ_script",
  "script": "script_NN_nombre.py",
  "command": "python 04_Config/scripts/script_NN_nombre.py",
  "cwd": "D:\\Proyecto Shot de mercado",
  "started_at": "ISO8601",
  "ended_at": "ISO8601",
  "exit_code": 0,
  "stdout": "...",
  "stderr": "...",
  "files_modified": [
    {"path": "", "hash_before": "", "hash_after": ""}
  ]
}
```

Guardar en `02_Analisis\_evidence\<bundle_id>.json`.

## 4. Cómo verificar éxito

### 4.1 Exit codes

| Exit code | Significado |
|---|---|
| 0 | Éxito |
| 1 | Sin candidatos / sin datos (no es error) |
| 2 | Fallo de API externa |
| 3 | Fallo de escritura de archivos |
| 124 | Timeout |
| > 125 | Error de ejecución Python |

Si exit != 0 y != 1 → reportar a YANG con stderr completo.

### 4.2 Verificaciones post-ejecución

```bash
# ¿Se actualizó _all_alerts.json?
python -c "import json,os; p='02_Analisis/alerts/_all_alerts.json'; print(json.load(open(p))) if os.path.exists(p) else print('NOT FOUND')"

# ¿Se creó o actualizó _accumulated.json?
python -c "import json,os; p='02_Analisis/shadow_v4/_accumulated.json'; print('SIZE:', os.path.getsize(p)) if os.path.exists(p) else print('NOT FOUND')"

# ¿Se registró el ciclo?
python -c "import json,os; p='_cycle_log.json'; print(json.load(open(p))) if os.path.exists(p) else print('NOT FOUND')"
```

## 5. Qué hacer si falla

### 5.1 API failure (exit 2)

1. Esperar 30 segundos.
2. Reintentar 1 vez.
3. Si falla de nuevo → registrar en `_scheduler_log.json` con `api_failed: true`.
4. Reportar a YANG.

### 5.2 Write failure (exit 3)

1. Verificar permisos de escritura en la carpeta.
2. Verificar espacio en disco.
3. Reportar a YANG con stderr.

### 5.3 Timeout (exit 124)

1. Verificar que no haya otro proceso consumiendo recursos.
2. Reintentar con timeout más alto si la operación es legítimamente larga.
3. Reportar a YANG.

### 5.4 Error desconocido

1. Capturar stdout, stderr, exit code.
2. Buscar en `12_TROUBLESHOOTING.md`.
3. Si no está documentado, reportar a YANG con toda la evidencia.

## 6. Formato de reporte

Después de cada ejecución, reportar a Dirección:

```
SCRIPT: script_NN_nombre.py
INICIO: YYYY-MM-DDTHH:MM:SSZ
FIN:    YYYY-MM-DDTHH:MM:SSZ
EXIT:   N

--- STDOUT ---
<stdout verbatim>

--- STDERR ---
<stderr verbatim>

--- ARCHIVOS MODIFICADOS ---
<path> | <hash_before> | <hash_after>

--- EVIDENCE BUNDLE ---
<path del bundle>
```

Sin narrativa adicional. Solo evidencia.

## 7. Reglas operativas

1. **Un script a la vez.** No paralelizar dentro de un mismo workflow.
2. **Capturar toda evidencia** antes de avanzar.
3. **No reintentar más de 3 veces** sin reportar.
4. **No modificar archivos de estado manualmente** salvo instrucción de YANG.
5. **No ejecutar scripts deprecados** (ver `08_PIPELINE_ACTIVO.md`).
6. **Respetar rate limits** de cada API.
7. **Nunca** subir credenciales al repo.

## 8. Ejemplos de invocación

### Ejemplo 1 — Ciclo rutinario de detección T+0

```bash
cd "D:\Proyecto Shot de mercado"
python 04_Config/scripts/script_82_final_detection.py
# Esperar exit code
# Capturar stdout/stderr
# Verificar _accumulated.json actualizado
# Reportar a Dirección
```

### Ejemplo 2 — Trust update manual

```bash
cd "D:\Proyecto Shot de mercado"
python 04_Config/scripts/script_98_trust_scheduler.py
# Verificar que _all_alerts.json tenga trust_updates actualizados
# Si price_change_pct == 0.0 siempre → reportar bug
```

### Ejemplo 3 — Envío de alerta

```bash
cd "D:\Proyecto Shot de mercado"
python 04_Config/scripts/script_97_emit_alerts.py
# Verificar en Telegram que llegó el mensaje
# Capturar message_id
```

## 9. Automatización futura (GitHub Actions)

Cuando los workflows estén activos, los scripts se ejecutan automáticamente según cron. El rol de YIN pasa de "ejecutor manual" a "auditor de ejecuciones".

Ver `03_FLUJOS.md` para detalles de cada workflow.

## 10. Recursos relacionados

- `03_FLUJOS.md` — descripción de cada workflow.
- `04_SCRIPTS_CATALOG.md` — catálogo completo de scripts.
- `08_PIPELINE_ACTIVO.md` — cuáles son canónicos.
- `12_TROUBLESHOOTING.md` — errores conocidos.

## VER TAMBIÉN

- [SKILLS_skill_entender_proyecto.md](SKILLS_skill_entender_proyecto.md) — entry point
- [SKILLS_skill_agregar_alerta.md](SKILLS_skill_agregar_alerta.md) — cómo emitir alertas
- [SKILLS_skill_debuggear.md](SKILLS_skill_debuggear.md) — cómo diagnosticar fallos
- [08_PIPELINE_ACTIVO.md](08_PIPELINE_ACTIVO.md) — scripts canónicos
- [12_TROUBLESHOOTING.md](12_TROUBLESHOOTING.md) — errores conocidos

## Changelog

- 2026-09-24 — v1.0 — Creación inicial (YANG, Ciclo 17.10.A)