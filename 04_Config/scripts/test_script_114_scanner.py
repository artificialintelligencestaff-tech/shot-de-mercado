#!/usr/bin/env python3
"""Tests del scanner multi-chain v0.2 (unittest, sin red: HTTP simulado). v0.1: scan(); v0.2: fichas por chain,
_categories.json y _history.jsonl.

Uso: python 04_Config/scripts/test_script_114_scanner.py
"""
import json
import math
import os
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

TMP = tempfile.mkdtemp(prefix="s114_")
os.environ["SHOT_ROOT"] = TMP
sys.path.insert(0, str(Path(__file__).resolve().parent))
import script_114_multichain_scanner as s114  # noqa: E402


class FakeResp:
    def __init__(self, status, data=None):
        self.status_code, self._data = status, data

    def json(self):
        return self._data


def coin(cid, ch1, ch24):
    return {"id": cid, "symbol": cid[:3], "name": cid.title(), "current_price": 1.0, "market_cap": 1e9,
            "total_volume": 1e8, "price_change_percentage_1h_in_currency": ch1,
            "price_change_percentage_24h_in_currency": ch24, "price_change_percentage_7d_in_currency": 1.0}


def pool(name, ch1, ch24, net="base"):
    return {"id": f"{net}_0xpool", "attributes": {"address": "0xpool", "name": name, "base_token_price_usd": "0.01",
                                                  "fdv_usd": "100000", "reserve_in_usd": "5000",
                                                  "volume_usd": {"h24": "20000"},
                                                  "price_change_percentage": {"h1": ch1, "h24": ch24},
                                                  "pool_created_at": "2026-09-30T10:00:00Z"},
            "relationships": {"base_token": {"data": {"id": f"{net}_0xtoken"}}}}


class ScannerTest(unittest.TestCase):
    def make_http(self, routes):
        self.urls, self.slept = [], []

        def get(url):
            self.urls.append(url)
            for key, resp in routes.items():
                if key in url:
                    return resp.pop(0) if isinstance(resp, list) else resp
            return FakeResp(404)
        clock = iter(range(0, 10_000, 100))
        return s114.Http(get=get, sleep=self.slept.append, clock=lambda: next(clock))

    def test_grupos_en_orden_de_prioridad_y_marca_de_aceleracion(self):
        http = self.make_http({"ids=bitcoin": FakeResp(200, [coin("bitcoin", 0.1, 2.0)]),
                               "category=layer-1": FakeResp(200, [coin("monad", 12.0, 35.0)]),
                               "category=layer-2": FakeResp(200, [coin("base", 0.5, 5.0)]),
                               "category=governance": FakeResp(200, [coin("uni", 1.0, 21.0)])})
        r = s114.scan(http, groups=["c", "f", "h"], networks=[])
        self.assertEqual(list(r["groups"]), ["h", "f", "c"])                 # h -> f -> c aunque se pidan al revés
        acc = {a["id"]: a for a in r["accelerating"]}
        self.assertEqual(sorted(acc), ["monad", "uni"])
        self.assertEqual(acc["monad"]["reasons"], ["24h +35.0% (>= +20%)", "1h +12.0% (>= +10%)"])
        self.assertEqual(r["accelerating"][0]["id"], "monad")                # ordenado por cambio 24 h
        self.assertEqual(r["not_covered"], s114.NO_FREE_SOURCE)

    def test_onchain_por_red(self):
        http = self.make_http({"networks/base/trending_pools": FakeResp(200, {"data": [pool("PEPE / WETH", 25.0, 80.0)]}),
                               "networks/monad/trending_pools": FakeResp(200, {"data": []})})
        r = s114.scan(http, groups=[], networks=["base", "monad"])
        item = r["onchain"]["base"]["items"][0]
        self.assertEqual((item["symbol"], item["token_address"], item["chain"]), ("PEPE", "0xtoken", "base"))
        self.assertEqual(r["accelerating"][0]["chain"], "base")
        self.assertEqual(r["onchain"]["monad"]["items"], [])

    def test_429_reintenta_una_vez_y_despues_registra_error(self):
        http = self.make_http({"ids=bitcoin": [FakeResp(429), FakeResp(200, [coin("bitcoin", 0, 0)])],
                               "category=layer-1": [FakeResp(429), FakeResp(429)],
                               "category=layer-2": FakeResp(200, [])})
        r = s114.scan(http, groups=["h", "f"], networks=[])
        self.assertEqual(len(r["groups"]["h"]["items"]), 1)                  # el reintento funcionó
        self.assertIn({"group": "f", "source": "layer-1", "status": 429}, r["errors"])
        self.assertIn(30.0, self.slept)                                      # esperó antes de reintentar

    def test_espaciado_por_host(self):
        http = s114.Http(get=lambda url: FakeResp(200, []), sleep=self._record, clock=lambda: 0.0)
        self.waits = []
        http.get_json(s114.CG + "/a")
        http.get_json(s114.CG + "/b")
        http.get_json(s114.GT + "/c")
        self.assertEqual(self.waits, [15.0])                                 # 2.º CoinGecko espera; GT no

    def _record(self, s):
        self.waits.append(s)

    def test_main_escribe_json_y_rechaza_grupo_b(self):
        out = Path(TMP) / "scan.json"
        orig = s114.scan
        s114.scan = lambda http, groups, networks: {"groups": {}, "onchain": {}, "accelerating": [], "errors": [],
                                                    "calls": 0}
        try:
            self.assertEqual(s114.main(["--groups", "h", "--networks", "", "--out", str(out), "--no-cards"]), 0)
            self.assertEqual(json.loads(out.read_text(encoding="utf-8"))["calls"], 0)
            with self.assertRaises(SystemExit):
                s114.main(["--groups", "b", "--out", str(out)])
        finally:
            s114.scan = orig


DAY = 86400
T0 = 1790800000                                                            # 2026-10-01 aprox, en s


def llama_series(values, start=T0 - 40 * DAY, skip=()):
    return [{"date": start + i * DAY, "tvl": v} for i, v in enumerate(values) if i not in skip]


def overview(total24h, total30d, change_1d=1.5):
    return {"total24h": total24h, "total7d": total24h * 7, "total30d": total30d, "change_1d": change_1d,
            "change_7d": -2.0, "change_1m": 10.0, "protocols": [{"name": "x"}]}


def cg_cat(cid, mcap, chg):
    return {"id": cid, "name": cid.title(), "market_cap": mcap, "market_cap_change_24h": chg, "volume_24h": mcap / 20,
            "top_3_coins_id": ["a", "b", "c"], "updated_at": "2026-10-01T14:00:00Z"}


class FichasTest(unittest.TestCase):
    """v0.2: fichas por chain, categorías e historial."""

    def http(self, routes):
        self.urls = []

        def get(url):
            self.urls.append(url)
            for key, resp in routes.items():
                if key in url:
                    return resp.pop(0) if isinstance(resp, list) else resp
            return FakeResp(404)
        clock = iter(range(0, 1_000_000, 100))
        return s114.Http(get=get, sleep=lambda s: None, clock=lambda: next(clock))

    def base_report(self):
        return {"generated_at": "2026-10-01T15:00:00+00:00", "errors": [], "accelerating": [{"id": "x"}], "calls": 9,
                "groups": {"h": {"sources": [{"source": "coingecko:ids=bitcoin,ethereum,solana", "status": 200}],
                                 "items": [dict(s114.cg_item(coin("ethereum", 0.2, 3.0)), source="bitcoin,ethereum,solana")]},
                           "f": {"sources": [{"source": "coingecko:category=layer-1", "status": 200},
                                             {"source": "coingecko:category=layer-2", "status": 429}],
                                 "items": [dict(s114.cg_item(coin(c, h1, h24)), source="layer-1")
                                           for c, h1, h24 in (("aaa", 1.0, 30.0), ("bbb", -1.0, -4.0),
                                                              ("ccc", 0.5, 2.0), ("ddd", None, None))]}},
                "onchain": {"base": {"status": 200, "items": [s114.gt_item(pool("PEPE / WETH", 25.0, 80.0), "base")]}}}

    def test_tvl_metrics_cambios_y_aceleracion(self):
        vals = [100.0] * 26 + [100.0 + 2 * i for i in range(15)]           # crece 2/día los últimos 14 días
        m = s114.tvl_metrics(llama_series(vals, skip={38}))                   # falta un día: tolera el hueco
        self.assertEqual(m["tvl_usd"], 128.0)
        self.assertAlmostEqual(m["change_1d_pct"], (128 / 126 - 1) * 100)
        self.assertAlmostEqual(m["change_7d_pct"], (128 / 114 - 1) * 100)
        self.assertAlmostEqual(m["change_30d_pct"], 28.0)
        self.assertAlmostEqual(m["accel_7d"], math.log(128 / 114) - math.log(114 / 100))
        self.assertEqual(m["days"], 40)
        self.assertIsNone(s114.tvl_metrics([]))
        self.assertIsNone(s114.tvl_metrics([{"date": "x", "tvl": 1}]))
        short = s114.tvl_metrics(llama_series([5.0, 6.0]))
        self.assertIsNone(short["change_7d_pct"])
        self.assertIsNone(short["accel_7d"])

    def test_overview_metrics(self):
        m = s114.overview_metrics(overview(1000.0, 30000.0))
        self.assertEqual((m["total24h"], m["total30d"], m["change_1d"]), (1000.0, 30000.0, 1.5))
        self.assertIsNone(s114.overview_metrics({"protocols": []}))
        self.assertIsNone(s114.overview_metrics(None))
        self.assertIsNone(s114._f(float("nan")))                            # NaN no llega al JSON

    def test_fichas_por_chain(self):
        routes = {
            "/v2/chains": FakeResp(200, [{"name": "Base", "tvl": 6e9, "gecko_id": None},
                                         {"name": "Arbitrum", "tvl": 2e9, "gecko_id": "arbitrum"},
                                         {"name": "OP Mainnet", "tvl": 5e8, "gecko_id": "optimism"},
                                         {"name": "Ethereum", "tvl": 6e10, "gecko_id": "ethereum"},
                                         {"name": "Bitcoin", "tvl": 7e9, "gecko_id": "bitcoin"}]),
            "historicalChainTvl/Base": FakeResp(200, llama_series([100.0] * 40)),
            "historicalChainTvl/OP%20Mainnet": FakeResp(404),
            "historicalChainTvl/Optimism": FakeResp(200, llama_series([50.0] * 40)),
            "historicalChainTvl/Arbitrum": FakeResp(200, llama_series([200.0] * 40)),
            "historicalChainTvl/Ethereum": FakeResp(200, llama_series([1000.0] * 40)),
            "historicalChainTvl/Bitcoin": FakeResp(200, llama_series([70.0] * 40)),
            "overview/dexs/Base": FakeResp(200, overview(10.0, 300.0)),
            "overview/fees/Base": FakeResp(200, overview(1.0, 30.0)),
            "overview/dexs/Bitcoin": FakeResp(404),
            "ids=arbitrum,bitcoin,optimism": FakeResp(200, [coin("arbitrum", 1.0, 25.0), coin("optimism", 0.0, 1.0),
                                                            coin("bitcoin", 0.1, 0.5)]),
            "networks/base/new_pools": FakeResp(200, {"data": [
                {"attributes": {"pool_created_at": "2026-10-01T14:30:00Z"}},
                {"attributes": {"pool_created_at": "2026-10-01T13:00:00Z"}}]}),
        }
        now = datetime(2026, 10, 1, 15, 0, tzinfo=timezone.utc)
        cards, shared = s114.build_chain_cards(self.http(routes), self.base_report(), now,
                                               chains=["bitcoin", "ethereum", "base", "arbitrum", "optimism"])
        self.assertEqual(list(cards), ["bitcoin", "ethereum", "base", "arbitrum", "optimism"])
        base = cards["base"]
        self.assertIsNone(base["native_token"])
        self.assertIn("ETH", base["native_token_note"])
        self.assertEqual(base["tvl"]["tvl_usd"], 100.0)
        self.assertAlmostEqual(base["derived"]["fees_tvl_annualized_pct"], 30.0 * 365 / 30 / 100.0 * 100)
        self.assertAlmostEqual(base["derived"]["dex_volume_tvl_24h"], 0.1)
        self.assertEqual(base["onchain"]["trending"]["pools"], 1)              # reusa scan(): sin llamada extra
        self.assertEqual(base["onchain"]["trending"]["accelerating"], 1)
        self.assertEqual(base["onchain"]["new_pools"]["page1"], 2)
        self.assertAlmostEqual(base["onchain"]["new_pools"]["per_hour_est"], 1.0)
        self.assertEqual(sum("trending_pools" in u for u in self.urls), 0)
        self.assertEqual(cards["ethereum"]["native_token"]["id"], "ethereum")  # del grupo h, sin pedirlo de nuevo
        self.assertEqual(sum("ids=" in u for u in self.urls), 1)               # nativos faltantes en UNA llamada
        self.assertEqual(cards["arbitrum"]["native_token"]["change_24h"], 25.0)
        self.assertEqual(cards["optimism"]["defillama_name"], "Optimism")     # alias tras 404 de "OP Mainnet"
        btc = cards["bitcoin"]
        self.assertIsNone(btc["onchain"])
        self.assertTrue(any(m.startswith("dex_volume") for m in btc["missing"]))
        self.assertTrue(any(m.startswith("onchain") for m in btc["missing"]))
        self.assertIn({"source": "defillama:/v2/chains", "status": 200}, shared)

    def test_fichas_sin_defillama_no_fallan(self):
        cards, shared = s114.build_chain_cards(self.http({}), {"groups": {}, "onchain": {}}, chains=["monad"])
        monad = cards["monad"]
        self.assertIsNone(monad["tvl"])
        self.assertTrue(any("gecko_id" in m for m in monad["missing"]))
        self.assertEqual(shared[0]["status"], 404)

    def test_categorias(self):
        routes = {"coins/categories": FakeResp(200, [cg_cat("layer-1", 2e12, 1.2), cg_cat("depin", 2e10, -3.0),
                                                      cg_cat("governance", 5e9, 4.0)])}
        cats = s114.build_categories(self.http(routes), self.base_report())
        self.assertEqual(list(cats["categories"]), list(s114.CATEGORIES))
        l1 = cats["categories"]["layer-1"]
        self.assertEqual((l1["market_cap_usd"], l1["market_cap_change_24h_pct"], l1["group"]), (2e12, 1.2, "f"))
        sample = l1["sample"]
        self.assertEqual((sample["n"], sample["accelerating"]), (4, 1))
        self.assertAlmostEqual(sample["median_change_24h"], 2.0)
        self.assertAlmostEqual(sample["breadth_24h"], 2 / 3)                 # sin dato no cuenta
        self.assertEqual(sample["top_gainers_24h"][0]["id"], "aaa")
        self.assertEqual(sample["top_losers_24h"][0]["id"], "bbb")
        self.assertEqual(cats["categories"]["layer-2"]["sample"]["source_status"], 429)
        self.assertEqual(cats["categories"]["layer-2"]["category_status"], "no listada en coins/categories")
        self.assertIn("no consultada", cats["categories"]["depin"]["sample"]["source_status"])
        self.assertEqual(cats["ranking_24h"], ["governance", "layer-1", "depin"])

    def test_salidas_e_historial(self):
        out_dir = Path(TMP) / "salidas"
        report = self.base_report()
        cards = {"base": {"chain": "base", "tvl": {"tvl_usd": 1e9, "change_7d_pct": 2.0, "accel_7d": 0.01},
                          "native_token": None, "dex_volume": {"total24h": 5e7}, "fees": {"total24h": 1e5},
                          "onchain": {"trending": {"pools": 20, "accelerating": 3}, "new_pools": {"per_hour_est": 4.2}}}}
        cats = {"categories": {"layer-1": {"market_cap_usd": 2e12, "market_cap_change_24h_pct": 1.2,
                                           "volume_24h_usd": 1e11, "sample": {"breadth_24h": 0.6, "median_change_24h": 1.1}}}}
        for _ in range(2):
            s114.write_outputs(out_dir / "scan_latest.json", report, None, cards, cats, calls=42)
        self.assertEqual(sorted(p.name for p in out_dir.iterdir()),
                         ["_categories.json", "_history.jsonl", "base.json", "scan_latest.json"])
        lines = (out_dir / "_history.jsonl").read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 2)                                       # append, no sobrescribe
        h = json.loads(lines[-1])
        self.assertEqual((h["calls"], h["accelerating"], h["chains"]["base"]["trend_acc"]), (42, 1, 3))
        self.assertEqual(h["categories"]["layer-1"]["chg24"], 1.2)
        self.assertEqual(json.loads((out_dir / "scan_latest.json").read_text(encoding="utf-8")), report)
        self.assertFalse(list(out_dir.glob("*.tmp")))

    def test_scan_latest_mantiene_el_esquema_v01(self):
        http = self.http({"ids=bitcoin": FakeResp(200, [coin("bitcoin", 0, 0)])})
        r = s114.scan(http, groups=["h"], networks=[])
        self.assertEqual(set(r), {"generated_at", "scanner_version", "accel_rule", "groups", "onchain", "not_covered",
                                  "accelerating", "errors", "calls"})
        self.assertEqual(set(r["groups"]["h"]["items"][0]), {"id", "symbol", "name", "price_usd", "mcap_usd",
                                                              "volume_24h_usd", "change_1h", "change_24h", "change_7d",
                                                              "source"})

    def test_cobertura_de_la_directiva(self):
        self.assertEqual(list(s114.CATEGORIES), ["layer-1", "layer-2", "governance", "depin", "real-world-assets-rwa",
                                                 "decentralized-perpetuals", "synthetic-issuer"])
        self.assertTrue({"bitcoin", "ethereum", "solana", "base", "arbitrum", "optimism", "blast", "monad"} <= set(s114.CHAINS))
        self.assertTrue({"arbitrum", "optimism", "blast", "monad", "base"} <= set(s114.NETWORKS))

    def test_solo_recoleccion_sin_emision_ni_score(self):
        src = Path(s114.__file__).read_text(encoding="utf-8").lower()
        for forbidden in ("api.telegram.org", "sendmessage", "senddocument", "script_82", "script_97", "score_token"):
            self.assertNotIn(forbidden, src)

    def test_main_completo_y_dry_run(self):
        out = Path(TMP) / "main" / "scan_latest.json"
        http = self.http({"coins/markets": FakeResp(200, []), "coins/categories": FakeResp(200, []),
                          "/v2/chains": FakeResp(200, [])})
        self.assertEqual(s114.main(["--groups", "h", "--networks", "", "--chains", "base", "--out", str(out),
                                    "--dry-run"], http=http), 0)
        self.assertFalse(out.parent.exists())
        self.assertEqual(s114.main(["--groups", "h", "--networks", "", "--chains", "base", "--out", str(out)],
                                   http=http), 0)
        self.assertEqual(sorted(p.name for p in out.parent.iterdir()),
                         ["_categories.json", "_history.jsonl", "base.json", "scan_latest.json"])
        with self.assertRaises(SystemExit):
            s114.main(["--chains", "dogechain", "--out", str(out)], http=http)

def tearDownModule():
    shutil.rmtree(TMP, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
