---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
skill_role: diagnóstico
---

# Skill — Debuggear el Proyecto

**Cuándo usar este skill:** cuando algo falla. Un script tira error, un archivo no aparece, un trust update da valores raros, un mensaje de Telegram no llega, un workflow de GitHub Actions falla.

## 1. Protocolo de diagnóstico — 5 pasos

```
PASO 1: IDENTIFICAR
  → ¿Qué se observa exactamente?
  → ¿Cuándo empezó?
  → ¿Qué cambió antes?

PASO 2: AISLAR
  → ¿Qué script está fallando?
  → ¿Qué input dispara el fallo?
  → ¿Es reproducible?

PASO 3: CAPTURAR EVIDENCIA
  → Exit code
  → stdout / stderr verbatim
  → Timestamps
  → Hashes de archivos

PASO 4: BUSCAR PRECEDENTE
  → ¿Está en 12_TROUBLESHOOTING.md?
  → ¿Hay decisión en 13_DECISIONES.md?
  → ¿Hay ciclo previo con este error?

PASO 5: REPORTAR O RESOLVER
  → Si es conocido: aplicar fix documentado
  → Si es nuevo: reportar a YANG con evidencia
```

## 2. Checklist de diagnóstico rápido

- [ ] Path canónico existe: `D:\Proyecto Shot de mercado\`.
- [ ] `.env` en `04_Config\` tiene los secrets.
- [ ] Bot Telegram responde (`getMe`).
- [ ] Script canónico elegido correctamente (ver `08_PIPELINE_ACTIVO.md`).
- [ ] Python 3.11 disponible.
- [ ] Dependencias instaladas (`requests`, `dotenv`, `websockets`).
- [ ] Espacio en disco.
- [ ] Permisos de escritura en la carpeta.

## 3. Comandos de diagnóstico por área

### 3.1 Verificar entorno

```bash
# Python version
python --version

# Path canónico
python -c "import os; print('EXISTS:', os.path.isdir(r'D:\Proyecto Shot de mercado'))"

# Dependencias
python -c "import requests, dotenv, websockets; print('OK')"
```

### 3.2 Verificar bot Telegram

```bash
# ¿El token es válido?
python -c "from dotenv import load_dotenv; import os, requests; load_dotenv(r'D:\Proyecto Shot de mercado\04_Config\.env'); t=os.getenv('TELEGRAM_BOT_TOKEN'); r=requests.get(f'https://api.telegram.org/bot{t}/getMe', timeout=10); print(r.json())"
```

Si devuelve `{"ok": true, "result": {...}}` → bot OK.
Si devuelve `{"ok": false}` → token inválido.

### 3.3 Verificar archivos de estado

```bash
# Listar todos los .json de estado
python -c "import os; root=r'D:\Proyecto Shot de mercado'; [print(os.path.join(r,f)) for r,_,fs in os.walk(root) for f in fs if f.endswith('.json') and (f.startswith('_') or f.startswith('trust_'))]"

# Verificar que _all_alerts.json sea JSON válido
python -c "import json; json.load(open(r'D:\Proyecto Shot de mercado\02_Analisis\alerts\_all_alerts.json')); print('JSON OK')"
```

### 3.4 Verificar hashes de archivos

```bash
# SHA-256 de un archivo
python -c "import hashlib; p=r'D:\Proyecto Shot de mercado\02_Analisis\alerts\_all_alerts.json'; print(hashlib.sha256(open(p,'rb').read()).hexdigest())"
```

Si el hash tiene patrones repetidos → sospechoso. Comparar con `_state_manifest.json`.

### 3.5 Verificar ejecución de script

```bash
cd "D:\Proyecto Shot de mercado"
python 04_Config/scripts/<script>.py 2>&1 | tee /tmp/script_output.log
echo "EXIT: $?"
```

Capturar todo. No resumir.

## 4. Errores comunes y soluciones

### Error 1 — Trust update da `price_change_pct: 0.0` siempre

**Diagnóstico:**
```bash
python -c "import json; a=json.load(open(r'D:\Proyecto Shot de mercado\02_Analisis\alerts\_all_alerts.json')); [print(x['symbol'], x.get('trust_updates')) for x in a]"
```

Si `trust_updates` tiene `price_change_pct: 0.0` en todos los stages → bug de baseline.

**Solución:** ver `12_TROUBLESHOOTING.md` Error 1. Fix en Ciclo 18.1.

### Error 2 — `FILE_NOT_FOUND` en ruta esperada

**Diagnóstico:**
```bash
# Buscar el archivo en cualquier parte del proyecto
python -c "import os; [print(os.path.join(r,f)) for r,_,fs in os.walk(r'D:\Proyecto Shot de mercado') for f in fs if f=='<nombre_archivo>']"
```

Si aparece en otra ruta → ajustar el script para usar esa ruta (o `_project_manifest.json`).

**Solución:** ver `12_TROUBLESHOOTING.md` Error 2.

### Error 3 — Hash con patrones repetidos

**Diagnóstico:** un SHA-256 real es criptográficamente aleatorio. Si tiene secuencias como `a1b2c3d4`, `c0d1e2f3`, etc. → sospechoso.

**Solución:** recapturar el hash directamente del filesystem. Nunca retype.

### Error 4 — Mensaje truncado

**Diagnóstico:** verificar la longitud del mensaje antes de enviar.

**Solución:** fragmentar en micro-mensajes <=2 KB. Un archivo por mensaje.

### Error 5 — Telegram no envía

**Diagnóstico:**
```bash
# Test manual
python -c "from dotenv import load_dotenv; import os, requests; load_dotenv(r'D:\Proyecto Shot de mercado\04_Config\.env'); t=os.getenv('TELEGRAM_BOT_TOKEN'); c=os.getenv('TELEGRAM_CHAT_ID'); r=requests.post(f'https://api.telegram.org/bot{t}/sendMessage', json={'chat_id': c, 'text': 'test'}, timeout=10); print(r.status_code, r.json())"
```

Si `status_code != 200` → revisar `response.json()` para el error exacto (chat_id incorrecto, bot bloqueado, etc.).

### Error 6 — API externa falla (429, 500)

**Diagnóstico:**
```bash
# Test manual contra la API
python -c "import requests; r=requests.get('https://api.dexscreener.com/latest/dex/tokens/<mint>', timeout=10); print(r.status_code, r.text[:200])"
```

Si es 429 → rate limit alcanzado. Esperar. Si es 500 → API caída.

**Solución:** reintentar con backoff. Si persiste, usar fuente alternativa de `05_FUENTES.md`.

### Error 7 — Script corre pero no produce output

**Diagnóstico:**
1. Verificar exit code: `echo $?`.
2. Verificar que el script tenga `if __name__ == "__main__": main()`.
3. Verificar que el script escriba al stdout (print o log).
4. Ejecutar con `python -u` (unbuffered).

### Error 8 — GitHub Actions falla (futuro)

**Diagnóstico:**
1. Abrir el run en GitHub UI.
2. Ver el step que falló.
3. Capturar el log completo.
4. Comparar con ejecución local.

**Solución común:**
- Falta un secret → cargar en Settings → Secrets.
- Falta una dependencia → actualizar `requirements.txt`.
- Path diferente → usar `$GITHUB_WORKSPACE`.

## 5. Árbol de decisión — ¿resolver o reportar?

```
¿Es error conocido?
├── SÍ → ¿Tiene fix documentado?
│   ├── SÍ → Aplicar fix. Verificar.
│   └── NO → Reportar a YANG con evidencia.
└── NO → Reportar a YANG con evidencia completa.
```

**Regla:** nunca modificar código sin autorización de YANG. Solo resolver si el fix ya está documentado en `12_TROUBLESHOOTING.md`.

## 6. Formato de reporte de bug

```
BUG REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SÍNTOMA: <qué se observa>
REPRODUCIBLE: SÍ / NO / A VECES
SCRIPT: <script afectado>
COMANDO: <comando exacto>
EXIT CODE: <N>

--- STDOUT ---
<stdout verbatim>

--- STDERR ---
<stderr verbatim>

--- TIMESTAMP ---
<ISO8601>

--- CONTEXTO ---
<qué se hizo antes>

--- ¿ESTÁ EN 12_TROUBLESHOOTING? ---
SÍ (Error N) / NO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Sin narrativa adicional. Solo evidencia.

## 7. Reglas operativas

1. **Capturar toda evidencia** antes de proponer fix.
2. **No modificar código en caliente.** Reportar a YANG.
3. **Documentar nuevos errores** en `12_TROUBLESHOOTING.md` siguiendo el formato.
4. **No reintentar más de 3 veces** sin reportar.
5. **No ocultar errores.** Un error no documentado es un error que va a volver.
6. **Aislar el problema.** Un script a la vez.
7. **Usar `-u` para Python** cuando se diagnostica output faltante.

## 8. Ejemplos de diagnóstico resueltos

### Ejemplo 1 — Trust update da 0.0%

**Reporte a YANG:**
- Síntoma: `price_change_pct: 0.0` en todos los trust updates.
- Comando: `python 04_Config/scripts/script_98_trust_scheduler.py`.
- Exit: 0.
- stdout: `[TRUST UPDATE] SI (t+1h): Precio=$0.000002 (+0.0%) -> Confianza: 56% [NEUTRAL]`.
- Análisis: precio actual = precio de referencia → bug de baseline.
- Fix: Ciclo 18.1.

### Ejemplo 2 — Telegram no envía

**Reporte a YANG:**
- Síntoma: script 97 reporta exit 0 pero no llega mensaje a Telegram.
- Diagnóstico: `getMe` devuelve `ok:true` pero `sendMessage` devuelve 400.
- Causa: `chat_id` mal formateado.
- Fix: verificar el `TELEGRAM_CHAT_ID` en `.env`.

### Ejemplo 3 — Shadow modes duplicados

**Reporte a YANG:**
- Síntoma: `_accumulated.json` de v4 y v5 crecen simultáneamente.
- Causa: migración incompleta.
- Fix: consolidar en v5. Deprecar v4 (Ciclo 18.6).

## 9. Recursos relacionados

- `12_TROUBLESHOOTING.md` — errores conocidos y fixes.
- `13_DECISIONES.md` — decisiones históricas que explican comportamientos.
- `08_PIPELINE_ACTIVO.md` — scripts canónicos.
- `_OPERATOR_HANDBOOK.md` — rutina diaria.

## VER TAMBIÉN

- [SKILLS_skill_entender_proyecto.md](SKILLS_skill_entender_proyecto.md) — entry point
- [SKILLS_skill_ejecutar_pipeline.md](SKILLS_skill_ejecutar_pipeline.md) — ejecución
- [SKILLS_skill_agregar_alerta.md](SKILLS_skill_agregar_alerta.md) — emisión
- [12_TROUBLESHOOTING.md](12_TROUBLESHOOTING.md) — errores conocidos

## Changelog

- 2026-09-24 — v1.0 — Creación inicial (YANG, Ciclo 17.10.C)