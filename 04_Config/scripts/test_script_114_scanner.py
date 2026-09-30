#!/usr/bin/env python3
"""Tests del scanner multi-chain v0 (unittest, sin red: HTTP simulado).

Uso: python 04_Config/scripts/test_script_114_scanner.py
"""
import json
import os
import shutil
import sys
import tempfile
import unittest
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
            self.assertEqual(s114.main(["--groups", "h", "--networks", "", "--out", str(out)]), 0)
            self.assertEqual(json.loads(out.read_text(encoding="utf-8"))["calls"], 0)
            with self.assertRaises(SystemExit):
                s114.main(["--groups", "b", "--out", str(out)])
        finally:
            s114.scan = orig


def tearDownModule():
    shutil.rmtree(TMP, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
