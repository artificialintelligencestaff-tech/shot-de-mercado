---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Contribución — Cómo Agregar Valor al Proyecto

Este archivo define **cómo cualquier agente, modelo o humano puede contribuir al proyecto** sin romper su coherencia ni duplicar esfuerzos. Es la guía de incorporación.

## 1. Quién puede contribuir

| Rol | Puede contribuir con |
|---|---|
| Humano (Dirección) | Decisiones estratégicas, autorización, contexto externo |
| YANG (analista) | Diseño, scoring, ciclos, cerebro documental |
| YIN (ejecutor) | Scripts, ejecución, evidencia |
| Otro LLM (Claude, GPT, Gemini, etc.) | Análisis paralelo, revisión crítica, ideas nuevas |
| Otro agente autónomo | Ejecución especializada, integración de fuentes |

## 2. Reglas de oro de la contribución

1. **Leer el cerebro antes de proponer.** El `SKILLS_skill_entender_proyecto.md` es obligatorio.
2. **No duplicar.** Antes de proponer algo, buscar si ya existe (`04_SCRIPTS_CATALOG.md`).
3. **Fundamentar.** Cada propuesta tiene fuente o etiqueta de especulación.
4. **No romper constraints.** Free-only, isolation, portabilidad son no negociables.
5. **Evidencia > opinión.** Sin ejecución verificable, no hay contribución válida.
6. **Etiquetar el cambio.** COMPLETO / PARCIAL / EXPERIMENTAL.
7. **Un archivo por mensaje.** Al proponer contenido largo, se fragmenta.
8. **Commit atómico.** Cada contribución se versiona individualmente.
9. **Documentar el cambio.** Si modifica el cerebro, se registra en `13_DECISIONES.md`.
10. **Respetar el append-only.** No editar entradas históricas de decisiones.

## 3. Tipos de contribución

### 3.1 Contribución al cerebro documental

**Qué:** agregar, corregir o expandir archivos del cerebro.

**Cómo:**
1. Identificar el archivo correspondiente (o proponer uno nuevo).
2. Redactar el contenido en formato markdown con header YAML.
3. Enviar a YANG vía Dirección.
4. YANG valida, ajusta, y emite versión final.
5. YIN escribe en disco.
6. Commit con mensaje: `cerebro: <archivo> — <resumen>`.

**Prohibido:** editar archivos sin pasar por YANG.

### 3.2 Contribución al pipeline

**Qué:** nuevo script, corrección de bug, optimización.

**Cómo:**
1. Identificar la función afectada en `08_PIPELINE_ACTIVO.md`.
2. Proponer cambio con justificación técnica.
3. YANG diseña la directiva.
4. YIN implementa.
5. Test + verificación empírica.
6. Documentar en `13_DECISIONES.md` si es decisión relevante.
7. Commit con mensaje: `pipeline: <script> — <cambio>`.

**Prohibido:** modificar scripts sin ejecución verificable.

### 3.3 Contribución a las fuentes

**Qué:** nueva fuente gratuita viable, reemplazo de fuente caída, mejora en la integración.

**Cómo:**
1. Verificar que la fuente es gratuita (free tier, open source).
2. Documentar en `05_FUENTES.md` con estado VIABLE.
3. Probar con script pequeño antes de integrar al pipeline.
4. Si funciona, promover a ACTIVA.
5. Commit con mensaje: `fuente: <nombre> — <estado>`.

**Prohibido:** fuentes pagas o con trial limitado.

### 3.4 Contribución a las decisiones

**Qué:** propuesta de cambio estratégico, reversión de decisión previa, nuevo rumbo.

**Cómo:**
1. Redactar con formato `D-YYYYMMDD-NN` de `13_DECISIONES.md`.
2. Incluir contexto, alternativas consideradas, consecuencias.
3. Enviar a Dirección.
4. Dirección decide.
5. Si aprueba, YANG agrega la entrada.
6. Commit con mensaje: `decision: <título>`.

**Prohibido:** decisiones unilaterales sin autorización de Dirección.

### 3.5 Contribución al scoring

**Qué:** nueva señal, ajuste de pesos, refinamiento de la fórmula.

**Cómo:**
1. Identificar la señal en `06_SCORING.md`.
2. Documentar la fuente y cómo se mide.
3. Proponer el valor de la señal (bonificación o penalización).
4. YANG valida con datos históricos si es posible.
5. Si aprueba, se integra como parte de la próxima versión (v8, v9, etc.).
6. Commit con mensaje: `scoring: <señal> — <cambio>`.

**Prohibido:** cambiar pesos con n<10 sin justificación empírica.

## 4. Flujo de contribución estándar

```
CONTRIBUYENTE
    ↓ propone
YANG
    ↓ valida, ajusta, diseña directiva
DIRECCIÓN
    ↓ autoriza
YIN
    ↓ ejecuta
EVIDENCIA VERIFICABLE
    ↓ confirma
YANG
    ↓ cierra el ciclo
```

**Nada se salta pasos.** Si un contribuyente intenta escribir directo a YIN, se redirige vía Dirección.

## 5. Cómo revisar el proyecto antes de contribuir

**Checklist mínimo:**

- [ ] Leí `SKILLS_skill_entender_proyecto.md`.
- [ ] Leí `00_NUCLEO.md` (fines del proyecto).
- [ ] Leí `02_ARQUITECTURA.md` (estructura).
- [ ] Revisé `04_SCRIPTS_CATALOG.md` para no duplicar.
- [ ] Revisé `05_FUENTES.md` para saber qué fuentes existen.
- [ ] Revisé `11_ROADMAP.md` para saber en qué fase estamos.
- [ ] Revisé `13_DECISIONES.md` para no proponer algo ya decidido.
- [ ] Mi propuesta respeta free-only, isolation, portabilidad.
- [ ] Mi propuesta trae evidencia o plan de verificación.

Si todo está marcado, la propuesta está lista.

## 6. Cómo integrar un nuevo modelo IA al proyecto

Si un LLM nuevo (Claude, GPT, Gemini, Llama, etc.) se incorpora al proyecto:

1. **Recibir el master prompt** (`99_MASTER_PROMPT.md`).
2. **Leer el cerebro completo** (18 archivos).
3. **Identificar su rol:**
   - Analista (como YANG) → diseño, scoring, ciclos.
   - Ejecutor (como YIN) → scripts, evidencia.
   - Revisor externo → análisis crítico, sin ejecución.
4. **Declarar sus capacidades específicas** (contexto, velocidad, herramientas).
5. **Firmar un "contrato de rol"** en `13_DECISIONES.md`.
6. **Comenzar a operar según el flujo estándar.**

## 7. Qué NO se acepta como contribución

- ❌ Propuestas sin fundamento ("creo que debería ser así").
- ❌ Duplicación de funciones existentes.
- ❌ Scripts sin ejecución verificable.
- ❌ Dependencias pagas.
- ❌ Cambios al pipeline sin autorización.
- ❌ Edición directa de decisiones históricas.
- ❌ Archivos fuera de `D:\Proyecto Shot de mercado\`.
- ❌ Uso de credenciales en código (deben ir en GitHub Secrets).

## 8. Reconocimiento de contribuciones

Toda contribución aceptada se registra en `13_DECISIONES.md` con el nombre del contribuyente. Es la memoria histórica del proyecto.

## 9. Canales de contribución

| Canal | Uso |
|---|---|
| Dirección (humano) | Punto de entrada único. Media todas las contribuciones. |
| GitHub Issues (futuro) | Propuestas públicas de la comunidad. |
| GitHub Pull Requests (futuro) | Contribuciones de código externas. |

**Regla:** sin autorización de Dirección, ninguna contribución se integra.

## 10. Errores comunes del contribuyente novato

| Error | Corrección |
|---|---|
| Proponer sin leer el cerebro | Leer primero, proponer después |
| Editar archivos directo | Enviar a YANG, esperar validación |
| Inventar datos | Etiquetar con fuente o especulación |
| Ignorar free-only | Verificar antes de proponer |
| Proponer sin evidencia | Traer plan de verificación |

## VER TAMBIÉN

- [SKILLS_skill_entender_proyecto.md](SKILLS_skill_entender_proyecto.md) — entry point
- [00_Directivas_INDEX.md](00_Directivas_INDEX.md) — índice general
- [13_DECISIONES.md](13_DECISIONES.md) — bitácora de decisiones
- [11_ROADMAP.md](11_ROADMAP.md) — fase actual del proyecto

## Changelog

- 2026-09-24 — v1.0 — Creación inicial (YANG, Ciclo 17.8.C)