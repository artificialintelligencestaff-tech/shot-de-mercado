#!/usr/bin/env python3
"""lib_early_signals (Fase 10, T2): señales anticipatorias con datos sintéticos. unittest, sin red.

Uso: python 04_Config/scripts/test_lib_early_signals.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_early_signals as es  # noqa: E402
import lib_scoring_multichain as lsm  # noqa: E402


def dx(**kw):
    base = {"volume_m5": 1000.0, "volume_h1": 12000.0, "txns_m5_buys": 10, "txns_m5_sells": 10,
            "txns_h1_buys": 100, "txns_h1_sells": 100, "priceChange_m5": 0.0}
    base.update(kw)
    return base


class Flujo(unittest.TestCase):
    def test_volumen_plano_no_suma_y_acelerado_suma_completo(self):
        self.assertEqual(es.volume_acceleration(1000, 12000)["s"], 0.0)          # ×1
        self.assertAlmostEqual(es.volume_acceleration(4000, 15000)["s"], 0.68)   # tasa 4000 vs 1250 = ×3.2
        full = es.volume_acceleration(6000, 15000)                              # ×4.8
        self.assertEqual(full["s"], 1.0)
        self.assertEqual(full["points"], es.POINTS["volume_acceleration"])

    def test_par_recien_nacido_sin_hora_previa_no_tiene_dato(self):
        self.assertIsNone(es.volume_acceleration(5000, 5000))                   # la hora = los 5 min
        self.assertIsNone(es.volume_acceleration(None, 100))

    def test_presion_compradora(self):
        self.assertIsNone(es.buy_pressure_shift(3, 2, 50, 50))                   # < 10 trades en 5 min
        s = es.buy_pressure_shift(18, 6, 100, 100)                               # 75 % vs 50 %
        self.assertEqual(s["s"], 1.0)
        self.assertEqual(es.buy_pressure_shift(10, 10, 100, 100)["s"], 0.0)

    def test_acumulacion_con_precio_quieto_es_la_firma_previa(self):
        quiet = es.quiet_accumulation(1.2, 3000, 14000, 30, 10)                  # vol ×2.6, compras 75 %, m5 +1.2 %
        self.assertGreater(quiet["s"], 0.25)
        moved = es.quiet_accumulation(40.0, 3000, 14000, 30, 10)                 # el precio ya se movió
        self.assertEqual(moved["s"], 0.0)

    def test_liquidez_entrante(self):
        series = [(0, 10000), (300, 11000), (600, 13000)]
        s = es.liquidity_inflow(series)
        self.assertAlmostEqual(s["s"], 1.0)
        self.assertIsNone(es.liquidity_inflow([(0, 10000)]))
        self.assertEqual(es.liquidity_inflow([(0, 10000), (120, 9000)])["s"], 0.0)   # sale liquidez: 0, no resta


class Libro(unittest.TestCase):
    def test_desequilibrio_comprador_suma(self):
        bids = [{"px": "100", "sz": "50"}, {"px": "99.5", "sz": "40"}, {"px": "90", "sz": "999"}]   # 90 fuera de ±2 %
        asks = [{"px": "100.5", "sz": "10"}, {"px": "101", "sz": "5"}]
        s = es.orderbook_imbalance(bids, asks)
        self.assertGreater(s["imbalance"], 0.5)
        self.assertEqual(s["s"], 1.0)

    def test_formato_dydx_y_lado_vendedor_no_resta(self):
        bids = [{"price": "10", "size": "1"}]
        asks = [{"price": "10.01", "size": "50"}]
        s = es.orderbook_imbalance(bids, asks)
        self.assertLess(s["imbalance"], 0)
        self.assertEqual(s["s"], 0.0)

    def test_libro_cruzado_o_vacio(self):
        self.assertIsNone(es.orderbook_imbalance([], [[1, 1]]))
        self.assertIsNone(es.orderbook_imbalance([[10, 1]], [[9, 1]]))


class OnChainSocialDerivados(unittest.TestCase):
    def test_holders_creciendo_y_concentracion(self):
        s = es.holder_accumulation([(0, 100, 30.0), (600, 150, 28.0)])          # +5/min
        self.assertEqual(s["s"], 1.0)
        half = es.holder_accumulation([(0, 100, 30.0), (600, 150, 40.0)])       # top10 sube: la mitad
        self.assertEqual(half["s"], 0.5)
        self.assertIsNone(es.holder_accumulation([(0, 100, 30.0), (30, 120, 30.0)]))   # < 1 min

    def test_snapshot_de_rugcheck(self):
        rep = {"totalHolders": 812, "topHolders": [{"pct": 12.5, "insider": True}, {"pct": 7.5}] + [{"pct": 1}] * 12,
               "graphInsidersDetected": 3}
        snap = es.rugcheck_snapshot(rep, 1000)
        self.assertEqual((snap["holders"], snap["top10_pct"], snap["insiders_top"]), (812, 28.0, 1))
        self.assertIsNone(es.rugcheck_snapshot({}, 1))

    def test_velocidad_social(self):
        quiet = es.social_velocity({"m_1h": 0, "m_prev_1h": 0, "surprise_nats": 0, "seff_1h": 0})
        self.assertEqual(quiet["s"], 0.0)
        burst = es.social_velocity({"m_1h": 6, "m_prev_1h": 1, "surprise_nats": 7.5, "seff_1h": 3})
        self.assertEqual(burst["s"], 1.0)
        trend = es.social_velocity({"m_1h": 0}, {"rank": 4})
        self.assertGreaterEqual(trend["s"], 0.6)
        self.assertIsNone(es.social_velocity(None))

    def test_funding_squeeze(self):
        hist = [0.0001, 0.00012, 0.00009, 0.00011, 0.0001, 0.0001, 0.00011, 0.00009]
        s = es.funding_squeeze(-0.0002, hist, oi_change=0.05)
        self.assertEqual(s["s"], 1.0)
        self.assertEqual(es.funding_squeeze(-0.0002, hist, oi_change=-0.1)["s"], 0.0)   # OI cae: no hay setup
        self.assertIsNone(es.funding_squeeze(0.0, hist[:3]))

    def test_fear_greed(self):
        self.assertEqual(es.fear_greed_extreme(10)["s"], 0.5)
        self.assertEqual(es.fear_greed_extreme(74)["s"], 0.0)


class Combinacion(unittest.TestCase):
    def test_bono_con_tope_y_solo_suma(self):
        sigs = [es.volume_acceleration(6000, 15000), es.buy_pressure_shift(18, 6, 100, 100),
                es.liquidity_inflow([(0, 1), (600, 2)]), es.fear_greed_extreme(0),
                es.social_velocity({"surprise_nats": 9}), None]
        out = es.combine(sigs)
        self.assertEqual(out["bonus"], es.BONUS_CAP)
        self.assertGreater(out["raw"], es.BONUS_CAP)
        self.assertEqual(es.apply_bonus(55, out), 63)
        self.assertEqual(es.apply_bonus(98, out), 100)
        self.assertIsNone(es.apply_bonus(None, out))

    def test_sin_senales_bono_cero(self):
        out = es.combine(es.dex_signals(dx()))
        self.assertEqual((out["bonus"], out["active"]), (0, []))
        self.assertEqual(es.apply_bonus(50, out), 50)

    def test_dex_signals_par_con_firma_previa(self):
        out = es.combine(es.dex_signals(dx(volume_m5=4000, volume_h1=15000, txns_m5_buys=30, txns_m5_sells=8,
                                           priceChange_m5=2.0), [(0, 10000), (600, 12000)]))
        self.assertIn("quiet_accumulation", out["active"])
        self.assertGreaterEqual(out["bonus"], 6)

    def test_multichain_aplica_el_bono_sin_restar(self):
        self.assertEqual(lsm.apply_early(60, ["r"], {"bonus": 3, "reasons": ["x"], "version": es.VERSION})[0], 63)
        self.assertEqual(lsm.apply_early(60, ["r"], {"bonus": -5})[0], 60)
        self.assertEqual(lsm.apply_early(None, [], {"bonus": 3})[0], None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
