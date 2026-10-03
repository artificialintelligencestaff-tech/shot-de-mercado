#!/usr/bin/env python3
"""lib_scoring_young v0.4 (D-023-R3): pesos continuos por edad, grupo estructural redistribuido, umbral 40 /
info mínima 5, flags informativos. unittest, sin red, datos sintéticos.

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
         "txns_h1_buys": 100, "txns_h1_sells": 100, "priceChange_m5": 2.0, "dexId": "pumpfun", "marketCapUsd": 34_500,
         "priceUsd": 0.001}
    d.update(dx)
    return {"token": {"mint": "M", "initialBuy": initial_buy}, "dexscreener": d}


def full(names, **extra):
    return [dict({"name": n, "s": 1.0, "detail": "x"}, **extra) for n in names]


FULL_PRICE = [{"name": n, "s": 1.0, "points": p} for n, p in ly.PRICE_SIGNALS.items()]


class Pesos(unittest.TestCase):
    def test_cortes_de_la_tabla(self):
        table = {0: (70, 15, 15), 10: (60, 20, 20), 30: (50, 25, 25), 60: (40, 25, 35), 360: (30, 25, 45),
                 1440: (20, 20, 60), 10_000: (20, 20, 60)}
        for age, (i, st, pv) in table.items():
            self.assertEqual(ly.weights_for_age(age), {"info": i, "struct": st, "pv": pv}, age)

    def test_interpolacion_continua_suma_100_y_minimo_15(self):
        self.assertEqual(ly.weights_for_age(20), {"info": 55.0, "struct": 22.5, "pv": 22.5})
        prev = None
        for a in range(0, 2000):
            w = ly.weights_for_age(a)
            self.assertAlmostEqual(sum(w.values()), 100.0)
            self.assertGreaterEqual(min(w.values()), 15.0)
            if prev:                                    # continua: saltos chicos entre minutos vecinos
                self.assertLessEqual(max(abs(w[k] - prev[k]) for k in w), 1.0)   # <= 1 punto por minuto
            prev = w
        self.assertEqual(ly.weights_for_age(None), ly.weights_for_age(0))

    def test_estructural_redistribuido(self):
        self.assertEqual(ly.STRUCT_WEIGHTS, {"bonding_progress": 12, "holders_struct": 6, "dev_wallet": 3,
                                             "bonding_curve_velocity": 1, "unique_buyer_acceleration": 1,
                                             "avg_buy_size_trend": 1, "holder_to_txn_ratio": 1})
        self.assertEqual(sum(ly.STRUCT_WEIGHTS.values()), 25)


class Score(unittest.TestCase):
    def test_todo_al_maximo_da_100_en_cualquier_edad(self):
        for age in (2, 15, 45):
            d = ly.score_young_detail(token(age_min=age), FULL_PRICE, full(ly.INFO_WEIGHTS), NOW,
                                      structural=full(ly.STRUCT_WEIGHTS))
            self.assertEqual((d["score"], round(d["coverage"]), d["fires"]), (100, 100, True), age)

    def test_la_edad_cambia_el_peso_del_grupo(self):
        only_info = [ly.score_young_detail(token(age_min=a), [], full(ly.INFO_WEIGHTS), NOW)["score"] for a in (0.5, 30, 59)]
        self.assertEqual(only_info, [70, 50, 40])
        only_pv = [ly.score_young_detail(token(age_min=a), FULL_PRICE, [], NOW)["score"] for a in (0.5, 30, 59)]
        self.assertEqual(only_pv, [15, 25, 35])

    def test_umbral_40_e_info_minima_5(self):
        self.assertEqual((ly.YOUNG_THRESHOLD, ly.INFO_MIN), (40, 5))
        t = token(age_min=30)                              # pesos 50 / 25 / 25
        no_info = ly.score_young_detail(t, FULL_PRICE, [], NOW, structural=full(ly.STRUCT_WEIGHTS))
        self.assertEqual((no_info["score"], no_info["fires"]), (50, False))       # 50 >= 40 pero info 0 < 5
        tiny = ly.score_young_detail(t, FULL_PRICE, [{"name": "dex_profile", "s": 1.0}], NOW,
                                     structural=full(ly.STRUCT_WEIGHTS))
        self.assertAlmostEqual(tiny["info_score"], 50 * 5 / 60, places=2)        # 4,17 < 5
        self.assertFalse(tiny["fires"])
        ok = ly.score_young_detail(t, FULL_PRICE, [{"name": "metadata_socials", "s": 1.0}], NOW,
                                   structural=full(ly.STRUCT_WEIGHTS))
        self.assertTrue(ok["fires"])                                            # info 8,3 >= 5

    def test_liquidez_cero_y_flag_informativo(self):
        t = token(liq=0.0)
        flags = inf.tradability(t["dexscreener"], [(NOW - 300, 0.0), (NOW, 0.0)])
        d = ly.score_young_detail(t, es.dex_signals(t["dexscreener"], []), full(ly.INFO_WEIGHTS), NOW,
                                  structural=full(ly.STRUCT_WEIGHTS), flags=flags)
        self.assertTrue(d["fires"])
        self.assertEqual(d["flags"]["buy_route"], "pump.fun (curva de bonding)")
        self.assertTrue(d["flags"]["tradable"])
        same = ly.score_young_detail(t, es.dex_signals(t["dexscreener"], []), full(ly.INFO_WEIGHTS), NOW,
                                     structural=full(ly.STRUCT_WEIGHTS))
        self.assertEqual(d["score"], same["score"])                              # el flag no suma

    def test_kill_switches_y_alcance(self):
        d = ly.score_young_detail(token(initial_buy=200_000_000), FULL_PRICE, full(ly.INFO_WEIGHTS), NOW)
        self.assertEqual((d["score"], d["fires"]), (0, False))
        self.assertEqual(len(ly.kill_switches(token(), {"mint_authority": "X", "holders": 10, "top10_pct": 70}, 15)), 3)
        self.assertIsNone(ly.score_young(token(age_min=75), [], full(ly.INFO_WEIGHTS), NOW)[0])

    def test_subtotales_variantes_y_jsonl(self):
        t = token(age_min=10)                             # 60 / 20 / 20
        d = ly.score_young_detail(t, [], [{"name": "mentions", "s": 1.0}, {"name": "narrative_wave", "s": 1.0}], NOW,
                                  structural=[{"name": "bonding_progress", "s": 1.0}])
        self.assertEqual((d["info_score"], d["struct_score"], d["pv_score"], d["h0_group"]),
                         (30.0, 9.6, 0, "info_ge20"))
        self.assertEqual(d["weights"], {"info": 60.0, "struct": 20.0, "pv": 20.0})
        self.assertTrue(ly.variants([], full(ly.INFO_WEIGHTS))["I_ge2_info"])
        tmp = Path(tempfile.mkdtemp(prefix="young_"))
        self.addCleanup(shutil.rmtree, tmp, True)
        rec = ly.young_record("M", "T", d, [], [], [], "x", "a")
        p = ly.append_jsonl(tmp / "a.jsonl", rec)
        got = json.loads(p.read_text().splitlines()[0])
        self.assertEqual((got["version"], got["weights"]["info"], got["info_score"]), ("young-0.4", 60.0, 30.0))
        self.assertTrue(ly.should_log(None, d))
        self.assertFalse(ly.should_log(d["score"] - 2, d))


if __name__ == "__main__":
    unittest.main(verbosity=2)
