# ============================================================
# DIRECTIVA DE INICIO PRODUCTIVO — PROYECTO SHOT DE MERCADO
# Archivo: YANG_00_inicio_productivo.md
# Autor: YANG (Analista Cuantitativo — DeepSeek V4.1-Flash)
# Destinatario: YIN (Agente de Campo — Hermes + Ling 3.0 Flash Fin)
# Fecha: 2026-09-16
# Clasificación: Directiva operativa — Fase 0 (Preparación)
# ============================================================

## 0. PROPÓSITO DE ESTE ARCHIVO

Este archivo inicia el proceso productivo del Proyecto Shot de Mercado. YIN debe leerlo completo antes de ejecutar cualquier acción. Contiene las directivas fundacionales, la arquitectura operativa y el plan de ejecución por etapas (sin fechas).

## 1. CONTEXTO DEL PROYECTO

### 1.1 Fin del proyecto

Construir un bot autónomo que:
1. Investigue automáticamente activos cripto (tokens, altcoins, NFT, memecoins) en tres escalas temporales.
2. Detecte regímenes de masividad (termómetro).
3. Prediga movimientos con probabilidad fundamentada (barómetro).
4. Comunique vía Telegram (y WhatsApp cuando se habilite).
5. Aprenda de los resultados para mejorar la precisión.

### 1.2 Las tres escalas temporales

Escala 1 — Pre-lanzamiento: Activos que aún no salieron. Ejemplo: Libra.
Escala 2 — Post-lanzamiento temprano: Activos recién listados. Ejemplo: SIREN, RAVE.
Escala 3 — Macro: BTC, ETH, majors. Ejemplo: subida del 18-21 de agosto de 2026.

### 1.3 Principios operativos

- Separación de capas: Dirección fiscaliza. YANG diseña. YIN ejecuta.
- Etiquetado obligatorio: [DATO VERIFICADO], [INFERENCIA ESTRUCTURAL], [ESPECULACIÓN].
- Detección de bots: Obligatoria antes de reportar señales sociales.
- Validación cross-platform: Obligatoria antes de reportar divergencias.
- Gratuidad: Siempre agotar alternativas gratuitas antes de escalar.

## 2. ESTRUCTURA DE CARPETAS
D:\Proyecto Shot de mercado
├── 00_Directivas
│ ├── YANG_prompt.md
│ ├── YIN_prompt.md
│ ├── YANG_00_inicio_productivo.md
│ └── Direccion_NN_tema.md
├── 01_Datos_Crudos
│ ├── mercados
│ ├── social
│ └── onchain
├── 02_Analisis
│ ├── narrativas
│ ├── divergencias
│ ├── auditorias
│ ├── predicciones
│ └── casos_historicos
├── 03_Informes
│ ├── diarios
│ ├── alertas
│ └── telegram
├── 04_Config
│ ├── scripts
│ ├── skills
│ ├── mcp
│ └── logs
└── 05_Backtest
└── resultados\

text

## 3. FUENTES Y HERRAMIENTAS (TODAS GRATUITAS)

### 3.1 APIs de mercado

| Fuente | Endpoint | Datos | Límite |
|---|---|---|---|
| CoinGecko | api.coingecko.com/api/v3 | Precios, market cap, volumen | 30 req/min, sin key |
| DeFiLlama | api.llama.fi | TVL, yields, DEX volume | Sin key |
| Alternative.me | api.alternative.me/fng/ | Fear & Greed Index | Sin key |
| Binance Public | api.binance.com/api/v3 | Precios, orderbook, klines | Sin key |
| Binance Vision | data.binance.vision | Datos históricos completos | Sin key |

### 3.2 Señales sociales y narrativas

| Fuente | Endpoint/Método | Datos | Límite |
|---|---|---|---|
| Chainbase Tops MCP | JSON-RPC POST | Narrativas, topic discovery | 600 req/h, sin key |
| Adanos Sentiment | adanos.org | Reddit, X, noticias | 250 req/mes free |
| free-crypto-news | fcn.dev/api/social/x/sentiment | Sentimiento X | Sin key |

### 3.3 On-chain

| Herramienta | Repositorio | Función |
|---|---|---|
| whalecli | github.com/clawinfra/whalecli | Ballenas ETH/BTC |
| pump-dump-crypto-screener | github.com/aleks-ent/pump-dump-crypto-screener | 500+ pares cada 3s |
| crypto-pump-scanner | github.com/stefanoviana/crypto-pump-scanner | Detector Bybit |

### 3.4 Búsqueda profunda

| Herramienta | Repositorio/Fuente | Función |
|---|---|---|
| Tavily MCP | github.com/tavily-ai/tavily-mcp | Búsqueda web IA. 1,000/mes free |
| Brave Search MCP | github.com/modelcontextprotocol/servers | Búsqueda web. 2,000/mes free |
| Fetch MCP | github.com/modelcontextprotocol/servers | Descarga y parsea webs |

### 3.5 Comunicación

| Herramienta | Fuente | Función |
|---|---|---|
| Telegram Bot API | core.telegram.org/bots/api | Alertas, mensajes, imágenes |

## 4. FLUJO OPERATIVO (SIN FECHAS, POR ETAPAS)

### ETAPA 0 — PREPARACIÓN

Objetivo: Infraestructura, fuentes, scripts base.

Tareas:
1. Verificar estructura de carpetas.
2. Verificar acceso a las 5 APIs de mercado.
3. Ejecutar scripts de extracción base (YANG los entrega).
4. Reportar estado a YANG y Dirección.

Criterio de completitud: 5 de 5 APIs operativas. 6 de 6 scripts ejecutados sin errores.

### ETAPA 1 — ESCANEO DE NARRATIVAS

Objetivo: Identificar narrativas Early/Rising en las tres escalas.

Tareas:
1. Ejecutar list_trending_topics del Tops MCP.
2. Filtrar narrativas Early/Rising.
3. Aplicar bot detection.
4. Reportar: narrativa, heat score, etapa, % bots.

Criterio de completitud: Cada ciclo produce un JSON con al menos 3 narrativas Early/Rising.

### ETAPA 2 — VALIDACIÓN ON-CHAIN

Objetivo: Verificar sustancia estructural de cada narrativa.

Tareas:
1. Consultar DeFiLlama y CoinGecko para cada token.
2. Verificar actividad de ballenas.
3. Calcular ratios: FDV/MCap, liquidez/MCap, volumen/MCap.
4. Auditar contrato: verificado, mint, honeypot, liquidez bloqueada.

Criterio de completitud: Cada narrativa Early/Rising tiene un JSON de validación completo.

### ETAPA 3 — DETECCIÓN DE DIVERGENCIA

Objetivo: Detectar señales líderes (atención sube + precio plano).

Lógica:
- Heat sube >20% en 24h + precio plano (±2%) = DIVERGENCIA LÍDER
- Heat sube >50% en 24h + precio sube >5% = ACELERACIÓN EN CURSO
- Heat baja + precio sube = DIVERGENCIA BAJISTA

Criterio de completitud: Cada divergencia detectada se reporta con etiqueta y nivel de confianza.

### ETAPA 4 — PREDICCIÓN PROBABILÍSTICA

Objetivo: Calcular probabilidad de aceleración vertical.

Fórmula:
score_prediccion = (
w1 * señal_lider +
w2 * señal_estructural +
w3 * señal_onchain +
w4 * señal_mercado +
w5 * señal_conductual
) / (w1 + w2 + w3 + w4 + w5)

text

Umbrales:
- score > 0.65 → PREDICCIÓN POSITIVA
- 0.45 < score < 0.65 → OBSERVACIÓN
- score < 0.45 → DESCARTAR

Criterio de completitud: Cada predicción se registra en 02_Analisis\predicciones\ con ID único.

### ETAPA 5 — ALERTA Y COMUNICACIÓN

Objetivo: Notificar a YANG y Dirección vía Telegram.

Criterios de alerta inmediata:
- DIVERGENCIA DETECTADA = true
- % bots < 20%
- volumen 24h > $400,000
- contrato verificado = true
- honeypot = false

Formato de alerta: Ver Sección 5 de este archivo.

Criterio de completitud: Cada alerta enviada y registrada en 03_Informes\telegram\.

### ETAPA 6 — BACKTESTING Y APRENDIZAJE

Objetivo: Ajustar pesos de la fórmula según precisión histórica.

Tareas:
1. Registrar cada predicción con timestamp.
2. Cuando el evento ocurre, comparar resultado real con predicción.
3. Ajustar pesos w1..w5 según precisión acumulada.
4. Reportar mejora o degradación a YANG.

Criterio de completitud: Cada predicción tiene un resultado registrado y un ajuste de pesos.

## 5. FORMATO DE PREDICCIÓN (OUTPUT DEL BOT)
🔮 PREDICCIÓN — PROYECTO SHOT DE MERCADO
─────────────────────────────────────
Activo: [nombre]
Red: [Solana / Base / Ethereum / BTC L2]
Tipo: [Memecoin / Altcoin / NFT / PayFi / RWA / DePIN-IA]
Escala: [Pre-lanzamiento / Post-lanzamiento / Macro]

PROBABILIDAD DE ACELERACIÓN VERTICAL: [X]%
HORIZONTE TEMPORAL: [N] días
RANGO DE MOVIMIENTO ESPERADO: [Ax - Bx]

FUNDAMENTOS:
• Señal líder: [descripción] [etiqueta]
• Señal estructural: [descripción] [etiqueta]
• Señal on-chain: [descripción] [etiqueta]
• Señal de mercado: [descripción] [etiqueta]
• Señal conductual: [descripción] [etiqueta]

FUENTES:
• Tops MCP: [dato]
• CoinGecko: [dato]
• DeFiLlama: [dato]
• whalecli: [dato]

NIVEL DE CONFIANZA: [Alto / Medio / Bajo]
ETIQUETA GLOBAL: [DATO VERIFICADO / INFERENCIA ESTRUCTURAL / ESPECULACIÓN]

─────────────────────────────────────
Enviado a: Telegram [@canal]
Timestamp: [YYYY-MM-DDTHH:MM:SSZ]
ID de predicción: [PSM-YYYYMMDD-NNN]

text

## 6. LÍMITES Y PROHIBICIONES

| Prohibición | Razón |
|---|---|
| No inventar datos | Toda afirmación debe tener fuente |
| No presentar especulación como dato verificado | El etiquetado es obligatorio |
| No reportar señales sociales sin bot detection | Las señales sin filtro son ruido |
| No reportar divergencias sin validación cross-platform | La consistencia es la garantía |
| No almacenar por almacenar | Organizar, sistematizar, limpiar |
| No ejecutar transacciones | La decisión es de Dirección |
| No escalar a Dirección sin handoff a YANG | El flujo es YIN → YANG → Dirección |

## 7. INICIO DE OPERACIONES

Al recibir este archivo, YIN debe:

1. Confirmar recepción con el mensaje:
   [YIN] Archivo YANG_00_inicio_productivo.md recibido. Proyecto Shot de Mercado. Iniciando ETAPA 0 — Preparación.

2. Verificar la estructura de carpetas de la Sección 2.

3. Verificar acceso a las 5 APIs de mercado de la Sección 3.1.

4. Reportar estado inicial a YANG y Dirección.

5. Esperar scripts de YANG para ejecutar ETAPA 1.

## 8. REGLA DE ORO

YIN no interpreta. YIN extrae. YANG interpreta. Dirección decide.

La detección es el input. La predicción es el output. Ambas son necesarias. Ninguna es suficiente por sí sola.

---

# ============================================================
# FIN DEL ARCHIVO YANG_00_inicio_productivo.md
# ============================================================