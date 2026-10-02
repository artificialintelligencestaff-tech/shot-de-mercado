#!/usr/bin/env python3
"""lib_scoring_young v0.2 (D-014-R-3): 60 % informacional / 25 % estructural / 15 % precio-volumen. unittest, sin red.

Uso: python 04_Config/scripts/test_lib_scoring_young.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_early_signals as es  # noqa: E402
import lib_info_signals as inf  # noqa: E402
import lib_scoring_young as ly  # noqa: E402

NOW = 1_790_900_000.0


def token(age_min=15, liq=0.0, initial_buy=10_000_000, change24=150.0, **dx):
    d = {"pairCreatedAt": int((NOW - age_min * 60) * 1000), "liquidityUsd": liq, "priceChange24h": change24,
         "volume_m5": 6000, "volume_h1": 15000, "txns_m5_buys": 30, "txns_m5_sells": 8,
         "txns_h1_buys": 100, "txns_h1_sells": 100, "priceChange_m5": 2.0, "dexId": "pumpfun", "marketCapUsd": 34_500}
    d.update(dx)
    return {"token": {"mint": "M", "initialBuy": initial_buy}, "dexscreener": d}


def price(t):
    return es.dex_signals(t["dexscreener"], [])


def info_full():
    return [{"name": n, "s": 1.0, "detail": "x"} for n in ly.INFO_WEIGHTS]


def struct(t, rug=None):
    return [inf.bonding_progress(t["dexscreener"]), inf.holders_struct(rug), inf.dev_wallet(t["token"])]


class Young(unittest.TestCase):
    def test_pesos_suman_100(self):
        self.assertEqual(sum(ly.INFO_WEIGHTS.values()), 60)
        self.assertEqual(sum(ly.STRUCT_WEIGHTS.values()), 25)
        self.assertEqual(ly.PRICE_WEIGHT, 15)

    def test_todo_al_maximo_da_100_y_emite(self):
        t = token()
        full_price = [{"name": n, "s": 1.0, "points": p} for n, p in ly.PRICE_SIGNALS.items()]
        full_struct = [{"name": n, "s": 1.0} for n in ly.STRUCT_WEIGHTS]
        d = ly.score_young_detail(t, full_price, info_full(), NOW, structural=full_struct)
        self.assertEqual((d["score"], d["coverage"], d["fires"]), (100, 100, True))

    def test_liquidez_cero_se_acepta(self):
        t = token(liq=0.0)
        d = ly.score_young_detail(t, price(t), info_full(), NOW, structural=struct(t))
        self.assertGreater(d["score"], 60)
        self.assertEqual(d["blocks"], [])
        self.assertTrue(d["fires"])

    def test_sin_evidencia_informacional_no_emite(self):
        t = token()
        full_struct = [{"name": n, "s": 1.0} for n in ly.STRUCT_WEIGHTS]
        full_price = [{"name": n, "s": 1.0, "points": p} for n, p in ly.PRICE_SIGNALS.items()]
        weak_info = [{"name": "metadata_socials", "s": 1.0}]                       # 10 < INFO_MIN
        d = ly.score_young_detail(t, full_price, weak_info, NOW, structural=full_struct)
        self.assertEqual(d["score"], 50)                                          # 10 + 25 + 15
        self.assertFalse(d["fires"])
        self.assertFalse(ly.fires(d["score"], d["parts"]["info"]))

    def test_info_domina_sobre_precio(self):
        t = token()
        only_price = ly.score_young_detail(t, [{"name": n, "s": 1.0, "points": p} for n, p in ly.PRICE_SIGNALS.items()],
                                           [], NOW)
        only_info = ly.score_young_detail(t, [], info_full(), NOW)
        self.assertEqual((only_price["score"], only_info["score"]), (15, 60))

    def test_kill_switches_cortan(self):
        t = token(initial_buy=200_000_000)
        d = ly.score_young_detail(t, price(t), info_full(), NOW, structural=struct(t))
        self.assertEqual(d["score"], 0)
        self.assertFalse(d["fires"])
        self.assertTrue(any("sin filtros sería" in r for r in d["reasons"]))
        bad = ly.kill_switches(token(), {"mint_authority": "X", "holders": 10, "top10_pct": 70}, 15)
        self.assertEqual(len(bad), 3)
        self.assertIn("kill switch de script_82", ly.kill_switches(token(age_min=3, change24=50_000), None, 3)[0])

    def test_fuera_de_alcance(self):
        self.assertIsNone(ly.score_young(token(age_min=75), [], info_full(), NOW)[0])
        t = token()
        t["dexscreener"]["pairCreatedAt"] = 0
        self.assertIsNone(ly.score_young(t, [], info_full(), NOW)[0])

    def test_variantes(self):
        t = token()
        v = ly.variants(price(t), info_full())
        self.assertEqual(set(v), {"A_ge3_active", "B_ge3_strong", "C_points_ge4", "I_ge2_info"})
        self.assertTrue(v["I_ge2_info"])
        self.assertFalse(ly.variants([], [{"name": "mentions", "s": 0.5}])["I_ge2_info"])

    def test_registro_jsonl(self):
        tmp = Path(tempfile.mkdtemp(prefix="young_"))
        self.addCleanup(shutil.rmtree, tmp, True)
        t = token()
        d = ly.score_young_detail(t, price(t), info_full(), NOW, structural=struct(t))
        self.assertTrue(ly.should_log(None, d))
        self.assertFalse(ly.should_log(d["score"] - 2, d))
        self.assertTrue(ly.should_log(d["score"] - 2, d, emitted=True))
        rec = ly.young_record("M", "TST", d, price(t), info_full(), struct(t), "2026-10-02T00:00:00+00:00", "a")
        p = ly.append_jsonl(tmp / "y" / "a.jsonl", rec)
        ly.append_jsonl(p, rec)
        lines = p.read_text().splitlines()
        self.assertEqual(len(lines), 2)
        got = json.loads(lines[0])
        self.assertEqual((got["mint"], got["version"], got["variant"]), ("M", ly.VERSION, ly.VERSION))
        self.assertEqual(got["signals_info"]["mentions"], 1.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
