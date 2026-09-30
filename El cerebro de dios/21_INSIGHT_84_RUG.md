---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: HALLAZGO_REGISTRADO
last_updated: 2026-09-30
version: 1.0
---

# Insight: el 84% de los tokens que tocan +20% caen −99% después

Rótulos: [V] verificado · [I] inferido · [H] hipótesis · [P] pendiente.
Fuente de datos: `02_Analisis/diagnostics/threshold_analysis.json` y `v72_1_analysis.json` (filas `outcome_rows_legacy`), métrica dual del doc 19 §4.2.

## 1. Enunciado

> Entre los tokens detectados por el pipeline que cumplen la **métrica primaria** (tocar +20% antes de caer −30% dentro de las 48 h), **el 84% cae después −99% o más dentro de esas mismas 48 h** [V].

Con esta definición, la caída siempre ocurre **después** del +20%: si hubiera tocado −30% antes, la primaria habría fallado.

## 2. Evidencia [V]

Muestra: legado v7.1, estratificada por score, velas OHLC de 15 min de GeckoTerminal, n=75 tokens con datos.

| Subconjunto | Aciertos primarios | Luego ≤ −90% | Luego ≤ −99% | % (IC90 Wilson) |
|---|---|---|---|---|
| Todos | 38 | 32 | **32** | **84,2% (72,3-91,6)** |
| **Score ≥ 56** (umbral de emisión v7.2.1) | 21 | 16 | 16 | **76,2% (58,5-87,9)** |
| Score 30-69 | 34 | 32 | 32 | 94,1% (83,7-98,0) |

- **Mediana del mínimo después del acierto: −99,6%.** Mediana del último precio a 48 h de los aciertos: **−99,5%**.
- Solo **3 de 38** aciertos primarios cierran ≥ +20% a 48 h. Los 3 están en score ≥ 56, y de ahí sale la secundaria de 8,6% (3/35).
- Tasa de rug en todos los tokens con velas: 53/75 (70,7%).
- Todo acierto que cayó bajo −90% cayó también bajo −99% (32 y 32): en la muestra **no hay colapsos que se detengan entre −90% y −99%**.

**Limitaciones:**
- Los datos son del **v7.1**, no del v7.2.1: el v7.2.1 se valida en sombra (doc 20 §6.3).
- La muestra es estratificada y chica (n=75): 71 tokens dieron HTTP 429 y 19 no tenían velas, así que hay sesgo de selección posible.
- Hubo 39 velas ambiguas, resueltas de forma conservadora (primero la caída). Esto puede subestimar los aciertos primarios, pero no cambia que el rug venga después.
- El 84% es sobre todos los aciertos. **Para las alertas emitidas (≥ 56) la cifra que corresponde es 76%.**

## 3. Consistencia con la literatura 2026

| Paper | Hallazgo relacionado |
|---|---|
| arXiv 2608.20271 — *Catching the Rug* (Solana, 6,4 M tokens) | La gran mayoría de los memecoins muestra características de rug **dentro de la primera hora**; "over 80% of Memecoins experience rug pulls". Definición de rug: caída de TVL de 99% o inactividad |
| arXiv 2609.10246 — *Meme Coin Factories* (pump.fun, 15 M coins) | ≥ 17% de los trades son wash trading; ≥ 10% de los tokens son copias; existe "Market-Manipulation-as-a-Service". Los pumps rápidos e insostenibles son el negocio de actores estratégicos |
| arXiv 2601.22185 — *MemeChain* (4 chains) | El 5,15% de 34.988 memecoins deja de operar dentro de las 24 h |
| arXiv 2512.00377 — *Measuring Memecoin Fragility* | Resultados polarizados: "few extreme winners amid widespread collapse". Cita que más del 98% de los tokens nuevos en Ethereum y Solana muestran características de rug o de bots (cita de segunda mano, [I]) |

Nuestro 84% (−99% después de +20%) es coherente con un mercado en el que **el pump es el vehículo del dump**.

## 4. Implicancias

### 4.1 Producto
- La alerta **no es una recomendación de inversión**: como mucho es una **oportunidad de trade corto con salida disciplinada**. El valor, si existe, está en el **timing de salida**, no en la selección de activos.
- La métrica primaria ya tiene incorporado un plan de salida: toma de ganancia en +20% y stop en −30%. **Una alerta sin ese plan es engañosa.**
- [H] Se podría agregar una categoría "no operar": tokens con score alto pero señales de rug (liquidez drenada, dev con mucha tenencia, copias). Queda para medir.

### 4.2 Alerta de Telegram
- Hay que mostrar **las dos probabilidades**, con su IC y su n, calculadas para **la versión del scorer y el umbral que emiten** (no las del v7.1).
- Hay que incluir la advertencia con la cifra del umbral de emisión (hoy **76%** para ≥ 56 en el legado; se reemplaza por la del v7.2.1 cuando se valide) y la recomendación "tomar ganancia en +20%, stop −30%, NO mantener".
- **Hay que eliminar datos inventados:** el mensaje actual tiene valores por defecto que se muestran como si fueran datos, por ejemplo "Whale entry: 85.0 SOL (top 1%)" o "Liquidez: $25,000", cuando el token no los trae. La propuesta está en la rama `claude/fase2-p1` (ver §5 del reporte).

### 4.3 Comunicación pública
- **La cifra de portada es la secundaria:** "si comprás y mantenés 48 h, menos de 1 de cada 10 alertas cierra arriba de +20%" (8,6%, IC90 3,5-19,6, legado ≥ 56).
- No usar nunca "probabilidad de pump" sin definir el evento, el horizonte y el IC.
- Publicar la tasa de rug junto con los aciertos. Transparencia radical: acierto y colapso son el mismo evento visto en dos momentos distintos.

## 5. Pregunta abierta para Dirección

- ¿Emitir alertas sobre tokens cuyo desenlace más probable es −99% es compatible con "democratizar la anticipación"? Si el usuario llega tarde o no sale a tiempo, el sistema lo convierte en liquidez de salida del que manipula (2609.10246).
- Alternativas [H]:
  1. Emitir solo con el plan de salida explícito (propuesta actual).
  2. Pasar a alertas de **riesgo** (evitar) en lugar de oportunidad para Universo C.
  3. Exigir la validación del v7.2.1 con la métrica **secundaria** antes de emitir.
