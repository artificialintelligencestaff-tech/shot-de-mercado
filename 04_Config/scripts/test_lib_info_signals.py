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


if __name__ == "__main__":
    unittest.main(verbosity=2)
