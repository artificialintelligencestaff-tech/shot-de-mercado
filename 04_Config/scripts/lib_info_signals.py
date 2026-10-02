#!/usr/bin/env python3
"""
lib_info_signals.py — Señales informacionales y estructurales para tokens jóvenes (D-014-R-3). Funciones puras,
solo biblioteca estándar. Cada señal devuelve {"name", "s" (0..1), "detail"} o None si no hay dato.

Informacionales (fuente primaria para < 60 min, decisión de Dirección):
  narrative_wave     otros lanzamientos de la última hora que comparten palabra clave con el nombre/símbolo
                     (ola de una narrativa; sale del stream de PumpPortal, sin red)
  trending_match     nombre/símbolo coincide con CoinGecko trending (script_115, _index.json)
  metadata_socials   metadata del lanzamiento (IPFS de pump.fun): twitter, telegram, website, descripción
  dex_profile        perfil pago o boost en DexScreener (token-profiles / token-boosts)
  mentions           menciones por dirección (CA) o cashtag en el almacén de script_115 (_items.json: Reddit,
                     Telegram, 4chan, HN, RSS), última hora vs. 26 h
  github_repo        repositorio de GitHub enlazado en la metadata (estrellas, antigüedad)
Estructurales:
  bonding_progress   avance de la curva de pump.fun (mcap / mcap de graduación; graduado = 1)
  holders_struct     holders y concentración top-10 (RugCheck)
  dev_wallet         compra inicial del creador sobre el supply (PumpPortal initialBuy)
Parámetros heurísticos [H], no calibrados.
"""
import math
import re

VERSION = "info-0.2"
STOPWORDS = {"the", "and", "of", "to", "a", "in", "on", "for", "coin", "token", "sol", "solana", "pump", "fun",
             "official", "inu", "meme", "new", "first", "real", "ai", "is", "it", "my", "by", "with", "x"}
GRADUATION_MCAP_USD = 69_000.0        # [H] mcap aproximado en que la curva de pump.fun gradúa
PUMP_SUPPLY = 1_000_000_000


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


def _sig(name, s, detail):
    return {"name": name, "s": round(_clip01(s), 4), "detail": detail}


def keywords(*texts):
    """Palabras clave normalizadas (minúsculas, alfanuméricas, >= 3 letras, sin stopwords)."""
    out = set()
    for t in texts:
        for w in re.split(r"[^0-9a-z]+", str(t or "").lower()):
            if len(w) >= 3 and w not in STOPWORDS and not w.isdigit():
                out.add(w)
    return out


# ---------------------------------------------------------------------------
# Informacionales
# ---------------------------------------------------------------------------

def keyword_index(launches):
    """launches: [(mint, name, symbol)] de la ventana. Devuelve {palabra: {mints}}."""
    idx = {}
    for mint, name, symbol in launches:
        for k in keywords(name, symbol):
            idx.setdefault(k, set()).add(mint)
    return idx


def narrative_wave(mint, name, symbol, index, full=8):
    """Máximo de OTROS lanzamientos que comparten una palabra clave con este (8 = s 1)."""
    ks = keywords(name, symbol)
    if not ks:
        return None
    best_k, best_n = None, 0
    for k in ks:
        n = len(index.get(k, set()) - {mint})
        if n > best_n:
            best_k, best_n = k, n
    detail = f"ola '{best_k}': {best_n} lanzamientos más en 1 h" if best_k else "sin ola"
    return _sig("narrative_wave", best_n / full, detail)


def trending_match(name, symbol, trending):
    """Coincidencia con CoinGecko trending: símbolo igual (1.0) o palabra clave compartida (0.6)."""
    if not trending:
        return None
    sym = str(symbol or "").strip().upper()
    ks = keywords(name, symbol)
    for t in trending:
        if sym and sym == str(t.get("symbol") or "").upper():
            return _sig("trending_match", 1.0, f"símbolo = trending #{t.get('rank')} {t.get('name')}")
    for t in trending:
        shared = ks & keywords(t.get("name"), t.get("symbol"))
        if shared:
            return _sig("trending_match", 0.6, f"'{sorted(shared)[0]}' en trending #{t.get('rank')} {t.get('name')}")
    return _sig("trending_match", 0.0, "sin coincidencia con trending")


def metadata_socials(meta):
    """meta: JSON de la metadata del lanzamiento (twitter, telegram, website, description)."""
    if not isinstance(meta, dict):
        return None
    links = [k for k in ("twitter", "telegram", "website") if str(meta.get(k) or "").strip()]
    desc = len(str(meta.get("description") or "").strip())
    s = 0.8 * len(links) / 3 + (0.2 if desc >= 40 else 0.0)
    return _sig("metadata_socials", s, f"enlaces {links or 'ninguno'} · descripción {desc} caracteres")


def dex_profile(mint, profiles, boosts):
    """profiles: {mints con perfil pago}; boosts: {mint: monto total de boost}."""
    if profiles is None and boosts is None:
        return None
    has_profile = mint in (profiles or set())
    boost = _num((boosts or {}).get(mint)) or 0.0
    s = (0.6 if has_profile else 0.0) + 0.4 * _clip01(boost / 500)
    detail = ("perfil pago en DexScreener" if has_profile else "sin perfil") + (f" · boost {boost:g}" if boost else "")
    return _sig("dex_profile", s, detail)


def mentions(mint, symbol, items, now_s, full=5.0):
    """items: almacén de script_115 (_items.json → items: {"ts", "a": [direcciones], "c": [cashtags], "f"}).
    Peso: dirección 1, cashtag 0,25. Última hora; s = 1 con 5 menciones ponderadas."""
    if items is None:
        return None
    sym = str(symbol or "").strip().upper()
    w1, w26, fams = 0.0, 0.0, set()
    for it in items:
        if not isinstance(it, dict):
            continue
        w = 1.0 if mint in (it.get("a") or []) else (0.25 if sym and sym in [str(c).upper() for c in it.get("c") or []]
                                                     else 0.0)
        if not w:
            continue
        w26 += w
        if now_s - 3600 < (_num(it.get("ts")) or 0) <= now_s:
            w1 += w
            fams.add(it.get("f"))
    return _sig("mentions", w1 / full, f"menciones 1 h {w1:g} ({len(fams)} familias) · 26 h {w26:g}")


def github_repo(repo):
    """repo: respuesta de api.github.com/repos/{o}/{r} (stargazers_count, created_at, pushed_at)."""
    if not isinstance(repo, dict) or "stargazers_count" not in repo:
        return None
    stars = _num(repo.get("stargazers_count")) or 0.0
    return _sig("github_repo", math.log10(1 + stars) / 2, f"repo {repo.get('full_name')} · {stars:g} estrellas")


def github_link(meta):
    """'owner/repo' si la metadata enlaza un repositorio de GitHub."""
    for k in ("website", "twitter", "telegram", "description"):
        m = re.search(r"github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)", str((meta or {}).get(k) or ""))
        if m:
            return f"{m.group(1)}/{m.group(2).removesuffix('.git')}"
    return None


# ---------------------------------------------------------------------------
# Estructurales
# ---------------------------------------------------------------------------

def bonding_progress(dx, graduation_mcap=GRADUATION_MCAP_USD):
    """Curva de pump.fun: mcap / mcap de graduación. Par fuera de pump.fun (pumpswap, raydium) = graduado."""
    dx = dx or {}
    dex = str(dx.get("dexId") or "").lower()
    mcap = _num(dx.get("marketCapUsd"))
    if dex and dex != "pumpfun":
        return _sig("bonding_progress", 1.0, f"graduado ({dex})")
    if mcap is None:
        return None
    return _sig("bonding_progress", mcap / graduation_mcap, f"curva {100 * mcap / graduation_mcap:.0f} %")


def holders_struct(rug, full_holders=300, max_top10=30.0):
    if not isinstance(rug, dict) or _num(rug.get("holders")) is None:
        return None
    holders, top10 = _num(rug.get("holders")), _num(rug.get("top10_pct"))
    s = _clip01(holders / full_holders) * (0.5 if top10 is not None and top10 > max_top10 else 1.0)
    return _sig("holders_struct", s, f"holders {holders:.0f}" + (f" · top-10 {top10:.1f} %" if top10 is not None else ""))


def dev_wallet(token, lo_pct=2.0, hi_pct=10.0):
    """Compra inicial del creador: <= 2 % del supply = 1; >= 10 % = 0."""
    buy = _num((token or {}).get("initialBuy"))
    if buy is None:
        return None
    pct = 100 * buy / PUMP_SUPPLY
    return _sig("dev_wallet", 1 - (pct - lo_pct) / (hi_pct - lo_pct), f"creador compró {pct:.1f} % del supply")


# ---------------------------------------------------------------------------
# D-023-R3: señales estructurales nuevas (S-1..S-4) y flag de tradability
# ---------------------------------------------------------------------------

def bonding_curve_velocity(series, full_pct_per_min=2.0, window_s=600):
    """S-1. series: [(ts, progreso 0..1)] de polls propios (DexScreener mcap / mcap de graduación). Δ% de curva por
    minuto en la ventana (10 min); 2 %/min = s 1 [H]. Retroceso = 0 (no resta)."""
    pts = sorted((t, _num(p)) for t, p in series or [] if _num(p) is not None)
    if len(pts) < 2:
        return None
    t1, p1 = pts[-1]
    base = [x for x in pts if x[0] >= t1 - window_s and x[0] < t1] or [pts[-2]]
    t0, p0 = base[0]
    if t1 - t0 <= 0:
        return None
    rate = 100 * (p1 - p0) / ((t1 - t0) / 60)
    return _sig("bonding_curve_velocity", rate / full_pct_per_min, f"curva {rate:+.2f} %/min")


def _buys(trades):
    """trades: [(ts, wallet, side, sol)] del stream de PumpPortal (subscribeTokenTrade)."""
    return sorted((t for t in trades or [] if t and len(t) >= 4 and str(t[2]).lower() == "buy"), key=lambda t: t[0])


def unique_buyer_acceleration(trades, now_s, window_s=120, full_per_min=5.0):
    """S-2. Compradores únicos NUEVOS en la última ventana vs. la anterior (Δ por minuto); +5/min = s 1 [H]."""
    buys = _buys(trades)
    if not buys:
        return None
    seen_before = {t[1] for t in buys if t[0] < now_s - window_s}
    prev_win = {t[1] for t in buys if now_s - 2 * window_s <= t[0] < now_s - window_s}
    last_win = {t[1] for t in buys if t[0] >= now_s - window_s} - seen_before
    accel = (len(last_win) - len(prev_win)) / (window_s / 60)
    return _sig("unique_buyer_acceleration", accel / full_per_min,
                f"compradores nuevos {len(last_win)} vs {len(prev_win)} ({accel:+.1f}/min)")


def avg_buy_size_trend(trades, n=30, full_change=1.0):
    """S-3. Pendiente (mínimos cuadrados) del tamaño de compra en SOL sobre las últimas n compras, expresada como
    cambio relativo a lo largo de la ventana; +100 % = s 1 [H]. Requiere >= 5 compras."""
    buys = _buys(trades)[-n:]
    ys = [_num(t[3]) for t in buys if _num(t[3]) is not None]
    if len(ys) < 5:
        return None
    m = len(ys)
    xm, ym = (m - 1) / 2, sum(ys) / m
    den = sum((i - xm) ** 2 for i in range(m))
    slope = sum((i - xm) * (y - ym) for i, y in enumerate(ys)) / den if den else 0.0
    change = slope * (m - 1) / ym if ym > 0 else 0.0
    return _sig("avg_buy_size_trend", change / full_change,
                f"tamaño de compra {change:+.0%} en {m} compras (media {ym:.3f} SOL)")


def holder_to_txn_ratio(holders, txns, full_ratio=0.5):
    """S-4. holders únicos / txns totales: alto = participación distribuida; bajo = pocas billeteras operando mucho
    (bots / wash). 0,5 = s 1 [H]. holders de RugCheck (o compradores únicos del stream); txns de DexScreener."""
    h, x = _num(holders), _num(txns)
    if h is None or x is None or x <= 0:
        return None
    ratio = h / x
    return _sig("holder_to_txn_ratio", ratio / full_ratio, f"holders/txns {h:.0f}/{x:.0f} = {ratio:.2f}")


def tradability(dx, liquidity_series=None, min_liq_usd=1_000.0):
    """D-023-R3 T4: flag informativo (no bloquea ni suma). tradable: hay precio y una ruta de compra (curva de
    pump.fun abierta, o pool con liquidez >= min_liq_usd). initial_liquidity_usd: primera liquidez vista."""
    dx = dx or {}
    dex = str(dx.get("dexId") or "").lower()
    liq = _num(dx.get("liquidityUsd")) or 0.0
    price = _num(dx.get("priceUsd")) or 0.0
    first = next((_num(v) for _, v in sorted(liquidity_series or [], key=lambda p: p[0]) if _num(v) is not None), None)
    if dex == "pumpfun":
        route = "pump.fun (curva de bonding)"
    elif dex:
        route = f"{dex} (AMM) vía Jupiter o el DEX"
    else:
        route = "desconocida"
    tradable = price > 0 and (dex == "pumpfun" or liq >= min_liq_usd)
    return {"tradable": bool(tradable), "liquidity_usd": round(liq, 2), "buy_route": route,
            "initial_liquidity_usd": round(first, 2) if first is not None else None}
