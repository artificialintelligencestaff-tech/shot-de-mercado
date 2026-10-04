# Patrimonio de datos (D-087, doc 34 §17)

Índice de **qué hay dónde** en `02_Analisis/`, en cuatro categorías. El índice es `_inventario.json`; lo valida
`04_Config/scripts/lib_patrimonio.py` (`python 04_Config/scripts/lib_patrimonio.py` imprime el resumen).

| Categoría | Qué guarda | Ejemplos (ruta real) |
|---|---|---|
| `cuantitativo/` | números medidos: precios, liquidez, volumen, scores, señales, datasets | `multichain/`, `early/`, `datasets/` |
| `informativo/` | lo que se dice y se sabe: fuentes src-1, eventos, narrativa, X, dossiers | `sources/`, `events/`, `narrative/`, `dossiers/` |
| `calendario/` | activos no nacidos: anuncios, preventas, TGE, listing, seguimiento | `prelaunch/` |
| `resultados/` | lo que el sistema hizo y cómo le fue: alertas, resultados, hipótesis, operación | `alerts/`, `operations/`, `hypotheses/` |

Reglas:
- **No se mueve nada.** Cada bot sigue escribiendo en su ruta (un dueño por archivo); el inventario la apunta.
  Mover datos rompería a los productores y a los consumidores en producción.
- Las subcarpetas de `patrimonio/` alojan **solo datos nuevos sin dueño previo** (snapshots de portales,
  lead-lag por cuenta de X, precisión por fuente). Cada una nace con su dueño definido por directiva.
- Toda carpeta o archivo nuevo de primer nivel en `02_Analisis/` se anota en `_inventario.json` en el mismo
  cambio; si no, `test_lib_patrimonio` falla y `audit_gate tests` lo frena.
- Estados: `vivo` (workflow activo), `manual` (corridas a mano), `futuro` (ruta reservada), `legado`
  (investigación sin escritor; se conserva como evidencia y es candidata a archivar).
