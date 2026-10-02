---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: BORRADOR (D-014-R, Fase 12 MVP)
last_updated: 2026-10-02
version: 0.1
---

# 32 — Scorer de tokens jóvenes (< 60 min)

Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente.

- **Datos:** `02_Analisis/diagnostics/young_watch_analysis.json`. Son 50 snapshots de `_watch_{a,b}.json`
  (historial de git, 01/10 22:33 → 02/10 02:32 UTC) [V].
- **Código:** `lib_scoring_young.py` (aislado, no integrado), `young_watch_analysis.py` y sus tests.

**Veredicto anticipado.** Hoy no se puede saber si estas features discriminan: no hay ni un outcome de tokens
jóvenes, salvo Nike (−99,8 %). Lo que sí se puede afirmar con los datos:

1. Solo 5 de las 9 señales existen para este universo.
2. Las ≥ 3 activas son casi siempre el mismo trío de flujo.
3. El filtro de $20K deja afuera al 95,6 % de los lanzamientos.

El MVP vale como **experimento en sombra bien instrumentado**, no como scorer. Si el registro en sombra no entra,
mi recomendación es **no seguir**.

## 1. Features

| Señal (lib_early_signals) | Filas del top con edad < 60 min en que se activó (n = 748) | ¿Entra? | Por qué |
|---|---|---|---|
| `volume_acceleration` | 263 | Sí | Requiere h1 > m5: no existe antes de los ~5 min. |
| `liquidity_inflow` | 195 | Sí | Solo hay datos si el par tiene liquidez > 0, que es el 4,4 % de la población. |
| `buy_pressure_shift` | 96 | Sí | |
| `quiet_accumulation` | 7 | Sí | Rara; es la única "previa al precio" por diseño. |
| `holder_accumulation` | 6 | Sí | Hoy RugCheck solo se consulta para tokens cerca del umbral de v7.2.1. Sin cambiar eso, casi no aporta. |
| `social_velocity` | **0** | No | script_115 solo sigue tokens de `_accumulated` con score ≥ 40, nunca lanzamientos en vivo. Es 0 por construcción. |
| `orderbook_imbalance`, `funding_squeeze`, `clmm_imbalance` | 0 | No | No existen para un pool pump.fun / CPMM. |
| `fear_greed_extreme` | 0 | No | Es el mismo valor para todos los tokens del momento, así que no separa uno de otro. |

**Correlación** [V]. Las 4 primeras salen del **mismo snapshot de DexScreener**. De los 16 mints con ≥ 3 señales,
14 activaron exactamente {volumen, compras, liquidez} y 2 cambiaron liquidez por `quiet_accumulation`. "≥ 3
señales" es en la práctica "se activó el trío de flujo", no tres evidencias independientes.

**Filtros estructurales** (solo datos que el sistema ya tiene):
- liquidez > $20K;
- kill switch de script_82 (edad < 5 min con cambio 24 h > 10.000 %);
- RugCheck: mint authority o freeze authority activa, top-10 > 50 % [H], holders < 50 [H], creador > 10 % del
  supply [H];
- PumpPortal: compra inicial del creador (`initialBuy`) > 10 % del supply [H].

## 2. Umbral

- **Regla A (la que se evalúa).** Es la de la directiva: ≥ 3 señales elegibles activas (s > 0) + liquidez > $20K +
  ningún filtro. En el score: 20 × señales activas, umbral 60.
- **Frecuencia esperada** [V sobre el top]: 14 mints en 4 h con ≥ 3 señales y liquidez > $20K, unos 3,5 por hora,
  ~80 por día. Llegar a n ≥ 20 primarias toma ~6–10 h de sombra [I], mucho menos que las 48–72 h del plazo.
- **Variantes que se registran al lado** (calcularlas es gratis), para elegir walk-forward en vez de a ojo:
  - **B:** ≥ 3 señales "fuertes" (s ≥ 0,5). Hoy una señal con s = 0,05 cuenta igual que una con s = 1.
  - **C:** suma de puntos de lib_early_signals ≥ 4.
  - **Control:** una muestra al azar de tokens jóvenes que no disparan, ~10 %.
- **No propongo otro umbral sin outcome.** Elegirlo hoy sería decorativo.

## 3. Criterios

| | Regla | Comentario |
|---|---|---|
| Aceptación | n ≥ 20 primarias resueltas **y** tasa ≥ 40 % **y** IC90 inferior > tasa del control | Con n = 20, el IC90 de Wilson de 8/20 es [0,24; 0,58]. Sin la comparación con el control, 40 % puede ser solo la volatilidad de un token de 15 minutos. |
| Descarte | n ≥ 20 y tasa < 30 %, **o** IC90 superior < tasa del control | |
| Zona gris | 30–40 %, o sin diferencia con el control | Seguir hasta n = 40. Si persiste, descartar. |
| Métrica secundaria (informar, no decide) | % de aciertos que después caen ≤ −99 % (H-84) | La primaria cuenta como acierto el +20 % aunque el token rugee en la hora siguiente. |

La primaria es la de siempre: +20 % antes de −30 % en 48 h, desde el precio de la alerta, con velas de 15 min de
GeckoTerminal (`evaluate_outcome`, misma función que `monitor_shadow`). [P] Hay que verificar que GeckoTerminal
tenga velas de los pools jóvenes.

## 4. Relación con script_116: **lo envuelve, no lo modifica**

script_116 ya calcula, en cada poll, las señales de cada token vigilado. La integración (próximo paso, **no hecha**)
es una llamada a `score_young` dentro de `evaluate()` para edad < 60 min. Esa llamada solo **escribe un registro en
sombra**: no emite y no toca el score v7.2.1 ni la ruta de Telegram.

Hoy falta el dato base: `_watch_*.json` guarda solo el **top-15** de cada poll, así que no sirve para walk-forward.
El registro en sombra necesita una línea por token y poll con las señales crudas, el `dx` resumido, el score, la
decisión A/B/C y si cae en el control. El archivo sería `02_Analisis/early/young_shadow_<inst>.jsonl`, uno por
instancia, sin conflictos. Volumen estimado: ~400 tokens por poll × 30 polls/h por instancia. Hay que muestrear:
loguear solo los que tienen ≥ 1 señal o caen en el control [I].

## 5. Plan de test

1. **Unitarios** (hechos, 7): alcance por edad, filtros, kill switches, elegibilidad, variantes, determinismo. Más 3
   tests del análisis de cobertura.
2. **Paridad:** el registro en sombra guarda las entradas, y `score_young` re-ejecutado offline sobre esas entradas
   tiene que dar lo mismo que en vivo (test sobre el JSONL).
3. **Walk-forward:** outcome de todos los A/B/C positivos y del control. Folds cronológicos de 12 h: el umbral se
   elige con el fold k y se mide en el k+1. Nunca se mira el fold de evaluación.

## 6. Riesgos

- **Liquidez > $20K.** El 95,6 % de los tokens jóvenes tiene liquidez 0 en DexScreener: están en la curva de
  bonding de pump.fun. Los 86 que pasan $20K lo hacen al **minuto ~1** (mediana). Probablemente no son
  lanzamientos de la curva sino tokens que nacen en un AMM o migran al instante [I; falta ver `dexId`]. El filtro
  no "selecciona los que crecen": **cambia de población**.
- **Señales redundantes** (§1). El umbral "3 de 5" no da la independencia que sugiere.
- **Sesgo del análisis.** El top-15 está ordenado por score: la distribución de §1 no es la población.
- **Primaria vs. H-84.** Un experimento que "acepta" puede estar aceptando pumps que rugean en la hora siguiente.
  Por eso se informa la métrica secundaria.
- **Costo de outcomes.** GeckoTerminal permite ~550 velas por hora (6,5 s por llamada). A + B + C + control a ~100
  por día entra.

## 7. Preguntas abiertas (para YANG / Dirección)

1. ¿Se aprueba el registro en sombra dentro de script_116 (§4)? Sin eso no hay walk-forward posible.
2. ¿El control aleatorio (~10 %) entra en el presupuesto de GeckoTerminal, o alcanza con medir solo los positivos?
3. ¿Se mantiene el filtro de $20K sabiendo que deja afuera los tokens de la curva de bonding? La alternativa es
   abrir la población a liquidez 0 y usar volumen y compras como único filtro de actividad.
4. ¿Ampliar RugCheck a todos los tokens jóvenes con ≥ 2 señales? `holder_accumulation` y los kill switches de
   holders dependen de eso. Hoy se consulta solo cerca del umbral de v7.2.1.
5. ¿Agregar los lanzamientos en vivo al colector de menciones (script_115)? Es la única forma de que
   `social_velocity` exista para este universo. Hoy queda excluida.
