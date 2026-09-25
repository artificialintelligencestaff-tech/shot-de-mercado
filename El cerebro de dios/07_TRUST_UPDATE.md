---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Trust Update — Actualización de Confianza

Este archivo documenta el mecanismo de trust update: cómo una alerta emitida se actualiza en los checkpoints t+1h, t+6h, t+24h, y cómo esos updates modifican la confianza declarada y producen el veredicto final.

## 1. Qué es un trust update

Cuando se emite una alerta (ver `09_ALERTAS.md`), el activo entra en estado `active_tracking`. Desde ese momento, el sistema debe:

1. Consultar el precio real en checkpoints definidos.
2. Calcular el cambio porcentual desde la emisión (o desde el último checkpoint).
3. Ajustar la confianza declarada según reglas fijas.
4. Emitir notificación vía Telegram si el cambio es significativo (>= 10 puntos de confianza).
5. Persistir el update en `_all_alerts.json` y en `trust_<mint>.json`.
6. Al llegar a t+24h, fijar el veredicto final.

## 2. Checkpoints (stages)

| Stage | Threshold | Propósito |
|---|---|---|
| t+1h | 1.0 hora desde emisión | Detección temprana de rug pull o aceleración |
| t+6h | 6.0 horas desde emisión | Confirmación de tendencia |
| t+24h | 24.0 horas desde emisión | Veredicto final de la alerta |

**Regla:** cada checkpoint se ejecuta **una sola vez**. Una vez registrado, no se repite.

## 3. Reglas de veredicto

Para cada stage, se calcula `price_change_pct` y se aplica:

| Cambio de precio | Ajuste de confianza | Veredicto de stage |
|---|---|---|
| >= +20% | +15 puntos (cap 95) | ACIERTO |
| -20% a +20% | Sin cambio | NEUTRAL |
| -50% a -20% | -25 puntos | FALLO |
| <= -50% | Confianza = 0 | FALSO POSITIVO |

**Nota:** si el cambio cae entre -20% y +20%, no se modifica la confianza. Los rangos son asimétricos: el sistema penaliza más de lo que bonifica.

## 4. Verdad final (t+24h)

Al llegar a t+24h se fija el veredicto final de la alerta:

| Veredicto final | Criterio |
|---|---|
| ACIERTO | +20% o más |
| NEUTRAL | -20% a +20% |
| FALLO | -50% a -20% |
| FALSO POSITIVO | -50% o menos |

Este veredicto es inmutable. Se registra en `_all_alerts.json` con `verdict_final` y `closed_at`.

## 5. Estructura de `trust_<mint>.json`

Cada alerta tiene su archivo de trust asociado:

```json
[
  {
    "stage": "t+1h",
    "timestamp": "2026-09-24_024829",
    "price": 2.072e-06,
    "price_change_pct": 0.0,
    "confidence_adjustment": 0,
    "new_confidence": 56,
    "stage_verdict": "NEUTRAL"
  },
  {
    "stage": "t+6h",
    "timestamp": "...",
    "price": ...,
    "price_change_pct": ...,
    "confidence_adjustment": ...,
    "new_confidence": ...,
    "stage_verdict": "..."
  }
]
```

**Ubicación:** `02_Analisis\alerts\trust_<mint>.json`.

## 6. Estructura de `_all_alerts.json` (con trust embebido)

Cada alerta en `_all_alerts.json` incluye su historial de trust updates:

```json
{
  "timestamp": "2026-09-24_004501",
  "mint": "DegeC37wePGYLFD2RXuc2TNEFK2qCGJsMDxHCpSppump",
  "symbol": "SI",
  "score": 55,
  "confidence": 56,
  "initial_price": null,
  "status": "active_tracking",
  "trust_updates": [
    {
      "stage": "t+1h",
      "timestamp": "2026-09-24_024829",
      "price": 2.072e-06,
      "price_change_pct": 0.0,
      "confidence_adjustment": 0,
      "new_confidence": 56,
      "stage_verdict": "NEUTRAL"
    }
  ],
  "verdict_final": null
}
```

**Campo `initial_price`:** crítico para el cálculo correcto. Ver bug en sección 8.

## 7. Flujo de ejecución del trust scheduler

```
INICIO
  ↓
Leer _all_alerts.json
  ↓
Para cada alerta con status = active_tracking:
  ↓
  Calcular age_hours = (now - emit_time) / 3600
  ↓
  Para stage en [t+1h, t+6h, t+24h]:
    ↓
    Si stage no completado Y age_hours >= threshold:
      ↓
      Consultar precio actual (Dexscreener)
      ↓
      Determinar prev_price:
        - Si initial_price existe: prev_price = initial_price
        - Si trust_updates no vacío: prev_price = último price
        - Fallback: prev_price = current_price (BUG — ver sección 8)
      ↓
      Calcular price_change_pct
      ↓
      Aplicar reglas de veredicto
      ↓
      Actualizar confidence
      ↓
      Escribir trust_<mint>.json
      ↓
      Si cambio >= 10 puntos → notificar Telegram
      ↓
      Si stage == t+24h → fijar verdict_final
  ↓
Guardar _all_alerts.json
  ↓
Escribir _scheduler_log.json
  ↓
FIN
```

## 8. Bug conocido del trust scheduler (v1)

**Síntoma:** `price_change_pct: 0.0` en todas las alertas.

**Causa raíz:** en la primera pasada, `trust_updates` está vacío, y el código hace:

```python
prev_price = current_price  # Default if first check
```

Esto compara el precio actual contra sí mismo. El cambio es 0% por construcción.

**Impacto:** los trust updates nunca aplican los ajustes reales. La confianza no cambia. Los veredictos quedan en NEUTRAL siempre.

**Fix propuesto (3 partes):**

### Parte 1 — Persistir `initial_price` al emitir alerta

En `script_97_emit_alerts.py`:

```python
alert = {
    "timestamp": now.strftime("%Y-%m-%d_%H%M%S"),
    "mint": mint,
    "symbol": symbol,
    "score": score_final,
    "confidence": confidence_pct,
    "initial_price": current_price_at_emission,  # NUEVO
    "status": "active_tracking",
    "trust_updates": []
}
```

Si `current_price_at_emission` es None → no emitir la alerta (evita baseline rota).

### Parte 2 — Corregir el cálculo en `script_98_trust_scheduler.py`

**Antes (bug):**
```python
prev_price = current_price  # Default if first check
if trust_updates:
    prev_price = trust_updates[-1].get("price", current_price)
```

**Después (corregido):**
```python
if alert.get("initial_price") and alert["initial_price"] > 0:
    prev_price = alert["initial_price"]
elif trust_updates:
    prev_price = trust_updates[-1].get("price", current_price)
else:
    print(f"[WARN] {symbol} sin initial_price ni historial.")
    alert["initial_price"] = current_price
    prev_price = current_price
```

### Parte 3 — Backfill retroactivo

Para SI y OURA (alertas legacy), añadir `initial_price: null` y `note: "legacy alert, no baseline"`. Aplicar el fix solo a nuevas alertas.

## 9. Estado actual del trust scheduler

| Aspecto | Estado |
|---|---|
| Consulta fuentes externas | OK — Dexscreener real |
| Aplica reglas de veredicto | OK — lógica correcta |
| Persiste archivos | OK — escribe `trust_<mint>.json` |
| Cálculo de baseline | BUG — ver sección 8 |
| Notificaciones Telegram | OK — dispara cuando corresponde |

**Conclusión:** no es un stub. Es un script funcional con un bug de baseline puntual.

## 10. Plan de fix (Ciclo 17.10)

| Paso | Acción | Archivo |
|---|---|---|
| 1 | Añadir `initial_price` al emitir alerta | `script_97_emit_alerts.py` |
| 2 | Corregir baseline en trust scheduler | `script_98_trust_scheduler.py` |
| 3 | Backfill legacy en `_all_alerts.json` | manual |
| 4 | Ejecutar y verificar `price_change_pct != 0.0` | test |
| 5 | Registrar fix en `13_DECISIONES.md` | documentación |

## VER TAMBIÉN

- [06_SCORING.md](06_SCORING.md) — scoring y confianza base
- [03_FLUJOS.md](03_FLUJOS.md) — workflow Trust Update
- [09_ALERTAS.md](09_ALERTAS.md) — formato de alerta
- [12_TROUBLESHOOTING.md](12_TROUBLESHOOTING.md) — bug de baseline documentado
- [13_DECISIONES.md](13_DECISIONES.md) — bitácora del fix

## Changelog

- 2026-09-24 — v1.0 — Creación inicial + bug de baseline documentado (YANG, Ciclo 17.6.A)