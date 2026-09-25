---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Troubleshooting — Errores Conocidos y Cómo Resolverlos

Este archivo documenta errores ya encontrados, su causa raíz, y la solución. Sirve para que cualquier agente o humano resuelva problemas sin re-descubrirlos.

## Formato de entrada

Cada error documenta:
- **Síntoma:** qué se observa.
- **Causa raíz:** por qué ocurre.
- **Impacto:** qué rompe.
- **Solución:** cómo se arregla.
- **Prevención:** cómo evitar que vuelva a pasar.
- **Estado:** ABIERTO, RESUELTO, MITIGADO.

---

## Error 1 — Trust scheduler da `price_change_pct: 0.0` siempre

**Síntoma:** todos los trust updates registran cambio de precio cero, incluso cuando el precio real cambió significativamente.

**Causa raíz:** en la primera pasada, `trust_updates` está vacío, y el código hace `prev_price = current_price`. Esto compara el precio contra sí mismo.

**Impacto:** ALTO. Los trust updates nunca aplican ajustes reales. La confianza queda congelada. Los veredictos quedan en NEUTRAL permanente.

**Solución:** ver `07_TRUST_UPDATE.md` sección 8. Fix en 3 partes:
1. Persistir `initial_price` al emitir alerta.
2. Corregir el cálculo en `script_98_trust_scheduler.py`.
3. Backfill retroactivo de SI y OURA con `initial_price: null`.

**Prevención:** test automatizado que valide `price_change_pct != 0.0` cuando el precio de emisión y el actual difieren.

**Estado:** ABIERTO — fix planificado para Ciclo 18.1.

---

## Error 2 — `FILE_NOT_FOUND` en rutas esperadas

**Síntoma:** scripts reportan `FILE_NOT_FOUND` para archivos que deberían existir.

**Causa raíz:** discrepancia de path entre ciclos. En Ciclos 16-17 el `_all_alerts.json` estaba en `02_Analisis\alerts\`, pero en otros ciclos se buscó en `02_Analisis\` o `02_Analisis\shadow_v4\`.

**Impacto:** MEDIO. Fuerza re-descubrimiento de rutas cada vez.

**Solución:** path canónico declarado en `_project_manifest.json`. Todos los scripts deben leer de ahí.

**Prevención:** cualquier script nuevo debe usar `_project_manifest.json` como fuente de paths.

**Estado:** MITIGADO — path canónico establecido.

---

## Error 3 — Hashes fabricados en reportes de YIN

**Síntoma:** SHA-256 reportados con patrones repetitivos (ej: `a1b2c3d4e5f607182938495a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6`).

**Causa raíz:** retype manual del contenido en lugar de lectura del filesystem.

**Impacto:** ALTO. Evidencia no confiable. Auditoría imposible.

**Solución:** usar **base64** para transmisión de contenido. Un humano o modelo no puede fabricar base64 válido.

**Prevención:** todo reporte de evidencia incluye base64 byte-exacto. Si hay truncamiento o retype, se rechaza.

**Estado:** RESUELTO — protocolo base64 implementado en Ciclo 16.5-R.

---

## Error 4 — Truncamiento de mensajes largos

**Síntoma:** respuestas de YIN cortadas mid-stream. Ejemplo: `"Block 2: Base64/23 16:44 (HKT)<resolución-yin>"`.

**Causa raíz:** mensajes de más de ~8 KB se truncan en el canal.

**Impacto:** MEDIO. Fuerza repetición de envíos.

**Solución:** fragmentar en micro-mensajes de <=2 KB. Un archivo por mensaje.

**Prevención:** nunca enviar más de un archivo .md completo con contenido >4 KB en un mensaje.

**Estado:** RESUELTO — protocolo "un archivo, un mensaje".

---

## Error 5 — Variantes de scripts sin consolidar

**Síntoma:** existen `script_XX.py`, `script_XXb.py`, `script_XXc.py`, `script_XXd.py` con funciones similares.

**Causa raíz:** cada iteración se guardó como nuevo archivo en vez de reemplazar.

**Impacto:** MEDIO. Confusión sobre cuál es canónico.

**Solución:** declarar canónicos en `08_PIPELINE_ACTIVO.md`. Mover deprecados a `_archived/`.

**Prevención:** cualquier script nuevo reemplaza al anterior o se marca explícitamente como variante experimental.

**Estado:** ABIERTO — consolidación planificada para Ciclo 18.3.

---

## Error 6 — Shadow modes v4 y v5 activos simultáneamente

**Síntoma:** dos `_accumulated.json` con mints distintos, actualizándose en paralelo.

**Causa raíz:** migración incompleta de v4 a v5. Ambos siguen corriendo.

**Impacto:** MEDIO. Recursos duplicados. Alertas potencialmente duplicadas.

**Solución:** elegir canónico (recomendado: v5). Deprecar el otro.

**Prevención:** nunca correr dos versiones del mismo pipeline en paralelo.

**Estado:** ABIERTO — decisión pendiente de Dirección (Ciclo 18.2).

---

## Error 7 — Capa 1 (pre-launch) sin TGEs detectados

**Síntoma:** `script_99_prelaunch.py` corre pero devuelve 0 candidatos.

**Causa raíz:** las fuentes activas (Metaplex, three.ws, Clawnch) no devuelven TGEs en el entorno actual.

**Impacto:** MEDIO. La Capa 1 está inerte.

**Solución:** activar fuentes alternativas (airdrops.io, Dropstab, CoinMarketCal). Ver `05_FUENTES.md`.

**Prevención:** monitorear periódicamente cada fuente pre-launch. Si una cae, migrar a VIABLE.

**Estado:** ABIERTO — Fase 3 del roadmap.

---

## Error 8 — Git no inicializado

**Síntoma:** `git status` en `D:\Proyecto Shot de mercado` devuelve "not a git repository".

**Causa raíz:** el proyecto siempre se manejó localmente sin control de versiones.

**Impacto:** ALTO. Sin Git no hay portabilidad real, ni CI/CD, ni rollback.

**Solución:** `git init`, crear `.gitignore`, primer commit.

**Prevención:** n/a — es un one-time fix.

**Estado:** ABIERTO — Ciclo 17.11.

---

## Error 9 — Sin workflows de GitHub Actions

**Síntoma:** `.github/workflows/` no existe en el proyecto.

**Causa raíz:** migración a serverless aún no ejecutada.

**Impacto:** ALTO. El bot no corre 24/7 sin intervención local.

**Solución:** crear workflows `trust_update.yml`, `pipeline_t0.yml`, `prelaunch.yml`.

**Prevención:** n/a.

**Estado:** ABIERTO — Ciclo 17.12.

---

## Error 10 — Artefactos de truncamiento en documentación

**Síntoma:** documentos con caracteres contaminantes: `וֹכ6h`, `tire 20%`, `rub_ logs`, `on saat`, `alimentos.json`, `cenes`, `đẻ`.

**Causa raíz:** generación de texto con contaminación de encodings mezclados (hebreo, turco, alemán).

**Impacto:** BAJO funcionalmente, MEDIO en calidad de documentación.

**Solución:** regenerar el documento afectado. Verificar con `grep -E '[^\x00-\x7F]'` (contando solo caracteres fuera de UTF-8 extendido legítimo).

**Prevención:** revisar cada documento antes de entregarlo.

**Estado:** MITIGADO — documentos del cerebro actuales están limpios.

---

## Cómo diagnosticar un problema nuevo

1. **Identificar síntoma:** ¿qué se observa exactamente?
2. **Reproducir:** ¿se puede reproducir el error?
3. **Aislar:** ¿qué script está fallando? ¿qué input lo dispara?
4. **Capturar evidencia:** exit code, stdout, stderr, timestamps.
5. **Buscar precedente:** ¿está en este archivo?
6. **Si no está:** documentarlo siguiendo el formato de arriba.
7. **Reportar a YANG** vía Dirección con evidencia.
8. **YANG emite directiva** con fix.
9. **YIN aplica fix** y verifica.
10. **Actualizar este archivo** con estado RESUELTO o MITIGADO.

## Comandos de diagnóstico rápido

```
# Verificar que Git esté inicializado
git status

# Verificar que el bot Telegram funcione
python -c "from dotenv import load_dotenv; import os, requests; load_dotenv(r'D:\Proyecto Shot de mercado\04_Config\.env'); t=os.getenv('TELEGRAM_BOT_TOKEN'); r=requests.get(f'https://api.telegram.org/bot{t}/getMe', timeout=10); print(r.json())"

# Verificar que el path canónico exista
python -c "import os; print('EXISTS:', os.path.isdir(r'D:\Proyecto Shot de mercado'))"

# Listar todos los .json de estado
python -c "import os; root=r'D:\Proyecto Shot de mercado'; [print(os.path.join(r,f)) for r,_,fs in os.walk(root) for f in fs if f.endswith('.json') and (f.startswith('_') or f.startswith('trust_'))]"
```

## VER TAMBIÉN

- [07_TRUST_UPDATE.md](07_TRUST_UPDATE.md) — bug de baseline en detalle
- [08_PIPELINE_ACTIVO.md](08_PIPELINE_ACTIVO.md) — scripts canónicos y deprecados
- [10_ESTADO_ACTUAL.md](10_ESTADO_ACTUAL.md) — snapshot vivo del proyecto
- [13_DECISIONES.md](13_DECISIONES.md) — bitácora de decisiones

## Changelog

- 2026-09-24 — v1.0 — Creación inicial con 10 errores documentados (YANG, Ciclo 17.7.C)