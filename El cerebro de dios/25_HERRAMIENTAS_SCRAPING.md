---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: INVESTIGACIÓN (nada instalado)
last_updated: 2026-10-01
version: 1.0
---

# 25 — Herramientas de scraping: Agent-Reach, Patchright Enhanced y Scrapling

Rótulos: [V] verificado (API de GitHub o consulta HTTP en esta sesión, 01/10/2026 ~03:00 UTC) · [I] inferido · [H] hipótesis · [P] pendiente.

**Método.** Solo lectura por la API de GitHub (`gh api`): metadatos, árbol de archivos, commits, releases, contribuidores y código de los archivos de instalación y de los canales relevantes. **No se instaló ni se ejecutó nada.**

**Checklist de supply chain aplicado a cada repo:**
- licencia;
- actividad y mantenedores (bus factor);
- dependencias directas y extras;
- hooks de instalación (`setup.py` con comandos propios, `preinstall` / `postinstall` en `package.json`, `curl | bash`);
- descargas en tiempo de ejecución (browsers, CLIs de terceros);
- credenciales que exige;
- viabilidad en GitHub Actions free tier (2 vCPU, 7 GB de RAM y 14 GB de disco, sin estado entre corridas).

---

## 1. Hallazgo previo: el repo de Patchright indicado no existe

- `github.com/whaleyxbt/patchright` → **HTTP 404** [V].
- El usuario `whaleyxbt` existe (cuenta de 2024-03, 12 repos públicos). Lo más parecido es **`whaleyxbt/patchright-enhanced`** [V]: no es fork y su descripción ("Browser automation toolkit for QA, monitoring and internal workflows") no coincide con su README.
- El Patchright original es **`Kaliiiiiiiiii-Vinyzu/patchright`**, con sus variantes `patchright-python` y `patchright-nodejs` [V].
- Se auditaron los dos: el enhanced (el que probablemente se quiso indicar) y el original (la base real).

---

## 2. Tabla comparativa

| | **Agent-Reach** `Panniantong/Agent-Reach` | **Patchright Enhanced** `whaleyxbt/patchright-enhanced` | **Patchright** (original) `Kaliiiiiiiiii-Vinyzu/patchright` | **Scrapling** `D4Vinci/Scrapling` |
|---|---|---|---|---|
| Licencia | MIT [V] | **sin licencia** (todos los derechos reservados) [V] | Apache-2.0 [V] | BSD-3-Clause [V] |
| Estrellas / forks | 86.687 / 7.619 [V] | 185 / 46 en la red [V] | 4.730 / 233 [V] | 84.767 / 8.666 [V] |
| Creado · último push | 2026-02-24 · 2026-09-15 [V] | 2026-03-25 · 2026-09-20 [V] | 2023-11-07 · 2026-09-30 [V] | 2024-10-13 · 2026-09-30 [V] |
| Mantenedores | 1 principal (321 commits) + colaboradores de 2–9 commits [V] | 1 (14 commits) [V] | equipo chico, activo [V] | 1 principal (1.551 commits) [V] |
| Releases | v1.5.0 (2026-06-11), sin binarios [V] | ninguna [V] | sí [V] | v0.4.15 (2026-08-23), sin binarios [V] |
| Lenguaje · tamaño | Python [V] | TypeScript, 43 KB [V] | TypeScript [V] | Python [V] |
| Dependencias directas | requests, feedparser, python-dotenv, loguru, pyyaml, rich, **yt-dlp**. Extras: playwright, **browser-cookie3**, mcp [V] | dotenv, patchright (npm) [V] | Playwright parcheado + Chromium [V] | núcleo: lxml, cssselect, orjson, tld, w3lib. Extra `fetchers`: curl_cffi, **playwright, patchright**, browserforge, apify-fingerprint-datapoints, msgspec, anyio, protego [V] |
| Hooks de instalación | ninguno (wheel de hatchling, sin `setup.py`) [V] | ninguno (`package.json` sin `pre/postinstall`) [V] | descarga de Chromium con `patchright install` [V] | ninguno al hacer `pip install` (setuptools + pyproject) [V] |
| Descargas en ejecución | **sí**: `agent-reach install` corre `npm install -g` (OpenCLI, mcporter) y `pipx install` de CLIs de terceros, dos de ellos **desde commits de git** (`rdt-cli`, `boss-agent-cli`) [V] | Chrome del sistema + `npx patchright install chrome` [V] | Chromium (~150 MB+) [I] | solo si se corre `scrapling install`: `playwright install chromium` + `install-deps` (apt) + actualización de la lista de TLD [V] |
| Credenciales que exige | **X (búsqueda, timelines): cookies `auth_token` y `ct0` de una cuenta**; Reddit: sesión logueada obligatoria (su propio código lo dice); extractor de cookies del navegador (`cookie_extract.py`) [V] | archivo `proxies.txt` con usuario y contraseña de proxies [V] | ninguna [V] | ninguna [V] |
| ¿Navegador? | opcional (playwright) [V] | **sí**, Chrome en modo visible; la sesión queda abierta hasta que alguien cierra la ventana [V] | **sí** [V] | no para el núcleo ni para el fetcher estático (curl_cffi); sí para los fetchers `Dynamic` y `Stealthy` [V] |
| Propósito declarado | "dar a un agente de IA acceso a Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu… sin pagar APIs" [V] | "stealth browser automation framework for penetration testing, scraping, and WAF bypass… pass Cloudflare, Kasada, DataDome" [V] | Playwright "indetectable" [V] | framework de scraping adaptativo, desde una request hasta un crawl [V] |
| Viable en Actions free | parcial: el paquete sí; los canales útiles necesitan cookies de cuentas (no se cargan en secrets: regla de credenciales) [I] | **no**: espera una ventana manual [V] | técnicamente sí, pesado [I] | **sí** el núcleo y el fetcher estático; los fetchers con browser son pesados [I] |
| **Veredicto** | **No integrar** | **Descartar** | **No integrar** (no hace falta) | **Candidata condicional** (solo núcleo, más adelante) |

---

## 3. Detalle por herramienta

### 3.1 Agent-Reach

| Pregunta de la directiva | Respuesta |
|---|---|
| Licencia, actividad, dependencias | MIT; 86,7k estrellas en 7 meses; 169 issues abiertos; último push 15/09; dependencias arriba [V] |
| ¿Funciona sin X API key? | **Parcialmente.** La lectura básica de un tweet pasa por Jina Reader (`r.jina.ai`, servicio de terceros) [V]. **La búsqueda y los timelines necesitan las cookies de una cuenta de X** (`TWITTER_AUTH_TOKEN`, `TWITTER_CT0`) vía `twitter-cli` [V]. Para el proyecto no sirve: la regla es no tocar credenciales y no usar cuentas personales |
| ¿Solo texto o también video? | Texto + **video vía yt-dlp**: metadatos, subtítulos y descarga. La transcripción de audio usa Groq Whisper, que requiere API key de Groq (`guides/setup-groq.md`) [V] |
| ¿Instalable en Actions? | El paquete Python sí. Pero Reddit y X necesitan sesión logueada [V]. yt-dlp desde IPs de datacenter suele recibir "Sign in to confirm you're not a bot" [I] |
| ¿`postinstall` o hooks sospechosos? | Ninguno en el paquete [V]. El riesgo está en `agent-reach install`: instala de forma global paquetes npm y CLIs pipx de terceros, algunos fijados a commits de git, fuera de cualquier lockfile del proyecto [V]. Incluye además un extractor de cookies del navegador [V] |

**Qué se aprovecha:** la verificación que documentan sobre Reddit. El JSON anónimo de Reddit está bloqueado; lo confirmamos (HTTP 403 [V]). En cambio, **el RSS de Reddit funciona sin login** (`https://www.reddit.com/r/<sub>/new/.rss` → 200, Atom [V]). Esa es la ruta para el doc 26, sin Agent-Reach.

### 3.2 Patchright Enhanced (y el Patchright original)

| Pregunta | Respuesta |
|---|---|
| Licencia, actividad, dependencias | Enhanced: **sin licencia** (no se puede reutilizar legalmente), un solo autor, 14 commits, dependencias `dotenv` + `patchright` [V]. El historial borró `leadFormPentest.ts`, `leadFormConfig.ts` y `universalpages/` [V] |
| ¿Requiere Chromium/Playwright? | **Sí.** Chrome del sistema más Patchright [V] |
| ¿Viable en Actions free? | **No**: abre Chrome en modo visible y espera a que una persona cierre la ventana (`session-runner.ts`) [V]. El original sí correría headless, con Chromium pesado [I] |
| ¿`postinstall` o hooks? | Ninguno en `package.json` [V] |
| Propósito | Evadir WAF y sistemas anti-bot (Cloudflare, Kasada, DataDome) con proxies rotativos [V]. Es un envoltorio de ~40 líneas sobre el original, sin valor agregado [V] |

**Veredicto: descartar.**
- Las fuentes del proyecto son APIs públicas y gratuitas pensadas para consumo programático. No hace falta un navegador "indetectable".
- Evadir protecciones anti-bot choca con los términos de uso de esos sitios.
- El enhanced no tiene licencia.

### 3.3 Scrapling

| Pregunta | Respuesta |
|---|---|
| Licencia, actividad, dependencias | BSD-3-Clause; muy activo (push del 30/09, releases quincenales); núcleo liviano (lxml, cssselect, orjson, tld, w3lib) [V] |
| ¿Scraping genérico sin browser? | **Sí.** `Selector` (parser adaptativo) con el núcleo; `Fetcher` estático con curl_cffi [V]. Pero el extra `fetchers` arrastra playwright y patchright aunque no se usen [V] |
| ¿Rate limits? | **No trae límites por defecto.** Spiders: `download_delay = 0.0`, `concurrent_requests = 4`, `robots_txt_obey = False`; `AutoThrottle` es opcional [V]. Hay que configurarlos explícitamente |
| ¿Instalable en Actions? | Sí el núcleo [I]. `scrapling install` corre `playwright install-deps` (apt, pesado): **no usar** |
| ¿Hooks? | Ninguno al instalar [V]. El repo incluye `agent-skill/Scrapling-Skill.zip` (95 KB), que no forma parte del paquete Python [I] |

---

## 4. Recomendación de integración

1. **Ahora: no instalar ninguna.** Para la métrica de repetición (doc 26) alcanza la biblioteca estándar más `requests`, que ya está en el pipeline:
   - `xml.etree.ElementTree` para RSS/Atom;
   - `html.parser` para la vista pública de Telegram;
   - `json` para 4chan, HN y CoinGecko.

   Hoy el pipeline instala solo `requests`, `python-dotenv` y `websockets` [V]; `feedparser` y `lxml` no están [V]. Cero dependencias nuevas = cero superficie nueva de supply chain.
2. **Scrapling, condicional y más adelante.** Solo si una fuente sin API cambia su HTML seguido y el parser de la stdlib se rompe. Condiciones:
   - **núcleo** (`scrapling==0.4.15`, sin extras), con hashes fijados (`pip install --require-hashes`) verificados contra PyPI y revisión del diff del release;
   - `robots_txt_obey=True`, `download_delay ≥ 2 s`, `concurrent_requests_per_domain = 1`;
   - sin fetchers con navegador, sin `scrapling install` y sin funciones de evasión de huella.
3. **Agent-Reach: no.** Para Reddit se usa su RSS directo [V]. X queda fuera de alcance mientras no exista una vía gratuita sin credenciales.
4. **Patchright / Patchright Enhanced: no.** Si algún día hiciera falta renderizar JS en una fuente que lo permita, se evalúa Playwright oficial con su propia auditoría.

**Regla operativa para cualquier fuente nueva:** API pública o feed pensado para consumo, sin cookies ni cuentas, respetando `robots.txt` y los límites publicados. La sonda de deriva de fuentes (propuesta I-5, doc 23) la vigila desde Actions.
