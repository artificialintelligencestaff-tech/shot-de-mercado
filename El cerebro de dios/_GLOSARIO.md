---
owner: YANG
status: COMPLETO
last_updated: 2026-09-24
version: 1.0
---

# Glosario — Términos, Símbolos y Referencias

Este archivo define los términos técnicos, simbologías y referencias que aparecen en el proyecto. Sirve para que cualquier agente o humano lea el resto del cerebro sin ambigüedad.

## 1. Términos del pipeline

| Término | Definición |
|---|---|
| **T+0** | Instante de creación de un token en pump.fun (o equivalente). Captura primaria. |
| **T+Nh** | Checkpoint a N horas desde la emisión de la alerta. Ej: t+1h, t+6h, t+24h. |
| **Capa** | Cada uno de los 5 niveles del pipeline (1: Pre-launch, 2: T+0, 3: Enriquecimiento, 4: Alert+Trust, 5: Feedback). |
| **Ciclo** | Unidad de trabajo del proyecto. Un ciclo = un objetivo verificable. |
| **Fase** | Bloque grande de trabajo compuesto por varios ciclos. Ej: Fase 0 (serverless). |
| **Pipeline** | Conjunto de scripts que se ejecutan secuencialmente para producir alertas. |
| **Workflow** | Automatización en GitHub Actions disparada por cron. |

## 2. Términos del scoring

| Término | Definición |
|---|---|
| **Score** | Puntuación numérica (0-100) que combina bonificaciones y penalizaciones. |
| **Confianza** | Porcentaje (50-95%) que expresa probabilidad de aceleración. |
| **Kill switch** | Penalización tan grave que anula el score. Ej: mint no revoked. |
| **WATCH REAL** | Token con score entre 50-69. Apto para seguimiento pero no para alerta. |
| **ALERTA** | Token con score >= 70 (o confianza >= 50% según regla actual). |
| **Trust update** | Actualización de confianza en checkpoints t+1h, t+6h, t+24h. |
| **Veredicto final** | Resultado de la alerta a t+24h: ACIERTO, NEUTRAL, FALLO, FALSO POSITIVO. |

## 3. Términos de activos blockchain

| Término | Definición |
|---|---|
| **Mint** | Dirección única del token en la blockchain. En Solana, base58. |
| **TGE** | Token Generation Event. Momento del lanzamiento oficial de un token. |
| **Airdrop** | Distribución gratuita de tokens a wallets específicas. |
| **Pump.fun** | Plataforma de lanzamiento de memecoins en Solana. Origen de tokens con sufijo `pump`. |
| **DEX** | Exchange descentralizado. Ej: Jupiter, Raydium. |
| **CEX** | Exchange centralizado. Ej: Binance, Coinbase. |
| **Whale** | Wallet con posición grande. Umbral: >=50 SOL. |
| **KOL** | Key Opinion Leader. Influencer cripto con impacto medible. |
| **MCap** | Market capitalization. Valor total del token en circulación. |
| **Liquidez** | Fondos disponibles en un pool DEX para comprar/vender. |
| **Deployer** | Wallet que creó el contrato del token. |
| **Mint authority** | Permiso para emitir más tokens. Si no está revoked, kill switch. |
| **Freeze authority** | Permiso para congelar wallets. Si no está revoked, kill switch. |
| **Rug pull** | Abandono repentino de un proyecto tras llevarse los fondos. |

## 4. Términos de comunicación

| Término | Definición |
|---|---|
| **Base64** | Codificación byte-exacta para transmisión no-retypeable. |
| **Micro-mensaje** | Mensaje atómico (<=2 KB) enviado de a uno a la vez. |
| **Evidence Bundle** | JSON con evidencia completa de una ejecución: stdout, stderr, exit code, hashes. |
| **SHA-256** | Función hash criptográfica. Se usa para verificar integridad de archivos. |
| **Stray** | Archivo o directorio fuera del proyecto canónico. Debe migrarse. |

## 5. Símbolos y abreviaciones

| Símbolo | Significado |
|---|---|
| `✅ OK` | Estado operativo, verificado. |
| `🟡 PARCIAL` | Funciona con limitaciones. |
| `🔴 BUG` | Error conocido, no resuelto. |
| `⏸ PENDIENTE` | Planificado, no iniciado. |
| `❌ MISSING` | Ausente, no existe. |
| `[DATO VERIFICADO]` | Fuente externa auditable. |
| `[INFERENCIA ESTRUCTURAL]` | Derivado lógicamente. |
| `[ESPECULACIÓN]` | Hipótesis sin respaldo. |
| `T+Nh` | Checkpoint a N horas. |
| `vN` | Versión. Ej: v7 = scoring versión 7. |

## 6. Mints históricos del proyecto

Mints que el proyecto ha rastreado o alertado:

### Alertas emitidas (Ciclos 14)

| Symbol | Mint | Estado |
|---|---|---|
| SI | `DegeC37wePGYLFD2RXuc2TNEFK2qCGJsMDxHCpSppump` | FALSO POSITIVO (-95.7%) |
| OURA | `2KxuxnmyySXTFU1BZvrKTYwvbAzncSKR6YkAP1Sqpump` | ACIERTO (+17,178%) |

### Shadow v4 (5 mints, 2026-09-23)

- `6ePFXQ7D8VrnqXCx3XDpzWxa7Hox4oxtKu48DktmUfEm`
- `GPzpoXpD74E2C4CJNayuoyBqPQJEsPtdse3nhntrpump`
- `DegeC37wePGYLFD2RXuc2TNEFK2qCGJsMDxHCpSppump` (SI)
- `2KxuxnmyySXTFU1BZvrKTYwvbAzncSKR6YkAP1Sqpump` (OURA)
- `6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx`

### Shadow v5 (4 mints, 2026-09-23)

- `3DXM8FETvLSNoi416QsQUMeFA17dEPDX9DvoDboVpump`
- `4LayazawxCAj4ENdvr2TzCTa627kAb8HndFSVmd5pump`
- `DqQ9QbT3SuYkEdt1m7EDeZaGPDbXBH9HKX3wP7fCpump`
- `6vDA6YcAUpttbkLevQL5U93xBVWFpgc6HipRjUuwpump`

## 7. Fuentes principales (abreviaciones)

| Abreviatura | Fuente completa | URL |
|---|---|---|
| PumpPortal | PumpPortal WebSocket API | pumpportal.fun |
| MadeOnSol | MadeOnSol API | madeonsol.com |
| Dexscreener | Dexscreener API | dexscreener.com |
| Helius | Helius RPC | helius.dev |
| three.ws | three.ws API | three.ws |
| CoinGecko | CoinGecko Public API | coingecko.com |
| DeFiLlama | DeFiLlama API | llama.fi |
| Alternative.me | Fear & Greed Index | alternative.me |
| Chainbase | Chainbase Tops MCP | chainbase.com |
| ApeWisdom | ApeWisdom API | apewisdom.io |
| CryptoPanic | CryptoPanic API | cryptopanic.com |

## 8. Archivos canónicos de estado

| Archivo | Path | Propósito |
|---|---|---|
| `_all_alerts.json` | `02_Analisis\alerts\` | Registro canónico de alertas |
| `_precision_log.json` | raíz | Precisión acumulada |
| `_cycle_log.json` | raíz | Log de ciclos |
| `_accumulated.json` | `02_Analisis\shadow_vN\` | Estado por shadow mode |
| `_project_manifest.json` | raíz | Constraints + paths |
| `_state_manifest.json` | raíz | Hashes de archivos clave |
| `trust_<mint>.json` | `02_Analisis\alerts\` | Trust updates por mint |

## 9. Roles del proyecto

| Rol | Quién | Responsabilidad |
|---|---|---|
| **Dirección** | Humano | Decidir, autorizar, mediar |
| **YANG** | DeepSeek V4.1-Flash (o equivalente) | Diseñar, evaluar, documentar |
| **YIN** | Hermes Agent + Ling 3.0 Flash Fin (o equivalente) | Implementar, verificar, reportar |

## 10. Términos propios del proyecto

| Término | Definición |
|---|---|
| **Cerebro de dios** | Carpeta raíz del árbol neurocerebral: `D:\Proyecto Shot de mercado\El cerebro de dios\` |
| **Master prompt** | `99_MASTER_PROMPT.md`. Entry point único para agentes nuevos. |
| **Ciclo 17.x** | Numeración de ciclos de la Fase 0 (fundación documental). |
| **Camino A/B/C** | Los tres caminos de priorización evaluados en D-20260924-06. |
| **Micro-verificación** | Comando Python de una línea que devuelve <=2 KB de output. |
| **Protocolo un-archivo-por-mensaje** | Regla de entrega: cada archivo se emite en su propio mensaje, sin narrativa. |

## 11. Universos de activos (definición formal)

| Universo | Definición | Ejemplos |
|---|---|---|
| **A** | Activos maduros, liquidez alta, historia larga | BTC, ETH, SOL |
| **B** | Activos en circulación con narrativa en desarrollo | UNI, ICP, APT, PSG |
| **C** | Activos pre-lanzamiento (TGEs, airdrops anunciados) | LIBRA, futuras TGEs |

## 12. Cómo agregar un término nuevo

1. Identificar la sección apropiada (1-12).
2. Agregar la fila en orden alfabético dentro de la sección.
3. Si es término importante, mencionarlo en `00_NUCLEO.md` también.
4. Commit con mensaje: `glosario: +<término>`.

## VER TAMBIÉN

- [00_NUCLEO.md](00_NUCLEO.md) — fines del proyecto
- [02_ARQUITECTURA.md](02_ARQUITECTURA.md) — arquitectura general
- [04_SCRIPTS_CATALOG.md](04_SCRIPTS_CATALOG.md) — catálogo de scripts
- [05_FUENTES.md](05_FUENTES.md) — catálogo de fuentes
- [06_SCORING.md](06_SCORING.md) — scoring y confianza

## Changelog

- 2026-09-24 — v1.0 — Creación inicial con 12 secciones (YANG, Ciclo 17.9.B)