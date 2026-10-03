#!/usr/bin/env python3
"""Tests del método científico automatizado (patrón #2): lib_scientific_method. unittest, sin red.

Uso: python 04_Config/scripts/test_lib_scientific_method.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import early_review  # noqa: E402
import lib_scientific_method as sm  # noqa: E402

NOW = 1791000000
RATE = {"test": "rate_vs_baseline", "min_n": 10, "baseline": 0.30}
RATE_ACC = {"all": [["wilson_lo", ">", "$baseline"]]}
RATE_REJ = {"all": [["wilson_hi", "<", "$baseline"]]}


def rows_h0(k_ge, n_ge, k_lt, n_lt):
    def grp(name, k, n):
        return [{"h0_group": name, "primary": "hit" if i < k else "miss"} for i in range(n)]
    return grp("info_ge20", k_ge, n_ge) + grp("info_lt20", k_lt, n_lt) + [{"h0_group": "info_ge20",
                                                                           "primary": "sin_datos"}]


def rows_rate(k, n):
    return [{"primary": "hit" if i < k else "miss"} for i in range(n)]


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="sm_"))
        self.addCleanup(shutil.rmtree, self.root, True)

    def lines(self):
        return [json.loads(x) for x in sm.registry_path(self.root).read_text(encoding="utf-8").splitlines()]

    def reg(self, hid="H-t1", **kw):
        args = dict(statement="la tasa supera 30 %", prediction=dict(RATE), acceptance=RATE_ACC,
                    rejection=RATE_REJ, root=self.root, now=NOW)
        args.update(kw)
        return sm.register_hypothesis(hid, **args)


class Registro(Base):
    def test_preregistro_persiste_y_es_idempotente(self):
        line = self.reg()
        self.assertEqual((line["event"], line["id"], line["ts"]), ("register", "H-t1", NOW))
        self.assertEqual(self.reg()["hash"], line["hash"])            # mismo contenido: no escribe otra línea
        self.assertEqual(len(self.lines()), 1)
        self.assertEqual(sm.get_hypothesis("H-t1", self.root)["registration"]["statement"], "la tasa supera 30 %")

    def test_preregistro_inmutable_y_validaciones(self):
        self.reg()
        with self.assertRaises(ValueError):                             # variante con el mismo id
            self.reg(prediction=dict(RATE, baseline=0.25))
        with self.assertRaises(ValueError):
            self.reg(hid="hipotesis 1")
        with self.assertRaises(ValueError):
            self.reg(hid="H-t2", prediction={"test": "llm_judge"})
        with self.assertRaises(ValueError):
            self.reg(hid="H-t3", acceptance={"all": [["p_value", "~", 1]]})
        self.assertEqual(len(self.lines()), 1)


class Evaluacion(Base):
    def test_h0_migrada_reproduce_early_review(self):
        sm.migrate_h0(root=self.root, now=NOW)
        reg = sm.get_hypothesis("H-0", self.root)["registration"]
        self.assertEqual((reg["registered_at"], reg["prediction"]["min_n"], reg["prediction"]["alpha"]),
                         ("2026-10-02", early_review.H0_MIN_N, early_review.H0_ALPHA))
        for case in ((18, 25, 5, 20), (10, 22, 9, 20), (3, 10, 2, 10)):
            rows = rows_h0(*case)
            old = early_review.evaluate_h0(rows)
            new = sm.evaluate_hypothesis("H-0", rows, root=self.root, now=NOW, persist=False)
            self.assertEqual(new["label"], old["verdict"], case)
            self.assertEqual(new["result"]["n"], old["n_resolved"])
            self.assertEqual(new["result"]["groups"], old["groups"])
            if "p_value" in old:
                self.assertEqual(new["result"]["p_value"], old["p_value"])
        self.assertEqual(sm.fisher_one_sided(7, 12, 2, 11), early_review.fisher_one_sided(7, 12, 2, 11))

    def test_tasa_contra_baseline_tres_veredictos(self):
        self.reg()
        v = {k: sm.evaluate_hypothesis("H-t1", rows_rate(k, 40), root=self.root, now=NOW, persist=False)["verdict"]
             for k in (24, 4, 13)}
        self.assertEqual(v, {24: "aceptada", 4: "rechazada", 13: "inconclusa"})
        self.assertEqual(sm.evaluate_hypothesis("H-t1", rows_rate(9, 9), root=self.root, persist=False)["verdict"],
                         "pendiente")                                    # n < min_n

    def test_mediana_con_ic_por_estadisticos_de_orden(self):
        med, ci = sm.median_ci([5, 1, 4, 2, 3])
        self.assertEqual((med, ci), (3, [1, 5]))                         # n=5: P(B<=0)=1/32 <= 0,05
        self.assertEqual(sm.median_ci([7]), (7, None))
        self.reg(hid="H-b1", statement="rendimiento 24 h del listing > 0",
                 prediction={"test": "median_ci", "min_n": 5, "value_field": "ret_24h"},
                 acceptance={"all": [["ci_lo", ">", 0]]}, rejection={"all": [["ci_hi", "<", 0]]})
        good = [{"ret_24h": x} for x in (0.05, 0.12, 0.3, 0.08, 0.2, 0.15, 0.02)]
        mixed = [{"ret_24h": x} for x in (-0.2, 0.1, -0.05, 0.3, 0.0, -0.1, 0.2)]
        self.assertEqual(sm.evaluate_hypothesis("H-b1", good, root=self.root, persist=False)["verdict"], "aceptada")
        self.assertEqual(sm.evaluate_hypothesis("H-b1", mixed, root=self.root, persist=False)["verdict"],
                         "inconclusa")

    def test_evaluacion_append_only_con_hash_de_datos(self):
        first = self.reg()
        rows = rows_rate(24, 40)
        out = sm.evaluate_hypothesis("H-t1", rows, root=self.root, now=NOW + 60)
        sm.evaluate_hypothesis("H-t1", rows_rate(4, 40), root=self.root, now=NOW + 120)
        lines = self.lines()
        self.assertEqual([x["event"] for x in lines], ["register", "evaluate", "evaluate"])
        self.assertEqual(lines[0], first)                                # la registración no se reescribe
        self.assertEqual((lines[1]["data_hash"], lines[1]["hash"]), (sm.sha(rows), first["hash"]))
        self.assertEqual(out["verdict"], "aceptada")
        self.assertEqual([e["verdict"] for e in sm.get_hypothesis("H-t1", self.root)["evaluations"]],
                         ["aceptada", "rechazada"])
        with self.assertRaises(KeyError):
            sm.evaluate_hypothesis("H-nada", rows, root=self.root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
