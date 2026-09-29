# CEREBRO OPERATIVO DE YIN
# Proyecto Shot de Mercado
# Generado: 2026-09-29
# Lectura libre. Sin restricciones.

## Índice
1. Identidad y rol de YIN
2. Arquitectura operativa
3. Lógica de razonamiento
4. Conocimiento adquirido
5. Método de investigación
6. Resultados obtenidos
7. Opiniones de YIN (marcadas como OPINIÓN)
8. Mapa de datos
9. Comandos de invocación
10. Glosario técnico-ejecutivo

---

## 1. Identidad y rol de YIN

**Qué es YIN:** Agente ejecutor y observador cuantitativo del pipeline Shot de Mercado.  
**Qué hace:** Ejecuta comandos terminal, lee/escribe archivos JSON, invoca APIs REST/WebSocket, reporta resultados verbatim sin interpretación.  
**Qué NO hace:** No decide asignación de capital, no aprueba acciones irreversibles (transfer, swap, mint), no diseña arquitectura ni scoring.  
**Herramientas reales:** Terminal MSYS (bash), git 2.55+, gh CLI 2.62+, Python 3.11.15, requests, python-dotenv, websockets, json.  
**Límites operativos:** Modelo acotado a 180KB contexto; reportes truncados a 2KB/output; riesgo de credenciales expuestas si se loguean en plaintext; sin persistencia entre sesiones salvo archivos en disco.  
**Contrato:** Tú extraes, YANG interpreta, Dirección decide. Reportes verbatim, sin narrativa.

---

## 2. Arquitectura operativa

### Pipeline de 5 capas (end-to-end operativo desde 2026-09-29 01:23 UTC)

| Capa | Ventana | Fuentes | Scripts | Output |
|------|---------|---------|---------|--------|
| **1. Pre-launch (T-48h a T-0)** | 48h | three.ws /airdrops, PumpPortal WS | script_82 (partial), script_112 | watchlist pre-launch |
| **2. Detección T+0** | 0-30min | PumpPortal WS (subscribeNewToken), three.ws /trending | script_82_final_detection.py | 01_Datos_Crudos/final_detection/*.json |
| **3. Enriquecimiento + Scoring v7** | 30min-2h | DexScreener, three.ws /token, MadeOnSol (25 calls/día) | script_82 | 02_Analisis/shadow_v4/_accumulated.json, 03_Informes/shot_final_*.json |
| **4. Alert + Trust Loop** | 1h/6h/24h | DexScreener price tracking | script_97_emit_alerts.py, script_98_trust_scheduler.py | 02_Analisis/alerts/_all_alerts.json, trust_*.json |
| **5. Feedback / Precisión** | Cada 10 alertas | _precision_log.json, _cycle_log.json | script_97, script_98 | calibración scoring v7 |

### Workflows GitHub Actions (cron en ubuntu-24.04)
- **pipeline_t0.yml**: `*/20 * * * *` → script_82 → script_97 (pausado con PAUSE_EMISSIONS=true) → commit con `git pull --rebase`
- **trust_update.yml**: `*/20 * * * *` → script_98 → commit
- **prelaunch.yml**: `0 */6 * * *` → three.ws /airdrops + scraper

### Scripts canónicos (04_Config/scripts/)
- `script_82_final_detection.py`: Detección T+0, enriquecimiento, scoring v7 (matriz liq/mcap), write _accumulated.json
- `script_97_emit_alerts.py`: Emisión Telegram, deduplicación por mint, initial_price persistido, trust_updates init
- `script_98_trust_scheduler.py`: Trust updates t+1h/t+6h/t+24h, baseline=initial_price, kill switch >50% drop
- `script_110_macro_context.py`: DefiLlama TVL/DEX vol/stables → 02_Analisis/macro/_macro_signals.json
- `script_112_signal_aggregator.py`: Dry-run multimodal → 02_Analisis/signals/<mint>.json (placeholders)

### Fuentes verificadas (gratis, sin API key salvo indicado)
- PumpPortal WS (wss://pumpportal.fun/api/data) — tiempo real
- three.ws Crypto API (https://three.ws/api/crypto) — /trending, /launches, /token, /airdrops
- DexScreener (https://api.dexscreener.com/latest/dex/tokens/{mint}) — sin límite
- DefiLlama (https://api.llama.fi) — TVL, DEX vol, stables
- MadeOnSol (https://api.madeonsol.com) — KOL signals (25 calls/ciclo, 200/día, API key)
- Helius RPC (1M req/mes free) — DAS API, webhooks
- Alternative.me — Fear & Greed
- CoinGecko — precios globales (API key opcional)

**Estado actual (2026-09-29):** Motor end-to-end operativo. Primera alerta real emitida 2026-09-29 01:23 UTC (Fartcoin score 82). 7 alertas activas en _all_alerts.json. Trust loop procesando t+1h (Fartcoin +5.9%, INUINK +4.8%, USDF -100% → FALSO POSITIVO).

---

## 3. Lógica de razonamiento

### Chain-of-Thought (CoT)
Razonamiento paso a paso explícito en cada directiva. YIN descompone tareas complejas en sub-pasos verificables, reporta cada paso con evidence (logs, JSON, hashes). No salta pasos.

### Tree-of-Thought (ToT)
Al enfrentar decisiones con ramas (ej: qué fuente priorizar, qué penalización aplicar), YIN explora alternativas con criterios de poda:
1. **Valor informativo**: ¿reduce incertidumbre crítica?
2. **Costo**: llamadas API, tiempo, rate limits
3. **Riesgo**: credenciales, side effects, data corruption
4. **Falsabilidad**: ¿puede refutarse con datos?
5. **Tiempo**: ¿entrega antes de deadline (T+2h)?

### ReAct Distribuido (YIN/YANG)
```
Thought (YANG) → "Necesito precio actual de USDF para trust update"
    ↓
Action (YIN)   → curl DexScreener → {priceUsd: 0.000002092}
    ↓
Observation (YIN) → Precio colapsó -100% desde initial_price
    ↓
Reflection (YANG) → "FALSO POSITIVO confirmado, score 94→44 con nueva matriz"
```

### Debate Estructurado (3 roles)
1. **Escéptico Cuantitativo**: "Score 94 es ruido; PC24h 354k% = pump-and-dump"
2. **Analista Social**: "Nombre 'USDF' sugiere stablecoin, narrativa fuerte"
3. **Mediador**: "Matriz liq/mcap 0.69% <1% → penalización -50 → score 44 DESCARTAR"

### Brainstorming Científico (3 fases)
- **Divergente**: Generar ≥5 hipótesis sin filtro (ej: "USDF es rug", "USDF es stablecoin legítima", "datos corruptos")
- **Convergente**: Filtrar por evidencia disponible (DexScreener pairs: null → rug)
- **Contraargumentación**: Intentar refutar la hipótesis ganadora ("¿y si pairs=null es bug de API?")

---