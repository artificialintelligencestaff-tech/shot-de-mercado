---
owner: Claude Code (implementador) — pendiente auditoría YANG
status: PENDIENTE_AUDITORIA
last_updated: 2026-09-30
version: 1.0
---

# Capítulo II — Arquitectura Multimodal

Primera fuente real en el agregador (`script_112`) y marco de fusión sin priorización (`lib_fusion`).
Todo lo numérico de este capítulo es **heurístico no calibrado**: con n = 2 alertas cerradas no hay
datos para estimar razones de verosimilitud ni confiabilidades. La probabilidad que sale de acá es
una **probabilidad declarada**, con intervalo, y no reemplaza al scoring v7.2.

## 1. Qué se implementó

| Commit | Contenido |
|---|---|
| `a674ca9` | Fix aparte: `script_82` importa `timezone` (NameError en L334 que rompía `score_token`). Backup `.bak10`. |
| `6894209` | **A** — `script_112` con Jupiter Tokens V2, interfaz `(chain, mint)`, salida `signals/{chain}/{mint}.json`. Backup `.bak1`. |
| `a753768` | **B** — `lib_fusion.py` + `test_lib_fusion.py` (25 tests) + bloque `fusion` en cada señal. Backup `.bak2`. |
| (este) | **C** — este documento. |

Archivos:
- `04_Config/scripts/script_112_signal_aggregator.py` — recolección + evidencia por fuente + fusión.
- `04_Config/scripts/lib_fusion.py` — matemática de fusión. Solo stdlib, **sin ningún string de chain** (lo verifica un test).
- `04_Config/scripts/test_lib_fusion.py` — `python 04_Config/scripts/test_lib_fusion.py`.
- `02_Analisis/signals/{chain}/{mint}.json` — señales schema 1.1 (`chain` en la raíz).
- `02_Analisis/signals/_example.json` — ejemplo real completo (PARASITE).

`script_82` no se tocó más allá del fix de import. La fusión todavía **no** entra al scoring.

## 2. Fuentes

| Fuente | Alcance | Estado | Rol |
|---|---|---|---|
| Jupiter Tokens V2 | **Solo Solana** (chain-specific) | **Integrada** | calidad del token: audit, holders, organic score, flujo 1h/24h |
| GeckoTerminal | Multi-chain principal | Pendiente | pools, trending, OHLCV |
| DexPaprika | Multi-chain secundaria | Pendiente | redundancia de precio/liquidez, SSE |
| GoPlus | Multi-chain | Pendiente | seguridad del contrato (honeypot, taxes, owner) |
| DexScreener | Multi-chain | Pendiente en `script_112` (ya se usa en `script_82`) | liquidez, txns m5/h1 |

El registro vive en `SOURCE_REGISTRY` (`script_112`). `sources_total` = fuentes del registro que aplican
a la chain: **5 en Solana, 4 en EVM** (Jupiter no aplica). Una fuente registrada sin datos cuenta como
evidencia neutra (LLR = 0). Candidatas para capítulos siguientes: MadeOnSol (KOL, requiere key),
three.ws (trending pump.fun), DefiLlama (contexto macro por chain).

## 3. Jupiter — mapeo de campos (verificado contra API real 30/09/2026)

Endpoint: `GET https://api.jup.ag/tokens/v2/search?query={mint}`, sin API key, 0.5 RPS
(`time.sleep` ≥ 2 s entre llamadas), reintento con backoff en 429. `/search` es difuso: **solo se acepta
el item cuyo `id` coincide exactamente con el mint**.

| Directiva original | Campo real | Destino en la señal |
|---|---|---|
| `devWallet` | `dev` | `onchain.creator_wallet.address` |
| `totalTokensCreatedByDev` | `audit.devMints` | `onchain.creator_wallet.dev_mints` |
| — | `audit.devMigrations` | `onchain.creator_wallet.dev_migrations` |
| — | `audit.devBalancePercentage` | `onchain.creator_wallet.dev_balance_pct` |
| `holderCount` | `holderCount` | `onchain.holder_distribution.holder_count` |
| — | `audit.topHoldersPercentage` | `onchain.holder_distribution.top_holders_pct` |
| `audit.mintAuthorityDisabled` | igual | `onchain.token_program.mint_authority_disabled` |
| `audit.freezeAuthorityDisabled` | igual | `onchain.token_program.freeze_authority_disabled` |
| — | `tokenProgram`, `launchpad`, `graduatedPool`, `graduatedAt` | `onchain.token_program` / `onchain.bonding_curve` |
| `organicScore` | `organicScore`, `organicScoreLabel` | `market.jupiter.raw` + evidencia |
| — | `isVerified` | evidencia |
| — | `usdPrice`, `mcap`, `liquidity`, `stats24h.priceChange`, `stats24h.buyVolume+sellVolume` | `market.price_usd`, `market_cap_usd`, `liquidity_usd`, `price_change_24h`, `volume_24h_usd` |
| — | `stats5m/1h/6h/24h` | `market.jupiter.raw` (completo) |

La respuesta cruda completa queda en `signals.market.jupiter.raw` y cada campo mapeado declara su
fuente en `metadata.field_provenance`.

### 3.1 Evidencia Jupiter → LLR (heurística no calibrada)

LLR en nats a favor de "aceleración vertical sin rug". Cada componente queda escrito en
`evidence.jupiter.components` con su valor y su regla.

| Componente | Regla | LLR |
|---|---|---|
| `audit.mintAuthorityDisabled` | `false` (authority activa) | −1.0 |
| `audit.freezeAuthorityDisabled` | `false` | −1.0 |
| `organicScore` | lineal `(s − 50)/50 · 0.75` | −0.75 … +0.75 |
| `holderCount` | < 100 / ≥ 1000 | −0.5 / +0.25 |
| `audit.topHoldersPercentage` | > 50% / > 30% | −0.75 / −0.25 |
| `audit.devBalancePercentage` | > 10% / > 5% | −0.5 / −0.25 |
| `stats24h.liquidityChange` | ≤ −90% (liquidez drenada) | −1.5 |
| `stats1h` buy share | > 60% / < 40% del volumen | +0.25 / −0.25 |
| `isVerified` | `true` | +0.25 |
| `audit.devMints`, `audit.devMigrations` | informativos: dirección ambigua (el dev de Fartcoin tiene 495 mints) | 0 |

## 4. Modelo de fusión (`lib_fusion`)

```
P = logit⁻¹( base + Σ_s w_s · clip(LLR_s, ±c) )
```

1. **Priors iguales**: confiabilidad de cada fuente `r_s ~ Beta(1, 1)`.
2. **Trust loop**: por alerta cerrada, `alpha += 1` si el signo del LLR de la fuente coincidió con el
   resultado, `beta += 1` si no. Fuentes sin evidencia o con LLR = 0 no se actualizan.
   `replay_trust` reconstruye desde cero en cada corrida (idempotente, sin estado en disco) y
   **rechaza snapshots capturados después de la alerta** (guardia anti look-ahead).
3. **Pesos**: `w ∝ E[r_s]` → mezcla fixed-share `(1 − γ)·w + γ/N` (piso γ/N) → tope `w ≤ w_max`
   con redistribución del exceso. Σw = 1: **pool logarítmico**. Así la evidencia correlacionada entre
   fuentes (todas miran los mismos trades) no se suma dos veces, y una fuente sin datos encoge P hacia la base.
4. **Tasa base**: `Beta(1 + aciertos, 1 + fallos)` de las alertas cerradas **de esa chain**.
5. **IC 90%**: Monte Carlo (4000 muestras, semilla fija) sobre la Beta de la tasa base y las Beta de cada fuente.
6. **RRF**: `score(d) = Σ_listas 1/(k + rank)` para combinar rankings de trending. Clave de item:
   `asset_key(chain, mint)` = `"chain:mint"`.

### 4.1 Parámetros — todos heurísticos no calibrados

| Parámetro | Valor | Efecto |
|---|---|---|
| `LLR_CLIP` (c) | 2.0 nats | ninguna fuente aporta una razón de verosimilitud > e² ≈ 7.4 |
| `FIXED_SHARE_GAMMA` (γ) | 0.3 | piso = γ/N → 0.06 con 5 fuentes, 0.075 con 4, 0.05 con 6 |
| `MAX_WEIGHT` | 0.35 | tope individual; si 1/N > 0.35 se usa 1/N (infactible si no) |
| `RRF_K` | 60 | constante estándar (Cormack et al., 2009) |
| `PRIOR` | Beta(1, 1) | fuentes y tasa base |
| `MC_SAMPLES` / `MC_SEED` | 4000 / 20260930 | IC determinista |

### 4.2 Decisiones de diseño (para auditar)

- **`breakdown`** = pesos normalizados (suman 1, incluyen fuentes inactivas con su peso).
  **`max_individual_contribution`** = mayor fracción de `Σ|w·clip(LLR)|` aportada por una sola fuente
  (1.0 si hay una sola fuente activa). Adoptado por Dirección.
- Extra por fuente en `contributions`: `llr`, `llr_clipped`, `weight`, `weighted_llr` y `delta_p_loo`
  (cuánto cambia P si se quita la evidencia de esa fuente).
- **Fixed-share**: se implementa el paso de mezcla de Herbster-Warmuth sobre pesos derivados de las
  Beta, no la actualización exponencial por pérdida acumulada. Motivo: con fuentes que se abstienen
  y n < 20, la pérdida acumulada absoluta castiga a las fuentes que opinan más seguido. Queda como
  pregunta abierta para YANG.
- **Evento** que estima P: `final_verdict == 'ACIERTO'` en `_all_alerts.json` (label canónico actual).

## 5. Ejemplos con mints reales

Datos de Jupiter capturados 2026-09-30 00:15 UTC. Tasa base: 2 alertas cerradas, 0 aciertos → Beta(1, 3), media 0.25.
Trust: las 2 alertas cerradas (SI, OURA) no tienen snapshot previo → rechazadas → todas las fuentes en Beta(1, 1).
Con 1 de 5 fuentes activa, el peso de Jupiter es 0.2.

| Activo | Score alerta | Precio vs `initial_price` | LLR Jupiter (bruto) | Componentes ≠ 0 | P | IC 90% | ΔP Jupiter |
|---|---|---|---|---|---|---|---|
| **PARASITE** `8ed8xX8TVRDdeyyUwq7Kyo8VwxMWZ6c5J6ertxaBpump` | 65 | **+68.6%** | −0.50 | organicScore 0 (−0.75), 2195 holders (+0.25) | 0.2317 | [0.0158, 0.6183] | −0.018 |
| **USDF** `qDfLRLtPX5wLLXRV9CLRfHuH7kPEpw6q24Cwnzgpump` | 94 | **−100.0%** | −2.75 → recorte −2.0 | organicScore 0 (−0.75), 34 holders (−0.5), liquidez −99.99% (−1.5) | 0.1826 | [0.0113, 0.5477] | −0.067 |
| **Fartcoin** `9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump` | 82 | +8.9% | +0.57 | organicScore 88 (+0.57), 189k holders (+0.25), verificado (+0.25), top holders 33.6% (−0.25), buy share 1h 37.8% (−0.25) | 0.2720 | [0.0199, 0.6662] | +0.022 |

También en seguimiento activo: INUINK (−99.6%, LLR −1.28, P 0.205) y WOTF (−99.9%, LLR −2.75, P 0.1826).

**Lectura honesta:**
- El orden de las P coincide con lo que pasó, pero **no es evidencia predictiva**: los datos son
  posteriores a la emisión, y la regla de liquidez drenada detecta el rug una vez que ya ocurrió.
- PARASITE subió 68.6% y la heurística de `organicScore` lo penalizó. Los tokens pump.fun recién
  graduados suelen tener `organicScore` 0: puede ser un sesgo sistemático contra los tokens que el
  proyecto quiere detectar.
- Con 1 de 5 fuentes, P casi no se mueve de la base (|ΔP| ≤ 0.07) y el IC es muy ancho: la
  incertidumbre dominante es la tasa base con n = 2. **Es el comportamiento buscado**: sin evidencia
  no hay certeza.

**Salida para otra chain** (Base, BRETT `0x532f27101965dd16442E59d40670FaF5eBB142E4`) →
`signals/base/0x532f….json`. Jupiter queda en `sources_skipped` ("no aplica a chain 'base'"),
0/4 fuentes, sin historial → P = 0.5, IC [0.0487, 0.9505]: "no sabemos nada", declarado.

**Ejemplo sintético** con la forma del ejemplo de la directiva (6 fuentes, 4 activas, confianza no
uniforme). No son datos reales:
`P 0.4395, IC [0.2003, 0.6595], breakdown jupiter 0.277 · dexscreener 0.2266 · geckoterminal 0.1824 · madeonsol 0.1383 · three_ws 0.0878 · defillama 0.0878`.
El pool pesa 0.277 de Jupiter pero Jupiter aporta el **51%** de la evidencia (`max_individual_contribution` 0.5108).
No dominar en peso no es lo mismo que no dominar en evidencia.

**RRF sobre rankings reales de Jupiter** (`toptrending`, `toporganicscore`, `toptraded`, ventana 1h,
top 20 cada una, demo ad-hoc, no commiteada): 43 activos únicos; primeros STONK (ranks 2/12/2) y
ARTHUR (6/6/6). Aparecieron **dos tokens distintos con símbolo "SI"**, separados correctamente porque
la clave es `chain:mint`. Nunca indexar por símbolo.

## 6. Extensión a otros universos

### 6.1 Qué no cambia (invariantes)

- **Identidad** `(chain, mint)` y `asset_key = "chain:mint"` en todas las interfaces.
- **`lib_fusion` completo**: `fuse`, pesos, trust loop, IC y RRF no saben de chains, eventos ni fuentes.
- **Contrato de fuente**: cada fuente entrega `evidence.{fuente} = {llr_raw, label, components}`; la fusión solo lee `llr_raw`.
- **Salida**: `02_Analisis/signals/{chain}/{mint}.json`, schema 1.1, `chain` en la raíz, `field_provenance`.
- **Guardia anti look-ahead** y rehacer la confianza desde cero en cada corrida.

### 6.2 Qué cambia

| Aspecto | Universo C (hoy: memecoins Solana) | Universo A: BTC / ETH / SOL | Universo B: UNI / ICP / APT / PSG | Nuevas chains: Base / Blast / Monad |
|---|---|---|---|---|
| **Evento** que estima P | final_verdict (proxy de >20% en 24-48h) | otro umbral y horizonte (>20% en 48h es raro en majors) | narrativa: otro umbral y horizonte | igual que C |
| **Tasa base** | alertas cerradas de la chain | propia por universo | propia por universo | propia por chain (arranca en Beta(1,1)) |
| **Identidad** | mint base58 | activo nativo sin contrato → convención `mint = "native"` (hoy `MINT_RE` lo rechaza: hay que cambiarlo) | multi-deployment (UNI en varias chains) → falta un `asset_group` que agrupe deployments; ICP/APT nativos | 0x-hex (ya aceptado) |
| **Fuentes** | Jupiter + DEX multi-chain + GoPlus | métricas on-chain, flujos de ETF, opciones (a evaluar con las mismas restricciones de licencia y costo) | TVL de protocolo, gobernanza, actividad de desarrollo, noticias | GeckoTerminal / DexPaprika / DexScreener / GoPlus + un equivalente chain-specific de Jupiter (launchpad nativo, a evaluar) |
| **Alias de chain por fuente** | no aplica aún | por fuente | por fuente | GeckoTerminal usa ids propios (`eth`, `base`), GoPlus usa chain id numérico: hay que mapearlos en cada colector, no en `lib_fusion` |
| **Scope de la confianza** | por chain | por universo (la misma fuente puede ser buena en majors y mala en memes) | por universo | por chain |

**Lo concreto por hacer para abrir un universo o una chain nueva:**
1. Agregar sus fuentes a `SOURCE_REGISTRY` con `chains`.
2. Escribir el colector y el mapeo LLR de cada fuente nueva.
3. Definir el evento y su label de cierre.
4. Aplicar filtro de historial por universo además de por chain; hoy `build_history` filtra solo por chain.
5. Si hace falta, relajar `MINT_RE` (activos nativos).

`lib_fusion` no se toca.

## 7. Riesgos detectados

1. **Sin aprendizaje posible todavía**: el trust loop necesita el snapshot de señales **al momento de
   emitir**, y hoy nadie lo guarda. Si `script_97` no embebe `signals_snapshot` en la alerta, la
   confianza queda en Beta(1,1) para siempre (el contrato ya está implementado en `load_snapshot`).
2. **Heurísticas contra el objetivo**: `organicScore` penalizó al único token que subió (PARASITE).
3. **P poco informativa hoy**: 1/5 fuentes, tasa base con n = 2 → IC de ~0.6 de ancho. No usar para decidir.
4. **Label ambiguo**: OURA hizo +17,186% en t+1h y su `final_verdict` es FALSO POSITIVO. El evento que
   estima P (final_verdict) y el objetivo del proyecto (>20% en 24-48h) no son lo mismo.
5. **Trust loop del pipeline**: INUINK (−99.6%) y WOTF (−99.9%) siguen en `active_tracking`; WOTF no tiene
   ningún trust_update unas 7 h después de emitida (en la copia local; `origin/main` avanzó a `3d88015` y no fue revisado).
6. **Dominio de evidencia**: el piso y el tope limitan pesos, no evidencia. Lo reporta `max_individual_contribution`, pero nada lo limita.
7. **Pocas fuentes → tope ≈ 1/N**: con N = 3 el tope 0.35 anula casi toda diferenciación por confianza (test `test_cap_limits_differentiation_with_few_sources`).
8. **Jupiter sin key a 0.5 RPS**: ~2 s por activo (5 activos ≈ 10 s). Riesgo de que la API pase a exigir key (antecedente: `lite-api` deprecado).
9. **Ramas**: `main` local va 1 commit adelante (baseline) y `origin/main` avanzó con commits del cron. El push requiere rebase, y el baseline incluye cambios en workflows.
10. **Legado**: 7 archivos schema 1.0 (placeholders) en la raíz de `02_Analisis/signals/`. No se borraron.

## 8. Pendiente

- Colectores GeckoTerminal, DexPaprika, GoPlus y DexScreener en `script_112`, con sus mapeos LLR.
- `script_97`: campo `chain` en cada alerta y `signals_snapshot` al emitir.
- Workflow que corra `script_112` (hoy no está agendado).
- Integración de `fusion.probability` al scoring de `script_82` (paso posterior, requiere decisión de YANG).
- Calibrar reglas LLR y parámetros cuando haya ≥ 20 alertas cerradas.

## 9. Cómo ejecutar

```bash
python 04_Config/scripts/script_112_signal_aggregator.py --from-alerts --legacy-chain solana
python 04_Config/scripts/script_112_signal_aggregator.py --chain solana --mint <MINT> --legacy-chain solana
python 04_Config/scripts/script_112_signal_aggregator.py --chain base --mint <0x...> --dry-run
python 04_Config/scripts/test_lib_fusion.py
```

`--legacy-chain` indica a qué chain pertenecen las alertas de `_all_alerts.json` sin campo `chain`
(todas las actuales). Sin ese flag quedan fuera del historial y el script avisa. En Windows, usar
`PYTHONIOENCODING=utf-8` para ver bien los acentos en consola.
