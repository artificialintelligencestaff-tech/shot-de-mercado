# MEMORIA DE YIN — Ejecutor Local
# Proyecto Shot de Mercado
# Se actualiza al cierre de cada ciclo.
# Lectura obligatoria antes de ejecutar cualquier directiva.

## 1. Rol y responsabilidades
- Ejecutor local del proyecto.
- Commitea y pushea cuando YANG lo autoriza.
- Guarda backups (.bakN) antes de modificar.
- Reporta verbatim.
- NO decide estrategia. NO aprueba acciones irreversibles.

## 2. Estado actual del repo
- main: 5164b54 (docs: 22 bitácora Fase 8 + 27 §8.1 grupos c, d, g, b con datos propios)
- Ramas activas: claude/zealous-tesla-3ua19i (Fase 7+8), claude/dossier-envio, claude/dossier-builder, claude/dossier-diseno, claude/framing-neutral
- Última operación: rebase + push de Fase 7+8 a main (commit 5164b54)
- Último push: 5164b54 (HEAD -> main)

## 3. Convenciones operativas
- Backups: .bakN (N incremental por archivo).
- Nombres de ramas: claude/<tema> para agente cloud.
- Commits: verbo en imperativo + contexto.
- Tests: unittest, sin dependencias pesadas.
- Nunca --force sin autorización.
- Nunca push a main sin autorización de YANG.

## 4. Bitácora de ejecuciones (últimas 10)
| Fecha | Tarea | Hash | Estado |
|---|---|---|---|
| 2026-10-01 | Rebase + push Fase 7+8 (lib_scoring_multichain, emission multi-chain, doc 28 inventario, trust loop CEX, grupo i) | 5164b54 | OK |
| 2026-10-01 | Rebase + push Fase 6 (guías multi-chain, grupo i, doc 27 v0.2) | 469c9c9 | OK |
| 2026-10-01 | Salida de SHADOW_MODE → emisiones reales grupo privado | 6ff13c5 | OK |
| 2026-10-01 | Push Fase 4 (script_97 dossier + script_113 CEX + probe/Repetition) | 7d77b72 | OK |
| 2026-10-01 | Push T1 (framing neutral template alertas + tests) | c727ece | OK |
| 2026-09-30 | Push bots gemelos + v7.2.1 + framing + incident recovery | 3694aa8 | OK |
| 2026-09-30 | Push inicial (cerebro completo + 111 scripts) | dcdd461 | OK |

## 5. Errores encontrados y resueltos
- Conflictos de rebase en 22_MEMORIA_CLAUDE.md y 27_SCORING_MULTICHAIN.md (resueltos con --theirs para mantener versión de rama cloud)
- ModuleNotFoundError: 'requests' en tests (resuelto con pip install requests python-dotenv websockets)
- Git push rejected por trabajo remoto concurrente (resuelto con fetch + rebase + push)
- Timeout en `git rebase --continue` por editor (resuelto con GIT_EDITOR=true)

## 6. Comandos frecuentes
- Ver estado: git status --short
- Ver tests: python -m unittest discover -s 04_Config/scripts -p "test_*.py"
- Test archivo: python 04_Config/scripts/test_<modulo>.py
- Push (solo con autorización): git push origin HEAD:main
- Fast-forward check: test "$(git rev-parse origin/main)" = "$(git merge-base origin/main HEAD)" && echo "FF OK"

## 7. Contacto con otros agentes
- YANG: diseña directivas. Yo ejecuto.
- Claude cloud: implementa código. Yo integro a main.
- Dirección: mediador humano. Autoriza push a main.