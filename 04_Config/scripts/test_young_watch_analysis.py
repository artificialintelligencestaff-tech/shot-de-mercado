#!/usr/bin/env python3
"""young_watch_analysis (D-014-R, entregable 3): cobertura sobre snapshots sintéticos. unittest, sin red ni git.

Uso: python 04_Config/scripts/test_young_watch_analysis.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import young_watch_analysis as ya  # noqa: E402

T0 = 1_790_900_000


def snap(at, top, watch=None, liq=None):
    return ("x", {"updated_at": at, "instance": "a", "top": top, "watch": watch or {},
                  "state": {"liquidity": liq or {}}})


class Analisis(unittest.TestCase):
    def setUp(self):
        top1 = [{"mint": "A", "base": 35, "age_min": 10, "active": ["volume_acceleration", "buy_pressure_shift",
                                                                   "liquidity_inflow"]},
                {"mint": "B", "base": 60, "age_min": 40, "active": ["volume_acceleration"]},
                {"mint": "C", "base": 12, "age_min": 5, "active": []}]
        top2 = [{"mint": "A", "base": 45, "age_min": 12, "active": ["volume_acceleration"]},
                {"mint": "A", "base": 45, "age_min": 12, "active": ["volume_acceleration"]}]   # duplicada
        since = {"A": {"since": "2026-10-01T22:00:00+00:00"}, "C": {"since": "2026-10-01T22:00:00+00:00"}}
        t = ya.parse_iso("2026-10-01T22:00:00+00:00")
        liq = {"A": [[t + 60, 0.0], [t + 120, 25_000.0]], "C": [[t + 60, 0.0], [t + 4000, 50_000.0]]}
        self.rows, self.liq, self.since = ya.collect([snap("2026-10-01T22:10:00+00:00", top1, since, liq),
                                                      snap("2026-10-01T22:12:00+00:00", top2 + top2)])

    def test_dedup_y_distribucion(self):
        self.assertEqual(len(self.rows), 4)
        d = ya.score_distribution(self.rows)
        self.assertEqual((d["n_mints"], d["max"], d["ge_56"]), (2, 45, 0))      # B tiene 40 min: fuera de < 30
        self.assertEqual(d["buckets"], {"40-49": 1, "10-19": 1})

    def test_cobertura_de_senales(self):
        c = ya.signal_coverage(self.rows)
        self.assertEqual((c["rows_ge3"], c["mints_ge3"], c["mints_ge3_lt30min"]), (1, 1, 1))
        self.assertEqual(c["by_signal"]["volume_acceleration"], 3)

    def test_liquidez_por_edad(self):
        out = ya.liquidity_by_age(self.liq, self.since)
        self.assertEqual((out["n_mints"], out["liq_gt_min"], out["liq_zero_always"]), (2, 1, 1))  # C cruza a 66 min
        self.assertEqual(out["first_cross_age_median_min"], 2.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
