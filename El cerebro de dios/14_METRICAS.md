---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Métricas — Precisión, Cobertura y Performance

Este archivo registra las **métricas medibles** del proyecto: qué se mide, cómo se mide, valores actuales, y evolución esperada.

**Regla:** este archivo se actualiza cada vez que se cierra una alerta (nuevo dato de precisión) o cada 10 alertas cerradas (recalibración de pesos).

## 1. Métricas de predicción

### 1.1 Precisión direccional

**Definición:** porcentaje de alertas cuyo veredicto final es ACIERTO sobre el total de alertas cerradas.

**Fórmula:**
```
precision = aciertos / (aciertos + fallos + falsos_positivos + neutros)
```

**Criterio de ACIERTO:** precio final >= +20% desde emisión.

**Valor actual:**

| Métrica | Valor | Nota |
|---|---|---|
| Alertas emitidas | 2 | SI, OURA |
| Alertas cerradas | 0 | pendientes de fix de trust |
| Aciertos | 1 | OURA (+17,178%) |
| Fallos | 0 | — |
| Falsos positivos | 1 | SI (-95.7%) |
| Neutros | 0 | — |
| **Precisión** | **50%** | n=2, muestra insuficiente |

**Objetivo:** >55% con n>=20 alertas cerradas.

### 1.2 Cobertura por universo

**Definición:** proporción de alertas emitidas por cada universo de activos.

| Universo | Alertas emitidas | % del total |
|---|---|---|
| A — Maduros (BTC, ETH, SOL) | 0 | 0% |
| B — En circulación con narrativa (UNI, ICP, APT) | 2 | 100% |
| C — Pre-lanzamiento (LIBRA, TGEs) | 0 | 0% |

**Objetivo:** cubrir los 3 universos con al menos 3 alertas cada uno.

**Estado:** la cobertura está sesgada al Universo B (memecoins de Solana). Los universos A y C están inactivos.

### 1.3 Lead time

**Definición:** tiempo entre la emisión de la alerta y el pico de precio alcanzado.

**Medición:** timestamp_emisión → timestamp_pico.

**Valor actual:**

| Alerta | Lead time |
|---|---|
| SI | N/A (nunca subió) |
| OURA | ~0.6h (subió inmediatamente) |

**Objetivo:** 12-48h promedio (permite al usuario adquirir antes del pico).

**Observación:** OURA subió tan rápido que el usuario tuvo poco tiempo para adquirir. El proyecto busca anticipar más, no reaccionar.

### 1.4 Magnitud capturada

**Definición:** cuánto del movimiento real capturó la alerta (comparado con la predicción).

| Alerta | Predicción | Real | Error |
|---|---|---|---|
| SI | Sin movimiento esperado | -95.7% | Fallo de dirección |
| OURA | Movimiento alcista | +17,178% | Subestimó 100x |

**Objetivo:** predecir rango, no valor puntual.

### 1.5 Calibración de confianza

**Definición:** ¿una confianza declarada de X% acierta aproximadamente X% de las veces?

**Medición:** agrupar alertas por bucket de confianza (50-60, 60-70, 70-80, 80-90, 90-95) y comparar con precisión real.

**Valor actual:** no medible con n=2.

**Objetivo:** calibración ±10% (ej: alertas con 70% de confianza aciertan entre 60% y 80%).

## 2. Métricas de operación

### 2.1 Uptime

**Definición:** porcentaje del tiempo en que el pipeline corre según cron.

**Valor actual:** n/a (no hay cron aún; scripts se ejecutan manualmente).

**Objetivo:** >99% con GitHub Actions.

### 2.2 Frecuencia de ciclos

| Workflow | Frecuencia objetivo | Frecuencia actual |
|---|---|---|
| Pipeline T+0 | Cada 20 min | Manual |
| Trust update | Cada 20 min | Manual |
| Pre-launch | Cada 6h | Manual |

### 2.3 Tokens procesados

| Etapa | Tokens/ciclo |
|---|---|
| Capturados (PumpPortal) | ~400 |
| Pasan Quality Gate | ~30 |
| Validados con scoring | 9 |
| En WATCH REAL | 2 |
| Alertas emitidas | 0-2 |

### 2.4 Tasa de alertas

**Definición:** alertas emitidas / tokens procesados.

**Valor actual:** 2 / ~400 = 0.5%.

**Análisis:** ratio muy bajo. Puede indicar umbral demasiado alto o filtros demasiado estrictos. Evaluar en Fase 4.

## 3. Métricas de sistema

### 3.1 Latencia

| Operación | Latencia objetivo | Latencia actual |
|---|---|---|
| Captura T+0 | <5 seg | ~1 seg (WS) |
| Scoring | <10 seg | ~3 seg |
| Emisión Telegram | <2 seg | ~1 seg |
| Trust update | <30 seg | no medido |

### 3.2 Errores por ciclo

| Tipo de error | Frecuencia esperada |
|---|---|
| API failure (429, 500) | <5% |
| Timeout | <2% |
| Write failure | <1% |
| Telegram send failure | <1% |

### 3.3 Costo operativo

**Constraint:** free-only.

| Componente | Costo |
|---|---|
| GitHub Actions (público) | $0 (ilimitado) |
| GitHub repo (público) | $0 |
| Telegram Bot API | $0 |
| CoinGecko Public | $0 |
| Dexscreener | $0 |
| PumpPortal WS | $0 |
| MadeOnSol | $0 |
| Helius RPC | $0 |
| **Total mensual** | **$0** |

## 4. Métricas de calidad

### 4.1 Cobertura de fuentes

**Definición:** cuántas fuentes VIABLE del catálogo están efectivamente integradas al pipeline.

| Categoría | Total fuentes | Integradas | % |
|---|---|---|---|
| Mercado (precios) | 10 | 4 | 40% |
| On-chain | 7 | 3 | 43% |
| Social | 6 | 1 | 17% |
| Noticias | 5 | 0 | 0% |
| Pre-launch | 6 | 2 | 33% |
| Académico | 4 | 0 | 0% |
| MCPs | 6 | 0 | 0% |
| **Total** | **44** | **10** | **23%** |

**Objetivo:** >60% en Fase 3.

### 4.2 Cobertura de tests

**Definición:** % de módulos con tests automatizados.

**Valor actual:** 0%.

**Objetivo:** >50% en Fase 5.

### 4.3 Documentación

**Definición:** % del cerebro documental completo.

| Bloque | Archivos | Creados | % |
|---|---|---|---|
| Fundacionales | 3 | 0 | 0% |
| Cerebro (00-15) | 16 | 17 | 106% |
| Skills | 5 | 1 | 20% |
| Master prompt | 1 | 0 | 0% |
| **Total** | **25** | **18** | **72%** |

**Objetivo:** 100% en Fase 0.

## 5. Evolución esperada de la precisión

| Fase | Muestra | Precisión objetivo |
|---|---|---|
| Actual (Fase 0) | 2 | 50% (n insuficiente) |
| Fase 1 | 4 | ~50% |
| Fase 2 | 10 | >50% |
| Fase 3 | 20 | >55% |
| Fase 4 | 40 | >60% |
| Fase 5 | 100 | >65% |

**Nota:** los objetivos son proyecciones. La realidad puede ser mejor o peor. Se recalibra en cada fase.

## 6. Cómo se recopilan las métricas

| Métrica | Fuente |
|---|---|
| Precisión | `_precision_log.json` |
| Alertas emitidas | `_all_alerts.json` |
| Uptime | GitHub Actions logs (futuro) |
| Frecuencia | Cron schedule + logs |
| Tokens procesados | `_accumulated.json` |
| Latencia | Timestamps en logs |
| Costo | Auditoría manual mensual |

## 7. Dashboard conceptual

```
┌─────────────────────────────────────────────────────┐
│  SHOT DE MERCADO — MÉTRICAS AL 2026-09-24           │
├─────────────────────────────────────────────────────┤
│  Precisión:        50% (n=2, muestra insuficiente)  │
│  Alertas emitidas: 2                                │
│  Alertas cerradas: 0                                │
│  Universos cubiertos: 1 de 3 (solo B)               │
│  Fuentes integradas: 10 de 44 (23%)                 │
│  Cerebro completo:  18 de 25 (72%)                  │
│  Costo mensual:     $0                              │
│  Uptime:            n/a (manual)                    │
└─────────────────────────────────────────────────────┘
```

## 8. Próxima actualización

**Cuándo:** al cerrar cada alerta nueva (actualiza precisión), o al completar cada fase (recalibra objetivos).

**Quién:** YANG.

**Cómo:** el script `script_105_update_state.py` (a crear en Fase 2) podrá regenerar este archivo automáticamente desde `_precision_log.json` y `_all_alerts.json`.

## VER TAMBIÉN

- [06_SCORING.md](06_SCORING.md) — cómo se calcula el score
- [09_ALERTAS.md](09_ALERTAS.md) — cómo se emiten y cierran las alertas
- [10_ESTADO_ACTUAL.md](10_ESTADO_ACTUAL.md) — snapshot vivo
- [11_ROADMAP.md](11_ROADMAP.md) — fases y objetivos

## Changelog

- 2026-09-24 — v1.0 — Creación inicial con métricas de predicción, operación y sistema (YANG, Ciclo 17.8.B)