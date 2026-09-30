#!/usr/bin/env python3
"""
probe_grupos_activos.py — Verificación HTTP de fuentes gratuitas para los 8 grupos de activos (doc 23).

Por fuente registra: status, latencia, headers de rate limit, campos de la respuesta, tamaño y, donde se
puede, cobertura temporal (primer dato disponible). En las fuentes clave hace una ráfaga corta
(BURST requests seguidos, sin pausa) para medir si aparece 429. Es cortés a propósito: nada de barridos.

Grupos: a memes micro-cap · b presale/pre-market · c DeFi gobernanza nueva · d sintéticos/derivados
algorítmicos · e DePIN · f L1/L2 emergentes · g RWA especulativo · h blue chips.

Uso: python 04_Config/scripts/probe_grupos_activos.py [--out ruta.json] [--no-burst]
Sin API keys: si una fuente pide key, queda registrada como tal y no se usa.
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
OUT = ROOT / "02_Analisis" / "diagnostics" / "grupos_activos_probe.json"
UA = {"User-Agent": "shot-de-mercado-probe/1.0 (research; contact via GitHub repo)", "Accept": "application/json"}
BURST = 8
COOLDOWN = 70
NOW = int(time.time())
DEGEN_BASE = "0x4ed4e862860bed51a9570b96d89af5e1b0efefed"
BONK = "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263"

SNAPSHOT_Q = {"query": "{ proposals(first: 3, orderBy: \"created\", orderDirection: desc, where: {state: \"active\"}) "
                       "{ id title space { id } created end scores_total votes } }"}

# (grupo, id, método, url, cuerpo, burst, extractor de cobertura)
SOURCES = [
    # h — blue chips
    ("h", "binance_klines_btc", "GET", "https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=1d&startTime=0&limit=2", None, True, "binance_first"),
    ("h", "binance_futures_funding", "GET", "https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&startTime=1567296000000&limit=1", None, False, "binance_funding_first"),
    ("h", "coinbase_candles_btc", "GET", "https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=86400", None, True, None),
    ("h", "kraken_ohlc_btc", "GET", "https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1440", None, False, None),
    ("h", "deribit_dvol_btc", "GET", f"https://www.deribit.com/api/v2/public/get_volatility_index_data?currency=BTC&start_timestamp=0&end_timestamp={NOW*1000}&resolution=86400", None, False, "deribit_first"),
    ("h", "alternative_fng", "GET", "https://api.alternative.me/fng/?limit=0", None, False, "fng_first"),
    ("h", "coinpaprika_ticker_btc", "GET", "https://api.coinpaprika.com/v1/tickers/btc-bitcoin", None, True, None),
    ("h", "mempool_fees", "GET", "https://mempool.space/api/v1/fees/recommended", None, False, None),
    ("h", "coingecko_simple_keyless", "GET", "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd", None, True, None),
    # f — L1/L2 emergentes
    ("f", "defillama_chains", "GET", "https://api.llama.fi/v2/chains", None, True, "count"),
    ("f", "defillama_chain_tvl_base", "GET", "https://api.llama.fi/v2/historicalChainTvl/Base", None, False, "llama_first"),
    ("f", "defillama_chain_tvl_monad", "GET", "https://api.llama.fi/v2/historicalChainTvl/Monad", None, False, "llama_first"),
    ("f", "defillama_fees_base", "GET", "https://api.llama.fi/overview/fees/Base?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true", None, False, None),
    ("f", "growthepie_master", "GET", "https://api.growthepie.xyz/v1/master.json", None, False, None),
    ("f", "l2beat_summary", "GET", "https://l2beat.com/api/scaling/summary", None, False, None),
    ("f", "geckoterminal_networks", "GET", "https://api.geckoterminal.com/api/v2/networks?page=1", None, False, "gt_networks"),
    # e — DePIN
    ("e", "coingecko_category_depin", "GET", "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=depin&per_page=20", None, False, "count"),
    ("e", "coingecko_categories_list", "GET", "https://api.coingecko.com/api/v3/coins/categories/list", None, False, "count"),
    ("e", "depinscan_projects", "GET", "https://api.depinscan.io/api/projects", None, False, None),
    # c — DeFi gobernanza
    ("c", "snapshot_graphql", "POST", "https://hub.snapshot.org/graphql", SNAPSHOT_Q, True, None),
    ("c", "defillama_protocols", "GET", "https://api.llama.fi/protocols", None, False, "protocols"),
    ("c", "defillama_fees_overview", "GET", "https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true", None, False, None),
    ("c", "tally_graphql_keyless", "POST", "https://api.tally.xyz/query", {"query": "{ chains { id } }"}, False, None),
    ("c", "defillama_emissions_unlocks", "GET", "https://api.llama.fi/emissions", None, False, None),
    # g — RWA
    ("g", "coingecko_category_rwa", "GET", "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=real-world-assets-rwa&per_page=20", None, False, "count"),
    ("g", "rwa_xyz_keyless", "GET", "https://api.rwa.xyz/v3/assets", None, False, None),
    # b — presale / pre-market
    ("b", "hyperliquid_meta_ctxs", "POST", "https://api.hyperliquid.xyz/info", {"type": "metaAndAssetCtxs"}, True, "hl_meta"),
    ("b", "aevo_markets_perp", "GET", "https://api.aevo.xyz/markets?instrument_type=PERPETUAL", None, False, "aevo_prelaunch"),
    ("b", "hyperliquid_perp_dexs_hip3", "POST", "https://api.hyperliquid.xyz/info", {"type": "perpDexs"}, False, "hl_dexs"),
    ("b", "coingecko_new_coins", "GET", "https://api.coingecko.com/api/v3/coins/list/new", None, False, None),
    # d — sintéticos / derivados algorítmicos
    ("d", "defillama_stablecoins", "GET", "https://stablecoins.llama.fi/stablecoins?includePrices=true", None, False, "pegmech"),
    ("d", "defillama_derivatives_overview", "GET", "https://api.llama.fi/overview/derivatives?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true", None, False, None),
    ("d", "dydx_v4_markets", "GET", "https://indexer.dydx.trade/v4/perpetualMarkets", None, True, None),
    ("d", "gmx_arbitrum_tickers", "GET", "https://arbitrum-api.gmxinfra.io/prices/tickers", None, False, "count"),
    # a — memes micro-cap (multi-chain: Solana, Base, Blast, Monad)
    ("a", "goplus_token_base", "GET", f"https://api.gopluslabs.io/api/v1/token_security/8453?contract_addresses={DEGEN_BASE}", None, True, None),
    ("a", "goplus_token_solana", "GET", f"https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses={BONK}", None, False, None),
    ("a", "rugcheck_summary", "GET", f"https://api.rugcheck.xyz/v1/tokens/{BONK}/report/summary", None, True, None),
    ("a", "honeypot_is_base", "GET", f"https://api.honeypot.is/v2/IsHoneypot?address={DEGEN_BASE}&chainID=8453", None, False, None),
    ("a", "dexscreener_profiles_latest", "GET", "https://api.dexscreener.com/token-profiles/latest/v1", None, True, "count"),
    ("a", "geckoterminal_new_pools_base", "GET", "https://api.geckoterminal.com/api/v2/networks/base/new_pools", None, False, "count"),
    ("a", "geckoterminal_new_pools_blast", "GET", "https://api.geckoterminal.com/api/v2/networks/blast/new_pools", None, False, "count"),
    ("a", "geckoterminal_new_pools_monad", "GET", "https://api.geckoterminal.com/api/v2/networks/monad/new_pools", None, False, "count"),
]


def rl_headers(h):
    keep = {}
    for k, v in h.items():
        kl = k.lower()
        if "ratelimit" in kl or "rate-limit" in kl or kl in ("retry-after", "x-mbx-used-weight", "x-mbx-used-weight-1m",
                                                              "cf-cache-status", "cache-control", "age"):
            keep[kl] = v
    return keep


def shape(data, depth=0):
    """Campos de primer nivel (y del primer elemento si es lista) para documentar el esquema."""
    if isinstance(data, dict):
        out = {"type": "dict", "keys": sorted(data)[:40]}
        for k in ("data", "result", "protocols", "peggedAssets", "chains", "markets"):
            if k in data and depth == 0:
                out[f"{k}_shape"] = shape(data[k], 1)
        return out
    if isinstance(data, list):
        out = {"type": "list", "len": len(data)}
        if data and depth < 2:
            out["item"] = shape(data[0], depth + 1)
        return out
    return {"type": type(data).__name__}


def iso(ts):
    try:
        ts = float(ts)
        if ts > 1e12:
            ts /= 1000
        return datetime.fromtimestamp(ts, timezone.utc).date().isoformat()
    except (TypeError, ValueError, OSError):
        return None


def coverage(kind, data):
    try:
        if kind == "binance_first":
            return {"first_day": iso(data[0][0])}
        if kind == "binance_funding_first":
            return {"first_funding": iso(data[0]["fundingTime"])}
        if kind == "deribit_first":
            rows = data["result"]["data"]
            return {"first_day_in_page": iso(min(r[0] for r in rows)), "rows": len(rows),
                    "continuation": data["result"].get("continuation")}
        if kind == "fng_first":
            rows = data["data"]
            return {"first_day": iso(min(int(r["timestamp"]) for r in rows)), "rows": len(rows)}
        if kind == "llama_first":
            return {"first_day": iso(data[0]["date"]), "last_day": iso(data[-1]["date"]), "rows": len(data),
                    "last_tvl": data[-1].get("tvl")}
        if kind == "count":
            items = data if isinstance(data, list) else data.get("data", [])
            return {"items": len(items)}
        if kind == "gt_networks":
            return {"page_items": len(data["data"]), "sample_ids": [n["id"] for n in data["data"][:12]],
                    "total_pages": (data.get("meta") or {}).get("total_pages") or (data.get("links") or {}).get("last")}
        if kind == "protocols":
            from collections import Counter
            cats = Counter(p.get("category") for p in data)
            listed = [p.get("listedAt") for p in data if p.get("listedAt")]
            recent = sum(1 for t in listed if NOW - t < 90 * 86400)
            interest = {k: v for k, v in cats.items() if k and any(w in k.lower() for w in
                        ("rwa", "depin", "physical", "governance", "synthetic", "derivative", "algo", "prediction", "launchpad"))}
            return {"protocols": len(data), "top_categories": cats.most_common(25), "categories_of_interest": interest,
                    "listed_last_90d": recent, "first_listed": iso(min(listed)) if listed else None}
        if kind == "pegmech":
            from collections import Counter
            assets = data["peggedAssets"]
            return {"assets": len(assets), "peg_mechanism": dict(Counter(a.get("pegMechanism") for a in assets)),
                    "algorithmic_names": [a.get("symbol") for a in assets if a.get("pegMechanism") == "algorithmic"][:25]}
        if kind == "hl_meta":
            universe = data[0]["universe"]
            ctxs = data[1]
            flags = sorted({k for u in universe for k in u})
            return {"perps": len(universe), "fields_universe": flags, "fields_ctx": sorted(ctxs[0]) if ctxs else [],
                    "delisted": sum(1 for u in universe if u.get("isDelisted"))}
        if kind == "hl_dexs":
            dexs = [d for d in data if d]
            return {"hip3_dexs": len(dexs), "names": [d.get("name") for d in dexs][:20],
                    "assets_first_dex": len(dexs[0].get("assetToStreamingOiCap") or []) if dexs else 0}
        if kind == "aevo_prelaunch":
            from collections import Counter
            pre = [m for m in data if m.get("pre_launch") or m.get("market_type") == "pre_ipo"]
            return {"markets": len(data), "market_types": dict(Counter(m.get("market_type") for m in data)),
                    "pre_market_assets": [m.get("underlying_asset") for m in pre][:20],
                    "fields": sorted(data[0]) if data else []}
    except Exception as e:  # noqa: BLE001 — el probe documenta, no aborta
        return {"coverage_error": f"{type(e).__name__}: {e}"}
    return None


def call(method, url, body):
    t = time.perf_counter()
    try:
        if method == "POST":
            r = requests.post(url, json=body, headers=UA, timeout=25)
        else:
            r = requests.get(url, headers=UA, timeout=25)
        return r, round((time.perf_counter() - t) * 1000), None
    except requests.RequestException as e:
        return None, round((time.perf_counter() - t) * 1000), f"{type(e).__name__}: {str(e)[:160]}"


def probe(src, do_burst):
    group, sid, method, url, body, burst, cov = src
    r, ms, err = call(method, url, body)
    res = {"group": group, "id": sid, "method": method, "url": url, "latency_ms": ms}
    if err:
        res.update(status=None, error=err)
        return res
    res.update(status=r.status_code, bytes=len(r.content), rate_limit_headers=rl_headers(r.headers),
               content_type=r.headers.get("content-type", "")[:60])
    try:
        data = r.json()
        res["shape"] = shape(data)
        if r.ok and cov:
            res["coverage"] = coverage(cov, data)
        if not r.ok:
            res["body_head"] = json.dumps(data)[:300]
    except ValueError:
        res["body_head"] = r.text[:200]
    if burst and do_burst and r.ok:
        statuses, lat = [], []
        for _ in range(BURST):
            rb, msb, errb = call(method, url, body)
            statuses.append(rb.status_code if rb is not None else errb[:40])
            lat.append(msb)
        res["burst"] = {"n": BURST, "statuses": statuses, "n_429": statuses.count(429),
                        "median_ms": sorted(lat)[len(lat) // 2]}
        if res["burst"]["n_429"]:
            time.sleep(COOLDOWN)  # no contaminar la medición de la próxima fuente del mismo proveedor
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description="Probe HTTP de fuentes gratuitas para los 8 grupos (doc 23)")
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--no-burst", action="store_true")
    ap.add_argument("--only", default=None, help="solo este grupo (a..h)")
    args = ap.parse_args(argv)
    results = []
    for src in SOURCES:
        if args.only and src[0] != args.only:
            continue
        res = probe(src, not args.no_burst)
        results.append(res)
        extra = res.get("coverage") or res.get("error") or res.get("body_head", "")[:80]
        print(f"[{res['group']}] {res['id']:<34} {res['status']} {res['latency_ms']:>5} ms "
              f"{('burst429=' + str(res['burst']['n_429'])) if 'burst' in res else ''} {extra}")
        time.sleep(1.5)
    report = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "runner": "local (Argentina)" if not os.environ.get("GITHUB_ACTIONS") else "github-actions (EE.UU.)",
              "burst_size": 0 if args.no_burst else BURST, "results": results}
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[OK] {out} · {sum(1 for r in results if r.get('status') == 200)}/{len(results)} con 200")
    return 0


if __name__ == "__main__":
    sys.exit(main())
