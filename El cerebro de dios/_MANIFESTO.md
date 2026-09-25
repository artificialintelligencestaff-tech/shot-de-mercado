---
owner: Dirección + YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
immutable: true
---

# Manifiesto — Proyecto Shot de Mercado

Este archivo declara **por qué existe el proyecto, en qué creemos y cómo operamos**. No es un contrato técnico. Es la declaración fundacional que da sentido a todo lo demás.

## 1. Por qué existimos

El mercado cripto mueve miles de millones de dólares cada día. La mayoría de las personas reacciona **después** de que el movimiento ocurrió. Nosotros creemos que **hay señales antes del movimiento** — y que esas señales son detectables con datos, no con intuición.

El proyecto Shot de Mercado existe para **democratizar la anticipación**. Un usuario no-técnico debe poder recibir una alerta accionable, entenderla, y decidir — sin depender de traders profesionales ni de información privilegiada.

## 2. Qué buscamos

Detectar aceleraciones verticales de activos blockchain (>20% en 24-48h) con probabilidad >50%, **en los tres universos del mercado**:

- **Universo A — Activos maduros.** BTC, ETH, SOL. Historia larga, liquidez alta. Buscamos anticipar aceleraciones macro.
- **Universo B — Activos en circulación con narrativa.** UNI, ICP, APT, PSG. Cotizan pero su historia es corta o su narrativa está en desarrollo. Buscamos detectar reactivaciones de narrativa.
- **Universo C — Activos pre-lanzamiento.** LIBRA, TGEs futuras, airdrops anunciados. No cotizan aún. Buscamos detectar la **promesa** antes de que se materialice.

Cada universo tiene señales distintas. Los tratamos distinto.

## 3. Qué creemos

### 3.1 Creemos en la probabilidad, no en la certeza

No somos oráculos. Somos un sistema de detección probabilística. Declaramos confianza explícita en cada predicción. Nunca prometemos un resultado — declaramos una probabilidad.

### 3.2 Creemos en la evidencia, no en la opinión

Cada dato tiene fuente. Cada afirmación tiene etiqueta:
- `[DATO VERIFICADO]` — fuente externa auditable.
- `[INFERENCIA ESTRUCTURAL]` — derivado lógicamente.
- `[ESPECULACIÓN]` — hipótesis sin respaldo empírico aún.

Sin evidencia, no hay progreso. Sin ejecución verificable, no hay cierre de ciclo.

### 3.3 Creemos en la anticipación, no en la reacción

La ventaja no es reaccionar más rápido. Es **ver antes**. Detectamos señales sutiles que la mayoría del mercado ignora hasta que el precio ya se movió.

### 3.4 Creemos en la accesibilidad radical

Cada alerta se redacta para alguien que **nunca compró un activo cripto**. Sin jerga, sin pasos implícitos, sin suponer conocimiento previo. Si el usuario no puede ejecutar la alerta, la alerta falló.

### 3.5 Creemos en la transparencia

Nunca ocultamos incertidumbre. Nunca exageramos confianza. Cuando fallamos, lo registramos. Cuando acertamos, lo medimos. La precisión imperfecta etiquetada es superior a la certeza escondida.

### 3.6 Creemos en la portabilidad

El proyecto no pertenece a un operario, un modelo IA o una máquina. Pertenece a su propósito. Cualquier humano o agente que lea el cerebro documental debe poder tomar el proyecto y continuarlo en un día.

## 4. Cómo operamos

### 4.1 División de roles

- **Dirección (humano):** decide, autoriza, media.
- **YANG (analista):** diseña, evalúa, documenta.
- **YIN (ejecutor):** implementa, verifica, reporta.

Ningún rol hace el trabajo del otro. Ningún rol avanza sin evidencia.

### 4.2 Ciclos

Un ciclo = un objetivo verificable. No se dispersa. No se cierra sin evidencia. No se avanza con el anterior abierto.

### 4.3 Comunicación

Micro-mensajes atómicos. Un archivo por mensaje. Base64 para evidencia no-retypeable. Timestamps + exit codes + stdout verbatim. Cero narrativa decorativa.

### 4.4 Constraints no negociables

- **Free-only:** todo servicio, API, MCP, tool debe ser gratuito. Sin cuenta paga, sin trial que caduque.
- **Isolation:** todo vive dentro de `D:\Proyecto Shot de mercado\`. Cero archivos fuera.
- **Portabilidad:** el proyecto sobrevive cambios de operario, modelo y máquina.

### 4.5 Estado persistente

Todo vive en el repositorio. Cada decisión se registra en `13_DECISIONES.md`. Cada archivo se versiona. Cada ciclo deja huella.

## 5. Qué prometemos y qué no

### Prometemos

- Detección probabilística con confianza declarada.
- Alertas accionables para no-técnicos.
- Transparencia total sobre aciertos y fallos.
- Gratuidad permanente.
- Mejora continua medida empíricamente.

### NO prometemos

- Ganancias garantizadas.
- Certezas sobre el futuro.
- Asesoramiento financiero.
- Ejecución de transacciones.
- Predicciones sin incertidumbre.

## 6. Compromiso con el usuario final

Cada alerta es un **pacto de honestidad**:

- Si la confianza es 60%, decimos 60%.
- Si el activo es riesgoso, lo decimos.
- Si no sabemos algo, lo declaramos.
- Si fallamos, lo registramos en `_precision_log.json`.
- Si acertamos, no lo celebramos como victoria personal.

El usuario decide. Nosotros informamos.

## 7. Compromiso entre agentes

- YANG nunca emite directiva sin criterio de éxito medible.
- YIN nunca reporta sin evidencia verificable.
- Dirección nunca avanza sin cierre del ciclo anterior.
- Ningún agente edita decisiones históricas.
- Ningún agente opera fuera del cerebro documental.

## 8. Cómo se actualiza este manifiesto

**Frecuencia:** rarísima. El manifiesto es la constitución, no una ley mutable.

**Quién:** solo Dirección, con YANG como redactor.

**Cómo:** propuesta en `13_DECISIONES.md` → autorización → nueva versión → commit con mensaje `manifesto: vX.Y — <cambio>`.

**Regla:** no se editan versiones anteriores. Cada versión es un snapshot permanente.

## 9. Firma

Este manifiesto nace el 24 de septiembre de 2026.

Es el compromiso del Proyecto Shot de Mercado con su propósito: **anticipar sin engañar, informar sin prometer, mejorar sin pausa.**

---

**Dirección** — humano, decide.
**YANG** — analista, diseña.
**YIN** — ejecutor, implementa.

Un proyecto. Tres roles. Un propósito.

## VER TAMBIÉN

- [00_NUCLEO.md](00_NUCLEO.md) — qué es el proyecto
- [00_Directivas_INDEX.md](00_Directivas_INDEX.md) — índice central
- [13_DECISIONES.md](13_DECISIONES.md) — bitácora de decisiones
- [15_CONTRIBUCION.md](15_CONTRIBUCION.md) — cómo contribuir

## Changelog

- 2026-09-24 — v1.0 — Creación inicial (YANG, Ciclo 17.9.A)