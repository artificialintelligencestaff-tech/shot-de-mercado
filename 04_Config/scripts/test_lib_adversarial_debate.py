#!/usr/bin/env python3
"""Tests del debate adversario (patrón #8): lib_adversarial_debate. unittest, sin red.

Uso: python 04_Config/scripts/test_lib_adversarial_debate.py
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import lib_adversarial_debate as deb  # noqa: E402
import lib_scientific_method as sm  # noqa: E402

T0 = 1791000000                    # 2026-10-03 (semana ISO 40)
WEEK = 7 * 86400
TWO = {"test": "fisher_one_sided", "min_n": 40, "group_field": "sig", "group_a": "si", "group_b": "no",
       "outcome_field": "primary"}


def cell(chain, week, group, hits, total):
    return [{"chain": chain, "t0": T0 + week * WEEK, "sig": group, "primary": "hit" if i < hits else "miss"}
            for i in range(total)]


def grid(spec):
    """spec: {(chain, week): (hits_si, n_si, hits_no, n_no)}"""
    rows = []
    for (chain, week), (ks, ns, kn, nn) in sorted(spec.items()):
        rows += cell(chain, week, "si", ks, ns) + cell(chain, week, "no", kn, nn)
    return rows


STRONG = {(c, w): (7, 10, 3, 10) for c in ("solana", "base") for w in (0, 1)}
FLAT = {(c, w): (4, 10, 4, 10) for c in ("solana", "base") for w in (0, 1)}


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="debate_"))
        self.addCleanup(shutil.rmtree, self.root, True)
        sm.register_hypothesis("H-a1", "la señal sí supera a la señal no", TWO,
                               {"all": [["p_value", "<", 0.10], ["diff_pp", ">=", 10]]},
                               {"all": [["p_value", ">=", 0.10]]}, group="a", root=self.root, now=T0)

    def rules(self, out, role):
        return {a["rule"] for a in out[role]}


class Debate(Base):
    def test_efecto_robusto_queda_sostenido(self):
        out = deb.run_debate("H-a1", {"rows": grid(STRONG), "placebo_rows": grid(FLAT)}, self.root)
        self.assertEqual(out["verdict"], "sostenida")
        self.assertEqual(out["evaluation"]["verdict"], "aceptada")
        self.assertTrue({"A1_significancia", "A2_efecto", "A4_consistencia", "A5_placebo_nulo", "A6_permutacion",
                         "A7_estabilidad"} <= self.rules(out, "advocate"))
        self.assertFalse(any(a["fatal"] for a in out["challenger"]))
        self.assertGreaterEqual(out["confidence"], 0.8)
        self.assertEqual(out["reasons"][0], "el efecto es estadísticamente significativo")

    def test_submuestra_que_invierte_el_signo_refuta_aunque_el_total_pase(self):
        spec = {("solana", w): (18, 20, 4, 20) for w in (0, 1)}
        spec.update({("base", w): (3, 10, 5, 10) for w in (0, 1)})
        out = deb.run_debate("H-a1", {"rows": grid(spec), "placebo_rows": grid(FLAT)}, self.root)
        self.assertEqual(out["evaluation"]["verdict"], "aceptada")       # la prueba sola la aceptaría
        self.assertEqual(out["verdict"], "refutada")
        inv = [a for a in out["challenger"] if a["rule"] == "C4_inversion"]
        self.assertTrue(inv and inv[0]["fatal"])
        self.assertIn("chain=base", inv[0]["evidence"]["subsamples"])
        self.assertEqual(out["reasons"], ["una submuestra invierte el signo"])

    def test_placebo_que_rinde_igual_refuta(self):
        rows = grid(STRONG)
        out = deb.run_debate("H-a1", {"rows": rows, "placebo_rows": rows}, self.root)
        self.assertEqual(out["verdict"], "refutada")
        self.assertIn("C5_placebo", {a["rule"] for a in out["challenger"] if a["fatal"]})
        sin_placebo = deb.run_debate("H-a1", {"rows": rows}, self.root)
        self.assertIn("C10_sin_placebo", self.rules(sin_placebo, "challenger"))

    def test_muestra_insuficiente_no_debate(self):
        out = deb.run_debate("H-a1", {"rows": grid({("solana", 0): (7, 10, 3, 10)})}, self.root)
        self.assertEqual((out["verdict"], out["evaluation"]["verdict"]), ("insuficiente", "pendiente"))
        self.assertEqual([a["rule"] for a in out["challenger"]], ["C1_muestra"])
        with self.assertRaises(KeyError):
            deb.run_debate("H-zz", {"rows": []}, self.root)

    def test_tasa_inestable_en_el_tiempo_y_determinismo(self):
        sm.register_hypothesis("H-r1", "la tasa supera 30 %", {"test": "rate_vs_baseline", "min_n": 20,
                               "baseline": 0.30}, {"all": [["wilson_lo", ">", "$baseline"]]},
                               {"all": [["wilson_hi", "<", "$baseline"]]}, root=self.root, now=T0)
        rows = [{"t0": T0, "primary": "hit"} for _ in range(20)] + \
               [{"t0": T0 + WEEK, "primary": "hit" if i < 2 else "miss"} for i in range(20)]
        out = deb.run_debate("H-r1", {"rows": rows}, self.root)
        self.assertEqual(out["evaluation"]["verdict"], "aceptada")
        self.assertEqual(out["verdict"], "refutada")
        self.assertTrue({"C7_inestable", "C4_inversion"} <= self.rules(out, "challenger"))
        self.assertNotIn("permutation_p", out["features"])               # solo aplica a dos grupos
        again = deb.run_debate("H-r1", {"rows": rows}, self.root)
        self.assertEqual(json.dumps(out, sort_keys=True), json.dumps(again, sort_keys=True))
        two = deb.run_debate("H-a1", {"rows": grid(STRONG)}, self.root)
        self.assertEqual(two["features"]["permutation_p"],
                         deb.run_debate("H-a1", {"rows": grid(STRONG)}, self.root)["features"]["permutation_p"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
