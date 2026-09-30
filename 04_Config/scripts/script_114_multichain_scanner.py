#!/usr/bin/env python3
"""
script_114_multichain_scanner.py — Scanner multi-chain v0 (T5). SOLO recolecta y marca: no puntúa ni emite.

Cubre los grupos del doc 23 con fuentes gratuitas y sin key, en el orden de prioridad de Dirección:
  h  blue chips            CoinGecko coins/markets (bitcoin, ethereum, solana)
  f  L1/L2 emergentes      CoinGecko categorías layer-1, layer-2
  c  gobernanza DeFi       CoinGecko categoría governance
  d  sintéticos/derivados  CoinGecko categorías decentralized-perpetuals, synthetic-issuer
  e  DePIN                 CoinGecko categoría depin
  g  RWA                   CoinGecko categoría real-world-assets-rwa
  a  memes multi-chain     CoinGecko Onchain (GeckoTerminal) trending_pools por red: solana, base, eth, blast, monad
  b  preventa/pre-market   sin categoría cripto equivalente en CoinGecko (solo pre-IPO de acciones): fuera del v0

Marca de aceleración [H, heurística v0, NO es el score]: cambio 24 h >= +20% (el evento del proyecto) o
cambio 1 h >= +10%. Es un filtro de atención para investigar, no una señal validada.

Ritmo: CoinGecko sin key corta ráfagas de ~5 requests (doc 23: 4/8 con 429), así que va a 1 request cada
15 s con un reintento tras 429; GeckoTerminal a 1 cada 6,5 s (convención del pipeline). ~2,5 min por corrida.

Salida: 02_Analisis/multichain/scan_latest.json (se sobrescribe).
Uso: python 04_Config/scripts/script_114_multichain_scanner.py [--groups h,f,c] [--networks solana,base] [--dry-run]
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(os.environ.get("SHOT_ROOT") or Path(__file__).resolve().parents[2])
OUT_FILE = ROOT / "02_Analisis" / "multichain" / "scan_latest.json"
SCANNER_VERSION = "0.1"
CG = "https://api.coingecko.com/api/v3"
GT = "https://api.geckoterminal.com/api/v2"
UA = {"User-Agent": "shot-de-mercado-scanner/0.1", "Accept": "application/json"}

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
NETWORKS = ["solana", "base", "eth", "blast", "monad"]
PER_PAGE = 25
ACCEL_24H, ACCEL_1H = 20.0, 10.0                   # % — heurística v0 [H]


class Http:
    """GET JSON con espaciado por host y un reintento tras 429. Devuelve (status, data|None)."""

    def __init__(self, intervals=None, retry_wait=30.0, sleep=time.sleep, clock=time.monotonic, get=None):
        self.intervals = intervals or {"api.coingecko.com": 15.0, "api.geckoterminal.com": 6.5}
        self.retry_wait, self.sleep, self.clock = retry_wait, sleep, clock
        self.get = get or (lambda url: requests.get(url, headers=UA, timeout=25))
        self.last, self.calls = {}, 0

    def _pace(self, host):
        wait = self.intervals.get(host, 0) - (self.clock() - self.last.get(host, -1e9))
        if wait > 0:
            self.sleep(wait)
        self.last[host] = self.clock()

    def get_json(self, url):
        host = url.split("/")[2]
        for attempt in range(2):
            self._pace(host)
            self.calls += 1
            try:
                r = self.get(url)
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
        return float(x) if x is not None and not isinstance(x, bool) else None
    except (TypeError, ValueError):
        return None


def cg_item(x):
    return {"id": x.get("id"), "symbol": (x.get("symbol") or "").upper(), "name": x.get("name"),
            "price_usd": _f(x.get("current_price")), "mcap_usd": _f(x.get("market_cap")),
            "volume_24h_usd": _f(x.get("total_volume")),
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


def main(argv=None):
    ap = argparse.ArgumentParser(description="Scanner multi-chain v0: recolecta y marca aceleraciones (no emite)")
    ap.add_argument("--groups", default=",".join(GROUP_ORDER), help="subconjunto de h,f,c,g,d,e")
    ap.add_argument("--networks", default=",".join(NETWORKS), help="redes de GeckoTerminal ('' = ninguna)")
    ap.add_argument("--out", default=str(OUT_FILE))
    ap.add_argument("--dry-run", action="store_true", help="no escribe el archivo")
    args = ap.parse_args(argv)
    groups = [g for g in args.groups.split(",") if g]
    unknown = [g for g in groups if g not in GROUPS]
    if unknown:
        ap.error(f"grupos desconocidos: {unknown} (b no tiene fuente gratuita en el v0)")
    networks = [n for n in args.networks.split(",") if n]
    report = scan(Http(), groups, networks)
    counts = {g: len(e["items"]) for g, e in report["groups"].items()}
    counts.update({f"a:{n}": len(e["items"]) for n, e in report["onchain"].items()})
    print(f"[114] ítems por fuente: {counts} · llamadas: {report['calls']} · errores: {len(report['errors'])}")
    for a in report["accelerating"][:15]:
        print(f"[114] ACEL {a['group']} {a.get('chain') or '-':<7} {a['symbol']:<10} {'; '.join(a['reasons'])}")
    if not args.dry_run:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        tmp = out.with_suffix(".tmp")
        tmp.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        os.replace(tmp, out)
        print(f"[OK] {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
