#!/usr/bin/env python3
"""early_review (Fase 10b): suba de la edad mínima 10 -> 15 si la primaria < 40 % tras 24 h, y cobertura de
PumpPortal. unittest, sin red: velas simuladas.

Uso: python 04_Config/scripts/test_early_review.py
"""
import json
import os
import shutil
import sys
import tempfile
import time
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import early_review as er  # noqa: E402

NOW = time.time()


def ts(epoch):
    return datetime.fromtimestamp(epoch, timezone.utc).strftime("%Y-%m-%d_%H%M%S")


class Source:
    """Velas [ts, o, h, l, c, v] de 15 min: 'hit' sube +25 %, 'miss' cae −35 %."""

    def __init__(self, outcome_by_pool):
        self.outcome = outcome_by_pool

    def get(self, pool, t0):
        o = self.outcome.get(pool)
        if o is None:
            return "http_404", []
        hi, lo = (1.25, 0.99) if o == "hit" else (1.01, 0.65)
        return "ok", [[int(t0) + 900, 1.0, hi, lo, 1.0, 10]]


class Review(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="erev_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        env = mock.patch.dict(os.environ, {"SHOT_ROOT": str(self.root)})   # la bitácora de lib_persist va al tmp
        env.start()
        self.addCleanup(env.stop)
        (self.root / "02_Analisis" / "early" / "alerts").mkdir(parents=True)
        (self.root / "02_Analisis" / "alerts").mkdir(parents=True)

    def add(self, i, hours_ago, gate=10, outcome="hit"):
        mint = f"M{i:03d}pump"
        t = NOW - hours_ago * 3600
        rec = {"mint": mint, "symbol": f"T{i}", "timestamp": ts(t), "initial_price": 1.0, "gate_min": gate,
               "age_min_at_alert": 12.0, "score": 60, "early": True}
        (self.root / "02_Analisis" / "early" / "alerts" / f"{mint}.json").write_text(json.dumps(rec))
        (self.root / "02_Analisis" / "alerts" / f"alert_{mint}_{ts(t)}.json").write_text(
            json.dumps({"dexscreener": {"pairAddress": f"P{i}"}}))
        return f"P{i}", outcome

    def gate(self):
        p = self.root / "02_Analisis" / "early" / "_gate.json"
        return json.loads(p.read_text()) if p.exists() else None

    def test_primaria_baja_tras_24h_sube_a_15(self):
        outcomes = dict(self.add(i, 30 - i, outcome="hit" if i < 2 else "miss") for i in range(6))   # 2/6
        rep = er.run(self.root, Source(outcomes), NOW)
        self.assertEqual(rep["gate"]["decision"], "subir")
        self.assertEqual((rep["gate"]["k_hit"], rep["gate"]["n_resolved"]), (2, 6))
        self.assertEqual(self.gate()["early_min_age_min"], 15)
        # pegajoso: la próxima corrida no lo toca aunque la primaria mejore
        rep2 = er.run(self.root, Source({k: "hit" for k in outcomes}), NOW + 3600)
        self.assertEqual(rep2["gate"]["decision"], "ya_subido")

    def test_primaria_buena_mantiene_10(self):
        outcomes = dict(self.add(i, 30 - i, outcome="hit" if i < 3 else "miss") for i in range(6))   # 3/6 = 50 %
        self.assertEqual(er.run(self.root, Source(outcomes), NOW)["gate"]["decision"], "mantener")
        self.assertIsNone(self.gate())

    def test_antes_de_24h_o_con_pocos_datos_no_decide(self):
        outcomes = dict(self.add(i, 10, outcome="miss") for i in range(6))
        self.assertEqual(er.run(self.root, Source(outcomes), NOW)["gate"]["decision"], "en_prueba")
        shutil.rmtree(self.root / "02_Analisis" / "early" / "alerts")
        (self.root / "02_Analisis" / "early" / "alerts").mkdir()
        outcomes = dict(self.add(i, 30, outcome="miss") for i in range(3))
        self.assertEqual(er.run(self.root, Source(outcomes), NOW)["gate"]["decision"], "sin_datos_suficientes")
        self.assertIsNone(self.gate())

    def test_solo_cuentan_las_de_gate_10(self):
        self.add(1, 30, gate=30)
        self.add(2, 30, gate=None)
        self.add(3, 30, gate=10)
        self.assertEqual([r["mint"] for r in er.trial_rows(self.root)], ["M003pump"])

    def test_h0_fisher_y_veredicto(self):
        self.assertAlmostEqual(er.fisher_one_sided(5, 5, 0, 5), 1 / 252, places=6)
        self.assertEqual(er.fisher_one_sided(0, 5, 5, 5), 1.0)
        rows = [{"h0_group": "info_ge20", "primary": "hit" if i < 15 else "miss"} for i in range(20)] + \
               [{"h0_group": "info_lt20", "primary": "hit" if i < 4 else "miss"} for i in range(20)]
        v = er.evaluate_h0(rows)
        self.assertEqual((v["n_resolved"], v["verdict"]), (40, "H-0 rechazada"))
        same = [dict(r, h0_group="info_lt20" if r["h0_group"] == "info_ge20" else "info_ge20") for r in rows]
        self.assertEqual(er.evaluate_h0(same)["verdict"], "H-0 no rechazada")
        self.assertEqual(er.evaluate_h0(rows[:30])["verdict"], "pendiente")

    def test_h0_toma_las_alertas_con_subtotales(self):
        pool, _ = self.add(7, 30)
        d = self.root / "02_Analisis" / "early" / "alerts"
        rec = json.loads((d / "M007pump.json").read_text())
        rec.update(h0_group="info_ge20", info_score=31.0, struct_score=12.0, pv_score=3.0)
        (d / "M007pump.json").write_text(json.dumps(rec))
        rows = er.h0_rows(self.root)
        self.assertEqual([(r["h0_group"], r["pool"], r["info_score"]) for r in rows], [("info_ge20", pool, 31.0)])
        rep = er.run(self.root, Source({pool: "hit"}), NOW)
        self.assertEqual(rep["h0"]["groups"]["info_ge20"], {"n": 1, "k_hit": 1, "rate": 1.0})

    def test_cobertura_union_de_instancias(self):
        d = self.root / "02_Analisis" / "early"
        h = 3600
        (d / "_watch_a.json").write_text(json.dumps({"instance": "a", "listener_intervals": [
            [NOW - 24 * h, NOW - 12 * h], [NOW - 30 * h, NOW - 25 * h]]}))
        (d / "_watch_b.json").write_text(json.dumps({"instance": "b", "listener_intervals": [
            [NOW - 13 * h, NOW - 6 * h]]}))
        cov = er.coverage(er.load_intervals(self.root), NOW)
        self.assertEqual(cov["by_instance"], {"a": 0.5, "b": round(7 / 24, 4)})
        self.assertEqual(cov["union"], 0.75)               # 24 h → 6 h, solapamiento de 1 h
        self.assertEqual(er.union_seconds([], 0, 10), 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
