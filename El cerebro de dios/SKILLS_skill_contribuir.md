---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
skill_role: contribuyente
---

# Skill — Contribuir al Proyecto

**Cuándo usar este skill:** cuando sos un agente nuevo (o un humano) y querés proponer una mejora, corregir un error, agregar una fuente, refinar el scoring, o expandir el cerebro documental.

## 1. Antes de contribuir — checklist obligatorio

- [ ] Leí `SKILLS_skill_entender_proyecto.md`.
- [ ] Leí `00_NUCLEO.md` (fines del proyecto).
- [ ] Leí `_MANIFESTO.md` (principios).
- [ ] Leí `02_ARQUITECTURA.md` (estructura).
- [ ] Revisé `04_SCRIPTS_CATALOG.md` (no duplicar).
- [ ] Revisé `05_FUENTES.md` (no duplicar fuentes).
- [ ] Revisé `06_SCORING.md` (no duplicar señales).
- [ ] Revisé `11_ROADMAP.md` (sé en qué fase estamos).
- [ ] Revisé `13_DECISIONES.md` (no propongo algo ya decidido).
- [ ] Mi propuesta respeta free-only, isolation y portabilidad.
- [ ] Mi propuesta trae evidencia o plan de verificación.

Si todo está marcado → la propuesta está lista.

## 2. Los 5 tipos de contribución

| Tipo | A qué apunta | Va a |
|---|---|---|
| **Cerebro** | Mejorar/expandir archivos `.md` del cerebro | YANG → Dirección → YIN |
| **Pipeline** | Nuevo script, fix de bug, optimización | YANG → Dirección → YIN |
| **Fuentes** | Nueva fuente gratuita, reemplazo, integración | YANG → Dirección → YIN |
| **Scoring** | Nueva señal, ajuste de pesos | YANG → Dirección |
| **Decisiones** | Cambio estratégico, reversión, nuevo rumbo | Dirección |

## 3. Flujo de contribución estándar

```
CONTRIBUYENTE
    ↓ propone (con evidencia y fundamento)
YANG
    ↓ valida, ajusta, diseña directiva
DIRECCIÓN
    ↓ autoriza
YIN
    ↓ ejecuta
EVIDENCIA VERIFICABLE
    ↓ confirma
YANG
    ↓ cierra el ciclo y registra
```

**Regla:** ningún contribuyente escribe directo a YIN. Todo pasa por Dirección.

## 4. Cómo redactar una propuesta

### 4.1 Formato de propuesta

```
PROPUESTA — <título corto>

TIPO: cerebro | pipeline | fuentes | scoring | decisiones

CONTEXTO:
<por qué se propone esto>

PROPUESTA:
<qué se propone exactamente>

FUNDAMENTO:
<fuentes, datos, lógica>

ALTERNATIVAS CONSIDERADAS:
<qué se descarta y por qué>

EVIDENCIA / PLAN DE VERIFICACIÓN:
<cómo se verifica que funciona>

IMPACTO ESPERADO:
<qué mejora, en qué porcentaje>

CONSTRAINTS:
- Free-only: SÍ
- Isolation: SÍ
- Portabilidad: SÍ
```

### 4.2 Ejemplo — Propuesta de nueva señal

```
PROPUESTA — Señal de funding rates negativos

TIPO: scoring

CONTEXTO:
El scoring v7 no incluye señales de order flow. Los funding rates
negativos sugieren shorts dominantes → posible short squeeze.

PROPUESTA:
Agregar bonificación de +15 puntos si funding rate < -0.05% en
los últimos 8h.

FUNDAMENTO:
[DATO VERIFICADO] Binance publica funding rates sin key.
[INFERENCIA ESTRUCTURAL] Funding negativo precede rebotes históricos
en BTC y ETH.

ALTERNATIVAS CONSIDERADAS:
Usar open interest en su lugar (descartado: menos accesible gratis).

EVIDENCIA / PLAN DE VERIFICACIÓN:
- Script de prueba: consultar funding rate de BTC para 30 días históricos.
- Comparar con subidas >20% en ventana de 48h.
- Si correlación >0.6, integrar. Si no, descartar.

IMPACTO ESPERADO:
Mejor detección en Universo A (activos maduros).

CONSTRAINTS:
- Free-only: SÍ (Binance Public API sin key)
- Isolation: SÍ
- Portabilidad: SÍ
```

## 5. Qué NO se acepta como contribución

- ❌ Propuestas sin fundamento ("creo que debería ser así").
- ❌ Duplicación de funciones existentes.
- ❌ Scripts sin ejecución verificable.
- ❌ Dependencias pagas o con trial limitado.
- ❌ Cambios al pipeline sin autorización.
- ❌ Edición directa de decisiones históricas.
- ❌ Archivos fuera de `D:\Proyecto Shot de mercado\`.
- ❌ Uso de credenciales en código.
- ❌ Promesas de ganancias garantizadas.
- ❌ Uso de jerga sin explicación en alertas.

## 6. Cómo verificar antes de proponer

### 6.1 Verificar que no existe

```bash
# ¿Existe un script similar?
python -c "import os; root=r'D:\Proyecto Shot de mercado\04_Config\scripts'; [print(f) for f in os.listdir(root) if '<keyword>' in f.lower()]"

# ¿Existe una fuente similar?
python -c "content=open(r'D:\Proyecto Shot de mercado\El cerebro de dios\05_FUENTES.md').read(); print('<keyword>' in content.lower())"

# ¿Existe una decisión previa?
python -c "content=open(r'D:\Proyecto Shot de mercado\El cerebro de dios\13_DECISIONES.md').read(); print('<keyword>' in content.lower())"
```

### 6.2 Verificar constraints

```bash
# ¿La fuente es gratuita? Verificar con requests.
python -c "import requests; r=requests.get('<url>', timeout=10); print(r.status_code); print(r.text[:200])"

# ¿El servicio requiere key paga?
# Leer docs públicas antes de proponer.
```

## 7. Cómo se registra una contribución aceptada

1. YANG emite la directiva con la propuesta.
2. Dirección autoriza.
3. YIN ejecuta.
4. YANG agrega una entrada en `13_DECISIONES.md`:

```
### D-YYYYMMDD-NN — <título>
- **Fecha:** YYYY-MM-DD
- **Decisor:** Dirección
- **Contribuyente:** <nombre>
- **Contexto:** ...
- **Decisión:** ...
- **Consecuencias:** ...
- **Estado:** VIGENTE
```

5. Se hace commit con mensaje: `contribucion: <título>`.

## 8. Errores comunes del contribuyente novato

| Error | Corrección |
|---|---|
| Proponer sin leer el cerebro | Leer primero, proponer después |
| Editar archivos directo | Enviar a YANG, esperar validación |
| Inventar datos | Etiquetar con fuente o especulación |
| Ignorar free-only | Verificar antes de proponer |
| Proponer sin evidencia | Traer plan de verificación |
| Duplicar función existente | Buscar primero en `04_SCRIPTS_CATALOG.md` |
| Proponer cambio de scoring con n<10 | Esperar a tener muestra suficiente |

## 9. Cómo integrar un modelo IA nuevo al proyecto

Si un LLM nuevo (Claude, GPT, Gemini, Llama) se incorpora:

1. **Recibir el master prompt** (`99_MASTER_PROMPT.md`).
2. **Leer el cerebro completo** (25 archivos).
3. **Identificar su rol:**
   - Analista (como YANG) → diseño, scoring, ciclos.
   - Ejecutor (como YIN) → scripts, evidencia.
   - Revisor externo → análisis crítico, sin ejecución.
4. **Declarar capacidades específicas** (contexto máximo, herramientas, velocidad).
5. **Firmar "contrato de rol"** en `13_DECISIONES.md`.
6. **Comenzar a operar según el flujo estándar.**

## 10. Reconocimiento

Toda contribución aceptada se registra en `13_DECISIONES.md` con el nombre del contribuyente. Es la memoria histórica del proyecto.

## 11. Recursos relacionados

- `15_CONTRIBUCION.md` — guía completa (este skill es la versión operativa).
- `13_DECISIONES.md` — bitácora donde se registran.
- `04_SCRIPTS_CATALOG.md` — para no duplicar scripts.
- `05_FUENTES.md` — para no duplicar fuentes.
- `11_ROADMAP.md` — para saber en qué fase encaja.

## VER TAMBIÉN

- [SKILLS_skill_entender_proyecto.md](SKILLS_skill_entender_proyecto.md) — entry point
- [15_CONTRIBUCION.md](15_CONTRIBUCION.md) — guía completa de contribución
- [13_DECISIONES.md](13_DECISIONES.md) — bitácora
- [_MANIFESTO.md](_MANIFESTO.md) — principios del proyecto

## Changelog

- 2026-09-24 — v1.0 — Creación inicial (YANG, Ciclo 17.10.D)