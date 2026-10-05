#!/usr/bin/env python3
"""
bot_prelaunch_calendar.py — calendario de activos no nacidos (D-079; diseño D-078). Cada 6 h (sources_prelaunch.yml).

Un activo "no nacido" está anunciado (perp de preventa, mercado de FDV post-TGE, anuncio de listado) pero todavía no
tiene token en cadena ni spot. El calendario lo sigue hasta que nace y mide la diferencia entre el precio de preventa
y el de apertura (señal para el doc 36).

Ciclo de vida:  anunciado → confirmado → nacido → seguimiento → purgado      ·      anunciado → (30 d) → purgado
  anunciado    lo vio 1 fuente                       confirmado   ≥ 2 fuentes independientes coinciden
  nacido       transitorio: al nacer emite `prelaunch_nacido` y pasa a seguimiento (prelaunch_known: true)
  seguimiento  72 h después de nacer → memoria episódica (prelaunch_cerrado) y sale del calendario
  purgado      30 d sin nacer ("no_nacido"), cerrado el seguimiento, o nació sin confirmación suficiente

Fuentes [V 2026-10-03]: Hyperliquid (metaAndAssetCtxs) · Aevo (/markets) · Polymarket (public-search "FDV one day after
launch") · Bybit (announcements new_crypto) · Binance CMS (catálogo 48; desde runners US puede dar 451 [P]) ·
Bitcointalk board 159. D-089-R [V 2026-10-04]: CoinMarketCap (calendario ICO: ventas en curso y próximas con
icoPriceUsd) · ICO Drops (lista "upcoming" + página de cada proyecto nuevo: ticker y precio de la venta pública, con
caché de 7 d y tope de páginas por corrida). Cada fuente falla sola: una caída no rompe la corrida.

Precio de preventa: el último precio de un perp de preventa (Hyperliquid/Aevo) manda; si no hay, el precio de la
venta (CMC/ICO Drops). El de la venta queda además en `precio_venta`.

"No nacido" [H]: ni Hyperliquid ni Aevo marcan la preventa en la API, así que un perp es preventa si su símbolo NO
tiene spot en Bybit/OKX/Binance/Hyperliquid NI un par DEX con liquidez ≥ liq_born_usd (DexScreener). La regla sale
de la doc de Hyperliquid: una hyperp pasa a perp normal cuando el token lista spot en Binance, OKX o Bybit.

Emparejamiento al nacer (CRÍTICO):
  por contrato  el anuncio trajo contrato y coincide exacto → alertable
  por símbolo   símbolo (+ nombre + chain si ambos los tienen) y el activo con ≥ 2 fuentes → candidato, NO alertable
  sin eso       no hay emparejamiento
Nacimientos: el evento `token_nacido` (lo emitirán early_watch y multichain_scanner) y la observación propia (el
símbolo aparece en spot o en DEX).
Eventos (lib_events, escritor prelaunch_calendar): token_anunciado · token_confirmado · prelaunch_nacido ·
token_purgado. Van a 02_Analisis/events/prelaunch_calendar/ (el lugar estándar de lib_events, para que cualquier bot
los consuma).
Archivos propios: 02_Analisis/prelaunch/_calendar.json y _state.json; cursor events/_cursors/prelaunch_calendar.json;
episodios sources/_episodes_prelaunch.jsonl.
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_episodic_memory as episodes  # noqa: E402
import lib_events as events  # noqa: E402
import lib_normalize as norm  # noqa: E402
import lib_sources_store as store  # noqa: E402

VERSION = "prelaunch-1.1"
DIR_REL = "02_Analisis/prelaunch"
WRITER = "prelaunch_calendar"
HEADERS = {"User-Agent": "ShotDeMercado-prelaunch/1.0 (+public data)"}
TIMEOUT_S = 25
DEX_CACHE_S = 24 * 3600
URLS = {
    "hyperliquid": "https://api.hyperliquid.xyz/info",
    "aevo": "https://api.aevo.xyz/markets",
    "polymarket": "https://gamma-api.polymarket.com/public-search?q=" + quote("FDV one day after launch"),
    "bybit": "https://api.bybit.com/v5/announcements/index?locale=en-US&type=new_crypto&limit=50",
    "binance": "https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?type=1&catalogId=48&pageNo=1&pageSize=50",
    "bitcointalk": "https://bitcointalk.org/index.php?board=159.0",
    "coinmarketcap": "https://coinmarketcap.com/ico-calendar/",
    "icodrops": "https://icodrops.com/category/upcoming-ico/",
    "icodrops_project": "https://icodrops.com/{slug}/",
    "ref_bybit": "https://api.bybit.com/v5/market/instruments-info?category=spot&limit=1000",
    "ref_okx": "https://www.okx.com/api/v5/public/instruments?instType=SPOT",
    "ref_binance": "https://data-api.binance.vision/api/v3/exchangeInfo?permissions=SPOT",
    "dex": "https://api.dexscreener.com/latest/dex/search?q=",
}
LISTING_RES = [
    re.compile(r"Binance Will List (?P<name>[^()]+?) \((?P<sym>[A-Z0-9]{2,15})\)"),
    re.compile(r"Binance HODLer Airdrops?:?\s*(?P<name>[^()]+?) \((?P<sym>[A-Z0-9]{2,15})\)"),
    re.compile(r"Launchpool[^()]*?:?\s*(?P<name>[A-Z][^()]*?) \((?P<sym>[A-Z0-9]{2,15})\)"),
    re.compile(r"Bybit to List (?P<name>[^()]+?) \((?P<sym>[A-Z0-9]{2,15})\)"),
    re.compile(r"New listing: (?P<sym>[A-Z0-9]{2,15})USDT Perpetual"),
]
BTT_RE = re.compile(r"\[ANN\][^A-Za-z0-9]*(?P<name>[^|()\[\]]+?)\s*\((?P<sym>[A-Z][A-Z0-9]{1,9})\)")
BTT_ALIVE = re.compile(r"\b(is live|live mainnet|mainnet|mined|mining|pool|exchange|market|wallets?)\b", re.IGNORECASE)
PM_RE = re.compile(r"^(?P<name>.+?)\s+(?:market cap\s+)?\(?FDV\)?\s+one day after launch", re.IGNORECASE)
NAME_NOISE = re.compile(r"\b(token|coin|protocol|network|labs|foundation|finance|the)\b")
NEXT_RE = re.compile(r'<script id="__NEXT_DATA__" type="application/json"[^>]*>(.*?)</script>', re.S)
ICD_ROW_RE = re.compile(r'<li class="Tbl-Row Tbl-Row--usual".*?(?=<li class="Tbl-Row Tbl-Row--usual"|\Z)', re.S)
ICD_TITLE_RE = re.compile(r"<title>\s*(?P<name>[^<(]+?)\s*\((?P<sym>[A-Za-z0-9]{1,15})\)\s*-\s*All information", re.S)
ICD_PRICE_RE = re.compile(r'Cpsl-Items__item--pale">\s*Price\s*</span>\s*<span class="Cpsl-Items__item">\s*\$\s*([\d.,]+)')
PERP_PRICE = ("hyperliquid", "aevo")                 # precio de mercado antes de nacer
SALE_PRICE = ("coinmarketcap", "icodrops")           # precio fijo de la venta (ICO/IDO)
ICD_CACHE_S = 7 * 86400


# ---------------------------------------------------------------------------
# HTTP (nunca lanza)
# ---------------------------------------------------------------------------

class HTTP:
    def get(self, url):
        import requests
        try:
            r = requests.get(url, headers=HEADERS, timeout=TIMEOUT_S)
        except requests.RequestException as e:
            return f"error {type(e).__name__}", None
        return r.status_code, (r.text if r.status_code == 200 else None)

    def post(self, url, payload):
        import requests
        try:
            r = requests.post(url, json=payload, headers=HEADERS, timeout=TIMEOUT_S)
        except requests.RequestException as e:
            return f"error {type(e).__name__}", None
        return r.status_code, (r.text if r.status_code == 200 else None)


class SourceError(Exception):
    def __init__(self, status, msg=None):
        super().__init__(msg or f"HTTP {status}")
        self.status = status


def _json(status, body):
    if status != 200 or body is None:
        raise SourceError(status)
    return json.loads(body)


# ---------------------------------------------------------------------------
# Normalización y parsers (cuerpo → observaciones)
# ---------------------------------------------------------------------------

def norm_symbol(s):
    if s is None:
        return None
    s = re.sub(r"[^A-Za-z0-9]", "", str(s)).upper()
    return s if 1 <= len(s) <= 15 else None                   # 1 carácter existe: W (Wormhole), S (Sonic)


def norm_name(n):
    if not n:
        return None
    s = NAME_NOISE.sub(" ", str(n).lower())
    s = re.sub(r"[^a-z0-9]", "", s)
    return s or None


def ob(source, symbol=None, name=None, chain=None, contract=None, price=None, url=None, **extra):
    return {"source": source, "symbol": norm_symbol(symbol), "name": (name or "").strip() or None,
            "chain": (chain or "").lower() or None, "contract": norm.address(contract) if contract else None,
            "price": float(price) if price not in (None, "") else None, "url": url, "extra": extra}


def perp_symbol(name):
    """kPEPE (Hyperliquid) y 1000BONK (Aevo) son el mismo token que PEPE y BONK, cotizado por mil."""
    return re.sub(r"^(?:1000000|1000|1M|k)(?=[A-Z])", "", str(name or ""))


hl_symbol = perp_symbol


def parse_hyperliquid(data):
    meta, ctxs = data
    out = []
    for a, c in zip(meta.get("universe") or [], ctxs or []):
        if a.get("isDelisted"):
            continue
        out.append(ob("hyperliquid", hl_symbol(a.get("name")), price=c.get("markPx"),
                      url=f"https://app.hyperliquid.xyz/trade/{a.get('name')}", oi=c.get("openInterest"),
                      vol_24h=c.get("dayNtlVlm")))
    return out


def parse_aevo(data):
    out = []
    for m in data or []:
        if m.get("instrument_type") != "PERPETUAL" or not m.get("is_active"):
            continue
        mt = str(m.get("market_type") or "")
        if mt != "crypto" and not mt.startswith("pre_launch"):
            continue
        out.append(ob("aevo", perp_symbol(m.get("underlying_asset")), price=m.get("mark_price"),
                      url=f"https://app.aevo.xyz/perpetual/{str(m.get('underlying_asset') or '').lower()}",
                      market_type=mt))
    return out


def parse_polymarket(data):
    out = []
    for e in (data or {}).get("events") or []:
        if e.get("closed"):
            continue
        m = PM_RE.match(str(e.get("title") or ""))
        if m:
            out.append(ob("polymarket", name=m.group("name"), url=f"https://polymarket.com/event/{e.get('slug')}",
                          end_date=str(e.get("endDate") or "")[:10]))
    return out


def _listing(source, title, url):
    for rx in LISTING_RES:
        m = rx.search(title or "")
        if m:
            addr = store.ADDRESS_RE.search(title)
            return ob(source, m.group("sym"), name=m.groupdict().get("name"), url=url, title=title[:160],
                      contract=addr.group(0) if addr else None)
    return None


def parse_bybit(data):
    out = []
    for a in ((data or {}).get("result") or {}).get("list") or []:
        o = _listing("bybit", a.get("title"), a.get("url"))
        if o:
            out.append(o)
    return out


def parse_binance(data):
    out = []
    for c in ((data or {}).get("data") or {}).get("catalogs") or []:
        for a in c.get("articles") or []:
            o = _listing("binance", a.get("title"), f"https://www.binance.com/en/support/announcement/{a.get('code')}")
            if o:
                out.append(o)
    return out


def parse_bitcointalk(html):
    from bs4 import BeautifulSoup
    out = []
    for a in BeautifulSoup(html or "", "html.parser").select("span[id^=msg_] > a"):
        title = a.get_text(" ", strip=True)
        m = BTT_RE.search(title)
        if m and not BTT_ALIVE.search(title):
            addr = store.ADDRESS_RE.search(title)
            out.append(ob("bitcointalk", m.group("sym"), name=m.group("name"), url=a.get("href"),
                          contract=addr.group(0) if addr else None, title=title[:160]))
    return out


def _num_or_none(v):
    try:
        f = float(str(v).replace(",", ""))
    except (TypeError, ValueError):
        return None
    return f if f > 0 else None


def parse_coinmarketcap(html):
    """Calendario ICO de CMC (`__NEXT_DATA__`): ventas `ongoing` y `upcoming` (las `ended` ya pasaron) con
    `icoPriceUsd`, etapa, fechas, meta y launchpad. La red sale de `crypto.contracts[0].name`."""
    m = NEXT_RE.search(html or "")
    if not m:
        raise ValueError("CMC sin __NEXT_DATA__")
    pp = (json.loads(m.group(1)).get("props") or {}).get("pageProps") or {}
    if "ongoing" not in pp and "upcoming" not in pp:
        raise ValueError("CMC sin ongoing/upcoming")
    out = []
    for stage in ("ongoing", "upcoming"):
        for it in (pp.get(stage) or {}).get("icoList") or []:
            c = (it or {}).get("crypto") or {}
            if not c.get("symbol") and not c.get("name"):
                continue
            contracts = c.get("contracts") or []
            out.append(ob("coinmarketcap", c.get("symbol"), name=c.get("name"),
                          chain=(contracts[0] or {}).get("name") if contracts else None,
                          price=_num_or_none(it.get("icoPriceUsd")),
                          url=f"https://coinmarketcap.com/currencies/{c.get('slug')}/" if c.get("slug") else None,
                          etapa=stage, ronda=it.get("currentStage"), inicio=it.get("start"), fin=it.get("end"),
                          meta_usd=it.get("goalUsd"), launchpad=(it.get("launchPad") or {}).get("exchangeName")))
    return out


def _cell(row, col):
    m = re.search(r'Tbl-Row__item--' + col + r'"[^>]*>(.*?)</div>', row, re.S)
    v = " ".join(re.sub(r"<[^>]+>|&nbsp;?", " ", m.group(1)).split()) if m else ""
    return None if v in ("", "—", "-") else v


def parse_icodrops_list(html):
    """Lista "upcoming" de ICO Drops → [{"slug", "name", "ronda", "recaudado", "pre_valuacion", "fecha"}]. La
    lista no trae ticker ni precio: están en la página de cada proyecto (parse_icodrops_project)."""
    rows = ICD_ROW_RE.findall(html or "")
    if not rows:
        raise ValueError("ICO Drops sin filas")
    out = []
    for r in rows:
        slug = re.search(r'href="/([a-z0-9][a-z0-9-]*)/"', r)
        name = re.search(r'Cll-Project__name[^>]*>\s*(.*?)\s*</p>', r, re.S)
        if slug and name:
            out.append({"slug": slug.group(1), "name": " ".join(re.sub(r"<[^>]+>", " ", name.group(1)).split()),
                        "ronda": _cell(r, "round"), "recaudado": _cell(r, "raised"),
                        "pre_valuacion": _cell(r, "pre-valuation"), "fecha": _cell(r, "date")})
    return out


def parse_icodrops_project(html):
    """Página de un proyecto: ticker (del título "Nombre (TICKER) - All information") y el primer precio de una
    ronda ("Price $0.2"). Sin venta pública, no hay precio; sin ticker publicado, no hay símbolo."""
    t, p = ICD_TITLE_RE.search(html or ""), ICD_PRICE_RE.search(html or "")
    return {"symbol": norm_symbol(t.group("sym")) if t else None, "price": _num_or_none(p.group(1)) if p else None}


def fetch_icodrops(http, ctx):
    """Lista + página de cada proyecto que no esté en la caché (7 d), hasta `detalle_max` páginas por corrida;
    los que exceden el tope salen solo con nombre y se completan en las corridas siguientes."""
    st, body = http.get(URLS["icodrops"])
    if st != 200 or body is None:
        raise SourceError(st)
    cache, now = ctx["cache"], ctx["now"]
    budget, out = int(ctx.get("detalle_max", 15)), []
    for row in parse_icodrops_list(body):
        hit = cache.get(row["slug"])
        if not (hit and now - hit.get("ts", 0) < ICD_CACHE_S) and budget > 0:
            budget -= 1
            ctx["sleep"](ctx.get("pause_s", 1))
            pst, pbody = http.get(URLS["icodrops_project"].format(slug=row["slug"]))
            hit = dict(parse_icodrops_project(pbody), ts=int(now)) if pst == 200 and pbody else None
            if hit:
                cache[row["slug"]] = hit
        info = hit or {}
        out.append(ob("icodrops", info.get("symbol"), name=row["name"], price=info.get("price"),
                      url=f"https://icodrops.com/{row['slug']}/", ronda=row["ronda"], recaudado=row["recaudado"],
                      pre_valuacion=row["pre_valuacion"], fecha=row["fecha"]))
    return out


def fetch_source(name, http, ctx=None):
    if name == "hyperliquid":
        return parse_hyperliquid(_json(*http.post(URLS[name], {"type": "metaAndAssetCtxs"})))
    if name in ("bitcointalk", "coinmarketcap"):
        st, body = http.get(URLS[name])
        if st != 200 or body is None:
            raise SourceError(st)
        return parse_bitcointalk(body) if name == "bitcointalk" else parse_coinmarketcap(body)
    if name == "icodrops":
        return fetch_icodrops(http, ctx or {"cache": {}, "now": time.time(), "sleep": lambda s: None})
    parser = {"aevo": parse_aevo, "polymarket": parse_polymarket, "bybit": parse_bybit, "binance": parse_binance}[name]
    return parser(_json(*http.get(URLS[name])))


# ---------------------------------------------------------------------------
# Referencia de "ya nacido"
# ---------------------------------------------------------------------------

def born_reference(http):
    """Bases con spot en Bybit, OKX, Binance y Hyperliquid. Devuelve (set, {ref: estado})."""
    refs, status = set(), {}
    plans = [("ref_bybit", lambda d: [x["baseCoin"] for x in d["result"]["list"]]),
             ("ref_okx", lambda d: [x["baseCcy"] for x in d["data"]]),
             ("ref_binance", lambda d: [x["baseAsset"] for x in d["symbols"]])]
    for name, pick in plans:
        try:
            refs.update(norm_symbol(x) for x in pick(_json(*http.get(URLS[name]))))
            status[name] = 200
        except SourceError as e:
            status[name] = e.status
        except (ValueError, KeyError, TypeError) as e:
            status[name] = f"parse {type(e).__name__}"
    try:
        d = _json(*http.post(URLS["hyperliquid"], {"type": "spotMeta"}))
        refs.update(norm_symbol(t.get("name")) for t in d.get("tokens") or [])
        status["ref_hyperliquid_spot"] = 200
    except SourceError as e:
        status["ref_hyperliquid_spot"] = e.status
    except (ValueError, KeyError, TypeError) as e:
        status["ref_hyperliquid_spot"] = f"parse {type(e).__name__}"
    refs.discard(None)
    return refs, status


def dex_pair(http, symbol, liq_min, cache, now):
    """El par DEX de más liquidez cuyo token base tiene ese símbolo, si supera liq_min (con caché de 24 h)."""
    hit = cache.get(symbol)
    if hit and now - hit.get("ts", 0) < DEX_CACHE_S:
        return hit.get("pair")
    pair = None
    try:
        d = _json(*http.get(URLS["dex"] + quote(symbol)))
        best = None
        for p in d.get("pairs") or []:
            base = p.get("baseToken") or {}
            if norm_symbol(base.get("symbol")) != symbol and norm_name(base.get("name")) != symbol.lower():
                continue
            liq = float((p.get("liquidity") or {}).get("usd") or 0)
            if liq >= liq_min and (best is None or liq > best[0]):
                best = (liq, p)
        if best:
            p = best[1]
            pair = {"chain": p.get("chainId"), "contract": (p.get("baseToken") or {}).get("address"),
                    "price": float(p["priceUsd"]) if p.get("priceUsd") else None, "liquidity_usd": best[0],
                    "url": p.get("url")}
    except (SourceError, ValueError, KeyError, TypeError):
        return None                                           # sin dato: no se decide "nacido" por DEX
    cache[symbol] = {"ts": int(now), "pair": pair}
    return pair


# ---------------------------------------------------------------------------
# Calendario
# ---------------------------------------------------------------------------

def key_of(symbol, name):
    return f"sym:{symbol}" if symbol else f"name:{norm_name(name)}"


def names_match(a, b):
    a, b = norm_name(a), norm_name(b)
    return not a or not b or a == b or (len(min(a, b, key=len)) >= 4 and (a in b or b in a))


class Calendar:
    def __init__(self, root, config, now, emit=True):
        self.root, self.cfg, self.now, self.emit = Path(root), config, int(now), emit
        self.dir = self.root / DIR_REL
        self.doc = self._read("_calendar.json", {"assets": {}, "purged": {}})
        self.doc.setdefault("assets", {})
        self.doc.setdefault("purged", {})
        self.emitted = []
        self.pending_new, self.pending_conf = [], []        # se emiten al final de la ingesta (flush_pending)

    def _read(self, name, default):
        try:
            d = json.loads((self.dir / name).read_text(encoding="utf-8"))
            return d if isinstance(d, dict) else default
        except (OSError, ValueError):
            return default

    @property
    def assets(self):
        return self.doc["assets"]

    def event(self, type, asset, severity=1, **data):
        subject = asset.get("contract") or asset["key"]
        payload = {"key": asset["key"], "symbol": asset.get("symbol"), "name": asset.get("name"), **data}
        if self.emit:
            ev = events.write_event(type, subject, severity, payload, writer=WRITER, now=self.now, root=self.root)
            if ev:
                self.emitted.append(ev)
        else:
            self.emitted.append({"type": type, "subject": subject, "data": payload})

    def set_state(self, asset, state):
        asset["state"], asset["state_since"] = state, self.now
        asset.setdefault("history", []).append([state, self.now])

    # -- altas y confirmación -----------------------------------------------------------------------------------
    def find(self, o):
        if o["contract"]:
            for a in self.assets.values():
                if a.get("contract") == o["contract"]:
                    return a
        if o["symbol"] and f"sym:{o['symbol']}" in self.assets:
            return self.assets[f"sym:{o['symbol']}"]
        if o["name"]:
            for a in self.assets.values():
                if a.get("name") and norm_name(a["name"]) == norm_name(o["name"]) and (not o["symbol"] or not a.get("symbol")):
                    return a
        return None

    def upsert(self, o):
        if not o["symbol"] and not norm_name(o["name"]):
            return
        key = key_of(o["symbol"], o["name"])
        if key in self.doc["purged"] or (o["contract"] and o["contract"] in self.doc["purged"]):
            return
        a = self.find(o)
        if a is None:
            a = {"key": key, "symbol": o["symbol"], "name": o["name"], "chain": o["chain"], "contract": o["contract"],
                 "first_seen": self.now, "sources": {}, "prelaunch_known": False}
            self.assets[key] = a
            self.set_state(a, "anunciado")
            self.pending_new.append(a)
        elif o["symbol"] and not a.get("symbol"):                 # un nombre suelto gana su símbolo: se re-indexa
            self.assets.pop(a["key"], None)
            a.update(key=key, symbol=o["symbol"])
            self.assets[key] = a
        for f in ("name", "chain", "contract"):
            if o[f] and not a.get(f):
                a[f] = o[f]
        orphan = self.assets.get(f"name:{norm_name(o['name'])}") if o["symbol"] and o["name"] else None
        if orphan is not None and orphan is not a:                  # el mismo activo visto antes solo por nombre
            for src_name, src_row in orphan["sources"].items():
                a["sources"].setdefault(src_name, src_row)
            a["first_seen"] = min(a["first_seen"], orphan["first_seen"])
            a["contract"] = a.get("contract") or orphan.get("contract")
            a.setdefault("merged", []).append(orphan["key"])
            self.assets.pop(orphan["key"], None)
            if any(x is orphan for x in self.pending_new) and not any(x is a for x in self.pending_new):
                self.pending_new.append(a)                         # nuevo en esta corrida, con la clave definitiva
        src = a["sources"].setdefault(o["source"], {"first_seen": self.now})
        src.update(last_seen=self.now, url=o["url"], price=o["price"], extra=o["extra"])
        if o["price"] is not None and o["source"] in PERP_PRICE:
            a["precio_preventa"], a["precio_preventa_ts"], a["precio_preventa_fuente"] = o["price"], self.now, o["source"]
        elif o["price"] is not None and o["source"] in SALE_PRICE:
            a["precio_venta"] = {"usd": o["price"], "fuente": o["source"], "ts": self.now}
            if not a.get("precio_preventa") or a.get("precio_preventa_fuente") in SALE_PRICE:   # el perp manda
                a["precio_preventa"], a["precio_preventa_ts"], a["precio_preventa_fuente"] = \
                    o["price"], self.now, o["source"]
        if a["state"] == "anunciado" and len(a["sources"]) >= self.cfg.get("min_sources_confirm", 2):
            self.set_state(a, "confirmado")
            self.pending_conf.append(a)

    def flush_pending(self):
        """Anuncios y confirmaciones de la corrida, solo de los activos que sobrevivieron a las fusiones."""
        alive = lambda a: self.assets.get(a["key"]) is a  # noqa: E731
        for a in self.pending_new:
            if alive(a):
                self.event("token_anunciado", a, 1, sources=sorted(a["sources"]))
        for a in self.pending_conf:
            if alive(a):
                self.event("token_confirmado", a, 1, sources=sorted(a["sources"]))
        self.pending_new, self.pending_conf = [], []

    # -- nacimiento ---------------------------------------------------------------------------------------------
    def match_birth(self, contract, symbol, name, chain):
        contract = norm.address(contract) if contract else None
        if contract:
            for a in self.assets.values():
                if a["state"] in ("anunciado", "confirmado") and a.get("contract") == contract:
                    return a, "contrato"
        symbol = norm_symbol(symbol)
        if not symbol:
            return None, None
        cands = [a for a in self.assets.values() if a["state"] in ("anunciado", "confirmado")
                 and a.get("symbol") == symbol and names_match(a.get("name"), name)
                 and (not chain or not a.get("chain") or a["chain"] == str(chain).lower())]
        if len(cands) != 1:
            return None, None
        if len(cands[0]["sources"]) < self.cfg.get("min_sources_confirm", 2):
            return cands[0], "insuficiente"
        return cands[0], "simbolo"

    def birth(self, a, match, contract=None, chain=None, price=None, via=None):
        alertable = match == "contrato"
        pre, op = a.get("precio_preventa"), price
        delta = round((op / pre - 1) * 100, 2) if pre and op else None
        a["born"] = {"ts": self.now, "match": match, "alertable": alertable, "via": via,
                     "contract": norm.address(contract) if contract else a.get("contract"), "chain": chain or a.get("chain"),
                     "precio_preventa": pre, "precio_apertura": op, "delta_preventa_apertura_pct": delta}
        if contract and not a.get("contract"):
            a["contract"] = norm.address(contract)
        a["prelaunch_known"] = True
        self.set_state(a, "nacido")
        self.event("prelaunch_nacido", a, 2 if alertable else 1, match=match, alertable=alertable,
                   candidato=not alertable, via=via, chain=a["born"]["chain"], contract=a["born"]["contract"],
                   precio_preventa=pre, precio_apertura=op, delta_preventa_apertura_pct=delta, sources=sorted(a["sources"]))
        self.set_state(a, "seguimiento")

    # -- purga ----------------------------------------------------------------------------------------------------
    def purge(self, a, motivo):
        ctx = {k: a.get(k) for k in ("symbol", "name", "chain", "contract", "first_seen")}
        ctx.update(sources=sorted(a["sources"]), born=a.get("born"), history=a.get("history"))
        if self.emit:
            episodes.write_episodes([episodes.make_episode("prelaunch_cerrado", a.get("contract") or a["key"], ctx,
                                                           motivo, ["prelaunch", motivo], self.now, "prelaunch")],
                                    self.root, "prelaunch")
        self.event("token_purgado", a, 0, motivo=motivo)
        self.doc["purged"][a["key"]] = {"ts": self.now, "motivo": motivo}
        self.assets.pop(a["key"], None)

    def purge_due(self):
        born_s = self.cfg.get("purge_born_hours", 72) * 3600
        unborn_s = self.cfg.get("purge_unborn_days", 30) * 86400
        for a in list(self.assets.values()):
            if a["state"] == "seguimiento" and self.now - a["born"]["ts"] >= born_s:
                self.purge(a, "seguimiento_cerrado")
            elif a["state"] in ("anunciado", "confirmado") and self.now - a["first_seen"] >= unborn_s:
                self.purge(a, "no_nacido")
        keep = self.cfg.get("purged_memory_days", 90) * 86400
        self.doc["purged"] = {k: v for k, v in self.doc["purged"].items() if self.now - v["ts"] < keep}

    def save(self):
        self.dir.mkdir(parents=True, exist_ok=True)
        self.doc.update(version=VERSION, updated_at=self.now,
                        counts={s: sum(a["state"] == s for a in self.assets.values())
                                for s in ("anunciado", "confirmado", "seguimiento")})
        (self.dir / "_calendar.json").write_text(json.dumps(self.doc, ensure_ascii=False, indent=1, sort_keys=True),
                                                 encoding="utf-8")


# ---------------------------------------------------------------------------
# Corrida
# ---------------------------------------------------------------------------

def load_config(path):
    import yaml
    doc = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    if not isinstance(doc.get("sources"), dict):
        raise ValueError("prelaunch.yaml: falta el mapa 'sources'")
    return doc


def run(config, root=None, http=None, now=None, sleep=time.sleep, consume=True, write=True):
    root = Path(root or store.ROOT)
    http = http or HTTP()
    now = int(now if now is not None else time.time())
    cal = Calendar(root, config, now, emit=write)
    state_path = root / DIR_REL / "_state.json"
    try:
        prev = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        prev = {}
    health = dict(prev.get("sources") or {})
    dex_cache = {k: v for k, v in (prev.get("dex_cache") or {}).items() if now - v.get("ts", 0) < DEX_CACHE_S}
    excluded = {norm_symbol(s) for s in config.get("excluir") or []}
    liq_min = float(config.get("liq_born_usd") or 100000)
    icd_cache = {k: v for k, v in (prev.get("icodrops_cache") or {}).items() if now - v.get("ts", 0) < ICD_CACHE_S}

    # 1) fuentes, cada una por separado
    observed = []
    for name, spec in (config.get("sources") or {}).items():
        if not (spec or {}).get("enabled"):
            continue
        row = dict(health.get(name) or {}, checked_at=now)
        ctx = {"cache": icd_cache, "now": now, "sleep": sleep, "pause_s": config.get("pause_s", 1),
               "detalle_max": (spec or {}).get("detalle_max", 15)}
        try:
            obs = fetch_source(name, http, ctx)
            observed += obs
            row.update(status=200, ok=True, items=len(obs), error=None, fails=0, last_ok=now)
        except SourceError as e:
            row.update(status=e.status, ok=False, items=0, error=str(e), fails=int(row.get("fails") or 0) + 1,
                       note="[P] bloqueado desde runners US" if e.status == 451 else None)
        except Exception as e:                                       # noqa: BLE001 — una fuente rota no frena al resto
            row.update(status="parse_error", ok=False, items=0, error=f"{type(e).__name__}: {e}"[:200],
                       fails=int(row.get("fails") or 0) + 1)
        health[name] = row
        sleep(config.get("pause_s", 1))

    # 2) referencia de "ya nacido"
    refs, ref_status = born_reference(http)

    def born_info(symbol):
        if not symbol:
            return None
        if symbol in refs:
            return {"via": "spot", "chain": None, "contract": None, "price": None}
        pair = dex_pair(http, symbol, liq_min, dex_cache, now)
        return dict(pair, via="dex") if pair else None

    # 3) activos del calendario que nacieron (observación propia)
    for a in list(cal.assets.values()):
        if a["state"] not in ("anunciado", "confirmado"):
            continue
        info = born_info(a.get("symbol"))
        if not info:
            continue
        if a.get("contract") and info.get("contract") and norm.address(info["contract"]) == a["contract"]:
            cal.birth(a, "contrato", info["contract"], info["chain"], info["price"], f"observado_{info['via']}")
        elif len(a["sources"]) >= config.get("min_sources_confirm", 2):
            cal.birth(a, "simbolo", info.get("contract"), info.get("chain"), info.get("price"), f"observado_{info['via']}")
        else:
            cal.purge(a, "nacio_sin_confirmacion")                  # una sola fuente y ya existe: no era "no nacido"

    # 4) observaciones de activos no nacidos
    for o in observed:
        if o["symbol"] in excluded:
            continue
        if o["symbol"] and o["symbol"] not in {a.get("symbol") for a in cal.assets.values()} and born_info(o["symbol"]):
            continue                                                 # ya existe: no es un activo no nacido
        cal.upsert(o)
    cal.flush_pending()

    # 5) nacimientos anunciados por otros bots (token_nacido)
    births = []
    if consume:
        def on_birth(ev):
            d = ev.get("data") or {}
            a, match = cal.match_birth(ev["subject"], d.get("symbol"), d.get("name"), d.get("chain"))
            if a is not None and match in ("contrato", "simbolo"):
                cal.birth(a, match, ev["subject"], d.get("chain"), d.get("price_usd"), "token_nacido")
                births.append(a["key"])
        events.consume(WRITER, on_birth, types="token_nacido", now=now, root=root)

    # 6) purga
    cal.purge_due()
    state = {"version": VERSION, "last_run": now, "sources": health, "born_reference": ref_status,
             "dex_cache": dex_cache, "icodrops_cache": icd_cache, "observed": len(observed),
             "emitted": len(cal.emitted)}
    if write:
        cal.save()
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    return {"calendar": cal.doc, "state": state, "events": cal.emitted, "births": births}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Calendario de activos no nacidos (D-079)")
    ap.add_argument("--dry-run", action="store_true", help="no escribe calendario, estado ni eventos")
    a = ap.parse_args(argv)
    cfg = load_config(store.ROOT / "04_Config" / "sources" / "prelaunch.yaml")
    out = run(cfg, write=not a.dry_run, consume=not a.dry_run)
    st, cal = out["state"], out["calendar"]
    print(f"prelaunch: {st['observed']} observaciones · eventos {st['emitted']} · calendario "
          f"{json.dumps(cal.get('counts') or {}, ensure_ascii=False)}")
    for name, row in sorted(st["sources"].items()):
        print(f"  {name:12s} {str(row.get('status')):>6s}  ítems={row.get('items')}  {row.get('error') or ''}")
    for name, s in sorted(st["born_reference"].items()):
        print(f"  {name:22s} {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
