---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Alertas — Formato y Reglas de Emisión

Este archivo define cómo se emite una alerta vía Telegram: cuándo se dispara, qué contiene, cómo se estructura para usuarios no-técnicos, y cómo se actualiza.

## 1. Cuándo se emite una alerta

Una alerta se emite cuando **todas** estas condiciones se cumplen:

| Condición | Umbral |
|---|---|
| Score final | >= 50 |
| Confianza declarada | >= 50% |
| Kill switch (mint/freeze) | NO activo |
| Liquidez | >= $5,000 |
| No duplicada | No hay alerta activa previa del mismo mint |

**Nota:** el umbral de confianza es >= 50% (no 70%). El proyecto notifica por calidad, no por cantidad.

## 2. Estructura del mensaje Telegram

Cada alerta sigue este formato exacto. Es lo que recibe el usuario final.

```
🚨 ALERTA SHOT DE MERCADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Activo: <SYMBOL>
Red: Solana
Mint: <mint_short>
Confianza: <50-95>%  |  Score: <score_final>
Ventana esperada: <24-48h>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 QUÉ ES
<descripción en 2-3 líneas: narrativa, utilidad, comunidad>

🔍 POR QUÉ
• <señal 1>
• <señal 2>
• <señal 3>

💰 CÓMO COMPRARLO (PASO A PASO)
1. Instalar Phantom Wallet (phantom.app)
2. Comprar SOL en exchange (Binance, Coinbase, Ripio)
3. Transferir SOL a la wallet Phantom
4. Conectar Phantom a Jupiter (jup.ag)
5. Swapear SOL por <SYMBOL> usando el mint <mint>
6. Verificar en Solscan que los tokens llegaron

⚠️ RIESGOS
• <riesgo específico 1>
• <riesgo específico 2>
• Este token es de alto riesgo. No invertir más de lo que se puede perder.

📅 ACTUALIZACIONES
Se actualizará a t+1h, t+6h, t+24h según evolución.
Última actualización: <timestamp>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ No es asesoramiento financiero. Es predicción probabilística.
```

## 3. Reglas de redacción

| Regla | Razón |
|---|---|
| Sin jerga técnica | El destinatario puede no saber qué es un mint, un swap, o una wallet |
| Paso a paso numerado | Cada paso debe ser ejecutable sin conocimiento previo |
| Riesgos explícitos | Nunca presentar una predicción como certeza |
| Disclaimer obligatorio | "No es asesoramiento financiero" |
| Nombres de servicios completos | Phantom, Jupiter, Binance — no "PHNT", "JUP", "BNB" |
| URLs cuando aplica | phantom.app, jup.ag — para que el usuario no busque en Google |

## 4. Actualizaciones de alerta

Una alerta activa se actualiza en cada checkpoint (t+1h, t+6h, t+24h). El mensaje de actualización es más corto:

```
🔄 ACTUALIZACIÓN SHOT DE MERCADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Activo: <SYMBOL>
Stage: t+<N>h
Precio actual: $<price>
Cambio desde emisión: <+/-X>%
Confianza actual: <Y>%
Veredicto parcial: <ACIERTO | NEUTRAL | FALLO | FALSO POSITIVO>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Última actualización: <timestamp>
```

**Regla:** solo se envía actualización si el cambio de confianza es >= 10 puntos. Si no, se actualiza `_all_alerts.json` en silencio.

## 5. Veredicto final (t+24h)

Al cierre de t+24h se emite el veredicto final:

```
✅/❌ VEREDICTO FINAL SHOT DE MERCADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Activo: <SYMBOL>
Emitida: <timestamp_emisión>
Cerrada: <timestamp_cierre>
Precio emisión: $<initial_price>
Precio cierre: $<final_price>
Cambio total: <+/-X>%
VEREDICTO: <ACIERTO | NEUTRAL | FALLO | FALSO POSITIVO>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Este mensaje cierra el ciclo de la alerta. Pasa a `_precision_log.json`.

## 6. Canal de emisión

- **Bot:** el configurado en `04_Config\.env` como `TELEGRAM_BOT_TOKEN`.
- **Chat:** el configurado como `TELEGRAM_CHAT_ID`.
- **Formato:** Markdown (o MarkdownV2 si el mensaje usa caracteres reservados).
- **Sin preview de links** (disable_web_page_preview: true).

## 7. Rate limits y fallback

- **Telegram Bot API:** 30 mensajes/segundo. El proyecto está muy por debajo.
- **Retry:** si falla el envío (HTTP != 200), reintentar 3 veces con backoff exponencial (1s, 2s, 4s).
- **Fallback:** si los 3 intentos fallan, registrar en `_scheduler_log.json` con `telegram_failed: true` y continuar.

## 8. Historial de alertas

Todas las alertas emitidas se registran en:

- `02_Analisis\alerts\_all_alerts.json` — registro canónico.
- `03_Informes\telegram\` — snapshots de mensajes enviados.
- `02_Analisis\alerts\trust_<mint>.json` — historial de trust de cada una.

## 9. Alertas emitidas (histórico)

| Fecha | Symbol | Score | Confianza | Veredicto final |
|---|---|---|---|---|
| 2026-09-14 | SI | 55 | 56 | FALSO POSITIVO |
| 2026-09-14 | OURA | 55 | 56 | ACIERTO |
| 2026-09-24 | (pendiente verificar mints de v5) | — | — | — |

**Precisión acumulada:** 50% (1 de 2).

## 10. Estado actual de emisión

| Aspecto | Estado |
|---|---|
| Bot funcional | OK — verificado Ciclo 17.1 |
| Formato del mensaje | ACTIVO — según sección 2 |
| Actualizaciones | ACTIVAS — pero sin baseline correcta (bug trust) |
| Veredicto final | PARCIAL — depende del fix de baseline |
| Registro histórico | OK — `_all_alerts.json` poblado |

## 11. Pendientes

1. **Fix de baseline** (Ciclo 17.10) → permitirá actualizaciones con cambio real.
2. **Plantilla para activos pre-lanzamiento** — el paso a paso cambia (no hay mint aún).
3. **Localización:** solo español rioplatense por ahora.
4. **Adjuntos:** considerar enviar gráfico de precio en la actualización.

## VER TAMBIÉN

- [06_SCORING.md](06_SCORING.md) — cómo se calcula score y confianza
- [07_TRUST_UPDATE.md](07_TRUST_UPDATE.md) — cómo se actualiza la alerta
- [03_FLUJOS.md](03_FLUJOS.md) — workflow Alert + Trust
- [12_TROUBLESHOOTING.md](12_TROUBLESHOOTING.md) — bugs conocidos
- [14_METRICAS.md](14_METRICAS.md) — precisión acumulada

## Changelog

- 2026-09-24 — v1.0 — Creación inicial con formato Telegram para no-técnicos (YANG, Ciclo 17.6.C)