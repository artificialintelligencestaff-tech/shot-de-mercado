---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Núcleo — Propósito Raíz del Proyecto Shot de Mercado

## Qué es este proyecto

Un **bot autónomo de predicción** que detecta aceleraciones verticales en activos blockchain (movimientos ≥20% en ventanas de 24-48h) usando multiplicidad de filtros independientes, y comunica las alertas vía Telegram en formato accionable para usuarios no-técnicos.

## Propósito (por qué existe)

Detectar **antes de que ocurran** los movimientos que la masa social aún no ha visto. La ventaja competitiva del proyecto no es la velocidad de reacción — es la **anticipación basada en señales sutiles** que la mayoría del mercado ignora hasta que el precio ya se movió.

## Principio epistémico

El proyecto **no es un oráculo**. Es un **adivinador probabilístico**. Declara confianza explícita en cada predicción. Etiqueta cada dato con su nivel de verificación:

| Etiqueta | Significado |
|---|---|
| `[DATO VERIFICADO]` | Viene de fuente externa auditable (API, on-chain, documentos públicos) |
| `[INFERENCIA ESTRUCTURAL]` | Derivado lógicamente de datos verificados |
| `[ESPECULACIÓN]` | Hipótesis sin respaldo empírico aún |

## Fines del proyecto

### Fin principal
Predecir aceleraciones verticales con >50% de probabilidad, usando multiplicidad de filtros independientes.

### Fines secundarios
1. **Cobertura dual:** activos ya listados (Escala A) + activos pre-lanzamiento (Escala B).
2. **Transparencia radical:** confianza declarada, nunca certeza escondida.
3. **Autonomía 24/7:** corre en la nube sin depender de hardware local.
4. **Adquisición accesible:** cada alerta incluye paso a paso para no-técnicos.
5. **Aprendizaje continuo:** cada alerta cerrada alimenta la mejora del scoring.
6. **Portabilidad:** cualquier operario nuevo puede tomar el proyecto en 1 día.

## Lo que NO es el proyecto

- ❌ No es asesoramiento financiero.
- ❌ No promete ganancias.
- ❌ No ejecuta transacciones (la decisión es siempre del usuario).
- ❌ No inventa datos (todo dato tiene fuente o etiqueta de especulación).

## Constraint no negociable: FREE-ONLY

Todos los servicios, APIs, MCPs, herramientas y skills que el proyecto use deben ser **gratuitos**. Sin cuenta paga obligatoria, sin billing, sin trial que caduque.

**Razón:** el bot opera 24/7 de forma indefinida. Cualquier dependencia paga rompe el modelo.

## Constraint no negociable: ISOLATION

Todo el proyecto vive dentro de `D:\Proyecto Shot de mercado\`. Cualquier archivo generado, log, cache o artefacto fuera de ese directorio se considera **stray** y debe migrarse o eliminarse.

## Constraint no negociable: PORTABILIDAD

El proyecto debe sobrevivir a:
- Cambio de operario humano.
- Cambio de modelo IA (YIN, YANG u otro).
- Cambio de máquina física.
- Cambio de plataforma de cómputo (local → cloud).

**Herramienta:** este árbol neurocerebral.

## VER TAMBIÉN

- [00_Directivas_INDEX.md](00_Directivas_INDEX.md) — índice central
- [01_HISTORIA.md](01_HISTORIA.md) — cómo llegamos acá
- [02_ARQUITECTURA.md](02_ARQUITECTURA.md) — cómo funciona el sistema
- [SKILLS_skill_entender_proyecto.md](SKILLS_skill_entender_proyecto.md) — entry point para agentes

## Changelog

- 2026-09-24 — v1.0 — Creación inicial (YANG, Ciclo 17.3)