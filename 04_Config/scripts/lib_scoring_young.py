#!/usr/bin/env python3
"""
lib_scoring_young.py — Scorer de tokens jóvenes (< 60 min), Fase 12 MVP / D-014-R. BORRADOR AISLADO.

No está integrado a script_116 ni a script_97: solo el módulo y sus tests. Diseño: doc 32.

Alcance: memecoins de Solana con par de < 60 min. No reemplaza v7.2.1 (tokens maduros) ni toca multi-chain.
Features: solo señales de lib_early_signals + filtros estructurales (liquidez, holders, kill switches, dev wallet).

Señales elegibles (las que pueden activarse en un token joven de Solana; ver doc 32 §1):
  volume_acceleration, buy_pressure_shift, quiet_accumulation, liquidity_inflow, holder_accumulation.
Excluidas: orderbook_imbalance, funding_squeeze, clmm_imbalance (no existen para un pool pump/CPMM),
fear_greed_extreme (es igual para todos los tokens del momento: no separa uno de otro) y social_velocity (script_115
no sigue lanzamientos en vivo: 0 activaciones en 4 h de producción).

Score = 20 × señales elegibles activas (s > 0), 0..100, solo si pasan los filtros; con un filtro fallido, 0.
Umbral YOUNG_THRESHOLD = 60 (≡ >= 3 señales activas), más liquidez > $20K y sin kill switches (candidato de la
directiva). Las variantes B y C se calculan para registrarlas en sombra y compararlas walk-forward.
Parámetros heurísticos [H]; nada está calibrado (no hay outcome todavía).
"""
VERSION = "young-0.1"
SCOPE_MAX_AGE_MIN = 60
ELIGIBLE = ("volume_acceleration", "buy_pressure_shift", "quiet_accumulation", "liquidity_inflow",
            "holder_accumulation")
POINTS_PER_SIGNAL = 20
YOUNG_THRESHOLD = 60                 # >= 3 señales activas
LIQ_MIN_USD = 20_000
MIN_HOLDERS = 50                     # [H] solo si RugCheck dio el dato
MAX_TOP10_PCT = 50.0                 # [H] concentración máxima de los 10 mayores holders
MAX_DEV_SUPPLY_PCT = 10.0            # [H] compra inicial del creador sobre el supply (pump.fun: 1e9)
PUMP_SUPPLY = 1_000_000_000
STRONG_S = 0.5                       # variante B: señales "fuertes"
VARIANT_C_POINTS = 4.0               # variante C: suma de puntos de lib_early_signals


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
    """Filtros de corte con datos que el sistema ya tiene. Devuelve [motivos]; vacío = pasa.
    token_data: {"token": evento de PumpPortal, "dexscreener": par aplanado (formato script_82)}.
    rug: snapshot de RugCheck (lib_early_signals.rugcheck_snapshot + campos mint/freeze/creador si los hay)."""
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


def active_signals(signals):
    """{nombre: señal} de las elegibles con s > 0 (signals: lista de lib_early_signals, con None posibles)."""
    return {s["name"]: s for s in signals or [] if s and s.get("name") in ELIGIBLE and (s.get("s") or 0) > 0}


def variants(signals):
    """Las tres reglas que se registran en sombra (doc 32 §2). Solo señales; los filtros van aparte."""
    act = active_signals(signals)
    return {"A_ge3_active": len(act) >= 3,
            "B_ge3_strong": sum(1 for s in act.values() if s["s"] >= STRONG_S) >= 3,
            "C_points_ge4": sum(s.get("points") or 0 for s in act.values()) >= VARIANT_C_POINTS}


def score_young(token_data, signals, now_s=None, rug=None):
    """(score 0..100 | None, reasons). None = fuera de alcance (edad >= 60 min o desconocida).
    Score = 20 × señales elegibles activas; 0 si falla un filtro (liquidez o kill switch)."""
    import time
    now_s = time.time() if now_s is None else now_s
    dx = (token_data or {}).get("dexscreener") or {}
    age = age_minutes(dx, now_s)
    if age is None:
        return None, ["fuera de alcance: edad desconocida"]
    if age >= SCOPE_MAX_AGE_MIN:
        return None, [f"fuera de alcance: edad {age:.1f} min >= {SCOPE_MAX_AGE_MIN} (lo puntúa v7.2.1)"]
    reasons = [f"{VERSION} · edad {age:.1f} min"]
    act = active_signals(signals)
    for name, s in act.items():
        reasons.append(f"{name}: {s.get('detail', '')} (s {s['s']:.2f})")
    score = min(100, POINTS_PER_SIGNAL * len(act))
    liq = _num(dx.get("liquidityUsd")) or 0.0
    blocks = kill_switches(token_data, rug, age)
    if liq <= LIQ_MIN_USD:
        blocks.insert(0, f"liquidez ${liq:,.0f} <= ${LIQ_MIN_USD:,.0f}")
    if blocks:
        return 0, reasons + [f"FILTRO: {b}" for b in blocks] + [f"(sin filtros sería {score})"]
    reasons.append(f"{len(act)} señales activas → {score} (umbral {YOUNG_THRESHOLD})")
    return score, reasons


def fires(score):
    return score is not None and score >= YOUNG_THRESHOLD
