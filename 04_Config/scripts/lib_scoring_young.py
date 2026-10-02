#!/usr/bin/env python3
"""
lib_scoring_young.py — Scorer de tokens jóvenes (< 60 min), D-014-R-3. Diseño: doc 32 v0.2.

Alcance: memecoins de Solana con par de < 60 min. Desde 60 min puntúa v7.2.1 (sin cambios). No toca multi-chain.

Ponderación (decisión de Dirección: para < 60 min la narrativa informacional es la fuente primaria):
  60 % informacionales  (lib_info_signals: narrativa, menciones, trending, metadata, perfil DexScreener, repo)
  25 % estructurales    (curva de bonding, holders, dev wallet; los kill switches cortan a 0)
  15 % precio/volumen   (lib_early_signals: las 5 señales que existen para un token joven, ahora complementarias)

score = Σ peso · s (0..100). Señal sin dato = 0 (conservador) y baja la cobertura, que se informa.
Emite si score >= YOUNG_THRESHOLD (40, D-014-R-5) Y el subtotal informacional >= INFO_MIN (10): sin evidencia
informacional no hay alerta, aunque la estructura y el flujo sumen. Liquidez 0 (curva de bonding) se acepta.
Variantes (A/B/C sobre precio/volumen, I sobre informacionales) se registran en el JSONL para comparar.
Parámetros heurísticos [H]; P-13: lo que no sirva al resultado se saca.
"""
import json
import os
from pathlib import Path

VERSION = "young-0.3"
SCOPE_MAX_AGE_MIN = 60
INFO_WEIGHTS = {"mentions": 15, "narrative_wave": 15, "trending_match": 10, "metadata_socials": 10,
                "dex_profile": 5, "github_repo": 5}                                   # 60
STRUCT_WEIGHTS = {"bonding_progress": 10, "holders_struct": 8, "dev_wallet": 7}       # 25
PRICE_WEIGHT = 15
PRICE_SIGNALS = {"volume_acceleration": 3, "buy_pressure_shift": 2, "quiet_accumulation": 3,
                 "liquidity_inflow": 2, "holder_accumulation": 2}                     # puntos máx. (lib_early_signals)
ELIGIBLE = tuple(PRICE_SIGNALS)
YOUNG_THRESHOLD = int(os.environ.get("YOUNG_THRESHOLD") or 40)   # D-014-R-5: 50 -> 40
INFO_MIN = 10                        # D-014-R-5: 20 -> 10
H0_INFO_SPLIT = 20                   # H-0 pre-registrada: info_score >= 20 vs < 20 (doc 32 §6)
MIN_HOLDERS = 50                     # [H] kill switch solo si RugCheck dio el dato
MAX_TOP10_PCT = 50.0                 # [H]
MAX_DEV_SUPPLY_PCT = 10.0            # [H]
PUMP_SUPPLY = 1_000_000_000
STRONG_S = 0.5
VARIANT_C_POINTS = 4.0
LOG_DELTA = 5                        # se registra una línea nueva cuando el score cambia >= 5 (o al emitir)


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


def score_young_detail(token_data, signals, signals_info=None, now_s=None, rug=None, structural=None):
    """Detalle completo: score, partes, cobertura, filtros, variantes, razones. score None = fuera de alcance.
    structural: señales estructurales ya calculadas (lib_info_signals: bonding_progress, holders_struct,
    dev_wallet); si faltan, el caller no las tenía."""
    import time
    now_s = time.time() if now_s is None else now_s
    dx = (token_data or {}).get("dexscreener") or {}
    age = age_minutes(dx, now_s)
    if age is None or age >= SCOPE_MAX_AGE_MIN:
        why = "edad desconocida" if age is None else f"edad {age:.1f} min >= {SCOPE_MAX_AGE_MIN} (lo puntúa v7.2.1)"
        return {"score": None, "reasons": [f"fuera de alcance: {why}"], "age_min": age}
    info = _by_name(signals_info, INFO_WEIGHTS)
    struct = _by_name(structural, STRUCT_WEIGHTS)
    price = active_signals(signals)
    parts = {"info": sum(w * (info[n]["s"] if n in info else 0) for n, w in INFO_WEIGHTS.items()),
             "struct": sum(w * (struct[n]["s"] if n in struct else 0) for n, w in STRUCT_WEIGHTS.items()),
             "price": PRICE_WEIGHT * sum(min(s.get("points") or 0, PRICE_SIGNALS[n]) for n, s in price.items())
             / sum(PRICE_SIGNALS.values())}
    covered = (sum(w for n, w in INFO_WEIGHTS.items() if n in info)
               + sum(w for n, w in STRUCT_WEIGHTS.items() if n in struct)
               + PRICE_WEIGHT * (1 if _by_name(signals, PRICE_SIGNALS) else 0))
    raw = int(round(sum(parts.values())))
    reasons = [f"{VERSION} · edad {age:.1f} min · info {parts['info']:.1f}/60 · estructura {parts['struct']:.1f}/25 · "
               f"precio/volumen {parts['price']:.1f}/15 · cobertura {covered}/100"]
    for group, sigs, weights in (("info", info, INFO_WEIGHTS), ("estructura", struct, STRUCT_WEIGHTS)):
        for n, s in sigs.items():
            if s["s"] > 0:
                reasons.append(f"[{group}] {n}: {s.get('detail', '')} → +{weights[n] * s['s']:.1f}")
    for n, s in price.items():
        reasons.append(f"[precio/volumen] {n}: {s.get('detail', '')} (s {s['s']:.2f})")
    blocks = kill_switches(token_data, rug, age)
    score = 0 if blocks else raw
    reasons += [f"FILTRO: {b}" for b in blocks] + ([f"(sin filtros sería {raw})"] if blocks else [])
    fire = score >= YOUNG_THRESHOLD and parts["info"] >= INFO_MIN
    reasons.append(f"score {score} (umbral {YOUNG_THRESHOLD}, info mínima {INFO_MIN}) → "
                   + ("EMITE" if fire else "no emite"))
    return {"score": score, "raw": raw, "parts": {k: round(v, 2) for k, v in parts.items()},
            "info_score": round(parts["info"], 2), "struct_score": round(parts["struct"], 2),
            "pv_score": round(parts["price"], 2), "h0_group": "info_ge20" if parts["info"] >= H0_INFO_SPLIT else "info_lt20",
            "coverage": covered,
            "blocks": blocks, "fires": fire, "variants": variants(signals, signals_info), "reasons": reasons,
            "age_min": round(age, 1), "variant": VERSION}


def score_young(token_data, signals, signals_info=None, now_s=None, rug=None, structural=None):
    """(score 0..100 | None, reasons). None = fuera de alcance (edad >= 60 min o desconocida)."""
    d = score_young_detail(token_data, signals, signals_info, now_s, rug, structural)
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
