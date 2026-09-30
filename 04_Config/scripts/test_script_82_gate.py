#!/usr/bin/env python3
"""Tests del gate de edad v7.2.1 en script_82.score_token y del umbral de emisión 56 (unittest, sin red).

Uso: python 04_Config/scripts/test_script_82_gate.py
"""
import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
NOW = 1_790_000_000.0
TEMPORAL = ("Volumen acelerado", "Volumen en aceleración", "Trades acelerados", "Trades en aceleración",
            "Buy pressure >", "Momentum", "Edge temprano", "Volumen activo m5", "Volumen moderado m5",
            "Buy pressure subiendo")


def load(name, filename, workdir):
    prev = os.getcwd()
    os.chdir(workdir)                      # makedirs relativos y _accumulated.json fuera del repo
    try:
        spec = importlib.util.spec_from_file_location(name, HERE / filename)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    finally:
        os.chdir(prev)


def dex(age_min, vol_m5=5000.0, vol_h1=5000.0, buys=80, sells=20, tx_h1_buys=80, tx_h1_sells=20,
        pc_m5=5.0, pc_h1=10.0, mcap=2_000_000.0, liq=150_000.0, vol24=200_000.0):
    return {"priceUsd": 0.01, "liquidityUsd": liq, "volume24hUsd": vol24, "marketCapUsd": mcap, "priceChange24h": 10.0,
            "dexId": "pumpswap", "pairAddress": "pool", "volume_m5": vol_m5, "volume_h1": vol_h1, "volume_h6": vol_h1,
            "txns_m5_buys": buys, "txns_m5_sells": sells, "txns_h1_buys": tx_h1_buys, "txns_h1_sells": tx_h1_sells,
            "priceChange_m5": pc_m5, "priceChange_h1": pc_h1,
            "pairCreatedAt": int((NOW - age_min * 60) * 1000) if age_min is not None else 0}


class GateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.s82 = load("s82_gate", "script_82_final_detection.py", cls.tmp.name)
        cls.prev = os.getcwd()
        os.chdir(cls.tmp.name)

    @classmethod
    def tearDownClass(cls):
        os.chdir(cls.prev)
        cls.tmp.cleanup()

    def score(self, dx, token=None):
        with mock.patch("time.time", return_value=NOW):
            return self.s82.score_token(token or {"score": 50}, dx)

    def temporal(self, reasons):
        return [r for r in reasons if r.startswith(TEMPORAL)]

    def test_version(self):
        self.assertEqual(self.s82.SCORING_VERSION, "7.2.1")
        self.assertEqual(self.s82.ACCEL_GATE_MIN_AGE, 60)

    def test_token_joven_saturado_sin_bonos_temporales(self):
        score, reasons = self.score(dex(age_min=3))           # m5 == h1: ratio 1.0 por construcción
        self.assertEqual(self.temporal(reasons), [])
        self.assertIn("v7.2.1: bonos temporales omitidos (<60 min, ventana h1 incompleta)", reasons)

    def test_token_maduro_recibe_bonos(self):
        score, reasons = self.score(dex(age_min=120, vol_m5=3000, vol_h1=5000, tx_h1_buys=120, tx_h1_sells=40))
        for r in ("Volumen acelerado (5m/1h > 50%)", "Trades acelerados (5m/1h > 50%)", "Buy pressure >60%",
                  "Momentum corto+medio positivo", "Edge temprano (<4h)", "Volumen activo m5 (>$1K)"):
            self.assertIn(r, reasons)
        self.assertNotIn("Edge temprano (<60 min)", reasons)

    def test_mismo_token_joven_vs_maduro_diferencia_de_score(self):
        young, _ = self.score(dex(age_min=10, vol_m5=3000, vol_h1=5000, tx_h1_buys=120, tx_h1_sells=40))
        mature, _ = self.score(dex(age_min=120, vol_m5=3000, vol_h1=5000, tx_h1_buys=120, tx_h1_sells=40))
        self.assertLess(young, mature)

    def test_penalizaciones_siguen_aplicando_a_jovenes(self):
        _, reasons = self.score(dex(age_min=3, buys=10, sells=90))
        self.assertIn("Venta dominante (buy_pressure <40%)", reasons)

    def test_bonos_no_temporales_sin_gate(self):
        _, reasons = self.score(dex(age_min=3))
        for r in ("MCap > $1M", "Volumen alto", "Liquidez alta"):
            self.assertIn(r, reasons)

    def test_edad_desconocida_no_es_madura(self):
        _, reasons = self.score(dex(age_min=None))
        self.assertEqual(self.temporal(reasons), [])

    def test_sin_dexscreener_no_marca_gate(self):
        _, reasons = self.score(None)
        self.assertFalse(any(r.startswith("v7.2.1") for r in reasons))

    def test_limite_exacto_60_min_es_maduro(self):
        _, reasons = self.score(dex(age_min=60.5, vol_m5=3000, vol_h1=5000))
        self.assertIn("Volumen acelerado (5m/1h > 50%)", reasons)


class UmbralEmisionTest(unittest.TestCase):
    def test_umbral_56(self):
        with tempfile.TemporaryDirectory() as tmp:
            os.environ["SHOT_ROOT"] = tmp
            try:
                s97 = load("s97_gate", "script_97_emit_alerts.py", tmp)
            finally:
                os.environ.pop("SHOT_ROOT", None)
        self.assertEqual(s97.EMIT_MIN_SCORE, 56)
        acc = {"A" * 40: {"score": 55}, "B" * 40: {"score": 56}}
        cands, _ = s97.select_candidates(acc, [], max_age_min=None)   # aísla el umbral del filtro R1
        self.assertEqual([m for m, _ in cands], ["B" * 40])


if __name__ == "__main__":
    unittest.main(verbosity=2)
