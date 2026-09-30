#!/usr/bin/env python3
"""Tests de la métrica dual de calibrate_threshold_v72 (unittest, sin red).

Uso: python 04_Config/scripts/test_calibrate_dual.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import calibrate_threshold_v72 as cal  # noqa: E402

T0 = 1_790_000_000.0
DONE = T0 + cal.HORIZON_S + 60        # 48 h cumplidas
EARLY = T0 + 3600                      # 1 h después


def candle(i, o, h, l, c):
    return [T0 + (i + 1) * cal.CANDLE_S, o, h, l, c, 1.0]


class TestDefiniciones(unittest.TestCase):
    def test_primary_directivas(self):
        self.assertTrue(cal.event_primary([1.0, 1.1, 1.25, 0.5], 1.0))     # +20% antes que −30%
        self.assertFalse(cal.event_primary([1.0, 0.65, 1.5], 1.0))          # −30% primero
        self.assertFalse(cal.event_primary([1.0, 1.1, 0.9], 1.0))           # ninguna barrera
        self.assertFalse(cal.event_primary([], 1.0))

    def test_secondary_directivas(self):
        self.assertTrue(cal.event_secondary([0.5, 1.21], 1.0))
        self.assertFalse(cal.event_secondary([2.0, 1.19], 1.0))             # el máximo no cuenta
        self.assertFalse(cal.event_secondary([], 1.0))


class TestVelas(unittest.TestCase):
    def test_orden_conservador_en_vela_ambigua(self):
        out = cal.evaluate_outcome([candle(0, 1.0, 1.5, 0.6, 1.2)], 1.0, T0, DONE)
        self.assertEqual(out["primary"], "miss")                              # low antes que high
        self.assertEqual(out["ambiguous_candles"], 1)

    def test_hit_limpio_y_rug_posterior(self):
        out = cal.evaluate_outcome([candle(0, 1.0, 1.3, 0.95, 1.2), candle(1, 1.2, 1.2, 0.01, 0.02)], 1.0, T0, DONE)
        self.assertEqual((out["primary"], out["secondary"]), ("hit", "miss"))
        self.assertLessEqual(out["min_ret"], cal.RUG_MOVE)

    def test_censura(self):
        quiet = [candle(0, 1.0, 1.1, 0.9, 1.05)]
        out = cal.evaluate_outcome(quiet, 1.0, T0, EARLY)
        self.assertEqual((out["primary"], out["secondary"]), ("pending", "pending"))
        out = cal.evaluate_outcome([candle(0, 1.0, 1.25, 0.95, 1.2)], 1.0, T0, EARLY)
        self.assertEqual((out["primary"], out["secondary"]), ("hit", "pending"))   # primaria decidida antes

    def test_sin_velas(self):
        self.assertEqual(cal.evaluate_outcome([], 1.0, T0, DONE)["primary"], "miss")
        self.assertEqual(cal.evaluate_outcome([], 1.0, T0, EARLY)["primary"], "pending")


class TestEstadistica(unittest.TestCase):
    def test_wilson_en_rango(self):
        self.assertEqual(cal.wilson(0, 0), None)
        lo, hi = cal.wilson(3, 78)
        self.assertTrue(0 <= lo < 3 / 78 < hi <= 1)
        self.assertEqual(cal.wilson(0, 10)[0], 0.0)

    def test_precision_block_ignora_pendientes(self):
        rows = [{"primary": "hit"}, {"primary": "miss"}, {"primary": "pending"}]
        b = cal.precision_block(rows, "primary")
        self.assertEqual((b["k_hit"], b["n_resolved"], b["pending"], b["rate"]), (1, 2, 1, 0.5))


if __name__ == "__main__":
    unittest.main(verbosity=2)
