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
  3. Emite en cuanto score + bono >= EMIT_MIN_SCORE (56) con edad >= EARLY_MIN_AGE_MIN (por defecto el mismo
     EMIT_MIN_AGE_MIN de script_97 = 30; configurable) y guía de compra (regla núcleo). Mensaje = el de script_97.
     Registro ANTES de enviar en 02_Analisis/early/_early_alerts.json (push inmediato). pipeline_t0 adopta esos
     registros en _all_alerts.json (script_98 los sigue) y les adjunta el dossier.
  4. Multi-chain (T4): order book de Hyperliquid (l2Book; dYdX v4 de respaldo) + funding/OI propios para los
     activos de multichain/_scores.json con perp -> 02_Analisis/early/_signals.json, que script_97 suma como bono.

Mientras este workflow está corriendo, script_97 deja la ruta Solana en sus manos (sin doble emisión): ver
script_97.early_watch_active.

Archivos (solo los suyos): 02_Analisis/early/{_watch.json, _early_alerts.json, _signals.json} y los
alert_<mint>_<ts>.json de sus alertas. Bitácora lib_persist "early_watch".

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

ROOT = Path(os.environ.get("SHOT_ROOT") or SCRIPTS.parents[1])
VERSION = "116-0.1"
EARLY_DIR_REL = "02_Analisis/early"
DEX_BATCH_URL = "https://api.dexscreener.com/tokens/v1/solana/{mints}"
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
GROUP_I_MIN_AGE_MIN = 180 * 1440
STORED_SCORE_MAX_AGE_MIN = 60      # script_97.CANDIDATE_MAX_AGE_MIN   # script_82.GROUP_I_MIN_AGE_DAYS


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


def evaluate(mint, entry, dx, state, now, scorer, root, min_age_min, threshold):
    """Score v7.2.1 con datos frescos + bono anticipatorio. Devuelve el resultado (sin efectos salvo las series)."""
    base, reasons = scorer(entry.get("token") or {}, dx)
    # Paridad con script_97: dentro de los 60 min de la detección vale el score de script_82 si es mayor
    stored, det = entry.get("score_82"), parse_iso(entry.get("since"))
    if isinstance(stored, (int, float)) and det is not None and now - det <= STORED_SCORE_MAX_AGE_MIN * 60 \
            and stored > base:
        reasons = list(reasons) + [f"score de detección {stored} (script_82, hace {round((now - det) / 60)} min) "
                                   f"> re-score {base}: vale el de detección (paridad con script_97)"]
        base = int(stored)
    liq = push_series(state, "liquidity", mint, [now, dx.get("liquidityUsd")])
    signals = es.dex_signals(dx, [(t, v) for t, v in liq]) + [holders_signal(state, mint), narrative_signal(root, mint)]
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
            "age_min": round(age, 1) if age is not None else None, "emittable": why == "emitible", "why": why}


def rugcheck_targets(results, state, now, threshold, per_poll=RUGCHECK_PER_POLL, refresh_s=RUGCHECK_REFRESH_S):
    near = [r for r in results if r["score_base"] is not None and r["score_base"] + NEAR_THRESHOLD >= threshold]
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
            self.connected_s += time.time() - t0
            time.sleep(3)

    async def _listen(self):
        import websockets
        async with websockets.connect(PUMPPORTAL_WS, ping_interval=20) as ws:
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
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


def alerted_mints(root):
    """Mints ya alertados: _all_alerts.json (pipeline_t0) + _early_alerts.json (este proceso)."""
    root = Path(root)
    out = set()
    for path in (root / "02_Analisis" / "alerts" / "_all_alerts.json", root / EARLY_DIR_REL / "_early_alerts.json"):
        data = read_json(path, [])
        for a in data if isinstance(data, list) else []:
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
            "detected_at": now_iso(now), "scoring_version": "7.2.1+" + es.VERSION, "early_watch": VERSION}


def emit_early(s97, root, mint, token, git, shadow, dry_run, now):
    """Registro -> push -> Telegram -> actualización del registro. Devuelve el registro."""
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
              "telegram_sent": None}
    alerts_path = root / EARLY_DIR_REL / "_early_alerts.json"
    detail_rel = f"02_Analisis/alerts/alert_{mint}_{ts}.json"
    if not dry_run:
        write_json_atomic(root / detail_rel, token)
        alerts = read_json(alerts_path, [])
        alerts.append(record)
        write_json_atomic(alerts_path, alerts)
        git.commit_push([f"{EARLY_DIR_REL}/_early_alerts.json", detail_rel], f"early_watch alert: {symbol} {ts}")
    sent = False
    if not shadow and not dry_run:
        sent = bool(s97.send_telegram(msg))
    record["telegram_sent"] = sent
    if not dry_run:
        alerts = read_json(alerts_path, [])
        for a in alerts:
            if a.get("mint") == mint and a.get("timestamp") == ts:
                a["telegram_sent"] = sent
        write_json_atomic(alerts_path, alerts)
    print(f"[EARLY] {symbol} score {token['score']} (base {token.get('score_base')} + bono {token['early']['bonus']})"
          f" edad {record['age_min_at_alert']} min · enviado={sent}")
    return record


# ---------------------------------------------------------------------------
# Bucle
# ---------------------------------------------------------------------------

def poll_once(ctx, now):
    """Un ciclo completo. ctx: dict con root, get, post, state, watch, scorer, s97, git, flags."""
    root, state = Path(ctx["root"]), ctx["state"]
    threshold, min_age = ctx["threshold"], ctx["min_age_min"]
    ctx["git"].pull()
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
    dexs = dexscreener_batch(ctx["get"], list(watch), ctx.get("sleep", time.sleep))
    results = []
    for mint, dx in dexs.items():
        if mint not in watch:
            continue
        try:
            results.append(evaluate(mint, watch[mint], dx, state, now, ctx["scorer"], root, min_age, threshold))
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
        rec = emit_early(ctx["s97"], root, r["mint"], token, ctx["git"], ctx["shadow"], ctx["dry_run"], now)
        if rec:
            emitted.append(rec)
            watch.pop(r["mint"], None)

    mc = {}
    if ctx.get("multichain", True):
        scores = read_json(root / "02_Analisis" / "multichain" / "_scores.json", {})
        perps = read_json(root / "02_Analisis" / "multichain" / "_perps.json", {})
        fng = (((read_json(root / "02_Analisis" / "multichain" / "bitcoin.json", {}) or {}).get("universe_a") or {})
               .get("fear_greed") or {}).get("value")
        mc = multichain_signals(multichain_targets(scores, perps), state, now, ctx["post"], ctx["get"],
                                hyperliquid_ctxs(ctx["post"]), fng)

    top = sorted(results, key=lambda r: -r["score"])[:15]
    snapshot = {"version": VERSION, "updated_at": now_iso(now), "poll_seconds": ctx["poll_seconds"],
                "threshold": threshold, "early_min_age_min": min_age, "watch_size": len(watch),
                "dex_hits": len(dexs), "listener_seen": getattr(ctx.get("listener"), "seen", None),
                "emitted": [{"mint": e["mint"], "symbol": e["symbol"], "score": e["score"],
                             "age_min": e["age_min_at_alert"]} for e in emitted],
                "top": [{"mint": r["mint"], "score": r["score"], "base": r["score_base"],
                         "bonus": r["early"]["bonus"], "active": r["early"]["active"], "age_min": r["age_min"],
                         "why": r["why"]} for r in top]}
    ctx["last"] = snapshot
    if not ctx["dry_run"]:
        early_dir = root / EARLY_DIR_REL
        write_json_atomic(early_dir / "_signals.json", {"version": VERSION, "generated_at": now_iso(now),
                                                        "lib": es.VERSION, "signals": mc})
        state_out = {k: v for k, v in state.items()}
        state_out["holders"] = {m: v for m, v in (state.get("holders") or {}).items() if m in watch}
        state_out["liquidity"] = {m: v for m, v in (state.get("liquidity") or {}).items() if m in watch}
        write_json_atomic(early_dir / "_watch.json", dict(snapshot, state=state_out,
                                                          watch={m: {"source": e.get("source"), "since": e.get("since")}
                                                                 for m, e in watch.items()}))
    return snapshot


def run_loop(ctx, loop_minutes, poll_seconds, clock=time.time, sleep=time.sleep):
    start, last_commit, polls = clock(), clock(), 0
    root = Path(ctx["root"])
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
            ctx["git"].commit_push([f"{EARLY_DIR_REL}/_watch.json", f"{EARLY_DIR_REL}/_signals.json"],
                                   f"early_watch: {now_iso()}")
            last_commit = clock()
        if clock() - start + poll_seconds > loop_minutes * 60:
            break
        sleep(max(1.0, poll_seconds - (clock() - t)))
    try:
        import lib_persist
        lib_persist.log_operation("early_watch", "script_116", [root / EARLY_DIR_REL / "_watch.json"], polls=polls,
                                  listener_seen=getattr(ctx.get("listener"), "seen", None))
    except Exception:
        pass
    ctx["git"].commit_push([f"{EARLY_DIR_REL}/_watch.json", f"{EARLY_DIR_REL}/_signals.json",
                            "02_Analisis/operations/early_watch.jsonl"], f"early_watch: {now_iso()}")
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
    min_age = int(os.environ.get("EARLY_MIN_AGE_MIN") or s97.EMIT_MIN_AGE_MIN)
    shadow = (os.environ.get("SHADOW_MODE") or "").strip().lower() in {"1", "true", "yes", "on"}
    prev = read_json(ROOT / EARLY_DIR_REL / "_watch.json", {})
    listener = None
    if not args.no_listen:
        listener = LaunchListener(s82.filter_pumpportal_tokens)
        listener.start()
    ctx = {"root": ROOT, "get": requests.get, "post": requests.post, "state": prev.get("state") or {},
           "watch": {}, "scorer": isolated_scorer(s82.score_token), "s97": s97, "git": Git(ROOT, enabled=not args.no_git),
           "shadow": shadow, "dry_run": args.dry_run, "threshold": s97.EMIT_MIN_SCORE, "min_age_min": min_age,
           "poll_seconds": args.poll_seconds, "listener": listener}
    print(f"[EARLY] {VERSION} · poll {args.poll_seconds}s · bucle {args.loop_minutes} min · umbral "
          f"{s97.EMIT_MIN_SCORE} · edad mínima {min_age} min · sombra={shadow}")
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
