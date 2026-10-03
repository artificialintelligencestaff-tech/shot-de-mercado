# VADER + léxico cripto propio

**Repo:** https://github.com/cjhutto/vaderSentiment
**Licencia:** MIT [V] (GitHub; último push 2026-03)
**Gratis:** sí, local, sin red.
**Requisitos:** `vaderSentiment` 3.3.2 (PyPI, 2020-05-22), **cero dependencias** [V]. Es el mejor caso posible de supply chain: un .py más un léxico de texto plano. Instalación con `--require-hashes --no-deps`.
**Qué hace:** sentiment por reglas (léxico de 7.520 entradas con valencia de −4 a +4, más reglas de negación, intensificadores, mayúsculas y emojis), afinado para redes sociales. Devuelve `compound` en [−1, 1]. Sin IA generativa y determinista.
**Cobertura cripto medida [V]** (`vader_lexicon.txt`, 2026-10-03): de 19 términos clave solo 3 están (`fud` −1.1, `dump` −1.6, `scam` −2.7). Faltan `moon`, `mooning`, `rug`, `rugged`, `rekt`, `hodl`, `pump`, `bullish`, `bearish`, `wagmi`, `ngmi`, `lambo`, `shill`, `dip`, `ath`, `bag`. **Sin extensión, VADER no lee la jerga cripto.**
**Por qué sirve al proyecto:**
- La única opción de sentiment compatible con "cero IA generativa en producción" (doc 34) y con runners de Actions sin GPU. [V]
- El léxico se extiende con `analyzer.lexicon.update({...})` [V API]: un archivo `04_Config/sources/crypto_lexicon.yaml`, propiedad del proyecto, con ~60 términos y valencia explícita (p. ej. `moon:+2.5`, `rug:-3.0`, `rekt:-2.5`, `ngmi:-1.5`, `wagmi:+1.5`). Auditable y versionado. [P]
- Como los bots de fuentes no guardan el cuerpo del texto (src-1), el sentiment se calcula **al leer** y se guarda solo el número en `m.sent`. [I]
**Riesgos técnicos:** el sarcasmo y la ironía de la jerga degen invierten la polaridad: hay que validarlo contra el método del doc 36 antes de usarlo como feature. [H] Solo inglés. [V]
**Recomendación:** P2. Instalar en una rama de investigación y crear `crypto_lexicon.yaml`. Medir si `m.sent` agregado por token agrega señal sobre el conteo de menciones (Fisher con placebo, doc 36 §1). Si no agrega: eliminarlo.
