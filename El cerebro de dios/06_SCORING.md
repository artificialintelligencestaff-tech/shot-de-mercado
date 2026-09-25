---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Scoring — Sistema de Puntuación y Confianza

Este archivo define cómo el pipeline convierte señales crudas en un score numérico, y cómo ese score se traduce en confianza declarada. Es el corazón del sistema de predicción.

## 1. Filosofía del scoring

El scoring **no busca certeza**. Busca **acumulación de señales independientes** que en conjunto indiquen probabilidad >50% de aceleración vertical.

- **Bonificaciones:** señales que sugieren movimiento alcista.
- **Penalizaciones:** señales que sugieren riesgo, manipulación o movimiento bajista.
- **Kill switches:** penalizaciones tan graves que anulan cualquier bonificación.

**Regla asimétrica:** las penalizaciones son más fuertes que las bonificaciones. Es preferible perder una oportunidad que emitir un falso positivo.

## 2. Scoring v7 — Fórmula vigente

### 2.1 Bonificaciones (máximo acumulable: +100)

| Señal | Puntos | Fuente |
|---|---|---|
| Whale entry (>=50 SOL) | +20 | Helius RPC |
| MCap en SOL (>=100) | +15 | Dexscreener |
| Age sweet spot (5-60 min) | +10 | Timestamp emisión |
| KOL accumulating signal | +30 | MadeOnSol |
| Dexscreener Boosted + priceChange > 0 | +15 | Dexscreener |
| Liquidez > $20,000 | +10 | Dexscreener |

### 2.2 Penalizaciones (sin límite acumulable)

| Señal | Puntos | Fuente |
|---|---|---|
| KOL signal distributing | -40 | MadeOnSol |
| Early buyer exit > 50% | -30 | Helius RPC |
| Deployer success rate < 5% | -30 | MadeOnSol |
| Deployer total > 100 tokens | -20 | MadeOnSol |
| Twitter reuse handle ajeno | -25 | Social scraping |
| Precio cambio 24h < -20% | -20 | Dexscreener |
| Liquidez < $10,000 | -15 | Dexscreener |
| Liquidez < $1,000 | -25 | Dexscreener |
| Price stale > 600s | -20 | Timestamp |
| Mint no revoked | -50 | Helius RPC (kill switch) |
| Freeze no revoked | -50 | Helius RPC (kill switch) |

### 2.3 Kill switches

Dos señales anulan la alerta independientemente del score acumulado:

1. **Mint authority no revoked:** el deployer puede emitir más tokens en cualquier momento. Riesgo de dilución infinita.
2. **Freeze authority no revoked:** el deployer puede congelar wallets. Riesgo de bloqueo de fondos.

Si cualquiera de las dos está activa, el score se marca como `KILLED` y no se emite alerta.

## 3. Cálculo del score final

```
score_final = max(0, min(100,
    sum(bonificaciones) - sum(penalizaciones)
))
```

Con kill switches: `score_final = 0` si mint o freeze no están revoked.

## 4. Cálculo de confianza declarada

```
confidence_pct = min(95, score_final * 0.9 + whale_bonus + kol_bonus + trending_bonus)
```

Donde:
- `whale_bonus` = 5 si whale entry >= 100 SOL, sino 0.
- `kol_bonus` = 10 si KOL accumulating, sino 0.
- `trending_bonus` = 5 si trending en three.ws, sino 0.

## 5. Niveles de confianza

| Nivel | Confianza | Categoría | Acción |
|---|---|---|---|
| NIVEL 1 | 50-59% | MODERADA | Alerta informativa |
| NIVEL 2 | 60-74% | ALTA | Alerta operativa |
| NIVEL 3 | 75-89% | MUY ALTA | Alerta prioritaria |
| NIVEL 4 | 90%+ | EXCEPCIONAL | Alerta inmediata |

**Regla operativa:** cualquier activo con confianza >= 50% se notifica. No se espera acumulación de muestra.

## 6. Trust update — reglas de actualización

A t+1h, t+6h, t+24h desde la emisión, se consulta el precio actual y se calcula `price_change_pct`.

| Cambio de precio | Ajuste de confianza | Veredicto de stage |
|---|---|---|
| >= +20% | +15 puntos (cap 95) | ACIERTO |
| -20% a +20% | Sin cambio | NEUTRAL |
| -20% a -50% | -25 puntos | FALLO |
| <= -50% | Confianza = 0 | FALSO POSITIVO |

**Regla t+24h:** en este stage se fija el veredicto final de la alerta:
- **ACIERTO:** +20% o más.
- **NEUTRAL:** -20% a +20%.
- **FALLO:** -50% a -20%.
- **FALSO POSITIVO:** -50% o menos.

## 7. Historial de versiones del scoring

| Versión | Cambio principal | Fecha | Estado |
|---|---|---|---|
| v1-v3 | Scoring exploratorio | pre-septiembre 2026 | ARCHIVADO |
| v4 | Introducción de whale entry | septiembre 2026 | ARCHIVADO |
| v5 | Añadido KOL tracking | septiembre 2026 | ARCHIVADO |
| v6 | Kill switches (mint, freeze) | septiembre 2026 | ARCHIVADO |
| **v7** | **Penalizaciones asimétricas + bonus diferenciados** | **actual** | **ACTIVO** |
| v8 | (pendiente) — integración de fuentes académicas + sociales | Fase 3 | PLANIFICADO |
| v9 | (pendiente) — calibración por backtesting | Fase 4 | PLANIFICADO |

## 8. Limitaciones conocidas del v7

1. **Solo 2 alertas reales medidas** (SI y OURA). Muestra insuficiente para ajuste de pesos.
2. **No incluye señales de order flow** (funding rates, open interest).
3. **No pondera por tipo de activo** (memecoin vs utility vs NFT).
4. **No integra sentimiento social medido** (solo KOL tracking binario).
5. **Bug de baseline en trust update** — ver `12_TROUBLESHOOTING.md`.

Estas limitaciones se abordan en v8 y v9.

## 9. Cómo se ajustan los pesos

**Regla actual:** no se ajustan pesos con n < 10 alertas cerradas.

**Cuando n >= 10:**
1. Calcular precisión real (aciertos / total).
2. Si precisión < 50%, revisar bonificaciones más frecuentes en falsos positivos.
3. Si precisión > 70%, reducir penalizaciones ligeramente para capturar más oportunidades.
4. Ajuste máximo permitido por iteración: ±20% del valor original.
5. Registrar el ajuste en `13_DECISIONES.md`.

## 10. Verificación empírica

Actualmente:
- **Alertas emitidas:** 2 (SI, OURA).
- **Resultados:** SI -95.7% (FALSO POSITIVO), OURA +17,178% (ACIERTO).
- **Precisión:** 50% (1 de 2).
- **Muestra suficiente:** NO (se requieren 10+).

Nota: aunque la muestra es insuficiente, ambos resultados son informativos: el sistema captura el espectro completo de riesgo (alto riesgo y alto potencial).

## VER TAMBIÉN

- [05_FUENTES.md](05_FUENTES.md) — fuentes que alimentan cada señal
- [07_TRUST_UPDATE.md](07_TRUST_UPDATE.md) — reglas de trust update en detalle
- [09_ALERTAS.md](09_ALERTAS.md) — cómo se materializa el score en una alerta
- [12_TROUBLESHOOTING.md](12_TROUBLESHOOTING.md) — bug de baseline conocido
- [14_METRICAS.md](14_METRICAS.md) — precisión medida y evolución

## Changelog

- 2026-09-24 — v1.0 — Creación inicial con scoring v7 documentado (YANG, Ciclo 17.5.B)