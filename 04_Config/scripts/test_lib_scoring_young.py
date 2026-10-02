#!/usr/bin/env python3
"""lib_scoring_young (Fase 12 MVP, D-014-R): score de tokens < 60 min. unittest, sin red, datos sintéticos.

Uso: python 04_Config/scripts/test_lib_scoring_young.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_early_signals as es  # noqa: E402
import lib_scoring_young as ly  # noqa: E402

NOW = 1_790_900_000.0


def token(age_min=15, liq=60_000, initial_buy=30_000_000, change24=150.0, **dx):
    d = {"pairCreatedAt": int((NOW - age_min * 60) * 1000), "liquidityUsd": liq, "priceChange24h": change24,
         "volume_m5": 6000, "volume_h1": 15000, "txns_m5_buys": 30, "txns_m5_sells": 8,
         "txns_h1_buys": 100, "txns_h1_sells": 100, "priceChange_m5": 2.0}
    d.update(dx)
    return {"token": {"mint": "M", "initialBuy": initial_buy}, "dexscreener": d}


def flow_signals(t, liq_series=((NOW - 600, 40_000), (NOW, 60_000))):
    return es.dex_signals(t["dexscreener"], list(liq_series))


class Young(unittest.TestCase):
    def test_tres_senales_con_liquidez_dispara(self):
        t = token()
        score, reasons = ly.score_young(t, flow_signals(t), NOW)
        self.assertGreaterEqual(score, ly.YOUNG_THRESHOLD)
        self.assertTrue(ly.fires(score))
        self.assertTrue(any("señales activas" in r for r in reasons))

    def test_fuera_de_alcance(self):
        t = token(age_min=75)
        self.assertEqual(ly.score_young(t, flow_signals(t), NOW)[0], None)
        t = token()
        t["dexscreener"]["pairCreatedAt"] = 0
        self.assertIsNone(ly.score_young(t, flow_signals(t), NOW)[0])

    def test_liquidez_baja_o_curva_de_bonding(self):
        t = token(liq=0)
        score, reasons = ly.score_young(t, flow_signals(t), NOW)
        self.assertEqual(score, 0)
        self.assertTrue(any("FILTRO: liquidez" in r for r in reasons))
        self.assertTrue(any("sin filtros sería" in r for r in reasons))

    def test_kill_switches(self):
        t = token(age_min=3, change24=25_000)
        self.assertIn("kill switch de script_82", ly.kill_switches(t, None, 3)[0])
        t = token()
        self.assertEqual(ly.kill_switches(t, {"holders": 300, "top10_pct": 30}, 15), [])
        bad = ly.kill_switches(t, {"mint_authority": "X", "freeze_authority": "Y", "holders": 20, "top10_pct": 70,
                                   "creator_pct": 25}, 15)
        self.assertEqual(len(bad), 5)
        dev = ly.kill_switches(token(initial_buy=200_000_000), None, 15)
        self.assertIn("compra inicial del creador 20.0 %", dev[0])
        score, _ = ly.score_young(token(initial_buy=200_000_000), flow_signals(token()), NOW)
        self.assertEqual(score, 0)

    def test_solo_cuentan_las_elegibles(self):
        t = token()
        extra = [es.fear_greed_extreme(0), es.orderbook_imbalance([[100, 50]], [[100.5, 1]]),
                 es.social_velocity({"surprise_nats": 9})]
        self.assertEqual(ly.active_signals(extra), {})
        s_only, _ = ly.score_young(t, extra, NOW)
        self.assertEqual(s_only, 0)               # 0 señales elegibles → 0 (pasa filtros, no dispara)
        self.assertFalse(ly.fires(s_only))

    def test_variantes_para_sombra(self):
        t = token()
        v = ly.variants(flow_signals(t))
        self.assertEqual(set(v), {"A_ge3_active", "B_ge3_strong", "C_points_ge4"})
        self.assertTrue(v["A_ge3_active"])
        weak = [{"name": n, "s": 0.1, "points": 0.2} for n in ly.ELIGIBLE[:3]]
        self.assertEqual(ly.variants(weak), {"A_ge3_active": True, "B_ge3_strong": False, "C_points_ge4": False})

    def test_determinista(self):
        t = token()
        self.assertEqual(ly.score_young(t, flow_signals(t), NOW), ly.score_young(t, flow_signals(t), NOW))


if __name__ == "__main__":
    unittest.main(verbosity=2)
