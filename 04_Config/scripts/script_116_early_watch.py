#!/usr/bin/env python3
"""
script_116_early_watch.py — Vigilancia temprana (Fase 10, T3–T6). Poll cada 2 min dentro de un job largo.

Por qué: la latencia medida (latency_analysis.json) la dominan el cron */20 con ~12 min de retraso del scheduler
de Actions, la escucha de PumpPortal de solo 5 min por corrida (75 % de los lanzamientos no se ven) y el chequeo
de la edad mínima que llega en promedio 10 min tarde. Este proceso corre en bucle (LOOP_MINUTES, por defecto 40;
el workflow lo relanza cada 30 min) y:

  1. Escucha PumpPortal en continuo (subscribeNewToken) con el mismo filtro de script_82.
  2. Cada POLL_SECONDS (120): watchlist = esos lanzamientos + candidatos recientes de _accumulated.json (score >= 40,
     últimas 6 h, no alertados). DexScreener en lotes de 30 (tokens/v1), re-puntúa con script_82.score_token
     (v7.2.1, sin cambios) y suma el bono anticipatorio de lib_early_signals (solo suma, tope 8):
       flujo (aceleración de volumen, presión compradora, acumulación con precio quieto, entrada de liquidez),
       on-chain (RugCheck: holders/min y top-10, T5) y social (script_115 / doc 26 + CoinGecko trending, T6).
  3. Emite en cuanto score + bono >= EMIT_MIN_SCORE (56) con edad >= la edad mínima y guía de compra (regla
     núcleo). Edad mínima (Fase 10b): 10 min por defecto; early_review.py la sube a 15 en _gate.json si la
     primaria de las alertas tempranas da < 40 %; EARLY_MIN_AGE_MIN (env) la fija a mano. Mensaje = el de script_97.
  4. Dos instancias en paralelo (EARLY_INSTANCE a = early_watch.yml en :07/:37, b = early_watch_b.yml en :22/:52):
     PumpPortal escuchado por dos conexiones desfasadas. Sin doble emisión: antes de enviar, cada instancia
     pushea el reclamo 02_Analisis/early/alerts/<mint>.json; si ya está en origin/main, lo emitió la otra y no se
     envía (Git.claim). pipeline_t0 adopta esos registros en _all_alerts.json (script_98 los sigue) con dossier.
  5. Order book (T4): Hyperliquid l2Book -> dYdX v4 -> Phoenix para perps multi-chain (+ funding/OI) ->
     _signals_<inst>.json, que script_97 suma como bono; Raydium CLMM (/pools/line/position) para tokens Solana
     en pools concentrados.

Mientras alguna instancia está corriendo, script_97 deja la ruta Solana en sus manos: ver
script_97.early_watch_active.

Archivos propios por instancia: 02_Analisis/early/{_watch_<inst>.json, _signals_<inst>.json}; compartidos sin
conflicto (un archivo por mint): early/alerts/<mint>.json y alert_<mint>_<ts>.json. Bitácora "early_watch_<inst>".
Cobertura de PumpPortal: listener_intervals en _watch_<inst>.json (early_review.py mide la unión en 24 h).

Uso: python 04_Config/scripts/script_116_early_watch.py [--loop-minutes 40] [--poll-seconds 120] [--once]
                                                       [--no-git] [--no-listen] [--dry-run]
"""
import argparse
import asyncio
import json
import os
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_early_signals as es  # noqa: E402
import lib_info_signals as inf  # noqa: E402
import lib_scoring_young as ly  # noqa: E402

ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
VERSION = "116-0.3"
INSTANCE = (os.environ.get("EARLY_INSTANCE") or "a").strip().lower() or "a"   # Fase 10b: a (:07/:37), b (:22/:52)
EARLY_DIR_REL = "02_Analisis/early"
CLAIMS_REL = f"{EARLY_DIR_REL}/alerts"      # un archivo por mint = reclamo de la emisión entre instancias
GATE_FILE_REL = f"{EARLY_DIR_REL}/_gate.json"
EARLY_MIN_AGE_MIN_DEFAULT = 10              # Fase 10b (Dirección): 30 -> 10; early_review puede subirlo a 15
PHOENIX_BOOK = "https://perp-api.phoenix.trade/v1/view/orderbook/{symbol}"
RAYDIUM_LINE = "https://api-v3.raydium.io/pools/line/position?id={pool}"
DEX_BATCH_URL = "https://api.dexscreener.com/tokens/v1/solana/{mints}"
DEX_PROFILES_URL = "https://api.dexscreener.com/token-profiles/latest/v1"
DEX_BOOSTS_URL = "https://api.dexscreener.com/token-boosts/latest/v1"
GITHUB_REPO_URL = "https://api.github.com/repos/{repo}"
YOUNG_DIR_REL = "02_Analisis/early/young"     # D-014-R-3: registro JSONL por token del scorer joven
META_PER_POLL = 40                            # metadata IPFS de lanzamientos nuevos por poll
META_BUDGET_S = 25                            # tope de tiempo por poll para la metadata (poll de 120 s)
GITHUB_PER_POLL = 1                           # API de GitHub sin token: 60/h por IP
YOUNG_NEAR = 15                               # RugCheck para jóvenes con score >= umbral − 15
DEX_BATCH = 30
RUGCHECK_URL = "https://api.rugcheck.xyz/v1/tokens/{mint}/report"
HYPERLIQUID_INFO = "https://api.hyperliquid.xyz/info"
DYDX_BOOK = "https://indexer.dydx.trade/v4/orderbooks/perpetualMarket/{ticker}-USD"
PUMPPORTAL_WS = "wss://pumpportal.fun/api/data"

POLL_SECONDS = int(os.environ.get("EARLY_POLL_SECONDS") or 120)
LOOP_MINUTES = int(os.environ.get("EARLY_LOOP_MINUTES") or 40)
WATCH_MIN_SCORE = 40
WATCH_HOURS = 6
PP_MAX_AGE_MIN = 180            # un lanzamiento de PumpPortal se vigila hasta 3 h
WATCH_CAP = 900
MAX_PER_POLL = 3                # igual que script_97 por ciclo
NEAR_THRESHOLD = es.BONUS_CAP   # RugCheck solo para los que el bono puede llevar al umbral
RUGCHECK_PER_POLL = 8
RUGCHECK_REFRESH_S = 300
OB_TOP_N = 25
SERIES_KEEP = 40                # puntos de liquidez / holders / funding guardados por activo
COMMIT_EVERY_S = 600
GROUP_I_MIN_AGE_MIN = 180 * 1440   # script_82.GROUP_I_MIN_AGE_DAYS
STORED_SCORE_MAX_AGE_MIN = 60      # script_97.CANDIDATE_MAX_AGE_MIN
CLMM_PER_POLL = 6
CLMM_REFRESH_S = 240
COVERAGE_KEEP_S = 26 * 3600        # intervalos de conexión de PumpPortal que se guardan (early_review mide 24 h)


def instance_paths(instance=None):
    """Archivos propios de una instancia: dos early watch en paralelo nunca escriben el mismo archivo."""
    inst = instance or INSTANCE
    return {"watch": f"{EARLY_DIR_REL}/_watch_{inst}.json", "signals": f"{EARLY_DIR_REL}/_signals_{inst}.json",
            "op": f"early_watch_{inst}"}


def merge_intervals(intervals):
    """Unión de [inicio, fin]: colapsa solapados (el intervalo abierto del listener crece en cada poll y el archivo
    guarda versiones anteriores del mismo intervalo)."""
    out = []
    for a, b in sorted((float(i[0]), float(i[1])) for i in intervals or []
                       if isinstance(i, (list, tuple)) and len(i) == 2 and i[1] >= i[0]):
        if out and a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


def claim_rel(mint):
    return f"{CLAIMS_REL}/{mint}.json"


def resolve_min_age(root, env=None):
    """Edad mínima de emisión: EARLY_MIN_AGE_MIN (env, manual) > _gate.json (early_review) > 10 por defecto."""
    env = os.environ if env is None else env
    if (env.get("EARLY_MIN_AGE_MIN") or "").strip():
        return int(env["EARLY_MIN_AGE_MIN"])
    gate = read_json(Path(root) / GATE_FILE_REL, {})
    try:
        return int(gate.get("early_min_age_min"))
    except (TypeError, ValueError, AttributeError):
        return EARLY_MIN_AGE_MIN_DEFAULT


def now_iso(ts=None):
    return datetime.fromtimestamp(ts if ts is not None else time.time(), timezone.utc).isoformat(timespec="seconds")


def parse_iso(value):
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None
    return (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).timestamp()


def read_json(path, default):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def write_json_atomic(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def isolated_scorer(score_token, workdir=None):
    """script_82.score_token relee _accumulated.json (11 MB, ruta relativa al cwd) en cada llamada para buscar un
    buy_pressure previo que ningún registro guarda (0 de 6956 en main, 2026-10-01): con 900 tokens por poll eso son
    minutos. Se lo llama desde un directorio vacío: mismo resultado, sin la relectura."""
    import tempfile
    workdir = workdir or tempfile.mkdtemp(prefix="s116_")

    def score(token_data, dx):
        prev = os.getcwd()
        os.chdir(workdir)
        try:
            return score_token(token_data, dx)
        finally:
            os.chdir(prev)
    return score


def _load_module(name, filename):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# DexScreener
# ---------------------------------------------------------------------------

def _f(x):
    try:
        return float(x or 0)
    except (TypeError, ValueError):
        return 0.0


def flatten_pair(best):
    """Mismo formato que script_82.fetch_dexscreener (el scorer v7.2.1 lo espera así)."""
    txns, volume, change = best.get("txns") or {}, best.get("volume") or {}, best.get("priceChange") or {}
    return {
        "priceUsd": _f(best.get("priceUsd")), "liquidityUsd": _f((best.get("liquidity") or {}).get("usd")),
        "volume24hUsd": _f(volume.get("h24")), "marketCapUsd": _f(best.get("marketCap")),
        "priceChange24h": _f(change.get("h24")), "dexId": best.get("dexId", ""),
        "pairAddress": best.get("pairAddress", ""),
        "volume_m5": _f(volume.get("m5")), "volume_h1": _f(volume.get("h1")), "volume_h6": _f(volume.get("h6")),
        "txns_m5_buys": int(_f((txns.get("m5") or {}).get("buys"))),
        "txns_m5_sells": int(_f((txns.get("m5") or {}).get("sells"))),
        "txns_h1_buys": int(_f((txns.get("h1") or {}).get("buys"))),
        "txns_h1_sells": int(_f((txns.get("h1") or {}).get("sells"))),
        "priceChange_m5": _f(change.get("m5")), "priceChange_h1": _f(change.get("h1")),
        "pairCreatedAt": int(_f(best.get("pairCreatedAt"))),
        "labels": list(best.get("labels") or []),
    }


def best_pairs(pairs):
    """{mint del token base: par aplanado de mayor liquidez}."""
    best = {}
    for p in pairs or []:
        if not isinstance(p, dict):
            continue
        mint = (p.get("baseToken") or {}).get("address")
        if not mint:
            continue
        liq = _f((p.get("liquidity") or {}).get("usd"))
        if mint not in best or liq > best[mint][0]:
            best[mint] = (liq, p)
    return {m: flatten_pair(p) for m, (_, p) in best.items()}


def dexscreener_batch(get, mints, sleep=time.sleep):
    out, mints = {}, list(mints)
    for i in range(0, len(mints), DEX_BATCH):
        chunk = mints[i:i + DEX_BATCH]
        try:
            r = get(DEX_BATCH_URL.format(mints=",".join(chunk)), timeout=20)
            data = r.json() if r.status_code == 200 else []
        except Exception:
            data = []
        out.update(best_pairs(data if isinstance(data, list) else (data or {}).get("pairs")))
        if i + DEX_BATCH < len(mints):
            sleep(0.25)
    return out


# ---------------------------------------------------------------------------
# Watchlist
# ---------------------------------------------------------------------------

def normalize_mint(mint):
    return str(mint or "").strip()


def watch_from_accumulated(accumulated, alerted, now, min_score=WATCH_MIN_SCORE, hours=WATCH_HOURS):
    out = {}
    for mint, tok in (accumulated or {}).items():
        if not isinstance(tok, dict) or normalize_mint(mint) in alerted:
            continue
        if (tok.get("score") or 0) < min_score or tok.get("group") == "i":
            continue
        det = parse_iso(tok.get("detected_at"))
        if det is None or now - det > hours * 3600:
            continue
        out[mint] = {"source": tok.get("source") or "accumulated", "token": tok.get("token") or {},
                     "windows": tok.get("windows"), "since": tok.get("detected_at"),
                     "score_82": tok.get("score")}
    return out


def merge_launches(watch, launches, now):
    for t in launches:
        mint = normalize_mint(t.get("mint"))
        if mint and mint not in watch:
            watch[mint] = {"source": "pumpportal_live", "token": t, "since": t.get("timestamp") or now_iso(now)}
    return watch


def prune_watch(watch, alerted, now, max_age_min=PP_MAX_AGE_MIN, cap=WATCH_CAP):
    keep = {}
    for mint, e in watch.items():
        if mint in alerted:
            continue
        since = parse_iso(e.get("since"))
        if e.get("source") == "pumpportal_live" and since is not None and now - since > max_age_min * 60:
            continue
        keep[mint] = e
    if len(keep) > cap:
        newest = sorted(keep, key=lambda m: parse_iso(keep[m].get("since")) or 0, reverse=True)[:cap]
        keep = {m: keep[m] for m in newest}
    return keep


# ---------------------------------------------------------------------------
# Evaluación
# ---------------------------------------------------------------------------

def push_series(state, bucket, key, point, keep=SERIES_KEEP):
    series = state.setdefault(bucket, {}).setdefault(key, [])
    series.append(point)
    del series[:-keep]
    return series


def narrative_signal(root, mint):
    doc = read_json(Path(root) / "02_Analisis" / "narrative" / f"{mint}.json", None)
    if not isinstance(doc, dict):
        return None
    return es.social_velocity(doc.get("snapshot"), doc.get("coingecko_trending"))


def holders_signal(state, mint):
    snaps = (state.get("holders") or {}).get(mint) or []
    return es.holder_accumulation([(s["ts"], s.get("holders"), s.get("top10_pct")) for s in snaps])


def evaluate(mint, entry, dx, state, now, scorer, root, min_age_min, threshold, info_ctx=None):
    """Score v7.2.1 con datos frescos + bono anticipatorio. Devuelve el resultado (sin efectos salvo las series).
    D-014-R-3: con info_ctx (scorer joven activo) y par de < 60 min, puntúa lib_scoring_young (evaluate_young)."""
    created0 = dx.get("pairCreatedAt") or 0
    if info_ctx is not None and created0 > 0 and (now - created0 / 1000) / 60 < ly.SCOPE_MAX_AGE_MIN:
        return evaluate_young(mint, entry, dx, state, now, root, min_age_min, info_ctx)
    base, reasons = scorer(entry.get("token") or {}, dx)
    # Paridad con script_97: dentro de los 60 min de la detección vale el score de script_82 si es mayor
    stored, det = entry.get("score_82"), parse_iso(entry.get("since"))
    if isinstance(stored, (int, float)) and det is not None and now - det <= STORED_SCORE_MAX_AGE_MIN * 60 \
            and stored > base:
        reasons = list(reasons) + [f"score de detección {stored} (script_82, hace {round((now - det) / 60)} min) "
                                   f"> re-score {base}: vale el de detección (paridad con script_97)"]
        base = int(stored)
    liq = push_series(state, "liquidity", mint, [now, dx.get("liquidityUsd")])
    signals = es.dex_signals(dx, [(t, v) for t, v in liq]) + [holders_signal(state, mint), narrative_signal(root, mint),
                                                              clmm_signal(state, mint, now)]
    early = es.combine(signals)
    score = es.apply_bonus(base, early)
    created = dx.get("pairCreatedAt") or 0
    age = (now - created / 1000) / 60 if created > 0 else None
    if score < threshold:
        why = f"score {score} < {threshold}"
    elif age is None:
        why = "edad desconocida"
    elif age < min_age_min:
        why = f"edad {age:.1f} < {min_age_min} min"
    elif age > GROUP_I_MIN_AGE_MIN:
        why = "grupo i (par > 180 días): registro, no emisión"
    elif not dx.get("priceUsd"):
        why = "sin precio"
    else:
        why = "emitible"
    return {"mint": mint, "score_base": base, "early": early, "score": score, "reasons": reasons,
            "age_min": round(age, 1) if age is not None else None, "emittable": why == "emitible", "why": why,
            "pool": dx.get("pairAddress"), "dex_id": dx.get("dexId"), "labels": dx.get("labels") or [],
            "price": dx.get("priceUsd")}


def young_signals(mint, entry, dx, state, now, info_ctx):
    """Señales del scorer joven: (precio/volumen, informacionales, estructurales, rug)."""
    tok = entry.get("token") or {}
    name, symbol = tok.get("name"), tok.get("symbol")
    liq = push_series(state, "liquidity", mint, [now, dx.get("liquidityUsd")])
    price = es.dex_signals(dx, [(t, v) for t, v in liq]) + [holders_signal(state, mint)]
    meta = (state.get("meta") or {}).get(mint, {}).get("data")
    repo = github_link_cached(state, meta)
    info = [inf.narrative_wave(mint, name, symbol, info_ctx.get("keywords") or {}),
            inf.trending_match(name, symbol, info_ctx.get("trending")),
            inf.metadata_socials(meta),
            inf.dex_profile(mint, info_ctx.get("profiles"), info_ctx.get("boosts")),
            inf.mentions(mint, symbol, info_ctx.get("items"), now),
            inf.github_repo(repo)]
    snaps = (state.get("holders") or {}).get(mint) or []
    rug = snaps[-1] if snaps else None
    struct = [inf.bonding_progress(dx), inf.holders_struct(rug), inf.dev_wallet(tok)]
    return price, info, struct, rug


def evaluate_young(mint, entry, dx, state, now, root, min_age_min, info_ctx):
    """Scorer joven (< 60 min): 60 % informacional / 25 % estructural / 15 % precio-volumen. Registra en JSONL."""
    price, info, struct, rug = young_signals(mint, entry, dx, state, now, info_ctx)
    token_data = {"token": entry.get("token") or {}, "dexscreener": dx}
    d = ly.score_young_detail(token_data, price, info, now, rug, struct)
    early = es.combine(price)
    early.update(bonus=0, reasons=[])                     # el precio/volumen ya está dentro del score joven
    age, score = d["age_min"], d["score"]
    if not d["fires"]:
        why = (f"joven: score {score} < {ly.YOUNG_THRESHOLD}" if score < ly.YOUNG_THRESHOLD
               else f"joven: info {d['parts']['info']:.0f} < {ly.INFO_MIN}")
    elif age < min_age_min:
        why = f"edad {age:.1f} < {min_age_min} min"
    elif not dx.get("priceUsd"):
        why = "sin precio"
    else:
        why = "emitible"
    log = state.setdefault("ylog", {})
    if info_ctx.get("log_path") and ly.should_log(log.get(mint), d):
        sym = (entry.get("token") or {}).get("symbol")
        ly.append_jsonl(Path(root) / info_ctx["log_path"],
                        ly.young_record(mint, sym, d, price, info, struct, now_iso(now), info_ctx.get("instance")))
        log[mint] = score
    return {"mint": mint, "score_base": score, "early": early, "score": score, "reasons": d["reasons"],
            "age_min": age, "emittable": why == "emitible", "why": why, "pool": dx.get("pairAddress"),
            "dex_id": dx.get("dexId"), "labels": dx.get("labels") or [], "price": dx.get("priceUsd"),
            "scorer": "young", "scoring_version": ly.VERSION, "young": d,
            "near": score is not None and score >= ly.YOUNG_THRESHOLD - YOUNG_NEAR,
            "signals_young": (price, info, struct)}


def github_link_cached(state, meta):
    repo = inf.github_link(meta) if meta else None
    return ((state.get("gh") or {}).get(repo) or {}).get("data") if repo else None


def young_info_context(ctx, root, watch, now, get):
    """Contexto informacional del poll: trending y menciones (script_115), perfiles/boosts de DexScreener (2
    llamadas), índice de palabras clave de los lanzamientos de la última hora. Y trae metadata IPFS de los
    lanzamientos nuevos y, con cupo, el repo de GitHub enlazado."""
    state = ctx["state"]
    idx_doc = read_json(root / "02_Analisis" / "narrative" / "_index.json", {}) or {}
    items_doc = read_json(root / "02_Analisis" / "narrative" / "_items.json", {}) or {}
    profiles, boosts = set(), {}
    for url, kind in ((DEX_PROFILES_URL, "p"), (DEX_BOOSTS_URL, "b")):
        try:
            r = get(url, timeout=15)
            data = r.json() if r.status_code == 200 else []
        except Exception:
            data = []
        for row in data if isinstance(data, list) else []:
            if not isinstance(row, dict) or str(row.get("chainId")) != "solana" or not row.get("tokenAddress"):
                continue
            if kind == "p":
                profiles.add(row["tokenAddress"])
            else:
                boosts[row["tokenAddress"]] = max(boosts.get(row["tokenAddress"], 0),
                                                  _f(row.get("totalAmount") or row.get("amount")))
    launches = []
    for mint, e in watch.items():
        since = parse_iso(e.get("since"))
        tok = e.get("token") or {}
        if since is not None and now - since <= 3600:
            launches.append((mint, tok.get("name"), tok.get("symbol")))
    meta = state.setdefault("meta", {})
    fetched, t_start = 0, time.monotonic()
    for mint, e in watch.items():
        uri = (e.get("token") or {}).get("uri")
        if fetched >= META_PER_POLL or time.monotonic() - t_start > META_BUDGET_S:
            break
        if not uri or mint in meta:
            continue
        fetched += 1
        try:
            r = get(uri, timeout=6)
            data = r.json() if r.status_code == 200 else None
        except Exception:
            data = None
        slim = {k: str(data.get(k) or "")[:160] for k in ("twitter", "telegram", "website", "description")} \
            if isinstance(data, dict) else None
        meta[mint] = {"ts": now, "data": slim}
    gh = state.setdefault("gh", {})
    asked = 0
    for mint in watch:
        repo = inf.github_link((meta.get(mint) or {}).get("data"))
        if not repo or repo in gh or asked >= GITHUB_PER_POLL:
            continue
        asked += 1
        try:
            r = get(GITHUB_REPO_URL.format(repo=repo), timeout=10)
            data = r.json() if r.status_code == 200 else None
        except Exception:
            data = None
        gh[repo] = {"ts": now, "data": {k: data.get(k) for k in ("full_name", "stargazers_count", "created_at",
                                                                 "pushed_at")} if isinstance(data, dict) else None}
    day = datetime.fromtimestamp(now, timezone.utc).strftime("%Y-%m-%d")
    inst = ctx.get("instance") or INSTANCE
    return {"trending": idx_doc.get("coingecko_trending"), "items": items_doc.get("items"),
            "profiles": profiles, "boosts": boosts, "keywords": inf.keyword_index(launches),
            "log_path": f"{YOUNG_DIR_REL}/{inst}_{day}.jsonl", "instance": inst}


def rugcheck_targets(results, state, now, threshold, per_poll=RUGCHECK_PER_POLL, refresh_s=RUGCHECK_REFRESH_S):
    near = [r for r in results if r.get("near") if "near" in r] + [
        r for r in results if "near" not in r and r["score_base"] is not None
        and r["score_base"] + NEAR_THRESHOLD >= threshold]
    near.sort(key=lambda r: -r["score_base"])
    out = []
    for r in near:
        snaps = (state.get("holders") or {}).get(r["mint"]) or []
        if snaps and now - snaps[-1]["ts"] < refresh_s:
            continue
        out.append(r["mint"])
        if len(out) >= per_poll:
            break
    return out


def fetch_rugcheck(get, mint, now):
    try:
        r = get(RUGCHECK_URL.format(mint=mint), timeout=20)
        if r.status_code != 200:
            return None
        return es.rugcheck_snapshot(r.json(), now)
    except Exception:
        return None


def is_clmm(result):
    return str(result.get("dex_id") or "").lower() == "raydium" and any(
        "clmm" in str(x).lower() for x in result.get("labels") or [])


def clmm_targets(results, state, now, threshold, per_poll=CLMM_PER_POLL, refresh_s=CLMM_REFRESH_S):
    """Pools CLMM de Raydium al alcance del bono, sin snapshot reciente."""
    out = []
    for r in sorted(results, key=lambda r: -(r.get("score_base") or 0)):
        if r.get("score_base") is None or r["score_base"] + NEAR_THRESHOLD < threshold or not is_clmm(r):
            continue
        last = (state.get("clmm") or {}).get(r["mint"])
        if last and now - last["ts"] < refresh_s:
            continue
        out.append(r)
        if len(out) >= per_poll:
            break
    return out


def raydium_line_points(data):
    """/pools/line/position -> [(precio, liquidez)]. Acepta la lista directa o {"data": {"line": [...]}}."""
    body = data.get("data") if isinstance(data, dict) else data
    if isinstance(body, dict):
        body = body.get("line") or body.get("data") or []
    out = []
    for p in body or []:
        if isinstance(p, dict):
            out.append((p.get("price"), p.get("liquidity")))
        elif isinstance(p, (list, tuple)) and len(p) >= 2:
            out.append((p[0], p[1]))
    return out


def fetch_clmm(get, result, now):
    try:
        r = get(RAYDIUM_LINE.format(pool=result["pool"]), timeout=15)
        pts = raydium_line_points(r.json()) if r.status_code == 200 else []
    except Exception:
        pts = []
    sig = es.clmm_imbalance(pts, result.get("price")) if pts else None
    return {"ts": now, "signal": sig} if sig else None


def clmm_signal(state, mint, now, max_age_s=2 * CLMM_REFRESH_S):
    snap = (state.get("clmm") or {}).get(mint)
    if not snap or now - snap["ts"] > max_age_s:
        return None
    return snap["signal"]


# ---------------------------------------------------------------------------
# Multi-chain: order book + funding (T4)
# ---------------------------------------------------------------------------

def hyperliquid_book(post, coin):
    try:
        r = post(HYPERLIQUID_INFO, json={"type": "l2Book", "coin": coin}, timeout=15)
        levels = (r.json() or {}).get("levels") if r.status_code == 200 else None
    except Exception:
        levels = None
    if not levels or len(levels) != 2:
        return None
    return levels[0], levels[1]


def dydx_book(get, ticker):
    try:
        r = get(DYDX_BOOK.format(ticker=ticker), timeout=15)
        data = r.json() if r.status_code == 200 else None
    except Exception:
        data = None
    if not isinstance(data, dict) or not data.get("bids") or not data.get("asks"):
        return None
    return data["bids"], data["asks"]


def _book_side(levels):
    out = []
    for lv in levels or []:
        if isinstance(lv, (list, tuple)) and len(lv) >= 2:
            out.append([lv[0], lv[1]])
        elif isinstance(lv, dict):
            px = lv.get("price", lv.get("px", lv.get("p")))
            sz = lv.get("size", lv.get("sz", lv.get("quantity", lv.get("q"))))
            out.append([px, sz])
    return out


def phoenix_book(get, symbol):
    """Phoenix (perps nativos de Solana, API pública sin key). Formato de respuesta no verificado desde el
    contenedor [I]: se aceptan bids/asks como listas [px, size] o dicts, en la raíz o bajo orderbook/data."""
    try:
        r = get(PHOENIX_BOOK.format(symbol=symbol), timeout=15)
        data = r.json() if r.status_code == 200 else None
    except Exception:
        data = None
    if not isinstance(data, dict):
        return None
    book = data.get("orderbook") or data.get("data") or data
    if not isinstance(book, dict):
        return None
    bids, asks = _book_side(book.get("bids")), _book_side(book.get("asks"))
    return (bids, asks) if bids and asks else None


def hyperliquid_ctxs(post):
    """{coin: {"funding": f, "oi": oi}} de metaAndAssetCtxs (una sola llamada para todos los perps)."""
    try:
        r = post(HYPERLIQUID_INFO, json={"type": "metaAndAssetCtxs"}, timeout=20)
        meta, ctxs = r.json() if r.status_code == 200 else (None, None)
    except Exception:
        return {}
    out = {}
    for asset, ctx in zip((meta or {}).get("universe") or [], ctxs or []):
        try:
            out[asset["name"]] = {"funding": float(ctx.get("funding")), "oi": float(ctx.get("openInterest"))}
        except (TypeError, ValueError, KeyError):
            continue
    return out


def multichain_targets(scores, perps, top_n=OB_TOP_N):
    """Activos puntuados (no b/i) con perp listado, los de score más alto primero."""
    names = set((perps or {}).get("perps") or {})
    rows = [r for r in (scores or {}).get("results") or []
            if r.get("score") is not None and r.get("group") not in ("b", "i") and r.get("symbol")]
    rows.sort(key=lambda r: -(r.get("score") or 0))
    out = []
    for r in rows:
        sym = str(r["symbol"]).upper()
        out.append({"key": r["key"], "symbol": sym, "hl": sym in names})
        if len(out) >= top_n:
            break
    return out


def multichain_signals(targets, state, now, post, get, ctxs=None, fear_greed=None):
    out = {}
    for t in targets:
        sym, sigs = t["symbol"], []
        book = hyperliquid_book(post, sym) if t["hl"] else None
        source = "hyperliquid" if book else None
        if book is None:
            book = dydx_book(get, sym)
            source = "dydx" if book else None
        if book is None:
            book = phoenix_book(get, sym)
            source = "phoenix" if book else None
        if book:
            sigs.append(es.orderbook_imbalance(book[0], book[1]))
        ctx = (ctxs or {}).get(sym)
        if ctx:
            hist = push_series(state, "funding", sym, [now, ctx["funding"], ctx["oi"]])
            prev_oi = hist[0][2] if len(hist) > 1 else None
            oi_change = (ctx["oi"] / prev_oi - 1) if prev_oi else None
            sigs.append(es.funding_squeeze(ctx["funding"], [h[1] for h in hist[:-1]], oi_change))
        sigs.append(es.fear_greed_extreme(fear_greed))
        early = es.combine(sigs)
        early["book_source"] = source
        out[t["key"]] = early
    return out


# ---------------------------------------------------------------------------
# PumpPortal en continuo
# ---------------------------------------------------------------------------

class LaunchListener(threading.Thread):
    """subscribeNewToken en un hilo, con reconexión. drain() devuelve los lanzamientos que pasan el filtro de
    script_82 (solAmount >= 0.5, marketCapSol 10–5000)."""

    def __init__(self, filter_fn):
        super().__init__(daemon=True)
        self.filter_fn, self._buf, self._lock, self.stop_flag = filter_fn, [], threading.Lock(), False
        self.seen, self.connected_s = 0, 0.0
        self._intervals, self._open = [], None

    def intervals(self, now=None):
        """[inicio, fin] de cada conexión suscripta (la abierta, hasta now): mide la cobertura efectiva."""
        out = [list(i) for i in self._intervals]
        if self._open is not None:
            out.append([self._open, now if now is not None else time.time()])
        return out

    def drain(self):
        with self._lock:
            buf, self._buf = self._buf, []
        passed, _ = self.filter_fn(buf)
        return passed

    def run(self):
        while not self.stop_flag:
            t0 = time.time()
            try:
                asyncio.run(self._listen())
            except Exception as e:
                print(f"[WS] {type(e).__name__}: {e}")
            if self._open is not None:
                self._intervals.append([self._open, time.time()])
                self._open = None
            self.connected_s += time.time() - t0
            time.sleep(3)

    async def _listen(self):
        import websockets
        async with websockets.connect(PUMPPORTAL_WS, ping_interval=20) as ws:
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
            self._open = time.time()
            while not self.stop_flag:
                try:
                    msg = await asyncio.wait_for(ws.recv(), timeout=10)
                except asyncio.TimeoutError:
                    continue
                data = json.loads(msg)
                if data.get("txType") != "create":
                    continue
                tok = {k: data.get(k) for k in ("mint", "symbol", "name", "bondingCurveKey", "pool", "uri",
                                                "signature", "traderPublicKey", "is_mayhem_mode")}
                for k in ("solAmount", "marketCapSol", "initialBuy", "vTokensInBondingCurve", "vSolInBondingCurve"):
                    tok[k] = _f(data.get(k))
                tok["timestamp"] = now_iso()
                with self._lock:
                    self._buf.append(tok)
                    self.seen += 1


# ---------------------------------------------------------------------------
# Git (solo los archivos propios) y emisión
# ---------------------------------------------------------------------------

class Git:
    def __init__(self, root, enabled=True, run=subprocess.run):
        self.root, self.enabled, self._run = str(root), enabled, run

    def _git(self, *args, timeout=60):
        return self._run(["git", *args], cwd=self.root, capture_output=True, text=True, timeout=timeout)

    def pull(self):
        if not self.enabled:
            return True
        r = self._git("pull", "-q", "--rebase", "--autostash", "origin", "main")
        if r.returncode != 0:
            self._git("rebase", "--abort")
        return r.returncode == 0

    def commit_push(self, paths, message, attempts=4):
        if not self.enabled:
            return True
        for p in paths:
            if Path(self.root, p).exists():
                self._git("add", "--", p)
        if self._git("diff", "--staged", "--quiet").returncode == 0:
            return True
        self._git("commit", "-q", "-m", message)
        for i in range(attempts):
            if self._git("pull", "-q", "--rebase", "--autostash", "origin", "main").returncode == 0 and \
                    self._git("push", "-q", "origin", "HEAD:main").returncode == 0:
                return True
            self._git("rebase", "--abort")
            time.sleep(3 * (i + 1))
        return False


    def claim(self, paths, message, key, attempts=4):
        """Commit + push de un reclamo (archivo nuevo `key`). "ok": quedó en main y esta instancia emite.
        "lost": otra instancia ya lo tenía en main; se deshace el commit local (reset --soft, nunca --hard) y se
        borran los archivos propios. "error": sin push tras los reintentos (red); el registro queda local."""
        if not self.enabled:
            return "ok"
        for p in paths:
            self._git("add", "--", p)
        self._git("commit", "-q", "-m", message)
        for i in range(attempts):
            if self._git("fetch", "-q", "origin", "main").returncode == 0 and \
                    self._git("cat-file", "-e", f"FETCH_HEAD:{key}").returncode == 0:
                self._git("reset", "-q", "--soft", "HEAD~1")
                self._git("reset", "-q", "--", *paths)
                for p in paths:
                    try:
                        Path(self.root, p).unlink()
                    except OSError:
                        pass
                return "lost"
            if self._git("pull", "-q", "--rebase", "--autostash", "origin", "main").returncode == 0 and \
                    self._git("push", "-q", "origin", "HEAD:main").returncode == 0:
                return "ok"
            self._git("rebase", "--abort")
            time.sleep(2 * (i + 1))
        return "error"


def early_records(root):
    """Registros de alertas tempranas: un archivo por mint en early/alerts/ + el _early_alerts.json de la v0.1."""
    root = Path(root)
    out = []
    legacy = read_json(root / EARLY_DIR_REL / "_early_alerts.json", [])
    out += [a for a in legacy if isinstance(a, dict)] if isinstance(legacy, list) else []
    d = root / CLAIMS_REL
    if d.is_dir():
        for f in sorted(d.glob("*.json")):
            rec = read_json(f, None)
            if isinstance(rec, dict):
                out.append(rec)
    return out


def alerted_mints(root):
    """Mints ya alertados: _all_alerts.json (pipeline_t0) + alertas tempranas (ambas instancias)."""
    root = Path(root)
    out = set()
    data = read_json(root / "02_Analisis" / "alerts" / "_all_alerts.json", [])
    for a in (data if isinstance(data, list) else []) + early_records(root):
        if isinstance(a, dict):
            out.add(normalize_mint(a.get("mint")))
    return out - {""}


def alert_token(entry, dx, result, now):
    """El registro con el formato de _accumulated.json (lo que format_alert_message y script_113 leen)."""
    reasons = list(result["reasons"])
    if result["early"]["bonus"]:
        reasons.append(f"Anticipación (lib_early_signals {es.VERSION}): +{result['early']['bonus']} — "
                       + "; ".join(result["early"]["reasons"]))
    return {"source": entry.get("source"), "windows": entry.get("windows"), "token": entry.get("token") or {},
            "dexscreener": dx, "score": result["score"], "score_base": result["score_base"], "reasons": reasons,
            "early": {k: result["early"][k] for k in ("version", "bonus", "raw", "active", "reasons")},
            "detected_at": now_iso(now), "scoring_version": result.get("scoring_version") or "7.2.1+" + es.VERSION,
            "early_watch": VERSION, "scorer": result.get("scorer") or "v7.2.1+early"}


def emit_early(s97, root, mint, token, git, shadow, dry_run, now, gate_min=None):
    """Reclamo (registro + push) -> Telegram -> actualización del registro. None si no se emite (sin precio o
    reclamo perdido contra la otra instancia)."""
    root = Path(root)
    ts = datetime.fromtimestamp(now, timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    price = s97.get_current_price(token)
    if not price or price <= 0:
        return None
    symbol = (token.get("token") or {}).get("symbol") or token.get("symbol") or "UNKNOWN"
    msg, confidence = s97.format_alert_message(token, [], s97.load_emission_calibration())
    record = {"timestamp": ts, "mint": mint, "symbol": symbol, "score": token["score"],
              "score_base": token.get("score_base"), "early_bonus": token["early"]["bonus"],
              "confidence": confidence, "initial_price": price,
              "status": "shadow" if shadow else "active_tracking", "trust_updates": [], "early": True,
              "age_min_at_alert": round((now - (token["dexscreener"].get("pairCreatedAt") or 0) / 1000) / 60, 1),
              "gate_min": gate_min, "instance": INSTANCE, "early_watch": VERSION, "telegram_sent": None}
    claim_path = root / claim_rel(mint)
    detail_rel = f"02_Analisis/alerts/alert_{mint}_{ts}.json"
    if not dry_run:
        write_json_atomic(root / detail_rel, token)
        write_json_atomic(claim_path, record)
        status = git.claim([claim_rel(mint), detail_rel], f"early_watch {INSTANCE} alert: {symbol} {ts}",
                           claim_rel(mint))
        if status == "lost":
            print(f"[EARLY] {symbol}: la otra instancia ya lo emitió; no se envía.")
            return None
        if status == "error":
            print(f"[WARN] {symbol}: reclamo sin push (red); se envía igual y el registro sube en el próximo commit.")
    sent = False
    if not shadow and not dry_run:
        sent = bool(s97.send_telegram(msg))
    record["telegram_sent"] = sent
    if not dry_run:
        write_json_atomic(claim_path, record)
    print(f"[EARLY] {symbol} score {token['score']} (base {token.get('score_base')} + bono {token['early']['bonus']})"
          f" edad {record['age_min_at_alert']} min · instancia {INSTANCE} · enviado={sent}")
    return record


# ---------------------------------------------------------------------------
# Bucle
# ---------------------------------------------------------------------------

def poll_once(ctx, now):
    """Un ciclo completo. ctx: dict con root, get, post, state, watch, scorer, s97, git, flags."""
    root, state = Path(ctx["root"]), ctx["state"]
    ctx["git"].pull()
    threshold = ctx["threshold"]
    min_age = ctx["min_age_min"] if ctx.get("min_age_min") is not None else resolve_min_age(root)
    paths = instance_paths(ctx.get("instance"))
    alerted = alerted_mints(root)
    acc = read_json(root / "02_Analisis" / "shadow_v4" / "_accumulated.json", {})
    watch = ctx["watch"]
    for mint, e in watch_from_accumulated(acc, alerted, now).items():
        watch.setdefault(mint, e)
    if ctx.get("listener"):
        merge_launches(watch, ctx["listener"].drain(), now)
    watch = ctx["watch"] = prune_watch(watch, alerted, now)

    # RugCheck (T5) antes de evaluar, para los que en el poll anterior quedaron al alcance del bono
    for mint in rugcheck_targets(ctx.get("prev_results") or [], state, now, threshold):
        if mint in watch:
            snap = fetch_rugcheck(ctx["get"], mint, now)
            if snap:
                push_series(state, "holders", mint, snap)
    # Order book de Solana (T4, Fase 10b): distribución de liquidez de pools CLMM de Raydium
    for r in clmm_targets(ctx.get("prev_results") or [], state, now, threshold):
        if r["mint"] in watch:
            snap = fetch_clmm(ctx["get"], r, now)
            if snap:
                state.setdefault("clmm", {})[r["mint"]] = snap
    dexs = dexscreener_batch(ctx["get"], list(watch), ctx.get("sleep", time.sleep))
    info_ctx = young_info_context(ctx, root, watch, now, ctx["get"]) if ctx.get("young_scorer") else None
    results = []
    for mint, dx in dexs.items():
        if mint not in watch:
            continue
        try:
            results.append(evaluate(mint, watch[mint], dx, state, now, ctx["scorer"], root, min_age, threshold,
                                    info_ctx))
        except Exception as e:
            print(f"[WARN] {mint[:10]}...: {type(e).__name__}: {e}")
    ctx["prev_results"] = results
    results.sort(key=lambda r: (not r["emittable"], -r["score"]))

    emitted = []
    for r in results:
        if len(emitted) >= MAX_PER_POLL or not r["emittable"]:
            break
        entry, dx = watch[r["mint"]], dexs[r["mint"]]
        token = alert_token(entry, dx, r, now)
        if not ctx["s97"].acquisition_ready(token, r["mint"]):
            continue
        rec = emit_early(ctx["s97"], root, r["mint"], token, ctx["git"], ctx["shadow"], ctx["dry_run"], now, min_age)
        watch.pop(r["mint"], None)          # emitida o reclamada por la otra instancia: sale de la vigilancia
        if rec:
            emitted.append(rec)
            if r.get("scorer") == "young" and info_ctx and info_ctx.get("log_path"):
                price_s, info_s, struct_s = r["signals_young"]
                ly.append_jsonl(root / info_ctx["log_path"], ly.young_record(
                    r["mint"], rec.get("symbol"), r["young"], price_s, info_s, struct_s, now_iso(now),
                    info_ctx.get("instance"), emitted=True))

    mc = {}
    if ctx.get("multichain", True):
        scores = read_json(root / "02_Analisis" / "multichain" / "_scores.json", {})
        perps = read_json(root / "02_Analisis" / "multichain" / "_perps.json", {})
        fng = (((read_json(root / "02_Analisis" / "multichain" / "bitcoin.json", {}) or {}).get("universe_a") or {})
               .get("fear_greed") or {}).get("value")
        mc = multichain_signals(multichain_targets(scores, perps), state, now, ctx["post"], ctx["get"],
                                hyperliquid_ctxs(ctx["post"]), fng)

    top = sorted(results, key=lambda r: -r["score"])[:15]
    listener = ctx.get("listener")
    # Fase 11: se une con lo que ya está en el archivo después del pull (la corrida anterior de esta instancia puede
    # haber escrito después del checkout de esta: Actions hace checkout del SHA del momento en que se encoló)
    on_file = (read_json(root / paths["watch"], {}) or {}).get("listener_intervals") or []
    intervals = [i for i in merge_intervals(list(on_file) + list(ctx.get("intervals_prev") or [])
                                            + (listener.intervals(now) if listener else []))
                 if i[1] >= now - COVERAGE_KEEP_S]
    snapshot = {"version": VERSION, "instance": ctx.get("instance") or INSTANCE, "updated_at": now_iso(now),
                "poll_seconds": ctx["poll_seconds"], "listener_intervals": intervals,
                "threshold": threshold, "early_min_age_min": min_age, "watch_size": len(watch),
                "dex_hits": len(dexs), "listener_seen": getattr(ctx.get("listener"), "seen", None),
                "emitted": [{"mint": e["mint"], "symbol": e["symbol"], "score": e["score"],
                             "age_min": e["age_min_at_alert"]} for e in emitted],
                "top": [{"mint": r["mint"], "score": r["score"], "base": r["score_base"],
                         "bonus": r["early"]["bonus"], "active": r["early"]["active"], "age_min": r["age_min"],
                         "why": r["why"]} for r in top]}
    ctx["last"] = snapshot
    if not ctx["dry_run"]:
        write_json_atomic(root / paths["signals"], {"version": VERSION, "generated_at": now_iso(now),
                                                    "lib": es.VERSION, "signals": mc})
        state_out = {k: v for k, v in state.items()}
        state_out["holders"] = {m: v for m, v in (state.get("holders") or {}).items() if m in watch}
        state_out["liquidity"] = {m: v for m, v in (state.get("liquidity") or {}).items() if m in watch}
        state_out["clmm"] = {m: v for m, v in (state.get("clmm") or {}).items() if m in watch}
        state_out["meta"] = {m: v for m, v in (state.get("meta") or {}).items() if m in watch}
        state_out["ylog"] = {m: v for m, v in (state.get("ylog") or {}).items() if m in watch}
        write_json_atomic(root / paths["watch"], dict(snapshot, state=state_out,
                                                          watch={m: {"source": e.get("source"), "since": e.get("since")}
                                                                 for m, e in watch.items()}))
    return snapshot


def run_loop(ctx, loop_minutes, poll_seconds, clock=time.time, sleep=time.sleep):
    start, last_commit, polls = clock(), clock(), 0
    root = Path(ctx["root"])
    paths = instance_paths(ctx.get("instance"))
    own = [paths["watch"], paths["signals"], CLAIMS_REL, YOUNG_DIR_REL]
    while True:
        t = clock()
        try:
            snap = poll_once(ctx, t)
            polls += 1
            print(f"[POLL {polls}] watch {snap['watch_size']} · dex {snap['dex_hits']} · emitidas "
                  f"{len(snap['emitted'])} · top {[(x['score'], x['why']) for x in snap['top'][:3]]}")
        except Exception as e:
            print(f"[ERROR] poll: {type(e).__name__}: {e}")
        if clock() - last_commit >= COMMIT_EVERY_S:
            ctx["git"].commit_push(own, f"early_watch {ctx.get('instance') or INSTANCE}: {now_iso()}")
            last_commit = clock()
        if clock() - start + poll_seconds > loop_minutes * 60:
            break
        sleep(max(1.0, poll_seconds - (clock() - t)))
    try:
        import lib_persist
        lib_persist.log_operation(paths["op"], "script_116", [root / paths["watch"]], polls=polls,
                                  listener_seen=getattr(ctx.get("listener"), "seen", None))
    except Exception:
        pass
    ctx["git"].commit_push(own + [f"02_Analisis/operations/{paths['op']}.jsonl"],
                           f"early_watch {ctx.get('instance') or INSTANCE}: {now_iso()}")
    return polls


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--loop-minutes", type=int, default=LOOP_MINUTES)
    ap.add_argument("--poll-seconds", type=int, default=POLL_SECONDS)
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--no-git", action="store_true")
    ap.add_argument("--no-listen", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="no escribe ni envía")
    args = ap.parse_args(argv)
    if (os.environ.get("PAUSE_EMISSIONS") or "").strip().lower() in {"1", "true", "yes", "on"}:
        print("[INFO] PAUSE_EMISSIONS activo: early watch no corre.")
        return 0
    import requests
    s97 = _load_module("script_97_emit_alerts", "script_97_emit_alerts.py")
    s82 = _load_module("script_82_final_detection", "script_82_final_detection.py")
    shadow = (os.environ.get("SHADOW_MODE") or "").strip().lower() in {"1", "true", "yes", "on"}
    git = Git(ROOT, enabled=not args.no_git)
    git.pull()     # Fase 11: el checkout es del SHA de cuando se encoló la corrida; el estado se lee del main actual
    prev = read_json(ROOT / instance_paths()["watch"], {})
    listener = None
    if not args.no_listen:
        listener = LaunchListener(s82.filter_pumpportal_tokens)
        listener.start()
    ctx = {"root": ROOT, "get": requests.get, "post": requests.post, "state": prev.get("state") or {},
           "watch": {}, "scorer": isolated_scorer(s82.score_token), "s97": s97, "git": git,
           "shadow": shadow, "dry_run": args.dry_run, "threshold": s97.EMIT_MIN_SCORE, "min_age_min": None,
           "poll_seconds": args.poll_seconds, "listener": listener, "instance": INSTANCE,
           "intervals_prev": prev.get("listener_intervals") or [],
           "young_scorer": (os.environ.get("YOUNG_SCORER") or "true").strip().lower() in {"1", "true", "yes", "on"}}
    print(f"[EARLY] {VERSION} · instancia {INSTANCE} · poll {args.poll_seconds}s · bucle {args.loop_minutes} min · "
          f"umbral {s97.EMIT_MIN_SCORE} · edad mínima {resolve_min_age(ROOT)} min · sombra={shadow} · scorer joven "
          f"{ly.VERSION if ctx['young_scorer'] else 'apagado'} (umbral {ly.YOUNG_THRESHOLD}, info >= {ly.INFO_MIN})")
    if args.once:
        if listener:
            time.sleep(min(args.poll_seconds, 60))   # junta lanzamientos antes del único poll
        print(json.dumps(poll_once(ctx, time.time()), indent=1, ensure_ascii=False)[:4000])
        return 0
    run_loop(ctx, args.loop_minutes, args.poll_seconds)
    if listener:
        listener.stop_flag = True
    return 0


if __name__ == "__main__":
    sys.exit(main())
