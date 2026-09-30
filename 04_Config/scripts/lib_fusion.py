#!/usr/bin/env python3
"""
lib_fusion.py — Fusión multimodal sin priorización (Capítulo II, Proyecto Shot de Mercado).

Agnóstico a chain: `chain` y `mint` son identificadores opacos que solo se propagan a la
salida. Ninguna función asume una chain, un formato de dirección ni un conjunto fijo de
fuentes. Solo biblioteca estándar.

Modelo
------
    P = logit⁻¹( base + Σ_s w_s · clip(LLR_s, ±c) )

1. Priors iguales: la confiabilidad de cada fuente arranca en r_s ~ Beta(1, 1).
2. Trust loop: cada alerta cerrada suma 1 a alpha (la fuente acertó la dirección del
   resultado) o a beta (falló). Solo cuentan señales capturadas ANTES de la alerta
   (guardia anti look-ahead). Fuentes sin evidencia o con LLR = 0 no se actualizan.
3. Pesos: w_s ∝ E[r_s]; mezcla fixed-share de Herbster & Warmuth (1998):
   w ← (1 − γ)·w + γ/N, que garantiza un piso γ/N a cada fuente; luego tope w_s ≤ w_max
   (redistribuyendo el exceso). Σ w = 1: es un pool logarítmico, así la evidencia
   correlacionada no se suma dos veces, y una fuente registrada sin datos aporta LLR = 0,
   lo que encoge P hacia la tasa base (sin evidencia no hay certeza).
   Nota: se usa el paso de mezcla de fixed-share sobre pesos derivados de las Beta, no la
   actualización exponencial completa por pérdida acumulada (ver 16_CAPITULO_II_MULTIMODAL.md).
4. base = logit(tasa base), con tasa base ~ Beta(1 + aciertos, 1 + fallos) de alertas cerradas.
5. IC 90%: Monte Carlo muestreando r_s y la tasa base de sus Beta, con semilla fija.
6. RRF (Cormack, Clarke & Büttcher, 2009): score(d) = Σ_listas 1 / (k + rank_lista(d)),
   para combinar rankings de trending sin normalizar escalas.

Parámetros — TODOS HEURÍSTICOS NO CALIBRADOS (n < 20 alertas cerradas):
    LLR_CLIP          = 2.0     recorte ±c por fuente, en nats (razón de verosimilitud máx ≈ 7.4)
    FIXED_SHARE_GAMMA = 0.3     fracción repartida en partes iguales (piso = γ/N)
    MAX_WEIGHT        = 0.35    tope de peso individual (si 1/N > tope, se usa 1/N)
    RRF_K             = 60      constante estándar de RRF
    PRIOR             = (1, 1)  Beta uniforme para fuentes y tasa base
    MC_SAMPLES        = 4000    muestras Monte Carlo para el IC
    MC_SEED           = 20260930
"""
import math
import random
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

LLR_CLIP = 2.0
FIXED_SHARE_GAMMA = 0.3
MAX_WEIGHT = 0.35
RRF_K = 60
PRIOR = (1.0, 1.0)
MC_SAMPLES = 4000
MC_SEED = 20260930
CI_LEVEL = 0.90
LABEL = "HEURISTICA_NO_CALIBRADA"

_P_EPS = 1e-12


# ---------------------------------------------------------------------------
# Primitivas
# ---------------------------------------------------------------------------

def logit(p: float) -> float:
    p = min(max(p, _P_EPS), 1.0 - _P_EPS)
    return math.log(p / (1.0 - p))


def inv_logit(x: float) -> float:
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    z = math.exp(x)
    return z / (1.0 + z)


def clip(x: float, c: float = LLR_CLIP) -> float:
    return max(-c, min(c, x))


def asset_key(chain: str, mint: str) -> str:
    """Identificador único de un activo entre chains (para RRF y registros)."""
    return f"{chain}:{mint}"


def _clean_llr(value: Any) -> Optional[float]:
    """None/NaN/no numérico = fuente sin evidencia. ±inf se acepta (lo resuelve el recorte)."""
    if value is None or isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    if math.isnan(value):
        return None
    return float(value)


def _normalize(weights: Sequence[float]) -> List[float]:
    total = sum(weights)
    if not weights:
        return []
    if total <= 0:
        return [1.0 / len(weights)] * len(weights)
    return [w / total for w in weights]


def _quantile(sorted_values: Sequence[float], q: float) -> float:
    pos = q * (len(sorted_values) - 1)
    lo, hi = math.floor(pos), math.ceil(pos)
    return sorted_values[lo] + (sorted_values[hi] - sorted_values[lo]) * (pos - lo)


# ---------------------------------------------------------------------------
# Pesos: confiabilidad Beta → fixed-share → tope
# ---------------------------------------------------------------------------

def default_trust(sources: Iterable[str], prior: Tuple[float, float] = PRIOR) -> Dict[str, Dict[str, float]]:
    """Priors iguales: Beta(prior) para cada fuente."""
    return {s: {"alpha": prior[0], "beta": prior[1]} for s in sources}


def fixed_share(weights: Sequence[float], gamma: float = FIXED_SHARE_GAMMA) -> List[float]:
    """Mezcla fixed-share: (1 − γ)·w + γ/N. Cada peso queda ≥ γ/N."""
    w = _normalize(weights)
    n = len(w)
    return [(1.0 - gamma) * wi + gamma / n for wi in w]


def cap_weights(weights: Sequence[float], max_weight: float = MAX_WEIGHT) -> List[float]:
    """Tope por fuente con redistribución proporcional del exceso (water-filling).

    Si max_weight < 1/N el tope es infactible (los pesos deben sumar 1) y se usa 1/N.
    El exceso solo se suma a pesos no topeados, así que los pisos se preservan.
    """
    w = _normalize(weights)
    n = len(w)
    if n == 0:
        return []
    cap = max(max_weight, 1.0 / n)
    fixed = [False] * n
    while True:
        over = [i for i in range(n) if not fixed[i] and w[i] > cap + 1e-12]
        if not over:
            return w
        for i in over:
            w[i], fixed[i] = cap, True
        free = [i for i in range(n) if not fixed[i]]
        if not free:
            return w
        remaining = 1.0 - cap * (n - len(free))
        free_total = sum(w[i] for i in free)
        for i in free:
            w[i] = (w[i] / free_total if free_total > 0 else 1.0 / len(free)) * remaining


def reliability(trust: Mapping[str, Mapping[str, float]], source: str,
                prior: Tuple[float, float] = PRIOR) -> Tuple[float, float]:
    t = trust.get(source) or {}
    return float(t.get("alpha", prior[0])), float(t.get("beta", prior[1]))


def source_weights(sources: Sequence[str], trust: Optional[Mapping[str, Mapping[str, float]]] = None,
                   gamma: float = FIXED_SHARE_GAMMA, max_weight: float = MAX_WEIGHT,
                   reliabilities: Optional[Sequence[float]] = None) -> Dict[str, float]:
    """Pesos normalizados por fuente. `reliabilities` permite inyectar muestras (Monte Carlo)."""
    if not sources:
        return {}
    if reliabilities is None:
        trust = trust or {}
        reliabilities = []
        for s in sources:
            a, b = reliability(trust, s)
            reliabilities.append(a / (a + b))
    return dict(zip(sources, cap_weights(fixed_share(reliabilities, gamma), max_weight)))


# ---------------------------------------------------------------------------
# Tasa base y trust loop
# ---------------------------------------------------------------------------

def base_rate_posterior(outcomes: Iterable[bool], prior: Tuple[float, float] = PRIOR) -> Tuple[float, float]:
    """Beta(prior + aciertos, prior + fallos) a partir de resultados de alertas cerradas."""
    outcomes = list(outcomes)
    hits = sum(1 for o in outcomes if o)
    return prior[0] + hits, prior[1] + len(outcomes) - hits


def update_trust(trust: Mapping[str, Mapping[str, float]], llrs: Mapping[str, Any], outcome: bool,
                 prior: Tuple[float, float] = PRIOR, eps: float = 1e-9) -> Dict[str, Dict[str, float]]:
    """Actualiza la confiabilidad de cada fuente con una alerta cerrada. No muta `trust`.

    La fuente acierta si el signo de su LLR coincide con el resultado (LLR > 0 y acierto,
    o LLR < 0 y fallo). Fuentes sin evidencia o con |LLR| ≤ eps no se actualizan.
    """
    new = {s: {"alpha": float(v.get("alpha", prior[0])), "beta": float(v.get("beta", prior[1]))}
           for s, v in trust.items()}
    for source, raw in llrs.items():
        llr = _clean_llr(raw)
        if llr is None or abs(llr) <= eps:
            continue
        t = new.setdefault(source, {"alpha": prior[0], "beta": prior[1]})
        if (llr > 0) == bool(outcome):
            t["alpha"] += 1.0
        else:
            t["beta"] += 1.0
    return new


def replay_trust(sources: Iterable[str], records: Iterable[Mapping[str, Any]],
                 prior: Tuple[float, float] = PRIOR) -> Tuple[Dict[str, Dict[str, float]], Dict[str, Any]]:
    """Reconstruye la confiabilidad desde cero a partir de alertas cerradas (idempotente).

    Cada registro: {"id", "alert_ts" (epoch s), "snapshot_ts" (epoch s | None),
                    "llrs" {fuente: LLR}, "outcome" bool}.
    Guardia anti look-ahead: solo se aplica si snapshot_ts ≤ alert_ts.
    """
    trust = default_trust(sources, prior)
    stats: Dict[str, Any] = {"applied": 0, "rejected": []}
    for rec in records:
        snap, alert = rec.get("snapshot_ts"), rec.get("alert_ts")
        if snap is None or alert is None:
            stats["rejected"].append({"id": rec.get("id"), "reason": "sin snapshot de señales"})
            continue
        if snap > alert:
            stats["rejected"].append({"id": rec.get("id"),
                                      "reason": "look-ahead: señales capturadas después de la alerta"})
            continue
        known = {s: v for s, v in (rec.get("llrs") or {}).items() if s in trust}
        trust = update_trust(trust, known, rec["outcome"], prior)
        stats["applied"] += 1
    return trust, stats


# ---------------------------------------------------------------------------
# Fusión
# ---------------------------------------------------------------------------

def _pooled_logodds(base_logodds: float, weights: Mapping[str, float],
                    clipped: Mapping[str, Optional[float]]) -> float:
    return base_logodds + sum(weights[s] * c for s, c in clipped.items() if c is not None)


def fuse(chain: str, mint: str, sources: Mapping[str, Any],
         trust: Optional[Mapping[str, Mapping[str, float]]] = None,
         base_prior: Tuple[float, float] = PRIOR, *,
         llr_clip: float = LLR_CLIP, gamma: float = FIXED_SHARE_GAMMA,
         max_weight: float = MAX_WEIGHT, mc_samples: int = MC_SAMPLES,
         seed: int = MC_SEED) -> Dict[str, Any]:
    """Probabilidad fusionada para un activo.

    chain, mint: identificadores opacos (se devuelven tal cual).
    sources:     {fuente: LLR | None}. Todas las fuentes registradas para la chain;
                 None = registrada pero sin evidencia (cuenta en sources_total).
    trust:       {fuente: {"alpha", "beta"}}; faltantes = prior Beta(1, 1).
    base_prior:  (a, b) de la tasa base, p.ej. base_rate_posterior(resultados).
    """
    if not isinstance(chain, str) or not chain or not isinstance(mint, str) or not mint:
        raise ValueError("chain y mint deben ser strings no vacíos")
    names = list(sources)
    trust = trust or {}
    llrs = {s: _clean_llr(sources[s]) for s in names}
    clipped = {s: (None if v is None else clip(v, llr_clip)) for s, v in llrs.items()}

    a0, b0 = base_prior
    base_mean = a0 / (a0 + b0)
    base_lo = logit(base_mean)
    weights = source_weights(names, trust, gamma, max_weight)
    x = _pooled_logodds(base_lo, weights, clipped)
    p = inv_logit(x)

    weighted = {s: (weights[s] * c if c is not None else 0.0) for s, c in clipped.items()}
    total_abs = sum(abs(v) for v in weighted.values())
    contributions = {
        s: {
            "llr": llrs[s],
            "llr_clipped": clipped[s],
            "weight": round(weights[s], 4),
            "weighted_llr": round(weighted[s], 4),
            "delta_p_loo": round(p - inv_logit(x - weighted[s]), 4),
        }
        for s in names
    }

    # IC por Monte Carlo sobre la incertidumbre de la tasa base y de la confiabilidad de cada fuente
    rng = random.Random(seed)
    betas = [reliability(trust, s) for s in names]
    samples = []
    for _ in range(max(mc_samples, 2)):
        base_s = logit(rng.betavariate(a0, b0))
        rel = [rng.betavariate(a, b) for a, b in betas]
        w_s = source_weights(names, gamma=gamma, max_weight=max_weight, reliabilities=rel) if names else {}
        samples.append(inv_logit(_pooled_logodds(base_s, w_s, clipped)))
    samples.sort()
    tail = (1.0 - CI_LEVEL) / 2.0

    return {
        "chain": chain,
        "mint": mint,
        "asset": asset_key(chain, mint),
        "probability": round(p, 4),
        "ci_90": [round(_quantile(samples, tail), 4), round(_quantile(samples, 1.0 - tail), 4)],
        "sources_active": sum(1 for v in llrs.values() if v is not None),
        "sources_total": len(names),
        "max_individual_contribution": round(max(abs(v) for v in weighted.values()) / total_abs, 4)
                                       if total_abs > 0 else 0.0,
        "breakdown": {s: round(w, 4) for s, w in weights.items()},
        "contributions": contributions,
        "base_rate": {"mean": round(base_mean, 4), "alpha": a0, "beta": b0},
        "trust": {s: {"alpha": a, "beta": b, "mean": round(a / (a + b), 4)}
                  for s, (a, b) in zip(names, betas)},
        "params": {"llr_clip": llr_clip, "fixed_share_gamma": gamma, "max_weight": max_weight,
                   "mc_samples": mc_samples, "mc_seed": seed, "ci_level": CI_LEVEL},
        "label": LABEL,
    }


# ---------------------------------------------------------------------------
# Reciprocal Rank Fusion
# ---------------------------------------------------------------------------

def rrf(rankings: Mapping[str, Sequence[str]], k: float = RRF_K) -> List[Dict[str, Any]]:
    """Combina rankings: score(d) = Σ_listas 1 / (k + rank). Rank empieza en 1.

    rankings: {nombre_lista: [item, ...]} en orden de mejor a peor. Para mezclar chains,
    usar asset_key(chain, mint) como item. Un item repetido en una lista cuenta una vez
    (su mejor posición). Empates se ordenan por item para que la salida sea determinista.
    """
    scores: Dict[str, float] = {}
    ranks: Dict[str, Dict[str, int]] = {}
    for list_name, items in rankings.items():
        seen = set()
        for rank, item in enumerate(items, start=1):
            if item in seen:
                continue
            seen.add(item)
            scores[item] = scores.get(item, 0.0) + 1.0 / (k + rank)
            ranks.setdefault(item, {})[list_name] = rank
    ordered = sorted(scores, key=lambda it: (-scores[it], it))
    return [{"item": it, "rrf_score": round(scores[it], 6), "ranks": ranks[it]} for it in ordered]
