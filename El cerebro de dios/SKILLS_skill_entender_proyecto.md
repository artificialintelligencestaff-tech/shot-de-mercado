---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Skill — Entender el Proyecto Shot de Mercado

**Lee este archivo PRIMERO si sos un agente IA que acaba de ser introducido al proyecto.**

## Qué es este proyecto en 3 líneas

Un bot de Telegram que predice aceleraciones verticales (>20% en 24-48h) de activos blockchain. Usa multiplicidad de filtros gratuitos. Emite alertas accionables para usuarios no-técnicos. Opera 24/7 sin depender de hardware local.

## Cómo funciona en 5 pasos

1. **Captura T+0:** PumpPortal WS detecta tokens al instante de creación (25 tokens/min).
2. **Enriquecimiento:** Quality Gate filtra (7.5% pass rate), luego MadeOnSol, Dexscreener, Helius RPC añaden señales.
3. **Scoring v7:** Se calcula un score con bonificaciones (whale entry +20, KOL accumulating +30) y penalizaciones (KOL distributing -40, mint no revoked -50 kill switch).
4. **Alerta:** Si score ≥ umbral y confianza ≥50%, se emite alerta vía Telegram con descripción, guía de compra y riesgos.
5. **Trust update:** A t+1h, t+6h, t+24h se actualiza la confianza según cambio de precio real.

## Qué hacer según tu rol

| Si sos... | Leé esto primero | Después esto |
|---|---|---|
| Agente nuevo (cualquier modelo) | Este archivo | [_INDEX.md](../00_Directivas/_INDEX.md) |
| Agente que va a ejecutar | Este archivo | [skill_ejecutar_pipeline.md](skill_ejecutar_pipeline.md) |
| Agente que va a debuggear | Este archivo | [skill_debuggear.md](skill_debuggear.md) |
| Dirección (humano) | [_MANIFESTO.md](../00_Directivas/_MANIFESTO.md) | [_OPERATOR_HANDBOOK.md](../00_Directivas/_OPERATOR_HANDBOOK.md) |

## Constraints no negociables

- ✅ Todo gratis (free tier, open source).
- ✅ Todo dentro de `D:\Proyecto Shot de mercado`.
- ✅ Todo versionado en Git + GitHub.
- ❌ Nunca inventar datos. Etiquetar siempre.
- ❌ Nunca saltar pasos de verificación.

## Estado actual del proyecto (2026-09-24)

- **Bot Telegram:** operativo.
- **Scripts:** ~100, sin consolidar.
- **Git:** no inicializado.
- **GitHub Actions:** no existe todavía.
- **Shadow modes activos:** v4 (5 mints), v5 (4 mints).
- **Fase:** 0 (migración a serverless).

## Cómo saber si algo está roto

1. Revisá `00_Directivas/CEREBRO/10_ESTADO_ACTUAL.md`.
2. Si el trust scheduler da `price_change_pct: 0.0`, leé `12_TROUBLESHOOTING.md` — hay un bug de baseline conocido.
3. Si un archivo no existe, revisá `_state_manifest.json` en la raíz para los hashes esperados.

## Cómo proponer un cambio

1. Identificá el archivo correspondiente en `00_Directivas/CEREBRO/`.
2. Documentá la propuesta en un archivo temporal.
3. Emití la propuesta vía Dirección a YANG.
4. YANG valida y autoriza.

## VER TAMBIÉN

- [../00_Directivas/_INDEX.md](../00_Directivas/_INDEX.md)
- [../00_Directivas/_MANIFESTO.md](../00_Directivas/_MANIFESTO.md)
- [../00_Directivas/CEREBRO/02_ARQUITECTURA.md](../00_Directivas/CEREBRO/02_ARQUITECTURA.md)

## Changelog

- 2026-09-24 — v1.0 — Creación inicial (YANG, Ciclo 17.2)