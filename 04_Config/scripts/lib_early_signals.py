#!/usr/bin/env python3
"""
lib_early_signals.py — Señales anticipatorias (Fase 10, T2). Funciones puras, solo biblioteca estándar.

Objetivo: ver el pump ANTES de que el precio se mueva (o en sus primeros minutos). Cada señal devuelve
{"name", "s" (0..1), "points" (aporte al bono), "detail"} o None si no hay datos suficientes.
Solo suman: ninguna señal resta puntos (directiva Fase 10). El bono total tiene tope (BONUS_CAP).

Señales:
  1. volume_acceleration   tasa de volumen de los últimos 5 min vs. la tasa media de la última hora (DexScreener).
  2. buy_pressure_shift    proporción de compras en 5 min vs. la de 1 h (DexScreener txns).
  3. quiet_accumulation    volumen acelerado + compras dominantes con el precio todavía quieto (|m5| < 5 %):
                           la firma previa al pump.
  4. liquidity_inflow      crecimiento de la liquidez del pool entre polls (serie propia del early watch).
  5. orderbook_imbalance   desequilibrio bid/ask dentro de ±2 % del mid (Hyperliquid l2Book / dYdX v4).
  6. holder_accumulation   crecimiento de holders por minuto con concentración top-10 que no sube (RugCheck).
  7. social_velocity       sorpresa de menciones (doc 26) + aceleración 1 h vs. 1 h previa + CoinGecko trending.
  8. funding_squeeze       funding anómalamente negativo con OI subiendo (setup de short squeeze, perps).
  9. fear_greed_extreme    Fear & Greed <= 20 (contrarian).
 10. clmm_imbalance        (0.2, Fase 10b) liquidez concentrada debajo vs. encima del precio en un pool CLMM de
                           Solana (Raydium /pools/line/position): el "order book" de un AMM concentrado.

Parámetros heurísticos [H], no calibrados: se calibran con historical_alerts.jsonl cuando haya n suficiente.
"""
import math
import statistics

VERSION = "early-0.2"
BONUS_CAP = 8                       # puntos máximos sobre el score (0..100)
POINTS = {"volume_acceleration": 3, "buy_pressure_shift": 2, "quiet_accumulation": 3, "liquidity_inflow": 2,
          "orderbook_imbalance": 3, "holder_accumulation": 2, "social_velocity": 3, "funding_squeeze": 2,
          "fear_greed_extreme": 1, "clmm_imbalance": 3}
MIN_TXNS_M5 = 10                    # menos trades en 5 min = ruido
QUIET_PRICE_M5 = 5.0                # % — "precio todavía quieto"
OB_DEPTH_PCT = 0.02                 # ±2 % del mid


def _num(x):
    if x is None or isinstance(x, bool):
        return None
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if math.isfinite(v) else None


def _clip01(x):
    return max(0.0, min(1.0, x))


def _signal(name, s, detail):
    s = round(_clip01(s), 4)
    return {"name": name, "s": s, "points": round(POINTS[name] * s, 2), "detail": detail}


# ---------------------------------------------------------------------------
# Señales de flujo (DexScreener)
# ---------------------------------------------------------------------------

def volume_rate_ratio(vol_m5, vol_h1):
    """Tasa de 5 min / tasa media de la hora. None si la hora no tiene más que los 5 min (par recién nacido)."""
    m5, h1 = _num(vol_m5), _num(vol_h1)
    if m5 is None or h1 is None or h1 <= 0 or h1 <= m5 * 1.05:
        return None
    return m5 / (h1 / 12.0)


def volume_acceleration(vol_m5, vol_h1, lo=1.5, hi=4.0):
    ratio = volume_rate_ratio(vol_m5, vol_h1)
    if ratio is None:
        return None
    return _signal("volume_acceleration", (ratio - lo) / (hi - lo), f"vol 5 min ×{ratio:.1f} la tasa horaria")


def buy_ratio(buys, sells):
    b, s = _num(buys), _num(sells)
    if b is None or s is None or b + s <= 0:
        return None
    return b / (b + s)


def buy_pressure_shift(buys_m5, sells_m5, buys_h1, sells_h1, min_txns=MIN_TXNS_M5):
    r5, r1 = buy_ratio(buys_m5, sells_m5), buy_ratio(buys_h1, sells_h1)
    if r5 is None or (_num(buys_m5) or 0) + (_num(sells_m5) or 0) < min_txns:
        return None
    base = max(r1 if r1 is not None else 0.5, 0.5)
    return _signal("buy_pressure_shift", (r5 - base) / 0.2,
                   f"compras {r5:.0%} en 5 min vs {r1:.0%} en 1 h" if r1 is not None else f"compras {r5:.0%} en 5 min")


def quiet_accumulation(price_m5, vol_m5, vol_h1, buys_m5, sells_m5, min_txns=MIN_TXNS_M5):
    """Volumen acelerado (>= ×2) + compras >= 60 % + precio quieto (|m5| < 5 %)."""
    p, ratio, r5 = _num(price_m5), volume_rate_ratio(vol_m5, vol_h1), buy_ratio(buys_m5, sells_m5)
    if p is None or ratio is None or r5 is None or (_num(buys_m5) or 0) + (_num(sells_m5) or 0) < min_txns:
        return None
    if abs(p) >= QUIET_PRICE_M5 or ratio < 2.0 or r5 < 0.6:
        return _signal("quiet_accumulation", 0.0, f"m5 {p:+.1f}% · vol ×{ratio:.1f} · compras {r5:.0%}")
    s = 0.5 * _clip01((ratio - 2.0) / 2.0) + 0.5 * _clip01((r5 - 0.6) / 0.2)
    return _signal("quiet_accumulation", max(s, 0.25),
                   f"precio quieto (m5 {p:+.1f}%) con vol ×{ratio:.1f} y compras {r5:.0%}")


def liquidity_inflow(series, window_s=600, full=0.30):
    """series: [(ts_s, liquidity_usd)] de polls propios. Cambio % de la liquidez en la ventana (por defecto 10 min)
    escalado: +30 % = s 1."""
    pts = sorted((t, _num(v)) for t, v in series or [] if _num(v))
    if len(pts) < 2:
        return None
    last_t, last_v = pts[-1]
    base = [p for p in pts if p[0] >= last_t - window_s]
    t0, v0 = base[0] if base and base[0][0] < last_t else pts[-2]
    if v0 <= 0 or last_t - t0 <= 0:
        return None
    change = last_v / v0 - 1
    return _signal("liquidity_inflow", change / full,
                   f"liquidez {change:+.0%} en {round((last_t - t0) / 60)} min")


# ---------------------------------------------------------------------------
# Order book (T4)
# ---------------------------------------------------------------------------

def book_depth(levels, mid, depth_pct=OB_DEPTH_PCT, side="bid"):
    """Suma notional (px × size) de los niveles dentro de ±depth_pct del mid."""
    total = 0.0
    for lv in levels or []:
        px, sz = (_num(lv[0]), _num(lv[1])) if isinstance(lv, (list, tuple)) else (_num(lv.get("px") or lv.get("price")),
                                                                                    _num(lv.get("sz") or lv.get("size")))
        if px is None or sz is None or px <= 0:
            continue
        if (side == "bid" and px >= mid * (1 - depth_pct)) or (side == "ask" and px <= mid * (1 + depth_pct)):
            total += px * sz
    return total


def orderbook_imbalance(bids, asks, depth_pct=OB_DEPTH_PCT, lo=0.15, hi=0.5):
    """(bid − ask) / (bid + ask) dentro de ±depth_pct del mid. Solo el lado comprador suma."""
    best_bid = max((_num(b[0] if isinstance(b, (list, tuple)) else b.get("px") or b.get("price")) or 0)
                   for b in bids) if bids else None
    best_ask = min((_num(a[0] if isinstance(a, (list, tuple)) else a.get("px") or a.get("price")) or float("inf"))
                   for a in asks) if asks else None
    if not best_bid or not best_ask or best_ask == float("inf") or best_ask < best_bid:
        return None
    mid = (best_bid + best_ask) / 2
    b, a = book_depth(bids, mid, depth_pct, "bid"), book_depth(asks, mid, depth_pct, "ask")
    if b + a <= 0:
        return None
    imb = (b - a) / (b + a)
    sig = _signal("orderbook_imbalance", (imb - lo) / (hi - lo),
                  f"bid/ask ±{depth_pct:.0%}: {imb:+.2f} (bid ${b:,.0f} · ask ${a:,.0f})")
    sig["imbalance"] = round(imb, 4)
    return sig


def clmm_imbalance(points, price, depth_pct=OB_DEPTH_PCT, lo=0.15, hi=0.5):
    """points: [(precio, liquidez)] de un pool de liquidez concentrada. La liquidez por debajo del precio actual
    compra si el precio baja (lado bid) y la de arriba vende si sube (lado ask). (bid − ask) / (bid + ask) dentro
    de ±depth_pct. Unidades de liquidez del pool (no USD): vale como proporción en una banda angosta [H]."""
    p = _num(price)
    if p is None or p <= 0:
        return None
    bid = ask = 0.0
    for px, liq in points or []:
        px, liq = _num(px), _num(liq)
        if px is None or liq is None or liq <= 0:
            continue
        if p * (1 - depth_pct) <= px < p:
            bid += liq
        elif p <= px <= p * (1 + depth_pct):
            ask += liq
    if bid + ask <= 0:
        return None
    imb = (bid - ask) / (bid + ask)
    sig = _signal("clmm_imbalance", (imb - lo) / (hi - lo), f"CLMM ±{depth_pct:.0%}: {imb:+.2f}")
    sig["imbalance"] = round(imb, 4)
    return sig


# ---------------------------------------------------------------------------
# On-chain (T5)
# ---------------------------------------------------------------------------

def holder_accumulation(snapshots, full_rate=5.0):
    """snapshots: [(ts_s, holders, top10_pct)] (RugCheck). Holders nuevos por minuto (5/min = s 1); si la
    concentración top-10 sube, la mitad (acumulan pocos)."""
    pts = sorted((t, _num(h), _num(c)) for t, h, c in snapshots or [] if _num(h) is not None)
    if len(pts) < 2:
        return None
    (t0, h0, c0), (t1, h1, c1) = pts[0], pts[-1]
    if t1 - t0 < 60:
        return None
    rate = (h1 - h0) / ((t1 - t0) / 60)
    factor = 0.5 if (c0 is not None and c1 is not None and c1 > c0 + 1.0) else 1.0
    detail = f"holders {h0:.0f}→{h1:.0f} ({rate:+.1f}/min)"
    if c0 is not None and c1 is not None:
        detail += f" · top10 {c0:.1f}%→{c1:.1f}%"
    return _signal("holder_accumulation", factor * rate / full_rate, detail)


def rugcheck_snapshot(report, now_s):
    """Del reporte de RugCheck (/v1/tokens/{mint}/report): (ts, holders, top10_pct, insiders)."""
    if not isinstance(report, dict):
        return None
    holders = _num(report.get("totalHolders"))
    top = report.get("topHolders") or []
    pcts = sorted((_num(h.get("pct")) or 0 for h in top if isinstance(h, dict)), reverse=True)
    top10 = round(sum(pcts[:10]), 2) if pcts else None
    insiders = sum(1 for h in top if isinstance(h, dict) and h.get("insider"))
    if holders is None and top10 is None:
        return None
    return {"ts": now_s, "holders": holders, "top10_pct": top10, "insiders_top": insiders,
            "graph_insiders": report.get("graphInsidersDetected")}


# ---------------------------------------------------------------------------
# Social (T6)
# ---------------------------------------------------------------------------

def social_velocity(snapshot, trending=None, surprise_full=6.0):
    """snapshot: el de script_115 (doc 26): m_1h, m_prev_1h, surprise_nats, seff_1h. trending: hit de CoinGecko."""
    if not isinstance(snapshot, dict):
        return None
    m1, m0 = _num(snapshot.get("m_1h")) or 0.0, _num(snapshot.get("m_prev_1h")) or 0.0
    surprise = max(_num(snapshot.get("surprise_nats")) or 0.0, 0.0)
    seff = _num(snapshot.get("seff_1h")) or 0.0
    s = _clip01(surprise / surprise_full)
    if m1 >= 2 and m1 >= 2 * max(m0, 1.0):
        s = max(s, 0.5 * _clip01(seff / 2.0) + 0.25)
    if trending:
        s = max(s, 0.6)
    detail = f"menciones 1 h {m1:g} (previa {m0:g}) · sorpresa {surprise:.1f} nats · fuentes ef. {seff:.1f}"
    if trending:
        detail += f" · CoinGecko trending #{trending.get('rank')}"
    return _signal("social_velocity", s, detail)


# ---------------------------------------------------------------------------
# Derivados y mercado
# ---------------------------------------------------------------------------

def funding_squeeze(funding_now, history, oi_change=None, z_full=3.0):
    """Funding muy por debajo de su historia (z <= −1.5) con OI que no baja: shorts cargados, setup de squeeze."""
    f = _num(funding_now)
    hist = [_num(x) for x in history or [] if _num(x) is not None]
    if f is None or len(hist) < 6:
        return None
    sd = statistics.pstdev(hist)
    if sd <= 0:
        return None
    z = (f - statistics.mean(hist)) / sd
    oi = _num(oi_change)
    if oi is not None and oi < 0:
        return _signal("funding_squeeze", 0.0, f"funding z {z:+.1f} con OI {oi:+.1%}")
    s = (-z - 1.5) / (z_full - 1.5)
    return _signal("funding_squeeze", s, f"funding z {z:+.1f}" + (f" · OI {oi:+.1%}" if oi is not None else ""))


def fear_greed_extreme(value):
    v = _num(value)
    if v is None:
        return None
    return _signal("fear_greed_extreme", (20 - v) / 20, f"Fear & Greed {v:.0f}")


# ---------------------------------------------------------------------------
# Combinación
# ---------------------------------------------------------------------------

def dex_signals(dx, liquidity_series=None):
    """Las señales de flujo a partir de un dict DexScreener aplanado (formato de script_82: volume_m5, volume_h1,
    txns_m5_buys, ..., priceChange_m5)."""
    dx = dx or {}
    return [volume_acceleration(dx.get("volume_m5"), dx.get("volume_h1")),
            buy_pressure_shift(dx.get("txns_m5_buys"), dx.get("txns_m5_sells"),
                               dx.get("txns_h1_buys"), dx.get("txns_h1_sells")),
            quiet_accumulation(dx.get("priceChange_m5"), dx.get("volume_m5"), dx.get("volume_h1"),
                               dx.get("txns_m5_buys"), dx.get("txns_m5_sells")),
            liquidity_inflow(liquidity_series)]


def combine(signals, cap=BONUS_CAP):
    """Bono entero 0..cap. Devuelve {"bonus", "raw", "signals", "reasons", "active"}."""
    sigs = [s for s in signals if s]
    raw = sum(s["points"] for s in sigs)
    bonus = int(min(cap, math.floor(raw + 1e-9)))
    active = [s["name"] for s in sigs if s["s"] > 0]
    reasons = [f"{s['name']}: {s['detail']} → +{s['points']:g}" for s in sigs if s["s"] > 0]
    return {"version": VERSION, "bonus": bonus, "raw": round(raw, 2), "cap": cap, "active": active,
            "signals": sigs, "reasons": reasons}


def apply_bonus(score, early):
    """Suma el bono (nunca resta). score None -> None."""
    if score is None:
        return None
    return int(min(100, score + max(0, int((early or {}).get("bonus") or 0))))
