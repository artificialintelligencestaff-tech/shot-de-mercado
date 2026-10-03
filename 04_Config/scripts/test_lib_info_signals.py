#!/usr/bin/env python3
"""lib_info_signals (D-014-R-3): señales informacionales y estructurales. unittest, sin red, datos sintéticos.

Uso: python 04_Config/scripts/test_lib_info_signals.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_info_signals as inf  # noqa: E402

NOW = 1_790_900_000.0


class Info(unittest.TestCase):
    def test_palabras_clave(self):
        self.assertEqual(inf.keywords("Pepe the Frog 2.0", "PEPE"), {"pepe", "frog"})
        self.assertEqual(inf.keywords("AI Coin", "X"), set())

    def test_ola_narrativa(self):
        idx = inf.keyword_index([("m1", "Frog King", "FROG"), ("m2", "Baby Frog", "BFROG"), ("m3", "Frog Wars", "FW"),
                                 ("m4", "Cat", "CAT")])
        s = inf.narrative_wave("m1", "Frog King", "FROG", idx)
        self.assertAlmostEqual(s["s"], 2 / 8)
        self.assertIn("frog", s["detail"])
        self.assertEqual(inf.narrative_wave("m4", "Cat", "CAT", idx)["s"], 0.0)
        self.assertIsNone(inf.narrative_wave("m5", "", "", idx))

    def test_trending(self):
        tr = [{"rank": 1, "symbol": "PENGU", "name": "Pudgy Penguins"}, {"rank": 2, "symbol": "MON", "name": "Monad"}]
        self.assertEqual(inf.trending_match("Pengu Sol", "PENGU", tr)["s"], 1.0)
        self.assertEqual(inf.trending_match("Monad Kitty", "MKIT", tr)["s"], 0.6)
        self.assertEqual(inf.trending_match("Dog", "DOG", tr)["s"], 0.0)
        self.assertIsNone(inf.trending_match("Dog", "DOG", None))

    def test_metadata_y_repo(self):
        full = {"twitter": "https://x.com/a", "telegram": "https://t.me/a", "website": "https://github.com/acme/agent",
                "description": "x" * 50}
        self.assertEqual(inf.metadata_socials(full)["s"], 1.0)
        self.assertEqual(inf.metadata_socials({})["s"], 0.0)
        self.assertIsNone(inf.metadata_socials(None))
        self.assertEqual(inf.github_link(full), "acme/agent")
        self.assertIsNone(inf.github_link({"website": "https://acme.io"}))
        self.assertEqual(inf.github_repo({"stargazers_count": 99, "full_name": "acme/agent"})["s"], 1.0)
        self.assertIsNone(inf.github_repo({"message": "Not Found"}))

    def test_perfil_dexscreener(self):
        self.assertEqual(inf.dex_profile("m", {"m"}, {"m": 500})["s"], 1.0)
        self.assertEqual(inf.dex_profile("m", {"m"}, {})["s"], 0.6)
        self.assertEqual(inf.dex_profile("z", set(), {})["s"], 0.0)
        self.assertIsNone(inf.dex_profile("m", None, None))

    def test_menciones(self):
        items = [{"ts": NOW - 60, "a": ["MINT"], "c": [], "f": "reddit_rss"},
                 {"ts": NOW - 120, "a": [], "c": ["frog"], "f": "4chan_biz"},
                 {"ts": NOW - 7200, "a": ["MINT"], "c": [], "f": "telegram_web"}]
        s = inf.mentions("MINT", "FROG", items, NOW)
        self.assertAlmostEqual(s["s"], 1.25 / 5)
        self.assertIn("26 h 2.25", s["detail"])
        self.assertIsNone(inf.mentions("MINT", "FROG", None, NOW))

    def test_estructurales(self):
        self.assertEqual(inf.bonding_progress({"dexId": "pumpswap"})["s"], 1.0)
        self.assertAlmostEqual(inf.bonding_progress({"dexId": "pumpfun", "marketCapUsd": 34_500})["s"], 0.5)
        self.assertIsNone(inf.bonding_progress({}))
        self.assertEqual(inf.holders_struct({"holders": 600, "top10_pct": 20})["s"], 1.0)
        self.assertEqual(inf.holders_struct({"holders": 600, "top10_pct": 45})["s"], 0.5)
        self.assertEqual(inf.dev_wallet({"initialBuy": 10_000_000})["s"], 1.0)        # 1 %
        self.assertEqual(inf.dev_wallet({"initialBuy": 120_000_000})["s"], 0.0)       # 12 %
        self.assertIsNone(inf.dev_wallet({}))


class NuevasD023(unittest.TestCase):
    """S-1..S-4 y tradability (D-023-R3)."""

    def test_s1_velocidad_de_curva(self):
        s = inf.bonding_curve_velocity([(NOW - 600, 0.10), (NOW - 300, 0.15), (NOW, 0.30)])   # +20 % en 10 min
        self.assertEqual(s["s"], 1.0)
        self.assertIn("+2.00 %/min", s["detail"])
        self.assertEqual(inf.bonding_curve_velocity([(NOW - 120, 0.5), (NOW, 0.45)])["s"], 0.0)   # retrocede: 0
        self.assertIsNone(inf.bonding_curve_velocity([(NOW, 0.1)]))

    def test_s2_aceleracion_de_compradores_unicos(self):
        prev = [(NOW - 200, f"w{i}", "buy", 0.1) for i in range(2)]
        last = [(NOW - 60, f"n{i}", "buy", 0.1) for i in range(12)] + [(NOW - 50, "w0", "buy", 0.1)]   # w0 repite
        s = inf.unique_buyer_acceleration(prev + last + [(NOW - 10, "x", "sell", 1.0)], NOW)
        self.assertEqual(s["s"], 1.0)                      # (12 − 2) / 2 min = 5/min
        self.assertIn("compradores nuevos 12 vs 2", s["detail"])
        self.assertEqual(inf.unique_buyer_acceleration(prev, NOW)["s"], 0.0)
        self.assertIsNone(inf.unique_buyer_acceleration([], NOW))

    def test_s3_tendencia_del_tamano_de_compra(self):
        growing = [(NOW - 100 + i, f"w{i}", "buy", 0.1 * (1 + i)) for i in range(10)]
        self.assertEqual(inf.avg_buy_size_trend(growing)["s"], 1.0)
        shrinking = [(NOW - 100 + i, f"w{i}", "buy", 1.0 - 0.09 * i) for i in range(10)]
        self.assertEqual(inf.avg_buy_size_trend(shrinking)["s"], 0.0)
        self.assertIsNone(inf.avg_buy_size_trend(growing[:4]))

    def test_s4_holders_por_txn(self):
        self.assertEqual(inf.holder_to_txn_ratio(100, 200)["s"], 1.0)
        self.assertAlmostEqual(inf.holder_to_txn_ratio(20, 200)["s"], 0.2)
        self.assertIsNone(inf.holder_to_txn_ratio(None, 200))
        self.assertIsNone(inf.holder_to_txn_ratio(10, 0))

    def test_tradability_informativa(self):
        curve = inf.tradability({"dexId": "pumpfun", "priceUsd": 0.001, "liquidityUsd": 0},
                                [(NOW - 60, 0.0), (NOW, 0.0)])
        self.assertEqual(curve, {"tradable": True, "liquidity_usd": 0.0, "buy_route": "pump.fun (curva de bonding)",
                                 "initial_liquidity_usd": 0.0})
        amm = inf.tradability({"dexId": "pumpswap", "priceUsd": 0.01, "liquidityUsd": 500}, [(NOW, 450.0)])
        self.assertEqual((amm["tradable"], amm["initial_liquidity_usd"]), (False, 450.0))   # < $1K de liquidez
        self.assertFalse(inf.tradability({}, None)["tradable"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
