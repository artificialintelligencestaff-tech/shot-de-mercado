# Shot de Mercado

Detecta aceleraciones verticales en activos blockchain **antes** de que ocurran y las emite por Telegram, con la
ruta de compra primero.

**Objetivo medido:** +20 % antes de −30 % dentro de 24–48 h ("tasa primaria").

**Grupos de activos:**
- a: memecoins
- b: preventa
- c: governance DeFi
- d: sintéticos
- e: DePIN
- f: L1/L2
- g: RWA
- h: blue chips
- i: establecidos sin grupo

Reglas del proyecto: 100 % gratis (APIs sin key o con plan gratuito sin tarjeta), licencias MIT/Apache/BSD, sin
modo sombra (emisión real desde el día 1).

## Cómo funciona (resumen)

| Capa | Qué hace | Dónde |
|---|---|---|
| Detección por cron | Score v7.2.1 para tokens de 60 min o más, emisión y seguimiento | `pipeline_t0.yml` (script_82 → script_97), `trust_update.yml` (script_98) |
| Detección temprana | Websocket de PumpPortal y scorer joven (< 60 min); dos instancias a/b con un claim por mint | `early_watch*.yml` (script_116), doc 31–32 |
| Multi-chain | Scanner por grupo (b–i) | `multichain_scanner.yml` (script_114), doc 27 |
| Fuentes informacionales | Bots de RSS, Telegram, X y recetas YAML → esquema `src-1` → `lib_sources_store.query()` | `sources_*.yml`, doc 34 |
| Preventa | Calendario de activos no nacidos | `sources_prelaunch.yml`, doc 34 §15 |
| Orquestación y reparación | Merge, salud, poda por carpeta, reparador por reglas, eventos entre bots | `sources_orchestrator.yml`, `sources_self_repair.yml`, `lib_events` |
| Método | Hipótesis preregistradas, debate adversario, memoria episódica | `lib_scientific_method`, doc 36 |

## Mapa del repo

| Carpeta | Contenido |
|---|---|
| `04_Config/scripts/` | Código. `bot_*` = bots, `lib_*` = bibliotecas, `script_NN_*` = pipeline, `test_*` = tests |
| `04_Config/sources/`, `04_Config/recipes/`, `04_Config/influencers.yaml` | Configuración de bots (sumar una fuente = sumar una línea) |
| `02_Analisis/` | Datos. Categorías, dueños y retención: doc 38 e índice `02_Analisis/patrimonio/_inventario.json` |
| `El cerebro de dios/` | Documentación; índice en su `README.md` |
| `_servicios_open_source/` | Fichas de servicios gratuitos verificados (YIN investiga; `bot_genesis` genera recetas desde ellas) |
| `.github/workflows/` | Los workflows de Actions (cron); la tabla está en `_project_manifest.json` |
| `_auditoria/` | Material de auditoría publicado para Claude1 |

## Para un agente nuevo

1. Leer `El cerebro de dios/README.md`, y en este orden: docs 35 → 38 → 34 → 32.
2. La última fila de `El cerebro de dios/22_MEMORIA_CLAUDE.md` es el estado.
3. Antes de tocar código, correr la batería completa (sin red, ~1 min):
   ```bash
   pip install -r requirements-dev.txt
   for t in 04_Config/scripts/test_*.py; do python3 "$t" || echo "FAIL $t"; done
   python3 04_Config/scripts/audit_gate.py prohibited --base origin/main
   ```
4. Reglas que no se rompen:
   - un dueño por archivo (`git add -- <ruta>`, nunca `-A`);
   - nada de `--force` ni `reset --hard`;
   - backups antes de editar un doc;
   - tests en verde antes de cada commit.
5. Roles:
   - **YIN** investiga, integra y pushea a `main`.
   - **YANG** audita.
   - **Claude1/Claude2** implementan en ramas `claude/*`.
   - **Dirección** decide.

`_project_manifest.json` se regenera con `python3 04_Config/scripts/gen_project_manifest.py`.
