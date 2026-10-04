#!/usr/bin/env python3
"""
bot_influencer_tracker.py — cuentas de X de alta señal (D-087). Cada 30 min (workflow sources_x_influencers.yml).

  1. Lee 04_Config/influencers.yaml: {cuenta, categoria, prioridad}; enabled: false la saca.
  2. Por cuenta, las últimas ~20 publicaciones sin login, con los mecanismos en el orden de `mecanismos`:
     fxembed (api.fxtwitter.com/2/profile/<cuenta>/statuses) y syndication (timeline del widget de inserción).
     El siguiente se usa si el anterior falla, viene vacío o trae solo publicaciones viejas.
  3. Extrae cashtags, direcciones, contratos (URLs de token y "CA:"), URLs y palabras clave, más
     likes/reposts/respuestas/vistas si vienen. Del texto guarda solo sha256 y un extracto de 200 caracteres
     centrado en lo detectado (D-089-R); el extracto marca casi-duplicados (`dup_de`).
  4. Dedup por id de publicación contra los diarios de historia_dias (y los ids vistos en dedup_hours). Registra
     las publicaciones de las últimas max_age_h (30 d: la ventana de evaluación).
  5. Ítems src-1 en 02_Analisis/sources/x_influencers/<fecha>.jsonl y eventos lib_events (tweet_influencer,
     mencion_token, keyword_narrativa) para las publicaciones de las últimas event_max_age_h.
  6. _state.json: salud por cuenta (estado HTTP, mecanismo, frescura, fallas seguidas; auto_off tras
     fail_auto_off fallas), límites de tasa por mecanismo y la evaluación (D-089-R).

Evaluación (D-089-R): por cuenta, dias_desde_ultimo_post, frescura_score (1.0 < 7 d, 0.5 de 7 a 30 d, 0.2 > 30 d
o sin posts), posts_30d y aporte_estimado (posts de 30 d que nombran un contrato o el cashtag de un activo
vigente). `evaluar: true` si no publica hace > 30 d o si aporta 0 con > 10 posts. Por mecanismo, posts frescos
(30 d) / total y `marginal` si < 0.10. Son SEÑALES para Yang: el bot nunca saca ni apaga una cuenta por esto.
Reporte semanal en x_influencers/_evaluar_semanal.md (+ _evaluar_log.jsonl).

Frescura por cuenta: vivo (último post <= stale_dias) se consulta cada corrida; lento (<= 30 d), congelado y
vacio, cada recheck_h. Una cuenta caída no corta las demás. Solo GET públicos, sin secretos ni envíos.

Uso: python 04_Config/scripts/bot_influencer_tracker.py [--dry-run] [--config ruta] [--max N] [--reporte]
"""
import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_audit as audit  # noqa: E402
import lib_normalize as norm  # noqa: E402
import lib_sources_store as store  # noqa: E402

BOT = "x_influencers"
WRITER = "x_influencers"
VERSION = "xinf-0.2"
TIMEOUT_S = 20
HEADERS = {"User-Agent": "shot-de-mercado-sources/1.0 (research; repo artificialintelligencestaff-tech/shot-de-mercado)"}
URLS = {"fxembed": "https://api.fxtwitter.com/2/profile/{cuenta}/statuses",
        "syndication": "https://syndication.twitter.com/srv/timeline-profile/screen-name/{cuenta}"}
CATEGORIAS = {"analista_onchain", "investigador", "solana", "launchpad", "cex", "narrativa", "noticias", "fundador",
              "ballena", "depin", "rwa", "sinteticos"}
HANDLE_RE = re.compile(r"^[A-Za-z0-9_]{1,15}$")
NEXT_RE = re.compile(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', re.S)
URL_RE = re.compile(r"https?://[^\s<>\"']+")
ADDR = r"(0x[0-9a-fA-F]{40}|[1-9A-HJ-NP-Za-km-z]{32,44})(?![0-9A-Za-z])"
TOKEN_URL_RE = re.compile(
    r"(?:pump\.fun/(?:coin/)?|dexscreener\.com/[a-z]+/|birdeye\.so/(?:[a-z]+/)?token/|solscan\.io/token/|"
    r"gmgn\.ai/[a-z]+/token/|(?:etherscan\.io|basescan\.org|bscscan\.com)/token/|jup\.ag/swap/[^/?#\s]*-)" + ADDR)
CA_RE = re.compile(r"(?<![A-Za-z])(?:CA|contract(?: address)?|token address|mint)\s*[:：]?\s*" + ADDR, re.IGNORECASE)
VANITY = ("pump", "bonk")              # sufijos de los launchpads de Solana: la dirección es un mint
DAY = 86400
LENTO_DIAS = 30
RATE_DEFAULT_S = 900                   # 429 sin cabecera de reset: 15 min (ventana medida de syndication)
URLS_MAX = 5
LIST_MAX = 10
EXTRACTO_CHARS = 200
SHINGLE = 5                            # n-gramas de caracteres para comparar extractos
EVAL_DEFAULTS = {"ventana_dias": 30, "dias_sin_post": 30, "posts_min_sin_aporte": 10, "marginal_ratio": 0.10}
DEFAULTS = {"max_age_h": 720, "event_max_age_h": 2, "dedup_hours": 72, "historia_dias": 31, "pause_s": 1.0,
            "mecanismos": ["fxembed", "syndication"], "syndication_max_por_corrida": 20, "stale_dias": 7,
            "recheck_h": {"vivo": 0, "lento": 6, "congelado": 24, "vacio": 24}, "fail_auto_off": 3,
            "auto_off_h": 6, "cashtags_mayores": ["BTC", "ETH", "SOL", "USDT", "USDC"],
            "dup_horas": 72, "dup_umbral": 0.7, "evaluacion": EVAL_DEFAULTS}


# -- configuración ----------------------------------------------------------------------------------------------
def config_path(root=None):
    return Path(root or store.ROOT) / "04_Config" / "influencers.yaml"


def load_config(path):
    import yaml
    return validate_config(yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {})


def validate_config(doc):
    if not isinstance(doc, dict) or not isinstance(doc.get("cuentas"), list):
        raise ValueError("influencers.yaml: falta la lista 'cuentas'")
    cfg = {**DEFAULTS, **{k: v for k, v in doc.items() if k != "cuentas"}}
    cfg["recheck_h"] = {**DEFAULTS["recheck_h"], **(doc.get("recheck_h") or {})}
    cfg["evaluacion"] = {**EVAL_DEFAULTS, **(doc.get("evaluacion") or {})}
    if float(cfg["historia_dias"]) * 24 <= float(cfg["max_age_h"]):
        raise ValueError("influencers.yaml: historia_dias tiene que cubrir max_age_h (si no, se registran duplicados)")
    bad = [m for m in cfg["mecanismos"] or [] if m not in URLS]
    if bad or not cfg["mecanismos"]:
        raise ValueError(f"influencers.yaml: mecanismos inválidos: {cfg['mecanismos']!r}")
    names, cuentas = set(), []
    for c in doc["cuentas"]:
        if not isinstance(c, dict) or not HANDLE_RE.match(str(c.get("cuenta") or "")):
            raise ValueError(f"influencers.yaml: cuenta inválida: {c!r}")
        if c["cuenta"].lower() in names:
            raise ValueError(f"influencers.yaml: cuenta repetida: {c['cuenta']}")
        if c.get("categoria") not in CATEGORIAS:
            raise ValueError(f"influencers.yaml: categoría desconocida en {c['cuenta']}: {c.get('categoria')!r}")
        if c.get("prioridad") not in (1, 2, 3):
            raise ValueError(f"influencers.yaml: prioridad 1-3 en {c['cuenta']}")
        names.add(c["cuenta"].lower())
        cuentas.append(c)
    cfg["cuentas"] = cuentas
    return cfg


# -- parsers ----------------------------------------------------------------------------------------------------
def _num(v):
    return int(v) if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def parse_fxembed(text, cuenta):
    """JSON de FxEmbed → [{"id", "ts", "text", "author", "repost", "likes", "reposts", "replies", "views"}]."""
    doc = json.loads(text)
    if not isinstance(doc, dict) or not isinstance(doc.get("results"), list):
        raise ValueError("FxEmbed sin 'results'")
    out = []
    for s in doc["results"]:
        if not isinstance(s, dict) or not str(s.get("id") or "").isdigit():
            continue
        author = str((s.get("author") or {}).get("screen_name") or cuenta)
        out.append({"id": str(s["id"]),
                    "ts": norm.timestamp(s.get("created_timestamp")) or norm.timestamp(s.get("created_at")),
                    "text": str(s.get("text") or ""), "author": author,
                    "repost": bool(s.get("reposted_by")) or author.lower() != cuenta.lower(),
                    "likes": _num(s.get("likes")), "reposts": _num(s.get("reposts")),
                    "replies": _num(s.get("replies")), "views": _num(s.get("views"))})
    return out


def parse_syndication(html, cuenta):
    """HTML del timeline de syndication (JSON en __NEXT_DATA__) → misma forma que parse_fxembed. Los t.co se
    reemplazan por la URL expandida de entities.urls (FxEmbed ya las trae expandidas)."""
    m = NEXT_RE.search(html or "")
    if not m:
        raise ValueError("syndication sin __NEXT_DATA__")
    timeline = ((json.loads(m.group(1)).get("props") or {}).get("pageProps") or {}).get("timeline")
    entries = timeline.get("entries") if isinstance(timeline, dict) else None
    if not isinstance(entries, list):
        raise ValueError("syndication sin timeline.entries")
    out = []
    for e in entries:
        t = ((e.get("content") or {}).get("tweet")) if isinstance(e, dict) else None
        if not isinstance(t, dict) or not str(t.get("id_str") or "").isdigit():
            continue
        src = t["retweeted_status"] if isinstance(t.get("retweeted_status"), dict) else t
        author = str((src.get("user") or {}).get("screen_name") or cuenta)
        text = str(src.get("full_text") or src.get("text") or "")
        for u in (src.get("entities") or {}).get("urls") or []:
            if isinstance(u, dict) and u.get("url") and u.get("expanded_url"):
                text = text.replace(u["url"], u["expanded_url"])
        out.append({"id": t["id_str"], "ts": norm.timestamp(t.get("created_at")), "text": text, "author": author,
                    "repost": src is not t or author.lower() != cuenta.lower(),
                    "likes": _num(src.get("favorite_count")), "reposts": _num(src.get("retweet_count")),
                    "replies": _num(src.get("reply_count")), "views": None})
    return out


PARSERS = {"fxembed": parse_fxembed, "syndication": parse_syndication}


def post_fields(text):
    """(URLs canónicas, contratos de token) del texto. Contrato = dirección dentro de una URL de token
    (pump.fun, DexScreener, Birdeye, Solscan, GMGN, exploradores EVM, Jupiter), tras "CA:" o con sufijo de
    launchpad (…pump, …bonk). Las direcciones de wallets (exploradores de cuentas) no cuentan como token."""
    text = text or ""
    urls = []
    for u in URL_RE.findall(text):
        n = norm.url(u.rstrip(".,;:!?)]}…"))
        if n and n not in urls and not n.startswith(("https://t.co/", "http://t.co/")):   # t.co: media sin expandir
            urls.append(n)
    found = TOKEN_URL_RE.findall(text) + CA_RE.findall(text)
    found += [a for a in store.BASE58_RE.findall(text) if a.lower().endswith(VANITY)]
    tok = []
    for a in found:
        n = norm.address(a)
        if n and n not in tok:
            tok.append(n)
    return urls[:URLS_MAX], tok[:LIST_MAX]


def sha256_texto(text):
    """sha256 del texto original, sin normalizar: dos textos iguales byte a byte dan el mismo hash."""
    return hashlib.sha256(str(text or "").encode("utf-8")).hexdigest()


def extracto(text, keywords=(), size=EXTRACTO_CHARS):
    """Hasta `size` caracteres del texto (espacios colapsados) centrados en lo primero que se detecta: un contrato,
    un $cashtag o una palabra clave; sin nada detectado, el comienzo. Es lo único del texto que se guarda."""
    flat = " ".join(str(text or "").split())
    if len(flat) <= size:
        return flat
    hits = [m.start() for m in TOKEN_URL_RE.finditer(flat)] + [m.start() for m in CA_RE.finditer(flat)]
    hits = hits or [m.start() for m in store.CASHTAG_RE.finditer(flat)]
    if not hits:
        hits = [m.start() for w in keywords for m in [store._kw_pattern(w).search(flat)] if m]
    center = min(hits) if hits else 0
    start = max(0, min(center - size // 2, len(flat) - size))
    return flat[start:start + size].strip()


def _shingles(text):
    s = re.sub(r"https?://\S+", " ", str(text or "").lower())      # URLs fuera: cambiar el link no hace otro post
    s = " ".join(re.sub(r"[^\w$]+", " ", s).split())
    return {s[i:i + SHINGLE] for i in range(max(0, len(s) - SHINGLE + 1))}


def casi_duplicado(a, b, umbral=0.7):
    """a, b = {"sha", "ext"}. Mismo sha256 → duplicado exacto. Si no, Jaccard de n-gramas de caracteres de los
    extractos (sin URLs ni puntuación) >= umbral: el mismo texto con un typo, un emoji o un link distinto."""
    if a.get("sha") and a.get("sha") == b.get("sha"):
        return True
    sa, sb = _shingles(a.get("ext")), _shingles(b.get("ext"))
    if len(sa) < 6 or len(sb) < 6:                                   # textos mínimos: solo el hash decide
        return False
    return len(sa & sb) / len(sa | sb) >= umbral


# -- red --------------------------------------------------------------------------------------------------------
def http_get(url):
    """Una request. Nunca lanza: (estado, texto|None, cabeceras en minúsculas)."""
    import requests
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT_S)
    except requests.RequestException as e:
        return f"error {type(e).__name__}", None, {}
    return r.status_code, (r.text if r.status_code == 200 else None), {k.lower(): v for k, v in r.headers.items()}


def _int(v):
    try:
        return int(str(v).strip())
    except (TypeError, ValueError):
        return None


def rate_reset(headers, now):
    """Hasta cuándo no se insiste: x-rate-limit-reset (epoch) o retry-after (s); si no, RATE_DEFAULT_S."""
    reset, retry = _int(headers.get("x-rate-limit-reset")), _int(headers.get("retry-after"))
    if reset and now < reset <= now + 3600:
        return reset
    return int(now + (retry if retry and 0 < retry <= 3600 else RATE_DEFAULT_S))


class Fetcher:
    """Los mecanismos de una corrida: límites de tasa (429 y x-rate-limit-remaining), cupo de syndication y pausa
    entre requests reales."""

    def __init__(self, cfg, fetch, now, limits, sleep):
        self.cfg, self.fetch, self.now, self.sleep = cfg, fetch, now, sleep
        self.limits = {k: v for k, v in (limits or {}).items() if (v or 0) > now}
        self.synd_left = int(cfg["syndication_max_por_corrida"])
        self.requests = 0

    def available(self, mec):
        if (self.limits.get(mec) or 0) > self.now:
            return False
        return mec != "syndication" or self.synd_left > 0

    def get(self, mec, cuenta):
        """("ok", publicaciones, 200) · ("limited", None, 429|"cupo") · ("fail", None, estado)."""
        if not self.available(mec):
            return "limited", None, 429 if (self.limits.get(mec) or 0) > self.now else "cupo"
        if self.requests:
            self.sleep(float(self.cfg["pause_s"]))
        self.requests += 1
        if mec == "syndication":
            self.synd_left -= 1
        status, text, headers = self.fetch(URLS[mec].format(cuenta=cuenta))
        if status == 404 and mec == "fxembed":     # FxEmbed da 404 pasajeros (D-089-R, 2026-10-04 [V]): un reintento
            self.sleep(float(self.cfg["pause_s"]))
            self.requests += 1
            status, text, headers = self.fetch(URLS[mec].format(cuenta=cuenta))
        if status == 429:
            self.limits[mec] = rate_reset(headers or {}, self.now)
            return "limited", None, 429
        remaining = _int((headers or {}).get("x-rate-limit-remaining"))
        if remaining is not None and remaining <= 1:
            self.limits[mec] = rate_reset(headers, self.now)          # el próximo sería 429: se corta acá
        if status != 200:
            return "fail", None, status
        try:
            return "ok", PARSERS[mec](text, cuenta), 200
        except (ValueError, TypeError, AttributeError, KeyError) as e:
            return "fail", None, f"parse {type(e).__name__}"


def estado_de(posts, now, stale_dias):
    if not posts:
        return "vacio"
    age = now - max(p["ts"] or 0 for p in posts)
    return "vivo" if age <= stale_dias * DAY else ("lento" if age <= LENTO_DIAS * DAY else "congelado")


def fetch_account(c, fx, cfg):
    """Mecanismos en orden hasta tener publicaciones frescas. Devuelve (mejor|None, errores, hubo_limite,
    respuestas). mejor = {"mec", "posts", "newest"} con la publicación más nueva entre los mecanismos que
    respondieron; respuestas = [(mecanismo, publicaciones)] de cada uno que respondió (para `marginal`)."""
    best, errors, limited, responses = None, {}, False, []
    for mec in cfg["mecanismos"]:
        kind, posts, status = fx.get(mec, c["cuenta"])
        if kind != "ok":
            errors[mec] = status
            limited = limited or kind == "limited"
            continue
        responses.append((mec, posts))
        newest = max((p["ts"] or 0 for p in posts), default=0)
        if best is None or newest > best["newest"]:
            best = {"mec": mec, "posts": posts, "newest": newest}
        if posts and fx.now - newest <= float(cfg["stale_dias"]) * DAY:
            break
    return best, errors, limited, responses


# -- evaluación (D-089-R): señales para Yang, nunca acciones automáticas -----------------------------------------
def _perp_base(sym):
    """kPEPE / 1000BONK (perps de Hyperliquid por mil) → PEPE / BONK."""
    s = re.sub(r"^1000+", "", str(sym or ""))
    return s[1:] if re.match(r"^k[A-Z0-9]", s) else s


def vigentes(root=None, now=None, alert_days=30):
    """Activos vigentes [H]: los que el sistema sigue hoy. Devuelve {"symbols", "contracts", "fuentes"}:
    calendario de preventa sin purgar, alertas de los últimos `alert_days`, scan multichain (grupos, on-chain y
    acelerando), perps de Hyperliquid y watchlists del early watch. Un archivo que falta no rompe: aporta 0."""
    base = Path(root or store.ROOT) / "02_Analisis"
    now = now if now is not None else time.time()
    syms, addrs, fuentes = set(), set(), {}

    def read(rel):
        try:
            return json.loads((base / rel).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return None

    def add(fuente, symbol=None, addr=None):
        s, a = norm.cashtag(symbol) if symbol else None, norm.address(addr) if addr else None
        if s:
            syms.add(s)
        if a:
            addrs.add(a)
        if s or a:
            fuentes[fuente] = fuentes.get(fuente, 0) + 1

    cal = read("prelaunch/_calendar.json") or {}
    for a in ((cal.get("assets") or {}) if isinstance(cal, dict) else {}).values():
        if isinstance(a, dict) and a.get("state") != "purgado":
            add("calendario", a.get("symbol"), a.get("contract") or (a.get("born") or {}).get("contract"))
    alerts = read("alerts/_all_alerts.json")
    for a in alerts if isinstance(alerts, list) else []:
        ts = norm.timestamp(str((a or {}).get("timestamp") or "")) if isinstance(a, dict) else None
        if ts and now - ts <= alert_days * DAY:
            add("alertas", a.get("symbol"), a.get("mint"))
    scan = read("multichain/scan_latest.json") or {}
    if isinstance(scan, dict):
        for g in (scan.get("groups") or {}).values():
            for it in (g or {}).get("items") or []:
                add("multichain", (it or {}).get("symbol"))
        for net in (scan.get("onchain") or {}).values():
            for it in (net or {}).get("items") or []:
                add("multichain", (it or {}).get("symbol"), (it or {}).get("token_address"))
        for it in scan.get("accelerating") or []:
            add("multichain", (it or {}).get("symbol"), (it or {}).get("token_address"))
    perps = read("multichain/_perps.json") or {}
    for sym in ((perps.get("perps") or {}) if isinstance(perps, dict) else {}):
        add("perps", _perp_base(sym))
    for path in sorted(base.glob("early/_watch_*.json")):
        w = read(path.relative_to(base).as_posix()) or {}
        for it in (w.get("top") or []) if isinstance(w, dict) else []:
            add("early_watch", (it or {}).get("symbol"), (it or {}).get("mint"))
    return {"symbols": syms, "contracts": addrs, "fuentes": fuentes}


def tiene_aporte(rec, vig, majors):
    """Un post aporta si nombra un contrato (señal concreta sobre un token vivo) o el cashtag de un activo vigente
    que no sea un mayor (BTC, ETH… no anticipan nada) [H]."""
    m = rec.get("m") or {}
    if m.get("tok") or set(rec.get("a") or []) & vig["contracts"]:
        return True
    return any(c in vig["symbols"] and c not in majors for c in rec.get("c") or [])


def frescura_score(dias):
    if dias is None:
        return 0.2
    return 1.0 if dias < 7 else (0.5 if dias <= 30 else 0.2)


def evaluar_cuentas(active, health, window, now, cfg, vig):
    """Agrega a cada fila de `health` las señales de evaluación. `window` = registros (historia + corrida).
    Devuelve las claves con evaluar: true. No toca `next_check`, `auto_off_until` ni la config: Yang decide."""
    ev = cfg["evaluacion"]
    since = now - float(ev["ventana_dias"]) * DAY
    majors = {norm.cashtag(x) for x in cfg.get("cashtags_mayores") or []}
    by = {}
    for r in window:
        if (r.get("ts") or 0) >= since:
            by.setdefault(r.get("src"), {})[r.get("id")] = r            # por id: un post cuenta una vez
    marked = []
    for c in active:
        key = c["cuenta"].lower()
        row = health.get(key)
        if not row or not row.get("checked_at"):
            continue                                                    # nunca consultada: sin datos, sin juicio
        posts = list((by.get(key) or {}).values())
        last = max([row.get("ultimo_post_ts") or 0] + [r.get("ts") or 0 for r in posts]) or None
        dias = round((now - last) / DAY, 1) if last else None
        aporte = sum(1 for r in posts if tiene_aporte(r, vig, majors))
        motivos = []
        if dias is None or dias > float(ev["dias_sin_post"]):
            motivos.append("sin_posts_visibles" if dias is None else f"sin_post_{int(ev['dias_sin_post'])}d")
        if aporte == 0 and len(posts) > int(ev["posts_min_sin_aporte"]):
            motivos.append("sin_aporte")
        row.update(ultimo_post_ts=int(last) if last else None, dias_desde_ultimo_post=dias,
                   frescura_score=frescura_score(dias), posts_30d=len(posts), aporte_estimado=aporte,
                   evaluar=bool(motivos), evaluar_motivo=motivos)
        if motivos:
            marked.append(key)
    return marked


def stats_mecanismos(prev, responses, now, cfg):
    """Por mecanismo y día: [posts devueltos, posts de los últimos 30 d], 30 días. ratio = frescos / total en la
    ventana; marginal si ratio < marginal_ratio. Solo marca: el orden de `mecanismos` no cambia solo."""
    ev = cfg["evaluacion"]
    keep = now - float(ev["ventana_dias"]) * DAY
    day = datetime.fromtimestamp(now, timezone.utc).strftime("%Y-%m-%d")
    out = {}
    for mec in cfg["mecanismos"]:
        days = {d: v for d, v in ((prev or {}).get(mec) or {}).get("dias", {}).items()
                if datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp() >= keep - DAY}
        tot, fre = days.get(day, [0, 0])
        for m, posts in responses:
            if m == mec:
                tot += len(posts)
                fre += sum(1 for p in posts if (p["ts"] or 0) >= keep)
        if tot:
            days[day] = [tot, fre]
        total, frescos = sum(v[0] for v in days.values()), sum(v[1] for v in days.values())
        ratio = round(frescos / total, 3) if total else None
        out[mec] = {"dias": days, "posts_total": total, "posts_frescos_30d": frescos, "ratio": ratio,
                    "marginal": ratio is not None and ratio < float(ev["marginal_ratio"])}
    return out


# -- corrida ----------------------------------------------------------------------------------------------------
def load_state(path):
    try:
        st = json.loads(Path(path).read_text(encoding="utf-8"))
        return st if isinstance(st, dict) else {}
    except (OSError, ValueError):
        return {}


def is_due(key, row, now, auto_off):
    off = (auto_off or {}).get(key) or {}
    return (row.get("auto_off_until") or 0) <= now and (off.get("until") or 0) <= now \
        and (row.get("next_check") or 0) <= now


def run(config, state, fetch=http_get, now=None, sleep=time.sleep, keywords=store.DEFAULT_KEYWORDS,
        auto_off=None, groups=None, max_accounts=None, history=None, vig=None):
    """Una pasada. Devuelve (registros nuevos, eventos [(tipo, subject, severidad, data)], estado actualizado).
    `auto_off`: {cuenta: {"until": epoch}} de bot_self_repair; la cuenta se salta hasta `until`.
    `history`: registros propios de los últimos historia_dias (diarios): dedup, casi-duplicados y evaluación.
    `vig`: activos vigentes (vigentes()); sin él, solo los contratos cuentan como aporte."""
    now = now if now is not None else time.time()
    history = history or []
    vig = vig or {"symbols": set(), "contracts": set(), "fuentes": {}}
    keep_s = float(config["dedup_hours"]) * 3600
    seen = {k: t for k, t in (state.get("seen") or {}).items() if now - t <= keep_s}
    known = set(seen) | {r.get("id") for r in history}
    dup_since = now - float(config["dup_horas"]) * 3600
    recent = [r for r in history if (r.get("m") or {}).get("ext") and (r.get("ts") or 0) >= dup_since]
    active = [c for c in config["cuentas"] if c.get("enabled", True) is not False]
    health = {k: v for k, v in (state.get("sources") or {}).items() if k in {c["cuenta"].lower() for c in active}}
    fx = Fetcher(config, fetch, now, state.get("rate_limit"), sleep)
    due = [c for c in active if is_due(c["cuenta"].lower(), health.get(c["cuenta"].lower()) or {}, now, auto_off)]
    due.sort(key=lambda c: (c["prioridad"], (health.get(c["cuenta"].lower()) or {}).get("checked_at") or 0))
    if max_accounts is not None:
        due = due[:max_accounts]
    records, fresh, responses = [], [], []
    min_ts, ev_ts = now - float(config["max_age_h"]) * 3600, now - float(config["event_max_age_h"]) * 3600
    for c in due:
        key = c["cuenta"].lower()
        if not any(fx.available(m) for m in config["mecanismos"]):
            break                                            # todos los mecanismos limitados: el resto, la próxima
        prev = health.get(key) or {}
        best, errors, limited, got = fetch_account(c, fx, config)
        responses += got
        real_errors = {m: s for m, s in errors.items() if s not in (429, "cupo")}
        if best is None and limited and not real_errors:
            health[key] = {**prev, "rate_limited_at": int(now)}
            continue
        newest_any = max([prev.get("ultimo_post_ts") or 0] + [p["ts"] or 0 for _, ps in got for p in ps
                                                              if (p["ts"] or 0) <= now + 600])
        row = {"status": 200, "mec": None, "items": 0, "fresh": 0, "new": 0, "checked_at": int(now),
               "last_ok": prev.get("last_ok"), "fails": 0, "estado": prev.get("estado"),
               "ultimo_post_ts": int(newest_any) or None}
        if errors:
            row["errores"] = {m: s for m, s in errors.items()}
        if best is None or (not best["posts"] and 404 in errors.values()):
            row["status"] = 404 if 404 in errors.values() else next(iter(real_errors.values()), "error")
            row["fails"] = int(prev.get("fails") or 0) + 1
            if row["fails"] >= int(config["fail_auto_off"]):
                row["auto_off_until"] = int(now + float(config["auto_off_h"]) * 3600)
            health[key] = row
            continue
        posts = best["posts"]
        row.update(mec=best["mec"], items=len(posts), last_ok=int(now),
                   estado=estado_de(posts, now, float(config["stale_dias"])),
                   newest_age_h=round((now - best["newest"]) / 3600, 1) if posts else None)
        row["next_check"] = int(now + float(config["recheck_h"].get(row["estado"], 0)) * 3600)
        for p in sorted(posts, key=lambda p: p["ts"] or 0):
            if not p["ts"] or p["ts"] < min_ts or p["ts"] > now + 600:
                continue
            row["fresh"] += 1
            if p["id"] in known:
                continue
            known.add(p["id"])
            seen[p["id"]] = now
            urls, tok = post_fields(p["text"])
            sig = {"sha": sha256_texto(p["text"]), "ext": extracto(p["text"], keywords)}
            dup = next((r for r in recent + records if r.get("id") != p["id"]
                        and casi_duplicado(sig, r.get("m") or {}, float(config["dup_umbral"]))), None)
            meta = {"cat": c["categoria"], "prio": c["prioridad"], "mec": best["mec"], "repost": p["repost"],
                    "likes": p["likes"], "reposts": p["reposts"], "replies": p["replies"], "views": p["views"],
                    "urls": urls, "tok": tok, **sig,
                    "dup_de": dup.get("id") if dup else None, "dup_cuenta": dup.get("src") if dup else None}
            rec = store.make_record(BOT, key, "tweet", p["text"], id=p["id"], url=f"https://x.com/i/status/{p['id']}",
                                    ts=p["ts"], seen=now, author=p["author"],
                                    meta={k: v for k, v in meta.items() if v not in (None, [], "")}, keywords=keywords)
            records.append(rec)
            row["new"] += 1
            if p["ts"] >= ev_ts:
                fresh.append((c, p, rec))
        health[key] = row
    events = build_events(fresh, config, groups)
    marked = evaluar_cuentas(active, health, history + records, now, config, vig)
    mecs = stats_mecanismos(state.get("mecanismos"), responses, now, config)
    return records, events, {"version": VERSION, "last_run": int(now), "items_last_run": len(records),
                             "events_last_run": len(events), "requests_last_run": fx.requests,
                             "rate_limit": fx.limits, "sources": health, "seen": seen, "mecanismos": mecs,
                             "evaluar": sorted(marked), "vigentes": dict(sorted(vig["fuentes"].items())),
                             "reporte_semana": state.get("reporte_semana")}


def build_events(fresh, cfg, groups=None):
    """[(cuenta, publicación, registro)] recientes → eventos. tweet_influencer: uno por publicación. mencion_token:
    uno por cashtag o contrato, con las cuentas que lo nombraron. keyword_narrativa: uno por palabra clave."""
    majors = {norm.cashtag(x) for x in cfg.get("cashtags_mayores") or []}
    out, agg = [], {}
    for c, p, rec in fresh:
        m = rec.get("m") or {}
        tok, prio = m.get("tok") or [], c["prioridad"]
        sev = 2 if prio == 1 and (rec["c"] or tok) else (1 if prio <= 2 else 0)
        if m.get("dup_cuenta") != c["cuenta"].lower():       # la misma cuenta repitiendo su texto no es otro aviso
            out.append(("tweet_influencer", p["id"], sev,
                        {"cuenta": c["cuenta"], "cat": c["categoria"], "prio": prio, "url": rec["url"],
                         "ts": p["ts"], "c": rec["c"][:LIST_MAX], "tok": tok, "k": rec["k"][:LIST_MAX],
                         "repost": p["repost"], "likes": p["likes"], "reposts": p["reposts"]}))
        subjects = [("mencion_token", f"${x}", "cashtag") for x in rec["c"]] + \
                   [("mencion_token", a, "contrato") for a in tok] + [("keyword_narrativa", k, None) for k in rec["k"]]
        for typ, subject, kind in subjects:
            a = agg.setdefault((typ, subject), {"kind": kind, "cuentas": [], "cats": set(), "prio": 3, "posts": []})
            if c["cuenta"] not in a["cuentas"]:
                a["cuentas"].append(c["cuenta"])
            a["cats"].add(c["categoria"])
            a["prio"] = min(a["prio"], prio)
            a["posts"].append(p["id"])
    for (typ, subject), a in sorted(agg.items()):
        n = len(a["cuentas"])
        data = {"cuentas": a["cuentas"][:20], "n_cuentas": n, "prio_min": a["prio"], "cats": sorted(a["cats"]),
                "posts": a["posts"][:LIST_MAX]}
        if typ == "mencion_token":
            major = a["kind"] == "cashtag" and subject[1:] in majors
            sev = 0 if major else min(3, 1 + int(n >= 2 or a["prio"] == 1) + int(n >= 3))
            data["tipo"] = a["kind"]
        else:
            sev = 0 if n == 1 else (1 if n < 4 else 2)
            if groups:
                data["grupo"] = norm.keyword_group(subject, groups)
        out.append((typ, subject, sev, data))
    return out


def load_history(now, days, root=None):
    """Registros propios de los diarios de los últimos `days` días (por fecha del archivo)."""
    folder = store.sources_dir(root) / BOT
    cutoff = datetime.fromtimestamp(now - float(days) * DAY, timezone.utc).strftime("%Y-%m-%d")
    out = []
    for path in sorted(folder.glob("20*.jsonl")):
        if path.name[:10] >= cutoff:
            out += [r for r in store.read_jsonl(path) if r.get("v") == store.SCHEMA]
    return out


def iso_week(now):
    year, week, _ = datetime.fromtimestamp(now, timezone.utc).isocalendar()
    return f"{year}-W{week:02d}"


def _fmt(v, nd=1):
    return "—" if v is None else (f"{v:.{nd}f}" if isinstance(v, float) else str(v))


def reporte_semanal(state, config):
    """(markdown, línea de log) para Yang: cuentas con evaluar: true y sus datos, y mecanismos marginales."""
    now, cfg_by = state["last_run"], {c["cuenta"].lower(): c for c in config["cuentas"]}
    activas = [c for c in config["cuentas"] if c.get("enabled", True) is not False]
    filas = []
    for key in state.get("evaluar") or []:
        r, c = state["sources"].get(key) or {}, cfg_by.get(key) or {}
        filas.append({"cuenta": c.get("cuenta", key), "categoria": c.get("categoria"), "prioridad": c.get("prioridad"),
                      "dias_desde_ultimo_post": r.get("dias_desde_ultimo_post"), "frescura_score": r.get("frescura_score"),
                      "posts_30d": r.get("posts_30d"), "aporte_estimado": r.get("aporte_estimado"),
                      "motivo": r.get("evaluar_motivo") or [], "status": r.get("status"), "mec": r.get("mec")})
    filas.sort(key=lambda f: (f["prioridad"] or 9, f["cuenta"].lower()))
    mecs = {m: {k: v.get(k) for k in ("posts_total", "posts_frescos_30d", "ratio", "marginal")}
            for m, v in (state.get("mecanismos") or {}).items()}
    vig = state.get("vigentes") or {}
    lines = [f"# Evaluación semanal de cuentas de X — {iso_week(now)}", "",
             f"Generado {datetime.fromtimestamp(now, timezone.utc).isoformat(timespec='minutes')} por "
             "bot_influencer_tracker (D-089-R). **Son señales: el bot no saca ni apaga cuentas. Decide Yang.**", "",
             "Criterios: `evaluar` si no publica hace > 30 días o si aporta 0 con > 10 posts en 30 días. Aporte = post "
             "que nombra un contrato o el cashtag de un activo vigente (no mayor) [H].", "",
             "Activos vigentes usados: " + (", ".join(f"{k} {v}" for k, v in vig.items()) or "ninguno") + ".", "",
             f"## Cuentas a evaluar: {len(filas)} de {len(activas)} activas", ""]
    if filas:
        lines += ["| Cuenta | Categoría | Prio | Días sin post | Frescura | Posts 30 d | Aporte | Motivo | HTTP |",
                  "|---|---|---|---|---|---|---|---|---|"]
        lines += [f"| {f['cuenta']} | {f['categoria']} | {f['prioridad']} | {_fmt(f['dias_desde_ultimo_post'])} | "
                  f"{_fmt(f['frescura_score'])} | {_fmt(f['posts_30d'])} | {_fmt(f['aporte_estimado'])} | "
                  f"{', '.join(f['motivo'])} | {_fmt(f['status'])} |" for f in filas]
    else:
        lines.append("Ninguna.")
    lines += ["", "## Mecanismos HTTP (posts de los últimos 30 días / posts devueltos)", "",
              "| Mecanismo | Frescos / total | Ratio | Marginal (< 0.10) |", "|---|---|---|---|"]
    lines += [f"| {m} | {_fmt(v['posts_frescos_30d'])} / {_fmt(v['posts_total'])} | {_fmt(v['ratio'], 3)} | "
              f"{'sí' if v['marginal'] else 'no'} |" for m, v in mecs.items()]
    lines += ["", "Syndication solo se consulta cuando FxEmbed falla o trae lo viejo: su muestra está sesgada a "
              "esas cuentas."]
    log = {"semana": iso_week(now), "ts": now, "evaluar": filas, "mecanismos": mecs, "vigentes": vig}
    return "\n".join(lines) + "\n", log


def write_reporte(state, config, folder=None):
    folder = Path(folder or store.sources_dir() / BOT)
    folder.mkdir(parents=True, exist_ok=True)
    md, log = reporte_semanal(state, config)
    (folder / "_evaluar_semanal.md").write_text(md, encoding="utf-8")
    with (folder / "_evaluar_log.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(log, ensure_ascii=False, sort_keys=True) + "\n")
    return folder / "_evaluar_semanal.md"


def write_audit(state, items_new, duration_s, folder=None):
    """Una línea en x_influencers/_audit.jsonl + _metrics.json (patrón #15), con las cuentas consultadas hoy."""
    now = state["last_run"]
    fetched = {k: r for k, r in state["sources"].items() if r.get("checked_at") == now}
    errors = sum(1 for r in fetched.values() if r.get("status") != 200)
    line = audit.audit_line(BOT, now, sum(r.get("items") or 0 for r in fetched.values()), items_new, errors,
                            len(fetched), duration_s)
    healthy = sum(1 for r in state["sources"].values() if r.get("status") == 200)
    return audit.record_run(folder or store.sources_dir() / BOT, line, healthy, len(state["sources"]))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--config", default=None)
    ap.add_argument("--max", type=int, default=None, help="cuentas como máximo en esta corrida")
    ap.add_argument("--reporte", action="store_true", help="escribe el reporte semanal aunque ya exista el de la semana")
    args = ap.parse_args(argv)
    config = load_config(args.config or config_path())
    state_file = store.sources_dir() / BOT / "_state.json"
    t_start = now = time.time()
    repair = load_state(store.sources_dir() / "_repair_state.json")
    records, events, state = run(config, load_state(state_file), fetch=http_get, now=now,
                                 keywords=store.load_keywords(), auto_off=(repair.get("auto_off") or {}).get(BOT),
                                 groups=norm.load_groups(), max_accounts=args.max,
                                 history=load_history(now, config["historia_dias"]), vig=vigentes(store.ROOT, now))
    fetched = {k: r for k, r in state["sources"].items() if r.get("checked_at") == state["last_run"]}
    print(f"{BOT}: {len(records)} publicaciones nuevas · {len(events)} eventos · cuentas consultadas "
          f"{len(fetched)} (OK {sum(1 for r in fetched.values() if r['status'] == 200)}) · requests "
          f"{state['requests_last_run']} · límites {state['rate_limit'] or '-'} · evaluar {len(state['evaluar'])} · "
          f"marginal {[m for m, v in state['mecanismos'].items() if v['marginal']] or '-'}")
    for name, r in sorted(fetched.items()):
        print(f"  {name:16s} {str(r['status']):>10s} {str(r.get('mec') or '-'):11s} {str(r.get('estado') or '-'):9s} "
              f"ítems {r['items']:3d} recientes {r['fresh']:3d} nuevos {r['new']:3d}"
              + (f"  {r['errores']}" if r.get("errores") else ""))
    if args.dry_run:
        return 0
    store.append_records(BOT, records, state["last_run"])
    try:
        import lib_events
        state["events_last_run"] = len(lib_events.write_events(events, writer=WRITER, now=state["last_run"],
                                                                     root=store.ROOT))
    except Exception as e:                    # un evento inválido no tira la corrida: los registros ya están
        print(f"::warning::{BOT}: eventos no escritos: {type(e).__name__}: {str(e)[:160]}")
        state["events_last_run"] = 0
    semana = iso_week(state["last_run"])
    if args.reporte or state.get("reporte_semana") != semana:
        print(f"{BOT}: reporte semanal → {write_reporte(state, config)}")
        state["reporte_semana"] = semana
    state_file.parent.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(state, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    write_audit(state, len(records), time.time() - t_start)
    return 0


if __name__ == "__main__":
    sys.exit(main())
