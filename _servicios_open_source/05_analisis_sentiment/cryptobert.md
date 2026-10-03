# CryptoBERT (ElKulako/cryptobert)

**Repo/modelo:** https://huggingface.co/ElKulako/cryptobert
**Licencia:** MIT [V] (tarjeta del modelo, 2026-10-03)
**Gratis:** sí. Modelo local, sin API ni key.
**Requisitos:** `transformers` + `torch` (CPU). Modelo de ~0,1B parámetros (base `vinai/bertweet-base`) [V]. Instalar torch en CPU suma cientos de MB por corrida en Actions [I] → necesita caché de pip y del modelo (`actions/cache`).
**Qué hace:** clasificador (no generativo) de sentiment cripto en 3 clases, Bearish/Neutral/Bullish [V]. Entrenado con 3,2M posts cripto (StockTwits 1,875M, Telegram 664k, Twitter 496k, Reddit 172k); la cabeza se ajustó con 2M posts etiquetados de StockTwits [V]. Largo recomendado ≤128 tokens [V].
**Por qué sirve al proyecto:**
- A diferencia de VADER, ya conoce la jerga cripto por entrenamiento: no hay que mantener un léxico. [I]
- Es un clasificador discriminativo, no un LLM generativo. [V] Igual corresponde que Dirección valide que entra en la regla "cero IA generativa" (doc 34). [P]
**Riesgos técnicos:**
- Corre en CPU: unos 20–50 ms por mensaje corto [I]. Con unos 300 ítems por hora es viable; con miles no, en runners gratuitos.
- Las etiquetas de StockTwits son autodeclaradas (ruidosas). [I]
- Sesgo temporal: entrenado antes del ciclo 2025–2026. [I]
**Recomendación:** P3. Evaluarlo solo si VADER más el léxico propio (ficha hermana) no pasa el test del doc 36. Si se evalúa: batch offline sobre los ítems de Telegram del día y comparación de señal contra VADER. No integrarlo en producción sin ese resultado.
