#!/usr/bin/env python3
"""Grupo i en el flujo Solana (Fase 8): un par de más de 180 días se registra como grupo i y no se emite como memecoin.

Caso testigo: arc (AI Rig Complex), alerta real del 01/10/2026 08:40 UTC con score v7.2.1 = 72 y par de 621,7 días.
Uso: python 04_Config/scripts/test_script_82_group_i.py
"""
import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
NOW = datetime(2026, 10, 1, 8, 40, 22, tzinfo=timezone.utc)
ARC = "61V8vBaqAGMpgDQi4JcAwo1dmBGHsyhzodcPqnEVpump"


def load(name, file, root):
    os.environ["SHOT_ROOT"] = root
    sys.path.insert(0, str(SCRIPTS))
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def arc_entry(created_ms=1737132291000, score=72):
    return {"source": "trending", "token": {"mint": ARC, "symbol": "arc", "name": "AI Rig Complex", "score": 76.07},
            "dexscreener": {"priceUsd": 0.07169, "liquidityUsd": 10333551.81, "volume24hUsd": 6955.45,
                            "marketCapUsd": 71693009.0, "priceChange24h": 0.6, "pairCreatedAt": created_ms},
            "score": score, "reasons": ["MCap > $1M", "Buy pressure >60%"],
            "detected_at": NOW.isoformat(timespec="seconds"), "scoring_version": "7.2.1"}


class GrupoITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="gi_")
        try:
            cls.s82 = load("s82_gi", "script_82_final_detection.py", cls.tmp)
        except ModuleNotFoundError as e:
            raise unittest.SkipTest(str(e))
        cls.s97 = load("s97_gi", "script_97_emit_alerts.py", cls.tmp)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_arc_pasa_a_grupo_i_con_su_propio_score(self):
        e = arc_entry()
        self.assertTrue(self.s82.apply_group_i(e, NOW.timestamp() * 1000))
        self.assertEqual(e["group"], "i")
        self.assertEqual((e["memecoin_score"], e["score"]), (72, 0))           # doc 27 §4.10: cobertura 0,2, score 0
        self.assertEqual(e["group_confidence"], 0.2)
        self.assertAlmostEqual(e["pair_age_days"], 621.7, delta=0.1)
        self.assertTrue(e["reasons"][0].startswith("Grupo i: par de 622 días"))
        self.assertIn("Descuento por edad: −10 (par > 1 año)", e["reasons"])
        self.assertEqual(e["memecoin_reasons"], ["MCap > $1M", "Buy pressure >60%"])

    def test_par_joven_o_sin_fecha_no_cambia(self):
        young = arc_entry(created_ms=int((NOW - timedelta(days=179)).timestamp() * 1000))
        self.assertFalse(self.s82.apply_group_i(young, NOW.timestamp() * 1000))
        self.assertEqual((young["score"], young.get("group")), (72, None))
        undated = arc_entry(created_ms=None)
        self.assertFalse(self.s82.apply_group_i(undated, NOW.timestamp() * 1000))
        self.assertFalse(self.s82.apply_group_i({"score": 80, "dexscreener": None}))

    def test_script_97_registra_y_no_emite_el_grupo_i(self):
        e = arc_entry()
        self.s82.apply_group_i(e, NOW.timestamp() * 1000)
        e["score"] = 90                                                        # aunque el score del grupo superara 56
        cands, stats = self.s97.select_candidates({ARC: e}, [], now=NOW.timestamp())
        self.assertEqual(cands, [])
        self.assertEqual(stats["group_i_registered"], 1)
        normal = arc_entry(created_ms=int((NOW - timedelta(hours=3)).timestamp() * 1000))
        cands, _ = self.s97.select_candidates({ARC: normal}, [], now=NOW.timestamp())
        self.assertEqual([m for m, _ in cands], [ARC])                         # el flujo memecoin sigue igual

    def test_score_token_no_cambia(self):
        tok, dx = arc_entry()["token"], arc_entry()["dexscreener"]
        score, reasons = self.s82.score_token(tok, dx)
        self.assertIn("Par >24h, no nativo pump.fun", reasons)                 # v7.2.1 intacto (calibración)


if __name__ == "__main__":
    unittest.main(verbosity=2)
