# Token Unlocks → Tokenomist — calendario de desbloqueos

**Repo:** no aplica (servicio). https://tokenomist.ai (`token.unlocks.app` sirve lo mismo)
**Licencia:** términos de Tokenomist. API comercial [I].
**Gratis:** parcial (2026-10-04, D-087):
- `GET https://tokenomist.ai/` → 200, 906 KB. Trae un script de Cloudflare, sin challenge. Los datos vienen como flight data de React Server Components (`self.__next_f`): filas de tokens (p. ej. `HYPE` con precio) y 29 fechas de octubre de 2026 [V].
- `GET https://api.tokenomist.ai/v1/token/list` → **401** sin key [V].
- Alternativa probada: el endpoint de unlocks de DefiLlama (`api.llama.fi/emissions`) → **402**, "Upgrade to the paid API plan" [V]. También es pago.
**Requisitos:** `requests` y un parser del flight data (cadenas JSON escapadas dentro de `self.__next_f.push`). Es frágil.
**Tipo de dato:** próximo desbloqueo por token (fecha, valor en $, tipo cliff o lineal), porcentaje liberado, supply máximo [V en columnas del HTML; detalle con key].
**Utilidad para pre-lanzamiento o anticipación:**
- **Desbloqueos grandes (cliff)** de tokens ya nacidos: anticipan presión de venta, lo opuesto a un lanzamiento [I]. Es contexto para no alertar un token justo antes de un cliff.
- Poca utilidad para activos **no nacidos** (todavía no tienen vesting publicado) [I].
**Riesgos técnicos:** el formato RSC cambia en cada deploy de Next.js. Sin key, solo lo que la portada muestra [I].
**Recomendación:** P3. Solo si Dirección consigue una key gratuita. Si no, el parser RSC no vale el mantenimiento: el dato de unlock no es central para preventa.
