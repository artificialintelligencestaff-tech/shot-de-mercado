#!/usr/bin/env python3
"""
lib_scoring_multichain.py — Scoring por tipo de activo (doc 27, Fase 7). Funciones puras, SIN red.

Entradas: lo que escribe script_114 en 02_Analisis/multichain/ (scan_latest.json, <chain>.json con el Universo A,
_categories.json, _protocols.json). Salida por activo: grupo (doc 27 §2.2), score 0–100, motivos y confianza.

Estructura común (doc 27 §4.1): cada componente da sᵢ ∈ [−1, +1] con peso wᵢ; las componentes sin dato (n/d) no
cuentan y no se rellenan.
    cobertura = Σ_{con dato} wᵢ / 100          D = Σ wᵢ·sᵢ / Σ_{con dato} wᵢ          score = clip(50 + 50·D·M + ajuste)
Cada scorer público devuelve (score, reasons, confidence), con confidence = cobertura. `evaluate()` devuelve el
detalle (componentes, versión, evento, si es emitible).

Grupos: a memecoins · b preventa · c gobernanza · d sintéticos · e DePIN · f L1/L2 · g RWA · h blue chips ·
i establecidos sin grupo. Emiten (si score >= umbral y cobertura >= 0,6): a, c, d, e, f, g, h. Solo registran: b, i
(i por decisión de Dirección; b porque antes del listing no hay ruta de compra).
Todas las escalas, pesos y umbrales son HEURÍSTICOS, NO CALIBRADOS (doc 27).
"""
import math
import statistics
from datetime import datetime, timezone

EMIT_THRESHOLD = {g: 56 for g in "acdefgh"}     # inicial 56 (directiva Fase 7), ajustable por grupo
MIN_COVERAGE = 0.6
REGISTER_ONLY = {"b": "preventa: sin ruta de compra antes del listing",
                 "i": "establecidos sin grupo: se registran, no se emiten (Dirección, Fase 6)"}
VERSION = "0.3"
# MemeChain (Fase 9): tasas base por chain y narrativa para las memecoins multi-chain (grupo a). Chains del dataset:
# ethereum, bsc, solana, base; el resto usa la tasa total.
MEMECHAIN_CHAIN_ALIASES = {"ethereum": "ethereum", "eth": "ethereum", "base": "base", "solana": "solana", "bsc": "bsc"}
MEMECHAIN_NARRATIVES = {
    "canino": r"\b(dog|doge|inu|shib|shiba|puppy|pup|wif|bonk)\b", "felino": r"\b(cat|kitty|meow|neko|popcat|mew)\b",
    "ia": r"\b(ai|gpt|agent|bot|neural|agi)\b", "rana_pepe": r"\b(pepe|frog|toad)\b",
    "politica": r"\b(trump|maga|biden|kamala|elon|musk|vance)\b"}
GOV_KEYWORDS = ("fee switch", "fee", "emission", "buyback", "burn", "tokenomics", "revenue", "reward", "inflation",
                "staking")
BLUE_CHIP_IDS = {"bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL"}
GT_TO_CHAIN = {"eth": "ethereum", "base": "base", "arbitrum": "arbitrum", "optimism": "optimism", "blast": "blast",
               "monad": "monad"}               # solana queda en la ruta rápida (script_82), no se duplica
EVENTS = {
    "a": "tocar +20% antes de −30% en 48 h (v7.2.1)",
    "h": "tocar +2σ₄₈ antes de −2σ₄₈ (σ del GARCH(1,1))",
    "f": "+20% antes de −15% en 48 h", "c": "+20% antes de −15% en 48 h", "e": "+20% antes de −15% en 48 h",
    "g": "+20% antes de −15% en 48 h", "d": "+20% antes de −15% en 48 h", "b": "precio al listar ≥ +20% sobre la referencia",
    "i": "+20% antes de −15% en 48 h (solo registro)",
}
DAY_MS = 86_400_000
CATEGORY_IDS = ("layer-1", "layer-2", "governance", "depin", "real-world-assets-rwa", "decentralized-perpetuals",
                "synthetic-issuer")


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def clip(x, lo=-1.0, hi=1.0):
    return max(lo, min(hi, x))


def _f(x):
    try:
        v = float(x) if x is not None and not isinstance(x, bool) else None
    except (TypeError, ValueError):
        return None
    return v if v is not None and math.isfinite(v) else None


def comp(name, s, w, value, source):
    """Componente: s=None significa n/d (no cuenta)."""
    return {"name": name, "s": None if s is None else round(clip(s), 4), "w": w, "value": value, "source": source}


def combine(components, multiplier=1.0, adjust=0.0, notes=()):
    avail = [c for c in components if c["s"] is not None]
    wsum = sum(c["w"] for c in avail)
    coverage = round(wsum / 100.0, 4)
    d = sum(c["w"] * c["s"] for c in avail) / wsum if wsum else 0.0
    score = int(round(clip(50 + 50 * d * multiplier + adjust, 0, 100))) if wsum else None
    reasons = [f"{c['name']}: {c['value']} → s={c['s']:+.2f} (w {c['w']})" for c in avail]
    reasons += [f"{c['name']}: n/d" for c in components if c["s"] is None]
    reasons += list(notes)
    return {"score": score, "confidence": coverage, "D": round(d, 4), "multiplier": multiplier, "adjust": adjust,
            "components": components, "reasons": reasons}


def _pct_rank(value, values):
    """Percentil de `value` dentro de `values` (0..1); None con menos de 3 valores."""
    vals = sorted(v for v in values if v is not None)
    if value is None or len(vals) < 3:
        return None
    below = sum(1 for v in vals if v < value)
    equal = sum(1 for v in vals if v == value)
    return (below + 0.5 * max(0, equal - 1)) / (len(vals) - 1)


def _log1p_pct(pct):
    return math.log(1 + pct / 100) if pct is not None and pct > -100 else None


# ---------------------------------------------------------------------------
# Modelos de volatilidad (solo blue chips: prohibidos en memecoins)
# ---------------------------------------------------------------------------

def closed_klines(rows, now_ms):
    """Velas diarias cerradas: descarta la del día en curso (closeTime > ahora)."""
    return [r for r in rows or [] if isinstance(r, (list, tuple)) and len(r) >= 7 and r[6] <= now_ms]


def log_returns(closes):
    return [math.log(b / a) for a, b in zip(closes, closes[1:]) if a and b and a > 0 and b > 0]


def garch11(returns, alphas=None, betas=None):
    """GARCH(1,1) con variance targeting (ω = σ²·(1−α−β)) y búsqueda en grilla por máxima verosimilitud.

    Python puro (doc 27 §3.2, opción 2): sin dependencias nuevas. Devuelve None con menos de 100 retornos.
    sigma_last: desvío condicional del último retorno; sigma_next: pronóstico para el próximo día.
    """
    r = list(returns or [])
    if len(r) < 100:
        return None
    var = statistics.pvariance(r) or 1e-12
    alphas = alphas or [a / 100 for a in range(2, 22, 2)]
    betas = betas or [b / 100 for b in range(70, 98)]
    best = None
    for a in alphas:
        for b in betas:
            if a + b >= 0.995:
                continue
            w = var * (1 - a - b)
            s2, ll = var, 0.0
            for x in r:
                ll -= 0.5 * (math.log(s2) + x * x / s2)
                s2_last, s2 = s2, w + a * x * x + b * s2
            if best is None or ll > best[0]:
                best = (ll, a, b, w, s2_last, s2)
    ll, a, b, w, s2_last, s2_next = best
    return {"alpha": a, "beta": b, "omega": w, "sigma_long": math.sqrt(var), "sigma_last": math.sqrt(s2_last),
            "sigma_next": math.sqrt(s2_next), "loglik": ll, "n": len(r)}


def atr(rows, n=14):
    """ATR(n) sobre velas [t, o, h, l, c, ...]."""
    if len(rows) < n + 1:
        return None
    trs = [max(h - l, abs(h - pc), abs(l - pc)) for (_, _, h, l, _c, *_), (_, _, _, _, pc, *_) in zip(rows[1:], rows)]
    return sum(trs[-n:]) / n


def bollinger(closes, n=20, k=2.0):
    """(media, banda inferior, banda superior, ancho relativo) de los últimos n cierres."""
    if len(closes) < n:
        return None
    win = closes[-n:]
    mid = sum(win) / n
    sd = statistics.pstdev(win)
    return mid, mid - k * sd, mid + k * sd, (2 * k * sd / mid) if mid else None


# ---------------------------------------------------------------------------
# Scorers por grupo (componentes de doc 27 §4; las sustituciones están marcadas [H])
# ---------------------------------------------------------------------------

def components_blue_chip(asset, now_ms=None):
    """h: retorno vs σ GARCH, Bollinger con squeeze, funding, Fear & Greed y tendencia MA20 ± ATR14."""
    now_ms = now_ms if now_ms is not None else int(datetime.now(timezone.utc).timestamp() * 1000)
    ua = asset.get("universe_a") or {}
    rows = closed_klines(ua.get("klines_1d"), now_ms)
    closes = [r[4] for r in rows]
    price, ch24 = _f(asset.get("price_usd")), _f(asset.get("change_24h"))
    g = garch11(log_returns(closes[-366:]))
    comps, extra = [], {}
    if g and ch24 is not None:
        z = math.log(1 + ch24 / 100) / g["sigma_next"]
        extra["garch"] = {k: round(v, 6) for k, v in g.items()}
        extra["barrier_pct"] = round(2 * g["sigma_next"] * math.sqrt(2) * 100, 3)
        comps.append(comp("Retorno 24 h / σ GARCH", z / 2, 30,
                          f"{ch24:+.2f}% / σ {g['sigma_next'] * 100:.2f}% = z {z:+.2f}", "Binance klines + CoinGecko"))
    else:
        comps.append(comp("Retorno 24 h / σ GARCH", None, 30, None, "Binance klines (< 100 días o sin precio)"))
    # Squeeze = bandas de las 20 velas CERRADAS angostas para su historia; la ruptura es el precio actual fuera de
    # esas bandas (si el precio entrara en el cálculo, la propia ruptura ensancharía la banda).
    series = closes + ([price] if price else [])
    bb = bollinger(closes)
    if bb and price and len(closes) >= 60:
        widths = [bollinger(closes[:i])[3] for i in range(20, len(closes) + 1)][-365:]
        pct = _pct_rank(bb[3], widths)
        squeeze = pct is not None and pct <= 0.20
        s = (1 if price > bb[2] else -1 if price < bb[1] else 0) if squeeze else 0
        comps.append(comp("Bollinger(20,2) con squeeze", s, 20,
                          f"ancho en percentil {pct:.2f} · precio {'>' if price > bb[2] else '<' if price < bb[1] else 'dentro de'} bandas",
                          "Binance klines"))
    else:
        comps.append(comp("Bollinger(20,2) con squeeze", None, 20, None, "Binance klines"))
    perp = ua.get("perp") or {}
    fr = _f(perp.get("funding_1h"))
    if fr is not None:
        ann = fr * 24 * 365
        comps.append(comp("Funding (contrarian en extremos) [H: umbral absoluto hasta tener historia]",
                          -1 if ann >= 0.30 else 1 if ann <= -0.10 else 0, 20,
                          f"{ann * 100:+.1f}% anualizado", "Hyperliquid"))
    else:
        comps.append(comp("Funding (contrarian en extremos)", None, 20, None, "Hyperliquid"))
    fng = _f((ua.get("fear_greed") or {}).get("value"))
    comps.append(comp("Fear & Greed (contrarian en extremos)",
                      None if fng is None else (1 if fng <= 20 else -1 if fng >= 80 else 0), 15,
                      None if fng is None else f"{fng:.0f}", "alternative.me"))
    a14 = atr(rows)
    if a14 and len(series) >= 20 and price:
        ma = sum(series[-20:]) / 20
        s = 1 if price > ma + a14 else -1 if price < ma - a14 else 0
        comps.append(comp("Tendencia (MA20 ± ATR14)", s, 15, f"precio {price:,.2f} · MA20 {ma:,.2f} · ATR {a14:,.2f}",
                          "Binance klines"))
    else:
        comps.append(comp("Tendencia (MA20 ± ATR14)", None, 15, None, "Binance klines"))
    return comps, 1.0, 0.0, ["Energía M = 1: DVOL (Deribit) sin colectar"], extra


def components_l1_l2(asset, peers=(), eth_change_7d=None):
    """f: momentum y aceleración del TVL, actividad (DEX/TVL) y fees/TVL contra las otras chains, y momentum relativo."""
    card = asset.get("card") or {}
    tvl = card.get("tvl") or {}
    g7, a7 = _f(tvl.get("log_growth_7d")), _f(tvl.get("accel_7d"))
    der = card.get("derived") or {}
    act, fees = _f(der.get("dex_volume_tvl_24h")), _f(der.get("fees_tvl_annualized_pct"))
    peer_act = [_f((p.get("derived") or {}).get("dex_volume_tvl_24h")) for p in peers]
    peer_fee = [_f((p.get("derived") or {}).get("fees_tvl_annualized_pct")) for p in peers]
    pa, pf = _pct_rank(act, peer_act), _pct_rank(fees, peer_fee)
    ch7 = _f(asset.get("change_7d"))
    rel = ch7 - eth_change_7d if ch7 is not None and eth_change_7d is not None else None
    comps = [comp("Momentum de TVL (g₇)", None if g7 is None else g7 / 0.10, 25,
                  None if g7 is None else f"{g7:+.4f}", "DefiLlama historicalChainTvl"),
             comp("Aceleración de TVL (a₇)", None if a7 is None else a7 / 0.05, 15,
                  None if a7 is None else f"{a7:+.4f}", "DefiLlama historicalChainTvl"),
             comp("Actividad DEX/TVL (ranking entre chains)", None if pa is None else 2 * pa - 1, 20,
                  None if pa is None else f"{act:.3f} · percentil {pa:.2f}", "DefiLlama overview/dexs"),
             comp("Fees/TVL anualizado (ranking entre chains)", None if pf is None else 2 * pf - 1, 15,
                  None if pf is None else f"{fees:.2f}% · percentil {pf:.2f}", "DefiLlama overview/fees"),
             comp("Momentum relativo vs ETH (7d)", None if rel is None else rel / 20, 25,
                  None if rel is None else f"{ch7:+.2f}% − ETH {eth_change_7d:+.2f}% = {rel:+.2f} pp", "CoinGecko")]
    return comps, 1.0, 0.0, [], {}


def _protocol_tvl_growth(asset):
    p = asset.get("protocol") or {}
    return _log1p_pct(_f(p.get("change_7d"))), _f(p.get("tvl"))


def _dilution(asset):
    fdv, mcap = _f(asset.get("fdv_usd")), _f(asset.get("mcap_usd"))
    if not fdv or not mcap or fdv < mcap * 0.999:
        return None, None
    r = fdv / mcap
    return -clip(math.log(r) / math.log(3), 0, 1), r


def _vs_category(asset):
    ch7, med = _f(asset.get("change_7d")), _f(asset.get("category_median_7d"))
    return (None, None) if ch7 is None or med is None else ((ch7 - med) / 20, ch7 - med)


def _fees_ratio(asset):
    """ρ = (fees₇d·30/7)/fees₃₀d del protocolo (doc 27 §4.4): > 1 = fees acelerando."""
    p = asset.get("protocol") or {}
    f7, f30 = _f(p.get("fees_7d")), _f(p.get("fees_30d"))
    return (f7 * 30 / 7) / f30 if f7 and f30 and f7 > 0 and f30 > 0 else None


def _governance_event(asset):
    """+1 si una propuesta activa de su espacio de Snapshot cierra en <= 48 h y toca fees/emisiones/buyback; 0 si
    no hay ninguna así; None si Snapshot no cargó."""
    gov = asset.get("governance") or {}
    if not gov.get("loaded"):
        return None, None
    hits = [p for p in gov.get("matches") or []
            if p.get("hours_left") is not None and 0 < p["hours_left"] <= 48
            and any(k in str(p.get("title") or "").lower() for k in GOV_KEYWORDS)]
    if hits:
        return 1.0, f"{hits[0]['title'][:60]} (cierra en {hits[0]['hours_left']:.0f} h)"
    return 0.0, f"{len(gov.get('matches') or [])} propuestas activas, ninguna de fees/emisiones en 48 h"


def components_governance(asset):
    """c: crecimiento de fees (o de TVL si no hay fees), valuación mcap/TVL, evento de gobernanza (Snapshot),
    dilución FDV/mcap y momentum contra la mediana de la categoría."""
    g7, tvl = _protocol_tvl_growth(asset)
    rho = _fees_ratio(asset)
    mcap = _f(asset.get("mcap_usd"))
    dil, ratio = _dilution(asset)
    rel, diff = _vs_category(asset)
    val = math.log(mcap / tvl) if mcap and tvl else None
    ev, ev_text = _governance_event(asset)
    growth = (comp("Crecimiento de fees (7d vs 30d)", math.log(rho) / 0.5, 25, f"ρ {rho:.2f}", "DefiLlama overview/fees")
              if rho is not None else
              comp("Crecimiento de TVL del protocolo (7d) [H: sin fees]", None if g7 is None else g7 / 0.10, 25,
                   None if g7 is None else f"{g7:+.4f}", "DefiLlama /protocols"))
    return [growth,
            comp("Valuación mcap/TVL", None if val is None else -val / math.log(4), 20,
                 None if val is None else f"{mcap / tvl:.2f}", "CoinGecko + DefiLlama"),
            comp("Evento de gobernanza (Snapshot)", ev, 20, ev_text, "Snapshot GraphQL"),
            comp("Dilución FDV/mcap", dil, 15, None if ratio is None else f"{ratio:.2f}", "CoinGecko"),
            comp("Momentum vs categoría (7d)", rel, 20, None if diff is None else f"{diff:+.2f} pp", "CoinGecko")], \
        1.0, 0.0, [], {}


def components_depin(asset):
    """e: actividad del token como proxy de ingresos [H], divergencia (n/d), dilución, momentum de categoría y relativo."""
    vol, mcap, med = _f(asset.get("volume_24h_usd")), _f(asset.get("mcap_usd")), _f(asset.get("category_median_turnover"))
    turn = vol / mcap if vol and mcap else None
    act = math.log(turn / med) / math.log(3) if turn and med else None
    dil, ratio = _dilution(asset)
    cat = _f(asset.get("category_vs_market_24h"))
    rel, diff = _vs_category(asset)
    rho = _fees_ratio(asset)
    first = (comp("Crecimiento de ingresos de red (fees 7d vs 30d)", math.log(rho) / 0.5, 30, f"ρ {rho:.2f}",
                  "DefiLlama overview/fees") if rho is not None else
             comp("Actividad (vol/mcap vs categoría) [H: proxy de ingresos de red]", act, 30,
                  None if act is None else f"{turn:.4f} vs mediana {med:.4f}", "CoinGecko"))
    return [first,
            comp("Divergencia ingresos vs precio", None, 20, None, "DefiLlama fees (sin colectar)"),
            comp("Dilución FDV/mcap", dil, 20, None if ratio is None else f"{ratio:.2f}", "CoinGecko"),
            comp("Momentum de la categoría (24 h vs mediana de las 7)", None if cat is None else cat / 5, 15,
                 None if cat is None else f"{cat:+.2f} pp", "CoinGecko coins/categories"),
            comp("Momentum vs categoría (7d)", rel, 15, None if diff is None else f"{diff:+.2f} pp", "CoinGecko")], \
        1.0, 0.0, [], {}


def is_stable_rwa(asset):
    """Filtro previo de g (doc 27 §4.6): activos tokenizados con precio casi fijo (T-bills, oro) no tienen evento."""
    ch24, ch7 = _f(asset.get("change_24h")), _f(asset.get("change_7d"))
    return ch24 is not None and ch7 is not None and abs(ch24) < 0.5 and abs(ch7) < 2.0


def _yield_comp(asset):
    p = asset.get("protocol") or {}
    f30, tvl = _f(p.get("fees_30d")), _f(p.get("tvl"))
    y = f30 * 365 / 30 / tvl if f30 and tvl and f30 > 0 else None
    return comp("Yield (fees/TVL anualizado; 5% = neutro)", None if y is None else math.log(y / 0.05) / math.log(4), 15,
                None if y is None else f"{y * 100:.2f}%", "DefiLlama overview/fees + /protocols")


def components_rwa(asset):
    """g: TVL de la plataforma, TVL vs mcap, yield (n/d), momentum de categoría y relativo."""
    g7, _ = _protocol_tvl_growth(asset)
    m7 = _log1p_pct(_f(asset.get("change_7d")))
    gap = g7 - m7 if g7 is not None and m7 is not None else None
    cat = _f(asset.get("category_vs_market_24h"))
    rel, diff = _vs_category(asset)
    return [comp("Crecimiento de TVL de la plataforma (7d)", None if g7 is None else g7 / 0.10, 30,
                 None if g7 is None else f"{g7:+.4f}", "DefiLlama /protocols"),
            comp("TVL vs mcap (7d)", None if gap is None else gap / 0.10, 25,
                 None if gap is None else f"{gap:+.4f}", "DefiLlama + CoinGecko"),
            _yield_comp(asset),
            comp("Momentum de la categoría (24 h vs mediana de las 7)", None if cat is None else cat / 5, 15,
                 None if cat is None else f"{cat:+.2f} pp", "CoinGecko coins/categories"),
            comp("Momentum vs categoría (7d)", rel, 15, None if diff is None else f"{diff:+.2f} pp", "CoinGecko")], \
        1.0, 0.0, [], {}


def _oi_change_24h(asset):
    """ln(OI_ahora / OI de hace ~24 h) con el historial de _perps.json (necesita >= 20 h de fotos)."""
    hist = asset.get("oi_history") or []
    if len(hist) < 2:
        return None
    try:
        last_t = datetime.fromisoformat(str(hist[-1][0]).replace("Z", "+00:00"))
    except ValueError:
        return None
    for t, oi in hist:
        try:
            age_h = (last_t - datetime.fromisoformat(str(t).replace("Z", "+00:00"))).total_seconds() / 3600
        except ValueError:
            continue
        if 20 <= age_h <= 30 and oi and hist[-1][1]:
            return math.log(hist[-1][1] / oi)
    return None


def components_synthetic(asset):
    """d1: funding (contrarian en extremos), OI que confirma, basis (mark − oráculo) y momentum 24 h, con el perp del
    token en Hyperliquid."""
    ch24 = _f(asset.get("change_24h"))
    perp = asset.get("perp") or {}
    fr = _f(perp.get("funding_1h"))
    ann = fr * 24 * 365 if fr is not None else None
    oi = _oi_change_24h(asset)
    mark, oracle = _f(perp.get("mark_px")), _f(perp.get("oracle_px"))
    basis = (mark - oracle) / oracle if mark and oracle else None
    sign = 0 if ch24 is None else (1 if ch24 > 0 else -1 if ch24 < 0 else 0)
    return [comp("Funding (contrarian en extremos)", None if ann is None else (-1 if ann >= 0.30 else 1 if ann <= -0.10 else 0),
                 25, None if ann is None else f"{ann * 100:+.1f}% anualizado", "Hyperliquid"),
            comp("Open interest que confirma (24 h)", None if oi is None else oi / 0.5 * sign, 25,
                 None if oi is None else f"{oi:+.3f} log", "Hyperliquid (historial de _perps.json)"),
            comp("Basis (mark − oráculo) [H: signo a medir]", None if basis is None else basis / 0.01, 20,
                 None if basis is None else f"{basis * 100:+.3f}%", "Hyperliquid"),
            comp("Momentum 24 h", None if ch24 is None else ch24 / 20, 30,
                 None if ch24 is None else f"{ch24:+.2f}%", "CoinGecko")], 1.0, 0.0, [], {}


def components_presale(asset):
    """b: calendario, narrativa, prima de pre-mercado y on-chain del listing (doc 27 §4.8)."""
    days = _f(asset.get("days_to_listing"))
    cal = None if days is None else (1.0 if -14 <= -days <= -1 else 0.5 if -2 <= days <= 0 else 0.0)
    nar = asset.get("narrative") or {}
    inten = _f(nar.get("intensity"))
    narr = None if inten is None else (clip(math.log(max(inten, 1)) / math.log(10), 0, 1) if nar.get("signal") else 0.0)
    prem = _f(asset.get("premarket_premium_pct"))
    onc = _f(asset.get("listing_onchain_pct"))
    return [comp("Calendario (días al listing)", cal, 25, None if days is None else f"{days:.1f} días", "script_99"),
            comp("Narrativa (intensidad, doc 26)", narr, 25, None if inten is None else f"{inten:.2f}", "script_115"),
            comp("Prima de pre-mercado", None if prem is None else prem / 20, 25,
                 None if prem is None else f"{prem:+.1f}%", "Hyperliquid pre-lanzamiento"),
            comp("On-chain del listing", None if onc is None else 2 * onc - 1, 25,
                 None if onc is None else f"percentil {onc:.2f}", "GeckoTerminal")], 1.0, 0.0, [], {}


def components_established(asset):
    """i: TVL, holders (n/d), fees (n/d), rotación y persistencia del volumen; −10 si el par tiene > 1 año."""
    g7, _ = _protocol_tvl_growth(asset)
    vol, liq = _f(asset.get("volume_24h_usd")), _f(asset.get("liquidity_usd"))
    turn = vol / liq if vol and liq else None
    age_d = _f(asset.get("pair_age_days"))
    adjust = -10.0 if age_d is not None and age_d > 365 else 0.0
    notes = ["Descuento por edad: −10 (par > 1 año)"] if adjust else []
    return [comp("TVL del protocolo (7d)", None if g7 is None else g7 / 0.10, 25,
                 None if g7 is None else f"{g7:+.4f}", "DefiLlama /protocols"),
            comp("Holders (crecimiento 7d)", None, 25, None, "RugCheck / GoPlus diarios (sin colectar)"),
            comp("Fees (7d vs 30d)", None, 20, None, "DefiLlama fees (sin colectar)"),
            comp("Rotación vol 24 h / liquidez", None if turn is None else math.log10(turn / 0.05), 20,
                 None if turn is None else f"{turn:.5f}", "GeckoTerminal / DexScreener"),
            comp("Persistencia del volumen", None, 10, None, "OHLCV diario (sin colectar)")], 1.0, adjust, notes, {}


def memechain_narrative(name, symbol):
    import re
    text = f"{name or ''} {symbol or ''}".lower()
    return next((k for k, pat in MEMECHAIN_NARRATIVES.items() if re.search(pat, text)), "otra")


def memechain_prior(index, chain, name=None, symbol=None):
    """Tasa base de MemeChain para una memecoin: inactividad de su chain, de su narrativa y del cruce (si n >= 30)."""
    if not isinstance(index, dict) or not index.get("all"):
        return None
    ch = MEMECHAIN_CHAIN_ALIASES.get(str(chain or "").lower())
    nar = memechain_narrative(name, symbol)
    total = (index.get("all") or {}).get("inactive_rate")
    chain_row = (index.get("by_chain") or {}).get(ch) if ch else None
    cross = ((index.get("chain_x_narrative") or {}).get(ch) or {}).get(nar) if ch else None
    return {"chain": ch, "narrative": nar, "inactive_rate_total": total,
            "inactive_rate_chain": (chain_row or {}).get("inactive_rate"),
            "inactive_rate_narrative": ((index.get("by_narrative") or {}).get(nar) or {}).get("inactive_rate"),
            "inactive_rate_cross": cross["inactive_rate"] if cross and cross.get("n", 0) >= 30 else None,
            "one_day_rate_chain": (((chain_row or {}).get("one_day") or {}).get("rate")),
            "n_chain": (chain_row or {}).get("n"), "source": "MemeChain (CC-BY-4.0, snapshot oct-2024)"}


def memechain_threshold(prior, base=None):
    """Umbral de emisión del grupo a ajustado por la tasa de inactividad de la chain contra la total [H]:
    56 + 10·(r_chain / r_total − 1), acotado a [51, 66]. Sin dato: el umbral base."""
    base = EMIT_THRESHOLD["a"] if base is None else base
    if not prior or not prior.get("inactive_rate_chain") or not prior.get("inactive_rate_total"):
        return base
    return int(round(clip(base + 10 * (prior["inactive_rate_chain"] / prior["inactive_rate_total"] - 1),
                          base - 5, base + 10)))


def memecoin_inputs(asset):
    """Pool de GeckoTerminal -> (token_data, dexscreener_data) con el formato que espera script_82.score_token."""
    created = asset.get("pool_created_at")
    try:
        created_ms = int(datetime.fromisoformat(str(created).replace("Z", "+00:00")).timestamp() * 1000)
    except ValueError:
        created_ms = None
    dx = {"priceUsd": _f(asset.get("price_usd")), "liquidityUsd": _f(asset.get("liquidity_usd")),
          "volume24hUsd": _f(asset.get("volume_24h_usd")),
          "marketCapUsd": _f(asset.get("mcap_usd")) or _f(asset.get("fdv_usd")),
          "priceChange24h": _f(asset.get("change_24h")), "priceChange_h1": _f(asset.get("change_1h")),
          "pairCreatedAt": created_ms, "pairAddress": asset.get("pool_address"), "dexId": asset.get("dex")}
    tok = {"mint": asset.get("address"), "symbol": asset.get("symbol"), "name": asset.get("name"), "score": 0}
    return tok, {k: v for k, v in dx.items() if v is not None}


MEMECOIN_FIELDS = ("priceUsd", "liquidityUsd", "volume24hUsd", "marketCapUsd", "priceChange24h", "pairCreatedAt",
                   "volume_m5", "volume_h1")


# ---------------------------------------------------------------------------
# API pública: un scorer por tipo -> (score, reasons, confidence)
# ---------------------------------------------------------------------------

def _summary(parts):
    comps, mult, adj, notes, _ = parts
    r = combine(comps, mult, adj, notes)
    return r["score"], r["reasons"], r["confidence"]


def score_blue_chip(token_data, now_ms=None):
    """BTC, ETH, SOL. GARCH(1,1), ATR, Bollinger, funding y Fear & Greed."""
    return _summary(components_blue_chip(token_data, now_ms))


def score_l1_l2(token_data, peers=(), eth_change_7d=None):
    """L1/L2 emergentes. Momentum y aceleración de TVL, actividad, fees y momentum relativo."""
    return _summary(components_l1_l2(token_data, peers, eth_change_7d))


def score_governance(token_data):
    """Gobernanza DeFi. TVL, valuación, dilución y momentum relativo (Snapshot pendiente)."""
    return _summary(components_governance(token_data))


def score_depin(token_data):
    """DePIN. Actividad (proxy de ingresos), dilución y momentum (nodos e ingresos de red: sin fuente gratuita)."""
    return _summary(components_depin(token_data))


def score_rwa(token_data):
    """RWA. TVL de la plataforma, TVL vs mcap y momentum. Los tokens estables no tienen score."""
    if is_stable_rwa(token_data):
        return None, ["RWA estable (|Δ24h| < 0,5% y |Δ7d| < 2%): sin evento que medir"], 0.0
    return _summary(components_rwa(token_data))


def score_synthetic(token_data):
    """Sintéticos / perps (d1)."""
    return _summary(components_synthetic(token_data))


def score_presale(token_data):
    """Preventa / pre-mercado (b)."""
    return _summary(components_presale(token_data))


def score_established(token_data):
    """Grupo (i). TVL, holders, fees, volumen sostenido. −10 si > 1 año."""
    return _summary(components_established(token_data))


def score_memecoin(token_data, scorer=None):
    """Memecoins multi-chain: reusa v7.2.1 (script_82.score_token). Sin GARCH/ATR/Bollinger."""
    if scorer is None:
        scorer = load_memecoin_scorer()
    tok, dx = memecoin_inputs(token_data)
    score, reasons = scorer(tok, dx)
    confidence = round(sum(1 for k in MEMECOIN_FIELDS if dx.get(k) is not None) / len(MEMECOIN_FIELDS), 4)
    return int(score), list(reasons), confidence


def load_memecoin_scorer():
    import importlib.util
    from pathlib import Path
    spec = importlib.util.spec_from_file_location("s82_mc", Path(__file__).resolve().parent / "script_82_final_detection.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.score_token


# ---------------------------------------------------------------------------
# Clasificación (doc 27 §2.2) y armado de activos desde las salidas de script_114
# ---------------------------------------------------------------------------

def classify(asset):
    """(grupo, regla). Gana la primera regla que aplica."""
    cats = set(asset.get("categories") or ())
    if asset.get("cg_id") in BLUE_CHIP_IDS:
        return "h", "1: blue chip"
    if asset.get("prelaunch"):
        return "b", "2: sin listar (calendario / pre-mercado)"
    if cats & {"synthetic-issuer", "decentralized-perpetuals"}:
        return "d", "3: categoría de sintéticos / perps"
    if "real-world-assets-rwa" in cats:
        return "g", "4: categoría RWA"
    if "depin" in cats:
        return "e", "5: categoría DePIN"
    if cats & {"layer-1", "layer-2"} or asset.get("card"):
        return "f", "6: L1/L2 o token nativo de una chain"
    if "governance" in cats:
        return "c", "7: categoría governance"
    age = _f(asset.get("pair_age_days"))
    if asset.get("source") == "onchain" and age is not None and age < 7:
        return "a", "8: memecoin nueva (pool < 7 días)"
    if asset.get("source") == "onchain" and age is not None and age > 180:
        return "i", "9: establecido sin grupo (pool > 180 días)"
    return "a", "10: por defecto"


def _age_days(iso_text, now):
    try:
        dt = datetime.fromisoformat(str(iso_text).replace("Z", "+00:00"))
    except ValueError:
        return None
    return (now - (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc))).total_seconds() / 86400


def build_assets(scan, cards=None, categories=None, protocols=None, now=None, governance=None, perps=None,
                 premarket=None, prelaunch=None):
    """Activos a puntuar: blue chips (fichas + Universo A), tokens de las categorías de CoinGecko, tokens nativos de
    las chains y pools en tendencia de GeckoTerminal fuera de Solana."""
    now = now or datetime.now(timezone.utc)
    cards = cards or {}
    cats = (categories or {}).get("categories") or {}
    protos = (protocols or {}).get("protocols") or {}
    cat_changes = [v.get("market_cap_change_24h_pct") for v in cats.values() if v.get("market_cap_change_24h_pct") is not None]
    cat_mid = statistics.median(cat_changes) if cat_changes else None
    by_id = {}
    for g, entry in ((scan or {}).get("groups") or {}).items():
        for item in entry.get("items") or []:
            if not item.get("id"):
                continue
            a = by_id.setdefault(item["id"], dict(item, cg_id=item["id"], categories=[], source="coingecko"))
            if item.get("source") in CATEGORY_IDS and item["source"] not in a["categories"]:
                a["categories"].append(item["source"])
    turnover_by_cat = {}
    for a in by_id.values():
        if a.get("volume_24h_usd") and a.get("mcap_usd"):
            for c in a["categories"]:
                turnover_by_cat.setdefault(c, []).append(a["volume_24h_usd"] / a["mcap_usd"])
    for chain, card in cards.items():
        nt = card.get("native_token") or {}
        if nt.get("id"):
            a = by_id.setdefault(nt["id"], dict(nt, cg_id=nt["id"], categories=[], source="coingecko"))
            a["card"] = card
            a["chain"] = chain
            if card.get("universe_a"):
                a["universe_a"] = card["universe_a"]
    for a in by_id.values():
        primary = a["categories"][0] if a["categories"] else None
        sample = (cats.get(primary) or {}).get("sample") or {}
        a["category"] = primary
        a["category_median_7d"] = sample.get("median_change_7d")
        cc = (cats.get(primary) or {}).get("market_cap_change_24h_pct")
        a["category_vs_market_24h"] = cc - cat_mid if cc is not None and cat_mid is not None else None
        tv = turnover_by_cat.get(primary) or []
        a["category_median_turnover"] = statistics.median(tv) if tv else None
        a["protocol"] = protos.get(a["cg_id"])
        a["key"] = f"cg:{a['cg_id']}"
        a.setdefault("chain", BLUE_CHIP_IDS.get(a["cg_id"]) and a["cg_id"])
    gov_loaded = bool((governance or {}).get("loaded"))
    proposals = (governance or {}).get("proposals") or []
    perp_rows = (perps or {}).get("perps") or {}
    oi_hist = (perps or {}).get("oi_history") or {}
    for a in by_id.values():
        sym = str(a.get("symbol") or "").upper()
        name = str(a.get("name") or "").lower()
        a["governance"] = {"loaded": gov_loaded,
                           "matches": [p for p in proposals if sym and (p.get("space_symbol") == sym or
                                                                        (name and str(p.get("space_name") or "").lower() == name))]}
        if sym in perp_rows:
            a["perp"], a["oi_history"] = perp_rows[sym], oi_hist.get(sym) or []
    assets = list(by_id.values())
    for m in (premarket or {}).get("markets") or []:
        if m.get("underlying"):
            assets.append({"key": f"pre:{str(m['underlying']).lower()}", "source": "premarket", "prelaunch": True,
                           "symbol": m["underlying"], "name": m["underlying"], "price_usd": m.get("mark_price"),
                           "premarket_type": m.get("type"), "categories": []})
    for t in (prelaunch or {}).get("tge_upcoming") or []:
        if isinstance(t, dict) and (t.get("symbol") or t.get("name")):
            assets.append({"key": f"pre:{str(t.get('symbol') or t.get('name')).lower()}", "source": "prelaunch",
                           "prelaunch": True, "symbol": t.get("symbol"), "name": t.get("name"),
                           "days_to_listing": t.get("days_to_listing"), "categories": []})
    for net, entry in ((scan or {}).get("onchain") or {}).items():
        chain = GT_TO_CHAIN.get(net)
        if not chain:
            continue
        for p in entry.get("items") or []:
            addr = p.get("token_address")
            if not addr:
                continue
            assets.append({"key": f"{chain}:{str(addr).lower() if str(addr).startswith('0x') else addr}",
                           "source": "onchain", "chain": chain, "address": addr, "symbol": p.get("symbol"),
                           "name": p.get("name"), "price_usd": p.get("price_usd"), "mcap_usd": p.get("mcap_usd"),
                           "fdv_usd": p.get("fdv_usd"), "liquidity_usd": p.get("reserve_usd"),
                           "volume_24h_usd": p.get("volume_24h_usd"), "change_1h": p.get("change_1h"),
                           "change_24h": p.get("change_24h"), "pool_created_at": p.get("pool_created_at"),
                           "pool_address": p.get("id"), "pair_age_days": _age_days(p.get("pool_created_at"), now),
                           "categories": []})
    return assets


def apply_early(score, reasons, early):
    """Fase 10: bono anticipatorio de script_116 (order book, funding/OI, Fear & Greed; lib_early_signals).
    Solo suma, con el tope que ya trae el bono. score None -> sin cambios."""
    bonus = int((early or {}).get("bonus") or 0)
    if score is None or bonus <= 0:
        return score, reasons
    note = f"Anticipación ({early.get('version', 'early')}): +{bonus} — " + "; ".join(early.get("reasons") or [])
    return int(min(100, score + bonus)), list(reasons) + [note]


def evaluate(asset, peers=(), eth_change_7d=None, memecoin_scorer=None, now=None, memechain=None, early=None):
    """Clasifica y puntúa un activo. Devuelve el detalle completo (lo que se registra y se muestra en el dossier).
    early: bono anticipatorio de este activo (02_Analisis/early/_signals.json), opcional."""
    now = now or datetime.now(timezone.utc)
    group, rule = classify(asset)
    notes_extra, extra = [], {}
    threshold = EMIT_THRESHOLD.get(group)
    if group == "a":
        score, reasons, conf = score_memecoin(asset, memecoin_scorer)
        comps = []
        prior = memechain_prior(memechain, asset.get("chain"), asset.get("name"), asset.get("symbol"))
        if prior:
            extra["memechain"] = prior
            threshold = memechain_threshold(prior)
            notes_extra.append(f"MemeChain: inactividad {prior['chain'] or 'total'} "
                               f"{prior['inactive_rate_chain'] or prior['inactive_rate_total']} -> umbral {threshold}")
    elif group == "g" and is_stable_rwa(asset):
        score, reasons, conf, comps = None, ["RWA estable: sin evento que medir"], 0.0, []
    else:
        parts = {"h": lambda: components_blue_chip(asset, int(now.timestamp() * 1000)),
                 "f": lambda: components_l1_l2(asset, peers, eth_change_7d),
                 "c": lambda: components_governance(asset), "e": lambda: components_depin(asset),
                 "g": lambda: components_rwa(asset), "d": lambda: components_synthetic(asset),
                 "b": lambda: components_presale(asset), "i": lambda: components_established(asset)}[group]()
        r = combine(*parts[:4])
        extra = parts[4]
        score, reasons, conf, comps = r["score"], r["reasons"], r["confidence"], r["components"]
    if early and group not in REGISTER_ONLY:
        score, reasons = apply_early(score, reasons, early)
        extra = dict(extra or {}, early_bonus=int(early.get("bonus") or 0))
    if group in REGISTER_ONLY:
        emit, why = False, REGISTER_ONLY[group]
    elif score is None:
        emit, why = False, "sin score"
    elif conf < MIN_COVERAGE:
        emit, why = False, f"cobertura {conf:.2f} < {MIN_COVERAGE}"
    elif score < threshold:
        emit, why = False, f"score {score} < {threshold}"
    else:
        emit, why = True, "emitible"
    return {"key": asset.get("key"), "group": group, "group_rule": rule, "scoring_version": f"mc-{group}-{VERSION}",
            "score": score, "confidence": conf, "reasons": reasons + notes_extra, "components": comps,
            "event": EVENTS[group], "threshold": threshold, "emittable": emit, "status_reason": why, "extra": extra,
            "symbol": asset.get("symbol"), "name": asset.get("name"), "chain": asset.get("chain"),
            "cg_id": asset.get("cg_id"), "address": asset.get("address"), "price_usd": _f(asset.get("price_usd")),
            "mcap_usd": _f(asset.get("mcap_usd")), "volume_24h_usd": _f(asset.get("volume_24h_usd")),
            "liquidity_usd": _f(asset.get("liquidity_usd")), "change_24h": _f(asset.get("change_24h")),
            "change_7d": _f(asset.get("change_7d")), "pool_address": asset.get("pool_address"),
            "pool_created_at": asset.get("pool_created_at"), "category": asset.get("category")}


def evaluate_all(scan, cards=None, categories=None, protocols=None, memecoin_scorer=None, now=None, governance=None,
                 perps=None, premarket=None, prelaunch=None, memechain=None, early=None):
    """Todos los activos del último scan, puntuados. Ordenados por (emitible, score).
    early: {key: bono} de script_116 (Fase 10), opcional."""
    now = now or datetime.now(timezone.utc)
    assets = build_assets(scan, cards, categories, protocols, now, governance, perps, premarket, prelaunch)
    peers = [c for c in (cards or {}).values()]
    eth = next((_f(a.get("change_7d")) for a in assets if a.get("cg_id") == "ethereum"), None)
    if memecoin_scorer is None and any(classify(a)[0] == "a" for a in assets):
        memecoin_scorer = load_memecoin_scorer()          # una sola carga de script_82 por corrida
    out = []
    for a in assets:
        try:
            out.append(evaluate(a, peers, eth, memecoin_scorer, now, memechain, (early or {}).get(a.get("key"))))
        except Exception as e:      # un activo con datos raros no frena al resto
            out.append({"key": a.get("key"), "group": None, "score": None, "emittable": False,
                        "status_reason": f"error: {type(e).__name__}: {e}", "symbol": a.get("symbol")})
    out.sort(key=lambda r: (not r.get("emittable"), -(r.get("score") or -1)))
    return out


def coverage_by_group(results):
    """Por grupo: activos evaluados, con score, con cobertura >= mínimo y emitibles (la 'cobertura' de la Fase 7)."""
    out = {}
    for r in results:
        g = r.get("group") or "?"
        row = out.setdefault(g, {"assets": 0, "scored": 0, "coverage_ok": 0, "emittable": 0})
        row["assets"] += 1
        row["scored"] += r.get("score") is not None
        row["coverage_ok"] += (r.get("confidence") or 0) >= MIN_COVERAGE
        row["emittable"] += bool(r.get("emittable"))
    return out


# ---------------------------------------------------------------------------
# Dossier multi-chain (🛒 primero, doc 24) — texto puro; script_97 lo guarda y lo adjunta
# ---------------------------------------------------------------------------

def _usd(x, fmt=",.0f"):
    return "n/d" if x is None else "$" + format(x, fmt)


def _sig(x):
    return "n/d" if x is None else format(x, "+.2f")


def render_dossier(result, acquisition_lines, detected_at, sources=()):
    """Markdown del dossier de un activo multi-chain: presentación → 🛒 → identificación → método → fundamento."""
    r = result
    name = f"{r.get('name') or r.get('symbol')} ({r.get('symbol')})"
    lines = [f"# {name} — dossier multi-chain",
             f"🎴 Grupo {r['group']} ({r['group_rule']}) · chain {r.get('chain') or 'n/d'} · precio "
             f"{_usd(r.get('price_usd'), ',.8g')} · mcap {_usd(r.get('mcap_usd'))}",
             f"Detectado {detected_at} · score {r['score']} (scoring {r['scoring_version']}, cobertura {r['confidence']:.2f})",
             "Ventana de la señal: < 48 h desde la detección.", "",
             "━━━━━━━━━━━━━━━━━━━━━━━━━━━", "## 🛒 CÓMO ADQUIRIR ESTE ACTIVO", "━━━━━━━━━━━━━━━━━━━━━━━━━━━",
             *acquisition_lines, "",
             "## 📊 Identificación", "| Campo | Valor |", "|---|---|",
             f"| Símbolo / nombre | {r.get('symbol')} / {r.get('name') or 'n/d'} |",
             f"| Id de CoinGecko | {r.get('cg_id') or 'n/d'} |", f"| Contrato | {r.get('address') or 'n/d'} |",
             f"| Chain | {r.get('chain') or 'n/d'} |", f"| Categoría | {r.get('category') or 'n/d'} |",
             f"| Volumen 24 h | {_usd(r.get('volume_24h_usd'))} |",
             f"| Cambio 24 h / 7 d | {r.get('change_24h') if r.get('change_24h') is not None else 'n/d'}% / "
             f"{r.get('change_7d') if r.get('change_7d') is not None else 'n/d'}% |", "",
             "## 🔬 Método", f"- Evento medido: {r['event']}.",
             "- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; "
             "cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.",
             "- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).", "",
             "## 🎯 Fundamento", "| Componente | Valor | sᵢ | wᵢ | Fuente |", "|---|---|---|---|---|"]
    for c in r.get("components") or []:
        lines.append(f"| {c['name']} | {c['value'] if c['value'] is not None else 'n/d'} | "
                     f"{_sig(c['s'])} | {c['w']} | {c['source']} |")
    if not r.get("components"):
        lines += [f"| {x} | | | | |" for x in r.get("reasons") or []]
    if (r.get("extra") or {}).get("garch"):
        g = r["extra"]["garch"]
        lines += ["", f"- GARCH(1,1): α={g['alpha']}, β={g['beta']}, σ próximo día {g['sigma_next'] * 100:.2f}% · "
                      f"barreras ±2σ₄₈ = ±{r['extra']['barrier_pct']:.2f}%"]
    lines += ["", f"**Total: {r['score']}** (umbral {r['threshold']}, cobertura {r['confidence']:.2f})", "",
              "## ⏱️ Vigencia", f"- < 48 h desde {detected_at}.", "", "## 📚 Fuentes",
              *[f"- {s}" for s in sources], "- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v" + VERSION]
    return "\n".join(lines) + "\n"
