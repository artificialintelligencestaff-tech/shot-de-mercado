# DePINscan (IoTeX) — explorador de proyectos DePIN (reemplazo de DePIN Ninja)

**Repo:** no aplica (servicio de IoTeX). https://depinscan.io
**Licencia:** términos de DePINscan [I].
**Gratis:** sí, sin cuenta ni key [V] (2026-10-04, D-087):
- `GET https://depinscan.io/` → 200, 745 KB, sin Cloudflare. `__NEXT_DATA__` trae `projectList` y `topMetrics`.
- `api.depinscan.io/api/projects` → 404: no hay API pública en esa ruta [V].
**Requisitos:** `requests`, `json` y `re`.
**Tipo de dato:**
- `projectList`: 440 proyectos con `project_name`, `market_cap`, `token_price`, `usd_24h_vol`, cambios de 24 h/7 d/30 d, `fully_diluted_valuation`, `total_devices` y `verification_time` [V].
- `topMetrics.lineCharts`: 364 días de market cap, volumen, dispositivos y cantidad de proyectos del sector [V].
**Utilidad para pre-lanzamiento o anticipación:**
- **Proyectos DePIN que aparecen en la lista** (con `verification_time` reciente) antes de tener token o listing: candidatos del sector e (DePIN) para el calendario [I].
- **Dispositivos en crecimiento con precio plano:** uso real que se adelanta al precio [H]; es lo que mide el método del doc 36.
**Riesgos técnicos:** sin API documentada; los datos viven en el HTML del sitio [I].
**Recomendación:** P2. Snapshot diario de `projectList` a `02_Analisis/patrimonio/informativo/depin/`. Las altas nuevas de un día a otro van como candidatas al calendario.
