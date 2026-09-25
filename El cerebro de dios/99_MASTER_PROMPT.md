---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
entry_point: true
---

# 99 — Master Prompt del Proyecto Shot de Mercado

**Si sos un agente IA o humano que acaba de recibir este archivo, leelo completo (5 minutos). Después tendrás todo lo necesario para entender, operar o contribuir al proyecto.**

## 1. Qué es el Proyecto Shot de Mercado

Un bot autónomo de predicción que detecta aceleraciones verticales (>20% en 24-48h) de activos blockchain, usando multiplicidad de filtros independientes gratuitos, y comunica alertas accionables vía Telegram para usuarios no-técnicos.

**No es un oráculo. No es asesoramiento financiero. Es un sistema probabilístico que declara confianza explícita.**

## 2. Los 3 universos de activos que cubre

| Universo | Definición | Ejemplos |
|---|---|---|
| **A** | Activos maduros, liquidez alta, historia larga | BTC, ETH, SOL |
| **B** | Activos en circulación con narrativa en desarrollo | UNI, ICP, APT, PSG |
| **C** | Activos pre-lanzamiento (TGEs, airdrops anunciados) | LIBRA, futuras TGEs |

Cada universo tiene señales distintas. Se tratan distinto.

## 3. Las 5 capas del pipeline

```
1. PRE-LAUNCH    → TGEs y airdrops antes del listing (cada 6h)
2. T+0           → Captura tokens al instante de creación (continuo)
3. ENRIQUECIMIENTO → Quality Gate + scoring (cada 20 min)
4. ALERT + TRUST → Alertas Telegram + trust updates (1h/6h/24h)
5. FEEDBACK LOOP → Precisión medida + ajuste de scoring
```

## 4. Constraints no negociables

- ✅ **Free-only:** todos los servicios, APIs, MCPs son gratuitos.
- ✅ **Isolation:** todo vive en `D:\Proyecto Shot de mercado\`.
- ✅ **Portabilidad:** cualquier agente o humano puede tomar el proyecto.
- ✅ **Evidencia > documentación:** sin ejecución verificable, no hay progreso.
- ✅ **Un ciclo = un objetivo verificable:** no se dispersa.
- ❌ No promete ganancias. No es asesoramiento financiero.

## 5. Roles del proyecto

| Rol | Quién | Responsabilidad |
|---|---|---|
| **Dirección** | Humano | Decide, autoriza, media |
| **YANG** | DeepSeek (o equivalente) | Diseña, evalúa, documenta |
| **YIN** | Hermes + Ling (o equivalente) | Implementa, verifica, reporta |

Ningún rol hace el trabajo del otro.

## 6. Índice del cerebro documental

Todos los archivos viven en `D:\Proyecto Shot de mercado\El cerebro de dios\`.

### Fundacionales

| Archivo | Qué contiene |
|---|---|
| `README.md` | Entrada raíz del proyecto |
| `00_Directivas_INDEX.md` | Índice central |
| `00_NUCLEO.md` | Propósito raíz |
| `_MANIFESTO.md` | Por qué existe el proyecto |
| `_GLOSARIO.md` | Términos y referencias |
| `_OPERATOR_HANDBOOK.md` | Manual del operario |

### Cerebro (arquitectura y operación)

| # | Archivo | Qué contiene |
|---|---|---|
| 01 | `01_HISTORIA.md` | Cronología del proyecto |
| 02 | `02_ARQUITECTURA.md` | Las 5 capas |
| 03 | `03_FLUJOS.md` | Workflows del sistema |
| 04 | `04_SCRIPTS_CATALOG.md` | Catálogo de ~100 scripts |
| 05 | `05_FUENTES.md` | APIs, MCPs, fuentes gratuitas |
| 06 | `06_SCORING.md` | Fórmula de scoring v7 |
| 07 | `07_TRUST_UPDATE.md` | Actualización de confianza |
| 08 | `08_PIPELINE_ACTIVO.md` | Scripts canónicos vs. deprecados |
| 09 | `09_ALERTAS.md` | Formato Telegram |
| 10 | `10_ESTADO_ACTUAL.md` | Snapshot vivo |
| 11 | `11_ROADMAP.md` | Fases y ciclos |
| 12 | `12_TROUBLESHOOTING.md` | Errores conocidos + fix |
| 13 | `13_DECISIONES.md` | Bitácora histórica |
| 14 | `14_METRICAS.md` | Precisión y cobertura |
| 15 | `15_CONTRIBUCION.md` | Guía de contribución |

### Skills (entry points por rol)

| Archivo | Para qué |
|---|---|
| `SKILLS_skill_entender_proyecto.md` | **Leer primero si sos agente nuevo** |
| `SKILLS_skill_ejecutar_pipeline.md` | Cómo correr el pipeline |
| `SKILLS_skill_agregar_alerta.md` | Cómo emitir una alerta |
| `SKILLS_skill_debuggear.md` | Cómo diagnosticar fallos |
| `SKILLS_skill_contribuir.md` | Cómo proponer mejoras |

### Meta

| Archivo | Qué contiene |
|---|---|
| `99_MASTER_PROMPT.md` | Este archivo. Entry point único. |

## 7. Cómo navegar según tu rol

| Si sos... | Leé en este orden |
|---|---|
| **Agente nuevo (cualquier modelo)** | Este archivo → `SKILLS_skill_entender_proyecto.md` → `00_NUCLEO.md` → `02_ARQUITECTURA.md` |
| **YIN (ejecutor)** | Este archivo → `SKILLS_skill_ejecutar_pipeline.md` → `03_FLUJOS.md` |
| **YANG (analista)** | Este archivo → todo el cerebro |
| **Dirección (humano)** | Este archivo → `_MANIFESTO.md` → `_OPERATOR_HANDBOOK.md` |
| **Revisor externo** | Este archivo → `13_DECISIONES.md` → `14_METRICAS.md` |
| **Contribuyente** | Este archivo → `SKILLS_skill_contribuir.md` → `15_CONTRIBUCION.md` |

## 8. Estado actual (al 2026-09-24)

- **Fase:** 0 — Fundación documental + migración a serverless.
- **Cerebro documental:** 25 de 25 archivos completados.
- **Git:** no inicializado (próximo paso).
- **GitHub:** sin repo.
- **GitHub Actions:** sin workflows.
- **Bot Telegram:** operativo.
- **Alertas emitidas:** 2 (SI y OURA).
- **Precisión medida:** 50% (n=2, muestra insuficiente).
- **Bug conocido:** trust scheduler con `price_change_pct: 0.0` (fix en Ciclo 18.1).

## 9. Cómo contribuir

1. Leé `SKILLS_skill_contribuir.md`.
2. Verificá que tu propuesta no exista ya en el cerebro.
3. Redactá con el formato de propuesta (contexto, propuesta, fundamento, evidencia).
4. Enviá a Dirección → YANG → autorización → YIN.
5. Se registra en `13_DECISIONES.md`.

**Nunca** editar archivos del cerebro directamente. **Nunca** escribir directo a YIN sin pasar por Dirección.

## 10. Cómo se actualiza este master prompt

**Frecuencia mínima:** revisión mensual por YANG.

**Cuándo se dispara una actualización:**
- Nuevo archivo agregado al cerebro.
- Cambio en constraints o roles.
- Cambio en el roadmap (fase completada, nuevo hito).
- Cambio de modelo IA (YANG o YIN).

**Cómo lo dispara Dirección a YANG:** copiando este mensaje:

> *"YANG: revisá y actualizá `99_MASTER_PROMPT.md` según el estado actual del proyecto. Devolvé el bloque markdown completo para copiar a YIN."*

YANG devuelve el master prompt actualizado. Dirección lo copia a YIN. YIN lo escribe en disco. Se hace commit con mensaje `master_prompt: vX.Y — <cambio>`.

## 11. Frase final

El proyecto no es un oráculo. Es un sistema de anticipación probabilística con honestidad declarada.

**Antes de actuar: leer el cerebro.** Casi toda respuesta ya está escrita.

Si tenés dudas que el cerebro no resuelve, escalá a Dirección.

## VER TAMBIÉN

- [SKILLS_skill_entender_proyecto.md](SKILLS_skill_entender_proyecto.md) — entry point para agentes
- [00_NUCLEO.md](00_NUCLEO.md) — fines del proyecto
- [_MANIFESTO.md](_MANIFESTO.md) — principios
- [00_Directivas_INDEX.md](00_Directivas_INDEX.md) — índice central
- [11_ROADMAP.md](11_ROADMAP.md) — fases y ciclos
- [10_ESTADO_ACTUAL.md](10_ESTADO_ACTUAL.md) — snapshot vivo

## Changelog

- 2026-09-24 — v1.0 — Creación inicial. Entry point único del proyecto (YANG, Ciclo 17.11)