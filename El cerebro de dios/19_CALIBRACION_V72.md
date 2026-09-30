---
owner: Claude Code (implementador) — pendiente decisión de YANG / Dirección
status: DIAGNOSTICO_COMPLETO_RECOMENDACION_PENDIENTE
last_updated: 2026-09-30
version: 1.0
---

# Calibración del scoring v7.2

Script: `04_Config/scripts/calibrate_threshold_v72.py`. Reporte: `02_Analisis/diagnostics/threshold_analysis.json`.
Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente.

## 1. Hipótesis y datos

| | Enunciado | Resultado |
|---|---|---|
| H1 (Dirección) | El umbral 50 quedó desactualizado tras las bonificaciones del v7.2 | **Parcial.** El umbral sí quedó desactualizado, pero **ningún umbral entre 50 y 90** lleva la tasa al objetivo del 5-15% |
| H2 (complementaria) | La inflación viene de tokens de menos de 60 min, donde vol_m5/vol_h1 ≈ 1 por construcción | **Confirmada [V]:** 96 de las 99 ALERTAS (≥70) son tokens de < 60 min con m5/h1 ≥ 0,9 |

- **Conjunto A (v7.2 completo):** 169 detecciones de las 4 corridas de producción del v7.2 (30/09, entre 01:09 y 02:08 UTC). Son las únicas que traen los campos m5/h1 [V].
  - El score se recalcula con `script_82.score_token`, con el reloj fijado a la hora de la detección más 330 s (edad del par medida en ese momento) y sin `_accumulated.json`.
  - **Reproducibilidad: 169/169 exacta** contra el score guardado en producción [V].
- **Conjunto B (legado v7.1):** 10.484 detecciones entre el 23 y el 29/09, sin campos v7.2. Sirven como línea base y para medir resultados.

## 2. Tasa de ALERTA por umbral

| Umbral | v7.2 en producción (n=169) | v7.2 con bonos de aceleración solo desde los 60 min | v7.1 legado (n=10.484) |
|---|---|---|---|
| ≥ 50 | **88,8%** | 29,0% | 3,5% |
| ≥ 60 | 84,0% | 1,8% | 3,5% |
| ≥ 70 | **58,6%** (etiqueta ALERTA de script_82) | 1,8% | 2,9% |
| ≥ 80 | 40,2% | 1,2% | 2,2% |
| ≥ 90 | **29,6%** | 0,6% | 0,4% |

- **Barrido fino (con el gate de 60 min):**

  | Umbral | Tasa |
  |---|---|
  | 50 | 29,0% |
  | 51–54 | 25,4% |
  | 55 | 24,9% |
  | **56–60** | **1,8%** |

  **La distribución es bimodal: no existe umbral que dé entre 5 y 15%.**
- **Por edad** (v7.2, ALERTA ≥ 70):
  - < 5 min: 84/143
  - 5-60 min: 12/21
  - 4-24 h: 1/1
  - > 24 h: 2/4
- **Razones más frecuentes entre las 99 ALERTAS** (varias por token):
  - "Volumen acelerado (5m/1h > 50%)": 96
  - "Trades acelerados": 96
  - "Edge temprano (<60 min)": 96
  - "Volumen bajo": 93
  - "MCap bajo": 89
  - "Liquidez baja": 89
- **Por corrida (≥ 70):**
  - 01:09 → 38/53
  - 01:31 → 17/35
  - 01:49 → 21/35
  - 02:08 → 23/46

**Mecanismo [V]:** en un token de minutos de vida, la ventana h1 contiene solo esos minutos. Por eso m5/h1 ≈ 1 y los bonos "acelerado" (+25 y +20) se disparan siempre. A eso se suman "Edge temprano" (+15), "Buy pressure > 60%" (+25, porque los primeros compradores dominan) y momentum m5/h1 (+20), que también premian la juventud [H para los tres últimos].

## 3. Precisión con resultados reales (legado v7.1, evento de Dirección: >20% en ≤48h)

Muestra estratificada por score, con semilla fija. Se usó el OHLCV de 15 min de GeckoTerminal del mismo pool.
- Muestreados: 164.
- **Con datos: 78.**
- Sin datos: 67 por HTTP 429 (aun con reintentos) y 19 sin velas.

| Score v7.1 | n | Máximo ≥ +20% en 48h | Cierre a 48h ≥ +20% | Rug (mínimo ≤ −90%) |
|---|---|---|---|---|
| 0-29 | 13 | 3 | 0 | 0 |
| 30-49 | 28 | 21 | 0 | **28** |
| 50-69 | 29 | 24 | 2 | **27** |
| 70-100 | 8 | 3 | 1 | 3 |
| **Total** | 78 | **51 (65%)** | **3 (3,85%, IC90 1,6-9,2%)** | **58 (74%)** |

- De los 51 que tocaron +20%, **44 (86%) también hicieron rug** en esas 48h.
- Mediana del máximo: **+54%**. Mediana del cierre a 48h: **−99,5%**.
- Precisión del score ≥ 50:
  - **73%** medida por el máximo (IC90 60-83%);
  - **8,1%** medida por el cierre (IC90 3,3-18,6%).
- AUC del score: 0,63 por el máximo; 0,82 por el cierre (**solo 3 positivos, no confiable**).
- Tasa base poblacional ponderada por bucket (máximo): 24,6% (97% de la población está en el bucket 0-29).

**Lectura:** operacionalizado como "el máximo toca +20%", el evento lo cumplen casi todos los tokens que se mueven, y el 86% de ellos termina en rug. Un usuario no puede vender en el máximo de un bombeo y descarga. **El score actual detecta movimiento, no aceleraciones sostenibles.**

## 4. Recomendación

1. **Umbral:** con el v7.2 tal como está, **ninguno cumple** (incluso ≥ 90 da 29,6%).
   - **Recomiendo corregir el feature, no solo el umbral:** que los bonos de aceleración cuenten solo con la ventana h1 completa (edad ≥ 60 min), y usar un **umbral de ALERTA de 56**. En la muestra da 1,8% (3/169): por debajo del objetivo, pero es el único corte con sentido en una distribución bimodal.
   - Si se prefiere estar dentro del objetivo en volumen, hay que rediseñar también "Edge temprano", "Buy pressure" y el momentum para tokens jóvenes (H a probar en un v7.3).
2. **No reactivar las emisiones** hasta tener la precisión del v7.2 medida sobre el evento definido. El modo sombra (§3 de la directiva) registra esas alertas; `calibrate_threshold_v72.py --outcomes-sample` las mide cuando pasan 48h (desde el **2026-10-02 01:10 UTC** para el Conjunto A).
3. **Operacionalizar el evento.** ">20% en ≤48h" medido por el máximo premia el bombeo y descarga (86% termina en rug). **Decidido por Dirección (30/09): métrica dual**, ver §4.2.

### 4.1 Actualización con más corridas (2026-09-30 03:09 UTC) [V]

Con 7 corridas de producción (n=282, reproducibilidad 282/282) se repite el mismo patrón, algo más marcado:

- **v7.2:** ≥50 91,5% · ≥60 88,3% · **≥70 66,0%** · ≥80 47,2% · **≥90 35,1%**.
- **Juventud:** de 186 ALERTAS, 182 (97,8%) son tokens de < 60 min con m5/h1 ≥ 0,9; 169 tienen "MCap bajo + Volumen bajo".
- **Con el gate de 60 min:** ≥50 33,7% · ≥55 28,0% · **≥56 1,4%**. Sigue bimodal, y la recomendación de umbral 56 no cambia.

El JSON versionado se regeneró el 2026-09-30 04:4x UTC con 8 corridas (n=297, coincidencia 297/297) y la métrica dual (§4.2).

### 4.2 Métrica dual de precisión (decisión de Dirección, 30/09) [V]

| Métrica | Definición | Uso |
|---|---|---|
| **Primaria** | Tocar **+20% antes de caer −30%** desde la entrada, dentro de las 48 h | Calibración (operativa) |
| **Secundaria** | **Cierre ≥ +20%** a las 48 h | Reporte al público (honestidad) |

Implementación (`calibrate_threshold_v72.py`):
- `event_primary` y `event_secondary` siguen la definición literal de Dirección.
- Velas OHLC de 15 min con orden **conservador** open → low → high → close: si una vela toca las dos barreras, cuenta primero la caída.
- **Velas ambiguas en el legado: 39**, así que la primaria está levemente subestimada.
- **Censura:** en el Conjunto A (menos de 48 h) la primaria queda decidida al tocar una barrera; si no, figura pendiente.
- Tests: `test_calibrate_dual.py` 8/8.

**Legado v7.1** (muestra estratificada, n=75 con velas; 71 dieron HTTP 429 y 19 no tenían velas):

| Score v7.1 | n | Primaria | Secundaria | Rug (−90%) |
|---|---|---|---|---|
| 0-29 | 11 | 1 (9,1%) | 0 | 0 |
| 30-49 | 27 | 16 (59,3%) | 0 | 27 |
| 50-69 | 29 | 18 (62,1%) | 3 | 25 |
| 70-100 | 8 | 3 (37,5%) | 0 | 1 |
| **Total** | 75 | **38 (50,7%, IC90 41,3-60,0)** | **3 (4,0%, IC90 1,6-9,6)** | 53 (70,7%) |

- **Por umbral:**

  | Umbral | Primaria | Secundaria |
  |---|---|---|
  | ≥ 50 | 21/37 = 56,8% (IC90 43,4-69,2) | 3/37 = 8,1% |
  | **≥ 56** | **21/35 = 60,0% (IC90 46,1-72,4)** | **3/35 = 8,6% (IC90 3,5-19,6)** |
  | ≥ 70 | 3/8 = 37,5% | 0/8 |

- **Tasa base poblacional (primaria), ponderada por bucket: 10,5%.** Si los tokens sin velas cuentan como fallo, la primaria total baja a 40,4%.
- **AUC del score:** primaria 0,61 · secundaria 0,76 (solo 3 positivos).
- **De los 38 aciertos primarios, 32 (84%) terminan en rug en 48 h.**

**Conjunto A v7.2 en producción** (censurado; 292 tokens: 68 con velas, 99 sin velas todavía, 125 con 429):
- Primaria resuelta en 23 casos: **8/23 = 34,8% (IC90 20,9-51,9)**, con 144 pendientes. La secundaria queda toda pendiente hasta el 2026-10-02 01:10 UTC.
- **Sesgo de la censura:** los que se resuelven primero son los de movimiento rápido.

**Interpretación:**
- La primaria mide si una alerta **daba la oportunidad de salir con +20% antes de un −30%**. El score v7.1 ≥ 30 multiplica esa probabilidad por unas 6 veces respecto del bucket 0-29 (59-62% contra 9%).
- Pero el 84% de esos aciertos termina en rug. La oportunidad existe **solo con disciplina de salida**: tomar ganancia en +20% y no mantener.
- La secundaria (mantener 48 h) casi nunca se cumple: 4% en total, 8,6% con score ≥ 56. **Es la cifra honesta para el público:** "si comprás y mantenés 48 h, menos de 1 de cada 10 alertas cierra arriba de +20%".

## 5. Limitaciones

- El Conjunto A tiene n=169, sale de 4 corridas en 1 hora (un solo régimen de mercado) y son solo tokens de Solana.
- Los resultados son del **v7.1**, no del v7.2 (los del v7.2 todavía no cumplen 48h).
- **Sesgo de selección en los resultados:** faltan 86 de 164 (429 y sin velas); los que no tienen velas probablemente sean tokens muertos. La mediana de cobertura de velas es 4,7%.
- Precio de entrada: el de DexScreener en la detección, contra velas de GeckoTerminal (pueden diferir levemente).
- El contrafáctico del gate resta los bonos del score ya topeado en 100 (subestima levemente a los que pasaban de 100).
- `bp_delta` quedó en 0 en el recálculo; en las 169 detecciones coincidió exacto con producción.

## 6. Cómo reproducir

```bash
python 04_Config/scripts/calibrate_threshold_v72.py                       # tasas por umbral (sin red)
python 04_Config/scripts/calibrate_threshold_v72.py --outcomes-sample 50  # + resultados a 48 h (~20 min, GeckoTerminal)
python 04_Config/scripts/calibrate_threshold_v72.py --outcomes-set-a --outcomes-sample 50 --cache velas.json            # métrica dual, llena la caché
python 04_Config/scripts/calibrate_threshold_v72.py --outcomes-set-a --outcomes-sample 50 --cache velas.json --offline  # mismo resultado, sin red
```
