INICIO DE ORDEN DE TRABAJO — YANG_10_orden_trabajo_script09.md

ORDEN DE TRABAJO — PROYECTO SHOT DE MERCADO
Archivo: YANG_10_orden_trabajo_script09.md
Autor: YANG (Analista Cuantitativo)
Destinatario: YIN (Agente de Campo)
Fecha: 16 de septiembre de 2026
Clasificación: Directiva operativa — Script 09


## 0. CONTEXTO

Dirección ha completado los siguientes pasos:

1. Creó el archivo .env en D:\Proyecto Shot de mercado\04_Config\.env con las API keys de Santiment y CoinGecko.
2. Guardó el script script_09_deepblue_whales.py en D:\Proyecto Shot de mercado\04_Config\scripts\.

Se autoriza la ejecución del script 09. Los scripts 07 y 08 quedan pendientes de guardar y se ejecutarán después.


## 1. VERIFICACIÓN DE PREREQUISITOS

Antes de ejecutar el script 09, verifica:

- El archivo script_09_deepblue_whales.py existe en 04_Config\scripts\.
- La dependencia requests está instalada.
- El archivo .env existe en 04_Config\ y contiene las API keys (NO las muestres en el reporte, solo confirma que existen).
- La carpeta 01_Datos_Crudos\onchain\ existe y tiene permisos de escritura.


## 2. EJECUCIÓN DEL SCRIPT 09

Ejecuta:

    python "D:\Proyecto Shot de mercado\04_Config\scripts\script_09_deepblue_whales.py"

El script consultará Deep Blue Alpha (alternativa gratuita a Whale Alert) y guardará el resultado en:

    01_Datos_Crudos\onchain\deepblue_whales_YYYY-MM-DD_HHMMSS.json


## 3. REPORTE

Independientemente del resultado, genera un reporte en 03_Informes\diarios\YYYY-MM-DD_script09.json con este formato:

    {
      "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
      "fase": "script_09_deepblue_whales",
      "estado_ejecucion": "exito|error",
      "archivo_salida": "01_Datos_Crudos/onchain/deepblue_whales_YYYY-MM-DD_HHMMSS.json",
      "errores": ["..."],
      "notas": "..."
    }

Si hubo error, incluye el mensaje completo del servidor.


## 4. MENSAJE DE REPORTE A YANG Y DIRECCIÓN

Envía un mensaje con este formato exacto:

    [YIN] Script 09 — Deep Blue Alpha
    Estado: [exito|error]
    Archivo: [ruta]
    Endpoints consultados: [stats, whale-index u otros]
    Contenido del campo "datos": [verbatim, sin resumir]
    Si hubo error: [mensaje completo]
    Esperando interpretación de YANG.


## 5. RECORDATORIOS

- YIN no interpreta los datos. Solo extrae, guarda y reporta.
- Si el servicio Deep Blue Alpha está caído o responde con error, reporta el error exacto sin improvisar alternativas.
- NO muestres las API keys del archivo .env en el reporte. Solo confirma que el archivo existe.


## 6. ESTADO DEL PROYECTO

    Scripts guardados: 01, 01b, 01c, 01d, 01f, 01g, 02, 03, 04, 05, 06, 09
    Scripts pendientes de guardar: 07, 08
    Última auditoría: script 06 (2 aceleraciones detectadas: LSK +30.32%, DRV +69.61%)
    Watchlist activa: ZEC (+17.23% 24h, 7 narrativas)

FIN DE ORDEN DE TRABAJO — YANG_10_orden_trabajo_script09.md