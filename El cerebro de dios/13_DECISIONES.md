---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
immutable_log: true
---

# Decisiones — Bitácora Histórica

Este archivo registra **cada decisión relevante** tomada en el proyecto: qué se decidió, cuándo, por quién, con qué fundamento, y qué consecuencias tuvo.

**Regla:** este archivo es **append-only**. No se editan entradas anteriores. Si una decisión se revierte, se agrega una nueva entrada indicando la reversión.

## Formato de entrada

```
### D-YYYYMMDD-NN — <título corto>
- **Fecha:** YYYY-MM-DD
- **Decisor:** Dirección | YANG | YIN
- **Contexto:** por qué se decidió
- **Decisión:** qué se decidió
- **Alternativas consideradas:** qué se descartó y por qué
- **Consecuencias:** impacto esperado
- **Estado:** VIGENTE | REVERTIDA | SUPERADA
```

---

## D-20260912-01 — Iniciar el proyecto Shot de Mercado

- **Fecha:** 2026-09-12
- **Decisor:** Dirección
- **Contexto:** exploración previa del dominio cripto; necesidad de un sistema de detección de aceleraciones verticales.
- **Decisión:** iniciar el proyecto con foco en predicción de movimientos >20% en 24-48h.
- **Alternativas consideradas:** trading automatizado (descartado: viola "no ejecutar transacciones"); análisis fundamental puro (descartado: no captura volatilidad).
- **Consecuencias:** nace el proyecto.
- **Estado:** VIGENTE.

## D-20260914-01 — Emitir las primeras 2 alertas reales (SI, OURA)

- **Fecha:** 2026-09-14
- **Decisor:** YANG + YIN
- **Contexto:** pipeline v4 detecta 2 tokens con score 55, en WATCH REAL.
- **Decisión:** bajar el umbral de emisión a 55 para emitir las dos alertas.
- **Alternativas consideradas:** mantener umbral 70 (descartado: no se emitiría ninguna alerta).
- **Consecuencias:** SI resultó FALSO POSITIVO (-95.7%); OURA resultó ACIERTO (+17,178%). Precisión 50%.
- **Estado:** VIGENTE (aprendizaje aplicado).

## D-20260915-01 — Adoptar scoring v7 con penalizaciones asimétricas

- **Fecha:** 2026-09-15
- **Decisor:** YANG
- **Contexto:** los scoring previos no distinguían bien entre alto riesgo y baja calidad.
- **Decisión:** penalizaciones más fuertes que bonificaciones. Kill switches para mint/freeze authority no revoked.
- **Alternativas consideradas:** scoring lineal simple (descartado: no captura asimetría).
- **Consecuencias:** mejor discriminación entre candidatos.
- **Estado:** VIGENTE.

## D-20260923-01 — Auditar el trust scheduler

- **Fecha:** 2026-09-23
- **Decisor:** YANG
- **Contexto:** trust updates mostraban `price_change_pct: 0.0` siempre.
- **Decisión:** auditar el código del script 98 completo.
- **Alternativas consideradas:** aceptar los trust updates como válidos (descartado: contradice Regla de Oro 2).
- **Consecuencias:** se identifica el bug de baseline (`prev_price = current_price`). Fix planificado.
- **Estado:** VIGENTE.

## D-20260924-01 — Adoptar arquitectura serverless (GitHub Actions)

- **Fecha:** 2026-09-24
- **Decisor:** Dirección
- **Contexto:** dependencia de laptop local impedía 24/7 real y portabilidad.
- **Decisión:** migrar el proyecto a GitHub Actions con cron triggers, zero-local-footprint.
- **Alternativas consideradas:** Windows Task Scheduler local (descartado: dependencia de laptop); cron-job.org (descartado: no permite commit de estado).
- **Consecuencias:** bot 24/7 sin hardware local; estado versionado en repo.
- **Estado:** VIGENTE (en implementación).

## D-20260924-02 — Repo GitHub público con `.gitignore` + secrets

- **Fecha:** 2026-09-24
- **Decisor:** Dirección
- **Contexto:** repo público da minutos ilimitados en Actions y auditoría abierta.
- **Decisión:** repo público. Credenciales viven en GitHub Secrets, nunca en código.
- **Alternativas consideradas:** repo privado (descartado: 2000 min/mes limita operación 24/7).
- **Consecuencias:** minutos ilimitados; obliga a `.gitignore` estricto y pre-commit hook.
- **Estado:** VIGENTE.

## D-20260924-03 — Adoptar "un archivo por mensaje" como protocolo

- **Fecha:** 2026-09-24
- **Decisor:** YANG
- **Contexto:** mensajes con múltiples archivos grandes se truncan en el canal YANG↔YIN.
- **Decisión:** cada archivo se emite en su propio mensaje, sin narrativa alrededor.
- **Alternativas consideradas:** comprimir varios archivos por mensaje (descartado: pérdida de contenido).
- **Consecuencias:** más mensajes, cero truncamiento.
- **Estado:** VIGENTE.

## D-20260924-04 — Adoptar base64 para evidencia no-retypeable

- **Fecha:** 2026-09-24
- **Decisor:** YANG
- **Contexto:** hashes reportados en Ciclos 16.2 y 16.4 tenían patrones repetidos (fabricados).
- **Decisión:** toda evidencia de contenido se transmite en base64 byte-exacto.
- **Alternativas consideradas:** hashes SHA-256 (descartado: se pueden fabricar); copia en texto plano (descartado: reformateable).
- **Consecuencias:** evidencia verificable; imposible fabricar.
- **Estado:** VIGENTE.

## D-20260924-05 — Reformular los fines: 3 universos de activos

- **Fecha:** 2026-09-24
- **Decisor:** Dirección + YANG
- **Contexto:** los fines originales eran binarios (vivos vs. pre-lanzamiento). Faltaba taxonomía.
- **Decisión:** 3 universos — A (maduros: BTC, ETH, SOL), B (en circulación con narrativa: UNI, ICP, APT), C (pre-lanzamiento: LIBRA, TGEs futuras).
- **Alternativas consideradas:** mantener binario (descartado: no distingue señales por universo).
- **Consecuencias:** scoring y fuentes se diferencian por universo.
- **Estado:** VIGENTE.

## D-20260924-06 — Adoptar Camino A (máximo beneficio inmediato)

- **Fecha:** 2026-09-24
- **Decisor:** Dirección
- **Contexto:** tres caminos posibles con perfiles de riesgo distintos.
- **Decisión:** Camino A — primero cerebro + Git + fix de baseline, después autonomía serverless.
- **Alternativas consideradas:** Camino B (autonomía primero, score 82%); Camino C (fuentes primero, score 46%).
- **Consecuencias:** elimina riesgo de pérdida total en las primeras 4 horas del plan.
- **Estado:** VIGENTE.

## D-20260924-07 — Crear `99_MASTER_PROMPT.md` como entry point

- **Fecha:** 2026-09-24
- **Decisor:** Dirección + YANG
- **Contexto:** necesidad de un único archivo que resuma el proyecto para cualquier LLM nuevo.
- **Decisión:** crear `99_MASTER_PROMPT.md` en `El cerebro de dios\`. Índice del cerebro + contexto + instrucciones de uso.
- **Alternativas consideradas:** solo carpeta del cerebro (descartado: requiere leer 18 archivos); solo prompt externo (descartado: se desincroniza).
- **Consecuencias:** cualquier LLM nuevo entiende el proyecto en 1 lectura.
- **Estado:** VIGENTE (se implementa en Ciclo 17.11).

## D-20260924-08 — Cerebro documental primero, master prompt después

- **Fecha:** 2026-09-24
- **Decisor:** YANG
- **Contexto:** el master prompt es un índice del cerebro. Si el cerebro está incompleto, el master prompt también.
- **Decisión:** terminar los 18 archivos del cerebro antes de emitir el master prompt.
- **Alternativas consideradas:** invertir el orden (descartado: master prompt sería un índice de contenido inexistente).
- **Consecuencias:** orden de construcción: cerebro → master prompt → Git → serverless.
- **Estado:** VIGENTE.

---

## Decisiones pendientes

| # | Decisión pendiente | Responsable | Bloquea |
|---|---|---|---|
| 1 | Shadow mode canónico: ¿v5 o v4? | Dirección | Consolidación (18.6) |
| 2 | Umbral de ajuste de pesos del scoring | YANG + Dirección | Fase 4 |
| 3 | Protocolo de integración de fuentes académicas | YANG | Fase 3 |
| 4 | Manejo de strays fuera del proyecto | Dirección | Fase 1 |

## Cómo agregar una decisión nueva

1. YANG redacta la entrada con formato D-YYYYMMDD-NN.
2. Se agrega al final del archivo (nunca en el medio).
3. Se commitea al repo con mensaje: `decision: <título corto>`.
4. Si revierte una decisión anterior, la nueva entrada indica "REVERSIÓN DE D-YYYYMMDD-NN".

## VER TAMBIÉN

- [00_NUCLEO.md](00_NUCLEO.md) — fines del proyecto
- [11_ROADMAP.md](11_ROADMAP.md) — fases y ciclos
- [12_TROUBLESHOOTING.md](12_TROUBLESHOOTING.md) — errores conocidos
- [14_METRICAS.md](14_METRICAS.md) — precisión medida

## Changelog

- 2026-09-24 — v1.0 — Creación inicial con 8 decisiones históricas + 4 pendientes (YANG, Ciclo 17.8.A)