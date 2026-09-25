---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Operator Handbook — Manual del Operario

Este manual es para **cualquier humano o agente** que tome el proyecto Shot de Mercado y necesite operarlo. Se lee en 20 minutos. Se aplica en 1 día.

## 1. Qué es este proyecto en 3 párrafos

Es un bot de Telegram que predice aceleraciones verticales (>20% en 24-48h) de activos blockchain. Usa multiplicidad de filtros independientes gratuitos. Emite alertas accionables para usuarios no-técnicos.

Corre 24/7 en la nube (GitHub Actions), sin depender de hardware local. El estado vive en el repositorio, versionado.

Tiene tres roles: Dirección (humano) decide, YANG (analista IA) diseña, YIN (ejecutor IA) implementa. Ninguno hace el trabajo del otro.

## 2. Primeros 20 minutos — lectura mínima

En este orden:

1. `README.md` — qué es el proyecto.
2. `00_NUCLEO.md` — fines.
3. `_MANIFESTO.md` — por qué existe.
4. `02_ARQUITECTURA.md` — cómo funciona.
5. `11_ROADMAP.md` — en qué fase estamos.
6. `10_ESTADO_ACTUAL.md` — qué está pasando hoy.
7. `_GLOSARIO.md` — términos que no entiendas.
8. `SKILLS_skill_entender_proyecto.md` — cómo actuar según tu rol.

Con eso, ya podés operar.

## 3. Roles y responsabilidades

| Rol | Qué hace | Qué NO hace |
|---|---|---|
| Dirección | Decide, autoriza, media entre YANG y YIN | No edita scripts, no ejecuta |
| YANG | Diseña, evalúa, documenta, emite directivas | No ejecuta scripts |
| YIN | Implementa, ejecuta, verifica, reporta evidencia | No decide rumbo |

Regla: **ningún rol hace el trabajo del otro.**

## 4. Rutina diaria

### 4.1 Chequeos de mañana (5 min)

```bash
# 1. Verificar que el repo sigue sincronizado
cd "D:\Proyecto Shot de mercado"
git status

# 2. Verificar último ciclo ejecutado
python -c "import json; print(json.load(open('_cycle_log.json')))"

# 3. Verificar alertas activas
python -c "import json; a=json.load(open('02_Analisis/alerts/_all_alerts.json')); print(f'Alertas: {len(a)}'); [print(f'  {x[\"symbol\"]} | {x.get(\"verdict_final\",\"PENDIENTE\")}') for x in a]"
```

Si algo no cuadra → ir a sección 7 (diagnóstico).

### 4.2 Chequeos de tarde (5 min)

- Verificar que no haya errores en logs de GitHub Actions (cuando estén activos).
- Verificar que no haya strays fuera del proyecto.
- Verificar que los trust updates se hayan aplicado.

### 4.3 Cierre de semana (30 min)

- Revisar `14_METRICAS.md` — ¿cambió la precisión?
- Revisar `13_DECISIONES.md` — ¿hay decisiones pendientes?
- Actualizar `10_ESTADO_ACTUAL.md` con el snapshot de la semana.

## 5. Cómo emitir una alerta (si sos YANG o YIN)

### 5.1 Cuando el pipeline detecta un candidato

1. El pipeline calcula score.
2. Si score >= 50 y confianza >= 50% → candidato a alerta.
3. Verificar kill switches (mint/freeze).
4. Verificar liquidez >= $5,000.
5. Verificar que no exista alerta activa del mismo mint.
6. Emitir alerta con el formato de `09_ALERTAS.md`.

### 5.2 Formato de emisión

El mensaje de Telegram contiene:
- Activo, red, mint.
- Confianza y score.
- Ventana esperada.
- Qué es, por qué.
- Cómo comprarlo (paso a paso).
- Riesgos.
- Disclaimer.

Nunca se omite el disclaimer.

## 6. Cómo actualizar el cerebro documental

### 6.1 Si sos YANG

1. Identificás un archivo que necesita cambio.
2. Redactás el nuevo contenido en markdown completo.
3. Lo emitís en un único mensaje (regla un-archivo-por-mensaje).
4. Actualizás la versión en el header YAML.
5. Registrás el cambio en el changelog del archivo.

### 6.2 Si sos YIN

1. Recibís el bloque markdown de Dirección.
2. Lo escribís byte-exacto en la ruta indicada.
3. Reportás tamaño + SHA-256.

### 6.3 Si sos Dirección

1. Copiás el bloque de YANG.
2. Lo pegás a YIN con la instrucción de escritura.
3. Esperás confirmación.

Nada más.

## 7. Cómo diagnosticar problemas

### 7.1 Checklist rápido

| Síntoma | Ir a |
|---|---|
| Trust update con `price_change_pct: 0.0` | `12_TROUBLESHOOTING.md` Error 1 |
| `FILE_NOT_FOUND` en ruta esperada | Error 2 |
| Hash con patrones repetidos | Error 3 |
| Mensaje truncado | Error 4 |
| Script duplicado | Error 5 |
| Shadow modes en paralelo | Error 6 |
| Capa 1 sin TGEs | Error 7 |
| Git no inicializado | Error 8 |
| Sin workflows | Error 9 |

### 7.2 Comandos de diagnóstico rápido

```bash
# ¿Existe el path canónico?
python -c "import os; print('EXISTS:', os.path.isdir(r'D:\Proyecto Shot de mercado'))"

# ¿Está el bot Telegram vivo?
python -c "from dotenv import load_dotenv; import os, requests; load_dotenv(r'D:\Proyecto Shot de mercado\04_Config\.env'); t=os.getenv('TELEGRAM_BOT_TOKEN'); r=requests.get(f'https://api.telegram.org/bot{t}/getMe', timeout=10); print(r.json())"

# ¿Cuántos .json de estado hay?
python -c "import os; root=r'D:\Proyecto Shot de mercado'; [print(os.path.join(r,f)) for r,_,fs in os.walk(root) for f in fs if f.endswith('.json') and f.startswith('_')]"
```

## 8. Cómo migrar a GitHub (Fase 0, Ciclos 17.11-17.13)

### 8.1 Preparación (una vez)

1. Crear cuenta GitHub (si no existe).
2. Crear repo público en GitHub: `shot-de-mercado`.
3. Generar Personal Access Token (PAT) con permisos de escritura.

### 8.2 En el directorio local

```bash
cd "D:\Proyecto Shot de mercado"

# 1. Inicializar Git
git init
git branch -M main

# 2. Crear .gitignore
# (contenido provisto por YANG en Ciclo 17.12)

# 3. Crear pre-commit hook
# (contenido provisto por YANG en Ciclo 17.12)

# 4. Agregar remoto
git remote add origin https://github.com/<usuario>/shot-de-mercado.git

# 5. Primer commit
git add .
git commit -m "init: primer commit del proyecto Shot de Mercado"

# 6. Push
git push -u origin main
```

### 8.3 Cargar secrets en GitHub

En GitHub UI → Settings → Secrets and variables → Actions:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `COINGECKO_API_KEY` (si aplica)
- `HELIUS_API_KEY`
- `MADEONSOL_API_KEY`

Nunca en código. Nunca en `.env` del repo.

## 9. Constraint no negociables (recordatorio)

- **Free-only:** todas las fuentes y herramientas son gratuitas.
- **Isolation:** todo vive en `D:\Proyecto Shot de mercado\`.
- **Portabilidad:** cualquier agente o humano puede tomar el proyecto.
- **Evidencia > documentación:** sin ejecución verificable, no hay progreso.
- **Un ciclo = un objetivo:** no se dispersa.

## 10. Checklist de operación diaria

- [ ] Repo sincronizado (`git status` limpio).
- [ ] Último ciclo ejecutado sin errores.
- [ ] Alertas activas verificadas.
- [ ] Trust updates aplicados.
- [ ] Sin strays fuera del proyecto.
- [ ] Sin mensajes de error en logs.
- [ ] Cerebro actualizado si hubo cambios.

## 11. Cómo contactar a los roles

| Rol | Cómo se activa |
|---|---|
| Dirección | Humano. Siempre disponible. |
| YANG | Se le pega una directiva o se le pide un ciclo nuevo. |
| YIN | Se le pega una directiva con instrucción de escritura o ejecución. |

**Regla:** nunca se le habla directo a YIN sin pasar por Dirección. El flujo es siempre `YANG → Dirección → YIN`.

## 12. Cuándo escalar a Dirección

- Decisión estratégica (cambio de rumbo, nueva fuente, nueva fase).
- Bloqueo operativo (no se puede avanzar sin input humano).
- Error crítico (pérdida de datos, corrupción de estado).
- Emergencia de seguridad (credenciales expuestas, acceso no autorizado).

## 13. Cuándo escalar a YANG

- Bug en el pipeline.
- Propuesta de nueva señal para el scoring.
- Conflicto entre scripts.
- Actualización del cerebro documental.
- Dudas sobre clasificación de un activo.

## 14. Frase final

El proyecto no es un oráculo. Es un sistema de anticipación probabilística con honestidad declarada.

Si tenés dudas: **leer el cerebro antes de actuar**. Casi toda respuesta ya está escrita.

## VER TAMBIÉN

- [SKILLS_skill_entender_proyecto.md](SKILLS_skill_entender_proyecto.md) — entry point
- [00_Directivas_INDEX.md](00_Directivas_INDEX.md) — índice central
- [12_TROUBLESHOOTING.md](12_TROUBLESHOOTING.md) — errores conocidos
- [15_CONTRIBUCION.md](15_CONTRIBUCION.md) — cómo contribuir
- [_MANIFESTO.md](_MANIFESTO.md) — principios del proyecto

## Changelog

- 2026-09-24 — v1.0 — Creación inicial (YANG, Ciclo 17.9.C)