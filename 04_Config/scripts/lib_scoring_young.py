#!/usr/bin/env python3
"""
lib_scoring_young.py — Scorer de tokens jóvenes (< 60 min). v0.4 (D-023-R3). Diseño: doc 32 v0.4.

Alcance en producción: memecoins de Solana con par de < 60 min (script_116). Desde 60 min sigue v7.2.1 (+ bono);
v7.2.2 (bono informacional) está propuesto, no implementado (doc 32 §7).

Marco (Dirección, D-023-R3): los grupos de señales nunca se sustituyen, siempre se combinan; la edad ajusta los
pesos, nunca elimina un grupo (ningún grupo baja de 15); lo informacional también anticipa en activos maduros; la
liquidez inicial no filtra: es un flag informativo.

Pesos de grupo continuos por edad (weights_for_age, interpolación lineal entre cortes):
    edad      0 min   10 min  30 min  60 min  6 h   24 h (y más)
    info       70      60      50      40     30     20
    estruct    15      20      25      25     25     20
    precio     15      20      25      35     45     60
Dentro de cada grupo, pesos relativos fijos: INFO_WEIGHTS, STRUCT_WEIGHTS, PRICE_SIGNALS.
score = Σ_grupo W_grupo(edad) · Σ_i w_i·s_i / Σ_i w_i   (0..100). Señal sin dato = 0 y baja la cobertura.
Emite si score >= 40 Y subtotal informacional >= 5 (D-023-R3: un mínimo bajo para no bloquear regímenes en que la
información falta legítimamente). Kill switches cortan a 0. Parámetros heurísticos [H]; P-13 los revisa.
"""
import json
import os
from pathlib import Path

VERSION = "young-0.4"
SCOPE_MAX_AGE_MIN = 60
# Pesos de grupo por edad (minutos): (edad, info, estructural, precio/volumen). Cada fila suma 100, mínimo 15.
AGE_ANCHORS = ((0, 70, 15, 15), (10, 60, 20, 20), (30, 50, 25, 25), (60, 40, 25, 35), (360, 30, 25, 45),
               (1440, 20, 20, 60))
# Pesos relativos dentro de cada grupo
INFO_WEIGHTS = {"mentions": 15, "narrative_wave": 15, "trending_match": 10, "metadata_socials": 10,
                "dex_profile": 5, "github_repo": 5}
STRUCT_WEIGHTS = {"bonding_progress": 12, "holders_struct": 6, "dev_wallet": 3,            # D-023-R3 T2
                  "bonding_curve_velocity": 1, "unique_buyer_acceleration": 1, "avg_buy_size_trend": 1,
                  "holder_to_txn_ratio": 1}
PRICE_SIGNALS = {"volume_acceleration": 3, "buy_pressure_shift": 2, "quiet_accumulation": 3,
                 "liquidity_inflow": 2, "holder_accumulation": 2}                     # puntos máx. (lib_early_signals)
ELIGIBLE = tuple(PRICE_SIGNALS)
INFO_FLAGS = ("initial_liquidity_usd",)                  # flag informativo del grupo estructural: peso 0
YOUNG_THRESHOLD = int(os.environ.get("YOUNG_THRESHOLD") or 40)
INFO_MIN = 5                         # D-023-R3: 10 -> 5
H0_INFO_SPLIT = 20                   # H-0 pre-registrada: info_score >= 20 vs < 20 (doc 32 §6)
MIN_HOLDERS = 50                     # [H] kill switch solo si RugCheck dio el dato
MAX_TOP10_PCT = 50.0                 # [H]
MAX_DEV_SUPPLY_PCT = 10.0            # [H]
PUMP_SUPPLY = 1_000_000_000
STRONG_S = 0.5
VARIANT_C_POINTS = 4.0
LOG_DELTA = 5                        # se registra una línea nueva cuando el score cambia >= 5 (o al emitir)


def weights_for_age(age_min):
    """{"info", "struct", "pv"} para una edad en minutos: interpolación lineal entre los cortes de AGE_ANCHORS.
    Antes del primer corte y después del último, constante. Suma 100; ningún grupo baja de 15."""
    a = max(0.0, float(age_min or 0.0))
    if a >= AGE_ANCHORS[-1][0]:
        _, i, st, pv = AGE_ANCHORS[-1]
        return {"info": float(i), "struct": float(st), "pv": float(pv)}
    for (a0, i0, s0, p0), (a1, i1, s1, p1) in zip(AGE_ANCHORS, AGE_ANCHORS[1:]):
        if a0 <= a < a1:
            f = (a - a0) / (a1 - a0)
            return {"info": i0 + f * (i1 - i0), "struct": s0 + f * (s1 - s0), "pv": p0 + f * (p1 - p0)}
    _, i, st, pv = AGE_ANCHORS[0]
    return {"info": float(i), "struct": float(st), "pv": float(pv)}


def _num(x):
    if x is None or isinstance(x, bool):
        return None
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def age_minutes(dx, now_s):
    created = _num((dx or {}).get("pairCreatedAt"))
    if not created or created <= 0:
        return None
    return (now_s - created / 1000) / 60


def kill_switches(token_data, rug=None, age_min=None):
    """Filtros de corte con datos existentes. [motivos]; vacío = pasa."""
    out = []
    dx = (token_data or {}).get("dexscreener") or {}
    tok = (token_data or {}).get("token") or {}
    change = _num(dx.get("priceChange24h"))
    if age_min is not None and age_min < 5 and change is not None and change > 10_000:
        out.append("kill switch de script_82: edad < 5 min y cambio 24 h > 10.000 %")
    rug = rug or {}
    if rug.get("mint_authority"):
        out.append("mint authority activa (RugCheck)")
    if rug.get("freeze_authority"):
        out.append("freeze authority activa (RugCheck)")
    top10 = _num(rug.get("top10_pct"))
    if top10 is not None and top10 > MAX_TOP10_PCT:
        out.append(f"top-10 holders {top10:.1f} % > {MAX_TOP10_PCT:.0f} %")
    holders = _num(rug.get("holders"))
    if holders is not None and holders < MIN_HOLDERS:
        out.append(f"holders {holders:.0f} < {MIN_HOLDERS}")
    dev = _num(tok.get("initialBuy"))
    if dev is not None and dev > 0 and 100 * dev / PUMP_SUPPLY > MAX_DEV_SUPPLY_PCT:
        out.append(f"compra inicial del creador {100 * dev / PUMP_SUPPLY:.1f} % del supply > {MAX_DEV_SUPPLY_PCT:.0f} %")
    creator_pct = _num(rug.get("creator_pct"))
    if creator_pct is not None and creator_pct > MAX_DEV_SUPPLY_PCT:
        out.append(f"creador con {creator_pct:.1f} % del supply (RugCheck) > {MAX_DEV_SUPPLY_PCT:.0f} %")
    return out


def _by_name(signals, names):
    return {s["name"]: s for s in signals or [] if s and s.get("name") in names}


def active_signals(signals):
    """Señales de precio/volumen elegibles con s > 0."""
    return {n: s for n, s in _by_name(signals, PRICE_SIGNALS).items() if (s.get("s") or 0) > 0}


def variants(signals, signals_info=None):
    act = active_signals(signals)
    info_act = [s for s in _by_name(signals_info, INFO_WEIGHTS).values() if (s.get("s") or 0) > 0]
    return {"A_ge3_active": len(act) >= 3,
            "B_ge3_strong": sum(1 for s in act.values() if s["s"] >= STRONG_S) >= 3,
            "C_points_ge4": sum(s.get("points") or 0 for s in act.values()) >= VARIANT_C_POINTS,
            "I_ge2_info": len(info_act) >= 2}


def score_young_detail(token_data, signals, signals_info=None, now_s=None, rug=None, structural=None, flags=None):
    """Detalle completo: score, partes, pesos por edad, cobertura, filtros, variantes, razones. score None = fuera
    de alcance. structural: señales estructurales (lib_info_signals). flags: datos informativos que no suman
    (tradability: tradable, liquidity_usd, buy_route, initial_liquidity_usd)."""
    import time
    now_s = time.time() if now_s is None else now_s
    dx = (token_data or {}).get("dexscreener") or {}
    age = age_minutes(dx, now_s)
    if age is None or age >= SCOPE_MAX_AGE_MIN:
        why = "edad desconocida" if age is None else f"edad {age:.1f} min >= {SCOPE_MAX_AGE_MIN} (lo puntúa v7.2.1)"
        return {"score": None, "reasons": [f"fuera de alcance: {why}"], "age_min": age}
    W = weights_for_age(age)
    info = _by_name(signals_info, INFO_WEIGHTS)
    struct = _by_name(structural, STRUCT_WEIGHTS)
    price = active_signals(signals)
    si, ss, sp = sum(INFO_WEIGHTS.values()), sum(STRUCT_WEIGHTS.values()), sum(PRICE_SIGNALS.values())
    parts = {"info": W["info"] * sum(w * (info[n]["s"] if n in info else 0) for n, w in INFO_WEIGHTS.items()) / si,
             "struct": W["struct"] * sum(w * (struct[n]["s"] if n in struct else 0)
                                         for n, w in STRUCT_WEIGHTS.items()) / ss,
             "price": W["pv"] * sum(min(s.get("points") or 0, PRICE_SIGNALS[n]) for n, s in price.items()) / sp}
    covered = (W["info"] * sum(w for n, w in INFO_WEIGHTS.items() if n in info) / si
               + W["struct"] * sum(w for n, w in STRUCT_WEIGHTS.items() if n in struct) / ss
               + W["pv"] * (1 if _by_name(signals, PRICE_SIGNALS) else 0))
    raw = int(round(sum(parts.values())))
    reasons = [f"{VERSION} · edad {age:.1f} min · pesos info {W['info']:.0f} / estructura {W['struct']:.0f} / "
               f"precio {W['pv']:.0f} · info {parts['info']:.1f} · estructura {parts['struct']:.1f} · "
               f"precio/volumen {parts['price']:.1f} · cobertura {covered:.0f}/100"]
    for group, sigs, weights, wg, tot in (("info", info, INFO_WEIGHTS, W["info"], si),
                                          ("estructura", struct, STRUCT_WEIGHTS, W["struct"], ss)):
        for n, s in sigs.items():
            if s["s"] > 0:
                reasons.append(f"[{group}] {n}: {s.get('detail', '')} → +{wg * weights[n] * s['s'] / tot:.1f}")
    for n, s in price.items():
        reasons.append(f"[precio/volumen] {n}: {s.get('detail', '')} (s {s['s']:.2f})")
    flags = dict(flags or {})
    if flags:
        reasons.append("[flag, no suma] " + ", ".join(f"{k}={v}" for k, v in flags.items()))
    blocks = kill_switches(token_data, rug, age)
    score = 0 if blocks else raw
    reasons += [f"FILTRO: {b}" for b in blocks] + ([f"(sin filtros sería {raw})"] if blocks else [])
    fire = score >= YOUNG_THRESHOLD and parts["info"] >= INFO_MIN
    reasons.append(f"score {score} (umbral {YOUNG_THRESHOLD}, info mínima {INFO_MIN}) → "
                   + ("EMITE" if fire else "no emite"))
    return {"score": score, "raw": raw, "parts": {k: round(v, 2) for k, v in parts.items()},
            "weights": {k: round(v, 2) for k, v in W.items()},
            "info_score": round(parts["info"], 2), "struct_score": round(parts["struct"], 2),
            "pv_score": round(parts["price"], 2), "h0_group": "info_ge20" if parts["info"] >= H0_INFO_SPLIT else "info_lt20",
            "coverage": round(covered, 1), "flags": flags,
            "blocks": blocks, "fires": fire, "variants": variants(signals, signals_info), "reasons": reasons,
            "age_min": round(age, 1), "variant": VERSION}


def score_young(token_data, signals, signals_info=None, now_s=None, rug=None, structural=None, flags=None):
    """(score 0..100 | None, reasons). None = fuera de alcance (edad >= 60 min o desconocida)."""
    d = score_young_detail(token_data, signals, signals_info, now_s, rug, structural, flags)
    return d["score"], d["reasons"]


def fires(detail_or_score, info_part=None):
    """Decisión de emisión. Acepta el detalle de score_young_detail o (score, subtotal informacional)."""
    if isinstance(detail_or_score, dict):
        return bool(detail_or_score.get("fires"))
    return (detail_or_score is not None and detail_or_score >= YOUNG_THRESHOLD
            and (info_part or 0) >= INFO_MIN)


# ---------------------------------------------------------------------------
# Registro JSONL por token
# ---------------------------------------------------------------------------

def should_log(last_logged_score, detail, emitted=False):
    """Primera vez, cambio de score >= LOG_DELTA, o emisión."""
    if detail.get("score") is None:
        return False
    return emitted or last_logged_score is None or abs(detail["score"] - last_logged_score) >= LOG_DELTA


def young_record(mint, symbol, detail, signals, signals_info, structural, now_iso, instance, emitted=False):
    def slim(sigs):
        return {s["name"]: s["s"] for s in sigs or [] if s}
    return {"at": now_iso, "mint": mint, "symbol": symbol, "instance": instance, "version": VERSION,
            "age_min": detail.get("age_min"), "score": detail.get("score"), "raw": detail.get("raw"),
            "info_score": detail.get("info_score"), "struct_score": detail.get("struct_score"),
            "pv_score": detail.get("pv_score"), "h0_group": detail.get("h0_group"),
            "weights": detail.get("weights"), "flags": detail.get("flags"),
            "parts": detail.get("parts"), "coverage": detail.get("coverage"), "fires": detail.get("fires"),
            "emitted": emitted, "blocks": detail.get("blocks"), "variants": detail.get("variants"),
            "variant": detail.get("variant"), "signals_info": slim(signals_info), "structural": slim(structural),
            "signals": slim(signals)}


def append_jsonl(path, record):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
    return path
