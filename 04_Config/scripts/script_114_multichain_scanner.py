#!/usr/bin/env python3
"""
script_114_multichain_scanner.py — Scanner multi-chain v0.2 (Fase 5, T2). SOLO recolecta y marca: no puntúa ni emite.

Cubre los grupos del doc 23 con fuentes gratuitas y sin key, en el orden de prioridad de Dirección:
  h  blue chips            CoinGecko coins/markets (bitcoin, ethereum, solana)
  f  L1/L2 emergentes      CoinGecko categorías layer-1, layer-2
  c  gobernanza DeFi       CoinGecko categoría governance
  d  sintéticos/derivados  CoinGecko categorías decentralized-perpetuals, synthetic-issuer
  e  DePIN                 CoinGecko categoría depin
  g  RWA                   CoinGecko categoría real-world-assets-rwa
  a  memes multi-chain     CoinGecko Onchain (GeckoTerminal) trending_pools por red:
                           solana, base, eth, arbitrum, optimism, blast, monad
  b  preventa/pre-market   sin categoría cripto equivalente en CoinGecko (solo pre-IPO de acciones): fuera

Salidas (02_Analisis/multichain/):
  scan_latest.json   v0.1 sin cambios de esquema (lo lee script_113): grupos, pools en tendencia, aceleración.
  <chain>.json       ficha por chain (v0.2): bitcoin, ethereum, solana, base, arbitrum, optimism, blast, monad.
                     Token nativo (CoinGecko), TVL con cambios 1d/7d/30d y aceleración log 7d (DefiLlama
                     historicalChainTvl), volumen DEX y fees 24h/7d/30d (DefiLlama overview), pools en tendencia y
                     ritmo de pools nuevos (GeckoTerminal), y cocientes descriptivos (fees/TVL, volumen/TVL).
  _categories.json   las 7 categorías de CoinGecko de la directiva: mcap, cambio 24 h y volumen de la categoría
                     (coins/categories) + muestra top-25 por mcap (medianas 1h/24h/7d, amplitud, ganadores).
  _history.jsonl     una línea compacta por corrida (append): serie propia desde el día 1 (doc 23 §6.5).

Marca de aceleración [H, heurística v0, NO es el score]: cambio 24 h >= +20% (el evento del proyecto) o
cambio 1 h >= +10%. Es un filtro de atención para investigar, no una señal validada.

Ritmo: CoinGecko sin key corta ráfagas de ~5 requests (doc 23: 4/8 con 429), así que va a 1 request cada
15 s con un reintento tras 429; GeckoTerminal a 1 cada 6,5 s (convención del pipeline); DefiLlama a 1 por
segundo (ráfaga 0/8 con 429, doc 23). ~5 min por corrida. Workflow: multichain_scanner.yml, cada 1 h.

Uso: python 04_Config/scripts/script_114_multichain_scanner.py [--groups h,f,c] [--networks solana,base]
                                                               [--chains base,monad] [--no-cards] [--dry-run]
"""
import argparse
import json
import math
import os
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import requests

ROOT = Path(os.environ.get("SHOT_ROOT") or Path(__file__).resolve().parents[2])
OUT_FILE = ROOT / "02_Analisis" / "multichain" / "scan_latest.json"
SCANNER_VERSION = "0.4"
CG = "https://api.coingecko.com/api/v3"
GT = "https://api.geckoterminal.com/api/v2"
LL = "https://api.llama.fi"
UA = {"User-Agent": "shot-de-mercado-scanner/0.4", "Accept": "application/json"}
BINANCE = "https://data-api.binance.vision/api/v3"
FNG = "https://api.alternative.me/fng/?limit=1"
HYPERLIQUID = "https://api.hyperliquid.xyz/info"
# Universo A (Fase 7): velas diarias para GARCH/ATR/Bollinger, Fear & Greed y funding de Hyperliquid (fallback
# de Binance fapi, que suele dar 451 desde EE.UU., doc 23). Se guardan en las fichas de bitcoin/ethereum/solana.
UNIVERSE_A = {"bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL"}
KLINES_LIMIT = 400
# Fase 8: grupos c, d, g, b con datos propios (mismo workflow horario, sin servicios nuevos).
SNAPSHOT = "https://hub.snapshot.org/graphql"
SNAPSHOT_QUERY = ("query { proposals(first: 500, where: {state: \"active\"}, orderBy: \"end\", orderDirection: asc) "
                  "{ id title end space { id name symbol } } }")
AEVO_MARKETS = "https://api.aevo.xyz/markets"
PERPS_HISTORY_POINTS = 30          # ~30 h de OI por perp (una foto por corrida horaria)

# grupo -> (descripción, fuentes). Fuente = ("ids", "bitcoin,...") o ("category", "<id de CoinGecko>").
GROUPS = {
    "h": ("blue chips", [("ids", "bitcoin,ethereum,solana")]),
    "f": ("L1/L2 emergentes", [("category", "layer-1"), ("category", "layer-2")]),
    "c": ("gobernanza DeFi", [("category", "governance")]),
    "d": ("sintéticos / derivados", [("category", "decentralized-perpetuals"), ("category", "synthetic-issuer")]),
    "e": ("DePIN", [("category", "depin")]),
    "g": ("RWA", [("category", "real-world-assets-rwa")]),
}
GROUP_ORDER = ["h", "f", "c", "g", "d", "e"]       # prioridad de Dirección: h -> f -> c -> resto
NO_FREE_SOURCE = {"b": "preventa/pre-market: sin categoría cripto equivalente en CoinGecko (solo pre-IPO de acciones)"}
NETWORKS = ["solana", "base", "eth", "arbitrum", "optimism", "blast", "monad"]
PER_PAGE = 25
ACCEL_24H, ACCEL_1H = 20.0, 10.0                   # % — heurística v0 [H]

# Fichas por chain (v0.2). `llama`: nombres de la chain en DefiLlama, en orden de prueba (el primero que esté en
# /v2/chains manda; OP Mainnet se llamaba Optimism). `gt`: red de GeckoTerminal. `gecko`: id de CoinGecko del token
# nativo si /v2/chains no trae gecko_id (None = sin token nativo: Base).
CHAINS = {
    "bitcoin": {"kind": "blue_chip", "group": "h", "llama": ["Bitcoin"], "gt": None, "gecko": "bitcoin"},
    "ethereum": {"kind": "blue_chip", "group": "h", "llama": ["Ethereum"], "gt": "eth", "gecko": "ethereum"},
    "solana": {"kind": "blue_chip", "group": "h", "llama": ["Solana"], "gt": "solana", "gecko": "solana"},
    "base": {"kind": "l2", "group": "f", "llama": ["Base"], "gt": "base", "gecko": None},
    "arbitrum": {"kind": "l2", "group": "f", "llama": ["Arbitrum"], "gt": "arbitrum", "gecko": "arbitrum"},
    "optimism": {"kind": "l2", "group": "f", "llama": ["OP Mainnet", "Optimism"], "gt": "optimism", "gecko": "optimism"},
    "blast": {"kind": "l2", "group": "f", "llama": ["Blast"], "gt": "blast", "gecko": "blast"},
    "monad": {"kind": "l1", "group": "f", "llama": ["Monad"], "gt": "monad", "gecko": None},
}
NO_NATIVE_TOKEN = {"base": "Base no tiene token nativo: el gas se paga en ETH"}
# Las 7 categorías de la directiva (Fase 5): id de CoinGecko -> (grupo del doc 23, rótulo).
CATEGORIES = {
    "layer-1": ("f", "L1"),
    "layer-2": ("f", "L2"),
    "governance": ("c", "gobernanza"),
    "depin": ("e", "DePIN"),
    "real-world-assets-rwa": ("g", "RWA"),
    "decentralized-perpetuals": ("d", "perpetuos descentralizados"),
    "synthetic-issuer": ("d", "emisores de sintéticos"),
}
OVERVIEW_Q = "excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true"
DAY = 86400


class Http:
    """GET JSON con espaciado por host y un reintento tras 429. Devuelve (status, data|None)."""

    def __init__(self, intervals=None, retry_wait=30.0, sleep=time.sleep, clock=time.monotonic, get=None, post=None):
        self.intervals = intervals or {"api.coingecko.com": 15.0, "api.geckoterminal.com": 6.5, "api.llama.fi": 1.0,
                                       "data-api.binance.vision": 1.0, "api.alternative.me": 1.0,
                                       "api.hyperliquid.xyz": 1.0, "hub.snapshot.org": 1.0, "api.aevo.xyz": 1.0}
        self.retry_wait, self.sleep, self.clock = retry_wait, sleep, clock
        self.get = get or (lambda url: requests.get(url, headers=UA, timeout=25))
        self.post = post or (lambda url, payload: requests.post(url, json=payload, headers=UA, timeout=25))
        self.last, self.calls = {}, 0

    def _pace(self, host):
        wait = self.intervals.get(host, 0) - (self.clock() - self.last.get(host, -1e9))
        if wait > 0:
            self.sleep(wait)
        self.last[host] = self.clock()

    def get_json(self, url, payload=None):
        """GET (o POST JSON si hay `payload`, p. ej. la API `info` de Hyperliquid, que es solo lectura)."""
        host = url.split("/")[2]
        for attempt in range(2):
            self._pace(host)
            self.calls += 1
            try:
                r = self.get(url) if payload is None else self.post(url, payload)
            except requests.RequestException as e:
                return f"error:{type(e).__name__}", None
            if r.status_code == 429 and attempt == 0:
                self.sleep(self.retry_wait)
                continue
            if r.status_code != 200:
                return r.status_code, None
            try:
                return 200, r.json()
            except ValueError:
                return "error:json", None
        return 429, None


def _f(x):
    try:
        v = float(x) if x is not None and not isinstance(x, bool) else None
    except (TypeError, ValueError):
        return None
    return v if v is None or math.isfinite(v) else None


def cg_item(x):
    return {"id": x.get("id"), "symbol": (x.get("symbol") or "").upper(), "name": x.get("name"),
            "price_usd": _f(x.get("current_price")), "mcap_usd": _f(x.get("market_cap")),
            "fdv_usd": _f(x.get("fully_diluted_valuation")), "volume_24h_usd": _f(x.get("total_volume")),
            "change_1h": _f(x.get("price_change_percentage_1h_in_currency")),
            "change_24h": _f(x.get("price_change_percentage_24h_in_currency", x.get("price_change_percentage_24h"))),
            "change_7d": _f(x.get("price_change_percentage_7d_in_currency"))}


def gt_item(pool, network):
    a = pool.get("attributes") or {}
    changes = a.get("price_change_percentage") or {}
    base = (((pool.get("relationships") or {}).get("base_token") or {}).get("data") or {}).get("id") or ""
    name = a.get("name") or ""
    return {"id": a.get("address") or pool.get("id"), "symbol": name.split(" / ")[0] if name else None,
            "name": name, "chain": network, "token_address": base.split("_", 1)[1] if "_" in base else base or None,
            "price_usd": _f(a.get("base_token_price_usd")), "fdv_usd": _f(a.get("fdv_usd")),
            "mcap_usd": _f(a.get("market_cap_usd")), "reserve_usd": _f(a.get("reserve_in_usd")),
            "volume_24h_usd": _f((a.get("volume_usd") or {}).get("h24")),
            "change_1h": _f(changes.get("h1")), "change_24h": _f(changes.get("h24")),
            "pool_created_at": a.get("pool_created_at")}


def accel_reasons(item):
    reasons = []
    if item.get("change_24h") is not None and item["change_24h"] >= ACCEL_24H:
        reasons.append(f"24h {item['change_24h']:+.1f}% (>= +{ACCEL_24H:.0f}%)")
    if item.get("change_1h") is not None and item["change_1h"] >= ACCEL_1H:
        reasons.append(f"1h {item['change_1h']:+.1f}% (>= +{ACCEL_1H:.0f}%)")
    return reasons


def cg_url(kind, value):
    q = f"vs_currency=usd&price_change_percentage=1h,24h,7d&per_page={PER_PAGE}&page=1&order=market_cap_desc"
    return f"{CG}/coins/markets?{q}&{'ids' if kind == 'ids' else 'category'}={value}"


def scan(http, groups=None, networks=None, now=None):
    """v0.1: grupos de CoinGecko + pools en tendencia por red. Su salida es scan_latest.json (esquema fijo)."""
    now = now or datetime.now(timezone.utc)
    groups = [g for g in GROUP_ORDER if g in (groups or GROUP_ORDER)]
    report = {"generated_at": now.isoformat(timespec="seconds"), "scanner_version": SCANNER_VERSION,
              "accel_rule": f"24h >= +{ACCEL_24H:.0f}% o 1h >= +{ACCEL_1H:.0f}% [H, v0, no es score]",
              "groups": {}, "onchain": {}, "not_covered": NO_FREE_SOURCE, "accelerating": [], "errors": []}
    for g in groups:
        desc, sources = GROUPS[g]
        entry = {"description": desc, "sources": [], "items": []}
        for kind, value in sources:
            status, data = http.get_json(cg_url(kind, value))
            entry["sources"].append({"source": f"coingecko:{kind}={value}", "status": status})
            if status != 200 or not isinstance(data, list):
                report["errors"].append({"group": g, "source": value, "status": status})
                continue
            for x in data:
                item = dict(cg_item(x), source=value)
                entry["items"].append(item)
                if accel_reasons(item):
                    report["accelerating"].append({"group": g, "chain": None, "id": item["id"], "symbol": item["symbol"],
                                                   "change_1h": item["change_1h"], "change_24h": item["change_24h"],
                                                   "reasons": accel_reasons(item)})
        report["groups"][g] = entry
    for net in networks if networks is not None else NETWORKS:
        status, data = http.get_json(f"{GT}/networks/{net}/trending_pools?page=1")
        pools = (data or {}).get("data") if isinstance(data, dict) else None
        entry = {"status": status, "items": []}
        if status != 200 or not isinstance(pools, list):
            report["errors"].append({"group": "a", "source": f"geckoterminal:{net}", "status": status})
        else:
            for p in pools:
                item = gt_item(p, net)
                entry["items"].append(item)
                if accel_reasons(item):
                    report["accelerating"].append({"group": "a", "chain": net, "id": item["id"], "symbol": item["symbol"],
                                                   "token_address": item["token_address"], "change_1h": item["change_1h"],
                                                   "change_24h": item["change_24h"], "reasons": accel_reasons(item)})
        report["onchain"][net] = entry
    report["accelerating"].sort(key=lambda a: -(a.get("change_24h") or 0))
    report["calls"] = http.calls
    return report


# ---------------------------------------------------------------------------
# v0.2 — fichas por chain
# ---------------------------------------------------------------------------

def _pct(new, old):
    return (new / old - 1) * 100 if new is not None and old not in (None, 0) else None


def tvl_metrics(series):
    """TVL diario de DefiLlama ([{date (epoch s), tvl}]) -> último valor, cambios 1d/7d/30d y aceleración log 7d.

    Cada cambio compara contra el último punto con fecha <= último − k días (tolera días faltantes).
    aceleración_7d = ln(T0/T−7) − ln(T−7/T−14): > 0 si el TVL crece más rápido que la semana anterior [H].
    """
    rows = []
    for r in series or []:
        try:
            d, v = int(float(r.get("date"))), _f(r.get("tvl"))
        except (TypeError, ValueError, AttributeError):
            continue
        if v is not None:
            rows.append((d, v))
    if not rows:
        return None
    rows.sort()
    last_d, last_v = rows[-1]

    def at(days):
        target = last_d - days * DAY
        prior = [v for d, v in rows if d <= target]
        return prior[-1] if prior else None

    t7, t14 = at(7), at(14)
    growth = math.log(last_v / t7) if last_v > 0 and t7 and t7 > 0 else None
    prev = math.log(t7 / t14) if t7 and t14 and t7 > 0 and t14 > 0 else None
    return {"tvl_usd": last_v, "date": datetime.fromtimestamp(last_d, timezone.utc).date().isoformat(),
            "change_1d_pct": _pct(last_v, at(1)), "change_7d_pct": _pct(last_v, t7), "change_30d_pct": _pct(last_v, at(30)),
            "log_growth_7d": growth, "accel_7d": growth - prev if growth is not None and prev is not None else None,
            "days": len(rows), "first_day": datetime.fromtimestamp(rows[0][0], timezone.utc).date().isoformat()}


def overview_metrics(data):
    """DefiLlama overview/{dexs|fees}/{chain}: totales y cambios (claves verificadas para fees, doc 23)."""
    if not isinstance(data, dict):
        return None
    out = {k: _f(data.get(k)) for k in ("total24h", "total7d", "total30d", "change_1d", "change_7d", "change_1m")}
    return out if any(v is not None for v in out.values()) else None


def llama_chain_index(http, sources):
    """/v2/chains -> {nombre: {tvl, gecko_id, tokenSymbol}}; {} si falla (las fichas siguen con los alias)."""
    status, data = http.get_json(f"{LL}/v2/chains")
    sources.append({"source": "defillama:/v2/chains", "status": status})
    if status != 200 or not isinstance(data, list):
        return {}
    return {c.get("name"): {"tvl": _f(c.get("tvl")), "gecko_id": c.get("gecko_id"), "token": c.get("tokenSymbol")}
            for c in data if isinstance(c, dict) and c.get("name")}


def llama_get(http, names, url_fmt, label, sources):
    """Prueba los nombres de la chain en orden hasta un 200. Devuelve (data|None, nombre usado|None, último status)."""
    status = None
    for name in names:
        status, data = http.get_json(url_fmt.format(quote(name)))
        sources.append({"source": f"defillama:{label}/{name}", "status": status})
        if status == 200:
            return data, name, status
    return None, None, status


def new_pools_activity(http, network, now, sources):
    """1.ª página de new_pools (20 más nuevos): cantidad y ritmo estimado de pools nuevos por hora [H]."""
    status, data = http.get_json(f"{GT}/networks/{network}/new_pools?page=1")
    sources.append({"source": f"geckoterminal:new_pools/{network}", "status": status})
    pools = (data or {}).get("data") if isinstance(data, dict) else None
    if status != 200 or not isinstance(pools, list):
        return {"status": status}
    stamps = []
    for p in pools:
        try:
            stamps.append(datetime.fromisoformat(((p.get("attributes") or {}).get("pool_created_at") or "")
                                                 .replace("Z", "+00:00")).timestamp())
        except ValueError:
            continue
    span_h = (now.timestamp() - min(stamps)) / 3600 if stamps else None
    return {"status": 200, "page1": len(pools),
            "newest_age_min": round((now.timestamp() - max(stamps)) / 60, 1) if stamps else None,
            "per_hour_est": round(len(stamps) / span_h, 3) if span_h and span_h > 0 else None}


def trending_summary(entry):
    items = (entry or {}).get("items") or []
    top = sorted(items, key=lambda i: -(i.get("volume_24h_usd") or 0))[:5]
    return {"status": (entry or {}).get("status"), "pools": len(items),
            "accelerating": sum(1 for i in items if accel_reasons(i)),
            "volume_24h_usd": sum(i.get("volume_24h_usd") or 0 for i in items) if items else None,
            "top_by_volume": [{k: i.get(k) for k in ("symbol", "token_address", "change_1h", "change_24h",
                                                     "volume_24h_usd", "reserve_usd")} for i in top]}


def build_chain_cards(http, report, now=None, chains=None):
    """Una ficha por chain. Reusa lo que ya trajo scan() (blue chips, L1/L2 y pools en tendencia)."""
    now = now or datetime.now(timezone.utc)
    shared = []
    index = llama_chain_index(http, shared)
    known = {}
    for g in ("h", "f"):
        for item in ((report.get("groups") or {}).get(g) or {}).get("items") or []:
            known.setdefault(item.get("id"), item)
    selected = [c for c in CHAINS if chains is None or c in chains]
    resolved = {}
    for chain in selected:
        cfg = CHAINS[chain]
        name = next((n for n in cfg["llama"] if n in index), None)
        names = [name] + [n for n in cfg["llama"] if n != name] if name else list(cfg["llama"])
        gecko = None if chain in NO_NATIVE_TOKEN else ((index.get(name) or {}).get("gecko_id") or cfg["gecko"])
        resolved[chain] = (names, gecko)
    missing_ids = sorted({g for _, g in resolved.values() if g and g not in known})
    if missing_ids:
        status, data = http.get_json(cg_url("ids", ",".join(missing_ids)))
        shared.append({"source": f"coingecko:ids={','.join(missing_ids)}", "status": status})
        if status == 200 and isinstance(data, list):
            for x in data:
                known.setdefault(x.get("id"), dict(cg_item(x), source="ids"))
    cards = {}
    for chain in selected:
        cfg, (names, gecko) = CHAINS[chain], resolved[chain]
        sources, missing = [], []
        card = {"chain": chain, "kind": cfg["kind"], "group": cfg["group"], "scanner_version": SCANNER_VERSION,
                "generated_at": now.isoformat(timespec="seconds"), "defillama_name": None, "native_token": None,
                "tvl": None, "dex_volume": None, "fees": None, "derived": {}, "onchain": None,
                "sources": sources, "missing": missing}
        if chain in NO_NATIVE_TOKEN:
            card["native_token_note"] = NO_NATIVE_TOKEN[chain]
        elif gecko and gecko in known:
            card["native_token"] = {k: v for k, v in known[gecko].items() if k != "source"}
        elif gecko:
            missing.append(f"native_token: sin datos de CoinGecko para '{gecko}'")
        else:
            missing.append("native_token: sin id de CoinGecko (DefiLlama /v2/chains no trae gecko_id)")
        series, used, status = llama_get(http, names, f"{LL}/v2/historicalChainTvl/{{}}", "historicalChainTvl", sources)
        card["defillama_name"] = used
        card["tvl"] = tvl_metrics(series if isinstance(series, list) else None)
        if card["tvl"] is None:
            missing.append(f"tvl: DefiLlama historicalChainTvl sin datos (status {status})")
        llama_names = [used] + [n for n in names if n != used] if used else names
        for key, kind in (("dex_volume", "dexs"), ("fees", "fees")):
            data, _, status = llama_get(http, llama_names, f"{LL}/overview/{kind}/{{}}?{OVERVIEW_Q}", f"overview/{kind}",
                                        sources)
            card[key] = overview_metrics(data)
            if card[key] is None:
                missing.append(f"{key}: DefiLlama overview/{kind} sin datos (status {status})")
        tvl = (card["tvl"] or {}).get("tvl_usd")
        fees30 = (card["fees"] or {}).get("total30d")
        dex24 = (card["dex_volume"] or {}).get("total24h")
        mcap = (card["native_token"] or {}).get("mcap_usd")
        card["derived"] = {
            "fees_tvl_annualized_pct": fees30 * 365 / 30 / tvl * 100 if fees30 is not None and tvl else None,
            "dex_volume_tvl_24h": dex24 / tvl if dex24 is not None and tvl else None,
            "mcap_tvl": mcap / tvl if mcap is not None and tvl else None,
            "note": "cocientes descriptivos [H]: entradas del doc 27, no son score"}
        if cfg["gt"]:
            card["onchain"] = {"network": cfg["gt"],
                               "trending": trending_summary((report.get("onchain") or {}).get(cfg["gt"])),
                               "new_pools": new_pools_activity(http, cfg["gt"], now, sources)}
        else:
            missing.append("onchain: sin red DEX en GeckoTerminal")
        cards[chain] = card
    return cards, shared


# ---------------------------------------------------------------------------
# v0.3 — Universo A (blue chips) y TVL por protocolo (Fase 7: entradas del scoring multi-chain)
# ---------------------------------------------------------------------------

def universe_a(http, sources):
    """Velas diarias de Binance (BTC/ETH/SOL), Fear & Greed y funding/OI de Hyperliquid. Lo que falla queda en None."""
    out = {"klines_1d": {}, "fear_greed": None, "perps": {}, "all_perps": {}}
    for chain, sym in UNIVERSE_A.items():
        status, data = http.get_json(f"{BINANCE}/klines?symbol={sym}USDT&interval=1d&limit={KLINES_LIMIT}")
        sources.append({"source": f"binance:klines/{sym}USDT", "status": status})
        rows = []
        for k in data if status == 200 and isinstance(data, list) else []:
            try:
                rows.append([int(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4]), float(k[5]), int(k[6])])
            except (TypeError, ValueError, IndexError):
                continue
        out["klines_1d"][sym] = rows or None
    status, data = http.get_json(FNG)
    sources.append({"source": "alternative.me:fng", "status": status})
    row = ((data or {}).get("data") or [None])[0] if isinstance(data, dict) else None
    if isinstance(row, dict) and _f(row.get("value")) is not None:
        out["fear_greed"] = {"value": _f(row.get("value")), "label": row.get("value_classification"),
                             "timestamp": row.get("timestamp")}
    status, data = http.get_json(HYPERLIQUID, {"type": "metaAndAssetCtxs"})
    sources.append({"source": "hyperliquid:metaAndAssetCtxs", "status": status})
    if status == 200 and isinstance(data, list) and len(data) == 2:
        names = [u.get("name") for u in (data[0] or {}).get("universe") or []]
        for name, ctx in zip(names, data[1] or []):
            if not name or not isinstance(ctx, dict):
                continue
            row = {"funding_1h": _f(ctx.get("funding")), "open_interest": _f(ctx.get("openInterest")),
                   "premium": _f(ctx.get("premium")), "mark_px": _f(ctx.get("markPx")), "oracle_px": _f(ctx.get("oraclePx")),
                   "day_volume_usd": _f(ctx.get("dayNtlVlm"))}
            out["all_perps"][str(name).upper()] = row          # grupo d (y cualquier activo con perp)
            if name in UNIVERSE_A.values():
                out["perps"][name] = row
    return out


def protocols_index(http, report, sources):
    """DefiLlama /protocols filtrado a los gecko_id que trajo scan(): TVL y cambios por protocolo (c, e, g, i)."""
    ids = {i.get("id") for e in (report.get("groups") or {}).values() for i in e.get("items") or [] if i.get("id")}
    status, data = http.get_json(f"{LL}/protocols")
    sources.append({"source": "defillama:/protocols", "status": status})
    out = {}
    for p in data if status == 200 and isinstance(data, list) else []:
        gid = p.get("gecko_id") if isinstance(p, dict) else None
        if gid in ids and (gid not in out or (_f(p.get("tvl")) or 0) > (out[gid]["tvl"] or 0)):
            out[gid] = {"name": p.get("name"), "defillama_id": p.get("id"), "slug": p.get("slug"),
                        "category": p.get("category"), "tvl": _f(p.get("tvl")),
                        "change_1d": _f(p.get("change_1d")), "change_7d": _f(p.get("change_7d")),
                        "mcap": _f(p.get("mcap")), "chains": (p.get("chains") or [])[:10]}
    if out:
        status, data = http.get_json(f"{LL}/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true")
        sources.append({"source": "defillama:/overview/fees", "status": status})
        fees = {}
        for f in ((data or {}).get("protocols") or []) if isinstance(data, dict) else []:
            for key in (f.get("defillamaId"), f.get("slug"), (f.get("name") or "").lower()):
                if key:
                    fees.setdefault(str(key), f)
        for gid, row in out.items():
            f = fees.get(str(row.get("defillama_id"))) or fees.get(str(row.get("slug"))) or fees.get((row.get("name") or "").lower())
            if f:
                row.update(fees_24h=_f(f.get("total24h")), fees_7d=_f(f.get("total7d")), fees_30d=_f(f.get("total30d")),
                           fees_change_1m=_f(f.get("change_1m")))
    return out


def snapshot_proposals(http, sources, now=None):
    """Propuestas activas de Snapshot (GraphQL público, 100 req/60 s, doc 23): grupo c."""
    now = now or datetime.now(timezone.utc)
    status, data = http.get_json(SNAPSHOT, {"query": SNAPSHOT_QUERY})
    sources.append({"source": "snapshot:proposals(active)", "status": status})
    rows = (((data or {}).get("data") or {}).get("proposals") or []) if isinstance(data, dict) else []
    out = [{"id": p.get("id"), "title": p.get("title"), "end": p.get("end"),
            "hours_left": round((p["end"] - now.timestamp()) / 3600, 2) if isinstance(p.get("end"), (int, float)) else None,
            "space": (p.get("space") or {}).get("id"), "space_name": (p.get("space") or {}).get("name"),
            "space_symbol": str((p.get("space") or {}).get("symbol") or "").upper() or None}
           for p in rows if isinstance(p, dict)]
    return {"generated_at": now.isoformat(timespec="seconds"), "status": status, "loaded": status == 200,
            "proposals": out}


def aevo_premarkets(http, sources):
    """Mercados de Aevo que no son perps cripto estándar (pre_ipo / pre-launch): grupo b (doc 23: 2 pre_ipo)."""
    status, data = http.get_json(AEVO_MARKETS)
    sources.append({"source": "aevo:markets", "status": status})
    out = []
    for m in data if status == 200 and isinstance(data, list) else []:
        kind = str(m.get("instrument_type") or m.get("type") or "").lower()
        if isinstance(m, dict) and ("pre" in kind or m.get("is_pre_launch") or m.get("pre_launch")):
            out.append({"underlying": m.get("underlying_asset"), "instrument": m.get("instrument_name"), "type": kind,
                        "mark_price": _f(m.get("mark_price")), "index_price": _f(m.get("index_price"))})
    return {"status": status, "markets": out}


# ---------------------------------------------------------------------------
# v0.2 — resumen de categorías
# ---------------------------------------------------------------------------

def _median(values):
    vals = [v for v in values if v is not None]
    return statistics.median(vals) if vals else None


def build_categories(http, report, now=None):
    """Las 7 categorías: datos de la categoría (coins/categories) + muestra top-25 por mcap (de scan())."""
    now = now or datetime.now(timezone.utc)
    status, data = http.get_json(f"{CG}/coins/categories?order=market_cap_desc")
    by_id = {c.get("id"): c for c in data if isinstance(c, dict)} if status == 200 and isinstance(data, list) else {}
    items_by_cat, source_status = {}, {}
    for g, entry in (report.get("groups") or {}).items():
        for src in entry.get("sources") or []:
            source_status[src["source"].split("=", 1)[-1]] = src["status"]
        for item in entry.get("items") or []:
            items_by_cat.setdefault(item.get("source"), []).append(item)
    out = {}
    for cat, (group, label) in CATEGORIES.items():
        c = by_id.get(cat) or {}
        items = items_by_cat.get(cat) or []
        ranked = sorted((i for i in items if i.get("change_24h") is not None), key=lambda i: -i["change_24h"])
        with_24h = [i for i in items if i.get("change_24h") is not None]
        out[cat] = {
            "group": group, "label": label, "name": c.get("name"),
            "market_cap_usd": _f(c.get("market_cap")), "market_cap_change_24h_pct": _f(c.get("market_cap_change_24h")),
            "volume_24h_usd": _f(c.get("volume_24h")), "top_3_coins_id": c.get("top_3_coins_id"),
            "updated_at": c.get("updated_at"),
            "category_status": 200 if c else (status if status != 200 else "no listada en coins/categories"),
            "sample": {"source_status": source_status.get(cat, "no consultada (grupo fuera de --groups)"),
                       "n": len(items), "median_change_1h": _median(i.get("change_1h") for i in items),
                       "median_change_24h": _median(i.get("change_24h") for i in items),
                       "median_change_7d": _median(i.get("change_7d") for i in items),
                       "breadth_24h": (sum(1 for i in with_24h if i["change_24h"] > 0) / len(with_24h)) if with_24h else None,
                       "accelerating": sum(1 for i in items if accel_reasons(i)),
                       "top_gainers_24h": [{k: i.get(k) for k in ("id", "symbol", "change_24h")} for i in ranked[:3]],
                       "top_losers_24h": [{k: i.get(k) for k in ("id", "symbol", "change_24h")} for i in ranked[-3:][::-1]]}}
    ranking = sorted((k for k in out if out[k]["market_cap_change_24h_pct"] is not None),
                     key=lambda k: -out[k]["market_cap_change_24h_pct"])
    return {"generated_at": now.isoformat(timespec="seconds"), "scanner_version": SCANNER_VERSION,
            "source": "CoinGecko /coins/categories (categoría) + coins/markets?category= top-25 por mcap (muestra)",
            "categories_status": status, "categories": out, "ranking_24h": ranking,
            "note": "solo recolección: sin score ni emisión"}


# ---------------------------------------------------------------------------
# Salidas
# ---------------------------------------------------------------------------

def _r(x, nd=4):
    return round(x, nd) if isinstance(x, float) else x


def history_line(report, cards, categories, calls):
    chains = {}
    for chain, c in (cards or {}).items():
        nt, tvl = c.get("native_token") or {}, c.get("tvl") or {}
        tr = ((c.get("onchain") or {}).get("trending") or {})
        npools = ((c.get("onchain") or {}).get("new_pools") or {})
        chains[chain] = {"tvl": _r(tvl.get("tvl_usd"), 0), "tvl_7d": _r(tvl.get("change_7d_pct")),
                         "tvl_acc": _r(tvl.get("accel_7d")), "dex24h": _r((c.get("dex_volume") or {}).get("total24h"), 0),
                         "fees24h": _r((c.get("fees") or {}).get("total24h"), 0), "px": nt.get("price_usd"),
                         "chg24": _r(nt.get("change_24h")), "trend": tr.get("pools"), "trend_acc": tr.get("accelerating"),
                         "new_h": npools.get("per_hour_est")}
    cats = {k: {"mcap": _r(v["market_cap_usd"], 0), "chg24": _r(v["market_cap_change_24h_pct"]),
                "vol": _r(v["volume_24h_usd"], 0), "breadth": _r(v["sample"]["breadth_24h"]),
                "med24": _r(v["sample"]["median_change_24h"])}
            for k, v in ((categories or {}).get("categories") or {}).items()}
    return {"ts": report.get("generated_at"), "v": SCANNER_VERSION, "calls": calls,
            "errors": len(report.get("errors") or []), "accelerating": len(report.get("accelerating") or []),
            "chains": chains, "categories": cats}


def _write_atomic(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, path)


def merge_perps(previous, perps, ts):
    """_perps.json: foto actual de todos los perps + historial de open interest por símbolo (últimas 30 fotos)."""
    hist = dict((previous or {}).get("oi_history") or {})
    for sym, row in (perps or {}).items():
        if row.get("open_interest") is not None:
            hist[sym] = (list(hist.get(sym) or []) + [[ts, row["open_interest"]]])[-PERPS_HISTORY_POINTS:]
    return {"generated_at": ts, "source": "hyperliquid metaAndAssetCtxs", "perps": perps or {}, "oi_history": hist}


def write_outputs(out_file, report, out_dir=None, cards=None, categories=None, calls=None, protocols=None,
                  extras=None, perps=None):
    """scan_latest.json (esquema v0.1) + fichas, _categories.json, _protocols.json, extras (_governance,
    _premarket), _perps.json con historial y una línea en _history.jsonl."""
    _write_atomic(out_file, report)
    written = [Path(out_file)]
    if cards is None and categories is None:
        return written
    out_dir = Path(out_dir or Path(out_file).parent)
    for chain, card in (cards or {}).items():
        _write_atomic(out_dir / f"{chain}.json", card)
        written.append(out_dir / f"{chain}.json")
    if categories is not None:
        _write_atomic(out_dir / "_categories.json", categories)
        written.append(out_dir / "_categories.json")
    if protocols is not None:
        _write_atomic(out_dir / "_protocols.json", protocols)
        written.append(out_dir / "_protocols.json")
    for name, data in (extras or {}).items():
        _write_atomic(out_dir / name, data)
        written.append(out_dir / name)
    if perps is not None:
        try:
            previous = json.loads((out_dir / "_perps.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            previous = None
        _write_atomic(out_dir / "_perps.json", merge_perps(previous, perps, report.get("generated_at")))
        written.append(out_dir / "_perps.json")
    line = json.dumps(history_line(report, cards, categories, calls if calls is not None else report.get("calls")),
                      ensure_ascii=False, separators=(",", ":"))
    with open(out_dir / "_history.jsonl", "a", encoding="utf-8") as f:
        f.write(line + "\n")
    written.append(out_dir / "_history.jsonl")
    return written


def main(argv=None, http=None):
    ap = argparse.ArgumentParser(description="Scanner multi-chain v0.2: recolecta y marca aceleraciones (no emite)")
    ap.add_argument("--groups", default=",".join(GROUP_ORDER), help="subconjunto de h,f,c,g,d,e")
    ap.add_argument("--networks", default=",".join(NETWORKS), help="redes de GeckoTerminal ('' = ninguna)")
    ap.add_argument("--chains", default=",".join(CHAINS), help="fichas por chain (subconjunto)")
    ap.add_argument("--no-cards", action="store_true", help="solo scan_latest.json (comportamiento v0.1)")
    ap.add_argument("--out", default=str(OUT_FILE), help="ruta de scan_latest.json")
    ap.add_argument("--out-dir", default=None, help="carpeta de fichas, _categories y _history (por defecto, la de --out)")
    ap.add_argument("--dry-run", action="store_true", help="no escribe archivos")
    args = ap.parse_args(argv)
    groups = [g for g in args.groups.split(",") if g]
    unknown = [g for g in groups if g not in GROUPS]
    if unknown:
        ap.error(f"grupos desconocidos: {unknown} (b no tiene fuente gratuita)")
    chains = [c for c in args.chains.split(",") if c]
    if [c for c in chains if c not in CHAINS]:
        ap.error(f"chains desconocidas: {[c for c in chains if c not in CHAINS]} (válidas: {', '.join(CHAINS)})")
    networks = [n for n in args.networks.split(",") if n]
    http = http or Http()
    report = scan(http, groups, networks)
    counts = {g: len(e["items"]) for g, e in report["groups"].items()}
    counts.update({f"a:{n}": len(e["items"]) for n, e in report["onchain"].items()})
    print(f"[114] ítems por fuente: {counts} · llamadas: {report['calls']} · errores: {len(report['errors'])}")
    for a in report["accelerating"][:15]:
        print(f"[114] ACEL {a['group']} {a.get('chain') or '-':<8} {a['symbol']:<10} {'; '.join(a['reasons'])}")
    cards = categories = protocols = extras = perps = None
    if not args.no_cards:
        cards, _ = build_chain_cards(http, report, chains=chains)
        categories = build_categories(http, report)
        ua_sources, proto_sources = [], []
        ua = universe_a(http, ua_sources)
        for chain, sym in UNIVERSE_A.items():
            if chain in cards:
                cards[chain]["universe_a"] = {"klines_1d": ua["klines_1d"].get(sym), "fear_greed": ua["fear_greed"],
                                              "perp": ua["perps"].get(sym), "sources": ua_sources}
        protocols = {"generated_at": report["generated_at"], "sources": proto_sources,
                     "protocols": protocols_index(http, report, proto_sources)}
        perps = ua["all_perps"] or None
        extra_sources = []
        extras = {"_governance.json": snapshot_proposals(http, extra_sources),
                  "_premarket.json": aevo_premarkets(http, extra_sources)}
        for chain, c in cards.items():
            tvl, nt = c.get("tvl") or {}, c.get("native_token") or {}
            print(f"[114] {chain:<9} TVL {tvl.get('tvl_usd')} ({tvl.get('change_7d_pct')} % 7d) · "
                  f"DEX 24h {(c.get('dex_volume') or {}).get('total24h')} · fees 24h {(c.get('fees') or {}).get('total24h')} · "
                  f"nativo {nt.get('symbol') or '-'} {nt.get('change_24h')} % 24h · faltan {len(c['missing'])}")
        for cat in categories["ranking_24h"]:
            v = categories["categories"][cat]
            print(f"[114] categoría {cat:<26} mcap 24h {v['market_cap_change_24h_pct']:+.2f}% · "
                  f"amplitud {v['sample']['breadth_24h']}")
    print(f"[114] llamadas totales: {http.calls}")
    if not args.dry_run:
        written = write_outputs(args.out, report, args.out_dir, cards, categories, http.calls, protocols, extras, perps)
        for path in written:
            print(f"[OK] {path}")
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import lib_persist   # Fase 9: bitácora de la operación
        lib_persist.log_operation("multichain_scan", "script_114", written, calls=http.calls,
                                  errors=len(report.get("errors") or []), accelerating=len(report.get("accelerating") or []))
    return 0


if __name__ == "__main__":
    sys.exit(main())
