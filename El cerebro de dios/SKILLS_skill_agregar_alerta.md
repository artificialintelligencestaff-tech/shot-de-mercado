---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
skill_role: emisor
---

# Skill — Agregar una Alerta

**Cuándo usar este skill:** cuando el pipeline detecta un candidato y hay que decidir si emitir alerta, o cuando YANG/Dirección pide emitir una alerta manual.

## 1. Antes de emitir — checklist

- [ ] Confianza >= 50% (ver `06_SCORING.md`).
- [ ] Kill switches inactivos: mint authority y freeze authority revoked.
- [ ] Liquidez >= $5,000.
- [ ] No existe alerta activa del mismo mint.
- [ ] El activo es adquirible al momento de la alerta.
- [ ] El paso a paso de adquisición está verificado (DEX funcional).

Si falla algún punto → no emitir. Reportar a YANG.

## 2. Estructura del mensaje

El mensaje sigue este formato exacto (definido en `09_ALERTAS.md`):

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
<descripción breve>

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
• <riesgo 1>
• <riesgo 2>
• Este token es de alto riesgo. No invertir más de lo que se puede perder.

📅 ACTUALIZACIONES
Se actualizará a t+1h, t+6h, t+24h según evolución.
Última actualización: <timestamp>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ No es asesoramiento financiero. Es predicción probabilística.
```

## 3. Cómo se registra la alerta

Además del mensaje Telegram, se debe:

1. ** agregar entrada en `_all_alerts.json`** con la estructura:

```json
{
  "timestamp": "YYYY-MM-DD_HHMMSS",
  "mint": "<mint_completo>",
  "symbol": "<SYMBOL>",
  "score": <score_final>,
  "confidence": <confianza>,
  "initial_price": <precio_al_emitir>,
  "status": "active_tracking",
  "trust_updates": [],
  "verdict_final": null
}
```

2. **Capturar el `message_id` de Telegram** (devuelto por la API).
3. **Guardar snapshot del mensaje** en `03_Informes\telegram\alerta_<mint>_<timestamp>.json`.

## 4. Cómo verificar que se emitió

```bash
# 1. ¿La alerta está en _all_alerts.json?
python -c "import json; a=json.load(open('02_Analisis/alerts/_all_alerts.json')); print([x['symbol'] for x in a])"

# 2. ¿El message_id fue capturado?
python -c "import os; d='03_Informes/telegram'; print(sorted(os.listdir(d))[-3:])"

# 3. ¿El bot respondió 200 en el envío?
# (ver stdout del script_97_emit_alerts.py)
```

## 5. Reglas de redacción

| Regla | Razón |
|---|---|
| Sin jerga técnica | El destinatario puede no saber qué es un mint, un swap, o una wallet |
| Paso a paso numerado | Cada paso debe ser ejecutable sin conocimiento previo |
| Riesgos explícitos | Nunca presentar una predicción como certeza |
| Disclaimer obligatorio | "No es asesoramiento financiero" |
| Nombres completos de servicios | Phantom, Jupiter, Binance — no "PHNT", "JUP", "BNB" |
| URLs cuando aplica | phantom.app, jup.ag |
| Emojis moderados | Solo los del template. No decorar |

## 6. Qué NO hacer al emitir

- ❌ Omitir el disclaimer.
- ❌ Prometer ganancias.
- ❌ Usar jerga sin explicar.
- ❌ Emitir sin baseline (`initial_price`).
- ❌ Emitir sin verificar kill switches.
- ❌ Emitir duplicado (mismo mint con alerta activa).
- ❌ Omitir la sección de riesgos.

## 7. Ejemplo completo — Alerta SI (histórica)

```
🚨 ALERTA SHOT DE MERCADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Activo: SI
Red: Solana
Mint: DegeC37...pump
Confianza: 56%  |  Score: 55
Ventana esperada: 24-48h
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 QUÉ ES
Token Solana recién lanzado en pump.fun. Narrativa emergente,
comunidad pequeña pero activa. Whale entry inicial de 85 SOL.

🔍 POR QUÉ
• Whale entry >= 50 SOL
• MCap en SOL >= 100
• Liquidez > $20,000

💰 CÓMO COMPRARLO (PASO A PASO)
1. Instalar Phantom Wallet (phantom.app)
2. Comprar SOL en exchange (Binance, Coinbase, Ripio)
3. Transferir SOL a la wallet Phantom
4. Conectar Phantom a Jupiter (jup.ag)
5. Swapear SOL por SI usando el mint DegeC37...pump
6. Verificar en Solscan que los tokens llegaron

⚠️ RIESGOS
• Token recién lanzado, sin historial
• Comunidad pequeña — puede desaparecer
• Este token es de alto riesgo. No invertir más de lo que se puede perder.

📅 ACTUALIZACIONES
Se actualizará a t+1h, t+6h, t+24h según evolución.
Última actualización: 2026-09-14_004501

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ No es asesoramiento financiero. Es predicción probabilística.
```

Resultado: FALSO POSITIVO (-95.7%). El formato fue correcto. La predicción falló. Eso es parte del sistema.

## 8. Cómo actualizar una alerta

Una alerta activa se actualiza en cada checkpoint t+1h, t+6h, t+24h. Formato reducido (ver `09_ALERTAS.md`).

Solo se notifica si el cambio de confianza es >= 10 puntos. Si no, se actualiza en silencio.

## 9. Cómo cerrar una alerta

Al llegar a t+24h, se emite veredicto final (formato en `09_ALERTAS.md`) y se registra:

1. `verdict_final` en `_all_alerts.json`.
2. `closed_at` con timestamp.
3. Actualización de `_precision_log.json`.

## 10. Recursos relacionados

- `09_ALERTAS.md` — formato completo + reglas.
- `06_SCORING.md` — cómo se calcula score y confianza.
- `07_TRUST_UPDATE.md` — cómo se actualiza la alerta.
- `_OPERATOR_HANDBOOK.md` — rutina de operación.

## VER TAMBIÉN

- [SKILLS_skill_entender_proyecto.md](SKILLS_skill_entender_proyecto.md) — entry point
- [SKILLS_skill_ejecutar_pipeline.md](SKILLS_skill_ejecutar_pipeline.md) — cómo ejecutar
- [SKILLS_skill_debuggear.md](SKILLS_skill_debuggear.md) — diagnóstico
- [09_ALERTAS.md](09_ALERTAS.md) — formato completo

## Changelog

- 2026-09-24 — v1.0 — Creación inicial (YANG, Ciclo 17.10.B)