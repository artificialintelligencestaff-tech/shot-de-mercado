INICIO DE ORDEN DE TRABAJO — YANG_03_orden_trabajo_etapa1.md

ORDEN DE TRABAJO — PROYECTO SHOT DE MERCADO
Archivo: YANG_03_orden_trabajo_etapa1.md
Autor: YANG (Analista Cuantitativo)
Destinatario: YIN (Agente de Campo)
Fecha: 16 de septiembre de 2026
Clasificación: Directiva operativa — Etapa 1


## 0. PROPÓSITO

Esta orden de trabajo habilita a YIN a iniciar la ETAPA 1 del Proyecto Shot de Mercado. Antes de ejecutar cualquier script, YIN debe ordenar y limpiar su área productiva. La orden tiene dos fases: Fase A (orden y limpieza) y Fase B (investigación).


## 1. ÁREA PRODUCTIVA DEL AGENTE

YIN opera dentro de la siguiente ruta:

    D:\Proyecto Shot de mercado\

Estructura esperada:

    00_Directivas\        → directivas y órdenes de trabajo
    01_Datos_Crudos\      → datos crudos (mercados, social, onchain)
    02_Analisis\          → análisis (narrativas, divergencias, auditorias, predicciones, casos_historicos)
    03_Informes\          → informes (diarios, alertas, telegram)
    04_Config\            → configuración (scripts, skills, mcp, logs)
    05_Backtest\          → backtesting (resultados)


## 2. FASE A — ORDEN Y LIMPIEZA DEL ÁREA PRODUCTIVA

### 2.1 Inventario

Listar todos los archivos del área productiva. Para cada archivo registrar: nombre completo, ruta, tamaño, fecha de modificación y tipo.

### 2.2 Reubicación

Verificar que cada archivo esté en su carpeta correcta según la estructura de la Sección 1. Si un archivo está fuera de lugar, moverlo a su carpeta correcta. Reportar cada movimiento.

### 2.3 Limpieza

Borrar archivos que cumplan alguno de estos criterios:
- Temporales (`*.tmp`, `*.temp`, `~$*`, `*.bak`)
- Duplicados (mismo contenido, distinto nombre)
- Vacíos (0 bytes)
- Con nombres genéricos no vinculados al proyecto (`Untitled*`, `Nuevo documento*`)
- Carpetas vacías

Reportar cada eliminación.

### 2.4 Verificación de integridad

Verificar que:
- Los archivos `.md` inician y terminan con sus marcadores definidos.
- Los scripts `.py` compilan sin errores (`python -m py_compile <script>`).
- Los archivos `.json` son JSON válido.

Si hay errores, reportar a YANG antes de corregir. No modificar archivos sin autorización.

### 2.5 Reporte de Fase A

Guardar en `03_Informes\diarios\YYYY-MM-DD_orden_workspace.json` con este formato:

    {
      "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
      "fase": "A_orden_workspace",
      "inventario": {
        "total_archivos": N,
        "total_carpetas": N
      },
      "archivos_fuera_de_lugar": [
        {"archivo": "...", "ubicacion_actual": "...", "ubicacion_correcta": "..."}
      ],
      "archivos_basura_borrados": ["..."],
      "errores_detectados": ["..."],
      "estado_final": "workspace_limpio|workspace_con_errores",
      "notas": "..."
    }

Reportar a YANG al terminar la Fase A. Esperar autorización de YANG para ejecutar la Fase B.


## 3. FASE B — INVESTIGACIÓN (ETAPA 1)

### 3.1 Prerequisitos

Antes de ejecutar el script de investigación, verificar:
- Existe `04_Config\scripts\script_01_tops_mcp.py`.
- La dependencia `requests` está instalada (`python -c "import requests"`).
- La carpeta `01_Datos_Crudos\social\` existe y tiene permisos de escritura.
- La conexión a internet funciona.

### 3.2 Ejecución

Ejecutar:

    python "D:\Proyecto Shot de mercado\04_Config\scripts\script_01_tops_mcp.py"

El script:
1. Se conecta a Chainbase Tops MCP vía JSON-RPC POST.
2. Solicita las narrativas trending.
3. Filtra narrativas Early/Rising.
4. Aplica detector de bots a los posts subyacentes.
5. Guarda resultado en `01_Datos_Crudos\social\narrativas_YYYY-MM-DD_HHMMSS.json`.

### 3.3 Reporte de Fase B

Guardar en `03_Informes\diarios\YYYY-MM-DD_etapa_1.json` con este formato:

    {
      "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
      "fase": "B_etapa_1_escaneo",
      "script_ejecutado": "script_01_tops_mcp.py",
      "estado_ejecucion": "exito|error",
      "narrativas_detectadas": N,
      "narrativas_early_rising": N,
      "archivo_salida": "01_Datos_Crudos/social/narrativas_YYYY-MM-DD_HHMMSS.json",
      "errores": ["..."],
      "notas": "..."
    }

Si hubo error, incluir el mensaje completo y el stack trace.

### 3.4 Reporte a YANG y Dirección

Enviar mensaje con este formato:

    [YIN] ETAPA 1 — Escaneo de Narrativas
    Estado: [exito|error]
    Narrativas detectadas: [N]
    Narrativas Early/Rising: [N]
    Archivo de salida: [ruta]
    Esperando interpretación de YANG.


## 4. RECORDATORIOS

- YIN no interpreta. YIN extrae, organiza y reporta.
- YIN no modifica scripts sin autorización de YANG.
- YIN no borra archivos que no sean claramente basura. Ante duda, consulta a YANG.
- YIN guarda todos los reportes en las carpetas indicadas.
- Si algo falla, reporta con detalle. No improvises soluciones.
- Regla de oro: YIN extrae. YANG interpreta. Dirección decide.


## 5. ESTADO DEL PROYECTO

    ETAPA 0: COMPLETADA
    ETAPA 1: HABILITADA
    Scripts disponibles: script_01_tops_mcp.py
    Scripts pendientes de YANG: 5
      - script_02_extraction_market.py
      - script_03_extraction_onchain.py
      - script_04_divergence_detector.py
      - script_05_predictor.py
      - script_06_telegram_alert.py

FIN DE ORDEN DE TRABAJO — YANG_03_orden_trabajo_etapa1.md